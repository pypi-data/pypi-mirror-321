import importlib.resources
from abc import ABC, abstractmethod
import fnmatch
from importlib.abc import Traversable
import json
import logging
import os
from pathlib import Path
import random
import re
import secrets
import shutil
import stat
import string
import subprocess
import tarfile
import time

import bsapi
import patoolib

from bsscripts.config import AssignmentConfig, Config
from bsscripts.distribute import AssignmentInfo, Division, ProgressReporter

logger = logging.getLogger(__name__)


def get_all_files(path: Path) -> list[Path]:
    result = []

    for dir_ in path.iterdir():
        if dir_.is_dir():
            result.extend(get_all_files(dir_))
        elif dir_.is_file():
            result.append(dir_)

    return result


def filter_files(files: list[Path], extensions: list[str]) -> list[Path]:
    return [file for file in files if file.suffix.lower().removeprefix('.') in extensions]


class SubmissionsPass(ABC):
    def __init__(self, progress_reporter: ProgressReporter = None):
        self.progress_reporter = progress_reporter

    @abstractmethod
    def process_submission(self, submission_path: Path):
        pass

    def execute(self, path: Path):
        dirs = [dir_ for dir_ in path.iterdir() if dir_.is_dir()]

        for idx, dir_ in enumerate(dirs):
            if self.progress_reporter:
                self.progress_reporter.start(idx + 1, len(dirs), dir_.name)
            self.process_submission(dir_)
        if self.progress_reporter:
            self.progress_reporter.finish(len(dirs))


class GraderPass(ABC):
    def __init__(self, progress_reporter: ProgressReporter = None):
        self.progress_reporter = progress_reporter

    @abstractmethod
    def process_grader(self, grader_path: Path):
        pass

    def execute(self, path: Path):
        dirs = [dir_ for dir_ in path.iterdir() if dir_.is_dir()]

        for idx, dir_ in enumerate(dirs):
            if self.progress_reporter:
                self.progress_reporter.start(idx + 1, len(dirs), dir_.name)
            self.process_grader(dir_)
        if self.progress_reporter:
            self.progress_reporter.finish(len(dirs))


class InjectGraderFilesPass(GraderPass):
    def __init__(self, config: AssignmentConfig, inject_path: Path, progress_reporter: ProgressReporter = None):
        super().__init__(progress_reporter)
        self.inject_path = inject_path / config.identifier / 'grader'

    def process_grader(self, grader_path: Path):
        # TODO: some check to prevent overwriting student files? Perhaps rename them in such cases?
        shutil.copytree(self.inject_path, grader_path, dirs_exist_ok=True)

    def execute(self, path: Path):
        if self.inject_path.exists():
            super().execute(path)


class AddGraderFilesPass(GraderPass):
    def __init__(self, grader_data_path: Traversable, course_path: Path, progress_reporter: ProgressReporter = None):
        super().__init__(progress_reporter)
        self.grader_data_path = grader_data_path
        self.course_path = course_path

    def process_grader(self, grader_path: Path):
        # TODO: some check to prevent overwriting student files? Perhaps rename them in such cases?
        with importlib.resources.as_file(self.grader_data_path) as grader_data_path:
            shutil.copytree(grader_data_path, grader_path, dirs_exist_ok=True)

        course_readme_path = self.course_path / 'course_readme.txt'
        course_grading_function_path = self.course_path / 'course_grading_function.sh'

        if course_readme_path.exists():
            shutil.copyfile(course_readme_path, grader_path / course_readme_path.name)
        if course_grading_function_path.exists():
            shutil.copyfile(course_grading_function_path, grader_path / 'data' / course_grading_function_path.name)


