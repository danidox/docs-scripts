---
title: "PiP - Child Session"
visible: true
slug: "pip-child-session"
---

The **Picture in Picture - Child Session** allows you to run attended processes in an isolated Windows session without interrupting your current work.

When a process is started in Picture-in-Picture mode, a new session is spawned. If you run an automation in PiP for the first time, you are asked to authenticate the new session using your Windows credentials.

After the session is created, a preview window appears on your desktop, providing real-time feedback from the process execution. This window can be resized, moved, placed in full screen, or put on top of other windows. You can exit Picture-in-Picture mode at any moment by right-clicking the Picture-in-Picture Windows Taskbar entry and selecting **Close Window** or simply closing the window. A confirmation dialog appears and choosing to close the PiP window stops the running process.
:::note
The default timeout to start a process in a PiP session is 180 seconds. If the login in the Picture-in-Picture session takes longer than that, a timeout error is thrown. This default timeout can be changed using `UIPATH_PIP_SESSION_TIMEOUT` environment variable on the machine. When using the Robot in Service Mode, make sure to set the `UIPATH_PIP_SESSION_TIMEOUT` variable as a system environment variable and restart the Robot Service. Admin rights are needed to enable the Picture-in-Picture functionality on the machine. This is needed only the first time Picture-in-Picture is used. Afterwards, the actual process can be started in Picture-in-Picture without elevated privileges.
:::

## Credentials for the Robot session

