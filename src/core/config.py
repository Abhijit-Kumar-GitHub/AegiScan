"""
Module: config
Purpose: Store configuration constants for AegiScan.
"""

# Buffer overflow detection threshold (in percentage)
BUFFER_OVERFLOW_THRESHOLD = 60.0

# Log file configurations
LOG_FILE = "logs/aegiscan.log"
MAX_LOG_BYTES = 1000000  # 1MB
BACKUP_COUNT = 3

# Database log file (simulated database logging)
DB_LOG_FILE = "logs/db_logs.json"

# Quarantine directory for trapdoor mitigation
QUARANTINE_DIR = "quarantine"