class CreateGraderConfigPass(GraderPass):
    def __init__(self, division: Division, assignment_info: AssignmentInfo, config: Config, api_config: bsapi.APIConfig,
                 assignment_config: AssignmentConfig, progress_reporter: ProgressReporter = None):
        super().__init__(progress_reporter)
        self.division = division
        self.assignment_info = assignment_info
        self.config = config
        self.api_config = api_config
        self.assignment_config = assignment_config

    def process_grader(self, grader_path: Path):
        submissions_info = self.division[grader_path.name]
        data_path = grader_path / 'data'
        config_path = data_path / 'config.json'
        grader_info = self.config.graders[grader_path.name]

        grade_object = self.assignment_info.grade_object
        grade_scheme = self.assignment_info.grade_scheme

        data_path.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps({
                'orgUnitId': self.assignment_info.course.org_unit.id,
                'folderId': self.assignment_info.assignment.id,
                'groupCategoryId': self.assignment_info.assignment.group_type_id,
                'assignmentId': self.assignment_config.identifier,
                'defaultCodeBlockLanguage': self.assignment_config.default_code_block_language,
                'draftFeedback': self.assignment_config.draft_feedback,
                'gradedByFooter': self.assignment_config.graded_by_footer,
                'tag': self.config.tag,
                'grader': {
                    'name': grader_info.name,
                    'email': grader_info.contact_email
                },
                'grade': {
                    'name': grade_object.name,
                    'type': grade_object.grade_type,
                    'aliases': self.assignment_config.grade_aliases,
                    'maxPoints': self.assignment_info.assignment.assessment.score_denominator,
                    'objectMaxPoints': grade_object.max_points,
                    'symbols': [r.symbol for r in grade_scheme.ranges]
                },
                'api': self.api_config.to_json(),
                'submissions': {info.folder_name: {
                    'entityId': info.entity_id,
                    'entityType': info.entity_type,
                    'submissionId': info.submission_id,
                    'submittedBy': int(info.submitted_by.identifier),
                    'students': {
                        int(student.identifier): {
                            'name': student.display_name,
                            'username': student.user_name,
                        } for student in info.students
                    }
                } for info in submissions_info}
            }, indent=4, ensure_ascii=False))


class CreateGradingInstructionsPass(GraderPass):
    def __init__(self, assignment_info: AssignmentInfo, assignment_config: AssignmentConfig,
                 progress_reporter: ProgressReporter = None):
        super().__init__(progress_reporter)
        self.assigment_info = assignment_info
        self.assignment_config = assignment_config

    def process_grader(self, grader_path: Path):
        grade_name = self.assigment_info.grade_object.name
        grade_type = self.assigment_info.grade_object.grade_type
        scheme_name = self.assigment_info.grade_scheme.name
        symbols = [f'"{r.symbol}"' for r in self.assigment_info.grade_scheme.ranges]
        aliases = self.assignment_config.grade_aliases

        assert grade_type in ['SelectBox', 'Numeric'], 'Update grading instructions for new grade type'

        with open(grader_path / 'grading_instructions.txt', 'w', encoding='utf-8') as f:
            f.write(
                f'This document outlines the grading instructions for "{self.assigment_info.assignment.name}" of "{self.assigment_info.course.org_unit.name}" if using the Brightspace upload script.\n')
            f.write('\n')
            f.write('There is a folder for each submission you have to grade in the submissions/ folder.\n')
            f.write('In there you find a "feedback.txt" template file with some information about that submission.\n')
            f.write('It also contains two parts you have to fill out: the grade and the feedback.\n')
            f.write('Instructions for filling out these parts can be found below.\n')
            f.write(
                'After all feedback and grades have been filled out, run the "data/upload.py" script to upload the grades and feedback to Brightspace using the API.\n')
            if self.assignment_config.draft_feedback:
                f.write('Your feedback and grades will be uploaded in a draft state.\n')
                f.write('Before they are visible to students, they have to be published in Brightspace.\n')
            else:
                f.write('Your feedback and grades will be uploaded in a published state.\n')
                f.write('This means the feedback and grades will be immediately visible to students.\n')
            f.write('\n')
            f.write('[Feedback]\n')
            f.write('Feedback is written in a mostly plaintext style, with some Markdown influence.\n')
            f.write(
                'Paragraphs are formed similar to Markdown, and there is support for inline code and code blocks.\n')
            f.write('Inline code is specified by putting text between single backtick \'`\' characters.\n')
            f.write(
                'Code blocks are specified by putting text between triple backtick \'```\' characters, which may span multiple lines.\n')
            f.write(
                f'Code blocks can specify the code language on a per-block basis, but defaults to "{self.assignment_config.default_code_block_language}".\n')
            f.write('See "readme.txt" for a more elaborate explanation of the feedback syntax.\n')
            f.write('\n')
            f.write('[Grade]\n')
            f.write('By default the grade has the placeholder "TODO" value.\n')
            f.write(
                'Any submission still having this placeholder value will be skipped when uploading the grades and feedback.\n')
            f.write('\n')
            f.write(
                f'The assignment is linked to grade "{grade_name}", which is a "{grade_type}" grade using scheme "{scheme_name}".\n')
            if grade_type == 'Numeric':
                f.write(
                    f'This means you have to replace the placeholder value with a numeric value between {0.0} and {self.assigment_info.assignment.assessment.score_denominator}.\n')
                f.write(
                    'It does not matter whether you use a dot or a period as the decimal separator, "9.5" and "9,5" will both be parsed into a 9.5.\n')
            elif grade_type == 'SelectBox':
                f.write(
                    f'This means you have to replace the placeholder value with one of the following values: {", ".join(symbols)}.\n')
                f.write(
                    'The case of the symbol does not matter, "good", "gOOD", "GOOD", and "Good" are all equivalent for example.\n')
            if aliases:
                f.write('\n')
                f.write('[Aliases]\n')
                f.write('You can also enter one of the grade aliases listed below.\n')
                f.write(
                    'If your grade matches any of the values to the left of the "=>" arrow (case insensitive), it is replaced with the value to the right.\n')
                f.write(
                    'These aliases are usually provided as a shorthand notation for long grade symbols which are otherwise tedious and error prone to type out.\n')
                f.write(
                    'Another use case may be to mimic "SelectBox" style grades for a "Numeric" grades, mapping a symbol to a numeric grade value.\n')
                f.write('\n')
                for alias, value in aliases.items():
                    f.write(f'"{alias}" => "{value}"\n')


