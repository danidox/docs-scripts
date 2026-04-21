---
title: "Debug Apps"
visible: true
slug: "debug-apps"
---

You can use the in-app logging mechanism during runtime to capture and download a debug log file to your machine. The debug log uses the JSON format.

There are two logging levels available:

* **Info**: Logs functional and high-level business-oriented data such as operation start, operation end etc.
* **Trace**: Logs highly detailed and granular data across every step of the application process and system flow.

To access the in-app logger:

1. Run your app.
2. Use the **Shift + 4** keyboard shortcut to activate the debugger.
3. Select **Record.** The debug logger starts.

To download the log file to your machine when you are done testing your app:

1. Select the **Stop** button.
2. Select the **Download** button.
   :::note
   If you use Assistant to launch your app, Assistant will automatically save the log data in the `combined.log` file. In this scenario, the **Download** button does not display.
   :::