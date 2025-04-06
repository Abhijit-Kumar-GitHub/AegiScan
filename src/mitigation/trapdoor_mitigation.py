"""
Module: trapdoor_mitigation
Purpose: Mitigate detected trapdoors by quarantining suspicious files.
"""

import os
import shutil
from src.core.logger import log
from src.core.config import QUARANTINE_DIR


class TrapdoorMitigation:
    def __init__(self, quarantine_folder: str = QUARANTINE_DIR):
        self.quarantine_folder = quarantine_folder
        os.makedirs(self.quarantine_folder, exist_ok=True)

    def quarantine_file(self, file_path: str) -> str:
        """
        Moves the suspicious file to a quarantine directory.
        Returns a status message.
        """
        if not os.path.isfile(file_path):
            message = f"File {file_path} does not exist."
            log.error(message)
            return message

        dest = os.path.join(self.quarantine_folder, os.path.basename(file_path))
        try:
            shutil.move(file_path, dest)
            message = f"File {file_path} moved to quarantine."
            log.info(message)
            return message
        except Exception as e:
            log.error(f"Error quarantining file {file_path}: {e}")
            return f"Error quarantining file: {e}"


if __name__ == "__main__":
    mitigation = TrapdoorMitigation()
    file_to_quarantine = "suspected_binary.exe"  # Replace with an actual file during testing.
    print(mitigation.quarantine_file(file_to_quarantine))
