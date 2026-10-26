# Adopt the foundation in an existing repository

Existing code is evidence, not an excuse to invent a perfect history. Adopting
this structure should make the present system understandable without claiming
that today's conventions were always enforced.

## Inspect before writing

Inventory source, manifests/lockfiles, migrations, tests, CI, deployment
configuration, runbooks, agent instructions, hooks, and repository settings
that are visible through authorized access.

Read existing documentation and compare its claims with the checkout. Record
the inspected revision and meaningful uncommitted differences. Use read-only
inspection first; do not run account-connected or destructive operations merely
to discover whether they work.

Separate:

- What the product is meant to do.
- What the code currently implements.
- What has actually been checked.
- What is deployed or externally configured.
- What remains unknown.

## Map existing facts to canonical homes

Move or consolidate documentation deliberately. Preserve stable IDs and inbound
references where possible. Add the documentation map and define which file owns
each kind of fact. Keep the root README focused on orientation and verified use.

Use arc42 to explain the actual system and clearly label desired changes.
Document current dependencies and data authority before proposing new modules.

An ADR written after implementation should state that it is retrospective,
identify the evidence/source, and distinguish an observed choice from owner
acceptance. Do not backdate approvals or present an inferred rationale as the
original author's reasoning.

## Reconcile differences

When an old README says a feature is planned but a roadmap says complete,
inspect the implementation and recorded evidence. Correct the source that owns
the status, then update the summary to link there. If proof is unavailable,
record the uncertainty instead of selecting the more optimistic statement.

When actual behavior conflicts with an accepted decision, record the discrepancy
as a risk or issue and ask about the intended resolution when needed. Do not
silently rewrite the decision to match the implementation.

Existing tests that use fakes remain useful within that boundary. Rename or
qualify their evidence claims; do not call them real-service integration unless
they exercise the relevant real protocol and service.

## Introduce process incrementally

Adopt the reading order, status vocabulary, PR template, and documentation
checker first. Adapt application check commands to the real stack.

Add provider permissions, local hooks, required checks, branch rules, and
evaluation tooling through explicit scoped work when they are useful. Inspect
existing protections before changing anything. Copying configuration neither
applies it nor proves it works.

If a Git policy is executable in multiple places, keep one policy
implementation and call it from hooks and CI rather than maintaining divergent
regular expressions. FounDaTionZy does not ship that larger enforcement system.

## Review the adoption as a real change

Use a branch/PR, describe source moves, resolve links, and run the actual checks.
Review for private information before any public publication.

The baseline can record known gaps and deferred work. It is complete when its
current-state claims are honest and the owner can decide what comes next, not
when every existing defect has been fixed.

The adoption does not require renaming application packages, replacing the
stack, rewriting working services, or renumbering historical roadmap steps.
