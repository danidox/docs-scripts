---
title: "Configuration checklist for Autopilot for Everyone in Automation Suite"
visible: true
slug: "configuration-checklist-for-autopilot-for-everyone-in-automation-suite"
---

## 1. Prerequisites

Confirm [system, access, and licensing requirements](https://docs.uipath.com/autopilot/other/latest/user-guide/prerequisites) are satisfied.

## 2. Setting up policies

1. Confirm the [Autopilot widget is enabled](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-widget) in your Assistant policy.
2. Confirm the [Anthropic model is enabled](https://docs.uipath.com/autopilot/other/latest/user-guide/enabling-anthropic-models#enabling-anthropic-models) in your AI trust Layer policy.

## 3. Configuring Integration Service connectors for LLMs

Install and configure required Integration Service connectors before proceeding with LLM setup. Ensure the following are installed:

* LLM connectors (mandatory)
  + Azure OpenAI
  + Amazon Bedrock
* Any connectors required for Autopilot Tools.

## 4. Configuring the LLM

Once Integration Service connectors are ready, proceed with [model configuration](https://docs.uipath.com/autopilot/other/latest/user-guide/bringing-your-own-model). 
  :::important
  The Gemini option may appear in the dropdown but is not yet supported.
  :::

## 5. Installing Autopilot for Everyone

[Install Autopilot for Everyone](https://docs.uipath.com/autopilot/other/latest/user-guide/installing-autopilot-for-everyone#installing-autopilot-for-everyone) in your desired tenant.

## 6. Configuring Autopilot for Everyone

1. [Create a Starting prompt](https://docs.uipath.com/autopilot/other/latest/user-guide/stating-prompts#adding-starting-prompts).
2. [Enable a Context Grounding index](https://docs.uipath.com/autopilot/other/latest/user-guide/context-grounding#enabling-context-grounding-indexes).
3. [Install a tool bundle](https://docs.uipath.com/autopilot/other/latest/user-guide/deploying-toolset-automations-from-marketplace).
4. [Enable or disable several Advanced settings](https://docs.uipath.com/autopilot/other/latest/user-guide/advanced-settings).
5. [Enable or disable the consumption of AI units in License settings](https://docs.uipath.com/autopilot/other/latest/user-guide/license-settings#license-settings).

## 7. Creating a specialized Autopilot for Everyone.

[Create a specialized Autopilot for Everyone](https://docs.uipath.com/autopilot/other/latest/user-guide/specialized-autopilot#creating-a-specialized-autopilot-for-everyone) and configure it to your needs.

## 8. Post-configuration validation

* Verify that Autopilot is enabled for targeted users and groups.
* Confirm that the widget, connectors, and models function as expected.
* Validate feature access and integration across your Automation Suite environment.