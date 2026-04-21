---
title: "Specialized Autopilot"
visible: true
slug: "specialized-autopilot"
---

## Overview

A specialized Autopilot is a task-specific configuration of the general Autopilot for Everyone, customized with specific instructions, tools, and settings, optimized for a particular use-case, within a single tenant.

Business user first interact with the general-purpose Autopilot for Everyone, and then they can select a specialized Autopilot to focus the conversation on the configured use-case. With every new chat, the specialized interaction reverts to the general-purpose one.

## Creating a specialized Autopilot for Everyone

To create a specialized Autopilot:

1. Navigate to the Automation Cloud™ > **Admin** > **AI Trust Layer** > **Autopilot for Everyone** tab, then choose the tenant where Autopilot for Everyone is installed.
2. Select **Create a specialized Autopilot**. The **Autopilot for Grammar** template panel opens.
3. In the **General** section of the template, provide the following mandatory values:

   | Option | Description |
   | --- | --- |
   | Display name * | Provide a name for your specialized Autopilot. The name displays as "Autopilot for <chosen display name>". |
   | Description * | Provide a short description to help business users identify the scope of the specialized Autopilot. |
   | Orchestrator folder * | The Orchestrator folder where the specialized Autopilot is deployed. Must be the same folder where the necessary Context Grounding indexes and automations are. |
   | Custom system prompt * | Provide a set of instruction to help Autopilot understand what it must do and how to answer to business users. |
4. Select **Save** to save the general configuration.
5. Configure [**Starting prompts**](https://docs.uipath.com/autopilot/other/latest/user-guide/stating-prompts#adding-starting-prompts) for the specialized Autopilot.
6. Enable [**Context grounding** indexes](https://docs.uipath.com/autopilot/other/latest/user-guide/context-grounding#enabling-context-grounding-indexes) for the specialized Autopilot.
7. Configure **[Tools](https://docs.uipath.com/autopilot/other/latest/user-guide/automation-properties#tools)** for the specialized Autopilot.