# Module docs template

Create a module's `docs/` folder only when its README is not enough, and add
only the files the module needs. Use these fixed names so an agent can find them
in any module. Replace `<component>` with the component's identifier and `{root}`
with the relative path from the module's `docs/` folder to the repository root,
such as `../../..`. Link each file from the module README's `Module docs`
section. [Module documentation](../guides/module-docs.md) explains the rules
and what the checker verifies.

Every file starts with a `Governed by:` paragraph that links its global source.
A file with another name links the global source it details.

## plan.md

````markdown
# <component> plan

Governed by: [roadmap]({root}/docs/roadmap.md). This plan breaks down what the
module delivers in each step. The roadmap and step documents own order, status,
gates and acceptance, and prevail on conflict. Implement only rows whose step is
active.

| Capability | Step | Depends on | Implementation |
| --- | --- | --- | --- |
| <capability> | [Step N]({root}/docs/roadmap/step-N-topic.md) | <capability or none> | planned |
````

Use `planned`, `partial` or `implemented` from the
[status vocabulary](../README.md#status-vocabulary) for the module's code only.
List later rows too: they show what the current design must accommodate without
implementing it early.

## spec.md

````markdown
# <component> specification

Governed by: [product baseline]({root}/docs/product/project-specification.md).
This document details the module's behavior. Requirements and scope stay in the
baseline and prevail on conflict.

## <Behavior or rule>

- Requirements: <REQ IDs>.
- Rule: <the precise behavior, including edge cases and failure behavior>.
- Examples: <inputs and expected results, mirrored by tests>.
````

## design.md

````markdown
# <component> design

Governed by: [architecture]({root}/docs/arc42/README.md). This document covers
the module's internal structure. System views, shared concepts and decisions
stay global and prevail on conflict.

## Internal structure

<Internal parts, their responsibilities and how data flows between them.>

## Internal sequences

<Sequences and lifecycles that stay inside the module, with failure paths.>

## Design notes

<Local choices worth explaining. A choice that affects anything outside the
module needs an ADR instead.>
````

## glossary.md

````markdown
# <component> glossary

Governed by: [domain glossary]({root}/docs/product/glossary.md). Terms shared
across modules belong there and prevail on conflict.

| Term | Meaning in this module | Notes |
| --- | --- | --- |
````

## testing.md

````markdown
# <component> testing

Governed by: [project test strategy]({root}/docs/development.md#project-test-strategy).
Required gates and repository commands stay there and prevail on conflict.

## Fixtures

<Where fixtures live, what each represents and their provenance.>

## Reference cases

<Cases that pin important behavior, linked to the specification.>

## Adding a case

<How to add a fixture or reference case and run it.>
````
