from dataclasses import dataclass
import logging
from os import listdir
from pathlib import Path
import sys
from typing import Optional
from zipfile import ZipFile, ZIP_DEFLATED
from shutil import copyfile
import json

import bsapi
import bsapi.feedback
import bsapi.identity
import bsapi.types

logger = logging.getLogger(__name__)


@dataclass
class Config:
    @dataclass
    class Grader:
        name: str
        email: str

    @dataclass
    class Grade:
        name: str
        type: str
        aliases: dict[str, str]
        max_points: float
        object_max_points: float
        symbols: list[str]

    @dataclass
    class Submission:
        @dataclass
        class Student:
            name: str
            username: str

        entity_id: int
        entity_type: str
        submission_id: int
        submitted_by: int
        students: dict[int, Student]

    org_unit_id: int
    folder_id: int
    group_category_id: Optional[int]
    assignment_id: str
    default_code_block_language: str
    draft_feedback: bool
    graded_by_footer: bool
    tag: str
    grader: Grader
    grade: Grade
    api: bsapi.APIConfig
    submissions: dict[str, Submission]

    @staticmethod
    def from_json(obj: dict):
        return Config(
            org_unit_id=obj['orgUnitId'],
            folder_id=obj['folderId'],
            group_category_id=obj['groupCategoryId'],
            assignment_id=obj['assignmentId'],
            default_code_block_language=obj['defaultCodeBlockLanguage'],
            draft_feedback=obj['draftFeedback'],
            graded_by_footer=obj['gradedByFooter'],
            tag=obj['tag'],
            grader=Config.Grader(
                name=obj['grader']['name'],
                email=obj['grader']['email']
            ),
            grade=Config.Grade(
                name=obj['grade']['name'],
                type=obj['grade']['type'],
                aliases=obj['grade']['aliases'],
                max_points=obj['grade']['maxPoints'],
                object_max_points=obj['grade']['objectMaxPoints'],
                symbols=obj['grade']['symbols']
            ),
            api=bsapi.APIConfig.from_json(obj['api']),
            submissions={
                folder_name: Config.Submission(
                    entity_id=submission['entityId'],
                    entity_type=submission['entityType'],
                    submission_id=submission['submissionId'],
                    submitted_by=submission['submittedBy'],
                    students={
                        int(user_id): Config.Submission.Student(
                            name=student['name'],
                            username=student['username']
                        )
                        for user_id, student in submission['students'].items()}
                )
                for folder_name, submission in obj['submissions'].items()}
        )


@dataclass
class ProcessedGrade:
    symbol: Optional[str]
    score: Optional[float]
    placeholder: bool

    @staticmethod
    def from_symbol(symbol: str):
        return ProcessedGrade(symbol, None, False)

    @staticmethod
    def from_score(score: float):
        return ProcessedGrade(None, score, False)

    @staticmethod
    def from_placeholder():
        return ProcessedGrade(None, None, True)

    def __str__(self) -> str:
        if self.placeholder:
            return '<None>'
        elif self.symbol is not None:
            return self.symbol
        elif self.score is not None:
            return str(self.score)
        else:
            return '<None>'


@dataclass
class ExportInfo:
    folder_name: str
    path: Path
    submission: Config.Submission
    grade: ProcessedGrade
    feedback: str
    feedback_html: str


@dataclass
class ProcessedFeedback:
    grade: str
    feedback: str


def process_grade(grade: str, name: str, config: Config) -> Optional[ProcessedGrade]:
    if grade == 'TODO':
        return ProcessedGrade.from_placeholder()

    # See if we have to apply a grade alias, e.g. 'nsa' to 'Not Seriously Attempted'
    for alias, to in config.grade.aliases.items():
        if grade.lower() == alias.lower():
            grade = to

    if config.grade.type == 'Numeric':
        try:
            # Allow grades to use both a comma and a period for the decimal separator.
            grade = grade.replace(',', '.')
            score = float(grade)

            if score < 0:
                logger.error('Invalid grade field "%s" for "%s" (cannot be negative)', grade, name)
            elif score > config.grade.max_points:
                logger.error('Invalid grade field "%s" for "%s" (cannot exceed %s)', grade, name,
                             config.grade.max_points)
            else:
                return ProcessedGrade.from_score(score)
        except ValueError:
            logger.error('Invalid grade field "%s" for "%s" (could not parse as float)', grade, name)

        return None
    elif config.grade.type == 'SelectBox':
        for symbol in config.grade.symbols:
            if grade.lower() == symbol.lower():
                return ProcessedGrade.from_symbol(symbol)

        logger.error('Invalid grade symbol "%s" for "%s" (valid options are %s)', grade, name,
                     ', '.join(f'"{s}"' for s in config.grade.symbols))
        if config.grade.aliases:
            logger.error('The following grade aliases are also available')
            for k, v in config.grade.aliases.items():
                logger.error('- %s => %s', k, v)

        return None
    else:
        logger.error('Grade type "%s" is not supported', config.grade.type)
        return None


