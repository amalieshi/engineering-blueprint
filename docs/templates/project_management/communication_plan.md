# Communication Plan

**Project:** [Project Name]
**Version:** [v1.0]
**Owner:** [Name]
**Date:** [YYYY-MM-DD]

---

## Purpose

This document defines who receives what information, at what frequency, and through which delivery mechanism. The goal is to eliminate both communication gaps and over-communication with equal discipline — information reaches the stakeholder who needs it, in the format most useful to them, on the schedule they require.

---

## Stakeholder Register

| ID | Stakeholder / Role | Interest | Influence | Communication Need |
|---|---|---|---|---|
| S-01 | [Engineering Lead] | Technical accuracy, delivery timeline | High | Detailed technical status, active blockers, architecture decisions |
| S-02 | [Project Sponsor / Product Owner] | Business outcomes, budget, schedule | High | Summary progress, risk escalations, scope change decisions |
| S-03 | [Data Owner / Clinical Informatics] | Data quality, schema compliance, DICOM conformance | Medium | Data validation reports, schema change notifications |
| S-04 | [Platform / Infrastructure Team] | Resource utilization, deployment readiness | Medium | Infrastructure requirements, deployment schedules, incident alerts |
| S-05 | [QA / Test Lead] | Test coverage, defect status, release readiness | Medium | Test results, defect trends, release gate status |
| S-06 | [Downstream Consumer Team] | API stability, contract changes, pipeline availability | Low | Breaking change notifications, planned downtime schedules |

---

## Communication Matrix

| ID | Communication Type | Content | Audience | Frequency | Owner | Delivery Mechanism |
|---|---|---|---|---|---|---|
| C-01 | Engineering Sync | Sprint progress, active blockers, technical decisions in-flight | S-01, S-05 | Weekly | Engineering Lead | Standing meeting (30 min) |
| C-02 | Stakeholder Status Report | Milestone status (RAG), risks, decisions required from sponsor | S-02 | Bi-weekly | Project Lead | Email report or Confluence page |
| C-03 | Operational Dashboard | Pipeline health, ingestion rates, error rates, SLA metrics | S-01, S-03, S-04 | Real-time (continuous) | Engineering Team | Grafana / observability dashboard |
| C-04 | Incident Notification | Incident declaration, impact scope, affected systems, ETA to resolution | S-01, S-02, S-04 | As-needed — P1/P2 within 15 minutes of declaration | On-call Engineer | PagerDuty alert + Slack `#incidents` |
| C-05 | Incident Post-Mortem | Root cause, timeline, corrective actions, owners | S-01, S-02, S-04, S-05 | Within 48h of incident close | Engineering Lead | Written report distributed via email |
| C-06 | Schema / Contract Change Notice | Proposed change, impact, effective date, required consumer action | S-03, S-06 | As-needed — minimum 5 business days notice before deployment | Data Engineer | Email + PR description with migration guide |
| C-07 | Release Notification | Version deployed, changes included, rollback status | S-01, S-02, S-04, S-05, S-06 | Per release | Engineering Lead | Slack `#deployments` + release notes in repo |
| C-08 | Risk Escalation | Risk at Score >= 6, proposed mitigation, decision required | S-02 | Within 24h of identification | Risk Owner | Direct message + follow-up email |
| C-09 | Architecture Decision Record (ADR) | Design decision, alternatives considered, rationale, consequences | S-01, S-03 | As-needed | Engineering Lead | Pull request to `docs/adr/` in repository |

---

## Delivery Mechanisms

| Mechanism | Tool | Appropriate Use |
|---|---|---|
| Standing meeting | [e.g., Google Meet / Teams] | Decisions, active blockers, collaborative problem-solving — not status recitation |
| Async status update | [e.g., Confluence / Notion] | Regular progress reporting; permanent record of milestone status |
| Real-time dashboard | [e.g., Grafana / Datadog] | Operational health monitoring — not a substitute for structured incident communication |
| Chat channel | [e.g., Slack / Teams] | Low-latency operational coordination, incident response, informal questions |
| Email | [e.g., Outlook / Gmail] | Formal notifications, external stakeholders, decisions requiring an audit trail |
| Pull request | GitHub | Technical review, architecture decisions, code and configuration changes |

---

## Escalation Path

1. **Blocker identified:** Engineer raises in the next engineering sync or async in `#[project-channel]` with a written summary.
2. **Unresolved within 24h:** Engineering Lead escalates to Project Sponsor in writing with a clear statement of the blocker, options considered, and the decision required.
3. **Unresolved within 48h:** Project Sponsor facilitates an emergency decision meeting with the relevant stakeholders.
4. **Formal escalation:** If the decision requires executive authority or budget change, Project Sponsor escalates via established governance process.

---

## Communication Principles

- **Precision over frequency.** A well-structured bi-weekly report is more valuable than daily noise with no signal.
- **Decisions are documented.** Any decision made in a meeting is captured in writing within 24 hours — meeting notes, an ADR, or a ticket update.
- **No surprise scope changes.** Any scope alteration is communicated to all affected stakeholders before implementation begins.
- **Incident communication is non-negotiable.** P1/P2 incidents are communicated within 15 minutes of declaration, regardless of time zone or business hours.
- **Contract changes require lead time.** Schema and API changes that affect downstream consumers require a minimum 5-business-day notice window before deployment.
