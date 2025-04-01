import hashlib
import requests
from src.core.logger import log

class CachePoisoningDetector:
    def __init__(self, cache_storage: dict):
        self.cache = cache_storage

    def detect_poisoning(self, url: str) -> bool:
        cached_response = self.cache.get(url)
        if not cached_response:
            log.info(f"No cached response for {url}.")
            return False
        try:
            actual_response = requests.get(url, timeout=5).text
        except requests.RequestException as e:
            log.error(f"Error fetching {url}: {e}")
            return False

        hash_cached = hashlib.sha256(cached_response.encode()).hexdigest()
        hash_actual = hashlib.sha256(actual_response.encode()).hexdigest()

        if hash_cached != hash_actual:
            log.warning(f"Cache poisoning detected for {url}.")
            return True
        return False


if __name__ == "__main__":
    # Example usage:
    dummy_cache = {
        "https://example.com": "<html><body>Safe Response</body></html>"
    }
    detector = CachePoisoningDetector(dummy_cache)
    if detector.detect_poisoning("https://example.com"):
        print("Cache poisoning detected!")
    else:
        print("Cache is clean.")
