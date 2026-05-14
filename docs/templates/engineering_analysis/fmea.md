# Failure Mode and Effects Analysis (FMEA)

**Document ID:** [FMEA-####]
**System / Component:** [e.g., `dicom-ingest-service`, `patient-merge-pipeline`]
**FMEA Type:** [Design FMEA (DFMEA) / Process FMEA (PFMEA)]
**Author:** [Name]
**Date:** [YYYY-MM-DD]
**Version:** [v1.0]
**Review Status:** [Draft / Under Review / Approved]
**Applicable Standard:** [e.g., IEC 60812, ISO 14971]

---

## Scope

**System boundary:** [Define exactly what is and is not included in this analysis]

**Analysis objective:** [e.g., "Identify failure modes in the DICOM tag normalization step that could result in incorrect study routing or PHI exposure"]

**Exclusions:** [e.g., "Network infrastructure, upstream PACS system, and storage backend are out of scope — covered by separate FMEAs"]

---

## Severity / Occurrence / Detection Rating Scales

### Severity (S)

| Rating | Category | Description |
|---|---|---|
| 9–10 | Catastrophic | Patient safety impact, regulatory violation, data loss with no recovery path |
| 7–8 | Critical | Significant system failure, data corruption, SLA breach with major business impact |
| 5–6 | Major | Partial loss of function, degraded output quality, manual intervention required |
| 3–4 | Minor | Reduced performance, minor inaccuracy, workaround exists |
| 1–2 | Negligible | Minimal impact, cosmetic, no effect on system integrity or output |

### Occurrence (O)

| Rating | Category | Approximate Frequency |
|---|---|---|
| 9–10 | Almost Certain | > 1 in 10 events |
| 7–8 | High | 1 in 10 to 1 in 100 |
| 5–6 | Moderate | 1 in 100 to 1 in 1,000 |
| 3–4 | Low | 1 in 1,000 to 1 in 10,000 |
| 1–2 | Remote | < 1 in 10,000 |

### Detection (D)

| Rating | Category | Description |
|---|---|---|
| 9–10 | Undetectable | No current control exists; failure reaches the end user undetected |
| 7–8 | Very Low | Detection relies on downstream complaint or manual audit |
| 5–6 | Moderate | Detected by periodic monitoring or test coverage with known gaps |
| 3–4 | High | Detected by automated test suite or continuous monitoring |
| 1–2 | Very High | Failure is immediately and reliably detected before impact |

**Risk Priority Number (RPN) = S × O × D**

> RPN >= 100: Immediate corrective action required before release.
> RPN 50–99: Action required; assign owner and target date.
> RPN < 50: Monitor; document and review at next cycle.

---

## FMEA Table

| ID | Item / Function | Potential Failure Mode | Potential Effect of Failure | S | Potential Cause of Failure | O | Current Controls (Prevention / Detection) | D | RPN | Recommended Action | Responsibility | Target Date | Action Taken | Revised S | Revised O | Revised D | Revised RPN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FM-01 | [e.g., DICOM tag normalization] | [e.g., Modality tag (0008,0060) mapped to incorrect value] | [e.g., Study routed to wrong reading worklist; incorrect clinical workflow triggered] | [e.g., 8] | [e.g., Missing entry in normalization lookup table for non-standard sender modality string] | [e.g., 5] | [e.g., Prevention: lookup table review process / Detection: integration test for known modalities] | [e.g., 6] | [e.g., 240] | [e.g., Add validation against DICOM conformance statement at receive time; alert on unmapped modality string] | [Name] | [YYYY-MM-DD] | [Describe action taken] | [#] | [#] | [#] | [#] |
| FM-02 | [Item / function] | [Failure mode] | [Effect] | | [Cause] | | [Controls] | | | [Action] | [Name] | [YYYY-MM-DD] | | | | | |
| FM-03 | | | | | | | | | | | | | | | | | |

*Add rows as needed. Each row represents one failure mode of one item or function.*

---

## Summary of High-Priority Items

> List all items where RPN >= 100 or Severity >= 9. These require resolution before the system is considered safe to deploy.

| ID | Failure Mode | RPN | Action | Owner | Status |
|---|---|---|---|---|---|
| FM-01 | [Failure mode summary] | [RPN] | [Corrective action summary] | [Name] | [Open / In Progress / Closed] |

---

## Review and Approval

| Role | Name | Signature / Approval | Date |
|---|---|---|---|
| Author | [Name] | | [YYYY-MM-DD] |
| Technical Reviewer | [Name] | | [YYYY-MM-DD] |
| Quality / Compliance | [Name] | | [YYYY-MM-DD] |

---

## Revision History

| Version | Date | Author | Change Summary |
|---|---|---|---|
| v1.0 | [YYYY-MM-DD] | [Name] | Initial FMEA |
| v1.1 | [YYYY-MM-DD] | [Name] | [e.g., Revised FM-01 post corrective action; RPN reduced] |
