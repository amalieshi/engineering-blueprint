# Technical Risk Analysis

**Document ID:** [RA-####]
**System / Component:** [e.g., `patient-data-pipeline`, `dicom-ingest-service v2`]
**Analysis Trigger:** [New Design / Architecture Change / Pre-Release Review / Incident Response / Periodic Review]
**Author:** [Name]
**Date:** [YYYY-MM-DD]
**Version:** [v1.0]
**Status:** [Draft / Under Review / Approved]

---

## Purpose and Scope

**What is being analyzed:** [Define the system, component, integration, or change being assessed]

**Analysis boundary:** [What is in scope — be explicit about which interfaces, data flows, and dependencies are covered]

**Exclusions:** [What is explicitly out of scope and why — e.g., "Third-party PACS system internals are excluded; risk at the integration boundary is covered under EXT-01"]

**Risk acceptance authority:** [The role or individual who holds authority to accept residual risk — e.g., Engineering Lead, Data Owner, Compliance Officer]

---

## Risk Assessment Criteria

### Severity Scale

| Rating | Label | Description |
|---|---|---|
| 5 | Catastrophic | Unrecoverable data loss, patient safety impact, regulatory violation, or system-wide outage |
| 4 | Critical | Significant data corruption, SLA breach, or service failure requiring emergency intervention |
| 3 | Serious | Partial loss of function, degraded output, or significant manual remediation effort |
| 2 | Minor | Limited impact, recoverable, workaround available without data integrity risk |
| 1 | Negligible | Cosmetic or trivial; no meaningful operational consequence |

### Likelihood Scale

| Rating | Label | Description |
|---|---|---|
| 5 | Almost Certain | Expected to occur; observed in similar systems or previous iterations |
| 4 | Likely | Will probably occur under foreseeable operating conditions |
| 3 | Possible | May occur; triggered by specific or non-routine conditions |
| 2 | Unlikely | Requires unusual circumstances; low historical frequency |
| 1 | Rare | Theoretically possible; no known precedent in similar systems |

**Risk Score = Severity × Likelihood**

| Score Range | Risk Level | Required Response |
|---|---|---|
| 20–25 | Extreme | Do not proceed. Risk must be eliminated or reduced before deployment. |
| 12–19 | High | Corrective control required. Document owner and deadline. |
| 6–11 | Medium | Mitigation recommended. Monitor closely post-deployment. |
| 1–5 | Low | Accept with documentation. Include in periodic review. |

---

## Risk Register

### Data Integrity Risks

| ID | Risk Description | Severity | Likelihood | Score | Risk Level | Control / Mitigation | Residual Score | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| DI-01 | [e.g., Schema drift in upstream feed causes silent field truncation in the transformation layer, producing incorrect output without an exception] | [e.g., 5] | [e.g., 3] | [e.g., 15] | High | [e.g., Strict schema validation at ingestion boundary using Pydantic / JSON Schema; reject and dead-letter non-conforming records; alert on rejection rate spike] | [e.g., 5] | [Name] | [Open / Mitigated / Accepted] |
| DI-02 | [e.g., Deduplication key collision allows a replayed message to overwrite a newer record] | | | | | | | [Name] | |
| DI-03 | [e.g., PHI retained in intermediate queue beyond the 24h policy retention window] | | | | | | | [Name] | |

### System Availability Risks

| ID | Risk Description | Severity | Likelihood | Score | Risk Level | Control / Mitigation | Residual Score | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| SA-01 | [e.g., Single-node Redis instance failure causes complete pipeline stall with no fallback path] | [e.g., 4] | [e.g., 2] | [e.g., 8] | Medium | [e.g., Deploy Redis in cluster mode with 2 replicas; implement circuit breaker with fallback to synchronous processing; alert on replica lag] | [e.g., 4] | [Name] | [Open] |
| SA-02 | [e.g., Kubernetes node pool exhaustion under peak load with no autoscaler headroom] | | | | | | | [Name] | |
| SA-03 | [e.g., Downstream database connection pool exhaustion causing write failures under burst ingestion] | | | | | | | [Name] | |

### External Dependency Risks

| ID | Risk Description | Severity | Likelihood | Score | Risk Level | Control / Mitigation | Residual Score | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| EXT-01 | [e.g., Upstream HL7 sender changes message structure without notification, breaking the parsing contract] | [e.g., 4] | [e.g., 4] | [e.g., 16] | High | [e.g., Validate against registered conformance statement at receive time; dead-letter non-conforming messages; weekly conformance statement review cadence with upstream team] | [e.g., 8] | [Name] | [Open] |
| EXT-02 | [e.g., Third-party API rate limit causes message backlog and processing delay breaching SLA] | | | | | | | [Name] | |
| EXT-03 | [e.g., Cloud provider AZ outage affecting primary deployment region] | | | | | | | [Name] | |

### Security and Compliance Risks

| ID | Risk Description | Severity | Likelihood | Score | Risk Level | Control / Mitigation | Residual Score | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| SEC-01 | [e.g., PHI exposed in structured log output via unmasked field logging in the transformation step] | [e.g., 5] | [e.g., 3] | [e.g., 15] | High | [e.g., Implement log sanitizer middleware; define an allowlist of loggable fields; static analysis rule to block PHI field names in log statements] | [e.g., 5] | [Name] | [Open] |
| SEC-02 | [e.g., Service account credentials with excessive permissions used for database writes] | | | | | | | [Name] | |
| SEC-03 | [e.g., Insecure deserialization of external message payload enabling injection attack] | | | | | | | [Name] | |

### Operational Risks

| ID | Risk Description | Severity | Likelihood | Score | Risk Level | Control / Mitigation | Residual Score | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| OPS-01 | [e.g., No runbook for the most common failure modes; recovery depends on tribal knowledge] | [e.g., 3] | [e.g., 4] | [e.g., 12] | High | [e.g., Runbook completion is a launch gate; peer review required; stored in `docs/runbooks/`] | [e.g., 4] | [Name] | [Open] |
| OPS-02 | [e.g., Deployment pipeline failure during a live incident prevents hotfix delivery] | | | | | | | [Name] | |

---

## Risk Summary

| Risk Level | Count | IDs |
|---|---|---|
| Extreme (20–25) | [#] | [e.g., None] |
| High (12–19) | [#] | [e.g., DI-01, EXT-01, SEC-01, OPS-01] |
| Medium (6–11) | [#] | [e.g., SA-01] |
| Low (1–5) | [#] | [e.g., SA-01 (residual)] |

**Release recommendation:** [e.g., Conditional — the four High risks must be mitigated and verified before production deployment. No Extreme risks identified.]

---

## Residual Risk Acceptance

> Residual risk is the risk that remains after all planned controls are applied. Each residual risk above Low must be explicitly accepted by the appropriate authority.

| ID | Residual Risk Description | Residual Score | Accepted By | Date | Rationale |
|---|---|---|---|---|---|
| [e.g., DI-01] | [e.g., Residual risk of schema drift causing pipeline rejection — mitigated to detection within minutes via alert; no silent failure remains] | [e.g., 5] | [Name / Role] | [YYYY-MM-DD] | [e.g., Acceptable given the alert and dead-letter mechanism; no data loss path remains] |

---

## Risk Review Cadence

| Trigger | Action |
|---|---|
| Pre-deployment | Full risk register review; all High risks must have confirmed mitigations |
| Post-deployment (Day 1, Day 7) | Verify mitigations are operating as designed; update residual scores |
| Quarterly (steady state) | Re-assess likelihood ratings based on operational data |
| Any incident scoring Severity >= 3 | Immediate review of affected risk entries; update or add rows as required |
| Architecture or dependency change | Re-assess any risks where the control or the threat model has changed |

---

## Approval

| Role | Name | Approval | Date |
|---|---|---|---|
| Author | [Name] | | [YYYY-MM-DD] |
| Engineering Lead | [Name] | | [YYYY-MM-DD] |
| Data Owner / Quality | [Name] | | [YYYY-MM-DD] |

---

## Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| v1.0 | [YYYY-MM-DD] | [Name] | Initial risk analysis |
| v1.1 | [YYYY-MM-DD] | [Name] | [e.g., Post-deployment update; residual scores revised based on Day 7 operational data] |
