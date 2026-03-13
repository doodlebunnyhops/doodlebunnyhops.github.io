#!/usr/bin/env python3
"""Check Markdown files for broken internal links and anchors.

Default behavior:
- Scans all Markdown files under ./content
- Validates internal links in the form [text](target)
- Ignores external links (http, https, mailto, tel, javascript)
- Optionally validates #fragment anchors for Markdown targets
"""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlsplit


LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")
CODE_FENCE_RE = re.compile(r"^\s{0,3}(```|~~~)")
HTML_ID_RE = re.compile(r"\sid=(?:\"([^\"]+)\"|'([^']+)')")

IGNORE_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}


@dataclass
class LinkIssue:
    source_file: Path
    line: int
    link: str
    reason: str


def slugify_heading(text: str) -> str:
    """Approximate Hugo/GitHub-style heading IDs for basic validation."""
    text = text.strip().lower()
    text = re.sub(r"[\[\]`*_~]", "", text)
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def iter_markdown_files(root: Path, include_drafts: bool = True) -> Iterable[Path]:
    patterns = ("*.md",)
    for pattern in patterns:
        for path in root.rglob(pattern):
            if not include_drafts and path.name.startswith("draft"):
                continue
            yield path


def split_markdown_link_target(raw_target: str) -> str:
    target = raw_target.strip()

    # Handle markdown form: (url "optional title")
    if target.startswith("<") and target.endswith(">"):
        return target[1:-1].strip()

    if " " in target:
        first, _rest = target.split(" ", 1)
        return first.strip()

    return target


def collect_headings(md_file: Path) -> set[str]:
    anchors: set[str] = set()
    in_fence = False

    with md_file.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if CODE_FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            m = HEADING_RE.match(line)
            if not m:
                continue

            heading_text = m.group(1).strip()
            if heading_text:
                anchors.add(slugify_heading(heading_text))

    return anchors


def resolve_target_path(
    *,
    source_file: Path,
    raw_path: str,
    project_root: Path,
    content_root: Path,
    static_root: Path,
    assets_root: Path,
) -> list[Path]:
    """Build candidate filesystem paths for a markdown link target."""
    path = unquote(raw_path).strip()

    is_absolute_site_path = raw_path.startswith("/")

    if is_absolute_site_path:
        rel = Path(path.lstrip("/"))
        base_candidates = [
            project_root / rel,
            content_root / rel,
            static_root / rel,
            assets_root / rel,
        ]
    else:
        rel = Path(path)
        base_candidates = [
            source_file.parent / rel,
            content_root / rel,
            project_root / rel,
        ]

    resolved: list[Path] = []
    for base in base_candidates:
        resolved.append(base)
        if base.suffix == "":
            resolved.append(base.with_suffix(".md"))
            resolved.append(base / "_index.md")
            resolved.append(base / "index.md")
    return resolved


def public_candidates(raw_path: str, public_root: Path) -> list[Path]:
    """Map a site URL path to likely files in Hugo public output."""
    rel = raw_path.strip("/")
    base = public_root / rel if rel else public_root

    candidates = [base]
    if rel == "":
        candidates.append(public_root / "index.html")
        return candidates

    if base.suffix:
        return candidates

    candidates.append(base / "index.html")
    candidates.append(base.with_suffix(".html"))
    return candidates


def collect_html_ids(html_file: Path) -> set[str]:
    ids: set[str] = set()
    with html_file.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for m in HTML_ID_RE.finditer(line):
                value = m.group(1) or m.group(2)
                if value:
                    ids.add(value)
    return ids


def source_url_base(md_file: Path, content_root: Path) -> str:
    """Best-effort URL base for a source markdown file."""
    rel = md_file.relative_to(content_root)
    rel_parent = rel.parent
    name = rel.name

    if name.startswith("_index"):
        parts = [p for p in rel_parent.parts if p]
    else:
        stem = name[:-3] if name.endswith(".md") else name
        if stem.endswith(".ru"):
            stem = stem[:-3]
        parts = [p for p in rel_parent.parts if p] + [stem]

    return "/" + "/".join(parts) + "/"


def resolve_relative_url(base_url: str, rel_target: str) -> str:
    """Resolve a relative URL against a page URL base, returning site-absolute path."""
    joined = posixpath.join(base_url, rel_target)
    normalized = posixpath.normpath(joined)
    if not normalized.startswith("/"):
        normalized = "/" + normalized
    return normalized


