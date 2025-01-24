from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
import email.message
import logging
import datetime
from operator import attrgetter, itemgetter
from pathlib import Path
import random
import smtplib
import subprocess
from smtplib import SMTPException
from typing import Iterable, Optional

import bsapi
import bsapi.helper
import bsapi.identity
import bsapi.types

from bsscripts.config import Config, SMTPConfig
from bsscripts.utils import format_filesize

logger = logging.getLogger(__name__)


class ProgressReporter:
    def start(self, current: int, total: int, name: str):
        pass

    def finish(self, total: int):
        pass


@dataclass
class SubmissionInfo:
    entity_id: int
    entity_type: str
    submitted_by: bsapi.types.User
    submitted_at: datetime.datetime
    submission_id: int
    folder_name: str
    comment: str
    group_name: Optional[str]
    students: list[bsapi.types.User]


@dataclass
class AssignmentInfo:
    identifier: str
    course: bsapi.types.MyOrgUnitInfo
    assignment: bsapi.types.DropboxFolder
    users: dict[int, bsapi.types.User]
    groups: Optional[dict[int, bsapi.types.GroupData]]
    submissions: list[SubmissionInfo]
    grade_object: bsapi.types.GradeObject
    grade_scheme: bsapi.types.GradeScheme


@dataclass
class LogEntry:
    @dataclass
    class Student:
        name: str
        username: str

    entity_id: int
    submission_id: int
    folder_name: str
    students: list[Student]

    def serialize(self) -> str:
        return f'{self.entity_id};{self.submission_id};{self.folder_name};{",".join(f"{s.name} ({s.username})" for s in self.students)}'

    @staticmethod
    def deserialize(line: str):
        parts = line.split(';')
        entity_id = int(parts[0])
        submission_id = int(parts[1])
        folder_name = parts[2]
        students: list[LogEntry.Student] = []
        for student_str in parts[3].split(','):
            name, _, username = student_str.rpartition(' (')
            students.append(LogEntry.Student(name, username[:-1]))

        return LogEntry(entity_id, submission_id, folder_name, students)

    @staticmethod
    def from_info(info: SubmissionInfo):
        return LogEntry(info.entity_id, info.submission_id, info.folder_name,
                        [LogEntry.Student(s.display_name, s.user_name.lower()) for s in info.students])


def load_log(path: Path) -> list[LogEntry]:
    return [LogEntry.deserialize(line) for line in path.read_text(encoding='utf-8').splitlines()]


class DivisionLog:
    def __init__(self):
        self.division: dict[str, list[LogEntry]] = dict()
        self.grader: dict[int, str] = dict()

    def __iter__(self):
        return self.division.items().__iter__()

    def get_entries(self, grader_id: str) -> list[LogEntry]:
        return self.division[grader_id]

    def has_entity_id(self, entity_id: int) -> bool:
        return self.get_grader(entity_id) is not None

    def get_grader(self, entity_id: int) -> Optional[str]:
        return self.grader.get(entity_id, None)

    @staticmethod
    def read(path: Path) -> DivisionLog:
        log = DivisionLog()
        for log_path in path.iterdir():
            if not log_path.is_file() or log_path.suffix != '.log':
                continue

            grader_id = log_path.stem
            log_entries = load_log(log_path)
            log.division[grader_id] = log_entries
            for entry in log_entries:
                log.grader[entry.entity_id] = grader_id

        return log


