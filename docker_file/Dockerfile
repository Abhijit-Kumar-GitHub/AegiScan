# AegiScan\docker_file\Dockerfile

# 1. Use a minimal base image
FROM python:3.13-slim

# 2. Create a non-root user (least privilege)
RUN useradd -ms /bin/bash appuser

# 3. Install system dependencies (binutils for `strings`), then clean up
USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends binutils \
 && rm -rf /var/lib/apt/lists/*

# 4. Set working directory
WORKDIR /app

# 5. Copy and install Python dependencies
COPY ./AegiScan/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application source
COPY ./AegiScan/src /app/src

# 7. Copy demo files
COPY ./AegiScan/docker_file/demo_high_mem.py   /app/demo_high_mem.py
COPY ./AegiScan/docker_file/demo_normal_mem.py /app/demo_normal_mem.py
COPY ./AegiScan/docker_file/demo_backdoor.bin  /app/demo_backdoor.bin
COPY ./AegiScan/docker_file/demo_normal.bin    /app/demo_normal.bin

# 8. Switch to non-root user
USER appuser

# 9. Default command: run the main module
ENTRYPOINT ["python", "-m", "src.main"]
