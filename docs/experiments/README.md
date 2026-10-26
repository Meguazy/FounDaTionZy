# Experiments and evaluation gates

No project experiment has run. This index is for feasibility questions and,
when applicable, evaluations of nondeterministic application behavior.

| ID / record | Question | Step / decision gate | Required evidence | Outcome |
| --- | --- | --- | --- | --- |

Copy [the experiment template](experiment-template.md) to `EXP-NNN-topic.md`
and index it here. Probe code belongs under `experiments/EXP-NNN/`, not in
application modules; see [the probe-code convention](../../experiments/README.md).

Before execution, define the hypothesis, reproducible inputs, configuration
identity, pass/fail criteria, environment, cleanup, and applicable account/
credential/cost authorization. Use isolated fixtures and publish sanitized
results only.

Retain failures and inconclusive results. A correction creates a new run record,
not a rewritten historical success. Passing an experiment supplies evidence;
owner acceptance and ADR promotion remain separate decisions.

For models/prompts/tools, define representative datasets, regression cases,
quality thresholds, human evaluation where needed, and a recorded promotion
decision. Adopt this only if the application uses such behavior.
