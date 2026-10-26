#!/usr/bin/env python3
"""Check the foundation's documented structural invariants without dependencies.

This checker intentionally does not infer semantic truth, owner acceptance,
external-service compatibility, or effective repository protection.
"""

from __future__ import annotations

import argparse
import html
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

SKIP_DIRS = {
    ".git", ".venv", "node_modules", "target", "dist", "build", "__pycache__",
    ".private", ".claude", ".codex", "runtime", "artifacts", "worktrees",
}
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".json", ".toml"}
TEXT_NAMES = {"LICENSE", ".editorconfig", ".gitattributes", ".gitignore"}
REQUIRED = {
    "README.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md", "docs/README.md",
    "docs/product/README.md", "docs/product/project-specification.md",
    "docs/product/user-journeys.md", "docs/product/glossary.md",
    "docs/arc42/README.md", "docs/arc42/decisions/README.md",
    "docs/open-decisions.md", "docs/roadmap.md",
    "docs/roadmap/step-0-documentation-baseline.md",
    "docs/roadmap/sequencing-and-done.md", "docs/development.md",
    "docs/experiments/README.md", "docs/operations/README.md",
    "docs/workflows/README.md",
}
PROJECT_FIELDS = (
    "docs/product/project-specification.md", "docs/product/user-journeys.md",
    "docs/product/glossary.md", "docs/arc42/README.md", "docs/roadmap.md",
    "docs/roadmap/step-0-documentation-baseline.md",
)
STEP_STATUSES = {"planned", "active", "blocked", "complete", "deferred"}
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
HEADING = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
INLINE_LINK = re.compile(r"!?\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(?:\s+[^)\n]*)?\)")
DEFINITION = re.compile(r"^ {0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)", re.MULTILINE)
REFERENCE = re.compile(r"!?\[([^\]\n]+)\]\[([^\]\n]*)\]")


def paths_under(root: Path) -> list[Path]:
    """Return supported text files while excluding private/generated trees."""
    paths = []
    for directory, names, filenames in os.walk(root, followlinks=False):
        names[:] = sorted(n for n in names if n not in SKIP_DIRS)
        for name in sorted(filenames):
            path = Path(directory) / name
            if path.suffix in TEXT_SUFFIXES or name in TEXT_NAMES:
                paths.append(path)
    return paths


def markdown_body(text: str, label: str, errors: list[str]) -> str:
    """Remove fenced code while checking that opening fences are closed."""
    fence = None
    lines = []
    for number, line in enumerate(text.splitlines(), 1):
        match = FENCE.match(line)
        if fence is None and match:
            fence = (match[1][0], len(match[1]), number)
            lines.append("")
        elif fence is not None:
            if (match and match[1][0] == fence[0]
                    and len(match[1]) >= fence[1] and not match[2].strip()):
                fence = None
            lines.append("")
        else:
            lines.append(line)
    if fence is not None:
        errors.append(f"{label}:{fence[2]}: unclosed Markdown fence")
    return "\n".join(lines)


def heading_anchors(body: str) -> set[str]:
    """Build anchors for ordinary ATX headings, including duplicate suffixes."""
    anchors = set()
    counts: dict[str, int] = {}
    for line in body.splitlines():
        match = HEADING.match(line)
        if not match:
            continue
        heading = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", match[2])
        heading = re.sub(r"<[^>]+>", "", heading).replace("`", "")
        slug = re.sub(r"[^\w\- ]", "", html.unescape(heading).lower())
        slug = re.sub(r"\s", "-", slug)
        occurrence = counts.get(slug, 0)
        candidate = slug if occurrence == 0 else f"{slug}-{occurrence}"
        while candidate in anchors:
            occurrence += 1
            candidate = f"{slug}-{occurrence}"
        counts[slug] = occurrence + 1
        anchors.add(candidate)
    return anchors


def destinations(body: str, label: str, errors: list[str]) -> list[str]:
    """Collect simple inline/reference links, reporting undefined references."""
    without_code = re.sub(r"(`+).*?\1", "", body)
    definitions = {
        " ".join(m[1].lower().split()): m[2].strip("<>")
        for m in DEFINITION.finditer(without_code)
    }
    links = [m[1].strip("<>") for m in INLINE_LINK.finditer(without_code)]
    links.extend(definitions.values())
    for match in REFERENCE.finditer(without_code):
        key = " ".join((match[2] or match[1]).lower().split())
        if key not in definitions:
            errors.append(f"{label}: undefined reference link [{key}]")
        else:
            links.append(definitions[key])
    return links


