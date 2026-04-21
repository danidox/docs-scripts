---
title: "Robot Service troubleshooting"
visible: true
slug: "robot-service-troubleshooting"
---

## No connection to the Robot Service

### Description

When the Robot is installed as a Windows service, you might sometimes encounter issues such as:

* Uipath Studio does not open. You receive the following error: "One or more errors occured. (Could not connect to UiPath Robot Service. Make sure the service is started!)".
* Assistant displays the following error: "The UiPath Robot Service is unavailable."

One of the most common issues is that the Robot Service may not be active. Check the following table for potential issues and solutions.

:::important
The following solutions may need to be implemented by your network administrator.
:::

### Potential issue: The Robot Service is not running

**Solution:**

Manually start the Robot service:

1. Open the **Services** window.
2. Select the `UiPathRobotSvc` service.
3. Select **Start**.

### Potential issue: The Robot Service takes too long to start

**Solution:**

Windows reports services which do not load in a specified time. By default, this timeout value is 30 seconds, which can be insufficient for the Robot Service. To increase this value, you need to:

1. Open the Windows Registry Editor.
2. Navigate to the **HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control** registry key, and select the **Control** subkey.
3. If the **ServicesPipeTimeout** value is not available, create it:
   1. Right-click the **Control** subkey, and select **DWORD (32-bit) Value** from the **New** menu. A new blank DWORD Value is created.
   2. Type **ServicesPipeTimeout** as the name of the new value.
4. Double-click the **ServicesPipeTimeout** DWORD value. The **Edit DWORD (32-bit) Value** window is displayed.
5. From the **Base** section, select the **Decimal** option.
6. In the **Value data:** field, type in 180,000. This makes the default **ServicesPipeTimeout** 3 minutes. It should be enough time for all Windows services to properly load.
7. Close the Windows Registry Editor, then restart the system for the changes to take effect.

### Potential issue: The Robot machine has incorrect permissions

In this case, the Robot Service might also appear as running.

**Solution:**

Permissions to services are granted from the Windows Registry Editor, as follows:

1. Open the Windows Registry Editor.
2. Navigate to the**HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet** registry key.
3. Right-click the **Control** subkey, and click on **Permissions**. The **Permissions for Control** window is displayed.
4. Select the user under which you are logged in from the **Group or user names** section.
5. Enable the **Allow** option for **Full Control** in the **Permissions** section. This grants the necessary permissions to the Robot.
6. Select **Apply** and **OK** to confirm the changes, then close the window.
7. Restart the system for the changes to take effect.

## Errors when running as Administrator

### Description

Starting with version 2020.4, running UiPath Assistant or Studio as an administrator could block the communication with the Robot Service. The following issues may occur:

* Studio requests you to sign in, as you seem to be logged out.
* Assistant incorrectly displays the connection status as **Offline**, and the process list is not available.

### Potential issue

Studio and Assistant must communicate with the Robot Service, which is a separate Windows process. The Robot Service starts up at the same level of access rights as the Assistant or Studio, which ever calls the service first.

The issue arises when you start the Assistant or Studio at different levels of access rights, such as a normal user and then as an administrator. For example, say the Assistant starts as a normal user, and then you restart it as an administrator. The Robot Service, specifically the User Host service, which was started at the normal user level, is unable to communicate with the Assistant running at the administrator level.

### Solution

Ensure the Robot Service, Assistant, and Studio all operate at the same privilege level.