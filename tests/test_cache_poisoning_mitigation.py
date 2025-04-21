# AegiScan\tests\test_cache_poisoning_mitigation.py

from src.mitigation.cache_poisoning_mitigation import CachePoisoningMitigation

def test_purge_existing_url(caplog):
    cache = {"https://example.com": "old response"}
    mitigation = CachePoisoningMitigation(cache)
    
    message = mitigation.purge_cache("https://example.com")
    
    assert "purged" in message
    assert "https://example.com" not in cache
    assert "purged" in caplog.text

def test_purge_nonexistent_url(caplog):
    cache = {}
    mitigation = CachePoisoningMitigation(cache)

    message = mitigation.purge_cache("https://not-in-cache.com")

    assert "No cache entry found" in message
    assert "not-in-cache" in caplog.text
