# Security, Cost, and Production Readiness

- Redact secrets, authorization headers, payment data, and unnecessary identifiers near the source.
- Encrypt transport/storage; authenticate producers, queries, and administrators separately.
- Bound metric labels and log fields; alert on cardinality and ingestion growth.
- Use short raw retention, longer aggregates, and durable SLO/security evidence.
- Register owner, tier, dependencies, SLO, dashboard, and runbook.
- Test fast/slow alerts, stale data, collector loss, notification failure, and rollback correlation.
- Run collectors and alert paths redundantly with capacity, RTO, RPO, and backup evidence.
- Every page must describe impact, evidence, owner, and immediate action.

