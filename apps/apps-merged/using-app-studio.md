---
title: "Using App Studio"
visible: true
slug: "using-app-studio"
---

**UiPath Apps** is available on the left-hand sidebar of the UiPath Portal.

The **Apps** home page is divided into two tabs, **Build** and **Run**, which split the existing applications as follows:

* On the **Build** tab you can create new apps and search among apps that you can edit.

To edit an app, you need to be the owner or the [co-author](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/permission-management#managing-permissions-at-app-level) of that app.

  ![docs image](/images/apps/apps-docs-image-266089-e9bc3bb7.webp)
* On the **Run** tab you can run and search among:
  + Apps that were [deployed to Orchestrator folders](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-apps#deploying-apps) where you have **View** permissions on **Apps.**
    :::note
    To run published apps, you need to [deploy them to an Orchestrator folder](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-apps#deploying-apps).
    :::
  + Existing published apps that do not belong to any tenant (that is, apps that were published before the introduction of the [Apps in folders feature](https://docs.uipath.com/apps/automation-cloud/latest/release-notes/june-2023#14-june-2023))

:::note
The apps displayed in the **Run** tab are specific to the selected tenant. Existing published apps that were shared with users or within a tenant can still be accessed by the users with the [proper roles](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/permission-management#managing-permissions-at-organization-level). After republishing the app to a tenant, the [folder-level permissions](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/permission-management#managing-permissions-at-folder-level) take precedence.
:::

  ![docs image](/images/apps/apps-docs-image-266093-5a90c0d1.webp)

:::note
If you have feedback, share it on the [UiPath Apps Forum](https://forum.uipath.com/c/engage/apps/170).
:::

## Creating a New App

1. On the **Build** tab, click the **Create new app** button.
2. Give the new app a name.
3. Click the **Create** button.

You can select a template for the first page or blank page.

   ![docs image](/images/apps/apps-docs-image-92220-750e3c21.webp)

## Adding Controls

1. Click the **Add new control** ![docs image](/images/apps/apps-docs-image-Add_New_Control_icon_new2-815e38db.png) icon from the top of the canvas.
2. Click the 'v' icon to expand each control section and locate the control you would like to add.
3. Click and drag the control to the desired location on the canvas.

   ![docs image](/images/apps/apps-docs-image-92264-45006790.gif)

## Adding Pages

1. Click the **Add any**![docs image](/images/apps/apps-docs-image-Add_Any_icon-1117ace3.png) icon from the top of the canvas.
2. Select [Page](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/page#page).

   ![docs image](/images/apps/apps-docs-image-91428-dd414185.webp)

The first page in this list is the first page to run when you launch your app. The ordering of subsequent pages doesn't have an impact on runtime, but you can re-arrange them to help keep your app organized. To set another page as the start page you can either:

* Right Click &gt; Set as Start Page.
* Or click and drag the page to reorder it.

## Styling Your Controls

App Studio provides visual presets for many controls to help accelerate your app development, but you can always drill into specific styling properties to customize your app in any way you want.

To change the style of a control:

1. Select the control on the canvas
2. Select the **Style** tab in the properties panel
3. Change individual styling properties to change the look and feel of your app

For more details about styling, see the [Controls Overview](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/controls#controls-overview)

   ![docs image](/images/apps/apps-docs-image-92276-fbcf6471.gif)

## Adding a Process

To add a process that is already in Orchestrator:

1. Click the **Add any**![docs image](/images/apps/apps-docs-image-Add_Any_icon-1117ace3.png) icon from the top of the canvas.
2. Select **Process**.

   ![docs image](/images/apps/apps-docs-image-94592-b4356afc.webp)
3. Choose an Orchestrator tenant that you have access to within your account.
4. Select the folder where you published your process.
5. Select the process(es) you want to include in your app.
6. Click **Add**.

For more details, see [Referencing a Process From Orchestrator](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/connecting-your-app-to-an-orchestrator-tenant#referencing-a-process-from-orchestrator).

## Adding a Storage Bucket

1. Click the **Add any**![docs image](/images/apps/apps-docs-image-Add_Any_icon-1117ace3.png) icon from the top of the canvas.
2. Select **Storage bucket**.

   ![docs image](/images/apps/apps-docs-image-91500-fffb15ea.webp)
3. Choose an Orchestrator tenant that you have access to within your account.
4. Select the folder where the storage bucket is located in.
5. Select the storage bucket(s) you want to include in your app.
6. Click **Add**.

For more details, see [Referencing a Storage Bucket From Orchestrator](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/referencing-a-storage-bucket-from-orchestrator#referencing-a-storage-bucket-from-orchestrator).

## Adding an Entity

1. Click the **Add any**![docs image](/images/apps/apps-docs-image-Add_Any_icon-1117ace3.png) icon from the top of the canvas.
2. Select **Entity**.

   ![docs image](/images/apps/apps-docs-image-92772-c7d4009b.webp)
3. Choose an Orchestrator tenant that you have access to within your account.
4. Select the folder where the entity is located in.
5. Select the entity(es) you want to include in your app.
6. Click **Add**.

For more details, see [Referencing an Entity in Your App](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/referencing-an-entity-in-your-app#referencing-an-entity-in-your-app).

## Adding a Queue

1. Click the **Add any**![docs image](/images/apps/apps-docs-image-Add_Any_icon-1117ace3.png) icon from the top of the canvas.
2. Select **Queue**.

   ![docs image](/images/apps/apps-docs-image-91804-c448cf60.webp)
3. Choose an Orchestrator tenant that you have access to within your account.
4. Select the folder where the entity is located in.
5. Select the entity(es) you want to include in your app.
6. Click **Add**.

For more details, see [Referencing a Queue in Your App](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/referencing-a-queue-in-your-app#referencing-a-queue-in-your-app).

## Data Binding

To bind your controls to process inputs or outputs, use their Value Binding field. For more details, see [Binding Process Inputs/Outputs Arguments](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/connecting-your-app-to-an-orchestrator-tenant#binding-process-inputs%2Foutputs-arguments).

   ![docs image](/images/apps/apps-docs-image-92916-092ba4e2.gif)

## Events and Logic

[Events and Rules](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/about-events-and-rules#about-events-and-rules) control the end-user experience inside of your app. The events available for a control are determined by the type of the respective control. For example, Pages have a **Loaded** event, while a textbox has a **Value Changed** event.

To customize interactions within your app:

1. Select the control that you would like to add an event to.
2. Click the **Events** tab on the properties pane.
3. Choose an event you'd like to customize and click **Create Rule**.
4. Start typing or select a rule from the available list.

For more, see [Events and Rules](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/about-events-and-rules#about-events-and-rules).

   ![docs image](/images/apps/apps-docs-image-91828-23ef2e59.gif)

## Preview and Publish

You can preview your app at any time during development by clicking the **Preview** button in the header. Check out the rest of the documentation to learn more about [Testing Apps](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/overview1#testing-apps) and [Managing App Versions](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/publishing-a-new-version-of-an-app#managing-app-versions).

After publishing, business users can launch the same app in multiple tabs simultaneously.

## Deploying apps in Orchestrator folders

After you publish the app, you need to [deploy it to an Orchestrator folder](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-apps#deploying-apps).

## Apps in folders and UiPath Assistant

After the introduction of the [Apps in folders](https://docs.uipath.com/apps/automation-cloud/latest/release-notes/june-2023#14-june-2023) feature, publishing an app does not display it in UiPath Assistant. To see newly published apps, you first need to deploy them in an Orchestrator folder. The minimum Assistant version that supports displaying and running deployed apps is 2023.4.4.

Apps published before the introduction of the Apps in folders feature continue to show up in all UiPath Assistant versions.

The following table summarize the compatibility between UiPath Apps cloud version and UiPath Assistant:

| UiPath Assistant version | Displays apps published before the [Apps in folders](https://docs.uipath.com/apps/automation-cloud/latest/release-notes/june-2023#14-june-2023) feature | Displays deployed apps |
| --- | --- | --- |
| 2023.4.4 and newer | Yes | Yes |
| Previous to 2023.4.4 | Yes | No |