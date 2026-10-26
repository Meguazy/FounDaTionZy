# Behavioral workflow contracts

No application workflow is specified yet. Use this area only when lifecycle
semantics, state transitions, external effects, or integration contracts need
an explicit shared reference.

- [Workflow contract template](workflow-template.md)

Distinguish the application's behavior from the human/agent development process,
which is described in [the agent guide](../guides/agent-workflow.md).

A project may add a versioned YAML/JSON specification if it improves precision.
Select its schema and canonical authority explicitly, validate references and
conformance, and explain whether it is documentation or runtime configuration.
A state diagram or YAML file alone is not an executable workflow engine.

Preserve state/event IDs when meanings stay stable. Document guards, authority,
effect ordering, duplicate/stale events, concurrency, failure, retry, and
recovery. Diagrams are projections and must not silently remove requirements.
