# Feature Ideation

**Idea ID:** [FEAT-####]
**Author:** [Name]
**Date:** [YYYY-MM-DD]
**Status:** [Ideation / Under Review / Accepted / Deferred / Rejected]
**Target Domain:** [Ingestion / Transformation / Storage / API / Infrastructure / Observability]

---

## The Friction

> Describe the exact, observable technical problem being solved. Avoid solution language. Be specific: name the component, the failure mode, and the measurable cost.

- **Affected component:** [e.g., `dicom-router`, `patient-merge-pipeline`]
- **Failure mode / pain point:** [Precise description — e.g., "Tag normalization is performed per-message rather than batched, producing O(n) database round-trips under load exceeding 500 msg/s"]
- **Measurable cost:** [e.g., P99 latency of 4.2s against a 1.5s SLA; 18% error rate spike during peak ingestion windows observed in Grafana dashboard `api-latency`]
- **Current workaround (if any):** [Describe the manual intervention or tactical fix currently in place, and why it is not a permanent solution]

---

## The Hypothesis

> Describe the proposed architectural or implementation solution. This is a hypothesis subject to revision during design review.

### Proposed Approach

- [High-level description of the solution — e.g., "Introduce a stateful batching layer using Redis Streams to aggregate messages before dispatching to the normalization service, reducing DB call frequency by ~80%"]

### Architecture Delta

| Component | Current State | Proposed State |
|---|---|---|
| `[component-name]` | [e.g., Per-message synchronous DB write] | [e.g., Batch write via buffered queue, flushed every 500ms or 100 records] |
| `[component-name]` | [e.g., Not present] | [e.g., New Redis Streams consumer group — `normalization-batch-consumer`] |

### Expected Outcome

- [Quantified target tied directly to the friction metric — e.g., "Reduce P99 latency to <1.0s at 500 msg/s sustained throughput"]
- [Secondary benefits if any — e.g., "Reduces DB write amplification by ~80%; lowers connection pool contention"]

### Implementation Sketch

```
[Optional: ASCII diagram, pseudo-code, or data flow to anchor the discussion]

Example:
  Upstream → [MLLP Receiver] → Redis Streams → [Batch Consumer]
                                                      |
                                               [Normalization]
                                                      |
                                              PostgreSQL staging
```

---

## Constraints and Unknowns

### System Constraints

- **Infrastructure limits:** [e.g., Current Kubernetes node pool does not support horizontal scaling beyond 12 replicas without platform team approval]
- **Data contract limits:** [e.g., Upstream DICOM sender does not support chunked transfer; full payload must arrive before processing begins]
- **Regulatory / compliance constraints:** [e.g., PHI data must not persist in the intermediate queue beyond 24 hours per HIPAA retention policy — imposes a hard TTL on any buffer]
- **Existing SLA obligations:** [e.g., Downstream EHR system expects a response within 2s of DICOM receipt; the batching window must not violate this]

### Edge Cases

- [e.g., What happens if the batch buffer fills during a downstream outage? Risk of message loss or unbounded retry loop.]
- [e.g., Idempotency: if a message is replayed from the dead-letter queue, does the deduplication logic hold under the new batching scheme?]
- [e.g., Ordering: does the proposed architecture preserve message sequence guarantees required by the consumer?]

### Open Questions

- [ ] [e.g., Does the Redis Streams consumer group model support exactly-once delivery guarantees at this scale, or do we need a separate dedup layer?]
- [ ] [e.g., Who owns the operational burden of Redis in production — platform team or data engineering? This must be resolved before the design is accepted.]
- [ ] [e.g., What is the acceptable data loss window if Redis is lost between checkpoints?]

### Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [e.g., Redis becomes a new single point of failure] | High | Critical | [e.g., Deploy in cluster mode with sentinel; define circuit breaker to fall back to per-message processing] |
| [e.g., Batching introduces non-deterministic message ordering] | Medium | High | [e.g., Enforce sequence number from upstream sender; reject and dead-letter out-of-order batches] |
| [e.g., Increased complexity raises operational burden] | Medium | Medium | [e.g., Require runbook and alert coverage before launch; cross-train minimum one engineer] |

---

## Next Steps

- [ ] Present hypothesis to architecture review board
- [ ] Spike: prototype the batch consumer and benchmark against current baseline under simulated load
- [ ] Define acceptance criteria and add to scope management plan
- [ ] Identify owner and target sprint for implementation
