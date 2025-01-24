from abc import ABC, abstractmethod
from dataclasses import dataclass
import datetime
import email
import logging
import shutil
import smtplib
from typing import Callable, Optional

import bsapi
import bsapi.helper
import bsapi.types

import bsscripts
import bsscripts.distribute
from bsscripts.distribute.passes import AddGraderFilesPass, CreateFeedbackTemplatePass, CreateGraderArchivesPass, \
    CreateGraderConfigPass, CreateGradingInstructionsPass, DocxToPdfPass, ExtractArchivesPass, FixFilePermissionsPass, \
    FlattenPass, GraderPass, InjectFilesPass, InjectGraderFilesPass, MoveToGraderPass, NOPPass, RemoveFilesPass, \
    SmartFlattenPass, SubmissionsPass
from bsscripts.utils import TablePrinter, format_datetime, format_timedelta, is_match, to_local_time

logger = logging.getLogger(__name__)


class Command(ABC):
    @dataclass
    class Argument:
        name: str
        help: str
        validator: Optional[Callable[[str], bool]]

    def __init__(self, prefix: list[str], description: str):
        self.prefix = prefix
        self.description = description
        self.positional_args: list[Command.Argument] = []
        self.flag_args: list[Command.Argument] = []
        self.positional_values: list[str] = []
        self.flag_values: dict[str, bool] = dict()
        self.args: list[str] = []

    def prefix_starts_with(self, prefix: list[str]) -> bool:
        return len(prefix) <= len(self.prefix) and self.prefix[:len(prefix)] == prefix

    def add_positional_arg(self, name: str, help_: str, validator: Callable[[str], bool] = None):
        self.positional_args.append(Command.Argument(name, help_, validator))

    def add_flag_arg(self, name: str, help_: str):
        assert not any(f.name == name for f in self.flag_args), 'flag already exists'

        self.flag_args.append(Command.Argument(name, help_, None))

    def get_positional_arg(self, index: int) -> str:
        assert 0 <= index < len(self.positional_values), 'invalid index'

        return self.positional_values[index]

    def get_flag_arg(self, name: str) -> bool:
        assert name in self.flag_values, 'unknown flag'

        return self.flag_values[name]

    def parse_args(self, args: list[str]) -> bool:
        self.args = args

        self.positional_values = []
        for idx, arg in enumerate(self.positional_args):
            if idx >= len(args):
                logger.error('Missing positional argument "%s" at index %d', arg.name, idx)
                return False
            if arg.validator and not arg.validator(args[idx]):
                logger.error('Value "%s" is not valid for argument "%s"', args[idx], arg.name)
                return False
            self.positional_values.append(args[idx])

        leftover_args = args[len(self.positional_args):]
        self.flag_values = {f.name: (f'--{f.name}' in leftover_args) for f in self.flag_args}

        return True

    @abstractmethod
    def execute(self):
        pass

    def execute_with_args(self, args: list[str]):
        if self.parse_args(args):
            self.execute()


class AppCommand(Command, ABC):
    def __init__(self, prefix: list[str], description: str):
        super().__init__(prefix, description)
        from bsscripts.app import App
        self.app = App.get_instance()


class APICommand(AppCommand):
    def __init__(self, prefix: list[str], description: str):
        super().__init__(prefix, description)
        self.api = self.app.api
        self.api_helper = self.app.api_helper
        self.config = self.app.config

    @abstractmethod
    def execute_api(self):
        pass

    def execute(self):
        try:
            self.execute_api()
        except bsapi.APIError as e:
            logger.error('Failed to execute command "%s" due to API error: %s', ' '.join(self.prefix), e.cause)


class ListGradersCommand(AppCommand):
    def __init__(self):
        super().__init__(['list', 'graders'], 'List all graders')

    def execute(self):
        table = TablePrinter()
        table.add_column('identifier')
        table.add_column('name')
        table.add_column('contact')
        table.add_column('username')
        table.add_column('distribute')

        for grader_id, grader in self.app.config.graders.items():
            table.add_row(
                [grader_id, grader.name, grader.contact_email, grader.distribute_username, grader.distribute_email])

        table.print()


