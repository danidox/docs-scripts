---
title: "Document Viewer"
visible: true
slug: "document-viewer"
---

Use the **Document Viewer** control to render a document and display it inline in your app. For example, you can use the **Document** Viewer control to display an invoice document or a receipt which may be located in various sources, such as storage buckets, entities, or public links.

When assigning the file to an app variable, make sure the variable is of the type `AppsFile`.

If you only want to display an image, it is recommended to use the [Image](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/image#image) control.

:::important
If you are using Google Chrome, depending on your settings, the browser may download the document instead of opening it. This can cause the document to not display correctly in the app. If you are experiencing this issue, follow these steps:
1. Paste the following in your Google Chrome address bar: `chrome://settings/content`
2. Scroll down to the end of the page and select **Additional content settings.** A dropdown selection opens.
3. Select **PDF documents.**
4. Select the **Open PDFs in Chrome** option.
:::

## General

* **Hidden** - If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

No events.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs. **Horizontal**).
  :::
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Margin** - The margin of the control. By default, a margin of 4 px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`, which means `320 x 410px`. To set minimum or maximum values, select the three dot icon (...).

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Source` | `AppsFile` | The source file currently viewed. |
| `Value` | `AppsFile` | Value attached or outputted from the **Document Viewer** control. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |