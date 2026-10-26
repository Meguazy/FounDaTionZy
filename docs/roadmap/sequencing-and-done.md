# Sequencing and definition of done

## Sequencing rules

- Derive the order from product dependencies and feasibility risk.
- Work within the selected step and explicit owner changes.
- At step start/exit, enumerate all due unresolved ODs and proposed ADRs.
  Record owner resolutions or explicit justified deferrals before crossing gates.
- Use experiments early where an unsupported assumption could invalidate the
  architecture. Preparing a probe and running a live account/costly trial are
  different actions with different authorization needs.
- Address data ownership, privacy, migration, backup, and recovery when
  authoritative data is introduced, rather than saving them for release.
- Introduce narrow interfaces required by the active outcome; avoid shipping
  unrelated future behavior.
- Keep IDs stable across rescheduling and preserve historical evidence.
- Completion does not authorize the next step automatically.

## Definition of done for an implementation step

- Required production behavior and meaningful error paths exist.
- Appropriate unit, contract, real integration, E2E, and evaluation gates pass
  within explicitly described dependency and environment boundaries.
- Evidence matches the relevant revision/tree and states failures, skipped/
  unavailable/not-run checks, and residual limits.
- Configuration, permissions, secrets, storage/migrations, operations,
  rollback, and recovery consequences are addressed where applicable.
- Product, architecture, decisions, workflows, development, operations, and step
  evidence agree; new documents are discoverable from indexes.
- All exit criteria have a recorded assessment and all due decisions are resolved.
- The owner has accepted the presented scope and any explicitly recorded limits.
- The step and roadmap index are updated together with identical status.

For the documentation baseline, apply the relevant structural/design criteria
rather than inventing application test results. See
[Step 0](step-0-documentation-baseline.md).
