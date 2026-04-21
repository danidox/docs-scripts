---
title: "Configuring an LLM for Autopilot"
visible: true
slug: "configuring-an-llm-for-autopilot"
---

The AI Trust Layer card in the **Admin** section of your organization allows you to configure your own subscription for the models Autopilot supports.

To configure your own LLM, you need a connection to the following AI providers, depending on the model you want to incorporate:

* Amazon Bedrock or Amazon Web Services, for Anthropic models
* Google Vertex, for Gemini models.
  :::important
  To set up a Gemini model, you need to reach out to your designated UiPath technical account manager.
  :::

When you select Autopilot as the product for which you want to configure your own LLM, you must select the feature which will use that model:

## Generation

Configure your own LLM for generating automations, expressions, or apps in your Studio projects. You need to override all the default models with your own:

1. Go to your **Admin > AI Trust Layer** section of your organization.
2. In the **LLM configurations** tab, select the tenant where you want to configure your LLM.
3. Select **Add configuration** and provide the following properties:
   1. **Product** - select **Autopilot**
   2. **Feature** - select **Generation**
4. Provide the **Connections Folder**.
5. For every default **LLM Name**, configure a new **Connector** and a **Connection** for your own model.

   ![docs image](/images/autopilot/autopilot-docs-image-648678-530c3421.webp)

## Chat

Configure a different LLM for reading the context of your current page or project and answering questions, explaining automations, or suggesting improvements. The model you configure overrides the existing model.

Autopilot chat uses a dual-model architecture. Understanding this architecture helps you properly configure your own LLM for Autopilot chat:

* Primary model - used for complex tasks requiring advanced reasoning and capabilities
* Secondary model - used for simpler tasks to optimize costs and performance


:::important
When you configure a model for Autopilot chat, the system may automatically use a lighter secondary model for straightforward operations.
:::

* If you configure different primary and secondary models, a tooltip displays both model names and informs you that the secondary model is used for optimization.
* If you configure only the primary model, a warning message appears indicating that the secondary model configuration is missing. A lightweight, fast primary model is used across all tasks without invoking a secondary model.


:::important
For Automation Cloud organizations, not configuring a secondary model defaults to a UiPath owned subscription. For Automation Suite organizations, not configuring a secondary model may limit chat features, such as context compacting.
:::

1. Go to your **Admin > AI Trust Layer** section of your organization.
2. In the **LLM configurations** tab, select the tenant where you want to configure your LLM.
3. Select **Add configuration** and provide the following properties:
   1. **Product** - select **Autopilot**
   2. **Feature** - select **Chat**
4. Provide the **Connections Folder**.
5. Configure your new model.

   ![docs image](/images/autopilot/autopilot-docs-image-648682-2857fd98.webp)

For details, refer to [Setting up an LLM connection](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-ai-trust-layer#setting-up-an-llm-connection).