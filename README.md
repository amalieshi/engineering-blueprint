# Engineering Framework & Standard Operating Procedures

Core coding standards, project scaffolding, and operational templates for software development and data engineering.

**Quick navigation:** [KNOWLEDGE_MAP.md](KNOWLEDGE_MAP.md) — task-oriented index across all resources.

---

## Overview

This repository is the canonical professional framework for Data Engineering and Software Development work. It contains standard operating procedures, architectural guidelines, fill-in-the-blank templates, and engineering analysis tools designed to enforce consistency, maintainability, and production-grade engineering practices.

## Philosophy

The core tenet of this repository is **slow is smooth, and smooth is fast.** By eliminating the cognitive overhead of project setup, configuration, and standard documentation, mental bandwidth is freed for solving complex architectural problems.

This framework prioritizes:

1. **First Principles** — Understanding the *why* behind an architecture. No hidden magic in the codebase.
2. **Safety and Stability** — Strict typing, memory-safe patterns, and rigorous testing across Python and C# ecosystems.
3. **Reproducibility** — Every new project, whether a data pipeline or a .NET service, begins from an identical, vetted baseline.
4. **Explicit over Implicit** — Configuration, dependencies, and data flow are visible and documented, not inferred.

---

## Directory Structure

```
engineering-blueprint/
├── CLAUDE.md                                    # AI assistant configuration (Claude Code)
├── LICENSE
├── Taskfile.yml                                 # Build tasks: html, livehtml, clean
├── conf.py                                      # Sphinx configuration
├── index.md                                     # Sphinx site root and navigation
├── pyproject.toml                               # Project config and docs dependencies
├── .github/
│   └── workflows/
│       └── docs.yml                             # CI: build and deploy Sphinx site
└── docs/
    ├── architecture/
    │   └── project_scaffolding.md               # Universal directory layout for Python, C#, dbt
    ├── coding_standards/
    │   ├── python_guidelines.md                 # Type hints, ruff, mypy, pytest, structlog
    │   ├── csharp_guidelines.md                 # .NET 8, nullable types, async/await, DI, xUnit
    │   ├── yaml_best_practices.md               # Schema validation, secrets, CI/CD rules
    │   └── git_workflow.md                      # Branching, Conventional Commits, PR process
    ├── decisions/
    │   └── adr_template.md                      # Architecture Decision Record template
    └── templates/
        ├── code/
        │   ├── python_module_template.py        # Module header, structlog, error handling, entry point
        │   ├── csharp_class_template.cs         # DI constructor, async method, structured logging
        │   ├── python_test_template.py          # AAA pattern, fixtures, parametrize, integration stub
        │   ├── csharp_test_template.cs          # xUnit + NSubstitute + FluentAssertions
        │   └── code_review_checklist.md         # Architecture, types, errors, tests, security, ops
        ├── communication/
        │   ├── email_templates.md               # Incident, escalation, status update, review request, inquiry
        │   └── meeting_agenda.md                # Design review, sprint planning, post-mortem, 1:1
        ├── engineering_analysis/
        │   ├── fmea.md                          # Failure Mode and Effects Analysis
        │   ├── root_cause_analysis.md           # Structured RCA with 5 Whys and corrective action
        │   └── risk_analysis.md                 # System-level technical risk analysis
        ├── project_init/
        │   ├── pyproject.toml                   # Baseline: ruff, mypy (strict), pytest, coverage
        │   ├── .gitignore                       # Python, C#, secrets, data files, OS artifacts
        │   ├── .pre-commit-config.yaml          # ruff, mypy, yamllint, actionlint, commit-msg lint
        │   ├── Dockerfile                       # Multi-stage uv-based Python production image
        │   └── README_template.md               # Standard project README structure
        ├── project_management/
        │   ├── scope_management.md              # Scope definition, validation, change control process
        │   ├── risk_management.md               # Risk register with scoring, mitigation, and owners
        │   ├── communication_plan.md            # Stakeholder matrix, delivery mechanisms, escalation path
        │   └── status_report.md                 # Structured sprint/project status report
        └── software_tracking/
            ├── bug_report.md                    # Environment, reproduction steps, expected vs actual state
            ├── bug_resolution.md                # Root cause analysis, correction, automated verification
            ├── change_request.md                # Scope alteration, impact analysis, rollback strategy
            └── feature_ideation.md              # Friction, hypothesis, constraints and unknowns
```

---

## Starting a New Python Project

1. Copy the project template files:

```bash
cp docs/templates/project_init/pyproject.toml /path/to/new-project/
cp docs/templates/project_init/.gitignore /path/to/new-project/
cp docs/templates/project_init/.pre-commit-config.yaml /path/to/new-project/
```

