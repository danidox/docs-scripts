---
title: "Configuring OpenTelemetry"
visible: true
slug: "configuring-opentelemetry"
---

The **OpenTelemetry** tab in the AI Trust Layer allows administrators to configure export of [agent traces](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-traces) to an external OTEL-compatible observability platform.
:::note
This feature is currently available in preview.
:::

## Prerequisites

* An OpenTelemetry HTTP endpoint
* API key or required authentication headers
* Publicly accessible endpoint

## Adding an OpenTelemetry configuration

1. Navigate to **Administration > AI Trust Layer**.
2. Select the **OpenTelemetry (Preview)** tab.
3. Select the target tenant.
4. Select **Add** to open the **Add OpenTelemetry Configuration** panel.
5. In the configuration panel:
   * Select a **Vendor** from the dropdown (for example, OpenTelemetry Collector).
   * Enter the **API Key** (if required by the selected vendor).
   * Enter the **Endpoint URL** (for example: `https://your-otlp-endpoint.com`).
6. (Optional) Add **Custom Headers**:
   * Select **Add Header**.
   * Enter the **Header Name** and **Header Value**. Use this for vendor-specific requirements (for example, routing headers, authorization tokens). Remove a header using the delete icon if needed.
7. Select **Save** to create the configuration.

Once saved, agent and LLM execution traces are exported in near real time to the configured endpoint.

## What data is exported

Each agent execution generates OTEL spans containing:

* Trace and span identifiers
* Timestamps
* Execution status
* Prompts and completions
* Token usage
* Tool calls
* Guardrail evaluations
* UiPath metadata under `attributes.uipath.*`

Attributes are flattened into OTEL format using dot notation.

## Limitations

* 32 KB per attribute value
* 256 KB per span (total attributes)
* ~1 MB per OTLP batch
* File attachments exported as metadata only
* Vendor-specific schema or header requirements may apply