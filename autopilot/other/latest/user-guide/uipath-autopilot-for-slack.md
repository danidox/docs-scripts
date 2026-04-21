---
title: "UiPath Autopilot™ for Slack"
visible: true
slug: "uipath-autopilot-for-slack"
---

## Overview

UiPath Autopilot now boosts productivity by bringing UiPath automation capabilities directly into Slack, eliminating the need to switch between different applications. Key features include:

* UiPath Autopilot functions as an AI productivity companion seamlessly integrated within the Slack interface.
* Communicate with Autopilot **via natural language** to request task assistance - it will route your requests to the appropriate automations or agents.
* Launch automations using either serverless or unattended configurations, based on your needs.
* Easily discover and engage with conversational agents tailored to specific workflows.
* UiPath Autopilot functions as an AI productivity companion within Slack interface.
* Robust security maintained through the [UiPath Platform](https://www.uipath.com/legal/trust-and-security/privacy-policy) privacy policy.

## Privacy policy

To find out how we process the data shared through UiPath Autopilot for Slack, read the [UiPath Privacy Policy](https://www.uipath.com/legal/trust-and-security/privacy-policy).

## Prerequisites

Before you begin:

1. Ensure access to a UiPath Automation Cloud organization.
2. Verify permissions to see and run unattended automations.
3. Ensure installation of Autopilot for Everyone in the tenant where you want to connect.
4. Confirm you have access to Autopilot for Everyone.
5. Tag the automations you want to run in Slack with the **Autopilot** label. Only automations tagged with the **Autopilot** label are visible in Slack.


:::important
To enable Autopilot for Everyone to correctly route your requests within Slack, automations must be tagged with the **Autopilot** label.
:::
For more information on licensing, refer to [Autopilot - Licensing](https://docs.uipath.com/autopilot/other/latest/overview/licensing).

## Installing the Autopilot app in Slack

1. | |
   | --- |
   | [Add to Slack](https://cloud.uipath.com/pluginecosystem_/slack/install) |

You are redirected to the UiPath Autopilot app installation page.
2. Select **Allow**. A prompt asks you to open the Autopilot app in Slack.
3. UiPath Autopilot is now installed in the selected workspace. All users in the workspace can access it.

## Connecting to your UiPath account

1. To connect to your UiPath account:
   1. Interact directly in the newly opened chat.
   2. Navigate to the **Home** tab, and select **Sign In**.
2. When prompted, select **Allow** in the browser window that opens.
3. Once signed in successfully, select **Configure Tenant** in Slack to finalize your tenant selection.
4. To switch organizations, select **Sign Out** and repeat previous steps.


:::important
Slack offers the following in-chat commands:
* `/autopilot help` - Get help on how to use the agent.
* `/autopilot logout` - Logout from UiPath Autopilot.
* `/autopilot change-tenant` - Change the tenant for the current organization.
:::

## Running automations

The automation card has the following options:

* **Run Action** – Runs the automation. If any inputs are required, a modal window opens after selecting **Run Action** to collect them.
* **View in Orchestrator** – Opens the **Automations** page in Orchestrator.
* **Account / Machine Configuration** – Lets you select the **Runtime**, **Account**, **Machine**, and **Host**, similar to the configuration in Orchestrator. This configuration is stored as a user preference and is applied to subsequent runs.

  ![docs image](/images/autopilot/autopilot-docs-image-594979-a66c8214.webp)

## Chatting with conversational agents (preview)

If you have access to conversational agents, you can start a chat tailored to your needs by selecting **New Chat**, then selecting a conversation agent from the **Select Conversational Agents** list.

To switch to a different conversational agent or interact with Autopilot, simply navigate to the **Home** tab or open a new chat using **+ New Chat**.