The credentials used for the Robot session are managed by the Windows Child Session mechanism. For more information, read the [Microsoft child sessions documentation](https://learn.microsoft.com/en-us/windows/win32/termserv/child-sessions).

After PiP is enabled, these credentials are required when a PiP child session is launched until the user logs on again on the machine, or in [specific scenarios](https://docs.uipath.com/robot/standalone/2025.10/user-guide/pip-child-session#pip-requires-login-every-time) such as using a smart card or PIN instead of a username/password combination.

## Enabling PiP on the Machine

The Picture-in-Picture functionality of the machine can be either enabled through command-line, or manually when starting the PiP session for the first time on the machine.

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Method </p> </th>
   <th> <p> Command </p> </th>
   <th> <p> Description </p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td> <p> Manually </p> </td>
   <td> &nbsp; </td>
   <td> <p> The first time you start a Picture-in-Picture session from either Studio or Assistant, you are prompted to enable the PiP functionality on the machine. This requires administrator rights. </p> </td>
  </tr>
  <tr>
   <td> <p> Command-line </p> </td>
   <td> <p><code>UiRobot.exe PiP</code></p> </td>
   <td> <p> Allows you to enable or disable the Picture-in-Picture functionality on the machine. This setting is applied on the local machine and affects all users and is <strong>used for modifying existing installations</strong> . </p><p> It can have the following parameters: </p>
      <ul>
        <li> <code>PiP --enable</code> </li>
      </ul>
<p> Enables the Picture-in-Picture functionality of the machine. </p>
      <ul>
        <li> <code>PiP --disable</code> </li>
      </ul>
<p> Disables the Picture-in-Picture functionality of the machine. </p> Example: <code>UiRobot.exe PiP --Enable</code><p> Administrator rights are required to execute these commands. </p> </td>
  </tr>
  <tr>
   <td> <p> Command-line </p> </td>
   <td> <p><code>UiPathStudio.msi ENABLE_PIP</code></p> </td>
   <td> <p> Allows you to enable the Picture-in-Picture functionality of the machine <strong>during the UiPath command-line installation</strong> . </p><p> To enable it, use the following parameter: </p>
      <ul>
        <li> <code>ENABLE_PIP=1</code> </li>
      </ul>
<p> Example: </p><p><code>UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,RegisterService,Packages ENABLE_PIP=1</code></p> </td>
  </tr>
 </tbody>
</table>

## Known Issues and Limitations

There are a few things to consider when using the Picture-in-Picture feature:

* If you are using a PIN to log into the main Windows session, you are asked for your credentials every time you start a Robot session.
* When the Robot session is active, it also launches startup programs within the same session. This can reset the settings of your peripheral devices, such as keyboard and mouse light settings, back to their defaults.
* Enabling the Remote Desktop Session during an active Robot session requires logging out and logging back in the main Windows Session for the changes to take effect.
* You cannot restart or shut down your machine while the Robot session is active. Close the Robot session first.
* OS restrictions prevent Picture-in-Picture support for Home Editions of Windows 8 and 10.
* The clipboard is shared between the Robot session and the main session.
* Run as administrator cannot be used in the Robot session.
* You can start a single Robot session at a time.
* To start a Robot session, you need **Allow Log On Locally** permissions.

### Microsoft Office automation

Automations that use Microsoft Office resources do not run successfully in Picture-in-Picture if the resources are already open in the main session. In order to make sure that automations run smoothly in PiP, you can do the following:

* Close the resource used by Microsoft Office applications from the main session so they can be opened in the PiP session.
* Use an **Invoke Isolated Workflow** activity to invoke the part of the automation using Microsoft Office and set its [Target Session](https://docs.uipath.com/assistant/standalone/2025.10/user-guide/picture-in-picture) to **Picture in Picture** from Studio.

### Using web browser in PiP sessions

The browser data from a Picture-in-Picture session is saved on the main session by default. If there is an open Google Chrome or Microsoft Edge instance on the main session, it has to use another user profile in the PiP. This is done automatically by the Open Browser activity. We cannot have a specific browser (let's say Chrome) be open with the same user profile both in the PiP session and the Main session at the same time.

However, the mode and location of the browser data can be configured from the [Open Browser](https://docs.uipath.com/activities/other/latest/ui-automation/open-browser) activity properties.

Setting the `UserDataFolderMode` property to `Automatic` allows the browser to use separate user data folders in the main and PiP sessions.

Please note that if you clear the user data from the `%LocalAppData%\UiPath\PIP Browser Profiles` folder in this mode, the corresponding browser extension needs to be enabled again.

In case you need to use data from the main session (such as cookies or saved passwords), consider setting the `UserDataFolderMode` property to `DefaultFolder`. This means that both the main and PiP sessions use the same folder for the browser user data.
:::note
When setting the `UserDataFolderMode` to `DefaultFolder` the browser only works in one session at a time. If the browser is opened in the main session, it does not work in the PiP session. This is because the same browser profile cannot be used in two simultaneously sessions.
:::
:::note
`Target Session` and `UserDataFolderMode` are properties that can only be modified in **Studio**. Projects developed in **StudioX** need to opened in **Studio** to alter these properties.
:::

Setting the **UserDataFolderMode** property to `CustomFolder` allows you to specify different user data folders for the main and PiP sessions.

### PiP Requires login every time

Based on your environment, certain Windows policies might cause the PiP session to request a login every time it starts.

For example, the following setting set to `Disabled` triggers the PiP window to ask for credentials every time it starts:

* `Local Group Policy\Computer Configuration\Administrative Templates\System\Credential Delegation\Allow delegating default credentials`

This also happens when Windows Business Hello PIN is used. PIN authentication only works the first time a PiP session is launched. After that, the PiP session can only be authenticated using username and password.

### Smartcard Authentication

If your environment requires logon with a smartcard, the following policy should `not` be set to `Enabled`:

* `Computer Configuration\Administrative Templates\Windows Components\Remote Desktop Services\Remote Desktop Session Host\Device and Resource Redirection\Do not allow smart card device redirection`

### Workflow takes a long time to start in PiP

When launching a process in PiP for the first time, it takes longer than usual until the actual execution starts. This happens because the PiP session has to start all its Windows processes and start-up programs.

**Recommendation:** Launch a PiP session when starting the machine and keep it open throughout the day. This uses less resources than launching a new PiP session for every process.

### PiP session does not start

Some Windows policies can restrict the PiP session from starting. To avoid this, the user launching a PiP session must be a part of the following policies:

* `Computer Configuration\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Allow Log On Locally`
* `Computer Configuration\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Access this computer from the network`
  + 
  :::important
  This policy is needed if **Device Guard** is enabled on the robot machine. This means that both Kernel DMA Protection is turned on, and Local Group Policies enforce Device Guard on the machine.
    :::

In the scenario where **Device Guard** is enabled but the `Access this computer from the network` is disabled, when trying to launch a PiP session, the following error is displayed: "`ChildSession Disconnected: The system administrator has restricted the types of logon (network or interactive) that you may use. For assistance, contact your system administrator or technical support., Reason: 4871, ExtendedReason exDiscReasonNoInfo`"
:::note
We are currently investigating to find other policies that can affect the PiP functionality.
:::

### VPN client not working in PiP

When VPN clients are used in conjunction with PiP, there are some situations in which conflicts may occur. For example, if the VPN clients are set to start when the user logs in, when PiP starts, another instance of the VPN client is started. This causes a conflict between the two sessions, since the VPN client is set to run a single instance per user.

To resolve these scenarios, we have compiled a list of the most common VPN providers with their particularities, plus resolutions for the known issues that may occur.

### Cisco Anyconnect

**Observed Behavior**

When the Cisco Anyconnect client is running on the user machine and a PiP session is launched, another Cisco Anyconnect client is started in the PiP session.

**Cause**

The Cisco VPN server is set to accept one session per user at a time. When the PiP session starts, Cisco Anyconnect disconnects the VPN in the main session and throws an error in the PiP session.

This shuts down the user's VPN connection, leaving the user unable to access services that require a VPN connection.

**Resolution**

Do not set the VPN client to start automatically at Windows start-up. This stops the VPN client from starting a new connection when the PiP session starts and tunnels the PiP traffic through the main Windows session.

### Zscaler
:::important
Version 4.4.0.300 of Zscaler resolves the behavior observed here.
:::

**Observed Behavior**

When the PiP session is started, another Zscaler client is launched in the PiP session. This causes the Zscaler client to disappear from the main Windows session. Everything works as expected until the user closes the PiP session. When the PiP session is closed, the Zscaler client remains in a limbo state and the user must sign out and sign in again, or restart the machine to open the Zscaler.

**Cause**

Zscaler is investigating this issue on their side.

**Resolution**

Please open up a ticket with the Zscaler support team.

### Pulse secure

**Observed Behavior**

When a PiP session is started, the user is disconnected from the VPN.

**Cause**

The Pulse secure client cannot handle two Windows sessions for the same user.

**Resolution**

We recommend opening a ticket with Pulse Secure team.

### Palo Alto Global Protect

When PiP starts, the GUI shows the user disconnected from the VPN in both sessions. But the PiP session is still connected to the VPN.

**Resolution**

We recommend opening a ticket with Palo Alto team.

### PiP and Windows servers

In a scenario where multiple users are connected at the same time to a Windows Server, only one PiP session can be launched on the machine. This means only one PiP session can be opened on a single machine, regardless of which user or session type was used to open the PiP session.

### PiP and other virtualized environments

On other virtualized environments such as AppV or Citrix XenApps, PiP functionality is not available.