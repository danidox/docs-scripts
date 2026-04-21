---
title: "Using a PDF or image to generate an app"
visible: true
slug: "pdf-or-image-to-app"
---

## Prerequisites

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::

To use Autopilot in Apps, your tenant must have sufficient Autopilot actions available.

To create an app using PDFs or images in Autopilot for Apps, you must have Document Understanding enabled in your active Tenant, as well as sufficient AI units.

To generate an app using a PDF or image, follow these steps:

1. Create a new app, then select the attachment icon (paperclip) inside the **With Autopilot** text field.
   :::note
   If you do not want your app to contain an entity, clear the **Create entity** checkbox.
   :::
2. Attach any PDF or image which meets the following requirements:
   * A minimum resolution of of 50 x 50 pixels.
   * A maximum resolution of 10,000 x 10,000 pixels.
   * Text should be clearly readable so the generative AI can digitize it.
   * PDFs exceeding 3,500 characters may not be processed by the model.
   * Keep in mind that there may be differences between the original file and the form digitized by Autopilot.
3. Select the **Send** button to begin the app generation process. The app generation process immediately begins.

Once the process is complete, the app is displayed immediately.
:::note
The generated app contains:
* A main page with a page container
* A second page bound to the page container of the main page (this contains the form fields and input fields)
* A **Submit** button
* An entity mapped to your form's data schema
* A CreateEntityRecord rule bound to the Submit button and with its fields bound to the corresponding input controls
:::