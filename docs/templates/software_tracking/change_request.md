# Change Request

**CR Number:** [CR-####]
**Requestor:** [Name]
**Date Submitted:** [YYYY-MM-DD]
**Target Release:** [Version / Sprint / Date]
**Status:** [Draft / Under Review / Approved / Rejected / Implemented]
**Priority:** [Critical / High / Medium / Low]

---

## Scope Alteration

### Current State

- [Describe the existing behavior, contract, or architecture being changed]
- [Reference the original specification, ticket, or SOP if applicable]

### Proposed Change

- [Describe precisely what will be added, removed, or modified]
- [Be explicit about interface changes: API signatures, schema fields, data types, message formats, file paths]

### Justification

- [The technical or business reason driving this change — state the defect, constraint, or requirement explicitly]

### Out of Scope

- [Explicitly list what this CR does NOT change to prevent scope creep during implementation]

---

## Impact Analysis

### Memory and Performance

- **Estimated memory delta:** [e.g., +~200 MB per worker node due to expanded in-memory batch buffer]
- **CPU / throughput impact:** [e.g., Expected 15% increase in transformation latency under peak load; acceptable against current SLA headroom]
- **Benchmark baseline:** [Reference the existing performance benchmark or load test report if one exists]

### Downstream Pipelines

| Pipeline / Job | Impact | Action Required |
|---|---|---|
| `[pipeline-name]` | [e.g., Schema change requires consumer to update field mapping] | [Yes / No — describe] |
| `[job-name]` | [e.g., No functional change; config reload required on deploy] | [Yes / No — describe] |

### DICOM Endpoints and Data Contracts

| Endpoint / Service | Impact | Affected Tags / Fields |
|---|---|---|
| `[endpoint or service name]` | [e.g., Response payload structure changes — consumers must update parsers] | `[e.g., (0008,0060) Modality, (0010,0020) PatientID]` |
| `[endpoint or service name]` | [e.g., No impact] | N/A |

### Dependent Teams and Consumers

- [List teams, services, or external systems that must be notified or updated before deployment]

---

## Rollback Strategy

### Preconditions for Rollback

- [Define the specific, measurable conditions that trigger a rollback: e.g., error rate exceeds 2% within 15 minutes of deploy, data integrity check fails, SLA breach detected on monitoring dashboard]

### Rollback Procedure

1. [Step 1 — e.g., Revert to previous deployment artifact: `kubectl rollout undo deployment/[service-name]`]
2. [Step 2 — e.g., Restore configuration from `config/v[N-1].yaml` and apply: `kubectl apply -f config/v[N-1].yaml`]
3. [Step 3 — e.g., Flush affected message queue partition and replay from last known-good checkpoint]
4. [Step N — Verify system has returned to baseline using: `[monitoring link or validation command]`]

### Rollback Validation

- **Validation method:** [Specify exactly how to confirm the rollback succeeded — dashboard metric, integration test command, manual smoke test]
- **Estimated rollback time:** [e.g., < 10 minutes with no data migration required]
- **Data recovery required:** [Yes / No — if yes, describe the recovery procedure and estimated data window affected]

### Known Rollback Limitations

- [State conditions where rollback is not straightforward — e.g., "If the database migration script has executed, schema changes cannot be automatically reversed. A compensating migration must be authored and applied manually."]

---

## Approvals

| Role | Name | Decision | Date |
|---|---|---|---|
| Engineering Lead | [Name] | [Approved / Rejected] | [YYYY-MM-DD] |
| Data Owner | [Name] | [Approved / Rejected] | [YYYY-MM-DD] |
| QA / Test Lead | [Name] | [Approved / Rejected] | [YYYY-MM-DD] |
| Project Sponsor | [Name] | [Approved / Rejected] | [YYYY-MM-DD] |
