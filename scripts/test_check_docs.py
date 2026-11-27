#!/usr/bin/env python3
"""Behavior tests for the documentation checker, using standard library only.

Each test copies this checkout into a temporary fixture root, applies a focused
change, and asserts the checker's reported structural errors.
"""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_docs  # noqa: E402

REPO = Path(__file__).resolve().parents[1]

MODULE_ROW = (
    "| `engine` | Resolves sheets. | No module dependencies. | "
    "[README](../../crates/engine/README.md) | target |"
)

ADR_ROW = (
    "| [AD-001](AD-001-raw-sheets.md) | Store raw sheets | `engine` | proposed | "
    "Step 0 exit | planned |"
)

ADR = """# AD-001: Store raw sheets

- Decision status: proposed
- Implementation status: planned
- Affected components: {components}
"""

README_SECTIONS = {
    "Purpose": "Resolves character sheets.",
    "Global context": (
        "Component `engine` in the "
        "[building-block view](../../docs/arc42/README.md#5-building-block-view).\n"
        "Decisions: [ADR index](../../docs/arc42/decisions/README.md).\n"
        "Open questions: [OD register](../../docs/open-decisions.md)."
    ),
    "Public API": "Exposes `resolve`.",
    "Dependencies": "None.",
    "Owned data": "None.",
    "Invariants": "Deterministic.",
    "Related decisions": "- [AD-001](../../docs/arc42/decisions/AD-001-raw-sheets.md)",
    "Module docs": "- [Plan](docs/plan.md)",
    "Working on it": "Run the module tests.",
}

PLAN = """# engine plan

Governed by: [roadmap](../../../docs/roadmap.md).

| Capability | Step | Implementation |
| --- | --- | --- |
| Resolve sheets | [Step 0](../../../docs/roadmap/step-0-documentation-baseline.md) | planned |
"""


def readme(sections: dict[str, str]) -> str:
    """Render a module README from ordered section bodies."""
    parts = ["# engine\n"]
    for heading, body in sections.items():
        parts.append(f"## {heading}\n\n{body}\n")
    return "\n".join(parts)


class Fixture:
    """A temporary copy of the checkout with helpers for focused edits."""

    def __init__(self, root: Path) -> None:
        self.root = root

    def write(self, name: str, text: str) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def read(self, name: str) -> str:
        return (self.root / name).read_text(encoding="utf-8")

    def append_table_row(self, name: str, heading_prefix: str, row: str) -> None:
        """Append a row to the first table after the heading starting with prefix."""
        lines = self.read(name).splitlines()
        start = next(i for i, line in enumerate(lines) if line.startswith(heading_prefix))
        table = next(i for i in range(start, len(lines)) if lines[i].startswith("|"))
        end = table
        while end < len(lines) and lines[end].startswith("|"):
            end += 1
        lines.insert(end, row)
        self.write(name, "\n".join(lines) + "\n")

    def register_module(self, sections: dict[str, str] | None = None,
                        components: str = "`engine`", plan: str | None = PLAN) -> None:
        """Register `engine` in arc42 section 5 with a README, plan and ADR."""
        self.append_table_row("docs/arc42/README.md", "## 5. ", MODULE_ROW)
        self.write("crates/engine/README.md", readme(sections or README_SECTIONS))
        if plan is not None:
            self.write("crates/engine/docs/plan.md", plan)
        self.write("docs/arc42/decisions/AD-001-raw-sheets.md",
                   ADR.format(components=components))
        self.append_table_row("docs/arc42/decisions/README.md", "# ", ADR_ROW)

    def errors(self) -> list[str]:
        return check_docs.check(self.root.resolve(), False)[0]


class CheckerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        root = Path(self._tmp.name) / "repo"
        shutil.copytree(REPO, root, ignore=shutil.ignore_patterns(
            ".git", "__pycache__", "*.pyc"))
        self.fixture = Fixture(root)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def assertError(self, errors: list[str], *fragments: str) -> None:
        matches = [e for e in errors if all(f in e for f in fragments)]
        self.assertTrue(matches, f"no error containing {fragments!r} in:\n" + "\n".join(errors))


class TemplateTests(CheckerTestCase):
    def test_template_checkout_passes(self) -> None:
        self.assertEqual(self.fixture.errors(), [])