class CreateGraderArchivesPass(GraderPass):
    def __init__(self, dist_path: Path, assignment_config: AssignmentConfig,
                 progress_reporter: ProgressReporter = None):
        super().__init__(progress_reporter)
        self.dist_path = dist_path
        self.assignment_config = assignment_config

    def process_grader(self, grader_path: Path):
        grader_id = grader_path.name
        assignment_id = self.assignment_config.identifier

        # Create target file path, and ensure parent folders exists.
        parent_path = self.dist_path.resolve() / assignment_id
        archive_path = parent_path / f'{assignment_id}-{grader_id}.7z'
        password_path = parent_path / f'{assignment_id}-{grader_id}.password'
        parent_path.mkdir(parents=True, exist_ok=True)

        # Generate random password using CS-PRNG.
        alphabet = string.ascii_letters + string.digits
        password_length = 32
        password = ''.join(secrets.choice(alphabet) for _ in range(password_length))
        password_path.write_text(password, encoding='utf-8')

        # 'a'      => Add files to archive command.
        # '-ms=on' => Turn on solid mode (groups files together for potentially better compression).
        # '-mx=9'  => Use Ultra compression level.
        # '-mhe'   => Encrypt archive header to hide file table as file name may still expose student info like names/student numbers.
        # This creates an archive using AES-256-CBC encryption, and a PBKDF based on 2^19 SHA256 iterations.
        args = ['7za', 'a', '-ms=on', '-mx=9', '-mhe', f'-p{password}', archive_path, './']
        try:
            cp = subprocess.run(args, shell=False, check=False, capture_output=True, cwd=grader_path)
            if cp.returncode != 0:
                logger.fatal('Creating archive failed with exit code %d and stderr output "%s"', cp.returncode, cp.stderr)
        except FileNotFoundError:
            logger.fatal('Creating archive failed as 7-Zip was not found')

class NOPPass(SubmissionsPass):
    def process_submission(self, submission_path: Path):
        pass


class FlattenPass(SubmissionsPass):
    def process_submission(self, submission_path: Path):
        for file in get_all_files(submission_path):
            # No need to move files already at the top-level folder.
            if file.parent == submission_path:
                continue

            # Attempt to move file to top-level folder; add random component in name to handle duplicates.
            target_path = submission_path / file.name
            while target_path.exists():
                rand_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
                target_path = submission_path / f'dup-{rand_str}-{file.name}'

            file.rename(target_path)
        # Remove any leftover empty folders.
        for dir_ in [dir_ for dir_ in submission_path.iterdir() if dir_.is_dir()]:
            shutil.rmtree(dir_, ignore_errors=True)


