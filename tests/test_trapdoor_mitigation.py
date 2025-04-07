import os
import shutil
from src.mitigation.trapdoor_mitigation import TrapdoorMitigation

def test_quarantine_existing_file(tmp_path):
    quarantine_dir = tmp_path / "quarantine"
    mitigation = TrapdoorMitigation(str(quarantine_dir))

    # Create a dummy file to quarantine
    dummy_file = tmp_path / "dangerous.exe"
    dummy_file.write_text("Suspicious content")

    message = mitigation.quarantine_file(str(dummy_file))

    quarantined_path = quarantine_dir / "dangerous.exe"
    assert quarantined_path.exists()
    assert "moved to quarantine" in message

def test_quarantine_nonexistent_file(tmp_path, caplog):
    mitigation = TrapdoorMitigation(str(tmp_path / "quarantine"))

    message = mitigation.quarantine_file(str(tmp_path / "fake.exe"))
    assert "does not exist" in message
    assert "does not exist" in caplog.text
