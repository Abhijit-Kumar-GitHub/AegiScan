"""
Is going to be the main entry point for the AegiScan Security Vulnerability Detection Framework.
Its going to gombine detection and mitigation modules.
"""


from src.detection.cache_poisoning_detection import CachePoisoningDetector
from src.detection.trapdoor_detection import TrapdoorDetector

from src.mitigation.cache_poisoning_mitigation import CachePoisoningMitigation
from src.mitigation.trapdoor_mitigation import TrapdoorMitigation


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


    # Run trapdoor detection on a sample file
    trapdoor_detector = TrapdoorDetector()
    sample_file = "suspected_binary.exe"  # Update with a real file for actual testing
    if trapdoor_detector.scan_file(sample_file):
        trapdoor_mitigation = TrapdoorMitigation()
        log.info(trapdoor_mitigation.quarantine_file(sample_file))



if __name__ == "__main__":
    log.info("AegiScan started.")
    run_detection()
    log.info("AegiScan finished a detection cycle.")