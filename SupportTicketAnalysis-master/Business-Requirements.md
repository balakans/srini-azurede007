
# Business Requirements Document (BRD)
## Project: Support Ticket Analytics (ISP)
**Prepared:** 2025-12-01
**Owner:** IT/Ticketing Analytics Team

### 1. Background
Internet Service Provider (ISP) handles support tickets via multiple channels (phone, web, chat). Stakeholders require near real-time analytics to monitor operational KPIs and agent/team performance.

### 2. Objectives
- Ingest incremental ticket data from MySQL into Databricks.
- Cleanse, enrich, and derive fields to standardize analytics.
- Produce aggregated KPIs and write them back to MySQL for downstream dashboards.
- Maintain offsets for incremental processing and ensure idempotency.

### 3. Scope
**In scope**
- Data ingestion from MySQL `tickets` table (incremental).
- Metrics:
  - Total Tickets Created
  - Tickets by Channel
  - Tickets by Category
  - Tickets by Sub-Category
  - Tickets by Device/Plan Type
  - Tickets Resolved per Agent
  - Tickets Open per Agent
  - Resolution Time by Agent/Team (avg, p95)
  - Top/Bottom Performing Agents
- Write aggregated metrics into MySQL table `ticket_metrics_agg`.

### 4. Data Model & Assumptions
- Source `tickets` table contains at least:
  - ticket_id, created_at, updated_at, resolved_at, status, channel, category, sub_category, device, assigned_agent, team, priority
- Timestamps are stored in a consistent timezone or include timezone info.
- Offsets are tracked in `etl_offsets` table: (source_table, column_name, last_value, updated_at).
- The MySQL user has permission to read source tables and write target tables.

### 5. Scheduling & SLAs
- Recommended schedule: run every 5–15 minutes via Databricks Jobs.
- Failure SLA: notify on-failure via alerting (email/ops) and retry policy.

### 6. Acceptance Criteria
- ETL job runs without errors and writes metrics for each execution.
- Offsets updated correctly to avoid reprocessing duplicates.
- Metrics validated against sample manual queries.
