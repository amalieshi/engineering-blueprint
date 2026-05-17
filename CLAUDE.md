# CLAUDE.md — AI Assistant Instructions for engineering-blueprint

This file governs the behavior of AI assistants (Claude Code and related tools) operating within this repository.

---

## Repository Purpose

This repository is the canonical professional framework and SOP library for Data Engineering and Software Development work. It is maintained by a senior software engineer with a background in medical device software, healthcare informatics, and automated verification systems, transitioning into AI Engineering and Data Engineering roles.

---

## Persona and Communication Rules

- **Tone:** Professional, direct, and technically precise. No filler, no apologies, no enthusiastic openers.
- **Audience:** The owner is an experienced engineer. Do not explain foundational concepts unless explicitly asked.
- **Formatting:** Use clean Markdown. Prefer bullet points and headers over prose blocks. No emojis.
- **Trade-offs:** When a decision involves trade-offs, present the options as a senior engineer would — briefly, with a stated recommendation and the key reason why.

---

## Technical Stack and Priorities

**Primary Languages:** Python, C#  
**Ecosystem:** .NET, Azure, GitHub Actions, Docker  
**Data tooling:** dbt, Spark (PySpark), Airflow, SQL (PostgreSQL / SQL Server)  
**AI/ML:** Anthropic Claude API, LangChain, vector databases  

When generating code:

1. Default to Python 3.12+ with strict type hints (`from __future__ import annotations` where needed).
2. Default to C# 12 / .NET 8 for backend and tooling work.
3. Use `uv` or `poetry` for Python dependency management — never bare `pip install` in project scaffolding.
4. Prefer `ruff` for linting and formatting over `flake8`/`black` separately.

---

## Code Quality Requirements

All generated code must:

- Include structured error handling — raise specific, typed exceptions; never swallow errors silently.
- Use structured logging (`structlog` for Python, `Microsoft.Extensions.Logging` for C#) rather than bare `print()` or `Console.WriteLine()`.
- Be fully type-annotated in Python. In C#, use nullable reference types (`#nullable enable`).
- Have corresponding test stubs or full tests where the context is a testable unit.
- Follow the project structure standard defined in [docs/architecture/project_scaffolding.md](docs/architecture/project_scaffolding.md).

---

## Architecture Priorities

- **Scalability over convenience.** Do not generate quick-and-dirty solutions that will not survive production load or a second developer.
- **Explicit over implicit.** Configuration, dependencies, and data flow should be visible and documented, not inferred.
- **Fail fast.** Validate inputs at system boundaries. Surface errors early rather than propagating bad state.
- **Separation of concerns.** Business logic must not live in I/O layers (HTTP handlers, CLI entrypoints, pipeline tasks).

---

## Standards References

Before generating code or configuration, cross-reference the applicable standard:

| Domain | File |
|---|---|
| Python | [docs/coding_standards/python_guidelines.md](docs/coding_standards/python_guidelines.md) |
| C# / .NET | [docs/coding_standards/csharp_guidelines.md](docs/coding_standards/csharp_guidelines.md) |
| YAML / Config | [docs/coding_standards/yaml_best_practices.md](docs/coding_standards/yaml_best_practices.md) |
| Git workflow | [docs/coding_standards/git_workflow.md](docs/coding_standards/git_workflow.md) |
| Project layout | [docs/architecture/project_scaffolding.md](docs/architecture/project_scaffolding.md) |

---

## What to Avoid

- Do not generate `requirements.txt`-only Python projects. Use `pyproject.toml`.
- Do not generate bare `except Exception: pass` blocks.
- Do not add placeholder comments like `# TODO: implement this` without also generating the implementation skeleton.
- Do not propose solutions that introduce new dependencies without noting the dependency explicitly.
- Do not reformat files outside the scope of the current task.
