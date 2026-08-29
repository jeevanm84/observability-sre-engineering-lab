"""SLO math and multi-window burn-rate decisions."""
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

class SREError(ValueError):
    """Invalid reliability evidence."""

@dataclass(frozen=True)
class Window:
    name: str
    minutes: int
    valid_events: int
    bad_events: int
    slow_events: int

def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)

def validate(document: dict[str, Any]) -> None:
    missing = [key for key in ("name", "service", "slo", "windows", "expected_decision") if key not in document]
    if missing:
        raise SREError(f"missing fields: {', '.join(missing)}")
    target = document["slo"].get("availability_target")
    if not isinstance(target, (int, float)) or not 0 < target < 1:
        raise SREError("availability_target must be between zero and one")
    for item in document["windows"]:
        valid, bad, slow = item.get("valid_events"), item.get("bad_events"), item.get("slow_events")
        if not all(isinstance(value, int) for value in (valid, bad, slow)) or valid <= 0:
            raise SREError("event counts must be integers and valid_events positive")
        if not 0 <= bad <= valid or not 0 <= slow <= valid:
            raise SREError("bad and slow events must be within valid events")

def evaluate(document: dict[str, Any]) -> dict[str, Any]:
    validate(document)
    allowed = 1.0 - float(document["slo"]["availability_target"])
    results = []
    for raw in document["windows"]:
        window = Window(**raw)
        results.append({"name": window.name, "minutes": window.minutes, "availability": round(1-window.bad_events/window.valid_events, 6), "latency_success": round(1-window.slow_events/window.valid_events, 6), "burn_rate": round((window.bad_events/window.valid_events)/allowed, 3)})
    values = {item["name"]: item["burn_rate"] for item in results}
    fast = values.get("5m", 0) >= 14.4 and values.get("1h", 0) >= 14.4
    slow = values.get("30m", 0) >= 3 and values.get("6h", 0) >= 3
    decision = "critical-page" if fast else "ticket" if slow else "no-page"
    return {"scenario": document["name"], "service": document["service"], "windows": results, "decision": decision, "expected_decision": document["expected_decision"], "decision_matches": decision == document["expected_decision"]}

