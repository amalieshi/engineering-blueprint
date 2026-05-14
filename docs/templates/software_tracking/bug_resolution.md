# Bug Resolution

**Ticket:** [BUG-####]
**Resolver:** [Name]
**Resolution Date:** [YYYY-MM-DD]
**Time to Resolution:** [e.g., 4h 30m]
**Related Report:** [BUG-####]

---

## Root Cause Analysis

### Classification

| Field | Value |
|---|---|
| Category | [Logic Error / Memory Allocation / Race Condition / Configuration Drift / External Dependency / Data Contract Violation] |
| Layer | [Ingestion / Transformation / Storage / Transport / API / Infrastructure] |
| Scope | [Isolated / Cross-service / Data-corrupting] |

### Causal Chain

> Trace the failure from observable symptom back to the originating defect. Every step must be evidenced, not inferred.

1. **Symptom:** [What was observed at the surface]
2. **Proximate cause:** [The immediate code path or system state that produced the symptom]
3. **Root cause:** [The underlying logic defect, misconfiguration, or structural gap]
4. **Contributing factors:** [Missing guard, absent validation, schema mismatch, memory boundary violation, etc.]

### Why It Was Not Caught Previously

- [Explain the coverage gap: missing test, untested edge case, environment parity issue, inadequate validation at system boundary, etc.]

---

## The Correction

### What Changed

| File / Module | Change Summary | PR / Commit |
|---|---|---|
| `[path/to/file.py]` | [Concise description of the logic change] | [#PR or commit SHA] |
| `[path/to/config.yaml]` | [Concise description] | [#PR or commit SHA] |

### Change Rationale

- [Why this specific correction was chosen over alternatives. If a trade-off was made — e.g., correctness over performance — state it explicitly.]

---

## Automated Verification

### Tests Written or Modified

| Test | Framework | Location | Assertion |
|---|---|---|---|
| `test_[scenario]` | [pytest / xUnit / NUnit] | `[tests/path/test_file.py]` | [The invariant the test enforces] |

### Verification Steps

1. Run: `[exact command — e.g., pytest tests/unit/test_ingest.py -v -k test_null_payload]`
2. Expected result: [Pass / specific output]
3. CI pipeline gate: [Yes / No — if yes, note the job name]

### Regression Risk

- **Services at risk:** [Adjacent services whose behavior could be affected by this change]
- **Post-deploy monitoring:** [Specific alert or dashboard metric to watch — e.g., error rate on `/ingest`, queue depth on `dead-letter-queue`]

---

## Post-Mortem Actions

| Action | Owner | Due Date |
|---|---|---|
| [e.g., Add input validation at the DICOM receive boundary] | [Name] | [YYYY-MM-DD] |
| [e.g., Update runbook to document this failure mode and recovery steps] | [Name] | [YYYY-MM-DD] |
| [e.g., Add alert for the specific error condition that triggered this bug] | [Name] | [YYYY-MM-DD] |
