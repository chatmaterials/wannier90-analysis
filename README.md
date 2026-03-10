# wannier90-analysis

[![CI](https://img.shields.io/github/actions/workflow/status/chatmaterials/wannier90-analysis/ci.yml?branch=main&label=CI)](https://github.com/chatmaterials/wannier90-analysis/actions/workflows/ci.yml) [![Release](https://img.shields.io/github/v/release/chatmaterials/wannier90-analysis?display_name=tag)](https://github.com/chatmaterials/wannier90-analysis/releases)

Standalone skill for post-run Wannier90 result analysis and multi-run comparison.

## Install

```bash
npx skills add chatmaterials/wannier90-analysis -g -y
```

## Local Validation

```bash
python3 -m py_compile scripts/*.py
npx skills add . --list
python3 scripts/analyze_wannier90_result.py fixtures/completed --json
python3 scripts/compare_wannier90_results.py fixtures/compare/alpha fixtures/compare/beta --json
python3 scripts/run_regression.py
```
