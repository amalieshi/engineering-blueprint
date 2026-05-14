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

*   `docs/`
    *   Documentation regarding overarching system architectures, deployment strategies, and general professional development roadmaps.
*   `standards/`
    *   `python_guidelines.md`: Standards for typing, linting, and testing in Python.
    *   `csharp_guidelines.md`: Architectural patterns, memory management, and .NET ecosystem best practices.
    *   `yaml_best_practices.md`: Schema validation and configuration management rules.
*   `templates/`
    *   `communication/`: Standardized email drafts, meeting agendas, and technical proposal structures.
    *   `project_init/`: Universal `.gitignore` files, `pyproject.toml` configurations, and standardized CI/CD pipeline templates.
*   `meta/`
    *   `CLAUDE.md`: System instructions and contextual rules for AI assistants interacting with this codebase.

## Usage
When initiating a new project or drafting technical communication, consult the relevant directory here first. Do not reinvent the wheel unless the terrain has fundamentally changed.

## Maintenance
This repository is a living document. As paradigms shift and new best practices emerge, these standards must be updated to reflect current technical realities. Stagnant documentation is worse than no documentation at all.