class ListAssignmentsCommand(APICommand):
    def __init__(self):
        super().__init__(['list', 'assignments'], 'List all assignments')

    def execute_api(self):
        table = TablePrinter()
        table.add_column('identifier')
        table.add_column('name')
        table.add_column('group')
        table.add_column('grade')
        table.add_column('due')
        table.add_column('submitted')
        table.add_column('graded')

        org_unit_id = self.api_helper.find_course_by_name(self.config.course_name).org_unit.id
        dropbox_folders = {folder.name: folder for folder in self.api.get_dropbox_folders(org_unit_id)}
        group_categories = {category.group_category_id: category for category in
                            self.api.get_group_categories(org_unit_id)}

        for identifier, assignment in self.config.assignments.items():
            dropbox = dropbox_folders[assignment.name]
            due_date = format_datetime(to_local_time(dropbox.due_date)) if dropbox.due_date else '<None>'
            group_category_name = group_categories[
                dropbox.group_type_id].name if dropbox.group_type_id is not None else '<Individual>'
            grade_name = self.api.get_grade_object(org_unit_id,
                                                   dropbox.grade_item_id).name if dropbox.grade_item_id else '<None>'
            submitted = f'{dropbox.total_users_with_submissions}/{dropbox.total_users}'
            graded = f'{dropbox.total_users_with_feedback}/{dropbox.total_users_with_submissions}'

            table.add_row([identifier, assignment.name, group_category_name, grade_name, due_date, submitted, graded])

        table.print()


class ListDeadlinesCommand(APICommand):
    def __init__(self):
        super().__init__(['list', 'deadlines'], 'List all deadlines')

    def execute_api(self):
        table = TablePrinter()
        table.add_column('identifier')
        table.add_column('name')
        table.add_column('deadline')
        table.add_column('distributed')

        org_unit_id = self.api_helper.find_course_by_name(self.config.course_name).org_unit.id
        dropbox_folders = {folder.name: folder for folder in self.api.get_dropbox_folders(org_unit_id)}

        for identifier, assignment in self.config.assignments.items():
            dropbox = dropbox_folders[assignment.name]
            utc_now = datetime.datetime.now(datetime.timezone.utc)

            if dropbox.due_date is None:
                deadline = '<None>'
            elif dropbox.due_date < utc_now:
                deadline = format_timedelta(utc_now - dropbox.due_date) + ' ago'
            else:
                deadline = 'in ' + format_timedelta(dropbox.due_date - utc_now)

            distributed = (self.app.root_path / 'distributions' / identifier).is_dir()
            table.add_row([identifier, assignment.name, deadline, 'yes' if distributed else 'no'])

        table.print()


class CheckGradingProgressCommand(APICommand):
    @dataclass
    class Progress:
        draft: int
        published: int
        assigned: int

    def __init__(self):
        super().__init__(['check', 'grading', 'progress'], 'Check the grading progress of an assignment')
        self.add_positional_arg('assignment-id', 'The assignment identifier', self.app.is_valid_assignment_id)

    def execute_api(self):
        assignment_id = self.get_positional_arg(0)
        assignment_config = self.config.assignments[assignment_id]
        org_unit_id = self.api_helper.find_course_by_name(self.config.course_name).org_unit.id
        assignment = self.api_helper.find_assignment(org_unit_id, assignment_config.name)
        submissions = self.api.get_dropbox_folder_submissions(org_unit_id, assignment.id)
        division_log = self.app.load_division_log(assignment_id)

        table = TablePrinter()
        table.add_column('grader')
        table.add_column('draft')
        table.add_column('published')
        table.add_column('assigned')
        table.add_column('completed')

        progress = {grader: CheckGradingProgressCommand.Progress(0, 0, 0) for grader in self.config.graders}

        for submission in submissions:
            if submission.status == bsapi.types.ENTITY_DROPBOX_STATUS_UNSUBMITTED:
                continue
            if not division_log.has_entity_id(submission.entity.entity_id):
                continue

            graded_by = division_log.get_grader(submission.entity.entity_id)
            progress[graded_by].assigned += 1

            if submission.status == bsapi.types.ENTITY_DROPBOX_STATUS_PUBLISHED:
                progress[graded_by].published += 1
            elif submission.status == bsapi.types.ENTITY_DROPBOX_STATUS_DRAFT:
                progress[graded_by].draft += 1

        for grader_id, progress in progress.items():
            if progress.assigned == 0:
                continue

            if progress.published == progress.assigned:
                completed = 'yes'
            elif progress.draft + progress.published == progress.assigned:
                completed = 'draft'
            else:
                completed = 'no'

            table.add_row(
                [self.config.graders[grader_id].name, progress.draft, progress.published, progress.assigned, completed])

        table.sort_rows()
        table.print()


