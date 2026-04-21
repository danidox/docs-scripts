---
title: "Enabling Anthropic models"
visible: true
slug: "enabling-anthropic-models"
---


:::important
Starting with Autopilot for Everyone version 2025.4.1, the Anthropic model is enabled by default. However, if your AI Trust Layer Automation Ops policy disables Autopilot for Everyone or Anthropic models, you must update or remove that policy before using the new version.
:::

To enable Anthropic models for your tenant:

1. Navigate to Automation Ops in your Automation Cloud™ organization.
2. [Create a new product policy for **AI Trust Layer (preview)**](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/create-a-governance-policy).
3. On the **Product Toggles** tab, make sure the **Enable calls to third party AI models through AI Trust Layer** option is enabled.
4. On the **Models** tab, turn on the **Anthropic** option.
5. Save the policy.
6. Deploy the policy to the tenant where you want to install Autopilot for Everyone. Use the **No license** license type and the AI Trust Layer product policy.