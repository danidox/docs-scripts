---
title: "Managing App Versions"
visible: true
slug: "publishing-a-new-version-of-an-app"
---

Publishing an app is the action of creating a new version of the app in the selected tenant. When you publish, the following changes happen in the backend:

* A new app version is generated from the current state, within the cloud tenant where the app was published.
* The version history table is updated with a new line showing:
  + who published the new version
  + when the app was published
  + the tenant to which the app was published
* Any changes to permissions are updated.

## Publishing a New Version of an App

1. Click the **Publish** button in the UiPath Apps Studio header.
2. [Optional] Add a description of what has changed in the new version.
   :::note
   Make sure you are publishing to the proper tenant by checking the publishing dialog. ![docs image](/images/apps/apps-docs-image-305207-ded2596f.webp)
   :::
3. Click **Publish**.
4. A toast notification will appear stating that the publishing has started.
5. A second toast notification will appear when the publishing has completed.
6. [Deploy your app to an Orchestrator folder.](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-apps#deploying-apps)
   :::note
   Once deployed, you can find and run your app from the **Run** tab. You can also share the app with specific users. Make sure the users you want to share the app with are assigned to the same folder where the app was deployed.
   :::

## Managing Version History

1. Navigate to the version history window by clicking on the **Version History** ![docs image](/images/apps/apps-docs-image-Version_History_icon-2657a19e.png) icon at the top of the right-hand panel.
2. Hover over the text bubble ![](/images/apps/apps-image-History_bubble-e8d1d64f.png) icon of each version to check the comments if available.

   ![docs image](/images/apps/apps-docs-image-92828-d75acd25.webp)
3. Click on the three-dot icon ![](/images/apps/apps-image-More_VT-dba43f67.png) next to a version for more options. 3.1 Select **Duplicate app** to create a copy of the selected version of the app. 3.2 Select **Export as file** to export the selected version of the app. 3.3 Select **Restore to this version** to go back to the selected version of the app.

   ![docs image](/images/apps/apps-docs-image-91536-3bde5b73.webp)

## Apps in folders for on-premises Orchestrator instances

With Apps in folders, the integration of Apps with on-premises Orchestrator remains unchanged, despite the fact that [apps are always published to a cloud Orchestrator tenant](https://docs.uipath.com/apps/automation-cloud/latest/release-notes/june-2023#14-june-2023).

After publishing, you need to [deploy the app in an Orchestrator folder](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-apps#deploying-apps). The folder must be in the same tenant where you published the app. This generates a production URL that you can use to share your app with specific users.

Users you want to share your app with must be assigned to the same folder where the app was deployed and must have **View** permissions on **Apps**.

Apps users can continue to add processes, queues, or storage buckets that reside in on-premises Orchestrator. The only change is the publishing location of the app, which now utilizes the tenant of a cloud Orchestrator instance.

:::note
Deployment, version, and permission management for published apps is done through a cloud Orchestrator instance.
:::