class ListUngradedCommand(APICommand):
    def __init__(self):
        super().__init__(['list', 'ungraded'], 'List all ungraded submissions for an assignment')
        self.add_positional_arg('assignment-id', 'The assignment identifier', self.app.is_valid_assignment_id)

    def execute_api(self):
        assignment_id = self.get_positional_arg(0)
        assignment_config = self.config.assignments[assignment_id]
        org_unit_id = self.api_helper.find_course_by_name(self.config.course_name).org_unit.id
        assignment = self.api_helper.find_assignment(org_unit_id, assignment_config.name)
        submissions = self.api.get_dropbox_folder_submissions(org_unit_id, assignment.id)
        division_log = self.app.load_division_log(assignment_id)

        table = TablePrinter()
        table.add_column('name')
        table.add_column('grader')

        for submission in submissions:
            if submission.status != bsapi.types.ENTITY_DROPBOX_STATUS_SUBMITTED:
                continue

            graded_by = division_log.get_grader(submission.entity.entity_id)
            if graded_by is None:
                graded_by = '<None>'

            table.add_row([submission.entity.get_name(), graded_by])

        table.sort_rows(columns=[1])
        table.print()


class ListUndistributedCommand(APICommand):
    def __init__(self):
        super().__init__(['list', 'undistributed'], 'List all undistributed submissions')

    def execute_api(self):
        org_unit_id = self.api_helper.find_course_by_name(self.config.course_name).org_unit.id
        assignments = {folder.name: folder for folder in self.api.get_dropbox_folders(org_unit_id)}

        table = TablePrinter()
        table.add_column('name')
        table.add_column('assignment')

        for assignment_id, assignment_config in self.config.assignments.items():
            if not self.app.has_distributed(assignment_id):
                continue

            assignment = assignments[assignment_config.name]
            submissions = self.api.get_dropbox_folder_submissions(org_unit_id, assignment.id)
            division_log = self.app.load_division_log(assignment_id)

            for submission in submissions:
                if submission.status == bsapi.types.ENTITY_DROPBOX_STATUS_UNSUBMITTED:
                    continue

                if not division_log.has_entity_id(submission.entity.entity_id):
                    table.add_row([submission.entity.get_name(), assignment.name])

        table.sort_rows(columns=[1])
        table.print()


class ListDivisionCommand(AppCommand):
    def __init__(self):
        super().__init__(['list', 'division'], 'List the grading division made for an assignment')
        self.add_positional_arg('assignment-id', 'The assignment identifier', self.app.is_valid_assignment_id)

    def execute(self):
        assignment_id = self.get_positional_arg(0)

        table = TablePrinter()
        table.add_column('entity id')
        table.add_column('name')
        table.add_column('students')
        table.add_column('grader')

        division_log = self.app.load_division_log(assignment_id)
        for grader_id, entries in division_log:
            grader_name = self.app.config.graders[grader_id].name
            for entry in entries:
                students_str = ','.join(f'{s.name} ({s.username})' for s in entry.students)
                table.add_row([entry.entity_id, entry.folder_name, students_str, grader_name])

        table.sort_rows(columns=[3])
        table.print()


class FindGraderCommand(AppCommand):
    def __init__(self):
        super().__init__(['find', 'grader'], 'Find the grader for a search term')
        self.add_positional_arg('search', 'The search term')

    def execute(self):
        search = self.get_positional_arg(0)

        table = TablePrinter()
        table.add_column('entity id')
        table.add_column('name')
        table.add_column('students')
        table.add_column('grader')
        table.add_column('assignment')

        for assignment_id, assignment in self.app.config.assignments.items():
            if not self.app.has_distributed(assignment_id):
                continue

            division_log = self.app.load_division_log(assignment_id)
            for grader_id, entries in division_log:
                grader_name = self.app.config.graders[grader_id].name
                for entry in entries:
                    students_str = ','.join(f'{s.name} ({s.username})' for s in entry.students)

                    if is_match(search, entry.folder_name) or is_match(search, students_str):
                        table.add_row([entry.entity_id, entry.folder_name, students_str, grader_name, assignment.name])

        table.sort_rows(columns=[4])
        table.print()


