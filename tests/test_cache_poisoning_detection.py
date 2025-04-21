# AegiScan\tests\test_cache_poisoning_detection.py
import pytest
from unittest.mock import patch, MagicMock
from src.detection.cache_poisoning_detection import CachePoisoningDetector

def test_cache_poisoning_detected():
    dummy_cache = {
        "https://example.com": "old response"
    }
    detector = CachePoisoningDetector(dummy_cache)

    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.text = "new response"
        mock_get.return_value = mock_response

        assert detector.detect_poisoning("https://example.com") is True

def test_cache_clean():
    dummy_cache = {
        "https://example.com": "same response"
    }
    detector = CachePoisoningDetector(dummy_cache)

    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.text = "same response"
        mock_get.return_value = mock_response

        assert detector.detect_poisoning("https://example.com") is False

def test_no_cache_entry(caplog):
    detector = CachePoisoningDetector({})
    result = detector.detect_poisoning("https://no-cache.com")
    assert result is False
    assert "No cached response" in caplog.text
