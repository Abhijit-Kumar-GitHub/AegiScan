# AegiScan/src/detection/trapdoor_detection.py
"""
Module: trapdoor_detection
Purpose: Detect potential trapdoors/backdoors in binaries by scanning for suspicious strings.
"""

import subprocess
from src.core.logger import log


class TrapdoorDetector:
    def __init__(self):
        # Expanded list of suspicious keywords and commands used in trapdoors/backdoors
        self.suspicious_keywords = [
            "backdoor", "admin_bypass", "secret_access", "trapdoor", "hidden_shell",
            "nc", "netcat", "telnet", "bash -i", "powershell", "cmd.exe", "sh", "zsh",
            "reverse_shell", "rev_shell", "socket.connect", "socket.bind",
            "exec(", "system(", "subprocess", "os.system", "popen",
            "rm -rf", "wget", "curl", "base64 -d", "chmod +x", "crontab", 
            "nohup", "fork", "/bin/sh", "/bin/bash", "/dev/tcp/", "/dev/udp/",
            "python -c", "perl -e", "ruby -e", "php -r", "java.lang.Runtime",
            "expect", "spawn", "setuid", "setgid", "drop shell", "listener", "port bind"
        ]

    def scan_file(self, file_path: str) -> bool:
        """
        Scans the given file using the 'strings' utility.
        Returns True if any suspicious keywords are found.
        """
        try:
            output = subprocess.check_output(["strings", file_path], text=True)
        except Exception as e:
            log.error(f"Error scanning file {file_path}: {e}")
            return False

        for keyword in self.suspicious_keywords:
            if keyword.lower() in output.lower():
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
