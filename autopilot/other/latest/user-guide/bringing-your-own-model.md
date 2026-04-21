---
title: "Configuring an LLM for Autopilot for Everyone"
visible: true
slug: "bringing-your-own-model"
---

The AI Trust Layer card in the **Admin** section of your organization allows you to configure your own subscription for the models Autopilot for Everyone supports.

Configuring your own model simply replaces the UiPath LLM subscription with your own, provided it uses the same model family and version.

To configure your own LLM, you need a connection to the following AI providers, depending on the model you want to incorporate:

* Microsoft Azure OpenAI, for GPT models
* Amazon Bedrock or Amazon Web Services, for Anthropic models
* Google Vertex, for Gemini models.
  :::important
  To set up a Gemini model, you need to reach out to your designated UiPath technical account manager.
  :::

Configure your own LLM following the steps outlined in [Setting up an LLM connection](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-ai-trust-layer#setting-up-an-llm-connection).