def process_feedback_file(path: Path, name: str) -> Optional[ProcessedFeedback]:
    grade_header = '====================[Enter grade below]======================'
    feedback_header = '====================[Enter feedback below]==================='
    feedback_text = path.read_text(encoding='utf-8')
    grade_header_idx = feedback_text.find(grade_header)
    feedback_header_idx = feedback_text.find(feedback_header)

    if grade_header_idx < 0:
        logger.error(f'Feedback file of "%s" is missing grade field header', name)
        return None
    if feedback_header_idx < 0:
        logger.error(f'Feedback file of "%s" is missing feedback field header', name)
        return None
    if feedback_header_idx < grade_header_idx:
        logger.error(f'Feedback file of "%s" has feedback field header before grade field header', name)
        return None

    grade_field = feedback_text[grade_header_idx + len(grade_header):feedback_header_idx].strip()
    feedback_field = feedback_text[feedback_header_idx + len(feedback_header):].strip()

    if not grade_field:
        logger.error(f'Feedback file of "%s" has an empty grade field', name)
        return None

    return ProcessedFeedback(grade_field, feedback_field)


def export_submission(path: Path, submission: Config.Submission, export_path: Path, config: Config) -> Optional[
    ExportInfo]:
    name = path.name
    feedback_path = path / 'feedback.txt'
    submission_from = submission.students[submission.submitted_by]
    submitted_by = f'{submission_from.name} ({submission_from.username.lower()})'

    print(f'[-] {name} (submitted by {submitted_by})')

    if not feedback_path.is_file():
        logger.error('Skipping "%s" due to missing feedback file', name)
        return None

    processed_feedback = process_feedback_file(feedback_path, name)

    if processed_feedback is None:
        logger.error('Skipping "%s" due to errors while processing feedback file', name)
        return None

    grade = process_grade(processed_feedback.grade, name, config)

    if grade is None:
        logger.error('Skipping "%s" due to errors while processing grade', name)
        return None
    elif grade.placeholder:
        logger.warning('Skipping "%s" as it has not yet been graded', name)
        return None

    # Finalize feedback by applying graded by footer.
    feedback = processed_feedback.feedback
    if config.graded_by_footer:
        feedback += f'\n\nYour submission was graded by {config.grader.name} (you can contact me using {config.grader.email})'

    # Copy feedback file so that it can be zipped later with all other feedback files.
    copyfile(feedback_path, export_path / f'feedback-{name}.txt')

    feedback_encoder = bsapi.feedback.BasicCodeEncoder(config.default_code_block_language, line_numbers=True)
    feedback_html = feedback_encoder.encode(feedback)

    return ExportInfo(name, path, submission, grade, feedback, feedback_html)


def create_zip(source_path: Path, path: Path):
    with ZipFile(path, 'w', ZIP_DEFLATED) as zf:
        for file in listdir(source_path):
            zf.write(source_path / file, arcname=file)


