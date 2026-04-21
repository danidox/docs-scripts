---
title: "Downloading a file using a URL"
visible: true
slug: "dlfilelink"
---

To download a file using a URL, follow these steps:

You should know the name of the file, and the storage bucket containing it for the download. The filename may either be obtained from a process, or located in the storage bucket in Orchestrator.

1. Before designing your app, go to **Orchestrator.** Access the storage bucket containing the file you want to download. Copy the name of the file.
2. Go to the app where you want to use this feature.
3. Add a new **App variable**, of the type **AppsFile**. Name it.
4. On the **MainPage,** add a new **Label** control and configure it:
   1. Rename the **Label** control to "Download file", including quotation marks.
   2. Click the **Style** tab of the **Label** control. Change the style of the **Label** control. This will help the user identify the link as a downloadable. We recommend using italics and blue.
5. Switch to the **Events** section of the **Download file** control. Click the **Create rule** button**.**
6. Add a new **Download file from Storage bucket** rule. Configure it:
   1. Click on the **Storage bucket** field. In the newly opened **Resources** menu, add the storage bucket containing the file you want to download into the field.

   ![docs image](/images/apps/apps-docs-image-399363-603b0a48.webp)
   2. In the **File name** field, paste the name of the file from step 1. Surround the name and its extension with quotation marks. For example, "[file_name].png".
   3. Click on the **Assign file to app variable** field. Select the app variable you added in step 3. Add the variable to the field.

   ![docs image](/images/apps/apps-docs-image-399387-f05005d1.webp)
7. In the **When completed** section, add a **Set Values** rule.
8. In the **Items to set** field, type `[variable_name].Name`.
   1. Set the downloaded file name inside the **Value** field. This will update the file name once the file is downloaded.
9. In the **When completed** section, add a new **Open Url** rule.
   1. In the **Url** field of the rule, type `[variable_name].Url`.

When you click on the **Download file** in runtime, the file is downloaded in a new tab.