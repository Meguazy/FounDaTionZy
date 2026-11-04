# Step N: Observable outcome

Status: planned

## Intent

State the user/system outcome and why it follows the preceding work. Link
requirements, quality scenarios, and relevant decisions.

## Required context

Link the canonical sources needed for this outcome: requirements/journeys,
architecture sections and workflow contracts, binding ADRs and relevant ODs,
code/tests, and development or operations gates. Use section links and stable
IDs, and explain each dependency. For a large step, group references by increment.
For a compound invariant, identify its trigger and link all clauses governing
preserved/invalidated state and effects; avoid broad topic labels alone.

| Concern / increment | Canonical source / section / IDs | Why needed |
| --- | --- | --- |

Apply [the reading protocol](../README.md#required-reading-order) as well.
Maintain these references as scope and dependencies change. Missing references
require discovery; this map does not narrow the common core or step-boundary audit.

## Prerequisites

Name prior deliverables, evidence, dependencies, capabilities, and safe test
fixtures required before implementation.

## Start decisions

Enumerate all unresolved ODs/proposed ADRs due at `Step N start`. Resolve
blocking items with the owner and record answers before beginning.

## Deliverables

Describe a bounded vertical slice across the components required by the outcome.

## Non-goals

State what this step deliberately does not implement, including later behavior.

## Exit criteria

Use observable pass/fail conditions, failure/recovery scenarios, and appropriate
real/fake integration boundaries. Do not equate file creation with capability.

## Exit decisions

Enumerate ODs/proposed ADRs due at `Step N exit` and any new decisions
introduced during implementation.

## Validation and evidence

Link exact commands, revision/tree, environment, dependencies, outcomes/counts,
sanitized artifacts, failures/skips/not-run gates, and limits. Assess each exit
criterion explicitly.

Keep the current criterion assessments, applicable evidence and remaining gaps
concise here. Put detailed attempts and validation/work records beside the step
and link them, following [current state and history](../guides/current-state-and-history.md).
Preserve failed and unavailable required gates in the current assessment.

## Exit review

Summarize delivered behavior, remaining gaps, decisions, risks, and the proposed
scope for owner acceptance. Copy/adapt
[the exit-review template](../templates/exit-review-template.md) if useful.

## Owner acceptance

Pending. Record actual authority, date, direction, accepted scope, and limits.
A merge does not fill this section automatically.