def check_links(
    *,
    project_root: Path,
    content_root: Path,
    validate_anchors: bool,
    include_images: bool,
    use_public: bool,
    public_root: Path,
) -> list[LinkIssue]:
    issues: list[LinkIssue] = []
    static_root = project_root / "static"
    assets_root = project_root / "assets"

    heading_cache: dict[Path, set[str]] = {}
    html_id_cache: dict[Path, set[str]] = {}

    for md_file in iter_markdown_files(content_root):
        page_base_url = source_url_base(md_file, content_root)
        with md_file.open("r", encoding="utf-8", errors="ignore") as f:
            for line_no, line in enumerate(f, start=1):
                for m in LINK_RE.finditer(line):
                    whole_match = m.group(0)
                    target_raw = m.group(1)

                    # Skip image links unless explicitly requested.
                    if whole_match.startswith("!") and not include_images:
                        continue

                    target = split_markdown_link_target(target_raw)
                    if not target:
                        continue

                    if target.startswith("#"):
                        if not validate_anchors:
                            continue
                        anchor = slugify_heading(unquote(target[1:]))
                        if md_file not in heading_cache:
                            heading_cache[md_file] = collect_headings(md_file)
                        if anchor not in heading_cache[md_file]:
                            issues.append(
                                LinkIssue(md_file, line_no, target, "anchor not found in same file")
                            )
                        continue

                    parts = urlsplit(target)
                    if parts.scheme.lower() in IGNORE_SCHEMES:
                        continue

                    link_path = parts.path
                    fragment = unquote(parts.fragment)

                    url_resolved_path = (
                        link_path
                        if link_path.startswith("/")
                        else resolve_relative_url(page_base_url, link_path)
                    )

                    candidates = resolve_target_path(
                        source_file=md_file,
                        raw_path=link_path,
                        project_root=project_root,
                        content_root=content_root,
                        static_root=static_root,
                        assets_root=assets_root,
                    )

                    if url_resolved_path != link_path:
                        candidates += resolve_target_path(
                            source_file=md_file,
                            raw_path=url_resolved_path,
                            project_root=project_root,
                            content_root=content_root,
                            static_root=static_root,
                            assets_root=assets_root,
                        )

                    # When enabled, absolute site links are validated against built output.
                    if use_public:
                        candidates = public_candidates(url_resolved_path, public_root) + candidates

                    existing = next((p.resolve() for p in candidates if p.exists()), None)
                    if existing is None:
                        issues.append(LinkIssue(md_file, line_no, target, "target path does not exist"))
                        continue

                    if validate_anchors and fragment and existing.suffix.lower() == ".md":
                        fragment_slug = slugify_heading(fragment)
                        if existing not in heading_cache:
                            heading_cache[existing] = collect_headings(existing)
                        if fragment_slug not in heading_cache[existing]:
                            issues.append(
                                LinkIssue(
                                    md_file,
                                    line_no,
                                    target,
                                    f"anchor '#{fragment}' not found in {existing.relative_to(project_root)}",
                                )
                            )

                    if validate_anchors and fragment and existing.suffix.lower() == ".html":
                        if existing not in html_id_cache:
                            html_id_cache[existing] = collect_html_ids(existing)
                        if fragment not in html_id_cache[existing]:
                            issues.append(
                                LinkIssue(
                                    md_file,
                                    line_no,
                                    target,
                                    f"anchor '#{fragment}' not found in {existing.relative_to(project_root)}",
                                )
                            )

    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check Markdown files for broken internal links.")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Path to project root (default: current directory)",
    )
    parser.add_argument(
        "--content-dir",
        default="content",
        help="Content directory relative to project root (default: content)",
    )
    parser.add_argument(
        "--check-anchors",
        action="store_true",
        help="Also validate markdown heading anchors (#fragment) for markdown targets.",
    )
    parser.add_argument(
        "--include-images",
        action="store_true",
        help="Also validate image markdown links: ![alt](target).",
    )
    parser.add_argument(
        "--use-public",
        action="store_true",
        help="Validate absolute site links against generated files in ./public first.",
    )
    parser.add_argument(
        "--public-dir",
        default="public",
        help="Public output directory relative to project root (default: public).",
    )
    return parser.parse_args()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()
    project_root = Path(args.project_root).resolve()
    content_root = (project_root / args.content_dir).resolve()
    public_root = (project_root / args.public_dir).resolve()

    if not content_root.exists():
        print(f"ERROR: content directory not found: {content_root}")
        return 2

    if args.use_public and not public_root.exists():
        print(f"ERROR: public directory not found: {public_root}")
        print("Run 'hugo -D' first, or omit --use-public.")
        return 2

    issues = check_links(
        project_root=project_root,
        content_root=content_root,
        validate_anchors=args.check_anchors,
        include_images=args.include_images,
        use_public=args.use_public,
        public_root=public_root,
    )

    if not issues:
        print("OK: No broken internal markdown links found.")
        return 0

    print(f"BROKEN LINKS: found {len(issues)} issue(s)")
    for issue in issues:
        rel = issue.source_file.relative_to(project_root)
        print(f"- {rel}:{issue.line} -> {issue.link}")
        print(f"  reason: {issue.reason}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
