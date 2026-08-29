#!/usr/bin/env bash
set -euo pipefail
repository_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$repository_dir/.local"
"$repository_dir/scripts/evaluate.py" --scenario "$repository_dir/scenarios/fast-burn.json" --assert-expected > "$repository_dir/.local/incident-evaluation.json"
echo "Critical page confirmed in both 5m and 1h windows. Follow docs/RUNBOOK.md."

