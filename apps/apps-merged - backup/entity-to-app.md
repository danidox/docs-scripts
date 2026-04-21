---
title: "Using an entity to generate an app"
visible: true
slug: "entity-to-app"
---

## Prerequisites

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::
To use Autopilot in Apps, your tenant must have sufficient Autopilot actions available.

To generate an app using a Data Service entity, follow these steps:

1. Go to the Apps homepage.
2. Select the **App from entity** option.
3. In the dropdown menu, select the entity you want to use.
4. Once the text field is completed automatically, select **Send** to begin the app generation process**.** The app generation process immediately begins.

Autopilot creates an app which submits data to your entity and generates the respective fields. The generated app contains:

* A main page with a page container
* A second page bound to the page container of the main page (this contains the form fields and input fields)
* A **Submit** button
* An entity mapped to your form's data schema
* A `CreateEntityRecord` rule bound to the Submit button and with its fields bound to the corresponding input controls