import argparse
import re

from .error_log_file import ErrorLogFile
from .profile import Profile
from .summary_line import SummaryLine
from .text_output import TextOutput


def parse_args():
    """Parse args from command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('log')
    parser.add_argument('-a', '--all', action="store_true", help="report status of all profiles including passing ones.")
    parser.add_argument('-e', '--errors', action="store_true", help="report error messages.")
    parser.add_argument('-s', '--summary', action="store_true", help="report only the summary.")
    return parser.parse_args()


class DQCReport:

    def __init__(self, log_file):
        self.log = ErrorLogFile(log_file)
        self.profiles = {}

        self.create_profiles(self.log.summary)
        self.capture_errors(self.log.error_lines)
    
    def create_profiles(self, summary):
        for line in summary.split('\n'):
            if not line:
                continue

            summary_line = SummaryLine(line)

            if summary_line.profile not in self.profiles:
                profile = Profile(summary_line.profile)
                self.profiles[summary_line.profile] = profile
                profile.set_split_key(summary_line.split_key)
            else:
                profile = self.profiles[summary_line.profile]
            
            profile.add_summary_line(summary_line)
        
        # Order summary lines
        for profile in self.profiles.values():
            profile.order_summary_lines()

    def capture_errors(self, error_lines):

        for profile in self.profiles.values():
            for line in profile.failed_lines:
                pattern = rf"DQC-{line.process_id}/{line.max_cores}:FAILED\s(.*)\sChecker for profile {profile.name}"
                err_messages = list(set(filter(lambda x: bool(re.search(pattern, x)), error_lines)))
                line.err_messages = err_messages
                line.failed_checker = list(set([re.search(pattern, x).group(1) for x in err_messages]))

    def show(self, **kwargs):
        output = TextOutput(
            self.profiles,
            report_only_summary=kwargs.get('summary', False),
            report_passing_profiles=kwargs.get('all', False),
            report_error_messages=kwargs.get('errors', False),
        )
        output.show()


def main():
    args = parse_args()
    dqc_report = DQCReport(args.log)
    dqc_report.show(
        all=args.all,
        errors=args.errors,
        summary=args.summary
    )


if __name__ == '__main__':
    main()
