---
title: "Using a text prompt to generate an app"
visible: true
slug: "text-to-app"
---

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::

To generate an app using a text prompt, follow these steps:

1. Create a new app, and select the **Generate with Autopilot** text field.
   :::note
   App generation using a text prompt works best if the prompt is in the same language as the selected language in Automation Cloud.
   :::
2. Write or paste text into the field to build your prompt. The minimum text input is 20 characters. Your prompt should describe the use case of the intended form, for example: "An app that allows me to onboard new employees into my system", or "An app that lets me register for a dance competition".
   :::note
   If you do not want your app to contain an entity, clear the **Create entity** checkbox.
   :::
3. Select the **Send** button to begin the app generation process. The app generation process immediately begins.

Once the process is complete, the generated app displays immediately.
:::note
The generated app typically contains:
* A main page with a page container.
* A second page bound to the page container of the main page (this contains the form fields and input fields).
* A **Submit** button.
* An entity mapped to your form's data schema.
* A `CreateEntityRecord` rule bound to the Submit button and with its fields bound to the corresponding input controls.
:::