# Architecture

- Architecture status: draft project template
- Current system: documentation structure and checker; no application
- Target application architecture: TBD(project)
- Related: [product baseline](../product/project-specification.md),
  [roadmap](../roadmap.md), [ADRs](decisions/README.md)

Populate all twelve views. Label current and target state separately. A short
"not applicable" with a reason is better than speculative infrastructure.

## 1. Introduction and goals

TBD(project): Explain the product objective, stakeholders, and prioritized
quality goals. Link requirements instead of maintaining a competing product
specification.

## 2. Architecture constraints

TBD(project): Record binding organizational/technical constraints separately
from proposed choices. Cover supported environments, security, budget,
integration, and delivery restrictions that affect the architecture.

## 3. Context and scope

TBD(project): Show users and external systems, exchanged information, data
authority, and trust boundaries. Separate the system being built from its source
host, task tracker, development tools, and deployment environment.

## 4. Solution strategy

TBD(project): Explain the small set of design choices that address the quality
goals and constraints. Link their ADRs and evidence dependencies. Avoid selecting
layers, frameworks, or infrastructure without a reason.

## 5. Building-block view

TBD(project): Describe each meaningful component's responsibility, public
interfaces, dependencies, data ownership, runtime interactions, deployment
location, and quality/security considerations. Keep cohesive boundaries and
explicit dependency direction.

| Component | Responsibility / interface | Dependencies / data owner | Current vs target |
| --- | --- | --- | --- |

## 6. Runtime view

TBD(project): Show representative success and failure sequences, authorization,
ordering, transactions, concurrency, idempotency, timeouts, retry, and recovery.
Link user journeys and behavioral contracts. Explain where external effects and
authoritative state changes occur.

## 7. Deployment view

TBD(project): Describe actual and planned processes, machines/services,
installation, networking, storage, secrets, trust zones, and supported platforms.
A code module is not necessarily a deployment unit. Do not claim a service or
installer exists before it is implemented and checked.

## 8. Cross-cutting concepts

TBD(project): Cover validation, identity, permissions, configuration, structured
logging/correlation, privacy, error handling, versioning, persistence/migrations,
testing, and observability where relevant. Define shared concepts without
duplicating component-specific details.

## 9. Architecture decisions

Use the [ADR index](decisions/README.md) and [record template](decisions/adr-template.md).
TBD(project): Create consequential project decisions with alternatives,
consequences, status, due boundary, and evidence. An accepted decision can remain
unimplemented.

## 10. Quality requirements

TBD(project): Define prioritized `QA-NNN` scenarios with a stimulus, environment,
required response, measurable observation, and verification method. Mark targets
unmeasured until evidence exists.

| ID | Stimulus / environment | Required response | Verification / status |
| --- | --- | --- | --- |

## 11. Risks and technical debt

TBD(project): State feasibility gaps, failure/security risks, known drift, and
deliberate tradeoffs. Link an OD, experiment, issue, or step that owns resolution.
Separate existing debt from hypothetical concerns.

## 12. Glossary

Use the [domain glossary](../product/glossary.md) for shared terms.
TBD(project): Add architecture-specific terms here only when needed; link rather
than redefine domain terms.
