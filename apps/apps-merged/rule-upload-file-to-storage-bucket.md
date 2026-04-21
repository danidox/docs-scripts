---
title: "Rule: Upload File to Storage Bucket"
visible: true
slug: "rule-upload-file-to-storage-bucket"
---

Use the **Upload file to Storage bucket** to upload a file to the indicated Orchestrator storage bucket.

![docs image](/images/apps/apps-docs-image-364725-ebece465.webp)

## File to upload

Use the **Expression editor** to reference the object of type AppsFile you want to upload to the storage bucket.

:::note
Uploading `.exe` files is restricted.
:::

## Storage bucket

Clicking the **Storage bucket** field opens the **Resources** panel, which displays the available Orchestrator storage buckets.

Select the storage bucket you want to upload to by double-clicking on it.

## Upload File Name (with extension)

The name used to identify the file in the storage bucket. You can either provide a name for your file, or opt for a unique, automatically generated name.

To generate a unique name for your file, select the **Auto-generate name** checkbox.

:::note
To prevent file overwrites, we recommend you to use the **Auto-generate name** feature.
:::

## When completed

In this section you can define rules to be executed after the uploading of the file completes.

**For example:** After the file is successfully uploaded, you want to start the process that sends the file name as an input argument to the process. The process then can download the file from the storage bucket and perform further operations.

## Errors

In this section you can define rules to be executed when the uploading of the file encounters an error.

**For example:** To track the failure, you can add a **Show Message** rule. You can then specify the title, message, and type of the error.

## Rule output properties

* **Error -** references the error message shown if the job fails.
* **UploadedFileName -** references the name of the uploaded file.