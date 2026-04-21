---
title: "App Errors & Troubleshooting"
visible: true
slug: "app-errors-troubleshooting"
---

Apps with errors cannot be previewed or published. If your app has errors, an error dialog is displayed when you select **Preview** or **Publish**.

To identify all errors in your app, check the tree view on the left. Controls with errors have an error icon. Hover over the error to see the error description, or select the error icon to open the faulty general property or rule.

Once all the errors are resolved, you can preview or publish the app.

![docs image](/images/apps/apps-docs-image-290238-209c8de9.webp)

## Capturing errors at runtime

To capture an error thrown by a process or API at runtime, use the following expressions in a control:

* `<PageName>.<ControlName>.<ProcessName>.Error` for capturing a process integration error.
* `<PageName>.<ControlName>.<API>.Error` for capturing an API integration error.