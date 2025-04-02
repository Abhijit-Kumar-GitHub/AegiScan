"""
Is going to be the main entry point for the AegiScan Security Vulnerability Detection Framework.
Its going to gombine detection and mitigation modules.
"""


from src.detection.cache_poisoning_detection import CachePoisoningDetector


from src.mitigation.cache_poisoning_mitigation import CachePoisoningMitigation



from src.core.logger import log
import time


def run_detection():
    # Run cache poisoning detection on a sample URL
    dummy_cache = {
        "https://example.com": "<html><body>Safe Response</body></html>"
    }
    cache_detector = CachePoisoningDetector(dummy_cache)
    if cache_detector.detect_poisoning("https://example.com"):
        mitigation = CachePoisoningMitigation(dummy_cache)
        log.info(mitigation.purge_cache("https://example.com"))




if __name__ == "__main__":
    log.info("AegiScan started.")
    run_detection()
    log.info("AegiScan finished a detection cycle.")