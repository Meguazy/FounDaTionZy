# Development and documentation checks

This checkout supplies documentation and a Python standard-library checker.
It does not supply application code, a package manager, or a chosen stack.

## Current commands

Use Python 3.11 or newer. No Python package installation is required.

```sh
python3 scripts/check_docs.py
git diff --check
```

After initializing a derivative application's concrete baseline:

```sh
python3 scripts/check_docs.py --initialized
```

The initialized mode additionally rejects remaining `TBD(project)` fields in
the concrete product, arc42, roadmap, and Step 0 documents. Replace unknown
fields with a linked OD and honest status, not an invented answer. This mode
does not decide whether the owner accepted the result.

## What the checker covers

- Required baseline files and UTF-8 text hygiene: final newline, LF endings,
  and trailing whitespace in supported text files.
- Closed Markdown fences.
- Relative inline and reference-style links, target paths, and fragments for
  ordinary GitHub-style ATX headings in Markdown.
- Markdown discoverability from the root README/agent/contribution entry points.
- ADR/experiment records discoverable from their indexes.
- Roadmap rows linked to step documents, matching status, valid step statuses,
  and at most one selected active/blocked step.
- Twelve numbered arc42 sections.
- Unresolved project-field markers in initialized mode.

It supports this repository's Markdown conventions, not every extension of
Markdown. Use relative Markdown links, ATX headings, and simple destinations;
custom HTML anchors, generated docs, and other schemas need explicit tooling.

It does not check external URL availability, semantic correctness, complete
requirements, actual OD/ADR acceptance, application behavior, secrets, provider
capabilities, live repository settings, or CI enforcement. Review those directly.
A clean result does not make an application ready for release.

## Hosted CI

[The documentation workflow](../.github/workflows/docs.yml) runs the checker
and committed whitespace checks on pushes to `main`, PRs targeting `main`,
and manual dispatch. It uses read-only contents permission, disables persisted
checkout credentials, pins its checkout action by commit SHA, and needs no
owner secrets or private accounts.

It does not install branch protection, metadata enforcement, Git hooks, harness
permission rules, or application test jobs. A workflow definition and an actual
successful run are separate facts. The project owner decides which checks
become required and verifies the live settings in explicit setup work.

## Add project-specific development guidance

TBD(project): Once the initial scaffold is selected and implemented, document
verified prerequisites, pinned toolchains/dependencies, actual build/run/lint/
test/evaluation commands, test layout, fixtures, and local/hosted gate mapping.

Keep unit, contract/fake, real integration, and E2E boundaries explicit. Some
gates may require owner-controlled hardware, accounts, installed services, or
real models. Report those as local gates with exact results; do not replace
their dependencies and retain the same acceptance claim.

Language-specific docstrings, source layout, logging implementation, coverage
policies, and cross-platform support belong to the initialized project's
accepted choices. Planned commands must remain visibly planned.

## Project test strategy

During initialization or adoption, the agent proposes a concise strategy based
on requirements, architecture, risks, and existing tests. Explain the recommended
approach, meaningful alternatives, costs, and evidence limits. Suite layout,
tools, and thresholds follow the project; the foundation supplies the outline.

TBD(project): Replace this outline with the project's strategy and linked
decisions. Keep commands planned until they can be verified.

1. **Behavior and risk:** identify critical journeys, invariants, failure/recovery
   paths, and observable assertions. Include regressions for relevant defects.
2. **Verification boundaries:** select the levels needed, such as unit, contract,
   real integration, E2E, or model evaluations. State actual dependencies, where
   fakes are appropriate, and what each result can establish.
3. **Organization and reliability:** follow the language/ecosystem's conventions;
   describe test placement, fixtures, isolation, deterministic inputs, cleanup,
   and useful failure diagnostics. Keep assertions focused on behavior.
4. **Execution and evidence:** document verified commands, local/CI placement,
   required environments, revision identity, outcomes, and skipped/not-run gates.
5. **Acceptance and tradeoffs:** propose required checks and accepted gaps.
   Choose coverage targets or advanced techniques only when justified by risk
   and maintenance cost; no universal directory tree or numeric threshold applies.

The owner decides material guarantees, accepted risks, and required gates.
The agent handles reversible details within existing authorization. Record
agreed choices here and unresolved items in the
[OD register](open-decisions.md) with a deadline before they are relied on.
Use an ADR when the choice has significant architectural consequences.

### Test-first behavior changes

Use this default sequence within the agreed strategy:

1. **RED:** add a focused test for the intended behavior and run it against the
   unchanged implementation. Verify that it fails for the expected missing or
   incorrect behavior; infrastructure/setup errors do not establish RED.
2. **GREEN:** implement the behavior and run the focused test and affected checks.
3. **REFACTOR:** improve the design while keeping the relevant checks green.

A pure refactor starts from passing tests. If a new test already passes because
the behavior exists, retain useful regression coverage and record that fact.
Documentation-only changes use structural checks and review. When test-first is
impractical, record the reason and alternative validation in the change evidence;
resolve any resulting change to accepted guarantees or gates with the owner.
Preserve earlier authorization and avoid seeking approval for every test detail.

## Before publishing

Inspect the entire diff, run applicable checks, review private material, and
update affected indexes/statuses. Follow [the contribution process](../CONTRIBUTING.md)
and [the evidence template](templates/evidence-template.md).
