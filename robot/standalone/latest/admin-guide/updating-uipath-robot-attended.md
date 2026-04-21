---
title: "Updating UiPath Robot"
visible: true
slug: "updating-uipath-robot-attended"
---

The update process ensures that both Studio and Robot are upgraded to the latest available version.

Before updating your Robot version, check the [compatibility matrix](https://docs.uipath.com/overview/other/latest/overview/compatibility-matrix).

When planning for an update, keep the following recommendations in mind:

* Preserve the Robot operational mode: Service Mode or User Mode.
* Match Robot and Studio versions. Refer to the [compatibility matrix](https://docs.uipath.com/overview/other/latest/overview/compatibility-matrix#automation-projects) for guidance.
* `UiPathRobot.msi` cannot update an older `UiPathStudio.msi` installation.
  :::important
  When you have Orchestrator installed on the same machine as the Robot, we recommend updating your Orchestrator version first, followed by the Robot version. To apply the new settings, reconnect the Robot to Orchestrator.
  :::

## Manual update

:::important
This option is available exclusively for Enterprise LTS versions of Robot. Community versions are automatically updated to the latest release. For instance, you can manually update your 2024.10.5 LTS version to the latest 2024.10.9 LTS version. Community installations, however, are always updated to the most recent version, and selecting a specific version is not possible
:::

### Updating Service Mode robots

To update a Robot that was initially installed in Service Mode, run `UiPathStudio.msi` or `UiPathRobot.msi` with default settings. This replaces old files without altering your settings.

Updating stores activity packages in the `C:\Program Files\UiPath\Studio\Packages` folder.

To update the Service Mode Robot from the command line using `UiPathStudio.msi`, write:

```
UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot,RegisterService
```

### Updating User Mode robots

To update a Robot that was initially installed in User Mode, run `UiPathStudio.msi` or `UiPathRobot.msi` with default settings. This replaces old files without altering your settings.

To update the Service Mode Robot from the command line using `UiPathStudio.msi`, write:

```
UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot
```

### Switching between modes

When switching from Service Mode to User Mode, the Robot might not be able to access the `.xaml` files from the original NuGet Packages folder.

Updating the configuration variables requires a Robot restart to take effect, but several changes in Orchestrator settings do not need a restart. These include:

* `RunDisconnectedHours` - the number of hours the robot can run offline (disconnected from Orchestrator).
* SignalR settings - parameters related to the SignalR technology used for real-time communication between Robots and Orchestrator.
* `HeartbeatPeriodSeconds` - the frequency, in seconds, at which the Robot sends a heartbeat signal to Orchestrator to show it is online.
* NuGet feeds - references to package sources for activities.

To switch from User Mode to Service Mode, make sure the `RegisterService` parameter is **added** to the `ADDLOCAL` command.

To switch from Service Mode to User Mode, make sure the `RegisterService` parameter is **removed** from the `ADDLOCAL` command.

## Updating Robot Community editions

In the attended scenario, an update prompt is displayed with the following options:

* **Update Now** - Stops all currently running jobs and closes all active Studio and Assistantcinstances. The update then proceeds immediately.
* **Later** - Postpones the update. The notification is muted, and you can initiate the update process at your convenience. You can launch the update process by clicking **Check for updates** in the UiPath UI icon located in your system tray.

Once you approve the prompt, the update service gets the confirmation and starts the update process. Without a response in 24 hours from the first notification, the update installs automatically.

Community Preview installations running version 2021.8 or later can automatically update to the latest Community Preview release.

Closing Studio during the automatic update process causes the Robot to lose the connection to Orchestrator. This issue does not occur with licensed installations.

Refer to the [Update Service](https://docs.uipath.com/robot/standalone/latest/admin-guide/update-service#update-service) for more details.