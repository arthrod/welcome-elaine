# syntax=docker/dockerfile:1.21
FROM python:3.14-slim

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:0.10.3 /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

# Create non-root user early
RUN useradd -m app_user && \
    chown app_user:app_user /app

# Copy and install dependencies first for better caching
COPY --chown=app_user:app_user requirements.txt README.md /app/
COPY --chown=app_user:app_user notebooks /app/notebooks/

# Install dependencies, no dev dependencies
RUN uv pip install --no-cache-dir -r requirements.txt && \
    rm -rf /uv /bin/uv

# Switch to non-root
USER app_user

# Set environment variables
ENV PORT=4879
ENV HOST=0.0.0.0
ENV NOTEBOOK_PATH=/app/notebooks/welcome-elaine.py
ENV PROXY_URL=http://10.0.1.3:80

# Expose the server port
EXPOSE $PORT

# Run the server
CMD marimo run $NOTEBOOK_PATH --token $MARIMO_TOKEN -p $PORT --host $HOST --include-code False --proxy $PROXY_URL