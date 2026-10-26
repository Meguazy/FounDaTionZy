# How the foundation works

FounDaTionZy treats documentation as the project's durable working memory.
An agent session is temporary: its context can be shortened, another agent may
take over, and the owner may return weeks later. The repository must preserve
what the application is meant to do, which choices are binding, where delivery
stands, and what has actually been demonstrated.

The method is a feedback loop. It starts with a product discussion, becomes a
reviewable design and delivery plan, guides one bounded implementation change,
then absorbs the evidence and corrections from that change. It is useful even
without AI: humans need the same distinctions and traceability.

## 1. Describe the application before choosing its machinery

The owner explains goals, users, concrete examples, workflows, exceptions,
constraints, and non-goals. The agent consolidates this into
[the product baseline](../product/project-specification.md), supported by
[journeys](../product/user-journeys.md) and a [glossary](../product/glossary.md).

A request such as "build a booking application" leaves critical behavior open.
Who can book? What is being reserved? Can reservations overlap? Who can cancel?
Does a failed payment reserve capacity? These are product questions. Choosing a
framework first can hide them behind accidental implementation defaults.

The baseline preserves the full set of requirements, including less visible
constraints such as offline use, recovery, access control, portability, or
manual intervention. Focused documents explain parts of that baseline; they do
not replace it with shorter, incompatible versions.

## 2. Give each document a specific job

| Question | Canonical home | Why it lives there |
| --- | --- | --- |
| What problem and behavior are required? | Product baseline | Requirements survive implementation changes. |
| How do users encounter that behavior? | User journeys | Examples expose missing transitions and exceptions. |
| How is the system structured? | arc42 | Multiple architecture views describe the same system. |
| Why choose this option over alternatives? | ADR | A decision needs context and consequences, not only a diagram. |
| What is still undecided, and when does it block? | Open-decision register | Unknowns become actionable work with a deadline. |
| What is delivered next? | Roadmap index | One place identifies delivery order and active scope. |
| What proves a step is finished? | Individual step document | Evidence stays beside the criteria it supports. |
| Does an uncertain approach work? | Experiment record | Measurements remain separate from an architectural preference. |
| How do developers run checks? | Development guide | Commands describe the current checkout. |
| How do operators run and recover it? | Operations runbooks | Runtime procedures have different risks and users. |
| How must agents behave here? | AGENTS.md | Short instructions direct agents to the durable knowledge. |

This is a division of responsibility, not a demand to repeat everything twelve
times. An ADR links to the relevant quality scenario; a step links to the ADR
and experiment; the README links to the documentation map. Links connect facts
without creating extra authoritative copies.

## 3. Separate decisions from delivery

Two independent status dimensions prevent a common source of confusion.

| Statement | Decision status | Delivery/evidence status |
| --- | --- | --- |
| "We recommend SQLite." | Proposed | No implementation follows. |
| "The owner chose SQLite." | Accepted | It may still be planned. |
| "A SQLite adapter exists and passed local storage tests." | Accepted if previously selected | Implemented within the recorded local boundary. |
| "A fake provider passed the application scenario." | The provider choice may remain open | Fake-boundary evidence only. |
| "An alternative is intentionally postponed." | Deferred with rationale/deadline | No delivery claim. |

Decision statuses include `proposed`, `accepted`, `rejected`, `superseded`,
and `deferred`. Implementation can be `planned`, `partial`, or
`implemented`; a capability can also be `experiment-gated`. Experiments use
outcomes such as `not run`, `passed`, `failed`, and `inconclusive`.

An owner can accept an architectural direction while a feasibility question
remains open. The record must identify that dependency. A successful experiment
does not automatically accept an ADR, and an accepted ADR does not make its
commands runnable.

## 4. Use architecture to explain boundaries

The [arc42 document](../arc42/README.md) covers goals, constraints, context,
strategy, building blocks, runtime, deployment, cross-cutting concerns,
decisions, quality, risks, and vocabulary. These views answer different
questions about the same application.

For example, a storage component needs more than a box:

- The building-block view states its responsibility and interface.
- The runtime view shows transaction and failure ordering.
- The deployment view shows where the authoritative data resides.
- Quality scenarios define observable recovery requirements.
- Operations describes a verified backup and restore procedure.
- An ADR explains the storage choice and rejected alternatives.

