# Project Scaffolding Standard

**Applies to:** All new Python and C# projects  
**Purpose:** A predictable directory layout reduces cognitive overhead when navigating unfamiliar codebases. Every project should be navigable by structure alone.

---

## Python Project Layout

```
my-project/
├── pyproject.toml              # Single source of truth: metadata, deps, tool config
├── uv.lock                     # Reproducible dependency lockfile (commit this)
├── .pre-commit-config.yaml     # Pre-commit hook definitions
├── .gitignore
├── README.md
│
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── exceptions.py       # All project-specific exception types
│       ├── models.py           # Dataclasses, Pydantic models, domain entities
│       ├── config.py           # Settings, loaded from env vars via pydantic-settings
│       └── <domain modules>    # Feature-specific modules
│
├── tests/
│   ├── conftest.py             # Shared fixtures and test configuration
│   ├── unit/                   # Pure logic tests — no I/O
│   └── integration/            # Tests against real services; marked @pytest.mark.integration
│
├── config/                     # Runtime configuration files (non-secret)
│   ├── logging.yaml
│   └── <environment>.yaml
│
├── data/                       # Local development data only — never production data
│   ├── raw/                    # Input samples for testing and development
│   └── processed/              # Output of local pipeline runs
│
├── scripts/                    # One-off utility scripts; not part of the package
│   └── seed_dev_db.py
│
└── docs/                       # Project-specific documentation
    └── architecture.md
```

### Key Rules

- `src/` layout is mandatory — prevents accidental import of the source tree instead of the installed package.
- `config/` holds files that are checked in. Secrets come from environment variables or a secrets manager, never from config files.
- `data/` is gitignored. Add a `.gitkeep` to preserve directory structure.
- `scripts/` are operational tools, not library code. They may import from `src/`, but `src/` must never import from `scripts/`.

---

## C# / .NET Solution Layout

```
MySolution/
├── MySolution.sln
├── Directory.Build.props        # Solution-wide MSBuild properties (analyzers, nullable, LangVersion)
├── Directory.Packages.props     # Centralised package version management (CPM)
├── .editorconfig
├── .gitignore
├── README.md
│
├── src/
│   ├── MySolution.Domain/       # Entities, value objects, interfaces, domain exceptions
│   │   └── MySolution.Domain.csproj
│   ├── MySolution.Application/  # Use cases, DTOs, service interfaces, validation
│   │   └── MySolution.Application.csproj
│   ├── MySolution.Infrastructure/ # EF Core, HTTP clients, external integrations
│   │   └── MySolution.Infrastructure.csproj
│   └── MySolution.Api/          # ASP.NET Core entry point — thin, no business logic
│       └── MySolution.Api.csproj
│
├── tests/
│   ├── MySolution.Domain.Tests/
│   ├── MySolution.Application.Tests/
│   └── MySolution.Integration.Tests/
│
└── docs/
    └── architecture.md
```

### Key Rules

- `Directory.Build.props` applies `<Nullable>enable</Nullable>`, `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`, and analyzer packages to every project — no per-project repetition.
- `Directory.Packages.props` centralises NuGet version pins. Use Central Package Management (CPM) to prevent version drift across projects.
- The `Domain` project has **zero external dependencies** — no EF Core, no HTTP clients. It depends only on the BCL.
- `Infrastructure` depends on `Application` and `Domain`. `Api` depends on `Application` and `Infrastructure`.
- Test projects mirror the `src/` namespace: `MySolution.Application.Tests` tests `MySolution.Application`.

---

## Data Pipeline Layout (Python + dbt)

```
data-pipeline/
├── pyproject.toml
├── uv.lock
│
├── src/
│   └── pipeline/
│       ├── ingest/             # Raw data extraction and landing
│       ├── transform/          # Business logic transformations (called by Airflow/Prefect tasks)
│       ├── load/               # Target system write operations
│       ├── models.py           # Shared data models (Pydantic)
│       ├── config.py           # Pipeline-level configuration
│       └── exceptions.py
│
├── dbt/                        # dbt project root
│   ├── dbt_project.yml
│   ├── profiles.yml.example    # Committed template — actual profiles.yml is gitignored
│   ├── models/
│   │   ├── staging/            # stg_* models: raw → typed, renamed
│   │   ├── intermediate/       # int_* models: business joins and aggregations
│   │   └── marts/              # fct_* and dim_* models: consumption-ready
│   ├── tests/                  # Custom dbt generic tests
│   ├── macros/
│   └── snapshots/
│
├── airflow/                    # DAG definitions (if using Airflow)
│   └── dags/
│
├── tests/
│   ├── conftest.py
│   ├── unit/
│   └── integration/
│
└── config/
    ├── dev.yaml
    └── prod.yaml
```

---

## What Every Project Must Have at Initialisation

| Item | Purpose |
|---|---|
| `pyproject.toml` / `.csproj` + `Directory.Build.props` | Dependency and tooling baseline |
| `.pre-commit-config.yaml` | Enforce linting and formatting at commit time |
| `.gitignore` | Exclude secrets, build artifacts, local data |
| `README.md` | Setup instructions, what the project does, how to run tests |
| CI workflow (`.github/workflows/ci.yml`) | Automated test and lint on every PR |
| `tests/` directory with at least one passing test | Validates the test harness works from day one |
