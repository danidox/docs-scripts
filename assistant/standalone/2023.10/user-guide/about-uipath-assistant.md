---
title: "About UiPath Assistant"
visible: true
slug: "about-uipath-assistant"
---

The UiPath Assistant is a tool created specifically to turn the user's interaction with our robots into a great and enjoyable experience from the comfort of their desktops. It's the place where individuals can easily access, manage and run automations with just a couple of clicks. The interface can be customized to better suit the person behind it by choosing an avatar and a name for the robot, organizing processes in custom folders on the launchpad, or maybe choosing another theme. All of this makes the UiPath Assistant our bridge between humans and Robots.

The first time Assistant is started, you are presented with an interactive guided tour which takes you through its main features. This can always be restarted from the **Help** section in the **Preferences** menu.

As a client of the Robot, it can send commands to start or stop jobs and change settings, based on user input.

Although it is specially designed for attended use, UiPath Assistant doesn't impose any limits as to what processes you can start. This means that you're able to easily connect to Orchestrator and have jobs started from there.

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

The UiPath Assistant's Interface is composed of a two column design:

The left-hand side contains the tabs (Home, Reminders, and Marketplace), while the right-hand side, also named "The Launchpad" has your favorite processes to provide easier access to them. You can drag and drop them to arrange them and create sections as shown below. The right side also displays the automation details when used.

On the bottom of the UiPath Assistant you can find the Robot Identity and the search bar used to find available processes. Based on the governance policies applied, the search functionality can also return results from Automation Store, Marketplace, or templates available in Studio Web.

### The Home Page Tab

The Home Page tab enables you to:

* View all the available automations:
  + If UiPath Assistant is connected to Orchestrator, automations from the environments and folders the Robot is a part of are displayed. Hovering over an automation displays its name, version and folder.
  + If UiPath Assistant is set to[offline mode](https://docs.uipath.com/assistant/standalone/2023.10/user-guide/field-descriptions), automations in the `%ProgramData%\UiPath\Packages` folder are displayed.
* Download automations that have a newer version available, or that need to be downloaded and unpacked locally, and view the installation status.
* Add or remove an automation from the Launchpad, click the contextual menu and then select **Pin to Launchpad** or simply drag and drop the process from the left panel to the Launchpad.
* View all currently running foreground and background processes.
* Pause, resume, or stop a process. The Pause button can be disabled for a process from the [Studio Process Settings window](https://docs.uipath.com/studio/standalone/2023.10/user-guide/about-automation-projects#section-adjusting-process-settings). Once a process is started, the execution status is displayed. You can use the [Report Status](https://docs.uipath.com/activities/other/latest/workflow/report-status) activity to have custom status messages displayed during execution.
* Click on the tenant name next to the connection status to switch between tenants accessible within the Orchestrator to which you are currently connected to.

### The Reminders Tab

The Reminders tab enables you to specify a time or period for you to receive a notification for starting a process. For any process available in the **Process List** section, a reminder can be set.

Processes for which reminders are set, appear on the **Reminders** tab and a notification is displayed once a process is about to start. Please note that a process does not start without your consent. You can snooze the reminder for 10 minutes, dismiss it, or start the process.

### Automation Details

The automation details submenu provides the following:

* Automation Name and Description - these are based on details provided in Studio when the process was created. If an automation is tied to an idea, the Automation Hub URL will be available under the description. The Automation Hub URL can be completed in Studio, in Project Settings.
* [Input Arguments](https://docs.uipath.com/assistant/standalone/2023.10/user-guide/process-configuration) used to configure processes that make use of input arguments. If an Input Argument is mandatory, it is marked by an asterisk `*` next to its name.
* The [Start in PiP](https://docs.uipath.com/assistant/standalone/2023.10/user-guide/picture-in-picture) toggle is inherited from the project settings in Studio. If a process is set to Start in PiP in Studio, the toggle is enabled. Changing it from the UiPath Assistant overwrites the setting from Studio.
* Keyboard shortcut - provides you with the option to set a keyboard shortcut that starts the process.

#### The Contextual Menu

The contextual menu ![docs image](/images/assistant/assistant-docs-image-253243-6683d327.webp) allows you to manage an automation.

* Click on **Delete personal automation** to remove the automation from both UiPath Assistant and Orchestrator's personal workspace feed.
  :::note
  When deleting a process from your personal folder, it deletes the process from the Orchestrator and leaves the package in place.
  :::
* Click **Create desktop shortcut** to start automations directly from your desktop.
* Click **Add to favorites** to add the automations to the Favorites section of the Launchpad.
* Click **Copy link to automation** to create a link that, when accessed, opens Assistant to that automation. You can also do this by clicking the **Copy** button next to each automations name. This button is only visible for automations installed in shared folders. You can control this feature from the Automation Ops policy. Make sure you choose the 23.4.0 policy template.

### The UiPath Products Group

In the launchpad, you can find the UiPath Products, which based on the governance policies applied can contain the [Task Capture Launcher](https://docs.uipath.com/assistant/standalone/2023.10/user-guide/task-capture-launcher), the option to submit an idea to [Automation Hub](https://docs.uipath.com/assistant/standalone/2023.10/user-guide/automation-store-widget), and a shortcut to open [Studio Web](https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/overview).

This section can be disabled from the **Launchpad** section in the **Preferences** menu of the UiPath Assistant.

### The Running Tab

When an automation is running, you can see the steps it goes through in real time, by checking the **Running Tab** in the **Automation Details** section.

The automation steps presented in the Assistant window are configured using the [Report Status](https://docs.uipath.com/activities/docs/report-status) activity in the workflow. This allows you to have a better view on how the automation runs and how long it takes for each step to complete. TOPLEVELNOTEMARKER
  :::note
  You can split a status message on multiple lines when configuring the message in Studio. For this, use `Environment.NewLine` or `vbNewLine` as a line separator for the status message text.
  :::
Once an automation ends, the run history details are kept until you click on **Dismiss**, start the process again, or quit and restart the UiPath Assistant. After the automation is complete, the **Running Tab** is renamed to **Recent run**.

### Your Robot

To make the Robot more human, you can give it an identity by choosing an picture and a name. Just click on the Robot next to the search bar to change the Robot's appearance and name.

## Connections in UiPath Assistant

[Connections](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/connectors) can be used directly from the UiPath Assistant by accessing the **Process Details** menu.

If a process already has connections set up, the user can select it from the list. Otherwise, they can create a new one from the same menu.

If a connection has multiple accounts tied to it, you can select a specific one from the dropdown menu.