class CheckGradingGroupsCommand(APICommand):
    def __init__(self):
        super().__init__(['check', 'grading', 'groups'], 'Check the grading groups of an assignment')
        self.add_positional_arg('assignment-id', 'The assignment identifier', self.app.is_valid_assignment_id)

    def execute_api(self):
        assignment_id = self.get_positional_arg(0)
        assignment_config = self.config.assignments[assignment_id]

        if assignment_config.division.method != 'brightspace':
            return

        # Grab all required Brightspace metadata once to avoid making further API calls.
        org_unit_id = self.api_helper.find_course_by_name(self.config.course_name).org_unit.id
        grading_group_category = self.api_helper.find_group_category(org_unit_id,
                                                                     assignment_config.division.group_category_name)
        assignment = self.api_helper.find_assignment(org_unit_id, assignment_config.name)
        users = {int(user.user.identifier): user.user for user in
                 self.api.get_users(org_unit_id, role_id=bsapi.ROLE_STUDENT)}
        groups = {group.group_id: group for group in self.api.get_groups(org_unit_id,
                                                                         assignment.group_type_id)} if assignment.group_type_id is not None else None
        grading_groups = {group.group_id: group for group in
                          self.api.get_groups(org_unit_id, grading_group_category.group_category_id)}

        # Build a map of user identifier to a list of grading groups they are enrolled in, if any.
        user_to_grading_groups: dict[int, list[int]] = {user_id: [] for user_id in users}
        for grading_group in grading_groups.values():
            for user_id in grading_group.enrollments:
                user_to_grading_groups[user_id].append(grading_group.group_id)

        # If this is a group assignment, build a map of user identifier to assignment group.
        user_to_group: dict[int, int] = dict()
        if groups is not None:
            for group in groups.values():
                for user_id in group.enrollments:
                    user_to_group[user_id] = group.group_id

        # Loop over all users, and check if they are in exactly one grading group.
        for user_id, in_grading_groups in user_to_grading_groups.items():
            if len(in_grading_groups) == 1:
                continue

            user = users[user_id]

            # User is either not in any grading groups, or in multiple, so show this.
            if len(in_grading_groups) == 0:
                print(f'{user.display_name} ({user.user_name.lower()}) is not in any grading group')
            elif len(in_grading_groups) > 1:
                groups_str = ', '.join(grading_groups[group_id].name for group_id in in_grading_groups)
                print(f'{user.display_name} ({user.user_name.lower()}) is in multiple grading groups: {groups_str}')

            # Check if we have a group assignment, and whether the user is in an assignment group.
            if user_id not in user_to_group:
                continue

            # We have a group assignment, and the user is part of a group, so show which one.
            group = groups[user_to_group[user_id]]
            print(f'- In assignment group {group.name}')

            # Also show information on any group partners, such as their grading group membership.
            for partner_id in group.enrollments:
                if partner_id == user_id:
                    continue

                partner = users[partner_id]
                partner_grading_groups = user_to_grading_groups[partner_id]
                print(f'- Group partner {partner.display_name} ({partner.user_name.lower()}) ', end='')
                if partner_grading_groups:
                    groups_str = ', '.join(grading_groups[group_id].name for group_id in partner_grading_groups)
                    print(f'is in grading group(s): {groups_str}')
                else:
                    print('is not in any grading group')

        # Finally, loop over all assignment groups and check whether there are any split groups.
        # A split group is one that has more than one member, and not all members are part of the same grading group(s).
        for group in groups.values():
            if len(group.enrollments) <= 1:
                continue
            if all(user_to_grading_groups[group.enrollments[0]] == user_to_grading_groups[user_id] for user_id in
                   group.enrollments):
                continue

            print(f'Group {group.name} is split over multiple grading groups')
            for user_id in group.enrollments:
                user = users[user_id]
                print(f'- Group member {user.display_name} ({user.user_name.lower()}) ', end='')

                in_grading_groups = user_to_grading_groups[user_id]
                if in_grading_groups:
                    groups_str = ', '.join(grading_groups[group_id].name for group_id in in_grading_groups)
                    print(f'is in grading group(s): {groups_str}')
                else:
                    print('is not in any grading group')


class Report(bsscripts.distribute.ProgressReporter):
    def __init__(self, step: str):
        self.step = step

    def start(self, current: int, total: int, name: str):
        print('\x1b[2K', end='')  # clear line as next line printed may be shorter
        print(f'Starting "{self.step}" for {name} [{current}/{total}]', end='\r', flush=True)

    def finish(self, total: len):
        print('\x1b[2K', end='')  # clear line as next line printed may be shorter
        print(f'Completed "{self.step}" [{total}/{total}]')


