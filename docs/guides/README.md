# Guide index

These guides explain how to use FounDaTionZy: how the documentation fits together,
how an agent initializes or adopts the foundation, and how humans and agents
maintain it during development.

Start here when you want to understand the method or choose a workflow. The
[documentation map](../README.md) points to the actual project requirements,
architecture, decisions, roadmap, and operational records.

## Choose a guide

| Guide | What it explains | Read it when |
| --- | --- | --- |
| [How the foundation works](how-it-works.md) | The complete loop from the owner's description to requirements, architecture, decisions, delivery steps, evidence, and acceptance; why each document has a specific responsibility. | You want an overview of the method and how its parts connect. |
| [Initialize a project](bootstrap.md) | What to tell an agent about a new application, which documents it must populate, how to handle unknowns, and what a reviewable baseline contains. | You are starting a new application from the template. |
| [Adopt an existing project](adoption.md) | How to inspect code and existing docs, reconstruct the current state, reconcile contradictions, and integrate the conventions while preserving project history and decisions. | You already have a repository and want to introduce the standard. |
| [Conventions and rationale](conventions-and-rationale.md) | The reasoning, costs, and limits behind document ownership, arc42, ADRs, status vocabulary, agent instructions, tests, Git, CI, and enforcement. | You want to understand a convention or assess a proposed change to it. |
| [Agent workflow](agent-workflow.md) | How to start/resume a session, scope a change, implement, verify, review, publish a PR, close a step, and hand off work; when delegation is appropriate. | You are doing day-to-day development or continuing another session's work. |
| [Provenance](provenance.md) | Which Money Tracker and Devflow snapshots informed the foundation, which conventions were generalized, and how differences and documentation drift were handled. | You want to understand where the standard came from and the limits of that comparison. |

## Recommended reading paths

### Understand the foundation

Read [how it works](how-it-works.md), then
[the conventions and rationale](conventions-and-rationale.md).
Use [provenance](provenance.md) for the source comparison.

### Start a new application

Read [how it works](how-it-works.md), follow [bootstrap](bootstrap.md), then use
[the agent workflow](agent-workflow.md) for implementation sessions.
The [root README](../../README.md#initialize-a-project) contains a ready-to-copy
initialization prompt.

### Bring an existing application into the standard

Read [adoption](adoption.md) first. Use [how it works](how-it-works.md) and
[the rationale](conventions-and-rationale.md) to map existing knowledge to its
canonical home, then follow [the agent workflow](agent-workflow.md) for ongoing
changes. Base current-state claims on inspected code and evidence.

### Continue development or hand off work

Follow [the agent workflow](agent-workflow.md), the project's
[repository instructions](../../AGENTS.md), and the
[documentation reading order](../README.md#required-reading-order).
Use the [record templates](../templates/README.md) for decisions, experiments,
evidence, exit reviews, and handoffs as needed.

## Guides and project records

The guides describe the reusable method. During initialization or adoption,
the agent fills the concrete product, architecture, decision, roadmap,
development, and operations documents for the application.

The [documentation map](../README.md#canonical-responsibilities) defines which
document owns each fact. Keep current requirements, decisions, delivery status,
and evidence in those records and link to them from explanatory material.
