---
title: "About UiPath Assistant"
visible: true
slug: "about-uipath-assistant"
---

The UiPath Assistant is a tool created specifically to turn the user's interaction with our robots into a great and enjoyable experience from the comfort of their desktops. It's the place where individuals can easily access, manage and run automations with just a couple of clicks. The interface can be customized to better suit the person behind it by choosing an avatar and a name for the robot, organizing processes in custom folders on the launchpad, or maybe choosing another theme. All of this makes the UiPath Assistant our bridge between humans and Robots.

The first time Assistant is started, you are presented with an interactive guided tour which takes you through its main features. This can always be restarted from the **Help** section in the **Preferences** menu.

As a client of the Robot, it can send commands to start or stop jobs and change settings, based on user input.

Although it is specially designed for attended use, UiPath Assistant doesn't impose any limits as to what processes you can start. This means that you're able to easily connect to Orchestrator and have jobs started from there.

Additionally, if you run into any issues while using the Assistant, you can start the [UiPath Diagnostic Tool](https://docs.uipath.com/studio/standalone/2025.10/user-guide/diagnostic-tool) from the error dialog box to gather data related to the error.

During installation, you are able to choose to deploy the Robot in User Mode or Service Mode to better suit your environment. For more details, see the According to Deployment document.

After you install and run the UiPath Assistant, an icon ![](/images/assistant/assistant-image-connected-f1a36da2.png) is displayed in the system tray. Clicking this icon brings UiPath Assistant into focus, while right-clicking it brings up a menu from which you can access the Preferences, Orchestrator Settings, bring it to focus or Quit.

UiPath Assistant and Process Execution icons:

## Tray

* ![docs image](/images/assistant/assistant-image-connected-f1a36da2.png) - when the connection is established.
* ![docs image](/images/assistant/assistant-docs-image-disconnected-55749f22.png) - when not connected.
* ![docs image](/images/assistant/assistant-docs-image-error-1e2ff9ae.png) - when an error is encountered, such as the UiPath Robot service being stopped.
* ![docs image](/images/assistant/assistant-docs-image-warning-d29ddc27.png) - when there are new or unread notifications.

The Orchestrator connection status is also displayed in the UiPath Assistant next to the preferences menu.

## Taskbar

* ![docs image](/images/assistant/assistant-docs-image-UiPath%20Assistant-65fbeeb5.png) - Simple Assistant
* ![docs image](/images/assistant/assistant-docs-image-Running_Process-42f36b95.png) - Running Process.
* ![docs image](/images/assistant/assistant-docs-image-Running_Process_PIP-98b00741.png) - Running Process in PIP.

## Interface

The user interface of UiPath Assistant consists of mainly two panels:

* The left side panel contains the **Automations**, **Reminders**, and **Marketplace** tabs.
* If Autopilot for everyone is installed in the tenant where you are currently signed in, the **Autopilot** tab is displayed. Select it to initiate the chat experience with Autopilot for everyone.
* The right side panel, also referred to as "The Launchpad", displays your favorite processes for instant access. Additionally, the right side panel displays the details of the automation selected in the left side panel.

### The Autopilot tab

If Autopilot for everyone is installed in the tenant where you are currently signed in, the Autopilot tab is displayed.

Select it to initiate the chat experience with Autopilot, and [learn how you can interact with it](https://docs.uipath.com/autopilot/other/latest/everyone-user-guide/interacting-with-autopilot-for-everyone).

### The Automations tab

The **Automations** tab enables you to:

* View all the available **Automations**:
  + If UiPath Assistant is connected to Orchestrator, automations from the environments and folders the Robot is a part of are displayed. Hovering over an automation displays its name, version and folder.
  + If UiPath Assistant is set to[offline mode](https://docs.uipath.com/assistant/standalone/2025.10/user-guide/field-descriptions), automations in the `%ProgramData%\UiPath\Packages` folder are displayed.
* View all available **Apps** (from UiPath Apps).
* View all available **Studio Web** templates.
* Update automations that have a newer version available.
* Add an automation to the Launchpad, by clicking the contextual menu, and then selecting **Add to favorites,** or by simply dragging and dropping the automation from the left side panel to the Launchpad.
* View all currently running foreground and background processes.
* Pause, resume, or stop a process. The **Pause** button can be disabled for a process from the [Studio Process Settings window](https://docs.uipath.com/studio/standalone/2025.10/user-guide/about-automation-projects#section-adjusting-process-settings). Once a process is started, the execution status is displayed. You can use the [Report Status](https://docs.uipath.com/activities/other/latest/workflow/report-status) activity to have custom status messages displayed during execution.

### The Reminders tab

The Reminders tab enables you to specify a time or period for you to receive a notification for starting an automation.

You can reminders for any automation in the **Dashboard** tab.

Automations with reminders are listed under the **Reminders** tab and a notification pops up just before an automation is set to begin. Your approval is required for an automation to start. You can snooze the reminder for 10 minutes, dismiss it, or start the process.

### The Tasks tab

Assistant displays the **Tasks** tab when you have Action Center enabled on the selected tenant.

The **Tasks** tab displays the list of your **Pending**, **Unassigned**, and **Completed** Action Center tasks across all accessible folders in your selected tenant.

To provide a quick visual cue, a notification bubble appears next to the **Tasks** tab, indicating the count of **Pending** actions that require your attention.

The **Tasks** tab replicates the behavior of the Actions window in Action Center, namely:

* [Action views](https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/about-actions#action-views)
* [Action filtering operations](https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/about-actions#action-filtering-operations)
* [Action sorting operations](https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/about-actions#action-sorting-operations)
* [Editing action properties](https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/about-actions#editing-actions-properties)
* [Bulk editing and completing actions](https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/about-actions#bulk-editing-and-completing-actions)
* [Labeling actions](https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/about-actions#labeling-actions)

### Automation Details

#### Downloading the package

For automations marked with the **Awaiting install** status, UiPath Assistant first downloads the automation package. During this operation, the Automation details panel displays the size of the package and its dependencies.

#### Details

The **Details** tab displays data the automation developer provided during design time in Studio. Once you select an automation in the left-side panel, the tab displays the automation name, followed by a shareable link, accessible only by users with the necessary permissions.

* **Description**, optionally accompanied by the **More details** link, which redirects you to Automation Hub
* **Version** of the automation package
* **Last Run** indicator
* **Last Updated** indicator
* Any external **Apps** that were used in the automation, such as Outlook, Acrobat Reader, etc.
* The Orchestrator **Folder** that stores the automation package

If the automation is ready for running, you can start its execution by selecting the **Run** button at the bottom of the tab. Otherwise, if it needs extra configurations, such as input arguments or connections, the button **Configure** is displayed and redirects you to the **Configure** tab.

#### Configure

The **Configure** tab displays data the end user should consume during the execution of the automation:

* The **Inputs** section helps you configure the input argument required by the automation for a successful execution. Mandatory input fields are marked with an asterisk. If the automation was designed without input arguments, the **Inputs** section is absent.
  :::note
  If the process has input arguments, hover over the information icon to see their description.
  :::
* The **Connections** section helps you configure the connections required by the automation for a successful execution. If the automation was designed without connections, the **Connections** section is absent.
* The **Picture in picture** section allows you to turn on or off the Robot session. The setting is inherited from the project settings in Studio.
* The **Keyboard Shortcuts** section allows to set custom keyboard shortcuts to manage the execution of the automation, such as pause or stop commands.

Select **Save** to preserve the current configuration, then select **Run** to start the job execution.

#### Jobs

The **Jobs** tab displays the custom messages created using the Report Status activity. These messages monitor the job execution and inform you about every action the automation takes, until it successfully completes or fails due to errors.

If the selected automation was never run in the past seven days, the **Jobs** tab is empty. Once you start running a process, the corresponding jobs and their statuses are displayed in this tab.

If a job execution fails, you are redirected to the **Jobs** tab to see the errors that occurred, regardless of the tab which was currently in focus.

Jobs from multiple running automations are divided into separate collapsible sections. To view details on a particular execution, expand the relevant job section.

Once a job completes, its execution details remain accessible on the **Jobs** tab for a week, then they get dismissed automatically. You can always access execution details in the **History** tab.

#### History

Displays the job history for the selected automation, along with the job state and time stamp. Clicking on an entry displays the job details, such as machine name, error message, or output values (if applicable).

#### The More actions menu

The More actions menu ![docs image](/images/assistant/assistant-docs-image-253243-6683d327.webp) allows you to manage an automation:

* To remove the automation from both UiPath Assistant and Orchestrator personal workspace feed, select **Delete personal automation**.
* To add the automations to the **Favorites** section of the Launchpad, select **Add to favorites**.
* To create a link that, when accessed, opens Assistant to that automation, select **Copy link to automation**. You can also do this by selecting **Share** next to the automation name in the **Automation details** panel. This option is only visible for automations from shared folders.

### The UiPath Products Group

In the launchpad, you can find the UiPath Products, which based on the governance policies applied can contain the following products or features:

* [Task Capture Launcher](https://docs.uipath.com/assistant/standalone/2025.10/user-guide/task-capture-launcher)
* [Assisted Task Mining launcher](https://docs.uipath.com/task-mining/automation-cloud/latest/user-guide/assisted-task-mining-introduction)
* [Studio Web](https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/overview)
* [Submit an idea to Automation Hub](https://docs.uipath.com/assistant/standalone/2025.10/user-guide/automation-store-widget)
* [Clipboard AI](https://docs.uipath.com/clipboard-ai/standalone/latest/user-guide/introduction)
:::note
Assisted Task Mining launcher only works with an Automation Cloud license. The Clipboard AI card is displayed only Autopilot for everyone is installed in the connected tenant. Select it to launch the Clipboard AI toolbar.
:::

This section can be disabled from the **Launchpad** section in the **Preferences** menu of the UiPath Assistant.

## Connections in UiPath Assistant

[Connections](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/connectors) can be used directly from the UiPath Assistant by accessing the **Process Details** menu.

If a process already has connections set up, the user can select it from the list. Otherwise, they can create a new one from the same menu.

If a connection has multiple accounts tied to it, you can select a specific one from the dropdown menu.