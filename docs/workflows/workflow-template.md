# Workflow contract template

- Name / version: unset
- Status: proposed
- Authority: unset
- Related requirements / journeys / ADRs: unset
- Implementation / conformance evidence: none

## Purpose and boundary

State whose behavior is modeled, what it owns, what remains external, and
whether this is a design contract or executable runtime configuration.

## Vocabulary and data

Define stable states/events, normalized references, payload/schema validation,
versioning, data authority, permissions, and relevant correlation IDs.

## Transitions and effects

For each transition, specify source, trigger, guard, destination, effects,
transaction/effect ordering, and observable evidence. Do not rely on model text
or unverified callbacks as authoritative facts.

## Failure and concurrency semantics

Describe duplicates, stale/out-of-order input, retries, partial effects,
timeouts, cancellation, ownership/leases, reconciliation, and terminal paths.

## Examples and conformance

Give representative success/failure/recovery traces. State the tests and
structural checks that keep implementation, prose, and diagrams aligned.
