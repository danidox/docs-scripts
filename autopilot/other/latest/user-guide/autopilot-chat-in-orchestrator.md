---
title: "Orchestrator"
visible: true
slug: "autopilot-chat-in-orchestrator"
---

In Orchestrator, the first iteration of the Autopilot chat uses AI-powered advanced search capabilities to answer your questions. In the future, its capabilities will be extended.

Autopilot in Orchestrator focuses on helping you retrieve and explore information.

## Connected sources

You can use Autopilot to search across connected sources such as:

* **Web Reader**—Extracts and summarizes content from public web pages.
* **Web Search**—Answers questions that require updated, external information.
* **UiPath Documentation Search**—Retrieves content from UiPath documentation.

Autopilot in Orchestrator focuses on helping you retrieve and explore information. For full development support, use Autopilot in Studio Web or Studio 2025.10.1+.

## The LLM used

For the documentation AI functionality, Autopilot uses Azure OpenAI. To use this LLM, check you have the required policies in AI Trust Layer.

## The AI Trust Layer policy

To use the AI capabilities provided by Autopilot, make sure you have an AI Trust Layer policy active and deployed to your tenant.

Learn how to:

* [Create a policy](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/create-a-governance-policy)
* [Configure the policy for AI Trust Layer](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-ai-trust-layer-policies)
* [Deploy the policy to the tenant where you want use Autopilot](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/deploy-governance-policies#deploy-policies-at-tenant-level)

## User interface

Autopilot in Orchestrator includes the following options:

* **New chat**—Starts a fresh conversation and saves the previous one in your chat history. Use it when you want to switch topics, so your old prompts and answers do not affect the new interaction.
* **Settings**—Controls how the Autopilot chat behaves in Orchestrator. You can personalize its responses, or connect it to Orchestrator MCP Servers.
* **Chat history**—Displays and reopens past conversations with Autopilot from the last 30 days.
* **Expand/Collapse**—Toggles the chat screen between a compact and fullscreen view, so you can adjust the space it takes within the interface.
* **Close**—Closes the chat screen. You can reopen it anytime by selecting the Autopilot icon in the navigation bar.

## Accessing Autopilot chat in Orchestrator

1. In your Automation Cloud™ organization, open **Orchestrator**.
2. From the navigation bar, select the **Autopilot** icon ![Autopilot icon](/images/autopilot/autopilot-autopilot-icon-584119-3a958551.webp). This opens the Autopilot main screen.
3. Interact with Autopilot.