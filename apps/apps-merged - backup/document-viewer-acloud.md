---
title: "Document Viewer"
visible: true
slug: "document-viewer"
---

Use the **Document Viewer** control to render a document and display it inline in your app. For example, you can use the **Document** Viewer control to display an invoice document or a receipt which may be located in various sources, such as storage buckets, entities, or public links.

The **Document Viewer** control does not support files on the local machine. You must reference remote documents using a URL, a storage bucket, or an entity.

When assigning the file to an app variable, make sure the variable is of the type `IResource`.

If you only want to display an image, it is recommended to use the [Image](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/image#image) control.

:::important
The Document Viewer uses a built-in PDF.js viewer, which works consistently across browsers. No browser configuration is required. When loading PDFs from external file servers, the server must support cross-origin requests. If CORS is not enabled, the built-in PDF.js viewer will not be able to render the document.
:::

## Using the Document Viewer with a storage bucket

If you are working with a storage bucket in your app, the **Source** property of a **Document Viewer** control must be an `IResource` variable:

1. Add a **Download from storage bucket** rule to your app.
2. Bind an `IResource` variable to the **Download from storage bucket** rule.
3. Bind the same `IResource` variable to the **Source** property of the **Document Viewer.**

## ****Working with IResource****

If you obtain a file as an `ILocalResource`, it is automatically converted into an `IResource` using:

```
JobAttachment.fromResource(file) // file is a ILocalResource
```

:::important
The following functions have been deprecated and should no longer be used:
* `.toLocalResource`
* `.toAppsFile`
:::

**Page Navigation**

You can programmatically navigate to a specific page inside the Document Viewer using:

```
appsFile.NavigateToPage(pageNumber)
```

## General

* **Source** - The source of the document you want to display. The supported file types are `PDF` documents and images (`JPEG`, `PNG`, `BMP`, `GIF`, and `WEBP`).
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
| `Source` | `IResource` | The source file currently viewed. |
| `Value` | `IResource` | Value attached or outputted from the **Document Viewer** control. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |