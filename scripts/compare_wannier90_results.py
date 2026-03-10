#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path

from analyze_wannier90_result import analyze_path


def compare(paths: list[Path]) -> dict[str, object]:
    records = [analyze_path(path) for path in paths]
    records.sort(key=lambda item: (item["total_spread"] is None, item["total_spread"]))
    reference = next((record["total_spread"] for record in records if record["total_spread"] is not None), None)
    for record in records:
        spread = record["total_spread"]
        record["relative_spread"] = spread - reference if spread is not None and reference is not None else None
    return {"reference_spread": reference, "results": records}


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare multiple Wannier90 result directories.")
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    payload = compare([Path(path).expanduser().resolve() for path in args.paths])
    if args.json:
        print(json.dumps(payload, indent=2))
        return
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
