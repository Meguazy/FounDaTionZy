# Operations

No application runtime is supplied by this template. There is no installed
service, deployment, health endpoint, backup job, or rollback command to run.

- [Runbook template](runbook-template.md)

During initialization, identify required operational concerns and mark them
planned. As implementation lands, add verified runbooks for relevant setup,
configuration/identity, start/stop/health, safe retries, recovery, backup/restore,
retention, upgrades/rollback, and release procedures.

Each runbook names its environment, privileges, data boundaries, preconditions,
actual commands, expected observations, failure paths, cleanup/rollback, and
verification evidence. Never publish intended syntax as an installed command.

Keep secrets, native sessions, private datasets, and raw provider output out of
examples and evidence. Distinguish a local process restart from a demonstrated
backup restore or disaster-recovery test.