class Division:
    division: dict[str, list[SubmissionInfo]]

    def __init__(self, graders: Iterable[str]):
        self.division = {grader: [] for grader in graders}

    def __iter__(self):
        return self.division.items().__iter__()

    def __getitem__(self, grader_id: str) -> list[SubmissionInfo]:
        return self.division.get(grader_id, [])

    def graders(self) -> list[str]:
        return list(self.division.keys())

    def assign_to(self, grader_id: str, submission: SubmissionInfo):
        self.division[grader_id].append(submission)

    def assign_many_to(self, grader_id: str, submissions: list[SubmissionInfo]):
        self.division[grader_id].extend(submissions)

    def assign_randomly(self, submission: SubmissionInfo):
        grader_id = random.choice(list(self.division.keys()))
        self.assign_to(grader_id, submission)

    def write_logs(self, path: Path):
        path.mkdir(parents=True, exist_ok=True)

        for grader_id, submissions in self.division.items():
            log_path = path / f'{grader_id}.log'

            with open(log_path, 'w', encoding='utf-8') as f:
                for submission in submissions:
                    f.write(f'{LogEntry.from_info(submission).serialize()}\n')


class Divider(ABC):
    @abstractmethod
    def initialize(self, assignment: AssignmentInfo) -> bool:
        pass

    def divide(self, assignment: AssignmentInfo) -> Division:
        pass


class RandomDivider(Divider):
    def __init__(self, config: Config):
        self.config = config

    def initialize(self, assignment: AssignmentInfo) -> bool:
        return True

    def divide(self, assignment: AssignmentInfo) -> Division:
        assignment_config = self.config.assignments[assignment.identifier]
        grader_weights = assignment_config.division.grader_weights
        division = Division(grader_weights.keys())

        # Normalize weights so that they sum to 1.
        weight_sum = sum(grader_weights.values())
        for grader_id, weight in grader_weights.items():
            grader_weights[grader_id] = weight / weight_sum

        # Make copy of the list of submissions, and randomly shuffle it.
        total_submissions = len(assignment.submissions)
        to_divide = list(assignment.submissions)
        random.shuffle(to_divide)

        # Assign submissions from the shuffled list based on normalized weights.
        for grader_id, weight in grader_weights.items():
            # Add a random number between 0.0 and 1.0, then floor to do probabilistic rounding.
            # If the 'target' is 10.4, this means 40% of the time we get 11, and 60% of the time 10.
            # This should produce more accurate weight based divisions on average, compared to regular rounding/floor/ceiling.
            target = int(weight * total_submissions + random.random())
            num = min(target, len(to_divide))
            division.assign_many_to(grader_id, to_divide[:num])
            to_divide = to_divide[num:]

        # Mop up by dividing any remaining submissions randomly in case we did not get an exact division.
        for submission in to_divide:
            division.assign_randomly(submission)

        return division


class PersistentDivider(Divider):
    def __init__(self, config: Config, data_path: Path):
        self.config = config
        self.data_path = data_path

    def initialize(self, assignment: AssignmentInfo) -> bool:
        return True

    @staticmethod
    def _save_persist_list(path: Path, submissions: list[SubmissionInfo]):
        path.write_text('\n'.join(s.folder_name for s in submissions), encoding='utf-8')

    @staticmethod
    def _load_persist_list(path: Path) -> list[str]:
        if path.is_file():
            return path.read_text(encoding='utf-8').splitlines()
        else:
            return []

    def divide(self, assignment: AssignmentInfo) -> Division:
        assignment_config = self.config.assignments[assignment.identifier]
        grader_weights = assignment_config.division.grader_weights
        category = assignment_config.division.group_category_name
        category_path = self.data_path / 'divisions' / category

        # Normalize weights so that they sum to 1.
        weight_sum = sum(grader_weights.values())
        for grader_id, weight in grader_weights.items():
            grader_weights[grader_id] = weight / weight_sum

        if not category_path.is_dir():
            # No prior division exists, so create a random one now, based on same graders and weights.
            random_divider = RandomDivider(self.config)
            division = random_divider.divide(assignment)
        else:
            # Load previously created persist lists, transform it into a mapping of `folder_name` to `grader_id`.
            graders = grader_weights.keys()
            persist = {grader_id: self._load_persist_list(category_path / grader_id) for grader_id in graders}
            to_grader: dict[str, str] = dict()
            for grader_id, submissions in persist.items():
                for folder_name in submissions:
                    to_grader[folder_name] = grader_id
            division = Division(graders)

            # Partition submissions into those already assigned to a grader, and those not yet assigned to one.
            assigned: list[SubmissionInfo] = []
            unassigned: list[SubmissionInfo] = []
            for submission in assignment.submissions:
                (assigned if submission.folder_name in to_grader else unassigned).append(submission)

            # Assigned the already assigned submissions to their prior grader.
            for submission in assigned:
                division.assign_to(to_grader[submission.folder_name], submission)

            # Assign unassigned submissions to graders, taking weights and assigned submission count in division into account.
            for submission in unassigned:
                # Get grader based on grader the furthest away from target workload.
                grader_id, _ = max(
                    [(grader_id, weight * len(assignment.submissions) - len(division[grader_id])) for grader_id, weight
                     in grader_weights.items()], key=itemgetter(1))
                division.assign_to(grader_id, submission)

        # Save division to persist lists.
        category_path.mkdir(parents=True, exist_ok=True)
        for grader_id, submissions in division:
            self._save_persist_list(category_path / grader_id, submissions)

        return division


