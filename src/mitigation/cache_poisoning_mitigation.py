"""
Module: buffer_overflow_mitigation
Purpose: Provide mitigation actions for processes causing buffer overflow risks.
"""

import psutil
from src.core.logger import log


def kill_process(pid: int) -> dict:
    """
    Attempts to terminate a process with the given PID.
    Returns a dictionary with status and message.
    """
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        log.info(f"Process {pid} terminated successfully as a mitigation action.")
        return {"status": "success", "message": f"Process {pid} terminated"}
    except psutil.NoSuchProcess:
        log.error(f"Process {pid} not found for termination.")
        return {"status": "error", "message": f"Process {pid} not found"}
    except Exception as e:
        log.error(f"Error terminating process {pid}: {e}")
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    # For testing purposes only.
    pid_example = 1234                                           # Replace with an actual PID during testing.
    result = kill_process(pid_example)
    print(result)
