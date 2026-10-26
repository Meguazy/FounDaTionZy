# Initialize a project with an agent

Initialization turns an application idea into a reviewable working baseline.
It is documentation work, not permission to scaffold and implement the entire
application. The owner can authorize implementation separately after reviewing
the scope and the decisions needed by the next step.

## Give the agent a detailed application description

Use the prompt in [the root README](../../README.md), then explain the following.
You can speak naturally, provide examples, or supply existing material. You do
not have to fill out a formal form or select technologies first.

| Topic | Useful details |
| --- | --- |
| Problem and success | What is difficult today? What result makes this application useful? |
| Users and authority | Who uses it, owns data, administers it, approves actions, or resolves failures? |
| Concrete journeys | A normal example, an exception, a correction, and what happens after interruption. |
| Domain rules | Invariants, calculations, vocabulary, lifecycle rules, and forbidden outcomes. |
| Scope | Essential first release, later ideas, and explicit non-goals. |
| Data | Sources, ownership, sensitivity, retention, import/export, backup, and recovery. |
| Integrations | Systems involved, required capabilities, account/identity boundaries, and offline behavior. |
| Experience | Interfaces, target languages, accessibility, devices, and interaction constraints. |
| Environment | Platforms, local/hosted operation, installation, connectivity, and available hardware. |
| Quality | Correctness, response needs, security, recoverability, portability, and observability. |
| Constraints | Budget, subscriptions, skills, licensing needs, deadlines, and existing technical commitments. |
| Evidence | What must be demonstrated with real services/users, and what may use fakes initially? |
| Collaboration | Who decides, reviews, publishes, deploys, and merges? What is already authorized? |

"Unknown" is useful information. The agent should help refine it, not replace it
with an invented fact. Do not include real credentials, private financial data,
customer exports, or provider sessions in a public project brief.

## What the agent does

### 1. Inspect and preserve

Read the repository instructions and documentation map. If code already exists,
inspect manifests, source, tests, CI, migrations, and runbooks before making
implementation claims. Follow [adoption](adoption.md) for that case.

Capture the owner's requirements without losing exceptions or constraints.
Use a source reference that can be shared safely: a dated owner direction or
sanitized requirements note. Private chat need not be copied verbatim into Git.

### 2. Clarify important gaps

Summarize the intended application, then ask focused questions about choices
that materially affect scope, authority, data, architecture, or the next step.
Batch related questions and explain the tradeoffs.

Continue independent documentation while answers are pending. Do not use the
absence of a reply as acceptance. Label useful technical suggestions proposed,
and put unresolved questions in the OD register with an owner and deadline.

Routine reversible details within authorized scope can use agent judgment.
Business rules, licensing, privileged access, irreversible effects, and choices
that contradict accepted constraints need explicit owner direction.

### 3. Populate the product baseline

Replace project fields in:

- [Product index](../product/README.md)
- [Consolidated specification](../product/project-specification.md)
- [User journeys](../product/user-journeys.md)
- [Glossary](../product/glossary.md)

Assign stable requirement IDs. Separate confirmed requirements, proposals,
non-goals, and deferred work. Add observable acceptance conditions and failure
behavior, rather than adjectives such as "robust" or "user friendly."

### 4. Explain the architecture and choices

Populate all twelve [arc42 sections](../arc42/README.md). Mark current state and
target state separately. For small or inapplicable concerns, give a short reason.

Create ADRs only for consequential choices. Each needs context, options,
rationale, consequences, decision status, owner/acceptance evidence when known,
implementation status, and `Decide by` when proposed. Add every ADR to its
index. Do not invent an acceptance date because a recommendation looks obvious.

If feasibility is uncertain, create an experiment with reproducible inputs and
a pass/fail criterion. Record cost/credential/fixture authorization where the
experiment needs it. Preparing a probe does not mean running it was authorized.

### 5. Derive a roadmap from dependencies

Populate [the roadmap](../roadmap.md). Step 0 establishes the documentation
baseline. Derive subsequent steps from this application's risks and outcomes;
the template does not prescribe their count or a language-specific sequence.

Copy [the step template](../roadmap/step-template.md) into one file per real
step. Set intent, scope, prerequisites, non-goals, deliverables, exit criteria,
evidence requirements, and all start/exit decisions. Avoid fabricated dates.

Steps can be planned while later decisions stay open. Starting a step requires
resolving its blocking start decisions. Closing one requires reviewing its exit
decisions and criteria.

### 6. Adapt instructions, workflows, and commands

Keep the reusable safety, evidence, and documentation rules in `AGENTS.md`,
then add short project-specific constraints with links to the canonical docs.
Keep `CLAUDE.md` a thin pointer. Add other provider entry files only when they
are actually needed and supported; do not create competing instruction sources.

Populate development guidance with commands verified against the actual
checkout. Before the scaffold exists, describe the intended checks as planned
and leave command examples non-executable.

Use [workflow documentation](../workflows/README.md) only for meaningful
behavioral contracts. A machine-readable state model is optional; it is useful
for a complex lifecycle, not a mandatory application engine or an executable
agent controller.

Adapt operations to the actual runtime. A design-stage project must not expose
imaginary installers, deployment scripts, services, backups, or health endpoints.

### 7. Validate and present the baseline

Run the documentation checker and `git diff --check`. Inspect the diff for
sensitive material and accidental inherited domain/technology assumptions.
Review consistency across product, architecture, decisions, roadmap, and agents.

Present:

1. What the application is and what the first release excludes.
2. The proposed architecture and consequential alternatives.
3. The roadmap and why its order follows the dependencies.
4. Open choices, with the items due before the next action highlighted.
5. Exact structural validation performed and known limits.
6. A concrete request for any decision actually needed to continue.

Owner acceptance belongs in the relevant record, including date, scope, limits,
and a safe reference to the owner's actual direction. Do not infer acceptance
from a merge or from the request to initialize the repository.

## Initialization exit checklist

- The product brief has been consolidated into a coherent baseline.
- Requirements, journeys, vocabulary, and first-release boundaries agree.
- All twelve arc42 sections contain relevant content or a reasoned exclusion.
- Consequential choices have indexed ADRs with accurate status.
- Unknowns have owners, `Decide by` boundaries, and links to affected steps.
- The roadmap has useful outcomes and verifiable step criteria.
- Development and operations distinguish current capabilities from plans.
- Agent instructions point to the canonical sources and contain no stale status.
- New documents are discoverable through indexes; relative links work.
- The owner has a reviewable package; remaining approvals are recorded as pending.

Use `python3 scripts/check_docs.py --initialized` after completing the baseline.
It adds a scan for unresolved `TBD(project)` fields in the concrete project
documents. Instructions and reusable templates intentionally remain reusable.
Passing this mode is structural evidence; it cannot judge the quality of the
requirements or establish owner acceptance.

## Finish the transition from template to project

Replace the root README with a concise application entry point: purpose, honest
current capability, verified quick start if any, and links to `docs/`.
Retain the method guides if useful, or archive/remove them deliberately and fix
their references. The initialized checker expects the documented baseline paths;
if the project reorganizes them, adapt the checker in the same change.

Update the documentation map's initialization label and the project entry
instructions. Review the public-facing description, visibility, license,
ownership, and any shared agent settings. Preserve the inherited MIT notice
for reused foundation material; select licensing for the application's new
code explicitly. Template creation does not transfer source-project
secrets, settings, protection, external accounts, or implementation evidence.
