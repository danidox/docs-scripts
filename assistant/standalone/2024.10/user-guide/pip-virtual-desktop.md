---
title: "Robot session - Virtual Desktop"
visible: true
slug: "pip-virtual-desktop"
---

**Robot session - Virtual Desktop** allows you to run automations in a virtual desktop on your machine, freeing your main desktop. It also supports multiple PiP user sessions per machine and does not require re-authentication or starting any apps already opened in the main desktop.

## How it works

When a process is started in a Robot session, a new virtual desktop is launched and the process runs there, leaving the main desktops free to interact with. While the automation is running, you can see what the robot is doing and can use the **Switch to PiP desktop** button to access the virtual desktop where the automation is running.

## Additional information

* UIAutomation Activities v22.4 and above is required for Edge/Chrome browser automation when using PiP - Virtual Desktop.