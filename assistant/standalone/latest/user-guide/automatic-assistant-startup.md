---
title: "Automatic Assistant startup"
visible: true
slug: "automatic-assistant-startup"
---

## Enabling auto-start during installation

You can enable the **Automatically Starts Assistant with Windows** option during the attended MSI installation. This adds UiPath Assistant to your Windows Startup Apps and enables the corresponding **Automatically start Assistant with Windows** setting within your Assistant preferences.

## Managing auto-start after installation

The ability to control auto-start from your Assistant preferences depends on whether you enabled it during installation.

* **If auto-start was NOT enabled during installation—**Your Assistant application controls the UiPath Assistant entry in your Task Manager Startup Apps. You can enable or disable auto-start through your Assistant settings, and this is reflected in the Task Manager. However, if you manually disable UiPath Assistant in the Task Manager, your Assistant cannot re-enable it, and you must do so in your Task Manager.
* **If auto-start WAS enabled during installation—**The **Automatically start Assistant with Windows** setting in your Assistant preferences is enabled. To disable auto-start, you must manually disable UiPath Assistant in your Task Manager Startup Apps. The setting in Task Manager overwrites the setting within Assistant