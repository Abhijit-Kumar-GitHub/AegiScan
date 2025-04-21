# AegiScan\tests\test_trapdoor_detection.py

import subprocess
import shutil
import pytest
from unittest.mock import patch

from src.detection.trapdoor_detection import TrapdoorDetector

# ========== MOCK-BASED UNIT TESTS ==========

def test_detects_trapdoor_keyword():
    detector = TrapdoorDetector()
    with patch("subprocess.check_output") as mock_strings:
        mock_strings.return_value = "some string with backdoor inside"
        assert detector.scan_file("dummy.exe") is True

def test_detects_no_trapdoor_keyword():
    detector = TrapdoorDetector()
    with patch("subprocess.check_output") as mock_strings:
        mock_strings.return_value = "nothing suspicious here"
        assert detector.scan_file("dummy.exe") is False

def test_handles_strings_error():
    detector = TrapdoorDetector()
    with patch("subprocess.check_output", side_effect=subprocess.CalledProcessError(1, 'strings')):
        assert detector.scan_file("missing.exe") is False

# ========== INTEGRATION TESTS USING TEMP FILE ==========

@pytest.mark.skipif(not shutil.which("strings"), reason="strings utility is not available")
def test_trapdoor_detection_real_file(tmp_path):
    file = tmp_path / "suspicious.txt"
    file.write_text("This file contains a trapdoor keyword like backdoor.")
    detector = TrapdoorDetector()
    assert detector.scan_file(str(file)) is True

@pytest.mark.skipif(not shutil.which("strings"), reason="strings utility is not available")
def test_no_trapdoor_detection_real_file(tmp_path):
    file = tmp_path / "clean.txt"
    file.write_text("Completely normal content.")
    detector = TrapdoorDetector()
    assert detector.scan_file(str(file)) is False
