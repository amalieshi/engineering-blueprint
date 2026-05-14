# Python Coding Standards

**Applies to:** All Python projects in this portfolio  
**Minimum version:** Python 3.12  
**Enforcement:** `ruff`, `mypy` (strict), `pytest`

---

## 1. Environment and Dependency Management

### Tooling

Use `uv` as the primary package manager. It is faster than `pip`/`poetry` and produces a reproducible lockfile.

```bash
# Initialize a new project
uv init my-project
cd my-project

# Add a runtime dependency
uv add httpx

# Add a dev dependency
uv add --dev pytest ruff mypy

# Sync the environment from lockfile
uv sync
```

**Do not** commit bare `requirements.txt` files as the sole source of truth. If a `requirements.txt` is needed for compatibility (e.g., Docker builds), generate it from `pyproject.toml`:

```bash
uv export --format requirements-txt > requirements.txt
```

### Project Configuration

All project metadata, linter config, and tool settings live in a single `pyproject.toml`. See [templates/project_init/pyproject.toml](../templates/project_init/pyproject.toml) for the canonical baseline.

---

## 2. Type Annotations

Type hints are **mandatory** on all function signatures and class attributes. This is enforced by `mypy --strict`.

```python
# Correct
def fetch_records(patient_id: int, limit: int = 100) -> list[dict[str, str]]:
    ...

# Incorrect — missing annotations
def fetch_records(patient_id, limit=100):
    ...
```

Use `from __future__ import annotations` at the top of files when forward references are needed (standard for Python < 3.12 compatibility).

**Avoid `Any` except at genuine system boundaries** (e.g., deserializing raw JSON before validation). When `Any` is used, add an inline comment explaining why.

```python
raw_payload: Any = response.json()  # external API, schema validated below
```

---

## 3. Code Style and Formatting

Tool: `ruff` (replaces `black`, `isort`, `flake8`, `pyupgrade`).

Key rules enforced:

| Rule set | Purpose |
|---|---|
| `E`, `W` | pycodestyle errors and warnings |
| `F` | Pyflakes (unused imports, undefined names) |
| `I` | isort-compatible import sorting |
| `UP` | pyupgrade (modern Python idioms) |
| `ANN` | Missing type annotations |
| `S` | flake8-bandit security checks |
| `B` | flake8-bugbear (likely bugs and design issues) |

Run: `ruff check . && ruff format .`

---

## 4. Project Structure

Follow the canonical layout defined in [docs/architecture/project_scaffolding.md](../docs/architecture/project_scaffolding.md).

Business logic lives in `src/<package_name>/`. Entry points (CLI, API handlers, pipeline tasks) are thin — they parse input, call domain functions, and handle output. No logic in `__main__.py` or route handlers beyond delegation.

---

## 5. Error Handling

- Raise specific exception types. Define project-level exceptions in `src/<package>/exceptions.py`.
- Never use bare `except:` or `except Exception: pass`.
- Log the exception with context before re-raising or handling.

```python
import structlog

log = structlog.get_logger()

class RecordNotFoundError(Exception):
    """Raised when a requested record does not exist in the data store."""

def get_patient_record(patient_id: int) -> PatientRecord:
    record = db.query(patient_id)
    if record is None:
        log.warning("patient_record.not_found", patient_id=patient_id)
        raise RecordNotFoundError(f"No record for patient_id={patient_id}")
    return record
```

---

## 6. Logging

Use `structlog` for all logging. Do not use `print()` for anything that goes to production.

```python
import structlog

log = structlog.get_logger()

log.info("pipeline.started", source="s3://bucket/prefix", record_count=4200)
log.error("pipeline.failed", error=str(exc), source="s3://bucket/prefix")
```

Configure `structlog` once at the application entry point (not in library code). Library modules call `structlog.get_logger()` and let the application configure the renderer.

---

## 7. Testing

Framework: `pytest`  
Coverage threshold: **80% minimum**, enforced in CI.

### Test Layout

```
tests/
├── unit/           # Pure function tests, no I/O
├── integration/    # Tests against real services (DB, APIs) — use fixtures with teardown
└── conftest.py     # Shared fixtures
```

### Rules

- Unit tests must not hit the network or disk. Mock at the boundary using `pytest-mock` or `unittest.mock`.
- Integration tests are marked with `@pytest.mark.integration` and excluded from the default `pytest` run. Run them explicitly in CI.
- Test function names must state the scenario and expected outcome: `test_fetch_records_returns_empty_list_when_patient_has_no_records`.

```python
import pytest
from mypackage.records import get_patient_record
from mypackage.exceptions import RecordNotFoundError

def test_get_patient_record_raises_when_not_found(mocker: pytest.MockerFixture) -> None:
    mocker.patch("mypackage.records.db.query", return_value=None)
    with pytest.raises(RecordNotFoundError):
        get_patient_record(patient_id=9999)
```

---

## 8. Async Code

Use `asyncio` with `async`/`await`. Do not mix sync and async I/O in the same call stack without explicit bridging.

- Use `anyio` or `asyncio.run()` at the top-level entry point.
- Use `httpx.AsyncClient` for async HTTP — not `requests` (sync only).
- Use `asyncpg` or `sqlalchemy[asyncio]` for async database access.

---

## 9. Documentation

- Public modules, classes, and functions must have a one-line docstring stating *what* they do, not *how*.
- Do not write docstrings for private helpers (`_`-prefixed) unless the logic is non-obvious.
- Use Google-style docstrings for functions with complex signatures.

```python
def transform_hl7_segment(segment: str, encoding: str = "utf-8") -> dict[str, str]:
    """Parse a raw HL7v2 segment string into a field-keyed dictionary."""
    ...
```
