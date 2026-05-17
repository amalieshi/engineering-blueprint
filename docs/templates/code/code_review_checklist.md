# Code Review Checklist

**PR:** [link]  
**Reviewer:** [Name]  
**Date:** [YYYY-MM-DD]

Use this checklist as a structured pass, not a sequential one. A single `[ ]` that cannot be resolved is a blocking issue unless explicitly deferred with a linked ticket.

---

## Architecture and Design

- [ ] Business logic is isolated from I/O layers (HTTP handlers, CLI entrypoints, pipeline tasks contain no domain logic)
- [ ] New abstractions are justified by concrete, existing usage — not speculative future requirements
- [ ] Backward-incompatible changes to public interfaces, APIs, or event schemas are explicitly documented in the PR description
- [ ] Data flow is traceable end-to-end without reading three layers of indirection
- [ ] No circular dependencies introduced between modules or projects

---

## Type Safety

- [ ] All public function signatures and class attributes are fully annotated (Python: mypy strict; C#: nullable enabled)
- [ ] No `Any` used in Python without an inline comment explaining the boundary condition
- [ ] No null-forgiving operator (`!`) in C# without an inline comment
- [ ] Generics and type parameters are specific — no untyped collections (`list` → `list[str]`, `List` → `List<PatientRecord>`)

---

## Error Handling

- [ ] No bare `except:` or `except Exception: pass` in Python
- [ ] No top-level `catch (Exception)` in C# without a documented reason and re-throw or structured response
- [ ] Errors are logged with structured context (relevant IDs, inputs) before propagation
- [ ] Specific, typed exception classes are raised — not `RuntimeError("something went wrong")`
- [ ] External inputs are validated at the boundary before being passed to domain logic

---

## Testing

- [ ] New logic has corresponding unit tests covering the happy path and at least one error path
- [ ] External dependencies are mocked at the module/interface boundary — not at the internal call site
- [ ] Integration tests are marked `@pytest.mark.integration` (Python) or placed in `*.Integration.Tests` (C#)
- [ ] No existing tests were silently deleted or commented out to make the build pass
- [ ] Coverage threshold (≥ 80%) is maintained after this change

---

## Security

- [ ] No secrets, API keys, credentials, or PII appear in code, comments, log messages, or test fixtures
- [ ] All SQL is parameterised — no string concatenation or f-string interpolation in queries
- [ ] File paths, subprocess calls, and shell commands do not incorporate unvalidated user input
- [ ] No dependency version downgraded without an explicit, documented reason

---

## Operational Quality

- [ ] Log messages use structured format — no f-string or `%` interpolation in log calls
- [ ] `CancellationToken` is propagated through all async chains in C#
- [ ] No configuration values are hardcoded — they come from environment variables or a config file
- [ ] Resource handles (file descriptors, DB connections, HTTP clients) are closed via `with`/`using` or explicit teardown

---

## Documentation and Housekeeping

- [ ] Public APIs have a one-line docstring stating *what* they do (not *how*)
- [ ] Non-obvious logic includes an inline comment explaining *why* (hidden constraint, workaround, invariant)
- [ ] No commented-out code
- [ ] No debug artefacts: `print()`, `Console.WriteLine()`, temporary `TODO` without a linked ticket
- [ ] If an architectural decision was made in this PR, an ADR is referenced or created

---

## Summary

**Verdict:** Approve | Request Changes | Comment only

**Blocking issues:**
- [ ] None — or list them below

**Non-blocking notes:**
-
