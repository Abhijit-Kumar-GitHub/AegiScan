# AegiScan\tests\test_buffer_overflow_detection.py
import psutil
from unittest.mock import patch, MagicMock
from src.detection.buffer_overflow_detection import monitor_memory

def test_detects_overflow(caplog):
    mock_proc = MagicMock()
    mock_proc.info = {"pid": 123, "name": "vulnerable_app", "memory_percent": 85.0}
    
    with patch("psutil.process_iter", return_value=[mock_proc]):
        monitor_memory(threshold=60.0)
    
    assert any("exceeding threshold" in record.message for record in caplog.records)

def test_ignores_safe_processes(caplog):
    mock_proc = MagicMock()
    mock_proc.info = {"pid": 456, "name": "safe_app", "memory_percent": 20.0}
    
    with patch("psutil.process_iter", return_value=[mock_proc]):
        monitor_memory(threshold=60.0)
    
    assert not any("exceeding threshold" in record.message for record in caplog.records)
