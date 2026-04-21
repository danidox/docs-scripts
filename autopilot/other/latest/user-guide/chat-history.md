---
title: "Chat history"
visible: true
slug: "chat-history"
---

Chat history is a record of all interactions between you and Autopilot during a conversation session. While Autopilot can refer back to earlier parts of the same conversation to maintain context and provide relevant responses, it cannot access chat history from different sessions. This way, each interaction starts with a clean slate, ensuring unbiased responses. To provide relevant context across all sessions, you can add personal information and notes in the **User notes** section of **Settings**. To reference information from a previous conversation, you need to provide that context again in your new session.

## Accessing chat history

To access the chat history in a session, select the **Menu** icon next to the **New chat** button. The panel with the chat history opens. All chats are divided per day.


:::important
Chat history may be subject to limitations set by your admin.
:::

## Searching chat history

When you have many conversations with Autopilot, the chat history list may become lengthy. To narrow the list to several chats where you discussed a specific topic, use the **Search history** field to input specific keywords used in that conversation.

## Renaming chat history entries

By default, the title of a chat entry is the initial prompt in that conversation, or an auto-generated summary of the conversation.

To quickly identify a conversation, you can rename the corresponding chat entry:

1. Hover over the chat entry you want to rename. The **Rename chat** option becomes visible.
2. Select **Rename chat**. A prompt is displayed.
3. Write the new name for the chat, so that it provides context for the topic discussed with Autopilot.
4. Select **Save**.

## Deleting chat history entries

To delete a chat entry:

1. Hover over the chat entry you want to delete. The **Delete chat** option becomes visible.
2. Select **Delete chat**. A confirmation window is displayed.
3. Select **Delete**.

## Chat history storage management

### Data residency

Chat history for Autopilot for Everyone is stored in the Orchestrator system storage bucket of the user. As a result, the chat history data is stored in the same location where the Orchestrator cloud tenant resides.

### Data access

The system storage bucket is not accessible through the standard Orchestrator user interface, and is limited to individuals with authorized access to Orchestrator personal storage, such as:

* Orchestrator Administrators
* UiPath Site Reliability Engineers (SREs)
* UiPath Directly Responsible Individuals (DRIs)

### Data retention

Each chat session in the chat history is retained until the user explicitly deletes it within the Autopilot for Everyone interface. There is no automatic deletion or expiration of chat history.

Users can delete their chat sessions directly within the interface. Once a session is deleted, all associated chat information is permanently removed from the system.

If needed, users can also contact UiPath Support to request deletion of chat history.

### Data privacy and security

Autopilot for Everyone is intended for business purposes only. We strongly advise against sending private or confidential data through the platform.

While strict access controls are in place, chat history may be accessible to authorized personnel for system maintenance and support purposes.

All data is encrypted in accordance with [Automation Cloud<sup>TM</sup> encryption guidelines](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/encryption).

### Data compliance and protection

Storing and handling chat history comply with UiPath data protection policies and applicable regulations.

For more information about data residency or compliance with regional data protection laws, reach out to your UiPath representative.

### User responsabilities

As the end user, you are responsible for managing your chat history, and you should regularly review and delete any unnecessary or sensitive conversations.

Use Autopilot for Everyone in accordance with your organization data handling and privacy policies.