---
title: "Recording and Remote Control troubleshooting"
visible: true
slug: "recording-and-remote-control-troubleshooting"
---

## Minimized RDP window interference

RDP connection applications use different techniques to optimize resource consumption. One technique consists in disconnecting the remote display buffer when the RDP application is minimized. This may lead to issues with UI Automations, [screen recording](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-recording), or [remote control](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/live-streaming-and-remote-control). You can prevent these issues by disabling the resource consumption optimization.

To achieve this, edit the Remote Desktop registry settings on all computers connecting to the Robot via RDP, but not on the Robot machine. You need administrator privileges to perform the following steps:

1. Close any active Remote Desktop sessions.
2. Open the **Registry Editor** window.
3. Navigate to the following Registry keys:
   * For the current user:
     + `HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client` (32 bit)
     + `HKEY_CURRENT_USER\Software\Wow6432Node\Microsoft\Terminal Server Client` (64 bit)
   * For all users on the machine:
     + `HKEY_LOCAL_MACHINE\Software\Microsoft\Terminal Server Client` (32 bit)
     + `HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Terminal Server Client` (64 bit)
4. For every key, create a new **DWORD (32-bit) value**, and rename it to "RemoteDesktop_SuppressWhenMinimized".
5. Modify the previously created DWORD value: in the **Value data** field, write `2`.
6. Select **OK** to save the changes.
7. Close the **Registry Editor** window.
8. Sign off all users from the Robot machine before executing a job. You can now automate UI actions even when the RDP window is minimized.

## RealVNC missing component

### Description

Upon upgrading your Robot installation via existing scripts, you may encounter the following error: "Robot installation missing component: RealVNC".

### Potential issue

This can happen due to the introduction of the `LiveStreaming` parameter. To use the live streaming feature, you must add this parameter to the `ADDLOCAL` command.

If you did not update your installation scripts to include the `LiveStreaming` parameter, the update installs the Robot without the RealVNC capabilities.

### Solution

Starting with version 2024.10, the [live streaming](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/live-streaming-and-remote-control-via-realvnc) feature uses the RealVNC software, which comes bundled in the UiPath Robot and UiPath Studio 2024.10+ installers. Installing or upgrading to the 2024.10+ Robot using the GUI or the command prompt automatically installs RealVNC , unless the `ADDLOCAL` parameter is used. If you choose to use the `ADDLOCAL` parameter in a command prompt installation, you must add the `LiveStreaming` flag.

For example, the following `UiPathRobot.msi` command performs a custom installation or upgrade which also installs RealVNC, the software that is required for live streaming:

```
UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,RegisterService,LiveStreaming
```