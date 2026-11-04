# Working with agents throughout the project

The agent's role is to turn owner direction into a reviewable result within the
agreed scope, while keeping the repository's knowledge accurate. Instructions
support that work; they do not replace evidence, ownership, or actual access
controls.

## Start or resume a session

Read `AGENTS.md` and establish the common core in
[the reading protocol](../README.md#required-reading-order). Select its path for
initialization/adoption, a bounded change, a cross-cutting change, or a step
boundary. Inspect the current branch, uncommitted changes, actual code, and
check definitions relevant to the requested outcome.

For continuation, locate the matching current record in the
[handoff index](../handoffs/README.md) and apply the
[resume checks](#resume-from-a-handoff). The index is navigation; the roadmap
and canonical records retain their authority.

Use `Required context` in the selected step and current handoff to reach the
canonical sections and stable IDs. For a large step, use the references for the
current increment. Verify sources against the checkout, follow dependencies,
and expand the reading as the protocol requires. A handoff's recorded revision
helps identify changes; it does not establish current authority or valid evidence.

Establish four facts before editing:

1. What outcome has the owner requested?
2. Which existing requirements and accepted decisions constrain it?
3. What can be changed under the current authorization?
4. Which decisions or missing evidence genuinely block the next action?

Do not infer the active step from the largest number or an old chat summary.
The roadmap index and step document must agree. If they conflict, resolve the
drift before using either status as permission.

## Plan a bounded change

Connect the requested behavior to requirements and step criteria. Explain
consequential implementation choices and the relevant validation boundary.
Keep the plan proportional: a typo does not need an architecture exercise.

Identify the applicable reading path and source references in the change plan
or handoff. Maintain the context map when new dependencies are found or the
requested scope changes. Keep requirements and decisions in their canonical homes.

Check all ODs and proposed ADRs due at the step's start. Ask only for unresolved
blocking decisions. If the owner already authorized an action within this
scope, continue without asking for the same permission again.

A new request can change scope. Record resulting requirement/decision/roadmap
changes so the next session does not reconstruct a different project.

## Implement and maintain knowledge together

Use a change branch before editing a derivative project. Preserve unrelated
working-tree changes. Implement production behavior and meaningful failure
paths, with appropriate tests or evaluations.

Update the documents that own changed facts:

| Change | Usually affected documentation |
| --- | --- |
| User behavior or business rule | Product baseline, journeys, acceptance criteria, active step. |
| Component/interface/data ownership | arc42, relevant ADRs, developer guidance. |
| Lifecycle or transition semantics | Behavioral contract, runtime view, conformance checks, journeys. |
| Runtime process/configuration | Deployment view, development, operations, recovery/rollback. |
| Model/prompt/tool behavior | Evaluation plan, experiment result, promotion decision. |
| Delivery scope or sequence | Roadmap index, affected steps, open-decision deadlines. |

"Usually" matters: review the actual impact rather than mechanically editing
every document. Add new files to the appropriate index.

## Verify and review

Run checks appropriate to the change. Structural docs checks cannot replace
tests, and fake-boundary tests cannot establish real-provider compatibility.
Report not-run gates and their reasons.

Review the full diff for unintended behavior, drift, secrets, stale statements,
broken links, and unauthorized scope expansion. This self-check is useful,
but label it as self-review.

For a consequential implementation change, seek a fresh review context when
the project's policy or owner requires it. A review should record:

- The revision/tree and files or behavior reviewed.
- Requirements, invariants, and risk areas checked.
- Findings with evidence and severity.
- Checks independently run, if any.
- Limits, unresolved questions, and whether fixes need another review.

An independent reviewer can be a human or a separately authorized agent/session.
Do not invent a second reviewer, an approval, or checks that were not run.

## Multiple agents

The default is one writing agent. Delegation is used only when explicitly
requested by the owner or applicable instructions.

Before parallel work begins, assign a concrete outcome, owned files, shared
interfaces, constraints, check expectations, and integration owner. Avoid two
agents modifying the same contract simultaneously. Read shared work before
integrating it, and resolve inconsistent assumptions explicitly.

A delegated review should avoid writing production changes while another agent
is still defining the reviewed behavior. A separate session is not automatically
independent if it only repeats the author's conclusion without checking the diff.

## Publish a reviewable change

Complete the PR template with the outcome, reasoning, validation, docs/operations
impact, risks, and due decisions. Follow existing publication authorization.
Opening the PR is the default agent stopping point; the owner merges unless
explicitly authorizing a different scoped action.

CI results and human approval are facts from their respective systems. Do not
claim enforcement from a workflow file alone. Do not bypass required gates or
change repository settings to make the PR mergeable.

After a code/configuration change, rerun checks whose scope has changed. Evidence
belongs to the revision it validated.

## Close a roadmap step

Step completion is a separate assessment from finishing a task:

1. Enumerate all exit criteria and due exit ODs/proposed ADRs.
2. Link exact evidence to each criterion and disclose gaps.
3. Present an exit review with implemented behavior, actual test boundaries,
   remaining risks, and proposed handling of limits.
4. Obtain and record owner acceptance for that scope.
5. Set the same status in the step and roadmap index in one change.

If the owner accepts recorded limits, say so explicitly. Do not turn "accepted
with limits" into an unqualified compatibility claim. Acceptance does not
automatically start the next step.

## Durable handoff

Keep current facts and detailed work records organized using
[current state and history](current-state-and-history.md). When work will
continue or transfer, write a checkpoint using
[the handoff template](../templates/handoff-template.md):

1. Update changed requirements, accepted decisions, step assessments and other
   canonical facts first. Link detailed validation/work records beside their
   concern, including failures and limitations.
2. Capture the branch, HEAD, relevant dirty/untracked inputs and identity scope.
   Record completed and pending work, unrelated changes to preserve, uncertain
   effects, evidence applicability and the next concrete authorized action.
3. Write a uniquely named dated record in the [handoff index](../handoffs/README.md).
   Advance its current pointer for the scope and retain the previous record in
   history. When continuation ends, link its closure/stopping record instead of
   leaving an apparently active pointer.
4. Run applicable structural checks after writing the record and index. Declare
   later edits and reassess any affected evidence; do not label an earlier checked
   tree as the final tree when relevant inputs changed.

Keep the checkpoint concise by linking canonical facts and evidence. A completed
bounded task needs no new active workstream merely to fill the index. Handoffs
contain no raw conversations, credentials or provider sessions.

### Resume from a handoff

1. Match the workstream and branch to the checkout. Compare the recorded commit,
   relevant patch/tree inputs and pending work with actual files; preserve
   unrelated edits. A newer date or matching HEAD alone does not prove freshness.
2. Establish the reading protocol's common core, verify context-map sources and
   reconcile scope, decisions and step status with canonical records. At a step
   boundary, audit the entire OD register and ADR index, regardless of the map.
3. Classify required evidence as applicable within its recorded scope, requiring
   a rerun, or unknown. Check changed code/configuration, dependencies, fixtures
   and volatile external conditions. Retain failures as failures until new valid
   evidence replaces them; rerun affected gates within authorization rather than
   blindly repeating every historical check or carrying all old passes forward.
4. Continue with the stated first action when its prerequisites and current
   authorization still hold. Do not ask again for a recorded approval that covers
   it. If direction changed, reconcile the affected canonical records; if a real
   blocking decision or exhausted limit remains, request only that missing scope.

A handoff summarizes a checkpoint; it cannot extend authority, resolve an OD,
accept a step or prove external state. If it is missing or stale, reconstruct the
affected context and repair the navigation before relying on it.
