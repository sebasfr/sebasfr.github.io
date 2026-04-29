"""Rename Obsidian source notes back to numbered order.

Idempotent: skips if source missing or target already exists. Never deletes.
"""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ORDER: dict[str, list[str]] = {
    "_posts/MA0350": [
        "Sucesiones",
        "Subsucesiones",
        "Límite superior e inferior",
        "Series numéricas",
        "Criterios de convergencia de series",
        "Integral de Riemann",
        "Técnicas de integración",
        "Aplicaciones de la integral de Riemann",
        "Integrales impropias",
        "Series de funciones",
        "Convergencia de funciones",
        "Tópicos importantes y ejemplos",
    ],
    "_posts/MA0450": [
        "Topología en Rn",
        "Funciones de varias variables",
        "Diferenciación",
        "Integración en Rn",
        "Cálculo vectorial",
    ],
}


def main(dry_run: bool) -> int:
    problems: list[str] = []
    actions: list[tuple[Path, Path]] = []

    for folder, titles in ORDER.items():
        folder_path = ROOT / folder
        if not folder_path.is_dir():
            problems.append(f"missing folder: {folder}")
            continue
        for idx, title in enumerate(titles, start=1):
            src = folder_path / f"{title}.md"
            dst = folder_path / f"{idx:02d} - {title}.md"
            if src == dst:
                continue
            if dst.exists():
                # Already numbered — leave alone
                continue
            if not src.exists():
                problems.append(f"source not found: {src.relative_to(ROOT)}")
                continue
            actions.append((src, dst))

    print("Planned renames:")
    for src, dst in actions:
        print(f"  {src.relative_to(ROOT)}")
        print(f"    -> {dst.relative_to(ROOT)}")
    if not actions:
        print("  (none)")

    if problems:
        print("\nIssues:")
        for p in problems:
            print(f"  - {p}")

    if dry_run:
        print("\n(dry run — no changes made)")
        return 0

    for src, dst in actions:
        os.rename(src, dst)
    print(f"\nRenamed {len(actions)} files.")
    return 0 if not problems else 1


if __name__ == "__main__":
    import sys
    dry = "--apply" not in sys.argv
    raise SystemExit(main(dry_run=dry))
