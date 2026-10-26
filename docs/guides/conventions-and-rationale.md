# Conventions and rationale

The conventions below are a practical baseline distilled from two projects.
They are not a requirement to copy either project's stack or every process
detail. [Provenance](provenance.md) explains the source inspection and differences.

## Documentation structure

| Convention | Reason | Cost or boundary |
| --- | --- | --- |
| Short root README, detailed docs map | New readers get an entry point and a predictable reading path. | Keep the README's summary current; link to detail instead of copying it. |
| One canonical home per kind of fact | Reduces contradictions and makes changes easier to propagate. | Related documents still need explicit links and coordinated updates. |
| Full product baseline plus focused journeys | Preserves the owner's complete discussion while exposing real interactions. | Do not let a shorter journey silently remove a requirement. |
| Twelve arc42 sections | Covers runtime, deployment, quality, and risks as well as components. | Scale content to the project; explain inapplicable sections. |
| Indexed ADRs | Preserves alternatives, rationale, and consequences for future maintainers. | Record consequential choices; avoid an ADR for every local variable. |
| Stable identifiers | Evidence and historical decisions keep their meaning after scheduling changes. | Never renumber old steps or reuse a superseded decision's ID. |
| English technical documents | Keeps contracts, code, and architecture readable across tools and collaborators. | Owner discussion and application UI languages are separate decisions. |

## Status, scope, and decisions

The biggest distinction is between choosing a direction and delivering it.
Use separate fields rather than a single ambiguous "done" label.

| Convention | Reason | Boundary |
| --- | --- | --- |
| Decision status separate from implementation | Accepted direction cannot masquerade as working software. | Evidence must name its actual boundary. |
| Current and target architecture separated | A diagram of the intended system should not imply it is running. | Inspect code, configuration, and tests before claiming implementation. |
| Open questions with owners/deadlines | Uncertainty becomes visible, actionable work. | An unresolved item blocks only its declared boundary. |
| Decision gates at step start and exit | Prevents a convenient proposed default from hardening unnoticed. | Explicit deferral needs rationale, a new deadline, and scope impact. |
| Active-step discipline | Prevents opportunistic infrastructure from expanding a bounded change. | The owner can change scope; record the consequences. |
| Owner acceptance distinct from merge | Integration into main does not prove every milestone criterion. | Record acceptance against the presented evidence and limits. |

## Agent management

`AGENTS.md` is a navigation and behavior contract. It should hold stable rules
and short project constraints, while the knowledge it references lives under
`docs/`. It is not a copy of every architecture document or a diary of the
current implementation state.

`CLAUDE.md` points to that source. FounDaTionZy uses a plain Markdown pointer
rather than provider-specific hooks/settings because the baseline should remain
portable and understandable. A tool-specific configuration can be introduced
later with verified behavior, narrow permissions, and documented limits.

Fresh sessions reconstruct context by following the same reading order.
Handoffs report exact scope, evidence, decisions, and next actions. The original
chat is useful context, but the repository is the durable reference.

Start with one writing agent. Concurrency adds coordination costs and needs
explicit delegation. Review independence depends on context and authority, not
on calling a session "reviewer." A single agent can self-check, but must label
that result accurately.

Never hard-code a model or provider choice into this generic foundation. If an
application uses AI, its model, harness, credentials, permissions, evaluation
policy, and session/resume behavior belong to that application's documented
decisions. Money Tracker and Devflow intentionally use different approaches.

## Architecture and code

Separate deterministic domain behavior from I/O and infrastructure. Use
cohesive components and narrow interfaces so storage, external services, and
presentation can change without rewriting unrelated rules.

This is a design principle, not a demand for a universal ports-and-adapters
scaffold. A tiny application may need only a few modules. Additional boundaries
earn their place through responsibility, ownership, lifecycle, trust, or reasons
to change.

Language-specific conventions are selected during initialization. Python
docstrings, Rust crate pins, frontend tools, database choices, CI runner matrices,
and model providers from the source projects are not inherited defaults.

## Testing and evidence

Test production behavior and observable failures. Use lightweight real
implementations or contract fakes where isolation is the goal. Do not replace a
real service and then call the result proof of that service's integration.

A project may use application E2E with fake providers during an early step.
Name the boundary explicitly and schedule real-provider acceptance separately
when it is required. This resolves a difference between the source projects
without weakening either one's claims.

The [project test strategy](../development.md#project-test-strategy) turns these
principles into choices the agent proposes during initialization/adoption and
resolves with the owner where material. It defines the test-first default and
exceptions. Its outline stays stack independent: suite layout, tools, thresholds,
and optional techniques follow actual risks and ecosystem conventions.

For model/prompt/routing/tool changes, define evaluated cases, quality gates,
failure analysis, configuration identity, and promotion evidence. Not every
project needs AI evaluation infrastructure; one that does should not rely on
an attractive transcript as its acceptance suite.

Keep experiment code and sanitized results separate from application modules.
A probe's permissive assumptions and throwaway setup must not become production
dependencies accidentally.

## Git, CI, and enforcement

One branch/PR per cohesive change makes the work reviewable. Conventional
Commits give history a predictable shape. One author and no co-author trailers
preserve the owner's chosen attribution convention.

Squash merge is the portable default here, while Money Tracker permits more
merge methods. FounDaTionZy documents that difference rather than calling it a
shared rule. The owner can select another policy and record the rationale.

| Layer | What it can do | What is included here |
| --- | --- | --- |
| Instructions and PR template | Describe expected behavior and review evidence. | Included. |
| Local formatting/Git files | Standardize text and ignore common private artifacts. | Included; not a secret scanner. |
| Documentation checker | Reject selected structural defects. | Included and runnable locally. |
| Hosted CI | Repeat that checker and whitespace checks. | Workflow included; each run has its own result. |
| Hooks and provider permissions | Prevent some local mistakes in a specific tool. | Not installed by the template. |
| Branch rules and required checks | Enforce server-side merge requirements when active. | Not installed; select and verify during project setup. |

A CI file does not activate protected branches. A ruleset JSON would not prove
it was applied. Local deny patterns would not prove that a parser cannot be
bypassed. Only claim the enforcement actually configured and demonstrated.

Never weaken checks, disable security, bypass hooks, or silently lower a quality
threshold to get success. If a gate is unavailable, report the missing evidence
and address its cause or obtain a recorded scope change.

## Logging and private material

Prefer stable structured event names plus safe correlation fields. Values such
as credentials, owner content, provider payloads, and personal paths must not
leak into logs or public evidence. Choose project-specific allowed fields and
retention rules before adding sensitive runtime behavior.

Ignore files keep routine generated state out of Git; they do not remove an
already tracked secret or protect data from a running process. Shared harness
configuration must be reviewed explicitly, and native sessions remain local.

## Keep the process proportional

The template begins with documents because the requested foundation is
documentary. It does not require months of design before a small feature.
Write enough to make the next decision and next step reviewable. Refine later
sections when their questions become relevant, while keeping the unknowns
visible.

If a convention becomes costly without protecting a real invariant, propose a
change, explain the tradeoff, and update the affected instructions and tooling
together. Consistency is useful; ritual alone is not.
