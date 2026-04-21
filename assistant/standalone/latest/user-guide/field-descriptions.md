---
title: "Preferences"
visible: true
slug: "field-descriptions"
---

## Preferences menu

You can access the Preferences menu by selecting your user icon in the top-right corner of the Assistant window. The menu diplays:

* Your user name. Hover over your name to see a tooltip with the email address used for login.
* **Organization**—The organization where you are currently signed in. If you are a member of multiple organizations, you can switch to another organization from this dropdown. This option signs you out and back in silently in the background.
* **Tenant**—The tenant where you are currently signed in. If you are a member of multiple tenants, you can switch to another tenant from the dropdown.
* **Preferences**—Opens the **Preferences** settings window.
* **Help & Info**—Opens the Help section in the Preferences settings window.
* **Sign out**—Disconnects the robot from Orchestrator.
* **Sign in**—Connects the robot to Orchestrator.
* **Quit**—Closes Assistant.
:::important
All running automations are stopped upon switching organizations, tenants, disconnecting, or signing out.
:::

## Preferences settings

To access Assistant-related settings, navigate to the **Preferences** menu, then select **Preferences**.

The next windows displays the following settings options:

* **General**—Configure settings related to:
  + **Theme**—Change the theme for Assistant.
  + **Zoom**—Increase or decrease the size of the content in Assistant.
  + **Language**—Change the interface language of Assistant and Studio.
  + **Automations**—Decide how automations are displayed in the Dashboard panel:
    - **Group by folder** organizes the automations in groups by Orchestrator folders.
    - **Focus the Jobs tab after an automation starts** focuses on the running tab when an automation starts.
    - **Show in Windows Start Menu** makes the automations from Dashboard accessible from the Windows Start Menu.
  + **System**—Enable **Automatically start Assistant with Windows** to allow Assistant to launch at startup, in tray mode. A similar option exists for Assistant on MacOS. This setting is ignored when the **Automatically Start Assistant with Windows** option in the MSI installer is enabled during setup.
  + **EDR protection**—The Crowdstrike EDR (Endpoint Detection Response) protection status of your robot machines is visible in this window. You can control the visibility of this message from the [Automation Ops policies](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/define-governance-policies), by choosing the 22.10.0 or later policy template, or by adding this information in the policies.json file.
  + **Log Level**—Select the level at which the Robot should log information. The following levels are available: Verbose, Trace, Information, Warning, Error, Critical, and Off. You can control if the users can change the log level from Assistant from Automation Ops.
* **Keyboard Shortcuts**—Configure [keyboard shorcuts](https://docs.uipath.com/assistant/standalone/latest/user-guide/field-descriptions#keyboard-shortcuts-in-assistant) for diverse automation-related commands, such as:
  + Pause, resume, or stop an automation
  + Run a specific automation
    :::note
    In order to prevent stop/pause/resume actions that can affect multiple jobs at once, the keyboard shortcuts do not apply to background jobs.
    :::
* **Orchestrator Connection**—Configure your connection to Orchestrator:
  + **Connection Type**—Select the connection type to Orchestrator:
    - **UiPath Platform URL** asks you to provide the UiPath URL where you want to connect [using Interactive Sign In](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/robot-authentication#interactive-sign-in-sso-(recommended)).
    - **Client ID** asks you to provide the Orchestrator URL where you want to connect [using your **Cliend ID** and **Client Secret**](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/robot-authentication-with-client-credentials).
    - **Machine Key** asks you to provide the Orchestrator URL where you want to connect using your **Machine Name** and **Machine Key**. The machine name is automatically identified and filled in. The machine key is created once you provision the machine.
  + **Sign in**—Initiates the authentication automation when Interactive Sign In is used.
  + **Sign out**—Logs you out from Orchestrator and disconnects the Robot.
  + **Connect**—Connects the Robot to Orchestrator when Cliend ID or Machine Key options are used.
  + **Disconnect**—Disconnects the Robot from Orchestrator.
  + **Status**—Informs you about the Robot connection to Orchestrator.
  + **Use Assistant in offline mode**—Turn on to use Assistant in offline mode.
* **UiPath Products**—Decide to show or hide launchers for the following products or features:
  + [Task Capture Launcher](https://docs.uipath.com/assistant/standalone/latest/user-guide/task-capture-launcher)
  + [Assisted Task Mining launcher](https://docs.uipath.com/task-mining/automation-cloud/latest/user-guide/assisted-task-mining-introduction)
  + [Studio Web](https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/overview)
  + [Submit an idea to Automation Hub](https://docs.uipath.com/assistant/standalone/latest/user-guide/automation-store-widget)
* **Tools**—Migrate the automations that are only available on your machine and publish them to your Personal Workspace in Orchestrator. When an automation is migrated to your Personal Workspace for the first time, a new folder is automatically created in the local feed location. This folder is later used to store all future automations that are migrated from the local feed to Orchestrator.
* **Help & Info**—Quick access to the guided tour, documentation, feedback, build and runtime information, or starting the diagnostic tool.
* **Autopilot for Eveyone**—Configure settings specific to Autopilot for Everyone.

### Keyboard shortcuts in Assistant

There are a few things to consider when you configure automations keyboard shortcuts:

* You can use up to three different modifier keys (Ctrl, Alt, Shift) and any other keyboard button. Examples: Ctrl + Alt + Shift
  + P, Ctrl + Alt + P, Shift + P. Please note that the FN key modifier is not supported.
* Your character combination can contain numpad buttons, such as Ctrl + Alt + Num3. Note that using the numerical equivalent instead of the assigned numpad button doesn't work.
* If your character combination contains a numerical value, its numpad equivalent does not work. For instance, using Ctrl + Alt + Num3 instead of Ctrl + Alt + 3.
* You can use function key from F1 to F11. Please note that F12 is not supported because it is a Windows global keyboard shortcut.
* You can not use a global keyboard shortcut which is already in use by a different application.
* If a third-party running application uses the same keyboard shortcut but is not global, the Robot keyboard shortcut is taken into consideration.
* Global keyboard shortcuts can be registered and used by Robots installed on virtual environments.
* If the same keyboard shortcut is used by the **Unblock options** the **Block User Input** activity and the Robot, it unblocks the user input when first pressed, and either pauses/resumes, or stops the automation the next time it is pressed.
* You first need to start an automation before you can use the assigned global keyboard shortcuts.

You can also zoom in using the following keyboard shortcuts:

* `Ctrl + Shift +` = to zoom in
* `Ctrl + -` to zoom out
* `Ctrl + 0` to reset

## Notification Menu

The notification menu in UiPath Assistant provides information about any process that needs configuration, specific details on the tasks assigned or other details that might interest you.