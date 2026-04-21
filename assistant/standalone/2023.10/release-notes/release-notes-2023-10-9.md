---
title: "2023.10.9"
visible: true
slug: "release-notes-2023-10-9"
---

**Release date: October 16, 2024**

## Bug fixes

* Previously, the Robot stored Credential Provider logs under a temp folder, risking being cleaned up and possibly interrupting execution. Now, these logs are securely stored in the `%programdata%` directory, minimizing external impact.
* Screen readers now announce automation installation and running statuses in Assistant.
* We've added a retry feature for handling premature disconnections of Remote Desktop Session. This can occur in situations beyond the Robot's control, such as failures during the Windows login or loading the user profile.