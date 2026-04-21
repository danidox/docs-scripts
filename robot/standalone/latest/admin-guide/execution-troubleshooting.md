---
title: "Execution troubleshooting"
visible: true
slug: "execution-troubleshooting"
---

## Message too large to process

### Description

Automations that process large volumes of data may fail due to the following error: "Message: Could not retrieve the result of the job execution. This might be because a message was too large to process. Exception Type: System.Exception".

### Potential issue

The data produced by the automation exceeds the value of the `maxMessageSizeInMegabytes` parameter in the `uipath.config` file.

### Solution

Configure the automation to save the output in a [Storage Bucket in Orchestrator](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-storage-buckets) or in [Data Service](https://docs.uipath.com/data-service/automation-cloud/latest/user-guide/using-entities-in-projects), rather than using an output argument.

## Unattended automations using UIAutomation activities do not work

### Description

Unattended automations using UIAutomation activities do not work.

### Potential issue

When a program such as Server Manager, set to start up automatically, shows a Windows User Account Control (UAC) prompt, it prevents the Robot from interacting with the user interface.

### Solution

Identify the program that triggers the User Account Control (UAC) prompt and configure it so that it does not start up automatically.

## Robot fails to start execution

### Description

The Robot fails to start the execution of an automation and displays the following error: "Executor start process failed, reason System.Runtime.InteropServices.COMException: A specified logon session does not exist. It may already have been terminated.".

### Potential issue: The Robot machine does not have enough resources

The Robot machine does not have enough resources (such as CPU, RAM, or Disk Space), so the Robot Executor is unable to start the automation.

**Solution:**
* Make sure that the Robot machine has enough resources (such as CPU, RAM, or Disk Space).
* Check the connection time by using the `mstsc` command-line function. It needs to be greater than 60 seconds, otherwise the error is displayed.

### Potential issue: The logon session cannot be created at the moment

The logon session cannot be created at the moment. This can happen in the following situations:

* The [**Login to Console** property](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/robot-settings) is set to **True** for High-Density (HD) robots. In this case, the Robot Service attaches itself to the current console session. This is not recommended for HD Robots, because there can only be one active console session at a time.
* Multiple RDP sessions on desktop Windows versions (not Servers). Desktop Windows versions can only handle one RDP session at a time per machine, whereas Windows Server versions can handle multiple RDP sessions.

**Solution:**

In this case, you need to perform one of the following:

* Set **Login to Console** to **False**. This means that the Robot Service initiates an RDP connection from the Robot machine onto itself and attaches to it. This is the recommended method for HD Robots.
* Check the Windows version, it needs to be Windows Server.
* Check if the Studio and Robot versions is greater than 2018.1.3.
* Increase the value of the `UIPATH_SESSION_TIMEOUT`system environment variable on your server. The default value is 60 seconds, which might be insufficient due to slow performance on some machines. Restart the Robot Service after modifying this variable.
* Check if your Remote Desktop License is active on the server.
* Check if the Robots are in the proper groups. Local users need to be in the same Remote Desktop group.
* Check if the username of your RDP connection to the Robot machine is the same as the configured one. To avoid this error, sign off all the RDP connections on the Robot machine.

## Password not provided

### Description

Starting an automation from Orchestrator or Assistant displays the following error message: "Executor start process failed, reason System.UnauthorizedAccessException: Access is denied.".

### Potential issue: The Robot account was created without a password

**Solution:**

Edit the robot account in Orchestrator and provide the following values:

* **Domain\Username*** - The username used to connect to the machine on which the Robot is installed. If the user is under a domain, you are required to also specify it in a `DOMAIN\UserName` format.
* **Password** - The Windows login password.

### Potential issue: The Robot Service is inactive

**Solution:**
1. Open the **Services** window.
2. Select the `UiPathRobotSvc` service.
3. Open the **Properties** panel for the selected service.
4. On the **Log On** tab, select **Local System account**.
5. Select **Apply** and **OK** to confirm the changes, then close the window. This ensures the Robot Service is running and has all the privileges it needs for executing automations

### Potential issue: The Robot machine no longer has administrator privileges

**Solution:**

Log in to the Robot machine with the same set of credentials with which you created the Robot in Orchestrator. If a process fails to start from the Assistant, then you need to contact your network administrator to allow admin rights for that user account.

## System.Collections.IEnumerable cannot be serialized

### Description

When using a Data Table in a **Wait For Task and Resume** activity, it returns the following error: "Exception: Type 'System.Collections.IEnumerable' cannot be serialized."

### Potential issue

The DataRow object of Data Table cannot be serialized, so it cannot be persisted, leading to potential issues or errors.

### Solution

Execute the **Create Form Task** activity and build the output by looping through data rows, to create a list of task objects. Then, loop through the output list of task objects using the **Parallel For Each** or **For Each** activities. In these loops, execute the **Wait for Task and Resume** activity for each task object.

## Job stopped with an unexpected exit code

### Description

Your job execution fails and the following error message is logged in Orchestrator: "Job stopped with an unexpected exit code: 0x40010004".

### Potential issue

Commonly, this error occurs when:

* The user account, used by the Robot, is forcibly logged off during the execution of the process.
* The machine on which the Robot is running is manually shut down or restarted during the process execution.

### Solution

To avoid this error, make sure the Robot is installed correctly for the intended type of automation: attended or unattended. Having the Robot installed in User Mode cannot execute unattended automations.

Additionally, [configure the Robot session](https://docs.uipath.com/robot/standalone/latest/admin-guide/windows-sessions#windows-sessions) to suit your environment and business needs.

## Automation works in attended mode, but not in unattended mode

### Description

The same automation works as expected in attended mode, with a human user logged in and watching, but in unattended mode it fails. Other potential issues in unattended mode include:

* The Robot clicks in incorrect locations.
* Random windows open unexpectedly.
* Items from the taskbar activate without user input.
* The target application enters an unexpected state.

### Potential issue

For unattended automations, the Robot Service initializes the Windows session through an RDP connection and it relies on system settings for the display resolution and scaling, or on the Robot settings. Therefore, the resolution and scaling between the remote session and the local session is different.

### Solutions

:::important
Before testing, make sure the Robot user is logged out of the Robot machine. This way, the Robot operates in a clean environment.
:::

Resolution differences are often the primary distinction between attended and unattended modes. Refer to [Fixing resolution issues](https://docs.uipath.com/robot/standalone/latest/admin-guide/execution-troubleshooting#fixing-resolution-issues) and [Resolution best practices](https://docs.uipath.com/robot/standalone/latest/admin-guide/execution-troubleshooting#resolution-best-practices).

**Solution 1: Scaling settings check**
* Scaling settings can affect how the Robot interacts with the user interface.
* If resolution fixes do not help with the issue, check the Windows session scaling settings:
  1. Log in to the machine as if running an attended automation.
  2. Open PowerShell (use the **Run** dialog and type "powershell").
  3. Execute this command:
     ```
     (Get-ItemProperty 'HKCU:\Control Panel\Desktop\WindowMetrics' -Name AppliedDPI).AppliedDPI
     ```
  4. The returned value should be 96. If not, the Robot might have been developed with non-standard scaling. Refer to [Forcing scaling](https://docs.uipath.com/robot/standalone/latest/admin-guide/execution-troubleshooting#forcing-scaling).

**Solution 2: Real-time problem capture**
* If Solution 1 does not help, use the [Live Streaming and remote control](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/live-streaming-and-remote-control) features to capture the issue as it occurs. These tools allow you to observe the Robot behavior without directly logging into the machine, helping identify issues that may not be apparent otherwise.

**Solution 3: UiPath support**
* If the previous steps do not help identify the issue, open a support ticket with UiPath.

### Resolution best practices

* Review the [guidelines for UI Automations](https://docs.uipath.com/studio/standalone/latest/user-guide/ui-automation).
* Make resolution a key design requirement
* Ensure the resolution and scaling of your development and production environments are identical.
* Be aware that if you do not specify a resolution, system defaults apply. This may lead to low resolutions that the application does not support. UI elements may be offscreen or visually distorted.
* Do not overlook resolution-dependent activities:
  + Image-based activities, such as **[Find Image](https://docs.uipath.com/studio/standalone/latest/user-guide/image-activities)**, or [OCR activities](https://docs.uipath.com/studio/standalone/latest/user-guide/ocr-activities).
  + UI Automation activities with clipping regions enabled.
  + UI Automation activities with the **WaitVisible** option enabled.
  + Click activities that do not use **Window Messages** or **Simulate** input methods. For the **CursorPosition** property, refer to [Robot clicking in the wrong location](https://docs.uipath.com/robot/standalone/latest/admin-guide/execution-troubleshooting#robot-clicking-in-the-wrong-location).

### Robot clicking in the wrong location

Incorrect Robot clicks typically indicate the **CursorPosition** option is enabled on the **Click** activity.

The **CursorPosition** property is sometimes configured unintentionally when using the Recording feature in Studio. Identify the activity where the click occurs in the wrong location, determine if the option is enabled intentionally. In most cases, this property is unnecessary.

### Fixing resolution issues

1. Log in to the machine as if running an attended automation.
2. Open PowerShell (use the **Run** dialog and type "powershell").
3. Execute this command:
   ```
   [void][Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")
   [System.Windows.Forms.SystemInformation]::PrimaryMonitorSize
   ```
4. Write down the **Width** and **Height** values returned, as you need them in step 7b.
5. Check font smoothing:
   * Open **View advanced system settings** from the **Start** menu.
   * On the **Advanced** tab, select **Settings** under **Performance**.
   * Check if **Smooth edges of screen fonts** is enabled.
6. If you need bit depth or font smoothing, check display settings on the local machine that connects to the Robot machine:
   * Navigate to **Display Settings**.
   * Go to **Advanced display settings** for bit depth information.
7. [Access the **Robot Settings** section for the robot account](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/robot-settings#configuring-robot-settings) executing the automation (**Orchestrator** &gt; **Tenant** &gt; **Manage Access** &gt; **Access Rules** &gt; **Robot accounts**).
   1. Set the **Login To Console** option to **No**. This instructs the Robot to use RDP sessions for unattended automations.
   2. Set values for **Resolution Width** and **Resolution Height**. Use the same values returned in step 3.
   3. Set 32 for **Resolution Depth**.
   4. For image-based automations, also set **Font Smoothing** to **Yes**.
8. Select **Update**.

### Forcing scaling

Optimally, redesign the automation in a development environment with scaling set to 100%. The following steps are intended as a temporary workaround. Make sure the Robot runs in [an RDP session](https://docs.uipath.com/robot/standalone/latest/admin-guide/windows-sessions#rdp-session) (the **Login to Console** option is set to **No**).

1. Open the **Registry Editor** and navigate to `HKEY_CURRENT_USER\Control Panel\Desktop\LogPixels`.
2. Search for the registry value `LogPixels`. If the value does not exit, create it as a `32-DWORD` value. Consult the following list for possible decimal values:

   | DPI (resolution) | Scale factor, % (the **LogPixels** value) |
   | --- | --- |
   | 96 | 100 (no scaling) |
   | 120 | 125 (everything on the display is 25% larger) |
   | 144 | 150 (everything on the display is 50% larger) |
   | 192 | 200 (everything on the display is twice as large) |
3. Next, navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\`.
4. Search for the registry value `IgnoreClientDesktopScaleFactor`. This registry key tells the remote connection wheter to ignore the scaling on the Robot machine. If the value does not exit, create it as a `32-DWORD` value. Consult the following list for possible decimal values:
   1. 1 - ignores the scaling on the Robot machine
   2. 0 - takes into account the scaling on the Robot machine

## GCP Cloud - Failing UI automations with Linux robots

### Description

Using Linux robots to run a web-based process, developed with Studio Web, returns the following error:

```
Could not open target application.

UiPath.UIAutomationNext.Exceptions.ApplicationOpenException: Could not open target application. at UiPath.UIAutomationNext.Activities.NApplicationCard.GetMainWindowByTargetApp(IActivityContextWrapper context, ITargetApp targetApp, CancellationToken cancellationToken)
at UiPath.UIAutomationNext.Activities.NApplicationCard.GetRuntimeData(IActivityContextWrapper context, CancellationToken cancellationToken)
at UiPath.UIAutomationNext.Activities.NApplicationCard.OpenOrAttach(IActivityContextWrapper context, CancellationToken cancellationToken)
at UiPath.UIAutomationNext.Activities.NApplicationCard.ExecuteAsync(NativeActivityContext context, CancellationToken cancellationToken)
at UiPath.Shared.Activities.AsyncTaskNativeImplementation.BookmarkResumptionCallback(NativeActivityContext context, Object value)
at UiPath.Shared.Activities.AsyncTaskNativeActivity.BookmarkResumptionCallback(NativeActivityContext context, Bookmark bookmark, Object value)
at UiPath.Shared.Activities.ContinuableAsyncNativeActivity.BookmarkResumptionCallback(NativeActivityContext context, Bookmark bookmark, Object value)
at System.Activities.Runtime.BookmarkCallbackWrapper.Invoke(NativeActivityContext context, Bookmark bookmark, Object value)
at System.Activities.Runtime.BookmarkWorkItem.Execute(ActivityExecutor executor, BookmarkManager bookmarkManager)
```

When you use Docker to check what is running on the container, you can see multiple instances of Chrome open to the correct webpage. However, it appears that the Robot cannot connect to these Chrome instances.

### Potential issue

Running the Linux robot image using GCP Cloud run defaults to first generation environment, instead of second generation, [as outlined in this document](https://cloud.google.com/run/docs/about-execution-environments).

### Solution

Force the Robot to use GCP Cloud Run second generation environments: stop the docker image, remove it, and recreate it.