# Scope Management Plan

**Project:** [Project Name]
**Version:** [v1.0]
**Owner:** [Name]
**Date:** [YYYY-MM-DD]
**Status:** [Draft / Active / Closed]

---

## Purpose

This document defines the boundaries of the pipeline or system under development, the process for validating and controlling scope, and the explicit demarcation of what the system will and will not do. It is the authoritative reference for scope disputes and change request evaluation.

---

## Scope Definition

### In Scope

> What the system will do. Be specific: name the data sources, transformation logic, output targets, and consumers.

- [e.g., Ingest HL7 v2.5 ADT messages from the upstream HIS via TCP MLLP connection on port 2575]
- [e.g., Normalize patient demographic fields to the internal canonical schema defined in `docs/schemas/patient_canonical.json`]
- [e.g., Write validated records to the `patients_staging` table in PostgreSQL 16 — schema defined in `migrations/`]
- [e.g., Emit structured processing events to the `pipeline.audit` Kafka topic for downstream audit consumption]
- [e.g., Expose a `/health` and `/metrics` endpoint for operational monitoring — no business logic endpoints]

### Out of Scope

> What the system will explicitly not do. This list is as important as the in-scope list.

- [e.g., This pipeline does not perform MPI (Master Patient Index) matching — identity resolution is owned by the identity service]
- [e.g., This pipeline does not archive raw HL7 messages — archival is the responsibility of the integration engine upstream]
- [e.g., This system does not expose a real-time query API; it is write-only]
- [e.g., No transformation of DICOM imaging data — DICOM routing is handled by a separate subsystem and is explicitly excluded]
- [e.g., No user-facing UI — operational visibility is provided exclusively via the monitoring dashboard]

---

## Scope Validation

### Acceptance Criteria

> The conditions that must be met for the delivered system to be considered complete and within scope.

| ID | Criterion | Verification Method |
|---|---|---|
| AC-01 | [e.g., All ADT A01, A08, and A28 message types processed without error under normal load] | [Automated integration test suite — `pytest tests/integration/ -m adt`] |
| AC-02 | [e.g., Data latency from HIS receipt to staging write < 3 seconds at P95 under sustained 500 msg/s load] | [Load test benchmark report — `tests/load/k6_ingest_load.js`] |
| AC-03 | [e.g., Schema validation rejects records missing required fields and emits a structured error log entry with correlation ID] | [Unit tests — `pytest tests/unit/test_schema_validation.py`] |
| AC-04 | [e.g., Zero data loss under simulated upstream MLLP reconnect within a 30-second outage window] | [Chaos test — `tests/chaos/reconnect_test.py`] |
| AC-05 | [e.g., Service recovers to full processing capacity within 60 seconds of a graceful restart] | [Operational runbook procedure + timed manual test] |

### Validation Process

1. **Requirement traceability:** Every acceptance criterion maps to a specific requirement in the PRD or SOP. Orphaned tests are not accepted at the release gate.
2. **Sign-off gate:** Scope is considered validated only after the engineering lead, data owner, and QA lead approve the acceptance test results in writing.
3. **Automated regression:** Acceptance criteria are encoded as CI pipeline gates. A failing gate blocks the release branch merge with no exceptions.

---

## Scope Control

### Change Control Trigger

Any of the following constitutes a scope change and requires a formal Change Request (see [templates/software_tracking/change_request.md](../software_tracking/change_request.md)):

- Addition of a new data source, message type, or consumer not listed in the In Scope section
- Modification of the output schema or any downstream data contract
- Change to a stated non-functional requirement (latency, throughput, availability, retention)
- Removal of a previously committed deliverable

### Change Evaluation Criteria

A proposed scope change is evaluated against:

- **Schedule impact:** Does this extend the delivery timeline? By how much, in concrete days or sprints?
- **Resource impact:** Does this require additional headcount, infrastructure, or budget?
- **Technical risk:** Does this introduce new dependencies or increase system complexity in a way that affects reliability?
- **Downstream impact:** Does this require changes to consuming systems or data contracts?

### Approval Authority

| Change Size | Approver |
|---|---|
| Minor (no schedule or resource impact) | Engineering Lead |
| Moderate (< 1 sprint of additional work) | Engineering Lead + Project Sponsor |
| Major (> 1 sprint of work or external dependency change) | Engineering Lead + Project Sponsor + affected stakeholder sign-off |

---

## Scope Baseline

> Record the approved scope at each significant milestone. This provides an audit trail for scope drift.

| Version | Date | Change Summary | Approved By |
|---|---|---|---|
| v1.0 | [YYYY-MM-DD] | Initial scope definition and acceptance criteria | [Name] |
| v1.1 | [YYYY-MM-DD] | [e.g., Added support for ADT A34 patient merge event per CR-0012] | [Name] |
