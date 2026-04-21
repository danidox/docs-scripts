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
* **UiPath.AutomationStore.Widget** (available starting with the Assistant 21.10 policy template version)
* **UiPath.Autopilot.Widget** (available starting with the Assistant 2024.10.1 policy template)

The following settings are available:

* **Allow custom widgets**—Select whether to allow users to add their own custom widgets. This option is enabled by default.
* **Use official feeds**—Select whether to enable the official UiPath widgets feeds for downloading widgets, in addition to the Orchestrator feed. If this option is not enabled, only the Orchestrator Library Feed is available. This option is enabled by default.
* **Add another**—Select it to add a new widget, provide the following information, and then select **Save**:
  + Select whether to enable or disable the widget.
  + Enter the name of the widget NuGet package.
  + Enter the widget version.
* **Edit**—Select it to edit the corresponding widget.
* **Delete**—Select it to remove the corresponding widget.

## Feature Toggles
:::note
The settings on the **Feature Toggles** tab are available starting with the 23.10.0 policy template version.
:::

Select the **Feature Toggles** tab to enforce Assistant settings.

* **Enable Task Capture**—Select **Yes** to show the [Task Capture Launcher](https://docs.uipath.com/robot/standalone/2023.10/user-guide/task-capture-launcher).
* **Enable Task Mining**—Select **Yes** to display the [Assisted Task Mining launcher](https://docs.uipath.com/task-mining/automation-cloud/latest/user-guide/assisted-task-mining-introduction).
* **Group processes by folders**—Select **Yes** to group processes by Orchestrator folder on the home page. To allow users to change this option from Assistant, select the **Use local user preferences** checkbox.
* **Minimize Assistant while a process is running**—Select **Yes** to minimize the Assistant window when processes are running.
* **Automatically launch Assistant at startup**—Select **Yes** to start the Assistant at sign in time and add the Assistant icon in the Windows notification area.
* **Allow users to change the logging level in Assistant**—Select **Yes** to enable the Log Level picker in Assistant.
* **Allow users to run automations outside Personal Workspace—**Select **Yes** to allow running automations from other Orchestrator folders.
* **Enable Action Center**—Select **Yes** to allow the use of the [Action Center widget](https://docs.uipath.com/robot/v2022.10/docs/action-center-widget).
* **Allow users to share an automation URL**—Select **Yes** to allow users to share the URL of an automation installed in a shared folder.
* ****Display EDR Protection status in Assistant****—Select **Yes** to display in Assistant whether your machine is protected with EDR.
* **Automatically switch to Jobs Tab when an automation starts**—Select **Yes** to make the Assistant focus on the **Jobs** tab when an automation execution fails. To allow users to change this option from Assistant, select the **Use local user preferences** checkbox.
* **Enable Picture in Picture**—Select **Yes** to turn on the Robot session.
* **Skip headers overrides**—Use this setting to specify URLs where Assistant should ignore any on-request header overrides. Select **Add another** to include additional URLs.