---
title: "Using the Expression editor in controls"
visible: true
slug: "the-expression-editor"
---

The Expression editor allows you to use VB operators and functions, while respecting a predefined syntax. You can identify the properties that can be configured using VB expressions by the "tune" icon ![](/images/apps/apps-image-280277-e5d8b471.webp).

Expressions must reference the property name given in the app page. For example, to reference the main page, include the snippet **MainPage** in your expression. If you rename the main page to **FirstPage**, include the snippet **FirstPage** in your expression.

All custom Apps utility functions are grouped under a single interface that makes them easier to discover. This way, you only need to type in `App.` , and a list of available functions unfolds.

:::note
By default, when you use the Tab key in the expression editor, the system inserts a space in the expression. To enable keyboard navigation using the Tab key, use the Ctrl + M shortcut on Windows, or the Ctrl + Shift + M shortcut on Mac OS X. After you apply this shortcut, pressing Tab switches the focus to the next selectable item on the page.
:::

## Using the Expression editor

To unlock the power of VB expressions in your app:

1. Create a new app.
2. Drag and drop controls in the app pages, or configure rules and events.
3. To edit the **General** properties of a control, or to configure an event rule, look for the "tune" icon ![docs image](/images/apps/apps-image-280277-e5d8b471.webp).
4. For the desired property, click **Open expression editor** and start writing your VB expressions.

   ![docs image](/images/apps/apps-docs-image-280300-9c88c298.webp)