class BrightspaceDivider(Divider):
    def __init__(self, api: bsapi.BSAPI, config: Config):
        self.api = api
        self.config = config
        self.user_to_grader: dict[int, tuple[str, str]] = dict()

    def initialize(self, assignment: AssignmentInfo) -> bool:
        assignment_config = self.config.assignments[assignment.identifier]
        helper = bsapi.helper.APIHelper(self.api)

        group_category = helper.find_group_category(assignment.course.org_unit.id,
                                                    assignment_config.division.group_category_name)
        groups = self.api.get_groups(assignment.course.org_unit.id, group_category.group_category_id)

        # TODO: Check if Brightspace data is sane etc

        # Build mapping of student to grader based on grading groups.
        for group in groups:
            grader_id = assignment_config.division.group_mapping[group.name]
            for user_id in group.enrollments:
                if user_id in self.user_to_grader:
                    # Student is already in a grading group, so it is in multiple groups.
                    student = assignment.users[user_id]
                    prior_grader, prior_group = self.user_to_grader[user_id]
                    logger.warning('Student %s is in multiple grading groups (%s graded by %s, and %s graded by %s)',
                                   student.display_name, prior_group, prior_grader, group.name, grader_id)
                else:
                    self.user_to_grader[user_id] = (grader_id, group.name)

        # Check if all students are in a grading group.
        missing_students = [student for user_id, student in assignment.users.items() if
                            user_id not in self.user_to_grader]

        for student in missing_students:
            logger.warning('Student %s is not in any grading group', student.display_name)

        return True

    def divide(self, assignment: AssignmentInfo) -> Division:
        assignment_config = self.config.assignments[assignment.identifier]
        graders = set(assignment_config.division.group_mapping.values())
        division = Division(graders)

        for submission in assignment.submissions:
            submitter_id = int(submission.submitted_by.identifier)

            # Ensure a grader exists for this submission.
            if submitter_id not in self.user_to_grader:
                available_graders: set[str] = set()

                # No grader for the submitter of this submission, so look at partners if any exist.
                for student in submission.students:
                    # Skip submitter itself.
                    if student.identifier == submission.submitted_by.identifier:
                        continue

                    # Check if the partner has a grader, and if so add it to the set of possible graders.
                    partner_grader, _ = self.user_to_grader.get(int(student.identifier), (None, None))
                    if partner_grader:
                        available_graders.add(partner_grader)

                # If no partner graders are available, then consider every grader as a possible grader.
                had_partner_grader = len(available_graders) > 0
                if not available_graders:
                    available_graders = graders

                # Select a grader randomly from the set of possible graders.
                selected_grader = random.choice(list(available_graders))
                self.user_to_grader[submitter_id] = (selected_grader, '')
                if had_partner_grader:
                    if len(available_graders) == 1:
                        logger.warning('Student %s is not in any grading group, selected %s due to partner',
                                       submission.submitted_by.display_name, selected_grader)
                    else:
                        logger.warning('Student %s is not in any grading group, selected %s at random due to partner',
                                       submission.submitted_by.display_name, selected_grader)
                else:
                    logger.warning('Student %s is not in any grading group, selected %s at random',
                                   submission.submitted_by.display_name, selected_grader)

            # Find grader and assign submission to that grader.
            grader_id, _ = self.user_to_grader[submitter_id]
            division.assign_to(grader_id, submission)

        return division


