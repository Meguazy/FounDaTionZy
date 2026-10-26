# Contributing

Start with [AGENTS.md](AGENTS.md), the [documentation map](docs/README.md), and
the current roadmap step. The detailed process and rationale are in
[the agent workflow](docs/guides/agent-workflow.md).

## Changes and history

Use one branch and one PR per cohesive change. Start from an up-to-date `main`
without discarding local work. Name branches `<type>/<topic>`, or
`<type>/step-N-<topic>` for roadmap work. Use lowercase kebab-case topics.
Examples: `docs/project-baseline`, `feat/step-1-first-slice`.

Use Conventional Commits:

```text
<type>(<optional-scope>): <imperative summary>
```

Typical types: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `build`,
`ci`, and `chore`. Mark breaking changes explicitly. Every commit has exactly
one author; do not add `Co-authored-by` or other agent attribution trailers.

Keep change branches linear and resolve updates by rebasing when appropriate.
Do not rewrite another contributor's work. Review the entire diff before
committing; never use `--no-verify` or bypass installed checks.

The initial creation of an empty repository is a documented bootstrap exception:
a seed/default-branch commit is needed before PRs exist. This exception does not
authorize later direct-to-main development. FounDaTionZy's initial publication
is that bootstrap; derivative projects should open their initialization change
as a PR against the template's existing default branch.

## Pull requests

Use the PR template. Explain the resulting behavior, scope, validation, affected
documents, operational impact, unresolved risks, and owner decisions. Report
exact counts when a test runner provides them; do not invent counts for checks
that only return a status.

The owner merges by default. Prefer squash merge for a concise main history.
A project can select a different merge policy during bootstrap and record why.
No merge setting or protection is installed by copying this repository.

A new implementation revision invalidates evidence for the old revision where
the changed code/configuration affects that evidence. Run the affected gates
again. Do not present an earlier CI/review result as proof for a different head.

## Documentation and gates

Run:

```sh
python3 scripts/check_docs.py
git diff --check
```

Application-specific commands are added to [development](docs/development.md)
only after the chosen scaffold exists and the commands have been verified.
A structural check is not an application test or owner acceptance.

Step closure follows [the sequencing rules](docs/roadmap/sequencing-and-done.md).
Present an exit review with evidence and limits, record owner acceptance, and
update the step and index together. A dedicated closure PR is preferred for a
substantial milestone, but a small project may combine closure with an already
authorized change if acceptance is recorded.

## Permissions and licensing

Keep private material out of public changes. Check the actual diff and artifacts,
not only ignore patterns. Never copy personal configuration or provider sessions.

FounDaTionZy is [MIT-licensed](LICENSE); preserve that notice for reused template
material. The template does not choose a license for a derivative application's
new code. Select and record the project's license before claiming it is
available under one. A public
repository is a visibility setting; its files and publication history must be
reviewed for the audience you intend.
