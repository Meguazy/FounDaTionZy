# Documentation map

**Repository mode: uninitialized project template.** Method guides and the
structural checker are usable; project documents still contain explicit
`TBD(project)` fields. The [roadmap](roadmap.md) owns delivery status.

## Required reading order

1. [Product index](product/README.md), [baseline](product/project-specification.md),
   [journeys](product/user-journeys.md), and [glossary](product/glossary.md).
2. [Roadmap](roadmap.md), the active step, and
   [sequencing/done rules](roadmap/sequencing-and-done.md).
3. [arc42](arc42/README.md), [ADR index](arc42/decisions/README.md), and relevant ADRs.
4. [Open decisions](open-decisions.md) and applicable [workflows](workflows/README.md).
5. Relevant [experiments](experiments/README.md),
   [development](development.md), and [operations](operations/README.md).

[AGENTS.md](../AGENTS.md) defines behavior and authorization rules. It directs
agents to this map; it does not duplicate the knowledge below.

## Understand and apply the standard

Start with the [guide index](guides/README.md) for a summary of each guide and
recommended paths for new projects, existing repositories, and ongoing work.

- [How the foundation works](guides/how-it-works.md): the complete feedback loop.
- [Bootstrap a project](guides/bootstrap.md): detailed owner brief and agent outputs.
- [Conventions and rationale](guides/conventions-and-rationale.md): choices and tradeoffs.
- [Agent workflow](guides/agent-workflow.md): sessions, scoped work, review, and handoff.
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

Link canonical facts rather than maintaining authoritative copies. When a change
affects several views, update them together.

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
