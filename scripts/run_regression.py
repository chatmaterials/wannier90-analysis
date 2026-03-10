#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, *args], cwd=ROOT, text=True, capture_output=True, check=True)


def run_json(*args: str):
    return json.loads(run(*args).stdout)


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    single = run_json("scripts/analyze_wannier90_result.py", "fixtures/completed", "--json")
    ensure(single["completed"] is True, "completed fixture should be complete")
    ensure(abs(single["total_spread"] - 3.21) < 1e-6, "single-run spread should parse")

    compare = run_json("scripts/compare_wannier90_results.py", "fixtures/compare/alpha", "fixtures/compare/beta", "--json")
    ensure(compare["results"][0]["path"].endswith("alpha"), "alpha should have lower spread than beta")
    ensure(compare["results"][1]["relative_spread"] > 0, "beta should have larger spread")

    print("wannier90-analysis regression passed")


if __name__ == "__main__":
    main()
