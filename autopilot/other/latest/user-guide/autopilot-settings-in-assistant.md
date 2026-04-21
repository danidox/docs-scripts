---
title: "Autopilot settings for business users"
visible: true
slug: "autopilot-settings-in-assistant"
---

As a business user, you can customize the way Autopilot operates on your end. The available settings may be restricted by the configurations made at tenant-level.

To access the Autopilot settings, select the **Settings** icon at the top-right side of the Autopilot window.

## Profile

In this **Settings** section you can edit personal details, such as:

* Profile picture
* Name
* Email
* Role
* Department
* Location
* Localization toggle, to allow dynamic **AI translation of automations, data sources and their properties**, but only after you change the **Language** from Assistant Preferences. For example, the following image shows the Automations and Data Sources settings after the Language was changed to French.

  ![dynamic AI translation of automations, data sources and their properties, after you change the Language from Assistant Preferences](/images/autopilot/autopilot-dynamic-ai-translation-of-automations-data-sources-and-their-properties-after-you-change-the-language-from-assistant-preference-0dd07140.webp)

## Advanced settings

In this **Settings** section you can edit settings to customize Autopilot in helping with your daily tasks.

* **User notes**—allows you to configure a personalized interaction with Autopilot. User notes are key-value pairs, where the key refers to a preferred **Topic**, and the **Value** should indicate the desired behavior from Autopilot. Select **Add note** to provide your own key-value pairs. To remove a user note, select the bin icon.
* **Data sources**—provides the list of pre-response action data sources Autopilot can query when analyzing your request. To exclude a data source from Autopilot access, turn off the desired option. By default, Autopilot has access to all data sources available. Select **Refresh** to reload the list.
* **Automations**—provides the list of out-of-the-box and custom automations Autopilot can run when analyzing your request. To exclude an automation from Autopilot access, turn off the desired option. By default, Autopilot has access to all out-of-the-box automations. If you added automations in Orchestrator for Autopilot to execute, select **Refresh** to reload the list.
* **Available connections**—provides the list of available Integration Service connections required by the automations selected in the **Data sources**.

## Troubleshooting

If anything goes amiss in your interaction with Autopilot for Everyone, you can access the logs.

Select **Download Logs**, go to the default Downloads location on your device, look for `autopilot-troubleshooting-log.zip` file, then share the downloaded file with your support team. The downloaded file contains the logs and the chat history for the current session.

The **Troubleshooting** section also provides the option to [**Send Feedback**](https://docs.uipath.com/autopilot/other/latest/user-guide/giving-feedback#providing-general-feedback).

To exit autopilot and interrupt the active chat session, select **Exit Autopilot**. This action stops Autopilot and returns you to the restart screen in the Autopilot tab.