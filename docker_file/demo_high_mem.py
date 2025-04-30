# Allocates ~210 MB so it trips the limit of 60% of 256 MB which we will be allocating
big = bytearray(210 * 1024 * 1024)
import time
import os

print(f"High-mem process started, PID: {os.getpid()}")
time.sleep(60)