class DistributeCommand(APICommand):
    def __init__(self):
        super().__init__(['distribute'], 'Distribute an assignment')
        self.add_positional_arg('assignment-id', 'The assignment identifier', self.app.is_valid_assignment_id)
        self.add_flag_arg('no-upload', 'Do not run uploader and notifier')
        self.add_flag_arg('no-notify', 'Do not run notifier')
        self.add_flag_arg('no-confirm', 'Do not ask for confirmation before running notifier')

    def execute_api(self):
        do_not_upload = self.get_flag_arg('no-upload')
        do_not_notify = self.get_flag_arg('no-notify') or do_not_upload
        do_confirm = not self.get_flag_arg('no-confirm')

        assignment_id = self.get_positional_arg(0)
        assignment_config = self.config.assignments[assignment_id]
        root_path = self.app.root_path
        stage_path = root_path / 'stage'
        submissions_path = stage_path / 'submissions'
        graders_path = stage_path / 'graders'
        data_path = root_path / 'data'
        inject_path = data_path / 'inject'
        grader_data_path = self.app.package_data_path / 'grader'
        course_path = data_path / 'course' / self.config.course
        distributions_path = root_path / 'distributions'
        logs_path = root_path / 'logs'

        downloader = bsscripts.distribute.Downloader(self.api, self.config, root_path, Report('Download submissions'))
        assignment_info = downloader.download(assignment_id)
        if assignment_info is None:
            logger.fatal('Failed to download submissions, abandoning distribution')
            return

        division_method = assignment_config.division.method
        assert division_method in ['random', 'persistent', 'brightspace',
                                   'custom'], f'unknown division method "{division_method}"'
        match division_method:
            case 'random':
                divider = bsscripts.distribute.RandomDivider(self.config)
            case 'persistent':
                divider = bsscripts.distribute.PersistentDivider(self.config, data_path)
            case 'brightspace':
                divider = bsscripts.distribute.BrightspaceDivider(self.api, self.config)
            case 'custom':
                divider = self.app.course_plugin.get_divider(assignment_id)
            case _:
                assert False, 'Unreachable'

        if not divider.initialize(assignment_info):
            logger.fatal('Failed to initialize divider, abandoning distribution')
            return
        division = divider.divide(assignment_info)
        division.write_logs(logs_path / assignment_id)

        file_hierarchy = assignment_config.file_hierarchy
        assert file_hierarchy in ['flatten', 'smart', 'original'], f'unknown file hierarchy "{file_hierarchy}"'
        match file_hierarchy:
            case 'flatten':
                file_hierarchy_pass = FlattenPass(Report('Flatten files'))
            case 'smart':
                file_hierarchy_pass = SmartFlattenPass(Report('Smart flatten files'))
            case 'original':
                file_hierarchy_pass = NOPPass()
            case _:
                assert False, 'Unreachable'

        submission_passes: list[SubmissionsPass] = [
            ExtractArchivesPass(Report('Extract archives')),
            FixFilePermissionsPass(Report('Fix file permissions')),
            RemoveFilesPass(assignment_config, Report('Remove files')),
            DocxToPdfPass(Report('Convert DOCX to PDF')),
            file_hierarchy_pass,
            InjectFilesPass(assignment_config, inject_path, Report('Inject files')),
            CreateFeedbackTemplatePass(assignment_info, Report('Create feedback templates')),
            MoveToGraderPass(division, graders_path, Report('Move to graders'))
        ]
        grader_passes: list[GraderPass] = [
            InjectGraderFilesPass(assignment_config, inject_path, Report('Inject grader files')),
            AddGraderFilesPass(grader_data_path, course_path, Report('Add grader files')),
            CreateGraderConfigPass(division, assignment_info, self.config, self.app.api_config, assignment_config,
                                   Report('Create grader configs')),
            CreateGradingInstructionsPass(assignment_info, assignment_config, Report('Create grading instructions')),
            CreateGraderArchivesPass(distributions_path, assignment_config, Report('Create grader archives'))
        ]

        submission_passes = self.app.course_plugin.modify_submission_passes(submission_passes)
        grader_passes = self.app.course_plugin.modify_grader_passes(grader_passes)

        for pass_ in submission_passes:
            pass_.execute(submissions_path)
        for pass_ in grader_passes:
            pass_.execute(graders_path)

        if do_not_upload:
            return

        print('Uploading files to remote share...')
        uploader = bsscripts.distribute.Uploader(distributions_path, logs_path, self.config)
        if not uploader.upload(assignment_id):
            logger.fatal('Failed to upload to distribution share, abandoning distribution')
            return

        if do_not_notify:
            return

        notifier = bsscripts.distribute.Notifier(distributions_path, self.config, self.app.smtp_config, assignment_info,
                                                 division, Report('Send grader notifications'))
        notifier.create_notifications()

        # Ask before sending notifications in case it went tits up.
        # This way we can fix it and re-run the distribution before sending notifications out to the graders.
        if do_confirm and input('Send notifications? [y/n]: ').strip().lower() in ['y', 'yes']:
            if notifier.initialize():
                notifier.send_notifications()
                notifier.shutdown()
            else:
                logger.fatal('Failed to initialize notifier, no notifications sent')
            shutil.rmtree(stage_path, ignore_errors=True)
        else:
            print('Not sending notifications; stage folder still exists for debugging')


