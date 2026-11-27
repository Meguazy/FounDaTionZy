# Module documentation

A module is a component registered in the
[building-block view](../arc42/README.md#5-building-block-view) that has its own
directory, such as a package, crate or service folder. Module documentation lets
an agent working inside one module find that module's knowledge beside the code
and reach every global decision that constrains it through checked links.

## Authority stays global

Global documents own every fact that carries authority: requirements, decisions,
open questions, delivery order and status, step criteria and acceptance,
handoffs and evidence. Module documentation owns a module-scoped view of those
facts and the internal detail that has no other home. It links back instead of
copying.

| Global source | Module-local counterpart | What stays global |
| --- | --- | --- |
| Roadmap and steps | `docs/plan.md`: what the module delivers in each step | Order, status, gates and acceptance |
| Product baseline | `docs/spec.md`: detailed module behavior linked to requirement IDs | Requirements and scope |
| arc42 | `docs/design.md`: internal structure, internal sequences and lifecycles | System views, shared concepts and cross-module lifecycles |
| Domain glossary | `docs/glossary.md`: vocabulary only this module uses | Shared domain terms |
| Development and test strategy | `docs/testing.md`: fixtures, reference cases and how to add them | Repository commands and the test strategy |
| ADRs | `Invariants` in the README for durable local rules | Every decision record |
| Open decisions | None: filter the register by component | Every question |
| Handoffs, experiments, operations, evidence | None: use the module as a record's scope | All records |

A local schedule, register or acceptance record would escape the step-boundary
audit. It would also compete with the global instruction: an agent tends to
follow the most specific instruction it reads. Module documents therefore state
which global source governs them and that the global source prevails.

## Register the module

Give each component a stable identifier in backticks in the first column of the
building-block table. ADRs and the open-decision register use that identifier.
When the component has its own directory, link its README in the `Module docs`
column. That link makes the directory a module for the checker. A component
without a README, such as a planned one, remains an ordinary row.

## Module README

Create every module README from
[the module README template](../templates/module-readme-template.md). It has
these sections:

| Section | Content |
| --- | --- |
| `Purpose` | What the module does and deliberately does not do. |
| `Global context` | Links to the module's building-block row, cross-cutting concepts, ADR index and OD register, with the identifier to filter them by. |
| `Public API` | The interface other modules use, with an example kept executable where the ecosystem allows. |
| `Dependencies` | Allowed and forbidden dependencies on other modules. |
| `Owned data` | Data the module owns; other modules use its interface instead. |
| `Invariants` | Durable local rules a change must preserve, each with a short reason. |
| `Related decisions` | Every ADR that lists the component, with why it matters here. |
| `Module docs` | Links to each file in the module's `docs/` folder, when it exists. |
| `Working on it` | Verified commands, fixtures and harnesses for working on the module alone. |

Where the ecosystem lets the README double as API documentation, prefer that
so its examples run as tests. In Rust, `#![doc = include_str!("../README.md")]`
makes the README the crate page and runs its Rust code blocks as doctests.

## Module docs

Create a `docs/` folder inside a module only when the README would exceed about
a page, or when the module needs reference tables, diagrams or detailed
behavior. Use the fixed names from the table above, so an agent finds them
without exploring; add other files when needed. Copy their shapes from
[the module docs template](../templates/module-docs-template.md).

Each file starts with a `Governed by:` paragraph linking the global source it is
subordinate to and stating that the source prevails on conflict. Every row of a
module plan links the step that owns it and records only the module's
implementation status. Implement only rows whose step is active.

## Classify decisions by effect

Ask who else would have to change code or documents if the choice changed:

- Nobody outside the module, and the choice is reversible: decide within the
  authorized scope and explain it in the change.
- Nobody outside the module, and the rule should last: record it under
  `Invariants` with a reason.
- Anyone else, including another module, the protocol, data owned elsewhere,
  visibility, security or a quality requirement: propose an ADR that lists the
  affected components, and do not rely on it before its decision is recorded.

Questions that block a module go in the global
[open-decision register](../open-decisions.md), with the component in the
`Components` column and the module's maintainer as owner.

## Reading path

For a change inside a module, establish the common core first. Then read the
module README, the module docs the change touches, the step's references for
the module, and the ADRs and open decisions that list the component. A change to
the public API, owned data or dependency rules also follows the cross-cutting
path in [the reading protocol](../README.md#reading-paths).

## What the checker enforces

[The checker](../development.md#what-the-checker-covers) treats a README linked
from the building-block table as a module README and verifies that:

- the README has the required sections, plus `Module docs` when the module has
  a `docs/` folder;
- the README links the architecture document, the ADR index and the OD register;
- the README links every ADR whose `Affected components` field names the module;
- each module doc is linked from the README and has a `Governed by:` paragraph
  linking a global source, which must be the fixed source for a fixed name;
- every row of a module plan links a roadmap step;
- every ADR has an `Affected components` field naming registered components,
  `cross-cutting`, `none`, or `unset` while drafting.

It cannot judge whether a module document is accurate, complete or subordinate
in substance. Review that with the change.
