---
title: "AI features and model routing"
visible: true
slug: "ai-features-and-model-routing"
---

Some UiPath services use AI-powered capabilities delivered through third-party large language models (LLMs), including the GPT family (via Azure OpenAI Service), Gemini models (via Google Vertex AI), and Claude models (via Amazon Bedrock).

These models are hosted in specific regions. When an LLM endpoint is not available in the same region as your UiPath organization or tenant, data is temporarily routed to a region with an available model endpoint.

UiPath does not control the geographic availability of third-party LLMs. However, once a third-party provider makes a new model region available, UiPath investigates and works toward supporting that region for its AI-powered features, while continuing to define only the routing behavior.

## How data is processed

When you use an AI feature, the data path depends on three separate regions:

| Region types | Description | Who controls it |
| --- | --- | --- |
| Organization region | The region where your UiPath organization is provisioned.  The organization region is considered for services enabled at the organizational level, that inherit the organization region (for example, Apps, Automation Ops, and Studio Web). | You choose the organization region when you create the organization.  An organization region is not visible in the UI. |
| Tenant region | The region where a tenant-level service (for example, Orchestrator, Test Manager, or Agents) is hosted and processes data. | You choose the tenant region when you create the tenant.  A tenant’s region is visible in the UI, from the tenant dropdown. |
| LLM processing region | The region where the third-party model actually runs. | Determined by the third-party LLM provider, which defines where an LLM endpoint is available. If an endpoint is not available in the organization or tenant region, UiPath may temporarily route the request to another supported region. When a new LLM region becomes available, UiPath evaluates and works toward supporting it, while continuing to define only the routing behavior. |

These regions can differ. While your UiPath data remains in your selected organization or tenant region, data used when working with AI features may be temporarily routed to another region for model processing if no local LLM endpoint exists.

## AI features residency

Check the following definitions to understand the residency scopes used when working with UiPath’s AI features:

* **Organization region**: The geographic region you select when creating your UiPath organization. This determines where your organization data is stored, including the data for services that inherit the organization region. Such services are marked as **Organization-level** in the **Global cloud regions** table.
* **Tenant region**: The region where a tenant is hosted and where its services (for example, Orchestrator, Test Manager, or Agents) operate. Services that inherit the tenant region are marked as **Tenant-level** in the **Global cloud regions** table.
* **Service region**: The region where a specific service within an organization or tenant runs. In most cases, all services in a tenant follow the tenant region, but some follow the organization region. The data residency of a service is marked in the **Global cloud regions** table as either inheriting the organization region or tenant region, along with its availability across cloud regions.
* **LLM model endpoint region**: The region where the third-party large language model (LLM) executes data processing. The availability of LLM regions is determined by the third-party provider (for example, Azure OpenAI, Google Gemini, or Anthropic Claude). UiPath defines routing rules only when a model is unavailable in the selected tenant or organization region.
* **Global deployment (LLM)**: A deployment type in which the model is not tied to any specific geographic endpoint. Requests are processed in a vendor-selected region based on availability, and there is no guaranteed LLM processing region. When strict data residency requirements are enforced, globally deployed models are not available.

## AI residency example

The following example shows how data is handled across regions when using UiPath services that include AI features. It highlights the different residency scopes involved, and explains how data is processed.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-2DFE1F31-60AE-46E7-BCD7-EAD7A4270BA6__TABLE_Q4Q_BBJ_MHC" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Scenario
   </th>
   <th>
    Description
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d19271e210">
    Organization region
   </td>
   <td headers="d19271e213">
    European Union (EU)
   </td>
  </tr>
  <tr>
   <td headers="d19271e210">
    Tenant region
   </td>
   <td headers="d19271e213">
    EU
   </td>
  </tr>
  <tr>
   <td headers="d19271e210">
    Services used
   </td>
   <td headers="d19271e213">
    <ul>
     <li>
      <p>
       Organization-level: Studio Web design-time experience
                                       (uses AI features powered by Azure OpenAI models)
      </p>
     </li>
     <li>
      <p>
       Tenant-level: Test Manager (uses AI features with
                                       Anthropic Claude as the selected model)
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d19271e210">
    Model availability
   </td>
   <td headers="d19271e213">
    <ul>
     <li>
      <p>
       Organization-level: Azure OpenAI model endpoint available
                                       in EU for Studio Web.
      </p>
     </li>
     <li>
      <p>
       Tenant-level: Anthropic Claude model endpoint available
                                       in EU for Test Manager.
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d19271e210">
    LLM processing region
   </td>
   <td headers="d19271e213">
    The LLM processing region is the same as the organization and
                              tenant region: EU. All data is hosted and processed in the same
                              region.
   </td>
  </tr>
 </tbody>
