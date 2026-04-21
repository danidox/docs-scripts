---
title: "2023.10.4"
visible: true
slug: "release-notes-2023-10-4"
---

**Release date: 8 February 2024**

## Bug fixes

* **Erratum - added 22 February 2024** We’ve addressed a random "Connection Closed" error in Studio during process debugging or execution, which forced you to terminate both Studio and Executor in order to rerun the process again.
* Previously, creating a session assigned "RDP_xxxxx_xx" as the Client Name for the robot machine. With this update, the machine’s host name is used instead. This allows for reusing RDP licenses rather than allocating a new one for every session.
* We've fixed a bug that was causing the Legal Policy to be immediately re-enabled when a session connect ended, even if other sessions were still in the process of connecting.
* This patch brings several accessibility fixes in UiPath Assistant. Here’s some of them:
  + Errors that prevent you from saving reminders in UiPath Assistant are now clearly displayed.
  + Navigating in UiPath Assistant's left-side panels with the Tab key now shows two accessibility buttons: "Skip below main content" for quick jumps to the end of your list, and "Skip above main content" for easy returns to the list's start.
  + You can now access the list of your tenants in UiPath Assistant by clicking on your user profile.