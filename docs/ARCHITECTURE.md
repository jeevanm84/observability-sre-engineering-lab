# Architecture

Applications emit bounded vendor-neutral telemetry to redundant collectors, which redact, batch, sample, and route metrics, logs, and traces. Recording rules calculate stable SLIs; alert evaluation remains independent from dashboards. Scale by event rate, bytes, active series, query concurrency, and retention. Preserve Git configuration, SLO history, and critical incident evidence for recovery. Missing telemetry is a fault, never proof of health.

