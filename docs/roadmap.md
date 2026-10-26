# Delivery roadmap

Project mode: uninitialized. No application implementation step is active.
The first task is to initialize the documentation from the owner's application
description using [the bootstrap guide](guides/bootstrap.md).

This index owns delivery order and status. Step documents own prerequisites,
scope, criteria, evidence, and acceptance. The status text must match exactly.

| Step | Outcome | Status |
| --- | --- | --- |
| [Step 0](roadmap/step-0-documentation-baseline.md) | Reviewable product, architecture, decisions, and delivery baseline | planned |

## Derive the delivery sequence

TBD(project): Add application-specific steps in dependency order after the
product discussion. Use [the step template](roadmap/step-template.md). Do not
inherit the number, stack, integration sequence, or acceptance results of the
source projects.

Keep step IDs stable. The table order is delivery order; it need not be numeric
after insertions/deferrals. At most one step is selected as `active` or
`blocked` in this baseline. Parallel delivery requires an explicit policy change.

A completed step does not automatically activate the next one. Start and close
steps only after checking their due ODs/proposed ADRs and recording the relevant
owner direction. See [sequencing and done](roadmap/sequencing-and-done.md).