The level of detail follows the risk. A small library can have short deployment
and operations sections marked not applicable with a reason. Empty headings
and speculative infrastructure do not improve architecture.

Keep deterministic rules separate from I/O and provider details. Introduce a
component when responsibility, ownership, lifecycle, trust boundary, or reason
to change differs. Splitting every file into its own layer creates a different
maintenance problem.

## 5. Make uncertainty visible before it becomes code

Use an OD for an unresolved question, an ADR for a consequential choice, and an
experiment for a question that needs evidence. They often link to each other,
but their roles differ.

Illustrative chain:

```text
OD-007: Can the required offline mode meet the storage/recovery needs?
EXP-002: Measure the candidate's recovery behavior with isolated fixtures.
AD-004: Select the storage approach using the measured tradeoffs.
Step 1 start: requires OD-007 resolved and AD-004 accepted.
```

These are examples, not decisions of this template.

Every blocking OD and proposed ADR names a `Decide by` boundary, such as
`Step 1 start` or `Step 2 exit`. Before passing that boundary, enumerate the
due items and ask the owner for the unresolved choices. A deferral is itself
recorded with its rationale, new deadline, and scope impact. Silence cannot
promote the suggested default.

This does not require deciding the whole product upfront. Decide what the next
step depends on; leave later, reversible choices open with a real deadline.

## 6. Deliver outcomes through bounded steps

The roadmap is a sequence of independently verifiable outcomes rather than a
calendar promise. Its index stays short. Each step owns intent, prerequisites,
deliverables, non-goals, exit criteria, and evidence.

A useful first slice exercises meaningful behavior across the required
boundaries. A list such as "add files, add classes, add routes" describes
activity; "a user can create and recover a reservation without double booking"
describes an outcome that can be checked.

Keep step identifiers stable when scheduling changes. Defer or insert work
without renumbering the history that existing evidence references. A new scope
request can change the roadmap, but the owner direction and consequences must
be recorded.

Before implementation, verify the active scope and due decisions. Before
closure, assess each exit criterion against evidence, expose gaps, obtain owner
acceptance, and update the step and index together.

## 7. Let evidence limit the claim

Record what ran, on which revision or tree, in what environment, with which
dependencies, and what it demonstrated. Include failures, skips, not-run gates,
and limits.

| Evidence | Supports | Does not by itself support |
| --- | --- | --- |
| Documentation checker | Selected structural invariants | Product correctness or completeness. |
| Unit test | A narrow production behavior/invariant | External service compatibility. |
| Contract test with fake | Shared boundary semantics | A real account/provider working. |
| Real storage integration | Actual persistence behavior in that environment | Full product acceptance or every OS. |
| Application E2E with fake providers | Whole application path through declared fake boundaries | Real-provider end-to-end acceptance. |
| Isolated live integration | That service/account/version/fixture scope | Unlimited compatibility or future availability. |
| Owner acceptance | A recorded scope accepted with stated limits | Every deferred capability implemented. |

A fresh code/configuration revision may invalidate affected test or review
evidence. Keep the relevant source identity with the evidence and rerun the
affected gates. Do not inflate a local smoke test into a production guarantee.

## 8. Keep review and authority explicit

An agent can draft, implement, check, and explain. Its own statement that work
is correct is not an independent review or owner acceptance. A second review
session can help expose blind spots; the review should state its context,
scope, revision, findings, and limits.

Default to one writing agent. Multiple concurrent writers need explicit
delegation, file/scope boundaries, shared contracts, and an integration owner.
Parallel activity is useful only when it reduces dependencies and does not
create conflicting implementations or false review independence.

Repository instructions and local hooks guide behavior. CI repeats executable
checks. Server-side rules can prevent invalid merges when actually configured.
These are different enforcement layers. This template supplies a documentation
workflow and CI file; it does not claim to install every layer.

## 9. Revisit the baseline as the product changes

A change can affect requirements, interfaces, data ownership, failure handling,
deployment, or operations. Update the documents that own those facts in the
same cohesive change. If a requirement changes, follow its links through
journeys, architecture, decisions, workflow contracts, roadmap, and checks.

When sources disagree, inspect the code and evidence and resolve the canonical
documents. Do not pick whichever sentence permits the easiest next step.
[Adoption](adoption.md) explains this process for existing repositories.

The cost is deliberate maintenance. The benefit is that a new contributor or
agent can reconstruct the project's intent and current state without access to
the original conversation.
