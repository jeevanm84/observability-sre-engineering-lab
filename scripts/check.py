#!/usr/bin/env python3
import re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from sre.model import evaluate,read_json
fail=[]
scenarios=list((ROOT/"scenarios").glob("*.json"))
for path in scenarios:
    if not evaluate(read_json(path))["decision_matches"]: fail.append(f"{path}: decision mismatch")
catalog=read_json(ROOT/"service-catalog/checkout-api.json")
for key in ("owner","runbook","dependencies","slos","telemetry_labels"):
    if not catalog.get(key): fail.append(f"catalog missing {key}")
for path in ROOT.rglob("*.md"):
    text=path.read_text()
    if not re.search(r"^#\s+\S",text,re.M): fail.append(f"{path}: missing H1")
forbidden=("mamu"+"durijk","mamu"+"duri-jeevankumar","@g"+"mail.com")
for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix in {".md",".py",".sh",".json",".yml",".yaml"} and ".git" not in path.parts:
        if any(value in path.read_text().lower() for value in forbidden): fail.append(f"{path}: identity")
if fail: print("\n".join(fail),file=sys.stderr);raise SystemExit(1)
print(f"Validated {len(scenarios)} SLO scenarios and {len(list(ROOT.rglob('*.md')))} Markdown files.")

