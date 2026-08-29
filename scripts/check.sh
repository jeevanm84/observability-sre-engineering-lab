#!/usr/bin/env bash
set -euo pipefail
repository_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$repository_dir"
python3 -m compileall -q sre scripts tests
python3 -m unittest discover -s tests -v
python3 scripts/check.py
for scenario in scenarios/*.json; do
  ./scripts/evaluate.py --scenario "$scenario" --assert-expected >/dev/null
done
git diff --check

