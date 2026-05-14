# Getting Started with This Repository

This document is the entry point for using the engineering-blueprint framework in a new project.

---

## What This Repository Provides

| Directory | Contents |
|---|---|
| `standards/` | Coding guidelines for Python, C#, YAML, and Git |
| `templates/project_init/` | Copy-paste starting points for new projects |
| `templates/communication/` | Email and meeting templates for professional communication |
| `docs/architecture/` | Structural standards and scaffolding references |
| `docs/decisions/` | ADR template for logging significant technical decisions |
| `CLAUDE.md` | AI assistant configuration for Claude Code |

---

## Starting a New Python Project

1. Copy the project template files:

```bash
cp templates/project_init/pyproject.toml /path/to/new-project/
cp templates/project_init/.gitignore /path/to/new-project/
cp templates/project_init/.pre-commit-config.yaml /path/to/new-project/
```

2. Initialise the environment:

```bash
cd /path/to/new-project
uv sync
uv run pre-commit install
```

3. Apply the project structure defined in [docs/architecture/project_scaffolding.md](../architecture/project_scaffolding.md).

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

2. Copy `Directory.Build.props` (from `csharp_guidelines.md`) to the solution root.

3. Confirm baseline build and tests:

```bash
dotnet build
dotnet test
dotnet format --verify-no-changes
```

---

## Logging a Technical Decision

Whenever a non-trivial architectural decision is made:

1. Copy `docs/decisions/adr_template.md` to `docs/decisions/ADR-NNNN-short-title.md`.
2. Complete all sections. The **Context** and **Considered Alternatives** sections are mandatory.
3. Commit with: `docs: add ADR-NNNN for <decision topic>`

---

## Key Standards to Read First

If you are joining this project or starting a new one, read these in order:

1. [standards/python_guidelines.md](../../standards/python_guidelines.md) or [standards/csharp_guidelines.md](../../standards/csharp_guidelines.md) depending on your stack.
2. [standards/git_workflow.md](../../standards/git_workflow.md) — branching, commits, and PRs.
3. [docs/architecture/project_scaffolding.md](../architecture/project_scaffolding.md) — directory structure.
4. [standards/yaml_best_practices.md](../../standards/yaml_best_practices.md) — for any configuration work.
