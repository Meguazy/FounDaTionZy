# Documentation map

**Repository mode: uninitialized project template.** Method guides and the
structural checker are usable; project documents still contain explicit
`TBD(project)` fields. The [roadmap](roadmap.md) owns delivery status.

## Required reading order

[AGENTS.md](../AGENTS.md) defines behavior and authorization rules. It directs
agents to this protocol. Establish the common core, then select a path by the
requested activity. A fresh session can use a bounded path once it establishes
the applicable constraints and dependencies.

### Common core

Before planning or editing:

1. Read [AGENTS.md](../AGENTS.md), this protocol and the canonical responsibilities
   below, and applicable [contribution rules](../CONTRIBUTING.md).
2. Read the [product baseline](product/project-specification.md) sections defining
   first-release scope, non-goals, domain invariants, authority, and constraints;
   read [architecture constraints](arc42/README.md#2-architecture-constraints)
   and [cross-cutting concepts](arc42/README.md#8-cross-cutting-concepts).
   Follow links to binding decisions. Use the [product index](product/README.md)
   to locate related journeys and vocabulary as needed.
3. Inspect the current branch and working-tree changes. Read the
   [roadmap](roadmap.md) and the selected step's status, scope, non-goals, and exit
   criteria.
   Check the [ADR index](arc42/decisions/README.md) and
   [OD register](open-decisions.md) for applicable constraints and blockers.

If no step is selected, use the explicitly authorized initialization or
maintenance scope; do not activate a step merely to perform that work.

### Reading paths

| Activity | Additional required reading |
| --- | --- |
| Initialization or adoption | Reconstruct the full baseline: product requirements, journeys and glossary; roadmap and step records; all twelve arc42 views and relevant ADRs; ODs and [workflow contracts](workflows/README.md); relevant [experiments](experiments/README.md), [development](development.md) and [operations](operations/README.md). Follow [bootstrap](guides/bootstrap.md) or [adoption](guides/adoption.md), inspecting existing code and evidence where present. |
| Bounded change or continuation | Read the requirements, architecture sections, contracts, decisions, code, tests and check commands involved in the requested outcome. Use the step's `Required context` map and any matching handoff from its [index](handoffs/README.md). On continuation, verify the checkpoint and sources against the checkout using the [resume checks](guides/agent-workflow.md#resume-from-a-handoff). |
| Cross-cutting change | Extend the bounded path through affected callers, dependencies, shared invariants, lifecycle and authority boundaries. Include relevant quality scenarios, evaluations, deployment and recovery procedures. |
| Step start or closure | Read [sequencing/done rules](roadmap/sequencing-and-done.md), prerequisites and all criteria for that boundary. Audit the entire OD register and ADR index for every unresolved OD or proposed ADR due there, including deferred items; read their records and the required evidence. A context map cannot limit this audit. |

These paths compose: starting a step that changes shared authority also requires
the cross-cutting path. Historical records are read when they establish a
constraint, explain a relevant decision, or supply evidence for the current claim.

### Required context maps

Steps and handoffs link canonical sections and stable IDs using `Required context`.
Each entry explains why the source matters. Large steps group references by
increment so a continuation can locate its own dependencies. Keep maps current
when scope, contracts or dependencies change; link facts rather than copying them.

For compound invariants, identify the triggering condition and link the canonical
clauses for both preserved and invalidated state, including any required or
forbidden effects. A broad topic label is insufficient when it hides these
dependencies. Keep the rule itself in its canonical source.

Maps guide discovery; they do not establish authority, evidence validity, or an
exhaustive boundary. Follow referenced dependencies and inspect affected code.
If links are missing, stale or insufficient to establish constraints, read the
full affected documents and repair the map. Use full reconstruction if the
boundary remains unclear. Resolve contradictions before relying on a source.

## Understand and apply the standard

Start with the [guide index](guides/README.md) for a summary of each guide and
recommended paths for new projects, existing repositories, and ongoing work.

- [How the foundation works](guides/how-it-works.md): the complete feedback loop.
- [Bootstrap a project](guides/bootstrap.md): detailed owner brief and agent outputs.
- [Conventions and rationale](guides/conventions-and-rationale.md): choices and tradeoffs.
- [Agent workflow](guides/agent-workflow.md): sessions, scoped work, review, and handoff.
- [Current state and history](guides/current-state-and-history.md): concise canonical facts, linked records and safe reorganization.
- [Adoption](guides/adoption.md): reconcile an existing repository.
- [Provenance](guides/provenance.md): source inspections and extraction decisions.
- [Reusable record templates](templates/README.md).

## Canonical responsibilities

| Source | Owns |
| --- | --- |
| Product baseline | Complete requirements, first-release scope, non-goals, and acceptance conditions. |
| Journeys/glossary | Behavioral examples and domain vocabulary, linked to the baseline. |
| arc42 | Current/target architecture and its twelve views. |
| ADR index and records | Consequential choices, alternatives, acceptance, supersession, and implementation status. |
| Open-decision register | Unresolved questions, owners, `Decide by`, and resolution references. |
| Workflow contracts, when needed | Stable lifecycle/interface semantics; diagrams explain those contracts. |
| Roadmap index | Delivery order, active step, and matching per-step status. |
| Individual roadmap step | Prerequisites, scope, non-goals, exit criteria, evidence, and owner acceptance. |
| Experiments | Hypotheses, reproducible observations, outcomes, limitations, and promotion evidence. |
| Development | Commands and check boundaries verified against the checkout. |
| Operations | Runtime, failure recovery, backup, upgrade, and rollback procedures. |
| Handoff index and records | Current continuation pointer per scope and source/worktree checkpoints; link canonical facts and evidence. |

Link canonical facts rather than maintaining authoritative copies. When a change
affects several views, update them together.

## Current state and records

Canonical documents summarize the present contract, implementation and gaps.
Detailed attempts and validation history stay in dated, source-bound records
linked from the owning concern. Follow [the history guide](guides/current-state-and-history.md)
when extracting a growing work log; keep IDs, binding decisions and due gates
discoverable. [Handoffs](handoffs/README.md) identify a continuation checkpoint;
their age or current pointer does not establish evidence validity or authority.

## Status vocabulary

| Dimension | Values and meaning |
| --- | --- |
| Decision | `proposed`: not selected; `accepted`: explicitly binding; `rejected`: not selected with rationale; `superseded`: replaced by a linked record; `deferred`: postponed with reason/deadline. |
| Implementation | `planned`: target only; `partial`: named subset exists; `implemented`: code/configuration and appropriate evidence exist for the stated scope. |
| Feasibility | `experiment-gated`: a dependency still requires recorded validation. |
| Roadmap | `planned`, `active`, `blocked`, `complete`, `deferred`; a blocked step remains the selected current work. |
| Experiment | `not run`, `passed`, `failed`, `inconclusive`; retain failures and their context. |

An accepted decision is not implementation evidence. A passing check is not owner
acceptance. A completed step does not start the next step automatically.

## Template fields and checks

`TBD(project)` marks concrete fields the initialization agent must replace.
Reusable record templates intentionally describe how to write future records.
There are no invented application requirements, ADR approvals, or results.

See [development](development.md) for what the checker verifies and what remains
human review. Keep all new Markdown documents discoverable from these indexes.
