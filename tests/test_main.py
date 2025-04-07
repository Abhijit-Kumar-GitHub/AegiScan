# tests/test_main.py

import pytest
from unittest.mock import patch, MagicMock
from src.main import run_detection


def test_buffer_overflow_detection():
    with patch('psutil.process_iter') as mock_process_iter, \
         patch('src.mitigation.buffer_overflow_mitigation.kill_process') as mock_kill:

        mock_proc = type('proc', (), {
            'info': {'pid': 1234, 'name': 'test_proc', 'memory_percent': 85.0}
        })
        mock_process_iter.return_value = [mock_proc]
        mock_kill.return_value = {"status": "success", "message": "Process terminated"}

        run_detection()
        mock_kill.assert_called_once_with(1234)


def test_cache_poisoning_detection():
    with patch('requests.get') as mock_get, \
         patch('src.mitigation.cache_poisoning_mitigation.CachePoisoningMitigation.purge_cache_entry') as mock_purge:

        mock_response = type('response', (), {
            'text': "<html><body><h1>Welcome</h1></body></html>"
        })
        mock_get.return_value = mock_response
        mock_purge.return_value = "Cache entry purged"

        run_detection()
        mock_purge.assert_called_once()


def test_trapdoor_detection():
    with patch('subprocess.check_output') as mock_strings, \
         patch('src.mitigation.trapdoor_mitigation.TrapdoorMitigation.remove_file') as mock_remove:

        mock_strings.return_value = b"Some normal text\nbackdoor\nmore text"
        mock_remove.return_value = "File removed"

        run_detection()
        mock_remove.assert_called_once()
