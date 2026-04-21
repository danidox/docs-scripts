---
title: "Adding a page to your app"
visible: true
slug: "adding-page"
---

## Prerequisites

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::

To use Autopilot in Apps, your tenant must have sufficient Autopilot actions available.

To add a page to your app using PDFs or images in Autopilot for Apps, you must have Document Understanding enabled in your active tenant.

To add a page to your app using Autopilot, follow these steps:

1. Go to the app where you want to add a new page.
2. In the **Hierarchy** panel, select the **More options** "..." button to the right of a page entry.
3. Select **Add new page**. The **Autopilot** window opens.
4. To create a new page, you can use one of three different inputs:
   * Attach a PDF or image.
   * Write a text prompt describing the intended page.
   * Or select an entity to use as a base for the new page.

   ![docs image](/images/apps/apps-docs-image-435517-5b536506.webp)
5. Select **Send** to begin the generation process. The app generation process immediately begins.
   :::note
   * Please keep in mind that all limitations related to creating apps using Autopilot are applicable to creating pages.
   * By default, the **Create Entity** option is enabled. This creates a new entity and sets its rules accordingly. If you do not want an entity to be created,
   you should clear the checkbox.
   * Keep in mind that there may be differences between the original file and the form digitized by Autopilot.
   :::

Autopilot builds the new page and adds it to your app automatically.