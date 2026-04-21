---
title: "Robot session (previously Picture-in-Picture)"
visible: true
slug: "picture-in-picture"
---

The **Robot session** window allows you to run attended automations without having to interrupt your current activity on the machine.

![docs image](/images/assistant/assistant-docs-image-366185-b2ff8018.gif)

There are two versions of a Robot session, both isolating the automation from your work, and are based on the following technologies:

* [Child Session](https://docs.uipath.com/assistant/standalone/2024.10/user-guide/pip-child-session#pip---child-session) - Processes run in a separate Windows session on the machine.
* [Virtual Desktop](https://docs.uipath.com/assistant/standalone/2024.10/user-guide/pip-virtual-desktop) - Processes run in the same Windows session, but on a virtual desktop.

## Setting PiP type and PiP options

To set the PiP technology for your Robot session, or to indicate if the process should start in a Robot session by default:

1. Open the desired UiPath Studio project, then select the **Project** panel on the left side.
2. Open the **Project Settings** menu.
3. From the **PiP Options** dropdown menu, select an option to indicate whether the project was tested using Picture in Picture and whether it should start in a Robot session by default:
   1. **Tested for PiP Usage; Starting in PiP** - The automation has been approved to run in PiP mode. When you run the process, it starts in a Robot session by default.
   2. **Tested for PiP Usage; Not starting in PiP by default** - The automation has been approved to run in PiP mode. When you run the process, it starts in the main session by default.
   3. **Not tested for PiP usage** - The automation has not been approved to run in PiP mode. When you run the process, it starts in the main session by default.
4. From the **PiP Type** dropdown menu, select the technology to isolate the automation from the user session:
   1. **New Session** - When you run the process in PiP, the child session technology is used.
   2. **New Desktop** - When you run the process in PiP, the virtual desktop technology is used.

      ![docs image](/images/assistant/assistant-docs-image-366193-05feb534.webp)

## Using PiP for Invoke activities

When using Invoke activities such as [Invoke Process](https://docs.uipath.com/activities/docs/invoke-process), [Invoke Workflow File](https://docs.uipath.com/activities/docs/invoke-workflow-file), and [Run Parallel Process](https://docs.uipath.com/activities/docs/begin-process), you can set the session in which they should run.

This is done by setting the **Target Session** property of the activity in Studio using one of the following values:

* **Current** - The child process opens in the same session or desktop the user is in.
* **Process Default** - The child process uses the configuration set in the **Process Settings**.
* **Main** - The child process starts in the user session regardless of where the parent process runs.
* **Picture in Picture** - The child process starts in a Robot session regardless of where the parent process runs.

  ![docs image](/images/assistant/assistant-docs-image-102184-d25fe5c5.bmp)

  :::note
  You can edit the value of the **Target Session** property only from **Studio**. To modify this property for projects developed in **StudioX**, you need to open them in **Studio**.
  :::

## Using the Robot session

To start the Robot session:

1. In UiPath Studio/StudioX > **Debug** tab, select the **Picture in Picture** option, then run your process.
2. In UiPath Assistant, select the desired automation. In the right side panel, turn on the **Run in PiP** toggle, then run your process. The **Robot session** window pops up.

To interact with the screen within the Robot session, click on the **Join** button that appears on hover. Doing so expands the Robot session to full screen on your main display.

To exit full screen, select **Leave Robot session**. This returns you to the Robot session window, which is configured to remain on top of other applications.

To close the Robot session, select X. A prompt asks for your confirmation to end the Robot session.