---
title: "Uploading and downloading a file using the File Uploader control"
visible: true
slug: "uploading-and-downloading-a-file"
---

This example shows how you can use **File Uploader** with a storage bucket and with a file field of an entity.

1. In your app, add a Storage Bucket and a Data Service entity that has file fields.
2. Add a **File Uploader** and a **Button** control.
3. Create a variable of type `IResource` and name it "SB_file_var'. Use this variable to store the file downloaded from the storage bucket.
4. Add the **Upload file to Storage Bucket** rule to the **Clicked on** event of the button control.
   1. In the **File to upload** field, reference the file uploaded through the **File Uploader** control, as follows:
      ```
      MainPage.FileUploader.Value
      ```
   2. In the **Storage bucket** field, reference the Orchestrator storage bucket that you previously added to your app.
   3. Optionally, in the **When completed** field, you can add a **Show Message** rule to inform you the uploading completed successfully.
5. Add the **Download file from Storage Bucket** rule to the **Clicked on** event of the button control.
   1. In the **Storage bucket** field, reference the Orchestrator storage bucket that you previously added to your app.
   2. In the **File Name (with extension)** field, write the name of the file your users should download.
   3. In the **Assign file to app** variable, reference the previously created variable "SB_file_var".
   4. Optionally, in the **When completed** field, you can add a **Show Message** rule to inform you the downloading completed successfully.
6. Add a **Label** control to your app.
   1. In the Text field of the control, reference the name of the downloaded file, as follows:
      ```
      SB_file_var.Name
      ```
      - where "SB_file_var" is the variable used to store data about the downloaded file.
7. Run your app and upload a file using the **File Uploader** control. Click the button.

A success message should appear at the top of your screen informing you the upload/download completed successfully. Now check the storage bucket in Orchestrator and you should see the file you uploaded using the **File uploader** control.

Simultaneously, clicking the button downloaded the file indicated in the **Download file from Storage Bucket** rule to your local device and stored its data to a variable. The **Label** control displays the name of the downloaded file.