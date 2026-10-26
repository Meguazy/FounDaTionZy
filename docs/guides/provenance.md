# Provenance and extraction choices

The foundation was prepared on 2026-10-26 from read-only local inspections of
two owner repositories. No application source, private dataset, native session,
credential, or raw account output was copied into this template.

| Source | Inspected local HEAD | Relevant material |
| --- | --- | --- |
| Money Tracker | `39e1848b90ba6ec1711f9018cf82ed24e0430a8c` | Root instructions/README, docs map, product/arc42/roadmap layout, step gates, ADRs, development and operations structure, PR template, Git policy documentation, hooks/CI/settings conventions. |
| Devflow Orchestrator | `c90fe44ae2664f77697e9f10023acf33e1ec4724` | Root instructions/README, consolidated baseline, twelve-section arc42, decision and open-decision registers, step gates/evidence, workflow specification conventions, experiment and operational boundaries. |

The snapshots identify the local checkouts inspected. They do not assert that
those checkouts were the latest remote branches or establish a fresh audit of
either application's runtime behavior.

## Shared conventions retained

Both projects use a short root entry point, indexed English documentation, a
product baseline, arc42, stable `AD-NNN` records, step-specific roadmap
documents, evidence-driven completion, and active-scope discipline. Both
separate domain logic from infrastructure and require truthful test claims.
Conventional Commits, sole authorship, and no co-author attribution are shared
repository conventions.

Devflow adds a particularly explicit OD register and `Decide by` gates,
separation of decision and implementation status, a consolidated requirements
baseline, and machine-readable lifecycle semantics where needed.

Money Tracker provides a more developed source-control process: vertical
slices, PR evidence, a thin Claude entry file, structured logging rules, and
documented distinctions between local guardrails, hosted CI, and active
server-side enforcement.

## Differences resolved explicitly

| Difference | Foundation choice and reason |
| --- | --- |
| Python finance stack vs Rust orchestration stack | No application language, framework, database, model, or provider default. These follow the new product's needs. |
| Real-service integration/E2E policy vs early fake-provider application E2E | Name every evidence boundary. Require real services when claiming real integration; preserve clearly scoped fake checks. |
| Multiple allowed merge methods vs squash preference | Squash is a documented template default, configurable by owner direction; it is not claimed as identical source policy. |
| Provider hook/settings enforcement vs a documentation baseline | Keep portable instructions; introduce verified provider configuration only when required. |
| Rich machine-readable product workflow vs application-specific graphs | Workflow contracts are optional and project specific, not a universal runtime engine. |
| Different initial delivery sequences | Only documentation Step 0 is supplied; the agent derives implementation steps from the new application. |

## Drift lessons

The inspected copies contained examples of summary drift: Money Tracker's docs
map described release hardening as next while its roadmap recorded release
completion; Devflow's Claude entry text still described a documentation-only
baseline while its main instructions described implemented Step 2 code.

These observations concern the inspected text, not a new assessment of those
applications. FounDaTionZy responds by using pointer-only provider entry files,
explicit canonical responsibilities, shared roadmap status syntax, and
structural checks. Semantic summaries still need review; the checker cannot
determine whether prose describes the truth.

## What was deliberately left out

Finance rules, account names, subscriptions, hardware paths, deployment
topologies, databases, native harness authentication, operating-system isolation,
hard-coded model IDs, service-specific logging libraries, and private acceptance
results do not belong in a generic foundation.

No existing protection or permissions are imported into the new repository.
Their rationale is documented, while their actual setup remains an explicit
project decision. The result is a reusable method, not a renamed application.
