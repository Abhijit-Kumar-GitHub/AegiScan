# /AegiScan/src/core/utils.py
"""
Module: utils
Purpose: Helper functions for the AegiScan project.
"""

from src.core.logger import log
from src.core.config import DB_LOG_FILE
import json
from datetime import datetime


def insert_log(log_entry: dict):
    """
    Appends a JSON-formatted log entry to the DB log file.
    """
    try:
        # Convert datetime objects to string representation
        log_entry["timestamp"] = log_entry["timestamp"].isoformat() if isinstance(log_entry.get("timestamp"), datetime) else log_entry.get("timestamp")
        with open(DB_LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        log.debug(f"Inserted log entry: {log_entry}")
    except Exception as e:
        log.error(f"Error inserting log entry: {e}")
