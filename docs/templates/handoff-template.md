# Session handoff

Replace template guidance with concise checkpoint facts and links. Mark genuinely
inapplicable items explicitly; do not invent data to fill a field.

- Recorded at / timezone: unset
- Workstream / task and canonical step or scope link: unset
- Branch / HEAD commit: unset
- Relevant tree or patch identity / covered paths and exclusions: unset
- Previous handoff, if any: unset

Identify relevant uncommitted and untracked inputs as well as HEAD. State what
any digest covers; do not imply that it includes its own subsequently written
record or later edits. Use safe references rather than private source dumps.

## Authorized scope

- Requested outcome and authorized increment: unset
- Owner direction / canonical record and applicable limits: unset

Link consequential direction in its canonical home. Carry conditions, expiry and
consumed limits accurately; this checkpoint cannot grant or renew permission.
Current explicit owner direction applies when it changes an earlier scope.

## Progress and working tree

| Outcome / criterion | Completed, pending or interrupted work | Changed paths / evidence links |
| --- | --- | --- |

- Uncommitted / untracked inputs needed to continue: unset
- Pre-existing or unrelated changes to preserve: unset
- In-flight operations or uncertain outcomes and reconciliation reference: unset

Summarize the delta since the previous handoff. Link detailed records beside
their concern; avoid copying a session diary. Do not turn an uncertain external
effect into a successful result or retry it automatically.

## Checks and applicability

| Check / evidence record | Checked inputs / actual boundary | Outcome / counts | Reuse condition or rerun trigger |
| --- | --- | --- | --- |

Link exact commands, revision/tree, environment, configuration and dependencies
in the evidence record. Include failures, skipped, unavailable and not-run gates.
State whether each relevant result remains applicable, needs a rerun, or has
unknown applicability; retain the original outcome separately from that judgment.

- Review type / unresolved findings: unset

## Decisions and limits

Link unresolved ODs/proposed ADRs due before the next action, their canonical
deadlines, evidence gaps and blocking consequences. Link already recorded
resolutions instead of requesting the same decision again. A handoff cannot
restrict the full decision audit at a step boundary.

## Next authorized action

- First concrete action / expected observable result: unset
- Preconditions / stop conditions and affected checks: unset

Name the smallest action that advances the requested outcome. If none is
authorized, state the specific missing decision or limit. This field summarizes
existing authorization; it does not authorize implementation, a new step or
publication by itself.

## Required context

Name the next action's [reading path](../README.md#reading-paths). Link the step's
context map where applicable, then link the canonical sources for that action.
Include relevant requirement/decision IDs, architecture/contracts, code/tests
and check commands. Add references for newly discovered dependencies; avoid
copying the whole step map or restating its facts.
For compound invariants, identify the trigger and link the clauses for preserved
and invalidated state and required/forbidden effects.

| Source / section / IDs | Why needed for the next action |
| --- | --- |

The receiving session must establish the common core and verify these references
against current sources and the checkout, expanding the reading when needed.

Select this record through the [handoff index](../handoffs/README.md) and apply
the [resume checks](../guides/agent-workflow.md#resume-from-a-handoff).
Do not paste raw conversations, private datasets, credentials or provider session
state. Record self-review accurately and never invent acceptance.
