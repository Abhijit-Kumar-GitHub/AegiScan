# Allocates ~10 MB so it keeps on working
big = bytearray(10 * 1024 * 1024)
import time
import os

print(f"Normal process started, PID: {os.getpid()}")
time.sleep(60)