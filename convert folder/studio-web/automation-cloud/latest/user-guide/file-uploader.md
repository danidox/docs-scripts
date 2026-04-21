---
title: "File Uploader"
visible: true
slug: "file-uploader"
---

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

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **File Uploader**. |
| `Label` | String | The label of the **File Uploader**, typically text displayed preceding the control. |
| `Value` | `AppsFile` | Name of the currently uploaded file. |
| `Required` | Boolean | Specifies if the file upload is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the file upload is required, but was not provided. |
| `Hidden` | Boolean | Determines the visiblity of the **File Uploader** control. If set to true, hides the control at runtime. |
| `Disabled` | Boolean | Determines if the **File Uploader** control is interactable. If set to true, disables interaction with the **File Uploader** at runtime. |
| `IsValid` | Boolean | Checks validity of the **File Uploader value**. If true, indicates it is valid. |

## Using the File Uploader

This example shows how you can use the **File Uploader** with a storage bucket.

1. Open an existing app, or create a new one.
   1. Add a **File Uploader** control.
   2. Add a variable to your app and specify its type as **AppsFile.**
   3. Select **Events.** In **File added,** select **Define automation.**
2. Add an **Upload Storage File** activity to your workflow.
   1. Specify the Orchestrator folder path and the storage bucket name.
   2. In **Where to upload,** select the variable you added in step 1b.
   3. Select the **File** field, then the **Additional resources** button.
   4. Select **Expression editor,** then add the following expression: `Controls.MainPage.FileUploader.Value.ToLocalResource`
3. Test or run your app.

When you run the app and add a file in **File Uploader,** the app uploads the storage file to the storage bucket.