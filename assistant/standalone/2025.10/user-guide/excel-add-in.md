---
title: "UiPath Assistant for Excel add-in"
visible: true
slug: "excel-add-in"
---

The UiPath Assistant for Excel add-in allows you to use UiPath Assistant capabilities in the native Excel application. This provides an easy way to run, manage, and configure Excel-specific automations without having to switch between applications.

![docs image](/images/assistant/assistant-docs-image-273097-d0e81852.webp)

## Prerequisites

* UiPath Assistant 2023.4.2 or higher connected to Orchestrator with an attended license.
* At least one automation with the `excelAddin` tag or created with the "UiPath Assistant for Excel Process" Studio Template.
* Microsoft Excel 2016 or higher, or Microsoft 365 Excel online.
:::note
The UiPath Assistant for Excel Add-in does not currently support Excel for **macOS** or non-chromium based browsers when used in Excel online.
:::

## Installing the add-in

The UiPath Assistant for Excel add-in can be installed directly from the Microsoft Store, or using a manifest file to manually add it on your machine or deploy it to multiple machines it in your environment.
:::important
The Microsoft store always provides the latest version of UiPath Assistant for Excel add-in, which can break compatibility with older versions of the UiPath Assistant. Because of this, installing the add-in from the Microsoft store is recommended exclusively for Community users. For Enterprise users, we recommend deploying the add-in using the manifest file to ensure compatibility.
:::

### Using the manifest file

#### In Excel Desktop

The add-in is enabled through the manifest file using a process called "Side-Loading". This is done based on the steps below:

1. Download the manifest file from the **Product Downloads** section in [Customer Portal](https://customerportal.uipath.com/product-downloads).
2. Follow the steps described in the [Microsoft documentation](https://learn.microsoft.com/en-us/office/dev/add-ins/testing/create-a-network-shared-folder-catalog-for-task-pane-and-content-add-ins) on this topic.
3. In Excel, go to the **Insert** tab, and click **My Add-ins**, select **Shared Folder**, click on the **UiPath** tile, and select **Add**. A new tab called **UiPath** appears on the Microsoft Excel toolbar.
4. Select the **UiPath** tab -> **Find Automations** to see the UiPath Assistant for Excel add-in.

#### In Excel Online

1. In Excel Online, open a spreadsheet, then go to the **Home** tab.
2. Click **Add-ins** > **My Add-ins**.
3. Click **Upload my Add-ins**, and browse to the manifest file.

#### Admin deployment

1. Download the manifest file from the **Product Downloads** section in [Customer Portal](https://customerportal.uipath.com/product-downloads).
2. In a cloud deployment environment, you can deploy the add-in to your organization by using the [Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/admin-overview/admin-center-overview?view=o365-worldwide). Read more about using [Integrated Apps](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/test-and-deploy-microsoft-365-apps?view=o365-worldwide) or [Centralized Deployment](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins?view=o365-worldwide).
:::note
When the add-in is loaded for the first time, the latest version available is used. Once the connection with the UiPath Assistant is created, the add-in version syncs to the Assistant one.
:::

### From the Microsoft Store

1. Access [this link](https://appsource.microsoft.com/en-us/product/office/WA200005457?flightCodes=UiPathAssistantExcel) and select **Get it now**.
:::note
You need to be signed in to Microsoft Store to complete the download.
:::
Alternatively, you can add the UiPath Assistant for Excel add-in directly from the **Get Add-ins** section in the Excel application.

To do this, follow the steps below:

1. In Microsoft Excel (both desktop and online), open a spreadsheet, then go to the **Insert** tab.
2. Click **Get Add-ins,** enter the `WA200005457` ID in the search box, and click **Add.**

## Logging in

When you open the UiPath Assistant for Excel add-in for the first time, if Assistant is not running, you are prompted to launch it.

If you are not logged in the UiPath Assistant, or if no automations are available, make sure you are connected to Orchestrator with a valid attended license, and you have at least one automation that has the **excelAddin tag** deployed for your account.

## Creating automations using the template

To create an automation for the UiPath Assistant for Excel, use the dedicated Studio template with the same name. This template features the `excelAddin` tag and two input arguments (`in_FilePath` and `in_Selection`) that populate at runtime, making it easier to pass data between Excel and the automation. Since these automations have the `excelAddin` tag, they are automatically added to the UiPath Assistant for Excel add-in once published.

You can also create your own automations, making sure that they have the `excelAddin` tag. To benefit from either of those input arguments, they need to be created/used inside the workflow.

When the `in_FilePath` and `in_Selection` input arguments are present in an automation created for the add-in, they are automatically populated as follows:

* `in_FilePath` (String) - represents the file path from which the add-in is starts the process.
* `in_Selection` (String) - represents the cell/cells selected when the process is starting.

The `in_Selection` variable uses the `[Sheet]![Range]` schema, meaning that if you need to use different selections for different sheets, you can create separate variables to be used as values for each sheet or range. TOPLEVELNOTEMARKER
  :::note
  If you need more selections, create additional input arguments, new range variables, and new sheet variables if your selection is from a different sheet. Afterward, you can drag and drop the Parse Excel selection workflow into your main sequence and import the newly created arguments and variables.
  :::