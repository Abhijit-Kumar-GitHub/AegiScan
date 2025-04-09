"""
Module: cache_poisoning_mitigation
Purpose: Mitigate cache poisoning by purging or invalidating affected cache entries.
"""

from src.core.logger import log


class CachePoisoningMitigation:
    def __init__(self, cache_storage: dict):
        self.cache = cache_storage

    def purge_cache(self, url: str) -> str:
        """
        Purges the cache entry for the given URL.
        Returns a status message.
        """
        if url in self.cache:
            del self.cache[url]
            message = f"Cache entry for {url} purged."
            log.info(message)
            return message
        message = f"No cache entry found for {url}."
        log.warning(message)
        return message


if __name__ == "__main__":
    dummy_cache = {"https://example.com": "<html><body>Safe Response</body></html>"}
    mitigation = CachePoisoningMitigation(dummy_cache)
    print(mitigation.purge_cache("https://example.com"))
