---
title: "Configuring LLMs"
visible: true
slug: "configuring-llms"
---

:::note
**LLM configurations** is available on the following licensing plans:
* Unified Pricing: Enterprise Platform,
Standard Platform, Basic Platform, App Test Platform Enterprise, App Test Platform Standard.
* Flex: Advanced Platform, Flex
Standard Platform.
:::

The **LLM configurations** tab allows you to integrate your existing AI subscriptions while maintaining the governance framework provided by UiPath. You can:

* Replace UiPath LLM subscription: Replace UiPath-managed subscriptions with your own, provided they match the same model family and version already supported by the UiPath product. This allows for seamless swapping of UiPath-managed models with your subscribed models.
* Add your own LLM: Use any LLM that meets the product's compatibility criteria. To ensure smooth integration, your chosen LLM must pass a series of tests initiated through a probe call before it can be used within the UiPath ecosystem.

Configuring LLMs preserves most of the governance benefits of the AI Trust Layer, including policy enforcement via Automation Ops and detailed audit logs. However, model governance policies are specifically designed for UiPath-managed LLMs. This means that if you disable a particular model through an AI Trust Layer policy, the restriction only applies to the UiPath-managed version of that model. Your own configured models of the same type remain unaffected.

When leveraging the option to use your own LLM or subscription, keep the following points in mind:

* Compatibility requirements: Your chosen LLM or subscription must align with the model family and version currently supported by the UiPath product.
* Setup: Make sure you properly configure and maintain all required LLMs in the custom setup. If any component is missing, outdated, or incorrectly configured, your custom setup may cease to function. In such cases, the system will automatically revert to a UiPath-managed LLM to ensure continuity of service, unless UiPath LLMs are turned off through an Automation Ops policy.
* Cost-saving: If your custom LLM setup is complete, correct, and meets all necessary requirements, you may be eligible for a Reduced Consumption Rate.

## Setting up an LLM connection

LLM connections rely on Integration Service to establish the connection to your own models. You can create connections to the following providers:

* Azure Open AI
* Open AI
* Amazon Bedrock
* Google Vertex
* Open AI V1 Compliant LLM – Use this option to connect to any LLM provider whose API follows the OpenAI V1 standard. For details, refer to the [OpenAI V1 Compliant LLM connector documentation](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/uipath-openai-openaiv1compliant).

To set up a new connection, follow these steps:

1. Create a connection in Integration Service to your provider of choice. For connector-specific authentication details, see the [Integration Service user guide](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/introduction).
   :::note
   To prevent unauthorized access, create the Integration Service connection in a private, non-shared folder.
   :::
