"""
Module: logger
Purpose: Set up a centralized logging configuration for the AegiScan project.
"""

import logging
from logging.handlers import RotatingFileHandler
import os
from src.core.config import LOG_FILE, MAX_LOG_BYTES, BACKUP_COUNT

# Create log directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configure logger
logger = logging.getLogger("AegiScan")
logger.setLevel(logging.DEBUG)

# Rotating file handler
handler = RotatingFileHandler(LOG_FILE, maxBytes=MAX_LOG_BYTES, backupCount=BACKUP_COUNT)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Also log to console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

log = logger
