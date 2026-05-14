# Bug Report

**Ticket:** [BUG-####]
**Reporter:** [Name]
**Date:** [YYYY-MM-DD]
**Severity:** [Critical / High / Medium / Low]
**Status:** [Open / In Progress / Resolved]

---

## Environment

| Field | Value |
|---|---|
| Environment | [Staging / Production] |
| Service / Component | [e.g., `ingest-pipeline`, `dicom-router`] |
| Version / Build | [e.g., `v2.4.1`, commit `a3f92c1`] |
| Runtime | [e.g., Python 3.12.3, .NET 8.0.4] |
| Infrastructure | [e.g., Azure AKS 1.29, Docker 26.1] |
| OS | [e.g., Ubuntu 22.04 LTS] |
| Dependent Services | [e.g., PostgreSQL 16.2, Redis 7.2] |

---

## Steps to Reproduce

> Steps must be deterministic. If the bug is intermittent, note the frequency and known triggering conditions.

1. [Starting state: describe the exact system state, seed data, or preconditions]
2. [Action 1 — be explicit: endpoint called, input payload, CLI command, etc.]
3. [Action 2]
4. [Action N — the step at which failure occurs]

**Input / Payload (if applicable):**

```json
{
  "key": "value"
}
```

**Reproduction Rate:** [Always / ~X% of the time under condition Y]

---

## Expected State

- [Describe the correct, documented system behavior]
- [Reference the relevant specification, SOP, or contract — e.g., "Per SOP-012, the service must return HTTP 202 within 500ms"]

---

## Actual State

- [Describe the observed, incorrect behavior precisely]
- [Include exact error messages, stack traces, or log output — do not paraphrase]

**Error / Log Output:**

```
[Paste exact output here. Truncate only if >100 lines; always include the root exception and full traceback.]
```

---

## Supporting Artifacts

- [ ] Screenshot or recording attached
- [ ] Log file attached (filtered to relevant time window)
- [ ] Monitoring dashboard link: [URL]
- [ ] Related tickets: [BUG-####, FEAT-####]