def load_json(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


def format_remote_grade(feedback_out: bsapi.types.DropboxFeedbackOut, config: Config) -> str:
    if config.grade.type == 'SelectBox':
        symbol = feedback_out.graded_symbol
        return symbol if symbol else '<None>'
    elif config.grade.type == 'Numeric':
        if feedback_out.score is None: return '<None>'
        return str(feedback_out.score)
    else:
        return '<Unsupported type>'


def get_overwrite_method() -> str:
    while True:
        method = input("Overwrite attached feedback file? [yes/no/always/never]: ").lower().strip()

        if method in ['yes', 'no', 'always', 'never']:
            return method
        else:
            print('Invalid method, please try again')


def get_conflict_resolve_method() -> str:
    while True:
        method = input("Resolve method [discard/overwrite/select/cancel]: ").lower().strip()

        if method in ['discard', 'overwrite', 'select', 'cancel']:
            return method
        else:
            print('Invalid method, please try again')


def get_single_conflict_resolve_method(submission: ExportInfo, existing_feedback: bsapi.types.DropboxFeedbackOut,
                                       config: Config) -> str:
    # Present diff.
    print()
    print(f'<<< YOUR FEEDBACK (Grade: {str(submission.grade)}, select via overwrite) >>>')
    print(submission.feedback)
    print()
    print(f'>>> EXISTING FEEDBACK (Grade: {format_remote_grade(existing_feedback, config)}, select via discard) <<<')
    if existing_feedback.feedback:
        print(existing_feedback.feedback.text)
    else:
        print('<No feedback set>')
    print()

    # Get resolve action.
    while True:
        action = input("Resolve action [discard/overwrite/cancel]: ").lower().strip()

        if action in ['discard', 'overwrite', 'cancel']:
            return action
        else:
            print('Invalid action, please try again')


def format_student_description(user_id: int, users: dict[int, bsapi.types.User]) -> str:
    if user_id not in users:
        return f'UNKNOWN (D2LID={user_id})'
    else:
        user = users[user_id]
        return f'{user.display_name} ({user.user_name.lower()})'


def use_api(config: Config, export_info: list[ExportInfo], export_path: Path) -> bool:
    print('[*] Using Brightspace API to upload grades and feedback')

    identity_manager = bsapi.identity.IdentityManager.from_config(config.api)
    if not identity_manager.load_store():
        logger.error('Failed to load stored identities')
        return False
    identity = identity_manager.get_identity(config.tag)
    if not identity:
        logger.warning('No identity selected, aborting upload')
        return False

    api = bsapi.BSAPI.from_config(config.api, identity.user_id, identity.user_key)

    org_unit_id = config.org_unit_id
    folder_id = config.folder_id
    group_category_id = config.group_category_id
    draft_feedback = config.draft_feedback

    # Check if groups have changed between export and grading.
    if config.group_category_id is not None:
        print('[*] Checking if groups have changed')
        try:
            users = {int(user.user.identifier): user.user for user in
                     api.get_users(org_unit_id, role_id=bsapi.ROLE_STUDENT)}
        except bsapi.APIError as e:
            users: dict[int, bsapi.types.User] = dict()
            logger.error('Could not get list of users due to API error: %s', e.cause)

        for submission in export_info:
            entity_id = submission.submission.entity_id
            entity_type = submission.submission.entity_type
            name = submission.folder_name

            assert entity_type == 'Group', 'Incorrect entity type'

            try:
                group_info = api.get_group(org_unit_id, group_category_id, entity_id)
                export_enrollment = list(submission.submission.students.keys())
                current_enrollment = group_info.enrollments

                export_enrollment.sort()
                current_enrollment.sort()

                if export_enrollment != current_enrollment:
                    logger.warning(
                        'Group %s has changed since export! Only members currently enrolled will receive the grade',
                        name)
                    logger.warning('    During export it contained the following members:')
                    for uid in export_enrollment:
                        logger.warning('    - %s', format_student_description(uid, users))
                    logger.warning('    It now contains the following members:')
                    for uid in current_enrollment:
                        logger.warning('    - %s', format_student_description(uid, users))
                    logger.warning('    Please make sure to manually correct for any missing grades!')
            except bsapi.APIError as e:
                logger.error('Could not get group enrollment for %s due to API error: %s', name, e.cause)

    # Check for conflicts regrading existing feedback.
    # This should not occur if work is divided correctly, and everyone adheres to the division.
    # It could however be the case that a grader reruns the script after encountering issues.
    print('[*] Checking for existing feedback')
    existing_feedback: dict[int, tuple[ExportInfo, bsapi.types.DropboxFeedbackOut]] = dict()
    for submission in export_info:
        entity_id = submission.submission.entity_id
        entity_type = submission.submission.entity_type
        name = submission.folder_name
        submission_from = submission.submission.students[submission.submission.submitted_by]
        submitted_by = f'{submission_from.name} ({submission_from.username.lower()})'

        try:
            # TODO: Check if most recent submission matches 'submission.submission.submission_id', i.e. the one that
            # was distributed. If not warn that this entity has probably made a more recent submission, so the grader
            # knows to account for this. Problem is we cannot get this from the feedback API call below. We need to
            # call 'api.get_dropbox_folder_submissions' to get the 'bsapi.types.EntityDropBox' instance. This gives us
            # all the submissions from all entities, as there is no endpoint to just get it from one entity, making it
            # a bit awkward, so cache once and transform into a dict type for easy lookup?
            feedback_obj = api.get_dropbox_folder_submission_feedback(org_unit_id, folder_id, entity_type, entity_id)

            if feedback_obj:
                logger.warning('Found existing feedback for %s (submitted by %s)', name, submitted_by)
                logger.warning('    - Current Brightspace grade: %s, your grade: %s',
                               format_remote_grade(feedback_obj, config), str(submission.grade))
                existing_feedback[entity_id] = (submission, feedback_obj)

                # Make a local backup of existing feedback just in case it needs to be manually recovered.
                if feedback_obj.feedback:
                    with open(export_path / (name + '-existing-feedback.html'), 'w', encoding='utf-8') as ef:
                        ef.write(feedback_obj.feedback.html)
        except bsapi.APIError as e:
            logger.error('Could not get feedback for %s (submitted by %s) due to API error: %s', name, submitted_by,
                         e.cause)

    # Conflicts detected, so ask grader how to handle them.
    resolve_method = 'cancel'
    if existing_feedback:
        print(f'The existing feedback has been backed up to {export_path}')
        print('')
        print('Please deside how to handle the conflicts')
        print('    - discard:   Discard your feedback, keeping existing feedback in Brightspace for all conflicts')
        print('    - overwrite: Overwrite all existing conflicting feedback in Brightspace with your feedback')
        print('    - select:    Decide per conflicting submission')
        print('    - cancel:    Cancel the upload and exit')
        print('')

        resolve_method = get_conflict_resolve_method()
        if resolve_method == 'cancel':
            logger.warning('Canceling upload of feedback and grades')
            return True

    # Upload the grades and feedback.
    all_uploaded = True
    always_overwrite = False
    never_overwrite = False
    print('[*] Uploading feedback and grades')
    for submission in export_info:
        entity_id = submission.submission.entity_id
        entity_type = submission.submission.entity_type
        name = submission.folder_name
        submission_from = submission.submission.students[submission.submission.submitted_by]
        submitted_by = f'{submission_from.name} ({submission_from.username.lower()})'
        grade = submission.grade

        print(f'[-] {name} (submitted by {submitted_by})')

        # Handle conflict.
        if entity_id in existing_feedback:
            if resolve_method == 'select':
                sub, existing = existing_feedback[entity_id]
                action = get_single_conflict_resolve_method(sub, existing, config)
            else:
                action = resolve_method

            if action == 'discard':
                print('    - skipping, existing Brightspace feedback kept')
                continue
            elif action == 'cancel':
                logger.warning('Canceling upload of feedback and grades')
                logger.warning('Note that any uploads before cancellation are not undone!')
                return True
            elif action == 'overwrite':
                print('    - Overwriting existing Brightspace feedback')

        try:
            if config.grade.type == 'SelectBox':
                api.set_dropbox_folder_submission_feedback(org_unit_id, folder_id, entity_type, entity_id,
                                                           symbol=grade.symbol, html_feedback=submission.feedback_html,
                                                           draft=draft_feedback)
            elif config.grade.type == 'Numeric':
                api.set_dropbox_folder_submission_feedback(org_unit_id, folder_id, entity_type, entity_id,
                                                           score=grade.score, html_feedback=submission.feedback_html,
                                                           draft=draft_feedback)
        except bsapi.APIError as e:
            logger.error('Could not set feedback for %s due to API error: %s', name, e.cause)
            all_uploaded = False

        # Attach any feedback files if they exist.
        attach_feedback_path = submission.path / '__attach_feedback'
        if attach_feedback_path.is_dir():
            try:
                # Grab a list of currently attached files in the feedback to see if we are overwriting or not.
                current_feedback = api.get_dropbox_folder_submission_feedback(org_unit_id, folder_id, entity_type, entity_id)
                current_files = {file.file_name:file.file_id for file in current_feedback.files}

                for file_path in attach_feedback_path.iterdir():
                    # Only support uploading top-level files, nested folders not supported.
                    if not file_path.is_file():
                        logger.warning('Not attaching "%s" as feedback for %s as it is not a regular file', file_path.name, name)
                        continue

                    exists = file_path.name in current_files
                    overwrite = always_overwrite

                    # Found conflict, ask grader to overwrite or not, unless always/never overwriting.
                    if exists and not always_overwrite and not never_overwrite:
                        logger.warning('Feedback file "%s" already attached', file_path.name)

                        # Get overwrite method: yes/no/always/never.
                        choice = get_overwrite_method()
                        if choice == 'yes':
                            overwrite = True
                        elif choice == 'always':
                            always_overwrite = True
                            overwrite = True
                        elif choice == 'never':
                            never_overwrite = True

                    if exists and overwrite:
                        api.remove_dropbox_folder_submission_feedback_file(org_unit_id, folder_id, entity_type, entity_id, current_files[file_path.name])

                    if not exists or overwrite:
                        print(f'    - Attaching feedback file {file_path.name}')
                        api.add_dropbox_folder_submission_feedback_file(org_unit_id, folder_id, entity_type, entity_id, file_path)
            except bsapi.APIError as e:
                logger.error('Could not attach feedback files for %s due to API error: %s', name, e.cause)
                all_uploaded = False


    if all_uploaded:
        print('[*] All feedback and grades uploaded successfully')
        return True
    else:
        print()
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('!!! Not all feedback and grades were uploaded, please address issues !!!')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return False


def ask_user_to_use_api() -> bool:
    while True:
        response = input('[?] Do you want to upload the grades & feedback using the Brightspace API? (y/n): ').lower()

        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print('Invalid response, please try again')


def export(root_path: Path, config: Config):
    data_path = root_path / 'data'
    submissions_path = root_path / 'submissions'
    export_path = root_path / 'export'
    feedback_path = data_path / 'feedback'
    feedback_zip_path = export_path / f'{config.assignment_id}-feedback.zip'
    grades_path = export_path / f'{config.assignment_id}-grades.csv'

    if not submissions_path.is_dir():
        logger.critical('Could not find submissions folder')
        exit(1)
    if not data_path.is_dir():
        logger.critical('Could not find data folder')
        exit(1)

    feedback_path.mkdir(parents=True, exist_ok=True)
    export_path.mkdir(parents=True, exist_ok=True)

    # Process all submissions assigned to us.
    print('[*] Processing submissions')
    export_info: list[ExportInfo] = []

    for folder_name, submission in config.submissions.items():
        submission_path = submissions_path / folder_name

        # Check if folders exist or not.
        # Skip any missing folders rather than seeing it as an error.
        # This allows graders to easily exclude some submissions by just removing/renaming the folder.
        if submissions_path.is_dir():
            info = export_submission(submission_path, submission, feedback_path, config)

            if info is not None:
                export_info.append(info)
        else:
            print(f'- Skipping {folder_name} as submission folder does not exist')

    # Create the grades.csv file.
    print('[*] Creating grades CSV')
    with open(grades_path, 'w', encoding='utf-8') as grades:
        grade_type_headers = {
            'Numeric': 'Points Grade',
            'PassFail': 'Points Grade',
            'SelectBox': 'Grade Symbol',
            'Text': 'Text Grade'
        }

        # Write CSV header.
        grades.write(
            f'OrgDefinedId,{config.grade.name} {grade_type_headers[config.grade.type]},End-of-Line Indicator\n')

        # Write CSV rows.
        for info in export_info:
            if config.grade.type == 'SelectBox':
                formatted_grade = info.grade.symbol
            elif config.grade.type == 'Numeric':
                # Since assignments and their linked numeric grade can have different max point values we have to scale them.
                # This is because we want to apply the assignment grade to the linked grade object grade.
                scaled_score = (info.grade.score / config.grade.max_points) * config.grade.object_max_points
                formatted_grade = str(scaled_score).replace(',', '.')

            for student in info.submission.students.values():
                grades.write(f'#{student.username},{formatted_grade},#\n')

                # Zip all feedback files into a single archive.
    print('[*] Zipping feedback')
    create_zip(feedback_path, feedback_zip_path)

    # Ask user to upload grades/feedback to Brightspace via API
    if ask_user_to_use_api():
        # Try to upload via API, and exit with an error code if something went wrong.
        if not use_api(config, export_info, export_path):
            sys.exit(1)
    else:
        print("Please don't forget to manually enter the feedback and grades in Brightspace!")
        print("You can import the grades csv, but this does NOT include feedback!")


def manager(config: Config):
    identity_manager = bsapi.identity.IdentityManager.from_config(config.api)
    # identity_manager = bsapi.identity.IdentityManager(config.api.lms_url, config.api.app_id, config.api.app_key,
    #                                                   config.api.client_app_url)
    if not identity_manager.load_store():
        logger.error('Failed to load stored identities')

    identity_manager.manage()


def main():
    logging.basicConfig(level=logging.WARNING, format='[%(name)s] [%(levelname)s]: %(message)s')

    # Scan upwards from this script file to try and find correct root folder.
    # If running in a virtualenv we may be inside a sub-folder thus nested deeper.
    root_path = Path(sys.argv[0]).resolve().parent
    config_path = root_path / 'data' / 'config.json'
    while not config_path.is_file() and root_path.parent != root_path:
        root_path = root_path.parent
        config_path = root_path / 'data' / 'config.json'

    if not config_path.is_file():
        logger.critical('Config file not found')
        return

    log_path = root_path / 'data' / 'upload.log'
    file_handler = logging.FileHandler(log_path, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(file_handler)

    config = Config.from_json(load_json(config_path))

    if '-m' in sys.argv or '--manage' in sys.argv:
        manager(config)
    else:
        export(root_path, config)


if __name__ == '__main__':
    main()
