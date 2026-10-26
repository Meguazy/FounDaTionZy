# Open decisions

This register makes uncertainty actionable. A question is not resolved by a
proposed default, a successful experiment, or the absence of an owner reply.

The initial questions below are genuine initialization gates for a derivative
application. The template does not decide their answers.

| ID | Question | Status | Proposal / current knowledge | Owner | Decide by | Resolution / links |
| --- | --- | --- | --- | --- | --- | --- |
| OD-001 | What are the confirmed first-release requirements and exclusions? | open | Product fields are not initialized. | Project owner | Step 0 exit | [Product baseline](product/project-specification.md) |
| OD-002 | Which architecture choices must be accepted before the first implementation step? | open | Stack and deployment are intentionally unselected. | Project owner | Step 0 exit | [arc42](arc42/README.md), [ADR index](arc42/decisions/README.md) |
| OD-003 | What are the project's validation, review, publication, and merge authorities? | open | Template defaults exist; adapt them to the actual project. | Project owner | Step 0 exit | [Development](development.md), [contributing](../CONTRIBUTING.md) |

Add further questions discovered during initialization using stable
`OD-NNN` identifiers. Link relevant ADRs, experiments, and affected step
documents. Use `open`, `resolved`, or `deferred` as the question status;
the ADR has its own independent decision status.

Before step start/exit, enumerate every open/deferred question and proposed ADR
due at that boundary. Resolve blocking choices with the owner and record date,
direction, rationale, and source in the resolution cell or a linked record.

A deferral must explain why the current step can continue, what scope changes,
and the new `Decide by` boundary. Do not postpone a blocking item by changing
only its label. Keep resolved rows as history; do not reuse their IDs.
