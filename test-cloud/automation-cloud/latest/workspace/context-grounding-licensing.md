---
title: "Context Grounding licensing"
visible: true
slug: "context-grounding-licensing"
---

This page provides details on how Context Grounding requests are quantified through licensing units.

## Unified Pricing
:::note
The licensing information in this section applies to you if you are on Unified Pricing. For details, refer to [Licensing plan framework](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/unified-pricing-licensing-plan-framework).
:::

Context Grounding consumes Platform Units for each request (search, summarization, or RAG operations) as it is executed through GenAI Activities. The consumption of Platform Units occurs in the following way:

* **Basic search and retrieval is free**. This includes any time the index is accessed by a GenAI activity or an agent.
* **Basic ingestion is free**. Applies to digital text input only (excluding images and tables). Limited to 1.5 million tokens input tokens in a single index (approximately 1,000 pages in a single index).
* Advanced ingestion is charged at 0.4 Platform Units per 15,000 tokens of input (or 10 pages). Applies to multi-modal documents such as scans, tables, or images; large documents typically containing around 1.5 million tokens or more than 1,000 pages; or extensive unstructured text, like JSON files exceeding 6 million characters.
* DeepRAG queries are charged at 0.2 Platform Units per 30,000 tokens of input, equivalent to ~20 pages. This enables synthesized insights across documents.

Context Grounding requests made from Autopilot or Agents consume licensing units based on the host product:

* In Autopilot for Everyone, each action—whether or not it includes a Context Grounding query—consumes 1 Autopilot action.
* In Agents, executions consume Platform Units.
:::note
For DeepRAG, Platform Unit consumption may scale with input size (e.g., per 30K tokens or ~20 pages), though detailed per-unit pricing may vary depending on the surface.
:::

## Flex Licensing
:::note
The licensing information in this section applies to you if you are on the Flex plan. For details, refer to [Flex licensing plan framework](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/flex-licensing-plan-framework).
:::

Context Grounding consumes AI units for each request (search, summarization, or RAG operations) as it is executed through GenAI Activities. The consumption of AI units occurs in the following way:

* **Basic search and retrieval is free**. This includes any time the index is accessed by a GenAI activity or an agent.
* **Basic ingestion is free**. Applies to digital text input only (excluding images and tables).
* Advanced ingestion is charged at 2 AI Units per 15,000 tokens of input (or 10 pages). Applies to multi-modal documents such as scans, tables, or images; large documents typically containing around 1.5 million tokens or more than 1,000 pages; or extensive unstructured text, like JSON files exceeding 6 million characters.
* DeepRAG queries are charged at 1 AI Unit per 30,000 tokens of input, equivalent to ~20 pages. This enables synthesized insights across documents.

Context Grounding requests made from Autopilot or Agents consume licensing units based on the host product:

* In Autopilot for Everyone, each activity—whether or not it includes a Context Grounding query—consumes 1 Autopilot action.
* In Agents, executions consume AI units.

## Entitlements

**Community** users are subject to the following quotas:
* Index allocation: 10 indexes per tenant.
* Data ingestion: Daily limits based on the number of ingested pages.
* Query allowance: Up to 100 **free** queries per day, after which consumption starts.

Trial and Enterprise tenants receive:

* Index allocation: 10 indexes per tenant.
* Query allowance: Up to 100 **free** queries per day, after which consumption starts.
* DeepRAG: 2 **free** queries per day (equivalent to 50 basic searches per call), after which consumption starts.
:::note
Advanced ingestion is not available for Community and Trial accounts.
:::