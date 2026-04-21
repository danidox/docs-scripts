---
title: "Managing indexes"
visible: true
slug: "managing-indexes"
---

The **Indexes** page displays your currently configured indexes and enables you to create new indexes in shared folders that you have permissions to.

For each listed index, you can view its name, data source, description, ingestion status, when it was last synced, and when it was last queried. Use the refresh icon to retrieve the latest information.

For any listed index, select the context menu to:

* **Edit** the index, to update the index description. Once you create an index, you cannot change the ingestion technique, but you can specify which data formats to ingest in that specific job.
* **Sync** the index with the data source, to ingest the latest data.
* **Monitor** the index. This option redirects you to the tenant-level **Monitoring Indexes** page to view specific index details, such as the number of queries and sync history. For details, see [Indexes](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/monitoring-indexes).
* **Delete** the index. This action can break existing processes for indexes used in agents, GenAI activities, or Autopilot.

## Index health

The **Index health** helps you monitor the condition of your Context Grounding indexes and identify those that may need maintenance or cleanup. It provides an automated, objective score showing how well each index performs and how frequently it’s used.

Each index receives a health score based on two criteria:

* Ingestion reliability – How successfully documents were processed during the latest ingestion run.
* Utilization – How recently the index has been queried.

The combined score helps you determine whether an index is healthy and delivering value (overall score above 75%), or degraded (overall score 75% or below). The score updates automatically after each successful ingestion or query.

Index health is recalculated every 15 minutes for all tenants and only applies to indexes with completed ingestion jobs. New indexes have a 24-hour grace period after creation before health scoring begins.

The following table describes how each health criterion is calculated and weighted to determine the overall index health score.

| Criterion | Metric | Formula | Notes |
| --- | --- | --- | --- |
| Ingestion reliability | Success rate from last ingestion | 100 × (1 - failed_docs / total_docs) | Skipped and deleted documents are excluded. If no ingestion is completed within 24h, score = 0. |
| Utilization | Days since last query (max 90 days) | 100 × (1 - days_since_last_query / 90) | After 24h without any query, score = 0. |
| Overall health | Average of both metrics | (Ingestion Reliability + Utilization) | Calculated only if both component scores exist. |