---
title: "April 2024"
visible: true
slug: "april-2024"
---

## 24 April 2024

### Extract part of a workflow as a new workflow file

To help break down a large project into smaller components, you can now extract an activity or a sequence of activities as separate workflows using the new **Extract as Workflow** option from the **Actions** ![docs image](/images/sw/release-notes-docs-image-More_VT.png) menu. For more information, refer to .

![Extract workflow](/images/sw/release-notes-extract-workflow-386881.webp)

### Duplicate workflow files in the Project explorer

You can now duplicate workflow files by right-clicking an existing workflow in the **Project explorer** and selecting **Duplicate**. The name of the new workflow is the name of the workflow you duplicated followed by `1`. The new workflow contains the same activities and their respective properties as the original workflow.

### Download Studio and Assistant from Studio Web

You can now download Studio and Assistant directly from Studio Web by using the new **Install** button in the Templates and Projects pages.

![docs image](/images/sw/release-notes-docs-image-398279.webp)

### Improved Orchestrator error messages

Error messages now explicitly mention Orchestrator if an error is caused by Orchestrator.

![Orchestrator error message](/images/sw/release-notes-orchestrator-error-message-397933.webp)

### Recent activities updates

The following categories of activities are now in general availability:

* [Amazon Connect](https://docs.uipath.com/activities/other/latest/integration-service/uipath-amazon-connect-activities)
* [Amazon SES](https://docs.uipath.com/activities/other/latest/integration-service/uipath-amazon-ses-activities)
* [AWeber](https://docs.uipath.com/activities/other/latest/integration-service/uipath-aweber-aweber-activities)
* [Constant Contact](https://docs.uipath.com/activities/other/latest/integration-service/uipath-constantcontact-constantcontact-activities)
* [Drip](https://docs.uipath.com/activities/other/latest/integration-service/drip-activities)
* [Facebook](https://docs.uipath.com/activities/other/latest/integration-service/uipath-meta-facebook-activities)
* [Intercom](https://docs.uipath.com/activities/other/latest/integration-service/uipath-intercom-intercom-activities)
* [Keap](https://docs.uipath.com/activities/other/latest/integration-service/uipath-keap-keap-activities)
* [LinkedIn](https://docs.uipath.com/activities/other/latest/integration-service/uipath-microsoft-linkedin-activities)
* [Mailgun](https://docs.uipath.com/activities/other/latest/integration-service/uipath-sinch-mailgun-activities)
* [PDFMonkey](https://docs.uipath.com/activities/other/latest/integration-service/uipath-pdfmonkey-pdfmonkey-activities)
* [Shopify](https://docs.uipath.com/activities/other/latest/integration-service/uipath-shopify-shopify-activities)
* [TangoCard](https://docs.uipath.com/activities/other/latest/integration-service/uipath-tangocard-tangocard-activities)
* [Workable](https://docs.uipath.com/activities/other/latest/integration-service/uipath-workable-workable-activities)
* [YouTube](https://docs.uipath.com/activities/other/latest/integration-service/uipath-google-youtube-activities)

The following categories of activities have received updates:

* [Document Understanding (v2.4.2)](https://docs.uipath.com/activities/other/latest/document-understanding/release-notes-document-understanding-activities)
* [Google Workspace](https://docs.uipath.com/activities/other/latest/productivity/release-notes-uipath-gsuite-activities) (v2.5.10)
* [System (v24.3.1)](https://docs.uipath.com/activities/other/latest/workflow/release-notes-uipath-system-activities)
* [UI Automation (v23.10.11)](https://docs.uipath.com/activities/other/latest/ui-automation/release-notes-uipath-uiautomation-activities-v23-10)
* [WebAPI (v1.20.1)](https://docs.uipath.com/activities/other/latest/developer/release-notes-uipath-web-activities)

The following categories of activities are now available in preview:

* [Deputy](https://docs.uipath.com/activities/other/latest/integration-service/uipath-deputy-deputy-activities)
* [Egnyte](https://docs.uipath.com/activities/other/latest/integration-service/uipath-egnyte-egnyte-activities)
* [Insightly CRM](https://docs.uipath.com/activities/other/latest/integration-service/uipath-insightly-insightly-activities)
* [Zoho Campaigns](https://docs.uipath.com/activities/other/latest/integration-service/uipath-zoho-campaigns-activities)
* [Zoho Mail](https://docs.uipath.com/activities/other/latest/integration-service/uipath-zoho-mail-activities)

## 5 April 2024

### New ways to link multiple workflow files

It's now easier to link multiple workflow files to another workflow. Simply drag the workflow you want to link from the **Project explorer** and drop it in your project or use the new **Invoke in current workflow** Project explorer menu option. For more information, see .

  ![docs image](/images/sw/release-notes-docs-image-386829.webp)

### Navigate to an activity that caused an error

Clicking on an error message in the takes you to the activity that caused the error, selecting it.

### Improved Invoke Workflow File names

The default name of the [Invoke Workflow File](https://docs.uipath.com/activities/other/latest/workflow/invoke-workflow-file) activity will automatically update when selecting a workflow file.

### Improvements

* The default timeout for running a workflow has increased from 15 minutes to 30 minutes.
* You can now select a variable before assigning its value in the [Set Variable Value](https://docs.uipath.com/activities/other/latest/workflow/assign) activity.
* The **Expression Editor** ![docs image](/images/sw/release-notes-docs-image-386296.webp) button now only appears when hovering over incompatible variable types in the **Use Variable** window.

### Recent activities updates

The following categories of activities are now in general availability:

* [Adobe Acrobat Sign](https://docs.uipath.com/activities/other/latest/integration-service/uipath-adobe-sign-activities)
* [Amazon Polly](https://docs.uipath.com/activities/other/latest/integration-service/uipath-amazon-polly-activities)
* [Amazon Transcribe](https://docs.uipath.com/activities/other/latest/integration-service/uipath-amazon-transcribe-activities)
* [Calendly](https://docs.uipath.com/activities/other/latest/integration-service/calendly-activities)
* [Citrix ShareFile](https://docs.uipath.com/activities/other/latest/integration-service/uipath-citrix-sharefile-activities)
* [Customer.io](https://docs.uipath.com/activities/other/latest/integration-service/uipath-customerio-customerio-activities)
* [Datadog](https://docs.uipath.com/activities/other/latest/integration-service/uipath-datadog-datadog-activities)
* [Eventbrite](https://docs.uipath.com/activities/other/latest/integration-service/uipath-eventbrite-eventbrite-activities)
* [Expensify](https://docs.uipath.com/activities/other/latest/integration-service/uipath-expensify-expensify-activities)
* [GetResponse](https://docs.uipath.com/activities/other/latest/integration-service/uipath-getresponse-getresponse-activities)
* [Google Text-to-Speech](https://docs.uipath.com/activities/other/latest/integration-service/uipath-google-texttospeech-activities)
* [Greenhouse](https://docs.uipath.com/activities/other/latest/integration-service/uipath-greenhouse-greenhouse-activities)
* [Hootsuite](https://docs.uipath.com/activities/other/latest/integration-service/uipath-hootsuite-hootsuite-activities)
* [Klaviyo](https://docs.uipath.com/activities/other/latest/integration-service/uipath-klaviyo-klaviyo-activities)
* [MailerLite](https://docs.uipath.com/activities/other/latest/integration-service/uipath-mailerlite-mailerlite-activities)
* [Miro](https://docs.uipath.com/activities/other/latest/integration-service/uipath-miro-miro-activities)
* [PayPal](https://docs.uipath.com/activities/other/latest/integration-service/uipath-paypal-paypal-activities)
* [Quip](https://docs.uipath.com/activities/other/latest/integration-service/uipath-salesforce-quip-activities)
* [Trello](https://docs.uipath.com/activities/other/latest/integration-service/uipath-trello-trello-activities)
* [WooCommerce](https://docs.uipath.com/activities/other/latest/integration-service/uipath-automattic-woocommerce-activities)
* [Zoominfo](https://docs.uipath.com/activities/other/latest/integration-service/uipath-zoominfo-zoominfo-activities)

The following categories of activities have received updates:

* [Google Workspace](https://docs.uipath.com/activities/other/latest/productivity/release-notes-uipath-gsuite-activities) (v2.5.9)
* [Microsoft 365](https://docs.uipath.com/activities/other/latest/productivity/release-notes-microsoftoffice365-activities) (v2.5.9)

The following categories of activities are now available in preview:

* [Amazon Connect](https://docs.uipath.com/activities/other/latest/integration-service/uipath-amazon-connect-about)
* [Amazon SES](https://docs.uipath.com/activities/other/latest/integration-service/uipath-amazon-ses-activities)
* [AWeber](https://docs.uipath.com/activities/other/latest/integration-service/uipath-aweber-aweber-activities)
* [Discord](https://docs.uipath.com/activities/other/latest/integration-service/uipath-discord-discord-activities)
* [Intercom](https://docs.uipath.com/activities/other/latest/integration-service/uipath-intercom-intercom-activities)
* [LinkedIn](https://docs.uipath.com/activities/other/latest/integration-service/uipath-microsoft-linkedin-activities)
* [PDFMonkey](https://docs.uipath.com/activities/other/latest/integration-service/uipath-pdfmonkey-pdfmonkey-activities)
* [TangoCard](https://docs.uipath.com/activities/other/latest/integration-service/uipath-tangocard-tangocard-activities)
* [Workable](https://docs.uipath.com/activities/other/latest/integration-service/uipath-workable-workable-activities)