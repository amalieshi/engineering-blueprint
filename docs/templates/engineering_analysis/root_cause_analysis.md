# Root Cause Analysis (RCA)

**Document ID:** [RCA-####]
**Related Incident / Ticket:** [INC-#### / BUG-####]
**System / Component:** [e.g., `patient-merge-pipeline`, `dicom-router`]
**Author:** [Name]
**Date of Incident:** [YYYY-MM-DD HH:MM UTC]
**Date of RCA:** [YYYY-MM-DD]
**Status:** [Draft / Under Review / Approved / Closed]

---

## Problem Statement

> Define the problem with precision. A vague problem statement produces a vague root cause. Quantify the impact.

- **What failed:** [Describe the observable failure — not the cause, the symptom]
- **When it started:** [YYYY-MM-DD HH:MM UTC — include timezone]
- **When it was detected:** [YYYY-MM-DD HH:MM UTC — note if detection was delayed]
- **When it was resolved:** [YYYY-MM-DD HH:MM UTC]
- **Duration:** [e.g., 2h 14m]
- **Impact scope:** [e.g., All DICOM studies ingested between 14:30–16:44 UTC were routed to the wrong worklist; approximately 340 studies affected]
- **Data integrity:** [e.g., No data loss — studies were mis-routed but recoverable / or: 12 records permanently corrupted]
- **Users / systems affected:** [e.g., Radiologists at 3 sites; downstream RIS system]

---

## Immediate Containment Action

> Describe the action taken to stop the bleeding — not the fix, the triage. Include who did what and when.

| Action | Owner | Time Taken |
|---|---|---|
| [e.g., Disabled the normalization service to halt further mis-routing] | [Name] | [YYYY-MM-DD HH:MM UTC] |
| [e.g., Notified affected site coordinators to hold worklist review pending reprocessing] | [Name] | [YYYY-MM-DD HH:MM UTC] |
| [e.g., Identified affected study UIDs from audit log and flagged for reprocessing] | [Name] | [YYYY-MM-DD HH:MM UTC] |

---

## Incident Timeline

| Time (UTC) | Event |
|---|---|
| [HH:MM] | [e.g., Deployment of v2.4.1 completed] |
| [HH:MM] | [e.g., First mis-routed study recorded in audit log] |
| [HH:MM] | [e.g., Radiologist at Site A reported missing study via helpdesk] |
| [HH:MM] | [e.g., On-call engineer paged; investigation begins] |
| [HH:MM] | [e.g., Root cause identified: missing modality entry in lookup table] |
| [HH:MM] | [e.g., Normalization service disabled; containment complete] |
| [HH:MM] | [e.g., Hotfix deployed; reprocessing job initiated] |
| [HH:MM] | [e.g., All affected studies confirmed re-routed correctly; service restored] |

---

## 5 Whys Analysis

> Start from the confirmed symptom and ask "why" until you reach the systemic root cause. Each answer must be evidenced, not inferred.

| Level | Question | Answer | Evidence |
|---|---|---|---|
| Why 1 | Why did studies route to the wrong worklist? | [e.g., The Modality tag value `DX` was not present in the routing lookup table] | [e.g., Database query result showing null return for key `DX`] |
| Why 2 | Why was `DX` missing from the lookup table? | [e.g., The lookup table was seeded from the previous site's conformance statement, which did not include Digital Radiography] | [e.g., Seed script `db/seeds/modality_lookup.sql` — last updated 2024-11-03] |
| Why 3 | Why was the conformance statement incomplete? | [e.g., The new sending device was added to the network after the initial integration, and no update process existed to re-validate the lookup table] | [e.g., Change request CR-0031 — no lookup table validation step in the onboarding checklist] |
| Why 4 | Why was there no update process? | [e.g., The lookup table was not treated as a managed configuration artifact — it was a one-time seed with no version control or review gate] | [e.g., Absence of lookup table in `config/` versioning; no entry in change management SOP] |
| Why 5 | Why was it not version-controlled or reviewed? | [e.g., The system was designed under the assumption that the set of sending modalities was fixed; no process existed for handling new device onboarding post-go-live] | [e.g., Architecture decision record ADR-0007 — no multi-sender extensibility requirement was captured] |

---

## Fishbone (Ishikawa) Analysis

> Use this section for complex failures where multiple contributing cause categories are present. Mark with [PRIMARY] the cause confirmed as the root.

```
                          EFFECT: [State the failure effect here]
                                         |
        ┌──────────────────────────────────────────────────────────────┐
        |                                                              |
   [People]                                                      [Process]
   - [e.g., On-call runbook did not                - [PRIMARY] No device onboarding
     include lookup table validation step]           checklist or re-validation gate
   - [e.g., No second reviewer for                - [e.g., Lookup table treated as
     lookup table changes]                          static data, not managed config]
        |                                                              |
        └──────────────────────────┬───────────────────────────────────┘
                                   |
        ┌──────────────────────────┴───────────────────────────────────┐
        |                                                              |
  [Technology]                                                [Measurement]
  - [e.g., No schema validation on                - [e.g., No alert on unknown
    the lookup table at startup]                    modality value received]
  - [e.g., Routing logic did not                 - [e.g., Mis-routing not
    fail fast on unmapped keys]                    detected until user report]
        |                                                              |
        └──────────────────────────────────────────────────────────────┘
```

---

## Root Cause Statement

> A single, precise statement of the confirmed root cause. This is the thing that, if fixed, would prevent recurrence.

**Root cause:** [e.g., "The DICOM modality routing lookup table was treated as a static seed artifact with no version control, update process, or onboarding gate — resulting in unchecked configuration drift when new sending devices were added post-deployment."]

**Contributing factor(s):**

- [e.g., No alerting on unmapped modality values, delaying detection by 2h 14m]
- [e.g., Conformance statement review was not a documented step in the device onboarding checklist]

---

## Corrective Action Plan

> Actions that fix the confirmed root cause. These are not workarounds.

| ID | Action | Type | Owner | Due Date | Status |
|---|---|---|---|---|---|
| CA-01 | [e.g., Migrate the modality lookup table into versioned configuration under `config/modality_lookup.yaml`; add to deployment pipeline validation] | Corrective | [Name] | [YYYY-MM-DD] | [Open] |
| CA-02 | [e.g., Add startup validation: service must fail fast if any received modality key is absent from the lookup table] | Corrective | [Name] | [YYYY-MM-DD] | [Open] |
| CA-03 | [e.g., Create a device onboarding checklist that includes conformance statement review and lookup table update as mandatory gates] | Preventive | [Name] | [YYYY-MM-DD] | [Open] |
| CA-04 | [e.g., Add alert: trigger on unmapped modality key received; P2 severity] | Preventive | [Name] | [YYYY-MM-DD] | [Open] |

**Type definitions:**
- **Corrective** — directly eliminates the root cause
- **Preventive** — eliminates a contributing factor or detection gap to prevent recurrence of this class of failure

---

## Verification of Effectiveness

> Define how you will confirm that corrective actions have worked. Specify the observable evidence, not just "the fix was deployed."

| CA ID | Verification Method | Success Criteria | Review Date |
|---|---|---|---|
| CA-01 | [e.g., Deploy to staging; verify config-driven lookup loads correctly; confirm version appears in service startup log] | [e.g., No hardcoded lookup table in database seed scripts; config file present in repository under version control] | [YYYY-MM-DD] |
| CA-02 | [e.g., Integration test: send a study with an unmapped modality key; verify service rejects with a structured error and does not route] | [e.g., Test passes in CI; no silent mis-routing observed in staging for 5 business days] | [YYYY-MM-DD] |
| CA-03 | [e.g., Onboarding checklist executed for the next new device addition; checklist completion record reviewed by Engineering Lead] | [e.g., Signed checklist on file; no routing anomalies detected post-onboarding] | [YYYY-MM-DD] |
| CA-04 | [e.g., Confirm alert fires in staging when test request with unknown modality is sent] | [e.g., Alert received within 60 seconds; P2 ticket auto-created] | [YYYY-MM-DD] |

---

## Lessons Learned

- [e.g., Configuration artifacts that gate system behavior must be treated as code — versioned, reviewed, and tested — not as one-time seed data]
- [e.g., Fail-fast behavior at system boundaries is non-negotiable; silent failures are more costly than loud ones]
- [e.g., Device onboarding is a change event that requires a structured process, not an operational task handled informally]

---

## Approval

| Role | Name | Approval | Date |
|---|---|---|---|
| Author | [Name] | | [YYYY-MM-DD] |
| Engineering Lead | [Name] | | [YYYY-MM-DD] |
| Quality / Compliance | [Name] | | [YYYY-MM-DD] |
