---
title: "Advanced settings"
visible: true
slug: "advanced-settings"
---

The **Advanced settings** section contains all the tenant configurations available for Autopilot for Everyone.

To configure advanced settings:

1. Navigate to the Automation Cloud > **Admin** > **AI Trust Layer** > **Autopilot for Everyone** tab, then choose the tenant where Autopilot for Everyone is installed.
2. Expand the **Advanced settings** section. The following options are displayed:
   * **Idle exit**—By default, this option is disabled. Enable it to automatically exitAutopilot for Everyone after a specified period of inactivity. You can set the inactivity period in minutes, with a default value of 10 minutes. The idle exit occurs when you do not interact with Autopilot for Everyone during the specified time interval.
   * **File upload**—Enabled by default, allows you to upload files, screenshots, or active windows in the chat using icons, drag-and-drop, or copy-paste. If this feature is turned off, the upload icons are hidden, and end users cannot drag-and-drop or paste images or files.
   * **System prompt hints**—By default, this option is disabled. Enable it to allow adding additional instructions directly to the system prompt. These additional instructions apply to all users in the selected tenant.
   * **Suggested prompts**—By default, this option is enabled. Disable it to hide suggested prompts generated after every Autopilot response. These prompts apply to all users in the selected tenant.
   * **Suggested prompt hints—**By default, this option is disabled. Enable it to allow adding guidance to the suggested prompts generated after each Autopilot response.
   * **Request classification prompt hints—**By default, this option is disabled. Enable it runs two sequential LLM calls: first classify with the Request Classification Prompt, then process the result with System Prompt Hints.
   * **User notes—**Enabled by default, allows individual users to enhance their personalized interaction with the AI by including their own notes from the **User Notes** section. These user notes are added to the system prompt.
   * **Chat history visibility limit**—By default, this option is disabled, and you can access all chat history. Enable it to choose how many days of chat history to see, including fractional days. For example, a value of `0.5` would show chat sessions from the previous 12 hours.
     :::important
     This only limits how far back chat history is visible, but does not impact how long chat history is retained. Chat history is retained until the user deletes the chat session manually.
     :::
   * **Always search Context Grounding**—By default, this option is disabled. Enable it to allow adding a specific index that Autopilot should always search when answering the first query.
   * **Context Grounding search results**—By default, this option is disabled and returns five chunks for each index search. Enable it to allow specifying the number of chunks returned for each index search.
   * **Context Grounding search phrase hints**—By default, this option is disabled. Enable it to customize how queries are rewritten for Context Grounding searches. This optio is becomes available once you enable **Always search Context Grounding.**
   * **Max pre-response actions—**By default, this option is disabled. Enable it to allow specifying the maximum number of pre-response actions Autopilot for Everyone should perform per prompt.
   * **Send feedback to UiPath—**Enabled by default, allows the display and submission of the the feedback form to UiPath. If this feature is turned off, users cannot offer feedback when they vote answers.
   * **Send feedback using SubmitAutopilotFeedback automation—**By default, this option is disabled. Enable it to route your user feedback to a custom destination, using the **[SubmitAutopilotFeedback](https://docs.uipath.com/autopilot/other/latest/user-guide/configuring-custom-route-for-feedback)** automation. This capability is in addition to, or instead of, sending feedback to UiPath, depending on the **Send feedback to UiPath** setting.
   * **AI translations of automation, data sources and their properties**—By default, this option is disabled. Enable it to allow the auto-translation of automation cards and data source or automation names in settings when a non-English language is configured for Autopilot for Everyone.
   * **User acknowledgment—**By default, this option is disabled. Enable it to create an acknowledgment message that appears each time users start Autopilot for Everyone. Provide values for the following settings:
     + **Header*—**The title of the acknowledgment message
     + **Display image—**The URL of an image to be displayed in the acknowledgment window.
     + **Message*—**The HTML string of the body of the acknowledgment message.
     + **Button text**—The text on the button you need to select to close the acknowledgment message and start the chat.
   * **Color theme—**By default, this option is disabled. Enable it to style the appearance of the Autopilot for Everyone based on your company branding. Provide values for the following settings:
     + **Company logo URL**—The URL containing your company logo. This is displayed at the top of the chat window when Autopilot starts up.
     + **Header text**—The additional text added to the "Autopilot" title at the top of the chat window. For example, if you provided "Smart Agent", then the title would read "Autopilot - Smart Agent".
     + **Header background color (light mode)*—**Write the color for the header background that should be displayed in light-mode themes. Provide HEX format. Make sure you do not include additional spaces, or the value would not be validated.
     + **Header text color (light mode)*—**Write the color for the header text that should be displayed in light-mode themes. Provide HEX format. Make sure you do not include additional spaces, or the value would not be validated.
     + **Header background color (dark mode)*—**Write the color for the header background that should be displayed in dark-mode themes. Provide HEX format. Make sure you do not include additional spaces, or the value would not be validated.
     + **Header text color (dark mode)***—Write the color for the header text that should be displayed in dark-mode themes. Provide HEX format. Make sure you do not include additional spaces, or the value would not be validated.
   * **Maintenance mode**—By default, this option is disabled. Enable it to block usage for all Autopilot for Everyone users in this tenant.

When you are finished configuring the advanced settings, select **Save changes**. Select **Reset** to discard all changes, and reload the existing configuration. Restart Autopilot for Everyone for the changes to apply.