
import subprocess
from src.core.logger import log

class TrapdoorDetector:
    def __init__(self):
        # Define a list of suspicious keywords.
        self.suspicious_keywords = ["backdoor", "admin_bypass", "secret_access", "trapdoor"]

    def scan_file(self, file_path: str) -> bool:
        try:
            output = subprocess.check_output(["strings", file_path], text=True)
        except Exception as e:
            log.error(f"Error scanning file {file_path}: {e}")
            return False

        for keyword in self.suspicious_keywords:
            if keyword in output:
                log.warning(f"Potential trapdoor detected in {file_path}: keyword '{keyword}' found.")
                return True

        log.info(f"No trapdoor detected in {file_path}.")
        return False


if __name__ == "__main__":
    detector = TrapdoorDetector()
    file_to_scan = "suspected_binary.exe"  # Replace with a valid file for testing.
    if detector.scan_file(file_to_scan):
        print(f"Trapdoor detected in {file_to_scan}.")
    else:
        print(f"No trapdoor detected in {file_to_scan}.")
