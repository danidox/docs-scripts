---
title: "Publishing, deploying, and upgrading app
         projects"
visible: true
slug: "publishing-deploying-upgrading-app-projects"
---

## Publishing app projects

To publish an app project:

1. Select the **Publish** button at the top of the project designer.
2. In the **Publish automation** window, enter a name and a description for your automation, and select a version.
3. Select **Publish**.

You can then access your published app after deploying it in Orchestrator.

:::note
* App projects can only be published to
the **Orchestrator Tenant Processes Feed**, not to the **Orchestrator Personal Workspace Feed**.
* To publish an app project, you need to
have tenant-level permissions to create packages. To learn more, refer to [App permissions](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-apps#apps-permissions) in the Orchestrator guide.
:::

## Deploying app projects

To deploy a published app project, navigate to Orchestrator and:

1. Select the Orchestrator folder where you want to deploy your project.
2. Select **Automations**, and then open the **Apps** page. Here you can see each app project's name, version, description, and its associated process. You can also select the project name under the **App project** column to open the app in Studio Web.
3. Select **Deploy app**.
4. From the **App** drop-down menu, choose the app project you want to deploy, as well as the version from the **Version** column, then select **Deploy**. Your published app project is now deployed in the selected folder.

After deployment, your app appears under the **Apps** column.

See the Orchestrator guide for more information on [deploying app projects](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-apps) and [managing processes](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-processes#used-applications).

   ![docs image](/images/studio-web/studio-web-docs-image-486774.webp)

:::note
* The recommended **Cloud Robot -
Serverless** configuration for apps in Studio Web is **Medium**. You can change this setting from the **Processes** page, or while deploying your app.
:::

## Upgrading app projects

When you publish a new version of an app project, an **Updates are available** icon appears under the **Version** column in Orchestrator. To upgrade your published project:

1. Click the button on the right of the project.
2. Click **Upgrade to latest version**.
3. In the new window, select **Upgrade**.

   ![docs image](/images/studio-web/studio-web-docs-image-486832.webp)

Upgrading a deployed app project works in a similar way:

1. Locate the project in your Orchestrator folder (under **Automation**s &gt; **Processes &gt;****Apps**).
2. Select the button to the right of the process and select **Upgrade to latest version**.
3. In the **Update package version** window, select the **Confirm** button.

## Removing app projects

To remove a published app project:

1. Locate the project in your Orchestrator folder (under **Automation**s &gt; **Apps**).
2. Click the button on the right of the project and select **Remove**.
3. Select **Delete** in the resulting window.
   :::important
   Deleting an app project also deletes all the workflows used in the project. Do not delete the workflows used in your app project, as this causes errors. If you delete a workflow by accident, you can remove the app project and deploy it again.
   :::