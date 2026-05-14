# Engineering Framework & Standard Operating Procedures
Core coding standards, project scaffolding, and operational templates for software development and automation.

## Overview
This repository serves as a centralized blueprint for my professional software development and data engineering workflows. It contains standard operating procedures (SOPs), architectural guidelines, and boilerplate templates designed to enforce consistency, maintainability, and high-quality engineering practices.

## Philosophy
The core tenet of this repository is that **slow is smooth, and smooth is fast.** 
By removing the cognitive overhead of project setup, configuration, and standard communication, we free up mental bandwidth for solving complex architectural problems. 

This framework prioritizes:
1.  **First Principles:** Understanding the "why" behind an architecture, avoiding hidden "magic" in the codebase.
2.  **Safety and Stability:** Emphasizing strict typing, memory-safe patterns, and rigorous testing architectures across Python and C# ecosystems.
3.  **Reproducibility:** Ensuring that any new project, whether a machine learning pipeline or a .NET service, begins from an identical, highly vetted baseline.

## Directory Structure

```
engineering-blueprint/
├── CLAUDE.md                              # AI assistant configuration (Claude Code)
├── standards/
│   ├── python_guidelines.md               # Type hints, ruff, mypy, pytest, structlog
│   ├── csharp_guidelines.md               # .NET 8, nullable types, async/await, DI, xUnit
│   ├── yaml_best_practices.md             # Schema validation, secrets, CI/CD rules
│   └── git_workflow.md                    # Branching, Conventional Commits, PR process
├── docs/
│   ├── architecture/
│   │   └── project_scaffolding.md         # Universal directory layout for Python, C#, dbt
│   ├── decisions/
│   │   └── adr_template.md                # Architecture Decision Record template
│   └── onboarding/
│       └── getting_started.md             # Quick-start guide for new projects
└── templates/
    ├── communication/
    │   ├── email_templates.md             # Incident, escalation, status update, review request
    │   └── meeting_agenda.md              # Design review, sprint planning, post-mortem, 1:1
    └── project_init/
        ├── pyproject.toml                 # Baseline: ruff, mypy (strict), pytest, coverage
        ├── .gitignore                     # Python, C#, secrets, data files, OS artifacts
        ├── .pre-commit-config.yaml        # ruff, mypy, yamllint, actionlint, commit-msg lint
        └── Dockerfile                     # Multi-stage uv-based Python production image
```

## Usage
When starting a new project, read [docs/onboarding/getting_started.md](docs/onboarding/getting_started.md) first. For AI-assisted development in this repo, Claude Code reads `CLAUDE.md` automatically.

Do not reinvent the wheel unless the terrain has fundamentally changed.

## Maintenance
This repository is a living document. As paradigms shift and new best practices emerge, these standards must be updated to reflect current technical realities. Stagnant documentation is worse than no documentation at all.