</table>
:::note
If the organization or tenant is located in a region where a third-party provider does not offer an LLM endpoint, the request is routed to a region where an endpoint is available. Once the model response is returned, all further data processing continues within the organization’s or tenant’s region.
:::

## Models consumed by Autopilot

Some UiPath services use AI models that are consumed through **Autopilot**, alongside other proprietary AI capabilities specific to those services. Because Autopilot capabilities are shared across multiple UiPath services, we document Autopilot-consumed models by Autopilot type to clearly indicate how models are used, reused, and routed.

Categorizing models by Autopilot type helps you understand which Autopilot capability consumes a given model and how the same model may be reused across multiple services.

The following Autopilot types are used when documenting model consumption:

* [Autopilot Chat](https://docs.uipath.com/autopilot/other/latest/user-guide/about-autopilot-chat): Represents the conversational interface that enables natural-language interaction with UiPath products. Models in this category power chat-based assistance, explanations, and guidance within supported services. Currently, Autopilot Chat is surfaced in the following services: Orchestrator, Studio, and Studio Web.
* [Autopilot for Developers](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-for-developers): Represents capabilities that help generate and refine automations or agents using prompt-based generation. Models in this category support developer-focused scenarios such as creating workflows, improving logic, and accelerating automation development. Currently, Autopilot for Developers is surfaced in the following services: Apps, Maestro, ScreenPlay, Studio, and Studio Web,
* [Autopilot for Testers](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-for-testers): Represents capabilities that accelerate the testing lifecycle using prompt-based generation. Models in this category support generating, refactoring, and analyzing test cases. With a single natural-language prompt, you can create or modify manual, low-code, or coded test cases directly within Studio, Studio Web, or Test Manager.

## Model routings by service

Each UiPath service that uses AI models defines its own routing rules. These rules apply only when an LLM endpoint is not available in the organization or tenant region, and not when a request to an available endpoint fails. If a call to an available endpoint fails, retry the action.

When routing is triggered, UiPath temporarily changes the LLM processing region to another region where the model is available. Only the model processing takes place in the routing region. After the model returns its response, all remaining data processing continues in the organization or tenant region.

The following tables list the routing behavior for each service when an LLM endpoint is not regionally available.

**Legend:**
* AU - Australia
* CA - Canada
* CH - Switzerland
* EU - European Union
* IN - India
* JA - Japan
* SI - Singapore
* UAE - United Arab Emirates
* UK - United Kingdom
* US - United States

## Agents (playground design time experience)

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic.claude-3-5-sonnet-20240620-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-5-sonnet-20241022-v2:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-7-sonnet-20250219-v1:0 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| anthropic.claude-haiku-4-5-20251001-v1:0 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-20250514-v1:0 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-6 | Stays in the region | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| claude-opus-4-5@20251101 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Stays in the region | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.5-flash | N/A | N/A | N/A | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |
| gemini-2.5-pro | N/A | N/A | N/A | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |
| gemini-3-flash-preview | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Stays in the region |
| gemini-3-pro-preview | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Stays in the region |
| gemini-3.1-pro-preview | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL |
| gpt-4.1-2025-04-14 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4.1-mini-2025-04-14 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-05-13 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region, as gpt-4o-2024-08-06 | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-08-06 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to US | Routed to EU | Stays in the region | Stays in the region |
| gpt-4o-2024-11-20-community-agents | Routed to EU | Routed to EU | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Routed to EU |
| gpt-4o-mini-2024-07-18 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5-2025-08-07 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5-mini-2025-08-07 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5.1-2025-11-13 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5.2-2025-12-11 | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Stays in the region |
| gpt-5.4 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Routed to US | N/A | Routed to EU | Stays in the region |
| text-embedding-3-large | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to US | Stays in the region | Stays in the region | Stays in the region |

## Agents (runtime and debug experience)

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic.claude-3-5-sonnet-20240620-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-7-sonnet-20250219-v1:0 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| anthropic.claude-haiku-4-5-20251001-v1:0 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-20250514-v1:0 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-6 | Stays in the region | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| claude-opus-4-5@20251101 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Stays in the region | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.5-flash | N/A | N/A | N/A | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |
| gemini-2.5-pro | N/A | N/A | N/A | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |
| gemini-3-flash-preview | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Stays in the region |
| gemini-3-pro-preview | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Stays in the region |
| gemini-3.1-pro-preview | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL | Routed to GLOBAL |
| gpt-4.1-2025-04-14 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4.1-mini-2025-04-14 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-05-13 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region, as gpt-4o-2024-08-06 | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-08-06 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to US | Routed to EU | Stays in the region | Stays in the region |
| gpt-4o-2024-11-20-community-agents | Routed to EU | Routed to EU | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Routed to EU |
| gpt-4o-mini-2024-07-18 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5-2025-08-07 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5-mini-2025-08-07 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5.1-2025-11-13 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5.2-2025-12-11 | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Routed to US | Stays in the region |
| gpt-5.4 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Routed to US | N/A | Routed to EU | Stays in the region |
| text-embedding-3-large | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to US | Stays in the region | Stays in the region | Stays in the region |

## Apps

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gemini-2.0-flash-001 | Routed to EU | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.5-flash | Routed to EU | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Routed to EU | Stays in the region | Stays in the region |
| gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-35-turbo-0125 | Routed to EU | Stays in the region | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | Routed to EU | Stays in the region, as gpt-35-turbo-0125 | Stays in the region |

## Autopilot Chat

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic.claude-haiku-4-5-20251001-v1:0 | Routed to EU | Routed to EU | N/A | Stays in the region | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to EU | Stays in the region |
| anthropic.claude-opus-4-5-20251101-v1:0 | Routed to EU | Routed to EU | N/A | Stays in the region | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to EU | Stays in the region |
| anthropic.claude-opus-4-6-v1 | Routed to EU | Routed to EU | N/A | Stays in the region | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to JA | Routed to JA | N/A | Stays in the region | Routed to JA | Stays in the region | Routed to JA | N/A | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-6 | Routed to JA | Routed to JA | N/A | Stays in the region | Routed to JA | Stays in the region | Routed to JA | N/A | Routed to EU | Stays in the region |
| gemini-2.0-flash-001 | Routed to EU | Routed to EU | N/A | Stays in the region | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to EU | Stays in the region |
| gemini-2.5-flash | Routed to JA | Routed to JA | Routed to EU | Stays in the region | Routed to JA | Stays in the region | Routed to JA | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.5-pro | Routed to JA | Routed to JA | Routed to EU | Stays in the region | Routed to JA | Stays in the region | Routed to JA | Routed to EU | Routed to EU | Stays in the region |
| gemini-3-flash-preview | Routed to US | Routed to US | N/A | Routed to US | Routed to US | Routed to US | Routed to US | N/A | Routed to US | Stays in the region |
| gemini-3-pro-preview | Routed to US | Routed to US | N/A | Routed to US | Routed to US | Routed to US | Routed to US | N/A | Routed to US | Stays in the region |
| gpt-4.1-2025-04-14 | Routed to EU | Routed to EU | N/A | Stays in the region | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to EU | Routed to EU |
| gpt-4.1-mini-2025-04-14 | Routed to EU | Routed to EU | N/A | Stays in the region | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-4o-2024-08-06 | Routed to JA | Routed to US | N/A | Stays in the region | Routed to JA | Stays in the region | Routed to JA | N/A | Routed to EU | Stays in the region |
| gpt-4o-mini-2024-07-18 | Routed to JA, as gpt-4o-2024-08-06 | Routed to US | N/A | Stays in the region | Routed to JA, as gpt-4o-2024-08-06 | Stays in the region, as gpt-4o-2024-08-06 | Routed to JA, as gpt-4o-2024-08-06 | N/A | Routed to EU | Routed to EU |
| gpt-5-2025-08-07 | Routed to EU | Routed to EU | N/A | Routed to US | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to US | Stays in the region |
| gpt-5-mini-2025-08-07 | Routed to EU | Routed to EU | N/A | Routed to US | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to US | Stays in the region |
| gpt-5-nano-2025-08-07 | Routed to EU | Routed to EU | N/A | Routed to US | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to US | Stays in the region |
| gpt-5.2-2025-12-11 | Routed to US | Routed to US | N/A | Routed to US | Routed to US | Routed to US | Routed to US | N/A | Routed to US | Stays in the region |

## Autopilot for Developers

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic.claude-3-7-sonnet-20250219-v1:0 | Routed to EU | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.0-flash-001 | Routed to EU | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.5-flash | Routed to EU | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.5-flash-lite | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Stays in the region, as gemini-2.5-flash | Routed to EU | N/A | Routed to EU | Stays in the region |
| gemini-2.5-pro | Routed to EU | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gpt-4.1-2025-04-14 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-4.1-mini-2025-04-14 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-4o-2024-08-06 | Routed to JA | Routed to US | Routed to EU | Stays in the region | Routed to JA | Stays in the region | Routed to JA | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-mini-2024-07-18 | Routed to JA, as gpt-4o-2024-08-06 | Routed to US | Routed to EU | Stays in the region | Routed to JA, as gpt-4o-2024-08-06 | Stays in the region, as gpt-4o-2024-08-06 | Routed to JA, as gpt-4o-2024-08-06 | Routed to EU | Routed to EU | Stays in the region |
| gpt-5-2025-08-07 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-5-mini-2025-08-07 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-5-nano-2025-08-07 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Routed to EU | N/A | Routed to EU | Stays in the region |

## Autopilot for Everyone

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic.claude-3-5-sonnet-20240620-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-5-sonnet-20241022-v2:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-7-sonnet-20250219-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-haiku-20240307-v1:0 | Stays in the region | Routed to US | Routed to EU | Stays in the region | Routed to US | N/A | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-20250514-v1:0 | N/A | N/A | Routed to EU | N/A | N/A | N/A | N/A | Routed to EU | N/A | N/A |
| anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region | Routed to US | N/A | Stays in the region | Routed to US | Stays in the region | Routed to US | N/A | Routed to EU | Stays in the region |
| gemini-2.0-flash-001 | N/A | Routed to US | Routed to EU | Stays in the region | Routed to US | N/A | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.5-flash | Stays in the region | Routed to US | N/A | Stays in the region | Routed to US | Stays in the region | Routed to US | N/A | Routed to EU | Stays in the region |
| gemini-2.5-flash-lite | N/A | Routed to US | N/A | Stays in the region | Routed to US | N/A | Routed to US | N/A | Routed to EU | Stays in the region |
| gpt-4.1-mini-2025-04-14 | Stays in the region | Routed to US | N/A | Stays in the region | Routed to EU | Stays in the region | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-4o-2024-05-13 | Routed to EU | Routed to EU | Routed to EU | Stays in the region | Routed to EU | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-08-06 | Routed to EU | Routed to EU | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Routed to EU | Stays in the region | Stays in the region |
| gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-4.1-mini-2025-04-14 | Routed to US, as gpt-4.1-mini-2025-04-14 | Routed to EU | Stays in the region, as gpt-4.1-mini-2025-04-14 | Routed to EU, as gpt-4.1-mini-2025-04-14 | Stays in the region, as gpt-4.1-mini-2025-04-14 | Routed to EU, as gpt-4.1-mini-2025-04-14 | Routed to EU | Routed to EU, as gpt-4.1-mini-2025-04-14 | Stays in the region, as gpt-4.1-mini-2025-04-14 |
| text-embedding-ada-002 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Stays in the region | Stays in the region |

## Autopilot for Testers

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic.claude-3-5-sonnet-20240620-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to JA, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-7-sonnet-20250219-v1:0 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.0-flash-001 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.5-flash | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gemini-2.5-pro | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-08-06 | Routed to JA | Routed to US | Routed to EU | Stays in the region | Routed to JA | Stays in the region | Routed to JA | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to JA | Routed to EU | Stays in the region | Stays in the region |
| gpt-4o-mini-2024-07-18 | Routed to JA, as gpt-4o-2024-08-06 | Routed to US | Routed to EU | Stays in the region | Routed to JA, as gpt-4o-2024-08-06 | Stays in the region, as gpt-4o-2024-08-06 | Routed to JA, as gpt-4o-2024-08-06 | Routed to EU | Routed to EU | Stays in the region |
| gpt-5.1-2025-11-13 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to EU | Routed to EU | Routed to EU | Stays in the region |

## Coded agents

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic.claude-3-5-sonnet-20240620-v1:0 | N/A | N/A | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | N/A | N/A | N/A | N/A | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | N/A | N/A |
| anthropic.claude-3-7-sonnet-20250219-v1:0 | N/A | N/A | Routed to EU | N/A | N/A | N/A | N/A | Routed to EU | N/A | N/A |
| anthropic.claude-haiku-4-5-20251001-v1:0 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Routed to US | N/A | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-20250514-v1:0 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Routed to US | N/A | Routed to EU | Stays in the region |
| anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region | Routed to US | N/A | Stays in the region | Routed to EU | Stays in the region | Routed to US | N/A | Routed to EU | Stays in the region |
| claude-opus-4-5@20251101 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Stays in the region | N/A | Routed to EU | Stays in the region |
| gemini-2.0-flash-001 | N/A | N/A | Routed to EU | N/A | N/A | N/A | N/A | Routed to EU | N/A | N/A |
| gemini-2.5-flash | Routed to EU | Routed to EU | N/A | Stays in the region | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to EU | Stays in the region |
| gemini-2.5-pro | Routed to EU | Routed to EU | N/A | Stays in the region | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to EU | Stays in the region |
| gemini-3-pro-preview | Routed to US | Routed to US | N/A | Routed to US | Routed to US | Routed to US | Routed to US | N/A | Routed to US | Stays in the region |
| gpt-4 | N/A | N/A | Stays in the region, as gpt-4o-2024-11-20 | N/A | N/A | N/A | N/A | Routed to EU, as gpt-4o-2024-11-20 | N/A | N/A |
| gpt-4.1-2025-04-14 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4.1-mini-2025-04-14 | Routed to US | Routed to US | N/A | Stays in the region | Stays in the region | Stays in the region | Routed to US | N/A | Routed to EU | Stays in the region |
| gpt-4o-2024-05-13 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Stays in the region, as gpt-4o-2024-08-06 | Routed to US | N/A | Routed to EU | Stays in the region |
| gpt-4o-2024-08-06 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to US | Routed to EU | Stays in the region | Stays in the region |
| gpt-4o-2024-11-20-community-agents | Routed to EU | Routed to EU | N/A | Stays in the region | Routed to EU | Routed to EU | Routed to EU | N/A | Routed to EU | Routed to EU |
| gpt-4o-mini-2024-07-18 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5-2025-08-07 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5-mini-2025-08-07 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5.1-2025-11-13 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Routed to US | N/A | Routed to EU | Stays in the region |
| gpt-5.2-2025-12-11 | Routed to US | Routed to US | N/A | Routed to US | Routed to US | Routed to US | Routed to US | N/A | Routed to US | Stays in the region |
| text-embedding-3-large | Stays in the region | Stays in the region | N/A | Stays in the region | Stays in the region | Stays in the region | Routed to US | N/A | Stays in the region | Stays in the region |
| text-embedding-ada-002 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Stays in the region | Stays in the region |

## Context grounding

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic.claude-3-5-sonnet-20240620-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-5-sonnet-20241022-v2:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-7-sonnet-20250219-v1:0 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to US | Routed to US | Routed to US | Routed to EU | Routed to US | Stays in the region |
| anthropic.claude-3-haiku-20240307-v1:0 | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Stays in the region | Routed to US | Routed to US | Routed to EU | Stays in the region | Stays in the region |
| gemini-1.5-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 |
| gemini-1.5-pro-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 |
| gemini-2.0-flash-001 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to EU | Routed to EU | Routed to US | Stays in the region |
| gemini-2.5-flash | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to EU | Routed to EU | Routed to US | Stays in the region |
| gemini-2.5-flash-lite | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to EU | Routed to EU | Routed to US | Stays in the region |
| gemini-2.5-pro | N/A | N/A | Routed to EU | Stays in the region | N/A | N/A | N/A | Routed to EU | N/A | Stays in the region |
| gemini-embedding-001 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Stays in the region |
| gemini-pro | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 |
| gpt-35-turbo-1106 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-35-turbo-0125 | Routed to EU, as gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU, as gpt-4o-mini-2024-07-18 | Routed to EU, as gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-4o-mini-2024-07-18 |
| gpt-4.1-2025-04-14 | N/A | N/A | Routed to EU | Stays in the region | N/A | N/A | N/A | Routed to EU | N/A | Stays in the region |
| gpt-4.1-mini-2025-04-14 | N/A | N/A | Routed to EU | Stays in the region | N/A | N/A | N/A | Routed to EU | N/A | Stays in the region |
| gpt-4o-2024-05-13 | Routed to EU | Routed to EU | Routed to EU | Stays in the region | Routed to EU | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-08-06 | Routed to EU | Routed to EU | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Routed to EU | Stays in the region | Stays in the region |
| gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-35-turbo-0125 | Routed to EU | Stays in the region | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | Routed to EU | Stays in the region, as gpt-35-turbo-0125 | Stays in the region |
| gpt-5-2025-08-07 | N/A | N/A | Routed to EU | Stays in the region | N/A | N/A | N/A | Routed to EU | N/A | Stays in the region |
| text-embedding-3-large | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Stays in the region | Stays in the region |
| text-embedding-ada-002 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Stays in the region | Stays in the region |

## Document Understanding

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gemini-2.0-flash-001 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gpt-4-32k | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Routed to EU, as gpt-4o-2024-11-20 | Routed to EU, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 |
| gpt-4o-2024-08-06 | Routed to EU | Routed to EU | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Routed to EU | Stays in the region | Stays in the region |
| gpt-5.1-2025-11-13 | N/A | N/A | N/A | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |
| text-embedding-3-large | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Stays in the region | Stays in the region |
| text-embedding-ada-002 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Stays in the region | Stays in the region |

## GenAI activities

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic.claude-3-5-sonnet-20240620-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-5-sonnet-20241022-v2:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-7-sonnet-20250219-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-3-haiku-20240307-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to EU, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Routed to US, as anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region, as anthropic.claude-sonnet-4-5-20250929-v1:0 |
| anthropic.claude-haiku-4-5-20251001-v1:0 | Routed to US | Routed to US | N/A | Stays in the region | Routed to US | Routed to US | Routed to US | N/A | Routed to US | Stays in the region |
| anthropic.claude-opus-4-20250514-v1:0 | N/A | N/A | Routed to EU | N/A | N/A | N/A | N/A | Routed to EU | N/A | N/A |
| anthropic.claude-sonnet-4-20250514-v1:0 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to US | Routed to US | Routed to US | Routed to EU | Routed to US | Stays in the region |
| anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region | Routed to US | Routed to EU | Stays in the region | Routed to US | Stays in the region | Routed to US | Routed to EU | Routed to US | Stays in the region |
| anthropic.claude-sonnet-4-6 | Stays in the region | Routed to US | N/A | Stays in the region | Routed to EU | Stays in the region | Routed to EU | N/A | Routed to EU | Stays in the region |
| claude-opus-4-5@20251101 | Routed to US | Routed to US | N/A | Stays in the region | Routed to EU | Routed to US | Stays in the region | N/A | Routed to EU | Stays in the region |
| gemini-1.0-pro | Stays in the region, as gemini-2.5-flash | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.5-flash | Stays in the region, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.5-flash | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 |
| gemini-1.0-pro-001 | Stays in the region, as gemini-2.5-flash | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.5-flash | Stays in the region, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.5-flash | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 |
| gemini-1.5-flash-001 | Stays in the region | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.5-flash | Stays in the region, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.5-flash | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 |
| gemini-1.5-pro-001 | Stays in the region | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.5-flash | Stays in the region, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.5-flash | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 |
| gemini-2.0-flash-001 | Stays in the region, as gemini-2.5-flash | Routed to EU | Routed to EU, as gemini-2.5-flash | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Routed to EU, as gemini-2.5-flash | Routed to EU | Stays in the region |
| gemini-2.5-flash | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Stays in the region | Stays in the region |
| gemini-2.5-pro | Routed to EU | Routed to EU | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| gemini-pro | Stays in the region, as gemini-2.5-flash | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.5-flash | Stays in the region, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.0-flash-001 | Routed to EU, as gemini-2.5-flash | Routed to EU, as gemini-2.0-flash-001 | Stays in the region, as gemini-2.0-flash-001 |
| gpt-35-turbo | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-35-turbo-0125 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU, as gpt-4o-mini-2024-07-18 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-4o-mini-2024-07-18 |
| gpt-35-turbo-0125 | Routed to CA | Stays in the region | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-mini-2024-07-18 | Stays in the region | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU, as gpt-4o-mini-2024-07-18 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region | Stays in the region, as gpt-4o-mini-2024-07-18 |
| gpt-35-turbo-1106 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-35-turbo-0125 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU, as gpt-4o-mini-2024-07-18 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-4o-mini-2024-07-18 |
| gpt-35-turbo-16k | N/A | N/A | N/A | Stays in the region, as gpt-5-mini-2025-08-07 | N/A | N/A | N/A | N/A | N/A | N/A |
| gpt-4 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Routed to EU, as gpt-4o-2024-11-20 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 |
| gpt-4-1106-Preview | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Routed to EU, as gpt-4o-2024-11-20 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 |
| gpt-4-32k | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Routed to EU, as gpt-4o-2024-11-20 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 |
| gpt-4.1-2025-04-14 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4.1-mini-2025-04-14 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-4.1-nano-2025-04-14 | N/A | N/A | Routed to EU | Stays in the region | N/A | N/A | N/A | Routed to EU | N/A | Stays in the region |
| gpt-4o-2024-05-13 | Routed to EU, as gpt-5.1-2025-11-13 | Routed to EU | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region | Routed to EU | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | Routed to EU, as gpt-5.1-2025-11-13 | Routed to EU | Stays in the region |
| gpt-4o-2024-08-06 | Routed to EU, as gpt-5.1-2025-11-13 | Routed to EU | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU, as gpt-5.1-2025-11-13 | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region | Stays in the region, as gpt-5.1-2025-11-13 | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region | Stays in the region |
| gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-35-turbo-0125 | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | Routed to EU, as gpt-5.1-2025-11-13 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region |
| gpt-5-2025-08-07 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5-mini-2025-08-07 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5-nano-2025-08-07 | N/A | N/A | Routed to EU | Stays in the region | N/A | N/A | N/A | Routed to EU | N/A | Stays in the region |
| gpt-5.1-2025-11-13 | Routed to US | Routed to US | Routed to EU | Stays in the region | Routed to EU | Routed to US | Routed to US | Routed to EU | Routed to EU | Stays in the region |
| gpt-5.2-2025-12-11 | Routed to US | Routed to US | N/A | Routed to US | Routed to US | Routed to US | Routed to US | N/A | Routed to US | Stays in the region |

## Healing Agent

| Model | CH | EU | JA | US |
| --- | --- | --- | --- | --- |
| gemini-2.5-flash | Routed to EU | Stays in the region | Stays in the region | Stays in the region |
| gpt-4o-2024-08-06 | Routed to EU | Stays in the region | Stays in the region | Stays in the region |

## IXP
:::note
IXP - Unstructured and complex documents and IXP - Communications Mining use the same routing.
:::

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gemini-2.0-flash-001 | N/A | N/A | Routed to EU | Stays in the region | Routed to EU | N/A | Routed to EU | N/A | Routed to EU | Stays in the region |
| gemini-2.5-flash | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | N/A | Routed to EU | Stays in the region |
| gemini-2.5-pro | N/A | N/A | Routed to EU | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |
| gpt-35-turbo | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Routed to EU, as gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-4o-mini-2024-07-18 | Routed to EU, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU, as gpt-4o-2024-11-20 | N/A | Routed to EU, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-mini-2024-07-18 |
| gpt-4-1106-Preview | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Routed to EU, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Routed to EU, as gpt-4o-2024-11-20 | N/A | Routed to EU, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 |
| gpt-4.1-2025-04-14 | N/A | N/A | N/A | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |
| gpt-4o-2024-05-13 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Routed to EU | Stays in the region | Routed to EU | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-4o-2024-08-06 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-4o-2024-11-20 | Stays in the region, as gpt-4o-2024-11-20 | Routed to EU | Stays in the region | Routed to EU | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-5-2025-08-07 | N/A | N/A | N/A | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |
| gpt-5-mini-2025-08-07 | N/A | N/A | N/A | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |
| gpt-5-nano-2025-08-07 | N/A | N/A | N/A | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |
| gpt-5.1-2025-11-13 | N/A | N/A | N/A | Stays in the region | N/A | N/A | N/A | N/A | N/A | Stays in the region |

## Process Mining

| Model | AU | CA | CH | EU | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-4.1-mini-2025-04-14 | Stays in the region | Routed to EU | N/A | Stays in the region | Stays in the region | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-4o-2024-05-13 | Routed to EU | Routed to EU | N/A | Stays in the region | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | N/A | Stays in the region | Stays in the region | Routed to EU | N/A | Stays in the region | Stays in the region |
| gpt-4o-mini-2024-07-18 | Stays in the region, as gpt-35-turbo-0125 | Stays in the region, as gpt-35-turbo-0125 | N/A | Stays in the region | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | N/A | Stays in the region, as gpt-35-turbo-0125 | Stays in the region |

## ScreenPlay

| Model | EU | JA | US |
| --- | --- | --- | --- |
| anthropic.claude-3-7-sonnet-20250219-v1:0 | Stays in the region | Routed to US | Stays in the region |
| anthropic.claude-3-haiku-20240307-v1:0 | Stays in the region | Routed to US | Stays in the region |
| anthropic.claude-haiku-4-5-20251001-v1:0 | Stays in the region | Routed to US | Stays in the region |
| anthropic.claude-sonnet-4-20250514-v1:0 | Stays in the region | Routed to US | Stays in the region |
| anthropic.claude-sonnet-4-5-20250929-v1:0 | Stays in the region | Routed to US | Stays in the region |
| computer-use-preview-2025-03-11 | Stays in the region | Routed to EU | Routed to EU |
| gemini-2.0-flash-001 | Stays in the region, as gemini-2.5-flash | Routed to US, as gemini-2.5-flash | Stays in the region, as gemini-2.5-flash |
| gemini-2.5-flash | Stays in the region | Stays in the region | Stays in the region |
| gpt-4.1-2025-04-14 | Stays in the region | Routed to US | Stays in the region |
| gpt-4.1-mini-2025-04-14 | Stays in the region | Routed to US | Stays in the region |
| gpt-4o-2024-08-06 | Stays in the region | Stays in the region | Stays in the region |
| gpt-4o-mini-2024-07-18 | Stays in the region | Routed to US | Stays in the region |
| gpt-5-2025-08-07 | Stays in the region | Routed to US | Stays in the region |
| gpt-5-mini-2025-08-07 | Stays in the region | Routed to US | Stays in the region |
| gpt-5-nano-2025-08-07 | Stays in the region | Routed to US | Stays in the region |

## Studio Web

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-4o-2024-08-06 | Routed to EU | Routed to EU | Routed to EU | Stays in the region | Routed to EU | Stays in the region | Routed to EU | Routed to EU | Routed to EU | Stays in the region |
| text-embedding-ada-002 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | Stays in the region | Stays in the region | Stays in the region |

## Task Mining

| Model | AU | CA | CH | EU | IN | JA | SI | UAE | UK | US |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-4o-2024-05-13 | Routed to EU | Routed to EU | Routed to EU | Stays in the region | Routed to EU | Stays in the region, as gpt-4o-2024-08-06 | Routed to EU | N/A | Routed to EU | Stays in the region |
| gpt-4o-2024-11-20 | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Stays in the region | Routed to EU | N/A | Stays in the region | Stays in the region |