---
title: "Downloading a file using an Image control"
visible: true
slug: "dlfileimgctrldraft"
---

You should know the name of the file, and the storage bucket containing it for the download. The filename may either be obtained from a process, or located in the storage bucket in Orchestrator.

You can use the following image formats for this procedure:

* JPEG
* PNG
* BMP
* GIF
* SVG
1. Before designing your app, go to **Orchestrator.** Access the storage bucket containing the file you want to download. Copy the name of the file.
2. Go to the app where you want to use this feature.
3. Add a new **App variable** of the type **AppsFile.** Name it.
4. From the **MainPage,** click the **Events** tab. Click the **Create rule** button.
5. Add a new **Download file from Storage bucket** rule to the page's **Loaded** event.
6. Configure the **Download file from Storage bucket** rule:
   1. Click on the **Storage bucket** field. In the newly opened **Resources** menu, add the storage bucket containing the file you want to download into the field.

   ![docs image](/images/apps/apps-docs-image-399363-603b0a48.webp)
   2. In the **File name** field, paste the name of the file from step 1. Surround the name and its extension with quotation marks. For example, "[file_name].png".
   3. Click on the **Assign file to app variable** field. Select the app variable you added in step 3. Add the variable to the field.

   ![docs image](/images/apps/apps-docs-image-399387-f05005d1.webp)
7. Return to the **MainPage.** Click on **Add control,** and select **Display.** Add an **Image** control to your app.
8. In the **General** properties of the **Image** control, click on the **Source** field. Add the variable name specified in step 3 to the **Source** field**.**

   ![docs image](/images/apps/apps-docs-image-399395-b816353e.webp)

The image is rendered in the image control.