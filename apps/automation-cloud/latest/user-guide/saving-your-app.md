---
title: "Saving Your App"
visible: true
slug: "saving-your-app"
---

**UiPath Apps** has a 30-second interval auto-save feature. This means that every 30 seconds your application is automatically saved, but only if there are new changes during that time period.

## Auto-save Feature

You can see whether your application is saved at any time by checking the status in the user interface. If the application is saved, the following message is displayed: `All changes saved`.

![docs image](/images/apps/apps-docs-image-92924-6fde4226.webp)

After you make any changes, the application is automatically saved after the 30-second interval and the following message is displayed: `Busy saving all changes...`. The **Preview** and **Publish** options are disabled while the application is being saved, but they are enabled immediately after the saving process is done.

![docs image](/images/apps/apps-docs-image-92648-ae67cbc2.webp)

## Manual Save Feature

If you make any changes to your application and do not want to wait for the 30-second interval until auto-save, you can always manually save your progress. To do so, click **Save now** when the following message is displayed: `Unsaved changes (auto-save happens every 30 s) Save now`. You can also use the **Ctrl**+**S** keyboard shortcut to save the app.

The application is also saved if you press either **Preview** or **Publish** and there are unsaved changes before previewing or publishing.

![docs image](/images/apps/apps-docs-image-93605-4ab3e30e.webp)

## Internet Connection Issues

Since **UiPath Apps** is an online cloud-based application, your progress cannot be saved if you encounter Internet issues. In such cases, the auto-save feature still tries to save your progress every 30 seconds, or you can retry manually.

![docs image](/images/apps/apps-docs-image-94702-d76635dc.webp)

If the application cannot be saved after more than three retries, a `Save Failure` message is displayed.

![docs image](/images/apps/apps-docs-image-95564-f77520f3.webp)

:::note
There is a high risk that your progress is not properly saved if you encounter internet issues for longer periods or time or if your session expires. Make sure you have a stable internet connection when using **Apps**.
:::