def check(root: Path, initialized: bool) -> tuple[list[str], int, int]:
    """Validate text, links, discovery, indexes, and matching roadmap status."""
    errors: list[str] = []
    texts: dict[str, str] = {}
    for path in paths_under(root):
        label = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f"{label}: text-file symlinks are not supported")
            continue
        try:
            content = path.read_bytes()
            value = content.decode("utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"{label}: cannot read UTF-8 text: {exc}")
            continue
        texts[label] = value
        if content and not content.endswith(b"\n"):
            errors.append(f"{label}: missing final newline")
        if b"\r" in content:
            errors.append(f"{label}: expected LF line endings")
        for number, line in enumerate(value.splitlines(), 1):
            if line.rstrip(" \t") != line:
                errors.append(f"{label}:{number}: trailing whitespace")

    for label in sorted(REQUIRED - texts.keys()):
        errors.append(f"{label}: required baseline file is missing")

    bodies = {
        name: markdown_body(value, name, errors)
        for name, value in texts.items() if name.endswith(".md")
    }
    anchors = {name: heading_anchors(body) for name, body in bodies.items()}
    edges: dict[str, set[str]] = {name: set() for name in bodies}
    relative_count = 0
    for name, body in bodies.items():
        for destination in destinations(body, name, errors):
            try:
                parts = urlsplit(destination)
            except ValueError:
                errors.append(f"{name}: invalid link {destination!r}")
                continue
            if parts.scheme or parts.netloc:
                continue
            relative_count += 1
            raw_path = unquote(parts.path)
            target = (root / name).parent / raw_path if raw_path else root / name
            if raw_path.startswith("/"):
                errors.append(f"{name}: use a repository-relative link: {destination}")
                continue
            target = target.resolve()
            if not target.is_relative_to(root):
                errors.append(f"{name}: link leaves repository: {destination}")
                continue
            if not target.exists():
                errors.append(f"{name}: missing link target: {destination}")
                continue
            target_name = target.relative_to(root).as_posix()
            if target.is_dir():
                index = target / "README.md"
                if index.is_file():
                    target_name = index.relative_to(root).as_posix()
            if target_name in bodies:
                edges[name].add(target_name)
            if parts.fragment and target_name in anchors:
                fragment = unquote(parts.fragment)
                if fragment not in anchors[target_name]:
                    errors.append(f"{name}: missing heading anchor: {destination}")

    seen = set()
    pending = ["README.md", "AGENTS.md", "CONTRIBUTING.md", "CLAUDE.md",
               ".github/pull_request_template.md"]
    while pending:
        name = pending.pop()
        if name in seen:
            continue
        seen.add(name)
        pending.extend(edges.get(name, set()) - seen)
    for name in sorted(bodies.keys() - seen):
        errors.append(f"{name}: not discoverable from documentation entry points")

    for folder, pattern in (
        ("docs/arc42/decisions", "AD-[0-9]*-*.md"),
        ("docs/experiments", "EXP-[0-9]*-*.md"),
    ):
        index = f"{folder}/README.md"
        for path in sorted((root / folder).glob(pattern)):
            name = path.relative_to(root).as_posix()
            if name not in edges.get(index, set()):
                errors.append(f"{name}: missing direct link from {index}")

    architecture = bodies.get("docs/arc42/README.md", "")
    sections = re.findall(r"^## (\d+)\. ", architecture, re.MULTILINE)
    if sections != [str(i) for i in range(1, 13)]:
        errors.append("docs/arc42/README.md: expected sections 1 through 12 in order")

    indexed_steps = set()
    selected = []
    roadmap = bodies.get("docs/roadmap.md", "")
    row_pattern = re.compile(
        r"^\|\s*\[[^\]]+\]\((roadmap/step-[^)]+\.md)\)\s*\|"
        r"[^|]*\|\s*([^|]+?)\s*\|\s*$", re.MULTILINE,
    )
    for match in row_pattern.finditer(roadmap):
        name, status = f"docs/{match[1]}", match[2]
        if name in indexed_steps:
            errors.append(f"docs/roadmap.md: duplicate step row for {name}")
        indexed_steps.add(name)
        if status not in STEP_STATUSES:
            errors.append(f"{name}: invalid roadmap status {status!r}")
        step_status = re.search(r"^Status: (\S+)\s*$", bodies.get(name, ""), re.MULTILINE)
        if not step_status or step_status[1] != status:
            errors.append(f"{name}: status differs from roadmap index ({status})")
        if status in {"active", "blocked"}:
            selected.append(name)
    for path in sorted((root / "docs/roadmap").glob("step-[0-9]*-*.md")):
        name = path.relative_to(root).as_posix()
        if name not in indexed_steps:
            errors.append(f"{name}: missing roadmap status row")
    if len(selected) > 1:
        errors.append("docs/roadmap.md: more than one active/blocked step")

    if initialized:
        for name in PROJECT_FIELDS:
            if "TBD(project)" in texts.get(name, ""):
                errors.append(f"{name}: unresolved TBD(project) initialization field")
    return errors, len(bodies), relative_count


def main() -> int:
    """Run checks against this checkout or an explicit fixture root."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--initialized", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"repository root is not a directory: {root}")
    errors, documents, links = check(root, args.initialized)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAIL: {len(errors)} structural issue(s)", file=sys.stderr)
        return 1
    mode = "initialized" if args.initialized else "template"
    print(f"PASS: {documents} Markdown files, {links} relative links, {mode} mode")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
