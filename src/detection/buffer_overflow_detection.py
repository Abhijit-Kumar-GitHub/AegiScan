"""
Module: buffer_overflow_detection
Purpose: Monitor process memory usage to detect potential buffer overflow vulnerabilities.
"""

import psutil
from datetime import datetime
from src.core.logger import log
from src.core.utils import insert_log
from src.core.config import BUFFER_OVERFLOW_THRESHOLD


def monitor_memory(threshold: float = BUFFER_OVERFLOW_THRESHOLD):
    """
    Monitors running processes and logs those exceeding the memory threshold.
    """
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            mem_percent = proc.info.get('memory_percent', 0)
            if mem_percent > threshold:
                message = f"Process {proc.info['name']} (PID: {proc.info['pid']}) " \
                          f"using {mem_percent:.2f}% memory, exceeding threshold of {threshold}%."
                log.warning(message)
                insert_log({
                    "timestamp": datetime.now(),
                    "process_name": proc.info['name'],
                    "pid": proc.info['pid'],
                    "memory_usage": mem_percent,
                    "vulnerability": "Potential Buffer Overflow"
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


if __name__ == "__main__":
    monitor_memory()
