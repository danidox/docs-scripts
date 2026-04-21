---
title: "Installing UiPath Assistant"
visible: true
slug: "installing-uipath-assistant"
---

The UiPath Assistant is available for both Windows and MacOS machines. Here's how you install it:

## Installing on Windows

On Windows machines, UiPath Assistant comes bundled with the `UiPathStudio.msi` and `UiPathRobot.msi` installers. You can install is using the wizard, or by command line when installing the robot. The application can be deployed in user mode or in service mode.

Use the following `UiPathStudio.msi` command to install UiPath Assistant:

```
//command for silently installing Studio, Assistant, and Robot in User Mode:
UiPathStudio.msi ADDLOCAL=Robot /Q
```

Use the following `UiPathRobot.msi` commands to install UiPath Assistant:

```
//command for silently installing Assistant, and Robot in User Mode:
UiPathRobot.msi ADDLOCAL=Robot /Q
```

## Installing on Mac

The UiPath Assistant is available for macOS machines as a `.dmg` file for both Intel or Apple Silicon devices.

Installation steps:

1. Download the `.dmg` file from the Featured Download section in the Automation Cloud Resource Center
   * Download for Intel Macs - x64
   * Download for Apple Silicon
2. Double-click the DMG file to make its content available.
3. Drag the application from the DMG window into the Applications directory to install it.
4. Wait for the copy process to finish.