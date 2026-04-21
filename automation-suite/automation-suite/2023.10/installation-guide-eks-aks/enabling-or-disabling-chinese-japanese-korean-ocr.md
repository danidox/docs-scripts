---
title: "Enabling or disabling Chinese, Japanese, Korean OCR"
visible: true
slug: "enabling-or-disabling-chinese-japanese-korean-ocr"
---

If you want to use the **OCR for Chinese, Japanese, Korean** endpoint in an offline environment, you need to install the offline bundle and once the bundle is installed, you have to enable the OCR. For more information on how to install offline bundles, check the [ML packages offline installation](https://docs.uipath.com/document-understanding/automation-suite/2023.4/classic-user-guide/ml-packages-offline-installation) page from the **Document Understanding User Guide**.

:::note
* When **OCR for Chinese,
Japanese, Korean** is used in Document Understanding, make sure that you configured the activity with the public endpoint of the OCR, and the Document Understanding API Key.
* **OCR for Chinese, Japanese,
Korean** is only supported in Document Understanding deployed in Automation Suite. This is not supported in Document Understanding deployed in AI Center connected to an external Orchestrator.
:::

There are two ways in which you can enable the **Chinese, Japanese, Korean OCR**:

* Using ArgoCD.
* Using the `cluster_config.json` file.
  :::note
  You can only enable the **Chinese, Japanese, Korean OCR** using `cluster_config.json` starting with Automation Suite version 2023.4.11.
  :::

## Using ArgoCD

1. Open ArgoCD.
2. Open the Document Understanding framework.
3. Select the **Parameters** tab.
4. Navigate to `du-cjk-ocr.enabled`.
5. Select **Edit** and set the value to `TRUE`.
6. Select **Save**.
   :::note
   The endpoint for **OCR for Chinese, Japanese, Korean** in an Automation Suite installation is constructed as `{Cluster_FQDN}/du_/cjk-ocr/`.
   :::

## Using the cluster_config.json file

:::note
This procedure is only available starting with Automation Suite version 2023.4.11. For version older than 2023.4.11, you can only enable the Chinese, Japanese, Korean OCR using ArgoCD.
:::

1. After installing or upgrading Automation Suite, configure the `input.json` file.
2. Add the string for Chinese, Japanese, Korean OCR in the `input.json` file.
3. If the `documentunderstanding` object is not yet configured, you can use the following code to add it:
   ```
   "documentunderstanding": {
       "enabled": true,
       "cjkOcr": {
         "enabled": true,
       }
     },
   ```
   :::note
   If the `documentunderstanding` object is already configured, copy only the `cjkOcr` property without changing any other properties.
   :::
4. Execute the Automation Suite installer again using the following command:
   ```
   uipathctl manifest apply input.json --versions versions.json
   ```
5. Go to the ArgoCD panel, in the Document Understanding section and check if the Chinese, Japanese, Korean OCR is displayed.