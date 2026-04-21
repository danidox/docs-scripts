---
title: "Disabling use of pre-signed URLs when uploading data to Amazon S3 storage"
visible: true
slug: "disabling-use-of-pre-signed-urls-when-uploading-data-to-amazon-s3-storage"
---

:::important
The information on this page is applicable to versions 2023.10.0, 2023.10.1, 2023.10.2, and 2023.10.3. Starting with version 2023.10.4, disabling the use of pre-signed URLs is handled via the global `disable_presigned_url` flag. See [Pre-signed URL configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#pre-signed-url-configuration).
:::
If you use Amazon S3 storage objects and you want to prevent users uploading data using a pre-signed URL, you can configure this in the `blob_storage_account_use_presigned_uri` setting in the `cluster_config.json` file.

By default, the `blob_storage_account_use_presigned_uri` setting is set to `true`. If you do not want users to upload data using a pre-signed URL, you can set the `blob_storage_account_use_presigned_uri` setting to `false`.

![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/275735)