# tests/test_main.py

import pytest
from unittest.mock import patch, MagicMock
from src.main import run_detection

@patch('src.main.kill_process')
@patch('psutil.process_iter')
def test_buffer_overflow_detection(mock_process_iter, mock_kill):
    """
    Simulate a process exceeding the memory threshold and verify kill_process is called.
    """
    # Mock a single process over the threshold
    proc = MagicMock()
    proc.info = {'pid': 1234, 'name': 'test_proc', 'memory_percent': 85.0}
    mock_process_iter.return_value = [proc]

    # Simulate successful kill
    mock_kill.return_value = {'status': 'success', 'message': 'Process terminated'}

    run_detection()

    mock_kill.assert_called_once_with(1234)


@patch('src.main.CachePoisoningMitigation.purge_cache')
@patch('src.main.CachePoisoningDetector.detect_poisoning')
def test_cache_poisoning_mitigation(mock_detect, mock_purge):
    """
    Simulate cache poisoning detection and verify purge_cache is called.
    """
    # Force detection to return True
    mock_detect.return_value = True
    mock_purge.return_value = 'Cache entry for https://example.com purged.'

    run_detection()

    mock_detect.assert_called_once_with('https://example.com')
    mock_purge.assert_called_once_with('https://example.com')


@patch('src.main.TrapdoorMitigation.quarantine_file')
@patch('src.main.TrapdoorDetector.scan_file')
def test_trapdoor_detection_and_quarantine(mock_scan, mock_quarantine):
    """
    Simulate trapdoor detection and verify quarantine_file is called.
    """
    # Force trapdoor scan to return True
    mock_scan.return_value = True
    mock_quarantine.return_value = 'File quarantined.'

    run_detection()

    mock_scan.assert_called_once_with('suspected_binary.exe')
    mock_quarantine.assert_called_once_with('suspected_binary.exe')
