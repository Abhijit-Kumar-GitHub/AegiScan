# AegiScan\tests\test_buffer_overflow_mitigation.py
import psutil
from unittest.mock import patch, MagicMock
from src.mitigation.buffer_overflow_mitigation import kill_process

def test_kill_existing_process():
    with patch("psutil.Process") as mock_process_class:
        mock_proc = MagicMock()
        mock_process_class.return_value = mock_proc

        result = kill_process(9999)

        assert result["status"] == "success"
        mock_proc.terminate.assert_called_once()

def test_kill_nonexistent_process():
    with patch("psutil.Process", side_effect=psutil.NoSuchProcess(9999)):
        result = kill_process(9999)

        assert result["status"] == "error"
        assert "not found" in result["message"]
