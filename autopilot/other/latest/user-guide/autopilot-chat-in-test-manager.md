---
title: "Test Manager"
visible: true
slug: "autopilot-chat-in-test-manager"
---

**Autopilot Chat** connects with Test Manager’s built-in Autopilot tools and extends further through custom MCP server integration, allowing it to execute commands, evaluate requirements, generate test cases, and even run external automation processes and agents.

## Connected sources

In Test Manager, **Autopilot Chat** leverages a range of framework tools. By default, all tools are enabled.

* **Documentation Search** – Retrieves content from UiPath documentation.
* **Autopilot Search** – Retrieves all matching objects based on full terms, partial terms or fuzzy terms.
* **Web Reader** - Extracts and summarizes content from public web pages.
* **Web Search** – Answers questions that require updated, external information.
* **AI-Powered Requirement Evaluation** - Assesses the clarity, completeness, and testability of requirements.
* **AI-Powered Test Generation** - Creates structured test cases based on requirement details, user documents, RAG or user prompts.
* **Obsolete Test Detection** - Maintains a clean, up-to-date test repository by identifying the outdated or redundant test cases linked to requirements.
* **Autopilot Chart** - Generates a visual representation of your data in the form of bar charts, line charts, and pie charts.

## Supported LLMs

The list of supported LLMs can be found in the [Configuring LLMs](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/configuring-llms) topic. To use these LLMs, check you have the required policies in AI Trust Layer.

## The AI Trust Layer policy

To use the AI capabilities provided by Autopilot, make sure you have an AI Trust Layer policy active and deployed to your tenant.

Learn how to:

* [Create a policy](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/create-a-governance-policy)
* [Configure the policy for AI Trust Layer](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-ai-trust-layer-policies)
* [Deploy the policy to the tenant where you want use Autopilot](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/deploy-governance-policies#deploy-policies-at-tenant-level)

## User interface

**Autopilot Chat** includes the following options in Test Manager:
* **New chat**—Starts a fresh conversation and saves the previous one in your chat history. Use it when you want to switch topics, so your old prompts and answers do not affect the new interaction.
* **Settings**—Controls how the Autopilot Chat behaves in Test Manager. You can personalize its responses, connect to its built-in capabilities, or connect it to Orchestrator MCP Servers.
* **Chat history**—Displays and reopens past conversations with Autopilot from the last 30 days.
* **Expand/Collapse**—Toggles the chat screen between a compact and fullscreen view, so you can adjust the space it takes within the interface.
* **Close**—Closes the chat screen. You can reopen it anytime by selecting the Autopilot icon in the navigation bar.

## Accessing Autopilot Chat in Test Manager

1. In your Test Cloud™ organization, open **Test Manager**.
2. From the navigation bar, select the **Autopilot** icon from the global header. This opens the Autopilot main screen.
3. Interact with Autopilot Chat.