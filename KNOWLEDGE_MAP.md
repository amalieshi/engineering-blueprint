# Knowledge Map

Quick-reference index organized by workflow, not directory. Use this when you know what you need to do but not where to find it.

For full documentation and rendered output, see the Sphinx site built from `index.md`.

---

## Start a New Project

| Task | Resource | Stack |
|---|---|---|
| Python project baseline (`pyproject.toml`) | [docs/templates/project_init/pyproject.toml](docs/templates/project_init/pyproject.toml) | Python |
| Python `.gitignore` + pre-commit hooks | [.gitignore](docs/templates/project_init/.gitignore) · [.pre-commit-config.yaml](docs/templates/project_init/.pre-commit-config.yaml) | Python |
| Docker production image (multi-stage, uv) | [Dockerfile](docs/templates/project_init/Dockerfile) | Python |
| Repository README | [README_template.md](docs/templates/project_init/README_template.md) | All |
| Directory layout (Python / C# / dbt) | [project_scaffolding.md](docs/architecture/project_scaffolding.md) | Python / C# / dbt |

---

## Write Code

| Task | Resource | Stack |
|---|---|---|
| New Python module (header, logging, error handling, entry point) | [python_module_template.py](docs/templates/code/python_module_template.py) | Python |
| New C# class (DI, structured logging, async pattern) | [csharp_class_template.cs](docs/templates/code/csharp_class_template.cs) | C# |
| Python unit + integration test skeleton (AAA, fixtures, parametrize) | [python_test_template.py](docs/templates/code/python_test_template.py) | Python |
| C# xUnit test skeleton (NSubstitute, FluentAssertions, Theory) | [csharp_test_template.cs](docs/templates/code/csharp_test_template.cs) | C# |
| Python style, types, testing, async standards | [python_guidelines.md](docs/coding_standards/python_guidelines.md) | Python |
| C# nullable, async/await, DI, logging, architecture standards | [csharp_guidelines.md](docs/coding_standards/csharp_guidelines.md) | C# |
| YAML schema validation, secrets handling, CI/CD rules | [yaml_best_practices.md](docs/coding_standards/yaml_best_practices.md) | All |

---

## Review Code

| Task | Resource |
|---|---|
| Structured code review (architecture, types, errors, tests, security, ops) | [code_review_checklist.md](docs/templates/code/code_review_checklist.md) |
| Branching, Conventional Commits, PR process | [git_workflow.md](docs/coding_standards/git_workflow.md) |

---

## Document a Decision

| Task | Resource |
|---|---|
| Architecture Decision Record | [adr_template.md](docs/decisions/adr_template.md) |
| System-level technical risk analysis | [risk_analysis.md](docs/templates/engineering_analysis/risk_analysis.md) |
| Failure Mode and Effects Analysis (FMEA) | [fmea.md](docs/templates/engineering_analysis/fmea.md) |
| Structured Root Cause Analysis (5 Whys + corrective action) | [root_cause_analysis.md](docs/templates/engineering_analysis/root_cause_analysis.md) |

---

## Track an Issue or Change

| Task | Resource |
|---|---|
| File a defect (environment, repro steps, expected vs actual) | [bug_report.md](docs/templates/software_tracking/bug_report.md) |
| Document resolution (root cause, correction, regression coverage) | [bug_resolution.md](docs/templates/software_tracking/bug_resolution.md) |
| Request a scope or interface change | [change_request.md](docs/templates/software_tracking/change_request.md) |
| Capture a pre-design feature idea | [feature_ideation.md](docs/templates/software_tracking/feature_ideation.md) |

---

## Manage a Project

| Task | Resource |
|---|---|
| Define project scope and change control | [scope_management.md](docs/templates/project_management/scope_management.md) |
| Build and maintain a risk register | [risk_management.md](docs/templates/project_management/risk_management.md) |
| Stakeholder communication planning | [communication_plan.md](docs/templates/project_management/communication_plan.md) |
| Weekly or sprint status report | [status_report.md](docs/templates/project_management/status_report.md) |

---

## Communicate

| Task | Resource |
|---|---|
| Incident notification (initial) | [email_templates.md §1](docs/templates/communication/email_templates.md) |
| Post-mortem distribution | [email_templates.md §2](docs/templates/communication/email_templates.md) |
| Design review request | [email_templates.md §3](docs/templates/communication/email_templates.md) |
| Technical escalation to management | [email_templates.md §4](docs/templates/communication/email_templates.md) |
| Stakeholder status update | [email_templates.md §5](docs/templates/communication/email_templates.md) |
| Code / architecture feedback request | [email_templates.md §6](docs/templates/communication/email_templates.md) |
| Professional inquiry or collaboration request | [email_templates.md §7](docs/templates/communication/email_templates.md) |
| Meeting agendas (design review, sprint, post-mortem, 1:1) | [meeting_agenda.md](docs/templates/communication/meeting_agenda.md) |

---

## Tag Index

Use these tags to find related resources across categories.

| Tag | Resources |
|---|---|
| `python` | python_module_template, python_test_template, python_guidelines, pyproject.toml, Dockerfile, .pre-commit-config.yaml |
| `csharp` | csharp_class_template, csharp_test_template, csharp_guidelines |
| `testing` | python_test_template, csharp_test_template, code_review_checklist, python_guidelines §7, csharp_guidelines §9 |
| `error-handling` | python_module_template, csharp_class_template, python_guidelines §5, csharp_guidelines §6, code_review_checklist |
| `architecture` | project_scaffolding, adr_template, code_review_checklist, csharp_guidelines §8 |
| `incident` | email_templates §1–2, root_cause_analysis, bug_report, bug_resolution |
| `security` | code_review_checklist, yaml_best_practices, python_guidelines §3 (bandit) |
| `project-init` | pyproject.toml, .gitignore, .pre-commit-config.yaml, Dockerfile, README_template, project_scaffolding |
| `tracking` | bug_report, bug_resolution, change_request, feature_ideation |
| `communication` | email_templates, meeting_agenda, status_report |
