# Current state and historical records

Keep the present system understandable from its canonical documents. Preserve
the evidence and reasoning behind that state in linked, identity-bound records.
The [documentation map](../README.md#canonical-responsibilities) defines which
document owns each fact; this guide explains how to keep those documents usable
as a project accumulates work.

## Read current facts first

Product, architecture, workflow, development and operations documents describe
the current accepted constraints, implemented behavior, target behavior and
known gaps, with those dimensions labeled separately. Update these sections when
facts change instead of appending another session narrative that contradicts them.

Keep a step's outcome, prerequisites, criteria, unresolved gates and current
evidence assessment easy to locate. Link detailed attempts and procedures rather
than making readers reconstruct readiness from a chronological log. A failed or
unavailable required check remains visible in the current assessment.

Historical records describe what was decided, attempted or checked at a named
time and source identity. Their dates do not establish current authority or
validity. Accepted ADRs remain binding until explicitly superseded; an old record
can still be essential to a current constraint or claim.

## Keep records beside their concern

| Concern | Current entry point | Detailed records |
| --- | --- | --- |
| Requirements and architecture | Product baseline, arc42 and contracts | Link relevant ADRs and evidence; preserve stable requirement and section references. |
| Decisions and blockers | ADR index and OD register | Keep every indexed decision and OD row, including resolved/deferred items; link rationale and resolutions. |
| Step delivery | Roadmap index and step criteria/evidence assessment | Put long validation or work records beside the step, for example under `docs/roadmap/records/step-N/`, and link them from the step. |
| Experiment | Indexed `EXP-NNN` record with question, gate and outcome summary | When repeated runs need separate records, link each identified run from that experiment; retain failures and inconclusive runs. |
| Session continuation | [Handoff index](../handoffs/README.md) | Dated handoffs capture a source/worktree checkpoint and next action; the index selects the current record for the scope. |

Create record files and subdirectories when there is real material to preserve;
the example paths do not require empty scaffolding. Reuse the
[evidence template](../templates/evidence-template.md) and
[handoff template](../templates/handoff-template.md). Existing stable record paths
can stay in place when a clear current summary and links solve the navigation cost.

## Move history without losing meaning

1. Inspect code, current owner direction, accepted decisions and evidence before
   rewriting a current-state summary. Record uncertainty where proof is missing.
2. Extract dated procedures, failed attempts and session detail into records with
   their original source identity, environment, outcome and limitations. Preserve
   actual acceptance, deferrals and unresolved work; never infer missing approvals.
3. Update the canonical current statement and its evidence links in the same
   change. Leave required gaps and blockers visible there.
4. Preserve IDs and published paths/anchors where feasible. When moving a
   referenced section, retain its heading with a short link to the new location,
   or update every affected reference. Link records from their relevant index or
   concern; do not rely on a directory listing or Git search to discover them.
5. Keep ADRs indexed and OD status/deadline/resolution rows available to the full
   step-boundary audit. Archiving narrative must not hide a due decision, erase a
   rejection, or turn a proposal into an accepted rule.
6. Review the full change and run the documented structural checks. A prose move
   does not renew the runtime evidence it references; changed check inputs require
   their affected gates to be assessed again.

For adoption, preserve provenance instead of inventing past compliance. For an
ongoing project, apply this incrementally when a document starts mixing its
current contract with repeated work logs.

## Preserve evidence and assess its applicability

Keep a completed result tied to what actually ran. A new run or a substantive
correction gets a separate linked record; explain what it replaces or corrects.
Preserve the original result and its limits. Current summaries link the evidence
applicable to their claim and retain known failures or missing gates.

Compare the checked revision/tree, uncommitted inputs, configuration, dependencies,
fixtures and environment with the next action. Reuse evidence only within its
recorded scope when those relevant inputs still match. A matching HEAD alone
does not identify a dirty tree or prove that external state is unchanged. Unknown
applicability must be resolved before claiming a required gate passes.

The [handoff workflow](agent-workflow.md#durable-handoff) carries this assessment
to the next session. Source requirements, decision authority and step status
continue to live in their canonical homes.
