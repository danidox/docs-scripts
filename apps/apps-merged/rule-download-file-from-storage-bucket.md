---
title: "Rule: Download File From Storage Bucket"
visible: true
slug: "rule-download-file-from-storage-bucket"
---

Use the **Get file from Storage bucket** to download a specified file from the indicated Orchestrator storage bucket.

![docs image](/images/apps/apps-docs-image-294985-23ab21d7.webp)

## Storage bucket

Clicking the **Storage bucket** field opens the **Resources** panel, which displays the available Orchestrator storage buckets.

Select the storage bucket you want to download from by double-clicking on it.

## File Name (with extension)

Use the **Expression editor** to reference the name of the file in the storage bucket you want to download.

## Assign file to app variable

Optionally, you can assign the downloaded file to a variable, for further reference in your app.

Clicking the **Assign file to app variable** field opens the **Resources** panel, which displays the available Apps variables, or allows you to create a new variable right away.

Select the variable you want to use by double-clicking on it.

## When completed

In this section you can define rules to be executed after the downloading of the file completes.

**For example:** After the file is successfully downloaded, you want to pass the file details to an entity.

## Errors

In this section you can define rules to be executed when the downloading of the file encounters an error.

**For example:** To track the failure, you can add a **Show Message** rule. You can then specify the title, message, and type of the error.

## Rule output properties

* **Error -** references the error message shown if the job fails.