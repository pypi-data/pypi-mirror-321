class TextOutput:

    def __init__(self, profiles,
                 report_passing_profiles=False,
                 report_only_summary=False,
                 report_error_messages=False
                ):
        self.profiles = profiles
        self.report_passing_profiles = report_passing_profiles
        self.report_only_summary = report_only_summary
        self.report_error_messages = report_error_messages
    
    @staticmethod
    def format_string(msg, status):
        prepend = {
            "INFO": '\x1b[01;32m\x1b[K',
            "ERROR": '\x1b[01;31m\x1b[K'
        }
        append = {
            "INFO": '\x1b[m\x1b[K',
            "ERROR": '\x1b[m\x1b[K'
        }
        translated_msg = msg.replace("INFO", "PASSED").replace("ERROR", "FAILED")
        return f"{prepend.get(status, '')}{translated_msg}{append.get(status, '')}"

    def print_summary(self, profiles):
        print("Status summary for each profile:")
        for profile in profiles.values():
            print(f"Profile: {profile.name}. Status: {self.format_string(profile.status, profile.status)}")
        print("")

    def print_profile_status(self, profiles):
        print("Individual status for each process:")
        for profile in profiles.values():
            print(f"Profile: {profile.name}. Status: {self.format_string(profile.status, profile.status)} (split key: {profile.split_key})")
            lines = profile.summary_lines if self.report_passing_profiles else profile.failed_lines
            for line in lines:
                id_tag = f"{line.process_id}/{profile.used_cores}"
                failed_checkers = f"Failed: {line.failed_checker}" if line.failed_checker else ''
                print(f"{id_tag:>7} {self.format_string(line.status, line.status):<24}{line.split_key} {line.main_key_values} {failed_checkers}")  # fstatus format takes into account ANSI escape sequences
            if lines:
                print()
        print()

    def print_error_messages(self, profiles):
        print("##### Captured Error Messages: #####\n")
        for profile in profiles.values():
            if profile.status == "INFO":
                continue

            print(f"Profile: {profile.name}. Status: {self.format_string(profile.status, profile.status)}")
            for line in profile.failed_lines:
                for err_msg in line.err_messages:
                    print(f"{err_msg[:-2]}")
            print()
 
    def show(self):
        # Always report short summary
        self.print_summary(self.profiles)

        # If -s not provided, print normal output
        if not self.report_only_summary:
            self.print_profile_status(self.profiles)

            # If -e provided, print error messages
            if self.report_error_messages:
                self.print_error_messages(self.profiles)

        
    