class Notifier:
    def __init__(self, dist_path: Path, config: Config, smtp_config: SMTPConfig,
                 assignment_info: AssignmentInfo, division: Division,
                 progress_reporter: ProgressReporter = None):
        self.dist_path = dist_path
        self.config = config
        self.smtp_config = smtp_config
        self.assignment_info = assignment_info
        self.division = division
        self.progress_reporter = progress_reporter
        self.smtp: Optional[smtplib.SMTP] = None

    def create_notifications(self):
        distribute = self.config.distribute
        course_name = self.assignment_info.course.org_unit.name
        assignment_name = self.assignment_info.assignment.name
        assignment_id = self.assignment_info.identifier

        for grader_id, submissions in self.division:
            grader_info = self.config.graders[grader_id]
            num_submissions = len(submissions)

            # Create target file path, and ensure parent folders exists.
            parent_path = self.dist_path.resolve() / assignment_id
            archive_path = parent_path / f'{assignment_id}-{grader_id}.7z'
            message_path = parent_path / f'{assignment_id}-{grader_id}.message'
            password_path = parent_path / f'{assignment_id}-{grader_id}.password'
            parent_path.mkdir(parents=True, exist_ok=True)

            password = password_path.read_text(encoding='utf-8') if password_path.exists() else None

            with open(message_path, 'w', encoding='utf-8') as f:
                f.write(
                    f'You have {num_submissions} submission{"s" if num_submissions != 1 else ""} to grade for {course_name} - {assignment_name}.\n')
                f.write('\n')
                if num_submissions == 0:
                    f.write('As you have nothing to grade, no submissions archive was created.\n')
                else:
                    f.write(f'password: {password}\n')
                    # TODO: This is specific to SCP uploads.
                    # If we end up supporting different modes then perhaps an Uploader instance has to generate the text below?
                    f.write('\n')
                    f.write('Grab your submissions using the following command:\n')
                    f.write(
                        f'    scp {grader_info.distribute_username}@{distribute.host}:{distribute.share}/{assignment_id}/{archive_path.name} ./\n')
                    f.write('Then extract it using the following command:\n')
                    f.write(f'    7za x -o{assignment_id} -p{password} {archive_path.name} > /dev/null\n')

    def initialize(self) -> bool:
        try:
            self.smtp = smtplib.SMTP(self.smtp_config.host, self.smtp_config.port)
            self.smtp.starttls()
            self.smtp.login(self.smtp_config.username, self.smtp_config.password)
            return True
        except smtplib.SMTPException as e:
            self.smtp = None
            logger.fatal('SMTP exception during connection establishment: %s', type(e).__name__)
            return False

    def _send_mail(self, subject: str, content: str, to: str):
        msg = email.message.EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.smtp_config.from_
        msg['To'] = to
        msg.set_content(content)

        try:
            self.smtp.send_message(msg)
        except smtplib.SMTPException as e:
            logger.error('SMTP exception while sending email to %s: %s', to, type(e).__name__)

    def send_notifications(self):
        assert self.smtp is not None, 'SMTP client not initialized correctly'

        course_name = self.assignment_info.course.org_unit.name
        assignment_name = self.assignment_info.assignment.name
        assignment_id = self.assignment_info.identifier
        subject = f'{course_name}: {assignment_name}'
        graders = len(self.division.graders())

        for idx, grader_id in enumerate(self.division.graders()):
            if self.progress_reporter:
                self.progress_reporter.start(idx + 1, graders, grader_id)

            mail_to = self.config.graders[grader_id].distribute_email
            message_path = self.dist_path / assignment_id / f'{assignment_id}-{grader_id}.message'
            message_contents = message_path.read_text(encoding='utf-8')

            self._send_mail(subject, message_contents, mail_to)

        if self.progress_reporter:
            self.progress_reporter.finish(graders)

    def shutdown(self):
        if self.smtp is not None:
            try:
                self.smtp.quit()
            except (OSError, SMTPException):
                pass
            self.smtp = None


