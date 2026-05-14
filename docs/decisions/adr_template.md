# ADR-NNNN: [Short Decision Title]

**Date:** YYYY-MM-DD  
**Status:** Proposed | Accepted | Deprecated | Superseded by [ADR-NNNN]  
**Deciders:** [Name(s)]

---

## Context

Describe the situation, the problem being solved, and the forces at play. Include relevant constraints (technical, organisational, time). Be specific — vague context produces vague decisions.

*Example: The pipeline ingests HL7v2 messages from three hospital systems at a peak rate of ~2,000 messages/minute. The current synchronous processing model is creating a backlog under load, and message delivery guarantees are not met when the transform service is restarted.*

---

## Decision

State the decision clearly in one or two sentences.

*Example: We will introduce Apache Kafka as a message broker between the ingest and transform layers, replacing the current direct HTTP call model.*

---

## Considered Alternatives

List every option that was seriously considered, including the one that was rejected. For each:

### Option A — [Name]

**Summary:** What it involves.  
**Pros:** What it does well for this problem.  
**Cons / Risks:** What it doesn't do well, or what it costs.

### Option B — [Name]

**Summary:**  
**Pros:**  
**Cons / Risks:**

---

## Consequences

### Positive

- What improves as a result of this decision.

### Negative / Trade-offs

- What we give up or accept as a known cost.

### Risks and Mitigations

- Identified risks and the mitigations in place.

---

## Implementation Notes

Any specifics that guide implementation: configuration defaults, migration steps, phasing, rollback plan.

---

## References

- Link to relevant design docs, RFCs, or issue threads.
- Link to superseded ADRs if applicable.
