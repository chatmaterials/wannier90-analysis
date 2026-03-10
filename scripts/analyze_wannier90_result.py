#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(errors="ignore") if path.exists() else ""


def find_wout(path: Path) -> Path | None:
    candidates = sorted(path.glob("*.wout")) + sorted(path.glob("*.werr"))
    return candidates[0] if candidates else None


def analyze_path(path: Path) -> dict[str, object]:
    wout = find_wout(path)
    text = read_text(wout) if wout else ""
    spread_match = re.search(r"Omega Total\s*=\s*([\-0-9.Ee+]+)", text)
    spread = float(spread_match.group(1)) if spread_match else None
    completed = "Wannierisation convergence criteria satisfied" in text or "All done" in text
    observations = ["Wannier90 run completed." if completed else "Wannier90 run appears incomplete or unconverged."]
    return {
        "path": str(path),
        "completed": completed,
        "total_spread": spread,
        "observations": observations,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze a Wannier90 result directory.")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    record = analyze_path(Path(args.path).expanduser().resolve())
    if args.json:
        print(json.dumps(record, indent=2))
        return
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
