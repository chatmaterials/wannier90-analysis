---
name: "wannier90-analysis"
description: "Use when the task is to analyze completed or incomplete Wannier90 outputs, including spread summaries, convergence interpretation, comparing multiple Wannier models, and summarizing .wout results."
---

# Wannier90 Analysis

Use this skill for post-run Wannier90 result analysis rather than workflow setup.

## When to use

- analyze a completed or incomplete Wannier90 run
- compare spreads across multiple Wannier90 directories
- summarize convergence from `.wout`
- write a compact report from existing Wannier90 results

## Use the bundled helpers

- `scripts/analyze_wannier90_result.py`
  Summarize a single Wannier90 result directory.
- `scripts/compare_wannier90_results.py`
  Compare multiple Wannier90 result directories by spread and status.

## Guardrails

- Do not treat unconverged localization as a trustworthy final model.
- Distinguish spread extraction from the physical quality of the low-energy model.