class SmartFlattenPass(SubmissionsPass):
    @staticmethod
    def _is_empty(path: Path) -> bool:
        # Check if the path contains any files, directly or indirectly.
        for item in path.iterdir():
            if item.is_dir():
                if not SmartFlattenPass._is_empty(item):
                    return False
            else:
                return False

        return True

    @staticmethod
    def _prune(path: Path):
        # Prune folders without any files, directly or indirectly.
        dirs = [dir_ for dir_ in path.iterdir() if dir_.is_dir()]

        for dir_ in dirs:
            if SmartFlattenPass._is_empty(dir_):
                shutil.rmtree(dir_, ignore_errors=True)
            else:
                SmartFlattenPass._prune(dir_)

    @staticmethod
    def _merge(src: Path, dst: Path):
        for entry in list(src.iterdir()):
            if entry.is_file():
                # Ensure parent folder structure exists, then move the file there.
                dst.mkdir(parents=True, exist_ok=True)
                entry.rename(dst / entry.name)
            elif entry.is_dir():
                SmartFlattenPass._merge(entry, dst / entry.name)

    def process_submission(self, submission_path: Path):
        files = get_all_files(submission_path)
        if files:
            # Find the longest common prefix path of all files.
            common_path = files[0].parent
            while not all([common_path in file.parents for file in files]):
                common_path = common_path.parent

            # If this common prefix path is not the submission path itself, we have redundant empty top-level folders.
            # We merge all files and folders under this common prefix path into the submission path.
            # This gets rid of the redundant top-level folders, but will leave empty folders.
            # Those are cleaned up with the later prune call however, so this is not an issue.
            if common_path != submission_path:
                self._merge(common_path, submission_path)

        # Remove empty folder trees, i.e. trees only containing other folders and not any actual files.
        self._prune(submission_path)


class InjectFilesPass(SubmissionsPass):
    def __init__(self, config: AssignmentConfig, inject_path: Path, progress_reporter: ProgressReporter = None):
        super().__init__(progress_reporter)
        self.inject_path = inject_path / config.identifier / 'submission'

    def process_submission(self, submission_path: Path):
        # TODO: some check to prevent overwriting student files? Perhaps rename them in such cases?
        shutil.copytree(self.inject_path, submission_path, dirs_exist_ok=True)

    def execute(self, path: Path):
        if self.inject_path.exists():
            super().execute(path)


