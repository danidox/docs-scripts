---
title: "Settings for Assistant Policies"
visible: true
slug: "settings-for-assistant-policies"
---

This page describes the settings available for Assistant policies.

## Widgets

On the **Widgets** tab, you can configure settings that control user access to widgets. Widgets are plugins that add functionality to the Assistant. The following widgets are added by default:

* **UiPath.Apps.Widget**
* **UiPath.Marketplace.Widget**
* **UiPath.AutomationStore.Widget** (available starting with the Assistant 21.10 template version)

The following settings are available:

* **Allow custom widgets** - Select whether to allow users to add their own custom widgets. This option is enabled by default.
* **Use official feeds** - Select whether to enable the official UiPath® widgets feeds for downloading widgets, in addition to the Orchestrator feed. If this option is not enabled, only the Orchestrator Library Feed is available. This option is enabled by default.
* To add a new widget, click **Add another**, provide the following information, and then click **Save**:
  + Select whether to enable or disable the widget.
  + Enter the name of the widget NuGet package.
  + Enter the widget version.
* To edit a widget, click **Edit** next to it.
* To remove a widget, click **Delete** next to it.

## Feature Toggles
:::note
The settings on the **Feature Toggles** tab are available starting with the 23.10.0 policy template version.
:::

Select the **Feature Toggles** tab to enforce Assistant settings.

* **Enable Task Capture** - Select **Yes** to show the [Task Capture Launcher](https://docs.uipath.com/assistant/standalone/latest/user-guide/task-capture-launcher).
* **Enable Task Mining** - Select **Yes** to display the [Assisted Task Mining launcher](https://docs.uipath.com/task-mining/automation-cloud/latest/user-guide/assisted-task-mining-introduction).
* **Group processes by folders** - Select **Yes** to group processes by Orchestrator folder on the home page. To allow users to change this option from Assistant, select the corresponding checkbox.
* **Minimize Assistant while a process is running** - Select **Yes** to minimize the Assistant window when processes are running.
* **Automatically launch Assistant at startup** - Select **Yes** to start the Assistant at sign in time and add the Assistant icon in the Windows notification area.
* **Allow users to change the logging level in Assistant** - Select **Yes** to enable the Log Level picker in Assistant.
* **Allow users to run automations outside Personal Workspace** - Select **Yes** to allow running automations from other Orchestrator folders.
* **Enable Action Center** - Select **Yes** to allow the use of the [Action Center widget](https://docs.uipath.com/assistant/standalone/latest/user-guide/action-center-widget).
* **Allow users to share an automation URL** - Select **Yes** to allow users to share the URL of an automation installed in a shared folder.
* ****Display EDR Protection status in Assistant**** - Select **Yes** to display in Assistant whether your machine is protected with EDR.
* **Switch To Running Tab** - Select **Yes** to make the Assistant focus on the running tab when an automation is launched.