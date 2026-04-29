#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

MERMAID_FENCE_RE = re.compile(
    r"```mermaid\s*\n(.*?)```", re.DOTALL | re.IGNORECASE
)


@dataclass(frozen=True)
class MermaidTask:
    task_id: int
    md_file: Path
    rel_path: Path
    block_index: int
    block: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate Mermaid code blocks in markdown files via mmdc."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root (default: current directory).",
    )
    parser.add_argument(
        "--glob",
        default="**/*.md",
        help="Markdown glob pattern (default: **/*.md).",
    )
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Path prefix to include. Can be set multiple times.",
    )
    parser.add_argument(
        "--report",
        default="mermaid-validation-report.txt",
        help="Path to report file (default: mermaid-validation-report.txt).",
    )
    parser.add_argument(
        "--jobs",
        type=int,
        default=min(2, os.cpu_count() or 1),
        help="Number of parallel mmdc processes (default: 2 or CPU count).",
    )
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help="Validate only changed markdown files.",
    )
    parser.add_argument(
        "--base-ref",
        default="",
        help=(
            "Git base ref for --changed-only, for example origin/main. "
            "If omitted, checks local working tree changes vs HEAD."
        ),
    )
    return parser.parse_args()


def should_include(path: Path, include_prefixes: list[str]) -> bool:
    if not include_prefixes:
        return True
    normalized = path.as_posix()
    return any(
        normalized.startswith(prefix.rstrip("/") + "/")
        or normalized == prefix.rstrip("/")
        for prefix in include_prefixes
    )


def extract_mermaid_blocks(text: str) -> list[str]:
    return [
        match.group(1).strip() for match in MERMAID_FENCE_RE.finditer(text)
    ]