class ExitCommand(AppCommand):
    def __init__(self):
        super().__init__(['exit'], 'Exit application')

    def execute(self):
        self.app.keep_running = False


class HelpCommand(AppCommand):
    def __init__(self):
        super().__init__(['help'], 'Show help')

    def show_generic_help(self):
        table = TablePrinter()
        table.add_column('command')
        table.add_column('arguments')
        table.add_column('description')

        for command in self.app.commands:
            positional_args = ' '.join(f'<{arg.name}>' for arg in command.positional_args)
            flag_args = ' '.join(f'[--{arg.name}]' for arg in command.flag_args)
            args = ' '.join([positional_args, flag_args])

            table.add_row([' '.join(command.prefix), args, command.description])

        table.print()

        print('\nType \'help command\' to see detailed help.')

    @staticmethod
    def show_command_help(command: Command):
        print(f'Help for command: {" ".join(command.prefix)}\n')
        # TODO: Some 'long' description?
        print(command.description)
        print('\nPositional arguments (required):')
        for arg in command.positional_args:
            print(f'  <{arg.name}> - {arg.help}')
        print('\nFlag arguments (optional):')
        for arg in command.flag_args:
            print(f'  --{arg.name} - {arg.help}')
        print()

    def execute(self):
        if not self.args:
            self.show_generic_help()
        else:
            for command in self.app.commands:
                if command.prefix == self.args:
                    self.show_command_help(command)


class ResendNotificationsCommand(AppCommand):
    def __init__(self):
        super().__init__(['resend', 'notifications'], 'Resend email notifications for an assignment')
        self.add_positional_arg('assignment-id', 'The assignment identifier', self.app.is_valid_assignment_id)
        self.smtp = None

    def _send_mail(self, subject: str, content: str, to: str):
        msg = email.message.EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.app.smtp_config.from_
        msg['To'] = to
        msg.set_content(content)

        try:
            self.smtp.send_message(msg)
        except smtplib.SMTPException as e:
            logger.error('SMTP exception while sending email to %s: %s', to, type(e).__name__)

    def execute(self):
        # TODO: Perhaps tie it in to the Notifier itself?
        # At least extract some duplicated email setup/sending code into a utils.SMTPMailer class or something?
        assignment_id = self.get_positional_arg(0)
        if not self.app.has_distributed(assignment_id):
            logger.error('Assignment has not yet been distributed')
            return

        course_name = self.app.config.course_name
        assignment_name = self.app.config.assignments[assignment_id].name
        subject = f'{course_name}: {assignment_name}'

        try:
            self.smtp = smtplib.SMTP(self.app.smtp_config.host, self.app.smtp_config.port)
            self.smtp.starttls()
            self.smtp.login(self.app.smtp_config.username, self.app.smtp_config.password)
        except smtplib.SMTPException as e:
            logger.fatal('SMTP exception during connection establishment: %s', type(e).__name__)
            return

        distribution_path = self.app.root_path / 'distributions' / assignment_id
        for message_path in distribution_path.iterdir():
            if not message_path.is_file():
                continue
            if not message_path.suffix == '.message':
                continue

            grader_id = message_path.stem.removeprefix(f'{assignment_id}-')
            grader_mail = self.app.config.graders[grader_id].distribute_email
            message_contents = message_path.read_text(encoding='utf-8')

            print(f'Resending {grader_id} to {grader_mail}')
            self._send_mail(subject, message_contents, grader_mail)

        self.smtp.quit()
