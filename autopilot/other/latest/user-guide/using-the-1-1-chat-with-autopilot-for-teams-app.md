---
title: "Using the 1:1 chat with Autopilot for Teams app"
visible: true
slug: "using-the-1-1-chat-with-autopilot-for-teams-app"
---

## Connecting to your UiPath account

1. From the Teams sidebar, select UiPath Autopilot. The 1:1 chat with Autopilot screen opens, displaying the list of commands that become useful after you log in and configure your UiPath account.
2. To set up your UiPath account, prompt a text in the chat, then follow the steps provided in the conversation.

## Running commands

On the left-hand side, see the **View Prompts** drop-down, which lists all available commands:

* **Help -** Displays the help message.
* **Logout** - Signs you out from the current session. This command allows you to change your current UiPath organization.
* **Change tenant** - Prompts you to select a new tenant.
* **Switch Agent** - Allows you to choose from available conversational agents.
* **Machine configuration** - Allows you to select the **Runtime**, **Account**, **Machine**, and **Host**, similar to the configuration in Orchestrator. This configuration is stored as a user preference and will be used for future runs.
* **List my accessible automations** - Lists the catalogue of microautomations you have access to.
* **Brainstorm ideas for a project** - Is a placeholder prompt designed to give you an idea of how to phrase a request in the AI-powered chat.

## Running automations

The automation card has the following options:

* **Run Action** – Runs the automation. The automation card displays both mandatory and optional input.
* **View in Orchestrator** – Opens the **Automations** page in Orchestrator.

If input is needed, the automation card prompts you to provide the required input arguments.

  ![docs image](/images/autopilot/autopilot-docs-image-594991-06c376fb.webp)

## Chatting with conversational agents (preview)

If you have access to multiple conversational agents, you can switch between them by selecting the **Switch Agent** command from the **View Prompts** drop-down.

To switch to another agent or interact with Autopilot, simply run the command again.


:::important
Autopilot for Teams supports conversation with only one conversational agent at a time. This means you need to switch between agents within the same conversation. A current limitation prevents conversations from persisting when returning to a previously used agent.
:::

## Providing feedback

To give feedback on the AI-generated response, select the thumbs-up or thumbs-down button under the Autopilot reply. This opens the **Submit Feedback** window, where you can enter your comments. Select **Submit** to send your feedback.