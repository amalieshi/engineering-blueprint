# [Project Name]

[One sentence: what this system does and who uses it.]

---

## System Overview

[2–3 paragraphs. What problem this solves, the primary data flow or user journey, and where it fits in the larger architecture. Include context a new engineer needs to understand why this project exists.]

### Architecture

```
[ASCII or Mermaid diagram. Replace this block or link to docs/architecture.md]

Input → [Component A] → [Component B] → Output
```

Key components:

| Component | Purpose |
|---|---|
| `src/<package>/ingest/` | [What it does] |
| `src/<package>/transform/` | [What it does] |
| `src/<package>/config.py` | Settings loaded from environment variables |

---

## Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Python | >= 3.12 | Managed via `uv` |
| [Tool or service] | >= [version] | [Where to get it] |

Required environment variables (copy `.env.example` to `.env` and populate):

```bash
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/dbname
SECRET_KEY=
LOG_LEVEL=INFO
```

---

## Quick Start

```bash
# Clone
git clone <repo-url>
cd <project-name>

# Install environment (Python)
uv sync
uv run pre-commit install

# Verify toolchain
uv run ruff check .
uv run mypy src/
uv run pytest

# Or for .NET
dotnet restore
dotnet build
dotnet test
dotnet format --verify-no-changes
```

---

## Project Structure

```
<project-name>/
├── pyproject.toml          # Deps, tool config, metadata
├── src/
│   └── <package>/
│       ├── config.py       # pydantic-settings: env vars → typed config
│       ├── exceptions.py   # Project-specific exception types
│       ├── models.py       # Pydantic / dataclass domain models
│       └── <domain>/       # Feature modules
├── tests/
│   ├── conftest.py
│   ├── unit/
│   └── integration/
├── config/
│   ├── logging.yaml
│   └── dev.yaml
└── docs/
    └── architecture.md
```

---

## Running Tests

```bash
# Unit tests only (fast, no external services)
uv run pytest tests/unit/

# Full suite including integration
uv run pytest

# Integration tests only (requires running services)
uv run pytest -m integration

# Coverage report
uv run pytest --cov=src --cov-report=html
open htmlcov/index.html
```

---

## Configuration

Configuration is loaded from environment variables via `pydantic-settings` (see `src/<package>/config.py`).

| Variable | Required | Default | Description |
|---|---|---|---|
| `DATABASE_URL` | Yes | — | PostgreSQL async connection string |
| `LOG_LEVEL` | No | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| `[VAR]` | Yes / No | [default] | [description] |

---

## Dependency Management

```bash
uv add <package>           # Add runtime dependency
uv add --dev <package>     # Add dev/test dependency
uv sync                    # Sync environment from lockfile
uv export --format requirements-txt > requirements.txt  # For Docker builds
```

Do not edit `uv.lock` manually. Commit it.

---

## Deployment

[Describe: Docker image tag, Helm chart location, GitHub Actions workflow, environment promotion process.]

```bash
# Build production image
docker build -t <project>:<version> .

# Push to registry
docker push <registry>/<project>:<version>
```

---

## Contributing

1. Branch from `main`: `git checkout -b feat/<ticket>-<short-description>`
2. Follow [git workflow standards](../../coding_standards/git_workflow.md).
3. Ensure `ruff`, `mypy`, and `pytest` pass before opening a PR.
4. Use the [code review checklist](../code/code_review_checklist.md) when reviewing.

---

## Related Resources

| Resource | Link |
|---|---|
| Architecture Decision Records | `docs/decisions/` |
| Engineering Blueprint | [engineering-blueprint](https://github.com/amalieshi/engineering-blueprint) |
| CI/CD Pipeline | `.github/workflows/` |
| Monitoring Dashboard | [link] |
| Runbook | [link] |
