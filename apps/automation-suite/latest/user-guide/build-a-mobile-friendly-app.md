---
title: "Build a mobile-friendly app"
visible: true
slug: "build-a-mobile-friendly-app"
---

## Overview

You can use **UiPath<sup>®</sup> Apps** to build mobile-friendly apps. The same app can be used on devices with different screen sizes, such as mobile phones, tablets, or computers, without any issues.

To demonstrate this, follow the steps from the [Tutorial](https://docs.uipath.com/apps/automation-suite/latest/user-guide/build-a-mobile-friendly-app#tutorial) section.

You can also find a sample app file with more examples at the end of this page.

:::note
The **Custom List** control does not currently support mobile or small screens.
:::

## Tutorial

Use this example to build an app that contains three fields and a submit button. This app behaves differently depending on the screen size.

1. Create a new app.
2. Add a **Container** control to your app.
   1. Set the **Layout** of the container to **Horizontal**.
   2. Check the **Allow wrapping** property of the container.
   3. Configure the **Width** size of the container as `100 %`.

   ![docs image](/images/apps/apps-docs-image-92200-045fa081.webp)
3. Add a **Textbox** control in the container.
   1. Add `Name` in the **Label** property.
   2. Change the **Label Placement** to **Top** from the **Style** tab.
4. Add a second **Textbox** control after the first one.
   1. Add `Age` in the **Label** property.
   2. Change the **Label Placement** to **Top** from the **Style** tab.
5. Add a third **Textbox** control after the second one.
   1. Add `Address` in the **Label** property.
   2. Change the **Label Placement** to **Top** from the **Style** tab.
6. Add a second container below the first one with the same **Style** properties.
7. Add a **Button** control in the second container.

   ![docs image](/images/apps/apps-docs-image-92356-a28057c7.webp)

## Result and Testing

You can now preview and test your app.

To test your app using the **Google Chrome** browser, follow the steps below:

1. Right-click anywhere on the page.
2. Select **Inspect** from the menu.
3. From the menu on the right-hand side, click **Toggle device toolbar**.
4. Pick the desired dimensions from the dropdown list on the top of the page to test your app.

   ![docs image](/images/apps/apps-docs-image-91624-5845a8a9.gif)

   :::note
   In the case of the **Container layout** control, the containers inside are automatically mobile-friendly. If the controls inside the containers need to be reactive as well, use the **Allow wrapping** property.
   :::

For more examples, you can download the sample app file below.

[Download example](https://documentationexamplerepo.blob.core.windows.net/examples/Apps/Sample%20mobile-friendly%20app.uiapp)