2. Initialise the environment:

```bash
cd /path/to/new-project
uv sync
uv run pre-commit install
```

3. Apply the project structure defined in [docs/architecture/project_scaffolding.md](docs/architecture/project_scaffolding.md).

4. Run the baseline checks to confirm the toolchain works:

```bash
uv run ruff check .
uv run mypy src/
uv run pytest
```

---

## Starting a New C# Project

1. Create the solution with the standard structure:

```bash
dotnet new sln -n MyProject
mkdir -p src tests
dotnet new classlib -n MyProject.Domain -o src/MyProject.Domain
dotnet new classlib -n MyProject.Application -o src/MyProject.Application
dotnet new classlib -n MyProject.Infrastructure -o src/MyProject.Infrastructure
dotnet new webapi -n MyProject.Api -o src/MyProject.Api
dotnet new xunit -n MyProject.Domain.Tests -o tests/MyProject.Domain.Tests
dotnet sln add src/**/*.csproj tests/**/*.csproj
```

2. Copy `Directory.Build.props` (from [docs/coding_standards/csharp_guidelines.md](docs/coding_standards/csharp_guidelines.md)) to the solution root.

3. Confirm baseline build and tests:

```bash
dotnet build
dotnet test
dotnet format --verify-no-changes
```

---

## Tracking Software Issues

Use the templates in `templates/software_tracking/` for all issue and change documentation.

| Situation | Template |
|---|---|
| Defect found in staging or production | [docs/templates/software_tracking/bug_report.md](docs/templates/software_tracking/bug_report.md) |
| Defect resolved — document root cause and regression tests | [docs/templates/software_tracking/bug_resolution.md](docs/templates/software_tracking/bug_resolution.md) |
| Scope, interface, or contract modification needed | [docs/templates/software_tracking/change_request.md](docs/templates/software_tracking/change_request.md) |
| New capability being evaluated — pre-design stage | [docs/templates/software_tracking/feature_ideation.md](docs/templates/software_tracking/feature_ideation.md) |

---

## Engineering Analysis

Use the templates in `docs/templates/engineering_analysis/` for structured technical analysis.

| Situation | Template |
|---|---|
| Systematically identifying failure modes before or after a design decision | [docs/templates/engineering_analysis/fmea.md](docs/templates/engineering_analysis/fmea.md) |
| Investigating a significant defect, outage, or recurring failure | [docs/templates/engineering_analysis/root_cause_analysis.md](docs/templates/engineering_analysis/root_cause_analysis.md) |
| Assessing technical risk for a system, component, or integration | [docs/templates/engineering_analysis/risk_analysis.md](docs/templates/engineering_analysis/risk_analysis.md) |

---

## Managing a Project or Pipeline

Use the templates in `templates/project_management/` at project initiation and maintain them throughout delivery.

| Artifact | Template | When to Create |
|---|---|---|
| Scope Management Plan | [docs/templates/project_management/scope_management.md](docs/templates/project_management/scope_management.md) | Before development begins |
| Risk Management Plan | [docs/templates/project_management/risk_management.md](docs/templates/project_management/risk_management.md) | Before development begins; reviewed each sprint |
| Communication Plan | [docs/templates/project_management/communication_plan.md](docs/templates/project_management/communication_plan.md) | Before stakeholder engagement begins |

---

## Logging a Technical Decision

Whenever a non-trivial architectural decision is made:

1. Copy [docs/decisions/adr_template.md](docs/decisions/adr_template.md) to `docs/decisions/ADR-NNNN-short-title.md`.
2. Complete all sections. **Context** and **Considered Alternatives** are mandatory.
3. Commit with: `docs: add ADR-NNNN for <decision topic>`

---

## Standards to Read First

When starting a new project or joining this one, read these in order:

1. [docs/coding_standards/python_guidelines.md](docs/coding_standards/python_guidelines.md) or [docs/coding_standards/csharp_guidelines.md](docs/coding_standards/csharp_guidelines.md) — depending on your stack.
2. [docs/coding_standards/git_workflow.md](docs/coding_standards/git_workflow.md) — branching, commits, and PRs.
3. [docs/architecture/project_scaffolding.md](docs/architecture/project_scaffolding.md) — directory structure for all project types.
4. [docs/coding_standards/yaml_best_practices.md](docs/coding_standards/yaml_best_practices.md) — for any configuration or pipeline work.

---

## Maintenance

This repository is a living document. As paradigms shift and new best practices emerge, these standards must be updated to reflect current technical realities. Stagnant documentation is worse than no documentation at all.

Do not reinvent the wheel unless the terrain has fundamentally changed.
