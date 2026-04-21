---
title: "Apps in Solutions Management"
visible: true
slug: "apps-in-solutions-management"
---

Apps in Solutions Management allows you to package folder apps into solution packages. You can deploy these solution packages to a different tenant, organization or environment.

Packaging an app into a solution even includes integrations and resources, such as storage buckets or entities. Once a solution is deployed, all resources are automatically created, and all integration references are automatically updated. You do not need to manually build any resources or update any integrations.

Key use cases for Apps in Solutions include the following:

* Deploying an app from a development environment to a production environment.
* Deploying upgrades or downgrades to an app,.
* Deploy changes to integrations and resources in your app.
* Maintaining consistency of the app URL across upgrades or downgrades.

For more details on managing solution deployments, refer to [the Solutions Management documentation.](https://docs.uipath.com/solutions-management/automation-cloud/latest/user-guide/solutions-management-overview)

## Packaging an app into a solution

Before beginning this tutorial, make sure:

* You have built your app.
* You have deployed the app to Orchestrator.
* You meet [the Solutions Management prerequisites](https://docs.uipath.com/solutions-management/automation-cloud/latest/user-guide/prerequisites).

To package an app into a solution, apply the following steps:

1. Go to Automation Ops, and select **New project.**
2. Give your project a name, then select **Continue.** The **Solutions builder** window opens automatically.
3. In the **Solutions builder** window, select the app resources you wish to include in your package.
4. Once you have selected the resources, select **Add.** The **Component properties** window opens automatically.
   :::note
   There are two distinct resource categories: tenant-level resources and folder-level resources. For more details, refer to [the Solution Components guide](https://docs.uipath.com/solutions-management/automation-cloud/latest/user-guide/solution-components). Please keep in mind that a solution package cannot exceed 200MB in file size.
   :::
5. Select **Publish** to publish your package.
6. Return to **Solutions Management** in Automation Ops.
7. Go to **Packages.**
8. From the **options** button, select **Download latest version** to download your package.
9. Use the **Tenant selection** field to sign into a different tenant or organization.
10. If the package is not available in the new tenant, use the **Upload solution package** option to upload the package you downloaded in step 7.
11. Find the package you wish to deploy. Select the **options** button, then select **Deploy package.**
12. Choose the destination folder, or select **Install as a new root folder,** and then give the new root folder a name. The **Component properties** window opens automatically.
13. You can edit certain fields associated with your package. Once you are done, select **Deploy.** The deployment begins automatically and may take a few moments to complete.
14. The **Solutions Management** window opens automatically. In **Deployments,** select the **options** button, then select **Activate deployment.**
15. In the **Activate deployment** window, make sure to verify each of the necessary steps. If you have not yet activated your app, use the link in the prompt to activate it now.
16. When you are done, confirm the deployment activation by typing the package name.

The deployed solution and all of its associated resources are ready to be used.