class FileDiscoveryTests(CheckerTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.fixture.write("pkg/README.md", "# Generated package\n")
        self.fixture.write(".gitignore", self.fixture.read(".gitignore") + "pkg/\n")

    def test_without_git_generated_markdown_is_checked(self) -> None:
        self.assertError(self.fixture.errors(), "pkg/README.md", "not discoverable")

    @unittest.skipUnless(shutil.which("git"), "git is not installed")
    def test_git_checkout_skips_ignored_files(self) -> None:
        subprocess.run(["git", "init", "-q", str(self.fixture.root)], check=True)
        self.assertEqual(self.fixture.errors(), [])


class ModuleDocsTests(CheckerTestCase):
    def test_registered_module_with_complete_docs_passes(self) -> None:
        self.fixture.register_module()
        self.assertEqual(self.fixture.errors(), [])

    def test_module_readme_requires_each_section(self) -> None:
        sections = dict(README_SECTIONS)
        del sections["Invariants"]
        self.fixture.register_module(sections)
        self.assertError(self.fixture.errors(), "crates/engine/README.md",
                         "missing section", "Invariants")

    def test_module_readme_links_global_decision_sources(self) -> None:
        sections = dict(README_SECTIONS)
        sections["Global context"] = sections["Global context"].replace(
            "[OD register](../../docs/open-decisions.md)", "the OD register")
        self.fixture.register_module(sections)
        self.assertError(self.fixture.errors(), "crates/engine/README.md",
                         "docs/open-decisions.md")

    def test_adr_affecting_module_is_linked_from_its_readme(self) -> None:
        sections = dict(README_SECTIONS)
        sections["Related decisions"] = "None yet."
        self.fixture.register_module(sections)
        self.assertError(self.fixture.errors(), "crates/engine/README.md",
                         "AD-001-raw-sheets.md")

    def test_adr_components_must_be_registered(self) -> None:
        self.fixture.register_module(components="`engine`, `ghost`")
        self.assertError(self.fixture.errors(), "AD-001-raw-sheets.md",
                         "unknown component", "ghost")

    def test_adr_requires_affected_components_field(self) -> None:
        self.fixture.register_module()
        self.fixture.write("docs/arc42/decisions/AD-001-raw-sheets.md",
                           "# AD-001: Store raw sheets\n\n- Decision status: proposed\n")
        self.assertError(self.fixture.errors(), "AD-001-raw-sheets.md",
                         "Affected components")

    def test_module_doc_requires_governing_source(self) -> None:
        self.fixture.register_module(plan=PLAN.replace(
            "Governed by: [roadmap](../../../docs/roadmap.md).", "A local plan."))
        self.assertError(self.fixture.errors(), "crates/engine/docs/plan.md",
                         "Governed by")

    def test_fixed_name_module_doc_names_its_global_source(self) -> None:
        self.fixture.register_module()
        self.fixture.write("crates/engine/docs/spec.md",
                           "# engine spec\n\nGoverned by: [roadmap](../../../docs/roadmap.md).\n")
        sections = dict(README_SECTIONS)
        sections["Module docs"] += "\n- [Spec](docs/spec.md)"
        self.fixture.write("crates/engine/README.md", readme(sections))
        self.assertError(self.fixture.errors(), "crates/engine/docs/spec.md",
                         "docs/product/project-specification.md")

    def test_plan_rows_link_global_steps(self) -> None:
        self.fixture.register_module(plan=PLAN + "| Later work | Step 9 | planned |\n")
        self.assertError(self.fixture.errors(), "crates/engine/docs/plan.md",
                         "roadmap step", "Later work")

    def test_module_templates_satisfy_module_checks(self) -> None:
        def skeletons(name: str) -> list[str]:
            text = self.fixture.read(f"docs/templates/{name}")
            return [block.split("\n", 1)[1] for block in text.split("````")[1::2]]

        def instantiate(text: str, root: str) -> str:
            return (text.replace("<component>", "engine").replace("{root}", root)
                    .replace("AD-NNN-topic", "AD-001-raw-sheets")
                    .replace("step-N-topic", "step-0-documentation-baseline"))

        self.fixture.register_module(plan=None)
        (readme_skeleton,) = skeletons("module-readme-template.md")
        self.fixture.write("crates/engine/README.md", instantiate(readme_skeleton, "../.."))
        names = ("plan.md", "spec.md", "design.md", "glossary.md", "testing.md")
        for name, skeleton in zip(names, skeletons("module-docs-template.md"), strict=True):
            self.fixture.write(f"crates/engine/docs/{name}", instantiate(skeleton, "../../.."))
        self.assertEqual(self.fixture.errors(), [])

    def test_module_doc_is_linked_from_module_readme(self) -> None:
        self.fixture.register_module()
        self.fixture.write("crates/engine/docs/notes.md",
                           "# Notes\n\nGoverned by: [arc42](../../../docs/arc42/README.md).\n")
        self.assertError(self.fixture.errors(), "crates/engine/docs/notes.md",
                         "not linked from crates/engine/README.md")


if __name__ == "__main__":
    unittest.main()