class CreateFeedbackTemplatePass(SubmissionsPass):
    def __init__(self, info: AssignmentInfo, progress_reporter: ProgressReporter = None):
        super().__init__(progress_reporter)
        self.info = info
        self.submissions_info = {si.folder_name: si for si in info.submissions}

    def process_submission(self, submission_path: Path):
        assert submission_path.name in self.submissions_info, f'No submission info for folder {submission_path.name}'
        submission_info = self.submissions_info[submission_path.name]

        # Format as local time zone, rather than UTC.
        # This assumes the machine running this has the same timezone as the graders.
        submitted_at = submission_info.submitted_at.astimezone().strftime("%Y-%m-%d %H:%M:%S")

        # Mark late submissions and show how late they are to give graders more context.
        if self.info.assignment.due_date and submission_info.submitted_at > self.info.assignment.due_date:
            # No way to pick our own formatting, so manually break it down into the desired components.
            late_by = submission_info.submitted_at - self.info.assignment.due_date
            days = late_by.days
            hours = late_by.seconds // 3600
            minutes = (late_by.seconds // 60) % 60
            seconds = late_by.seconds % 60
            submitted_at += f' (!!!LATE!!! {days} day{"s" if days != 1 else ""}, {hours}h:{minutes}m:{seconds}s)'

        with open(submission_path / 'feedback.txt', 'w', encoding='utf-8') as f:
            f.write(f'Assignment: {self.info.assignment.name}\n')
            f.write(
                f'Submitted by: {submission_info.submitted_by.display_name} ({submission_info.submitted_by.user_name.lower()})\n')
            f.write(f'Submitted at: {submitted_at}\n')
            if self.info.groups:
                f.write(f'Group: {submission_info.group_name}\n')
                for student in submission_info.students:
                    f.write(f'Group member: {student.display_name} ({student.user_name.lower()})\n')
            f.write('====================[Brightspace comment]====================\n')
            f.write(f'{submission_info.comment}\n')
            f.write('====================[Enter grade below]======================\n')
            f.write('TODO\n')
            f.write('====================[Enter feedback below]===================\n')
            f.write('\n')


# removeFiles: list of glob: '.*' to remove all dotfiles, '*.exe' to remove all exe, etc
# removeFolders: list of glob: '.*' to remove all dotfolders, '__MACOSX' etc
# removeMimes: list of glob: 'application/x-sharedlib', 'application/x-executable', 'application/x-dosexec'
# ^ use python-libmagic? just subprocess.run 'file'?
class RemoveFilesPass(SubmissionsPass):
    def __init__(self, config: AssignmentConfig, progress_reporter: ProgressReporter = None):
        super().__init__(progress_reporter)
        self.config = config
        self.regex_files = [re.compile(fnmatch.translate(pattern), re.IGNORECASE) for pattern in config.remove_files]
        self.regex_folders = [re.compile(fnmatch.translate(pattern), re.IGNORECASE) for pattern in
                              config.remove_folders]

    def _should_remove_file(self, name: str) -> bool:
        for regex in self.regex_files:
            if regex.match(name):
                return True
        return False

    def _should_remove_folder(self, name: str) -> bool:
        for regex in self.regex_folders:
            if regex.match(name):
                return True
        return False

    def process_submission(self, submission_path: Path):
        entries = list(submission_path.iterdir())

        for entry in entries:
            if entry.is_fifo():
                # Python libraries like shutil do not handle fifo/named pipes well, so remove any encountered.
                # This is mostly an issue during Hacking in C where students use named pipes as part of their exploit and end up submitting them.
                entry.unlink()
            elif entry.is_symlink():
                # Remove any symbolic links encountered that may be produced due to extracting tarballs.
                # Following such links may have undesired consequences, or pull in files that should not be included.
                entry.unlink()
            elif entry.is_dir():
                if self._should_remove_folder(entry.name):
                    shutil.rmtree(entry, ignore_errors=True)
                else:
                    # Recursively process child directory.
                    self.process_submission(entry)
            elif entry.is_file():
                if self._should_remove_file(entry.name):
                    entry.unlink()
                # TODO: Check Mime type?


class DocxToPdfPass(SubmissionsPass):
    def process_submission(self, submission_path: Path):
        for file in get_all_files(submission_path):
            if file.suffix.lower() == '.docx':
                args = ['libreoffice', '--convert-to', 'pdf', '--outdir', file.parent, file]
                cp = subprocess.run(args, shell=False, check=False, capture_output=True)
                if cp.returncode != 0:
                    logger.warning('Converting "%s" to PDF failed: %s (exit code %d)', file.name,
                                   cp.stderr.decode('utf-8'), cp.returncode)

    def execute(self, path: Path):
        # Check whether libreoffice is installed.
        args = ['libreoffice', '--version']
        try:
            cp = subprocess.run(args, shell=False, check=False, capture_output=True)
            if cp.returncode == 0:
                logger.debug('Found LibreOffice version %s', cp.stdout.decode('utf-8'))
                super().execute(path)
            else:
                logger.warning('Skipping DOCX to PDF pass as LibreOffice was not found')
        except FileNotFoundError:
            logger.warning('Skipping DOCX to PDF pass as LibreOffice was not found')


class FixFilePermissionsPass(SubmissionsPass):
    READABLE = stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH

    def process_submission(self, submission_path: Path):
        for file in get_all_files(submission_path):
            stat_ = file.stat()
            permissions = stat.S_IMODE(stat_.st_mode)

            # Make sure we have read permissions to the files.
            # It can happen students submit files that are not readable by default.
            # One common cause is Wireshark packet captures as it runs as root.
            # The produced capture is stored as having root as the owner, which often leads to students mangling permissions when submitting them in tars.
            if permissions & self.READABLE != self.READABLE:
                os.chmod(file, permissions | self.READABLE)

            # Zip files do not support last modified timestamps before 1980.
            # This means trying to zip such files will fail, which has happened with some student submissions.
            # As such, update the last modified timestamp to the current time for all such files.
            # https://stackoverflow.com/questions/3725662/what-is-the-earliest-timestamp-value-that-is-supported-in-zip-file-format
            if time.localtime(stat_.st_mtime).tm_year < 1980:
                os.utime(file)


class ExtractArchivesPass(SubmissionsPass):
    @staticmethod
    def _extract_patoolib(path: Path, submission_name: str) -> bool:
        try:
            # Attempt to extract archive to parent folder.
            # The verbosity and interactive parameters should ensure nothing hangs, or shows output.
            # It may not be bulletproof however, as it only sets the stdin of the extraction process to an empty string.
            # Anything shown to standard error is also not hidden, and impossible to hide.
            patoolib.extract_archive(path, outdir=path.parent, verbosity=-1, interactive=False)
            return True
        except patoolib.util.PatoolError:
            logger.error('Failed to extract archive "%s" in %s', path.name, submission_name)
            return False

    @staticmethod
    def _extract_tarfile(path: Path, submission_name: str) -> bool:
        # TODO: should we extract a subset by manually filtering members as shown in the examples?
        # See https://docs.python.org/3/library/tarfile.html#examples.
        # Besides stripping out non-regular files like named pipes/links, we should also really check whether the file
        # extracts to the target folder, i.e. isn't absolute (/ prefix) or contains "..", permission bits etc.
        # We probably want to specify a custom filter callable if this is supported (enforce this?) and return `None`
        # on 'bad' entries to skip extracting them, rather than raising `FilterError`` to produce a fatal error.
        # We could take most of what the 'data' filter does, but tweak it a bit?
        # This would avoid rejecting (further) extraction of archives that do not pass the filter, which is done on a
        # member by member basis, so extraction of an archive may fail at any point and will not attempt to clean up.
        # This would leave a confusing mess of a potentially half extracted archive alongside the archive itself.
        try:
            with tarfile.open(path, errorlevel=2) as tf:
                # Filters were introduces as a Python 3.12 feature, but may be backported as a security feature.
                # See https://docs.python.org/3/library/tarfile.html#supporting-older-python-versions.
                if hasattr(tarfile, 'data_filter'):
                    # Specify a data filter to prevent most of the problematic stuff from occurring.
                    # See https://docs.python.org/3/library/tarfile.html#tarfile.data_filter.
                    # Note that any member not passing the filter will halt extraction entirely.
                    # This is because it is raised as a 'fatal' error.
                    tf.extractall(path.parent, filter='data')
                else:
                    logger.warning('Data filter not supported, update Python version')
                    tf.extractall(path.parent)
            return True
        except (tarfile.TarError, OSError):
            logger.error('Failed to extract archive "%s" in %s', path.name, submission_name)
            return False

    @staticmethod
    def _extract_archive(path: Path, submission_name: str) -> bool:
        name = path.name.lower()

        # Extract tar files using the Python tarfile library rather than passing it to patoolib.
        # While patoolib supports extracting these archives itself, it tends to use the installed GNU tar binary.
        # This is problematic as it does not handle tar files made on OSX by BSD tar well, which students often submit.
        # Such tars include extra extended header keywords it does not understand, which generate error messages that
        # are printed to the standard error stream, unless '--warning=no-unknown-keyword' is specified.
        # However, we have no way to hide the standard error stream, or to specify this warning option via patoolib.
        # This causes spamming of the standard error stream with messages like the following:
        # tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'
        # tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemWhereFroms'
        # tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.metadata:kMDItemDownloadedDate'
        # tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.macl'
        # tar: Ignoring unknown extended header keyword 'SCHILY.fflags'
        # tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.FinderInfo'
        # By extracting via tarfile we also have more control over what is extracted, which has security implications.
        if name.endswith('.tar') or name.endswith('.tar.xz') or name.endswith('.tar.gz') or name.endswith('.tar.bz2'):
            return ExtractArchivesPass._extract_tarfile(path, submission_name)
        else:
            return ExtractArchivesPass._extract_patoolib(path, submission_name)

    def process_submission(self, submission_path: Path):
        excluded_archives = []

        # Try to recursively extract archives as students sometimes submit nested archives.
        # We do limit to 3 iterations to help mitigate (un)intentional zip-bomb like situations.
        for _ in range(1, 3):
            # Walk the path to get a list of all files under path, either directly or in subdirectories, then filter on supported archive extensions.
            files = get_all_files(submission_path)
            arc_files = filter_files(files, ['zip', 'rar', '7z', 'tar', 'xz', 'gz', 'bz2'])

            # Break out early if no archives are found.
            if not arc_files:
                break

            for file in arc_files:
                # Do not try to extract archives that already failed to extract.
                if file in excluded_archives:
                    continue

                if self._extract_archive(file, submission_path.name):
                    # Remove the archive once extracted so that we do not try extracting it again.
                    file.unlink()
                else:
                    # Failed to extract, so mark it to prevent re-extracting next iteration.
                    # We also keep the file so that the grader can try to sort it out themselves.
                    excluded_archives.append(file)


class MoveToGraderPass(SubmissionsPass):
    def __init__(self, division: Division, graders_path: Path, progress_reporter: ProgressReporter = None):
        super().__init__(progress_reporter)
        self.submission_to_grader: dict[str, str] = dict()
        self.graders_path = graders_path

        for grader_id, submissions in division:
            for submission in submissions:
                self.submission_to_grader[submission.folder_name] = grader_id

            grader_path = graders_path / grader_id / 'submissions'
            grader_path.mkdir(parents=True, exist_ok=True)

    def process_submission(self, submission_path: Path):
        grader_id = self.submission_to_grader[submission_path.name]
        grader_path = self.graders_path / grader_id / 'submissions'
        shutil.move(submission_path, grader_path)
