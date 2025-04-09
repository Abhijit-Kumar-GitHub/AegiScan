"""
Main entry point for the AegiScan Security Vulnerability Detection Framework.
Combines detection and mitigation modules.
"""

from src.detection.buffer_overflow_detection import monitor_memory
from src.detection.cache_poisoning_detection import CachePoisoningDetector
from src.detection.trapdoor_detection import TrapdoorDetector

from src.mitigation.buffer_overflow_mitigation import kill_process
from src.mitigation.cache_poisoning_mitigation import CachePoisoningMitigation
from src.mitigation.trapdoor_mitigation import TrapdoorMitigation

from src.core.logger import log
from src.core.config import BUFFER_OVERFLOW_THRESHOLD

import psutil


def run_detection():
    # === BUFFER OVERFLOW DETECTION & MITIGATION ===
    log.info("Starting buffer overflow detection...")
    threshold = BUFFER_OVERFLOW_THRESHOLD
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            mem_percent = proc.info.get('memory_percent', 0)
            if mem_percent > threshold:
                log.warning(f"Process {proc.info['name']} (PID: {proc.info['pid']}) "
                            f"using {mem_percent:.2f}% memory, exceeding threshold of {threshold}%.")
                result = kill_process(proc.info['pid'])  # Mitigation
                log.info(f"Buffer overflow mitigation result: {result}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # === CACHE POISONING DETECTION & MITIGATION ===
    log.info("Starting cache poisoning detection...")
    dummy_cache = {
        "https://example.com": "<html><body>Safe Response</body></html>"
    }
    cache_detector = CachePoisoningDetector(dummy_cache)
    if cache_detector.detect_poisoning("https://example.com"):
        mitigation = CachePoisoningMitigation(dummy_cache)
        msg = mitigation.purge_cache("https://example.com")
        log.info(f"Cache poisoning mitigation result: {msg}")

    # === TRAPDOOR DETECTION & MITIGATION ===
    log.info("Starting trapdoor detection...")
    trapdoor_detector = TrapdoorDetector()
    sample_file = "suspected_binary.exe"  # Replace with real file during actual test
    if trapdoor_detector.scan_file(sample_file):
        trapdoor_mitigation = TrapdoorMitigation()
        msg = trapdoor_mitigation.quarantine_file(sample_file)
        log.info(f"Trapdoor mitigation result: {msg}")


if __name__ == "__main__":
    log.info("AegiScan started.")
    run_detection()
    log.info("AegiScan finished a detection cycle.")
