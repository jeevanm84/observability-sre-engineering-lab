#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from sre.model import SREError,evaluate,read_json
parser=argparse.ArgumentParser(); parser.add_argument("--scenario",type=Path,required=True); parser.add_argument("--assert-expected",action="store_true"); args=parser.parse_args()
try: result=evaluate(read_json(args.scenario))
except (OSError,json.JSONDecodeError,SREError) as error: print(f"evaluation error: {error}",file=sys.stderr); raise SystemExit(2)
print(json.dumps(result,indent=2)); raise SystemExit(1 if args.assert_expected and not result["decision_matches"] else 0)

