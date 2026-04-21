---
title: "Binding a media document to Image controls"
visible: true
slug: "binding-a-media-document-to-image-controls"
---

Make sure the media file is uploaded to your app.

:::note
Media support is relevant for the **Source** property of the **Image** control.
:::

1. Add an **Image** control to your app.
2. Open the **Expression editor** for the **Source** property.
   :::note
   Image controls accept the `IResource` data types. To reference a new `IResource` object, enter the following expression in the **Source** field: assignment
   ```
   new IResource("https://imageURL.png")
   ```
   :::
3. To bind the media file, use the following expression:
   ```
   Media.<file_name>
   ```