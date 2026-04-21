---
title: "Rule: Log Message"
visible: true
slug: "rule-log-message"
---

Use the **Log Message** rule to print a log to the browser console.

![docs image](/images/apps/apps-docs-image-538218-cbd48175.webp)

:::warning
Excessively printing logs in the browser console can degrade performance.
:::

## Message

The content of the log message. Use the **Expression editor** ![](/images/apps/apps-image-280277-e5d8b471.webp) button to configure it.

## Log level

You can select three log level options:

* **Info** - displays the message in blue, with an info icon. This is the default option.
* **Trace** - displays the message in black, with a trace icon.
* **Error** - displays the message in red, with an error icon.

When previewing an app, logging is enabled and set to the **Info** level by default.

When running a deployed app, logging is disabled by default.

## Modifying log levels at runtime

You can modify the log level when running an app as follows:

1. After launching the app, open the developer tools in your browser.
2. Select **Console.**
3. Type the following in the console:
   1. `sessionStorage.setItem("apps.runtime.loglevel", "trace")` to set the runtime log level to **Trace.**

This setting prints all logs to the console.
   2. `sessionStorage.setItem("apps.runtime.loglevel", "info")` to set the runtime log level to **Info.**

This setting prints only **Info** and **Error** messages.