# ============================================================
# Dockerfile — Standard multi-stage Python application image
# Replace <package_name> and <entrypoint_module> before use.
# ============================================================

# ── Stage 1: dependency resolution ───────────────────────────────────────────
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS resolver

WORKDIR /app

# Copy only the dependency files first — maximises layer cache reuse
COPY pyproject.toml uv.lock ./

# Install dependencies into the system environment (no venv needed in Docker)
# --frozen ensures the lockfile is not modified during build
# --no-dev excludes dev dependencies from the production image
RUN uv sync --frozen --no-dev --no-install-project

# ── Stage 2: production image ─────────────────────────────────────────────────
FROM python:3.12-slim-bookworm AS production

# Security: run as non-root user
RUN groupadd --gid 1001 appgroup && \
    useradd --uid 1001 --gid appgroup --shell /bin/bash --create-home appuser

WORKDIR /app

# Copy installed packages from resolver stage
COPY --from=resolver /app/.venv /app/.venv

# Copy application source
COPY src/ ./src/

# Ensure the venv is on PATH
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

USER appuser

# Health check — adapt the endpoint to match your application
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import <package_name>; print('ok')" || exit 1

# Override in docker-compose or Kubernetes for different entry points
CMD ["python", "-m", "<package_name>.<entrypoint_module>"]

# ── Stage 3: development image ────────────────────────────────────────────────
FROM resolver AS development

# Install dev dependencies in the development image
RUN uv sync --frozen

# Copy full source including tests and scripts
COPY . .

CMD ["uv", "run", "pytest"]