class Uploader:
    def __init__(self, dist_path: Path, logs_path: Path, config: Config):
        self.dist_path = dist_path
        self.logs_path = logs_path
        self.config = config

    def upload(self, assignment_id: str) -> bool:
        distribute = self.config.distribute
        assignment_path = self.dist_path / assignment_id
        assert assignment_path.exists(), f'Assignment path does not exist, wrong assignment id "{assignment_id}"?'

        # ssh DISTRIBUTER@HOST mkdir -p SHARE/<assignment_id>
        args = ['ssh', f'{distribute.distributor}@{distribute.host}', 'mkdir', '-p',
                f'{distribute.share}/{assignment_id}']
        cp = subprocess.run(args, shell=False, check=False, capture_output=False)
        if cp.returncode != 0:
            logger.fatal('Failed to create folder on distribution share, exit code %d', cp.returncode)
            return False

        # ssh DISTRIBUTER@HOST mkdir -p SHARE/logs/<assignment_id>
        args = ['ssh', f'{distribute.distributor}@{distribute.host}', 'mkdir', '-p',
                f'{distribute.share}/logs/{assignment_id}']
        cp = subprocess.run(args, shell=False, check=False, capture_output=False)
        if cp.returncode != 0:
            logger.fatal('Failed to create logs folder on distribution share, exit code %d', cp.returncode)
            return False

        # scp <assignment_id>/*.7z DISTRIBUTER@HOST:SHARE/<assignment_id>/
        args = f'scp {assignment_id}/*.7z {distribute.distributor}@{distribute.host}:{distribute.share}/{assignment_id}/'
        cp = subprocess.run(args, shell=True, check=False, capture_output=False, cwd=self.dist_path)
        if cp.returncode != 0:
            logger.fatal('Failed to copy grader archives to distribution share, exit code %d', cp.returncode)
            return False

        # scp <assignment_id>/*.log DISTRIBUTER@HOST:SHARE/logs/<assignment_id>/
        args = f'scp {assignment_id}/*.log {distribute.distributor}@{distribute.host}:{distribute.share}/logs/{assignment_id}/'
        cp = subprocess.run(args, shell=True, check=False, capture_output=False, cwd=self.logs_path)
        if cp.returncode != 0:
            logger.fatal('Failed to copy logs to distribution share, exit code %d', cp.returncode)
            return False

        return True


