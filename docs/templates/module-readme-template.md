# Module README template

Copy the skeleton below into `<module directory>/README.md` when the module's
directory is created, and link it from the module's row in the
[building-block view](../arc42/README.md#5-building-block-view). Replace
`<component>` with the component's identifier and `{root}` with the relative
path from the module directory to the repository root, such as `../..`.
[Module documentation](../guides/module-docs.md) explains each section and what
the checker verifies.

Keep the README to about a page. Move reference material into the module's
`docs/` folder using [the module docs template](module-docs-template.md).

````markdown
# <component>

## Purpose

<What this module does, in a few lines, and what it deliberately does not do.>

## Global context

Establish the repository's common core first: [AGENTS.md]({root}/AGENTS.md) and
[the reading protocol]({root}/docs/README.md#required-reading-order).

- Component `<component>` in the
  [building-block view]({root}/docs/arc42/README.md#5-building-block-view).
- Shared rules in the
  [cross-cutting concepts]({root}/docs/arc42/README.md#8-cross-cutting-concepts).
- Decisions in the [ADR index]({root}/docs/arc42/decisions/README.md), filtered
  by `<component>`.
- Open questions in the [OD register]({root}/docs/open-decisions.md), filtered
  by `<component>`.

These global sources prevail over this module's documents on conflict.

## Public API

<The types, functions or endpoints other modules use, with one example that runs
as a test where the ecosystem allows. Link generated API documentation rather
than copying signatures.>

## Dependencies

<Modules this one may depend on, modules it must not depend on, and how the rule
is enforced, such as the build manifest or a CI check.>

## Owned data

<Tables, schemas, files or state this module owns. Write "None" for a pure
module.>

## Invariants

- <A durable local rule a change must preserve.> Reason: <why it exists>.

## Related decisions

| Decision | Why it matters here |
| --- | --- |
| [AD-NNN]({root}/docs/arc42/decisions/AD-NNN-topic.md) | <The constraint it places on this module.> |

<List every ADR whose Affected components field names this module. Write "None
yet" when there is none.>

## Module docs

<Keep this section only when the module has a docs/ folder.>

- [Plan](docs/plan.md): what this module delivers in each roadmap step.
- [Specification](docs/spec.md): detailed behavior linked to requirement IDs.
- [Design](docs/design.md): internal structure and sequences.
- [Glossary](docs/glossary.md): vocabulary used only by this module.
- [Testing](docs/testing.md): fixtures, reference cases and how to add them.

## Working on it

<Verified commands to build and test only this module, the fixtures it uses and
any harness for trying it without the rest of the system. Keep planned commands
visibly planned.>
````
