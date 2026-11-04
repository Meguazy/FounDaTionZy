# Reusable record templates

These files explain the shape of future records. They do not contain project
acceptance or results.

- [Handoff](handoff-template.md)
- [Validation evidence](evidence-template.md)
- [Step exit review](exit-review-template.md)
- [Architecture decision](../arc42/decisions/adr-template.md)
- [Roadmap step](../roadmap/step-template.md)
- [Experiment](../experiments/experiment-template.md)
- [Workflow contract](../workflows/workflow-template.md)
- [Operations runbook](../operations/runbook-template.md)

Store completed records beside the concern they describe and link them from
the relevant index, following [current state and history](../guides/current-state-and-history.md).
For handoffs, use the [handoff index](../handoffs/README.md) and
[write/resume protocol](../guides/agent-workflow.md#durable-handoff). A checkpoint
links current roadmap status and captures evidence applicability, pending work
and the next authorized action; it does not maintain another authority source.

Step and handoff templates include `Required context` maps. Use them to link
canonical sections and stable IDs for the requested outcome, following
[the reading protocol](../README.md#required-reading-order).