class Downloader:
    def __init__(self, api: bsapi.BSAPI, config: Config, root_path: Path, progress_reporter: ProgressReporter = None):
        self.api = api
        self.config = config
        self.root_path = root_path
        self.submissions_path = root_path / 'stage' / 'submissions'
        self.progress_reporter = progress_reporter

    def download_submission(self, org_unit_id: int, folder_id: int, submission: bsapi.types.EntityDropBox,
                            users: dict[int, bsapi.types.User], groups: dict[int, bsapi.types.GroupData]) -> Optional[
        SubmissionInfo]:
        entity_id = submission.entity.entity_id
        entity_type = submission.entity.entity_type
        name = submission.entity.get_name()

        if entity_type == 'Group':
            folder_name = name.replace(' ', '-').lower()
            students = [users[user_id] for user_id in groups[entity_id].enrollments]
        else:
            folder_name = users[entity_id].user_name.lower()
            students = [users[entity_id]]

        # Find the latest submission if multiple exist, and default to None if no submission was made.
        latest_submission = max(submission.submissions, key=attrgetter('submission_date'), default=None)
        total_size = sum(map(lambda f_: f_.size, latest_submission.files)) if latest_submission else 0
        logger.info('Downloading submission from %s (%s)', name, format_filesize(total_size))

        if not latest_submission:
            logger.info('Skipping as no submission was made')
            return None

        submission_path = self.submissions_path.joinpath(folder_name)
        submission_path.mkdir(parents=True, exist_ok=True)

        for file in latest_submission.files:
            dest_path = submission_path.joinpath(file.file_name)
            contents = self.api.get_dropbox_folder_submission_file(org_unit_id, folder_id, latest_submission.id,
                                                                   file.file_id)

            with open(dest_path, 'wb') as f:
                f.write(contents)

        return SubmissionInfo(
            entity_id=entity_id,
            entity_type=entity_type,
            submitted_by=users[int(latest_submission.submitted_by.identifier)],
            submitted_at=latest_submission.submission_date,
            submission_id=latest_submission.id,
            folder_name=folder_name,
            comment=latest_submission.comment.text,
            group_name=submission.entity.name,
            students=students
        )

    def download_submissions(self, org_unit_id: int, folder_id: int, ignored_submissions: list[str],
                             users: dict[int, bsapi.types.User], groups: dict[int, bsapi.types.GroupData]) -> list[
        SubmissionInfo]:
        logger.info('Obtaining Brightspace dropbox folder submission metadata')
        submissions = self.api.get_dropbox_folder_submissions(org_unit_id, folder_id)
        submissions_info = []

        for idx, submission in enumerate(submissions):
            if self.progress_reporter:
                self.progress_reporter.start(idx + 1, len(submissions), submission.entity.get_name())

            if submission.entity.get_name() in ignored_submissions:
                logger.info('Ignoring submission from %s', submission.entity.get_name())
                continue

            info = self.download_submission(org_unit_id, folder_id, submission, users, groups)
            if info is not None:
                submissions_info.append(info)

        if self.progress_reporter:
            self.progress_reporter.finish(len(submissions))
        return submissions_info

    def download(self, assignment_id: str) -> Optional[AssignmentInfo]:
        if assignment_id not in self.config.assignments:
            logger.fatal('No assignment with id "%s" exists', assignment_id)
            return None

        api_helper = bsapi.helper.APIHelper(self.api)
        assignment_config = self.config.assignments[assignment_id]

        course = api_helper.find_course_by_name(self.config.course_name)
        assignment = api_helper.find_assignment(course.org_unit.id, assignment_config.name)
        users = {int(user.user.identifier): user.user for user in
                 self.api.get_users(course.org_unit.id)}
        groups = {group.group_id: group for group in self.api.get_groups(course.org_unit.id, assignment.group_type_id)
                  if group.enrollments} if assignment.group_type_id is not None else None

        if assignment.grade_item_id is None:
            logger.fatal('Assignment "%s" is not associated with a grade object', assignment.name)
            # TODO we should just continue, but make sure to indicate that this assignment is not graded
            return None
        if assignment.due_date and assignment.due_date > datetime.datetime.now(datetime.timezone.utc):
            logger.warning('Due date of assignment "%s" has not yet passed', assignment.name)

        grade_object = self.api.get_grade_object(course.org_unit.id, assignment.grade_item_id)
        grade_scheme = self.api.get_grade_scheme(course.org_unit.id, grade_object.grade_scheme_id) # TODO this fails if no grading book scheme is set, which is perfectly possible

        if grade_object.grade_type not in ['SelectBox', 'Numeric']:
            logger.fatal('Assignment "%s" has an unsupported grade type "%s"', assignment.name, grade_object.grade_type)
            return None
        if grade_object.grade_type == 'Numeric' and assignment.assessment.score_denominator is None:
            logger.fatal('Assignment "%s" has Numeric grade type but no Score Out Of field set', assignment.name)
            return None

        submissions = self.download_submissions(course.org_unit.id, assignment.id,
                                                assignment_config.ignored_submissions, users, groups)

        return AssignmentInfo(assignment_id, course, assignment, users, groups, submissions, grade_object, grade_scheme)
