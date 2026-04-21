---
title: "File Uploader"
visible: true
slug: "file-uploader"
---

UiPath Apps now support the **IResource** format for file handling.

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

* **Max file size** - The maximum file size users can upload. The recommended maximum file size is 10 MB.
* **Allowed file types** - The file types users can upload. Use "`,`" to separate file extensions. For example, if you write `.jpg, .png, .svg`, only these file types are allowed to be uploaded. The `.` symbol is not mandatory when listing the file types.
* **Helper text** - The help text to be displayed at runtime.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Label -** The display text of the control.
* **Required** - If true, app users must provide data in the control. To mark the control as mandatory at runtime, an asterisk `*` is added after the label text.
* **Custom error message** - The text to be displayed if the **Required** property is set to true and the control is left empty.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.
  :::note
  * The **File Uploader** control can upload only one file at a time.
  * Apps in a mobile browser do not support native camera-based photo uploads. Instead, save the photo to your device, then upload
  the saved file using the File Uploader control.
  :::

## Events

* **File added** - Configure what happens when a file is added.
* **File removed** - Configure what happens when a file is removed.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::

* **Label Placement** - By default, the label is set to be displayed on top of the control, at the left side. You can place it to the left of the control, on the same line. The **Label Width** property configures how wide the label should be, and the **Space between** property sets the distance between the label and the control.
* **Font** - The font attributes for both the label and the input text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...).

## Using File Uploader

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

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **File Uploader**. |
| `Label` | String | The label of the **File Uploader**, typically text displayed preceding the control. |
| `Value` | `IResource` | Name of the currently uploaded file. |
| `Required` | Boolean | Specifies if the file upload is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the file upload is required, but was not provided. |
| `Hidden` | Boolean | Determines the visiblity of the **File Uploader** control. If set to true, hides the control at runtime. |
| `Disabled` | Boolean | Determines if the **File Uploader** control is interactable. If set to true, disables interaction with the **File Uploader** at runtime. |
| `IsValid` | Boolean | Checks validity of the **File Uploader value**. If true, indicates it is valid. |