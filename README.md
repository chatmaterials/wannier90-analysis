# wannier90-analysis

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