2. Navigate to **Admin** > **AI Trust Layer** > **LLM Configurations**.
3. Select the tenant and folder where you want to configure the connection.
4. Select **Add configuration**.
5. Select the **Product** and **Feature**.
6. Choose how you want to configure:
   * **Replace UiPath LLM subscription** – Use your own connection instead of a UiPath-managed one.
   * **Add your own LLM** – Add an additional LLM configuration managed entirely by you.
     :::note
     When configuring your own LLM, you can optionally restrict which large language models are available for use in your organization. If you want to ensure that **only your custom models** are used, you can disable UiPath-managed third-party models by applying an **AI Trust Layer policy**. Check the [Models](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-ai-trust-layer-policies#models) section in the AI Trust Layer policies documentation.
     :::

Depending on the selected product, only one option may be available.
7. Set up the connection for **Replace UiPath LLM subscription**:
   1. **Folder** – Select the folder where the configuration will be stored.
   2. **Replaceable LLM** – From the dropdown, select the UiPath LLM you want to replace.
   3. **Connector** – Select your connector (e.g., Microsoft Azure OpenAI).
   4. **Connection** – Choose your Integration Service connection. If none are available, select **Add new connection** to be redirected to Integration Service.
   5. **LLM identifier** – Enter the identifier for your model.
      * For Azure-hosted models, enter the model identifier.
      * For AWS Bedrock cross-region inference, enter the inference profile ID instead of the model ID.
8. Set up the connection for **Add your own LLM**:
   1. **Folder** – Select the folder where the configuration will be stored.
   2. **Displayed (LLM) name** – Provide an alias for your LLM.
   3. **Connector** – Select your connector (e.g., Microsoft Azure OpenAI).
   4. **Connection** – Choose your Integration Service connection.
   5. **LLM identifier** – Enter the identifier for your model.
      * For Azure-hosted models, enter the model identifier.
      * For AWS Bedrock cross-region inference, enter the inference profile ID instead of the model ID.
9. Select **Test configuration** to check that the model is reachable and meets the required criteria.

UiPath can confirm reachability, verifying the exact model used is your responsibility.
10. If the test is successful, select **Save** to activate the connection.

## Managing existing LLM connections

You can perform the following actions on your existing connections:

* **Check status** – Verify the status of your Integration Service connection. This action ensures that the connection is active and functioning correctly.
* **Edit** – Modify any parameters of your existing connection.
* **Disable** – Temporarily suspend the connection. When disabled, the connection remains visible in your list but doesn't route any calls. You can re-enable the connection when needed.
* **Delete** – Permanently remove the connection from your system. This action disables the connection and removes it from your list.

## Configuring LLMs for your product

Each product supports specific large language models (LLMs) and versions. Use the table below to identify the supported models and versions for your product.

You can connect your own LLM using one of the following providers: Amazon Web Services, Google Vertex, Microsoft Azure OpenAI, or OpenAI V1 Compliant. Follow the steps outlined in the previous section to create a connection.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" data-condition="(Deployment=Cloud)" id="GUID-36483BEF-15CB-43B6-A7B1-5BB3B60E05E2__TABLE_MHP_VCP_VGC" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Product
   </th>
   <th>
    Feature
   </th>
   <th>
    LLM
   </th>
   <th>
    Version
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d130399e432" rowspan="2">
    Agents
    <sup>
     1
    </sup>
   </td>
   <td headers="d130399e434" rowspan="2">
    Design, Evaluate &amp; Deploy
   </td>
   <td headers="d130399e436">
    Anthropic
   </td>
   <td headers="d130399e438">
    <p>
     anthropic.claude-3.5-sonnet-20240620-v1:0
    </p>
    <p>
     anthropic.claude-3.5-sonnet-20241022-v2:0
    </p>
    <p>
     anthropic.claude-3.7-sonnet-20250219-v1:0
    </p>
    <p>
     anthropic.claude-3-haiku-20240307-v1:0
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d130399e436">
    OpenAI
   </td>
   <td headers="d130399e438">
    <p>
     gpt-4o-2024-05-13
    </p>
    <p>
     gpt-4o-2024-08-06
    </p>
    <p>
     gpt-4o-2024-11-20
    </p>
    <p>
     gpt-4o-mini-2025-04-14
    </p>
    <p>
     gpt-4o-mini-2024-07-18
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d130399e432" rowspan="12">
    Autopilot
   </td>
   <td headers="d130399e434" rowspan="4">
    Generation
   </td>
   <td headers="d130399e436" rowspan="4">
    Google
   </td>
   <td headers="d130399e438">
    gemini-2.5-flash
   </td>
  </tr>
  <tr>
   <td headers="d130399e438">
    gemini-2.5-flash-lite
   </td>
  </tr>
  <tr>
   <td headers="d130399e438">
    gemini-2.5-pro
   </td>
  </tr>
  <tr>
   <td headers="d130399e438">
    gemini-embedding-001
   </td>
  </tr>
  <tr>
   <td headers="d130399e434" rowspan="8">
    Chat
   </td>
   <td headers="d130399e436" rowspan="3">
    Anthropic
   </td>
   <td headers="d130399e438">
    anthropic.claude-haiku-4-5-20251001-v1:0
   </td>
  </tr>
  <tr>
   <td headers="d130399e438">
    anthropic.claude-sonnet-4-6
   </td>
  </tr>
  <tr>
   <td headers="d130399e438">
    anthropic.claude-opus-4-6-v1
   </td>
  </tr>
  <tr>
   <td headers="d130399e436" rowspan="5">
    Google
   </td>
   <td headers="d130399e438">
    gemini-2.5-pro
   </td>
  </tr>
  <tr>
   <td headers="d130399e438">
    gemini-2.5-flash
   </td>
  </tr>
  <tr>
   <td headers="d130399e438">
    gemini-3-flash-preview
   </td>
  </tr>
  <tr>
   <td headers="d130399e438">
    gemini-3-pro-preview
   </td>
  </tr>
  <tr>
   <td headers="d130399e438">
    gemini-3.1-pro-preview
   </td>
  </tr>
  <tr>
   <td headers="d130399e432" rowspan="2">
    Autopilot for everyone
   </td>
   <td headers="d130399e434" rowspan="2">
    Chat
   </td>
   <td headers="d130399e436">
    Anthropic
   </td>
   <td headers="d130399e438">
    <p>
     anthropic.claude-3.5-sonnet-20240620-v1:0
    </p>
    <p>
     anthropic.claude-3.7-sonnet-20250219-v1:0
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d130399e436">
    OpenAI
   </td>
   <td headers="d130399e438">
    gpt-4o-mini-2024-07-18
   </td>
  </tr>
  <tr>
   <td headers="d130399e432" rowspan="3">
    GenAI Activities
   </td>
   <td headers="d130399e434" rowspan="3">
    Build, Test &amp; Deploy
   </td>
   <td headers="d130399e436">
    Anthropic
   </td>
   <td headers="d130399e438">
    <p>
     anthropic.claude-3-5-sonnet-20240620-v1:0
    </p>
    <p>
     anthropic.claude-3-5-sonnet-20241022-v2:0
    </p>
    <p>
     anthropic.claude-3-7-sonnet-20250219-v1:0
    </p>
    <p>
     anthropic.claude-sonnet-4-20250514-v1:0
    </p>
    <p>
     anthropic.claude-sonnet-4-5-20250929-v1:0
    </p>
    <p>
     anthropic.claude-haiku-4-5-20251001-v1:0
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d130399e436">
    Google
   </td>
   <td headers="d130399e438">
    <p>
     gemini-2.0-flash-001
    </p>
    <p>
     gemini-2.5-pro
    </p>
    <p>
     gemini-2.5-flash
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d130399e436">
    OpenAI
   </td>
   <td headers="d130399e438">
    <p>
     gpt-5-2025-08-07
    </p>
    <p>
     gpt-5-mini-2025-08-07
    </p>
    <p>
     gpt-5-nano-2025-08-07
    </p>
    <p>
     gpt-5.1-2025-11-13
    </p>
    <p>
     gpt-4o-2024-11-20
    </p>
    <p>
     gpt-4o-mini-2024-07-18
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d130399e432" rowspan="2">
    Healing Agent
   </td>
   <td headers="d130399e434" rowspan="2">
    Workflow Recovery
   </td>
   <td headers="d130399e436">
    Google
   </td>
   <td headers="d130399e438">
    gemini-2.5-flash
   </td>
  </tr>
  <tr>
   <td headers="d130399e436">
    OpenAI
   </td>
   <td headers="d130399e438">
    gpt-4o-2024-08-06
   </td>
  </tr>
  <tr>
   <td headers="d130399e432" rowspan="3">
    UI Automation
   </td>
   <td headers="d130399e434" rowspan="3">
    ScreenPlay
   </td>
   <td headers="d130399e436">
    Anthropic
   </td>
   <td headers="d130399e438">
    anthropic.claude-sonnet-4-5-20250929-v1:0
   </td>
  </tr>
  <tr>
   <td headers="d130399e436">
    Google
   </td>
   <td headers="d130399e438">
    gemini-2.5-flash
   </td>
  </tr>
  <tr>
   <td headers="d130399e436">
    OpenAI
   </td>
   <td headers="d130399e438">
    <p>
     gpt-4.1-mini-2025-04-14
    </p>
    <p>
     gpt-4.1-2025-04-14
    </p>
    <p>
     gpt-5-2025-08-07
    </p>
    <p>
     gpt-5-mini-2025-08-07
    </p>
    <p>
     computer-use-preview-2025-03-11
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d130399e432" rowspan="3">
    Test Manager
   </td>
   <td headers="d130399e434" rowspan="3">
    Autopilot
    <ul>
     <li>
      Autopilot Search
     </li>
     <li>
      Find Obsolete Tests
     </li>
     <li>
      Generate Test Cases
     </li>
     <li>
      Import Test Cases
     </li>
     <li>
      Generate Reports
     </li>
     <li>
      Requirement Evaluation
     </li>
    </ul>
   </td>
   <td headers="d130399e436">
    Anthropic
   </td>
   <td headers="d130399e438">
    anthropic.claude-3.7-sonnet-20250219-v1:0 (to be replaced with anthropic.claude-4.5-sonnet in March 2026)
   </td>
  </tr>
  <tr>
   <td headers="d130399e436">
    Google
   </td>
   <td headers="d130399e438">
    <p>
     gemini-2.5-pro
    </p>
    <p>
     gemini-2.5-flash
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d130399e436">
    OpenAI
   </td>
   <td headers="d130399e438">
    gpt-4o-2024-11-20
   </td>
  </tr>
 </tbody>
</table>

<sup>1</sup> When configuring your model deployment for agents, ensure that your LLM supports the following capabilities:

* **Tool (function) calling** – Your model must be able to call tools or functions during execution.
* **Disabling parallel tool calls** – If supported by your LLM provider, the model should offer the option to disable parallel tool calls.
  :::note
  When using custom models, the system cannot determine the model’s true token capacity. Agents default to a 4096 token limit, even if the underlying model supports a higher value. This behavior is intentional, as UiPath cannot infer token limits for customer-defined deployments.
  :::