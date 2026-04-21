---
title: "User interface"
visible: true
slug: "user-interface"
---

## The chat screen

This is the main screen of the Autopilot chat, where all your interactions reside. To access the chat screen, look for the Autopilot icon in your product: ![docs image](/images/autopilot/autopilot-autopilot-icon-584119-3a958551.webp)

On the chat screen you can perform the following actions:

* Use the chat box to interact with Autopilot by providing prompts or asking questions
* Use the dynamic prompt suggestions, which change alongside your workflow context.
* Select the language model Autopilot uses in your interaction. You can select from the available Gemini or GPT-5 instantions, based on your needs.
* Upload files for future handling and exploration.
* Open a **New chat**![docs image](/images/autopilot/autopilot-docs-image-584160-85e9d42b.webp), access the **Settings**![docs image](/images/autopilot/autopilot-docs-image-584164-5868df26.webp)menu, or the **Chat History**.![docs image](/images/autopilot/autopilot-docs-image-584168-e3686e35.webp)

## New Chat

The **New Chat** option in the Autopilot header starts a fresh conversation and saves the previous one in your chat history. Use it when you want to switch topics, so your old prompts and answers do not affect the new interaction.

## Settings

The **Settings** options opens the **Settings** menu, where you can control how Autopilot behaves. You can personalize its responses, enable specific tools, or connect it to Orchestrator MCP Servers.

The available settings are:

* **Personalization**—This section focuses on customizing the chat interaction style and specific instructions:
  + **Show Follow Ups**—On by default, so Autopilot displays follow-up questions or actions after a response to help continue the conversation. Turn it off for a cleaner interaction.
  + **Custom Instructions**—A free-text field where you can write specific guidance or preferences for how Autopilot should respond. For example, preferred terminology, level of technical detail, or specific frameworks/tools you use often. A character counter (0/300) indicates the length limit for these instructions.
* **MCP Servers**—This section focuses on configuring and managing MCP servers that Autopilot can connect to, so it can generate context-aware suggestions based on structured, task-specific information.
  + **Enter server URL**—A text field to input the URL of an MCP server, then **Add** it.
  + **Current Servers**—The list the MCP servers already configured and available to Autopilot.
  + **Manage**—Provides access to the **MCP Servers** configuration page in Orchestrator.
    :::important
    Only MCP servers created in Orchestrator are supported.
    :::
* **Tools**—The list of the capabilities and tools available to the Autopilot chat, organized under **Framework Tools**. You can manage and configure each tool, depending on the context you use Autopilot in.
* **Save** and **Reset to Defaults** options
  + **Save—**Applies your current settings.
  + **Reset to Defaults—**Reverts all settings to their original state.
* **Download conversation**—Allows you to download the current conversation to your local device in JSON format. The file includes details about the organization, tenant, and specific conversation settings.

## Chat History

The **Chat History** option allows you to view and reopen past conversations with Autopilot from the last 30 days. It provides a searchable list of previous interactions. Select an entry to return to useful suggestions, troubleshooting steps, or workflow drafts. You can continue the conversation within that session and benefit from its existing context.