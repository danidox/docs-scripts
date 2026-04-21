---
title: "Picture in Picture"
visible: true
slug: "picture-in-picture"
---

Picture-in-Picture allows you to run attended automations without having to interrupt your current activity on the machine.

Just as you can consume media while using the computer with the help of Picture in Picture, the work you have can be separated as well.

While the Robot works in PiP, your machine is free and you can access your files, modify documents, send e-mails, answer phone calls, and other duties that can only be completed by you.

There are two versions of Picture in Picture, both isolating the automation from your work, and are based on the following technologies:

* [Child Session](https://docs.uipath.com/assistant/standalone/2023.10/user-guide/pip-child-session#pip---child-session) - Processes run in a separate Windows session on the machine.
* [Virtual Desktop](https://docs.uipath.com/assistant/standalone/2023.10/user-guide/pip-virtual-desktop) - Processes run in the same Windows session but on a virtual desktop. A PiP process is started from either the **Debug** tab in Studio, from StudioX, or from the UiPath Assistant.

## Setting the PiP type

The PiP technology used by your automations is set from the **PiP Type** menu in the **Project Settings** in Studio. By default, this is set to New Session.

The following options are available:

* **PiP Type**:
  + `New Session` - When the automation is run in PiP, the child session technology is used.
  + `New Desktop` - When the automation is run in PiP, the virtual desktop technology is used.

    ![docs image](/images/assistant/assistant-docs-image-102623-05a44c78.bmp)

## Marking a process as PiP ready

If a process has been tested and can be safely run in PiP, you can mark it it as such from the Project Settings in Studio.

From the same menu, you can also set it to start by default in Picture-in-Picture, and choose the PiP technology you want to use:

* **PiP Options**:
  + `Tested for PiP Usage; Starting in PiP` - The automation has been approved to run in PiP mode. When run, it starts in PiP by default.
  + `Tested for PiP Usage; Not starting in PiP by default` - The automation has been approved to run in PiP mode. When run, it starts in the main session by default.
  + `Not tested for PiP usage` - The automation has not been approved to run in PiP mode. When run, it starts in the main session by default.

    ![docs image](/images/assistant/assistant-docs-image-102180-95ffb4ad.bmp)

## Using PiP for Invoke activities

When using Invoke Activities such as Invoke Process, Invoke Workflow File, and Run Parallel Process, you can choose the session in which they run.

This is done by setting the **Target Session** property of the activity in Studio using the following values:

* Current - The child process opens in the same session or desktop the user is in.
* Process Default - The child process uses the configuration set in the **Process Settings**.
* Main - The child process starts in the user session regardless of where the parent process runs.
* Picture-in-Picture - The child process starts in Picture-in-Picture regardless of where the parent process runs.

  ![docs image](/images/assistant/assistant-docs-image-102184-d25fe5c5.bmp)

  :::note
  The `Target Session` property can **only** be modified from **Studio**. To alter this property for projects developed in **StudioX**, you must open them in **Studio**.
  :::

## Accessing the Picture in Picture feature

**From Studio**: Go to the **Debug** tab, then select the **Picture in Picture** option.

**From Assistant**: For the desired automation, select the **Configure** tab, then turn on the **Run in PiP** toggle.