def list_changed_markdown_files(
    root: Path,
    pattern: str,
    base_ref: str,
) -> list[Path]:
    diff_range = f"{base_ref}...HEAD" if base_ref else "HEAD"
    commands = [
        [
            "git",
            "-C",
            str(root),
            "diff",
            "--name-only",
            "--diff-filter=ACMR",
            diff_range,
            "--",
            pattern,
        ],
        [
            "git",
            "-C",
            str(root),
            "ls-files",
            "--others",
            "--exclude-standard",
            "--",
            pattern,
        ],
    ]
    changed: set[Path] = set()
    for cmd in commands:
        proc = subprocess.run(  # noqa: S603
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            continue
        for line in proc.stdout.splitlines():
            path = (root / line.strip()).resolve()
            if path.is_file() and path.suffix == ".md":
                changed.add(path)
    return sorted(changed)


def collect_markdown_files(
    root: Path,
    pattern: str,
    include_prefixes: list[str],
    changed_only: bool,
    base_ref: str,
) -> list[Path]:
    if changed_only:
        candidates = list_changed_markdown_files(root, pattern, base_ref)
    else:
        candidates = [
            p
            for p in root.glob(pattern)
            if p.is_file() and ".git/" not in p.as_posix()
        ]

    return [
        p
        for p in candidates
        if p.is_relative_to(root)
        and should_include(p.relative_to(root), include_prefixes)
    ]


def collect_mermaid_tasks(root: Path, md_files: list[Path]) -> list[MermaidTask]:
    tasks: list[MermaidTask] = []
    task_id = 0
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        blocks = extract_mermaid_blocks(text)
        for block_index, block in enumerate(blocks, start=1):
            task_id += 1
            tasks.append(
                MermaidTask(
                    task_id=task_id,
                    md_file=md_file,
                    rel_path=md_file.relative_to(root),
                    block_index=block_index,
                    block=block,
                )
            )
    return tasks


def ensure_puppeteer_config(puppeteer_cfg: Path) -> None:
    if puppeteer_cfg.exists():
        return
    puppeteer_cfg.write_text(
        json.dumps({"args": ["--no-sandbox", "--disable-setuid-sandbox"]}),
        encoding="utf-8",
    )


def validate_task(
    task: MermaidTask,
    mmdc: str,
    work_dir: Path,
    puppeteer_cfg: Path,
) -> tuple[Path, int, str] | None:
    work_dir.mkdir(parents=True, exist_ok=True)
    ensure_puppeteer_config(puppeteer_cfg)

    in_file = work_dir / f"block_{task.task_id}.mmd"
    out_file = work_dir / f"block_{task.task_id}.svg"
    try:
        in_file.write_text(task.block + "\n", encoding="utf-8")
    except FileNotFoundError:
        in_file.parent.mkdir(parents=True, exist_ok=True)
        in_file.write_text(task.block + "\n", encoding="utf-8")

    cmd = [
        mmdc,
        "-q",
        "-p",
        str(puppeteer_cfg),
        "-i",
        str(in_file),
        "-o",
        str(out_file),
    ]
    proc = subprocess.run(  # noqa: S603
        cmd,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode == 0:
        return None

    details = (proc.stderr or proc.stdout or "").strip()
    return task.rel_path, task.block_index, details


def write_report(
    report_path: Path,
    files_count: int,
    total_blocks: int,
    failed: list[tuple[Path, int, str]],
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        "# Mermaid Validation Report",
        "",
        f"Checked markdown files: {files_count}",
        f"Checked Mermaid blocks: {total_blocks}",
        f"Failed Mermaid blocks: {len(failed)}",
        "",
    ]

    if failed:
        lines.extend(["## Failed blocks", ""])
        for rel_path, idx, details in failed:
            lines.append(f"- {rel_path} (block #{idx})")
            if details:
                lines.extend(["  ```"])
                lines.extend(f"  {line}" for line in details.splitlines())
                lines.append("  ```")
            lines.append("")
    else:
        lines.extend(["Mermaid validation passed.", ""])

    report_path.write_text("\n".join(lines), encoding="utf-8")


def print_summary(
    files_count: int,
    total_blocks: int,
    failed_count: int,
    jobs: int,
    changed_only: bool,
    base_ref: str,
    report_path: Path,
) -> None:
    print(f"Checked markdown files: {files_count}")
    print(f"Checked Mermaid blocks: {total_blocks}")
    print(f"Failed Mermaid blocks: {failed_count}")
    print(f"Parallel jobs: {jobs}")
    if changed_only:
        print("Mode: changed files only")
        if base_ref:
            print(f"Base ref: {base_ref}")
    print(f"Report written to: {report_path}")


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()

    mmdc = shutil.which("mmdc")
    if not mmdc:
        print(
            "ERROR: 'mmdc' is not found in PATH. Install @mermaid-js/mermaid-cli.",
            file=sys.stderr,
        )
        return 2

    md_files = collect_markdown_files(
        root=root,
        pattern=args.glob,
        include_prefixes=args.include,
        changed_only=args.changed_only,
        base_ref=args.base_ref,
    )
    tasks = collect_mermaid_tasks(root, md_files)
    total_blocks = len(tasks)
    failed: list[tuple[Path, int, str]] = []
    report_path = Path(args.report).resolve()
    jobs = max(1, args.jobs)

    work_dir = root / ".mermaid-validate-work"
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)
    puppeteer_cfg = work_dir / "puppeteer.json"

    try:
        ensure_puppeteer_config(puppeteer_cfg)
        with ThreadPoolExecutor(max_workers=jobs) as executor:
            futures = [
                executor.submit(validate_task, task, mmdc, work_dir, puppeteer_cfg)
                for task in tasks
            ]
            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    failed.append(result)
    finally:
        if work_dir.exists():
            shutil.rmtree(work_dir)

    failed.sort(key=lambda item: (item[0].as_posix(), item[1]))
    write_report(report_path, len(md_files), total_blocks, failed)
    print_summary(
        files_count=len(md_files),
        total_blocks=total_blocks,
        failed_count=len(failed),
        jobs=jobs,
        changed_only=args.changed_only,
        base_ref=args.base_ref,
        report_path=report_path,
    )

    if failed:
        for rel_path, idx, details in failed:
            print(f"\n- {rel_path} (block #{idx})")
            if details:
                print(details)
        return 1

    print("Mermaid validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
