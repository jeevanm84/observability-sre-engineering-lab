# Checkout SLO Burn Runbook

Incident → Symptoms → Investigation → Metrics → Logs → Commands → Root Cause → Immediate Mitigation → Permanent Fix → Prevention.

Confirm traffic and data freshness; establish impact by operation/region; overlay release events; compare dependency errors, traces, saturation, and retry amplification. Run `./scripts/evaluate.py --scenario scenarios/fast-burn.json`. Pause rollout, restore a known-good release, reduce traffic, or isolate the dependency. Verify SLO recovery, document the causal chain, then assign prevention actions with owners and dates.

