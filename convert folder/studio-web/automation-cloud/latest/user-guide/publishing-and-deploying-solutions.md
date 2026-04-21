---
title: "Publishing and deploying solutions"
visible: true
slug: "publishing-and-deploying-solutions"
---

## Publishing solutions

Publishing a solution creates a solution package.

Before solutions in a unified developer experience, each project was individually published as a NuGet package. While NuGet packages continue to be the way to pack individual automations, the entire solution is packed in a ZIP file.

The solution package contains all the deployment configurations, as well as the corresponding NuGet packages pertaining to each automation project. The solution package is transferable across tenants and organizations.

To publish a solution:

1. Select the **Publish** button at the top of the designer.
2. In the **Publish solution** window, enter a name and a description for your solution, and select a version.
3. Under **Location**, choose where to publish your solution: **Orchestrator Tenant** or **Personal Workspace**.
4. Select **Publish**.

Solutions are published differently depending on the location you have selected.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/614899)

## Publishing to an Orchestrator Tenant

When you publish to an Orchestrator tenant, a validation message appears in your solution designer once the solution package is created. A notification also appears in the **Notifications panel**.

To check the published solution package, select the **Check package** link in the validation message. You are then directed to the **Tenant** &gt; **Solutions** &gt; **Packages** &gt; **Package Versions** page in Orchestrator.

For the developed automations to become executable, the solution package needs to be deployed. An Orchestrator Tenant enables other users to access your solution.

## Publishing to a Personal Workspace

The Personal Workspace is dedicated for your own usage. When you publish to your Personal Workspace, a validation message appears in your solution designer once the solution package is created. For convenience, publishing a solution to your Personal Workspace automatically performs a deployment, to bring the automation to an executable state.

To check the published and deployed solution package, select the **Check Automation** link in the validation message. You are then directed to the **My Workspace** &gt; **Solutions** &gt; **Deployments** &gt; **Deployment Summary** page in Orchestrator.

## Deploying solutions

Once published, a solution becomes available for deployment anywhere within the tenant. The solution package can be found in Orchestrator, at the tenant level, under the **Solutions** tab. You can then initiate the deployment process from this location.

The solution generates all required artifacts in the folder that you have selected. During deployment, you can choose to use already existing resources instead of creating new ones (for example, you can use an already available asset instead of creating a new one).
:::note
Solutions published to a Personal Workspace are automatically deployed during publishing.
:::

After a solution has been deployed for the first time, you need to follow the upgrade flow to deploy a new version of the solution, unless the goal is to deploy the solution in a different folder.

To move a solution package from one tenant to another, you need to manually download the package and uploaded it to the desired tenant.

Solutions are deployed as a whole. To minimize the manual tasks performed during deployment, reduce potential errors, and facilitate the development process, you can set the deployment configuration of a solution at design time.

This can be done from the [Deployment configuration panel](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/designing-solutions), where everything that will be deployed is listed along its respective configuration.

To learn more about deploying a solution published to an Orchestrator Tenant, refer to [Deploying a solution](https://docs.uipath.com/solutions-management/automation-cloud/latest/user-guide/deploying-a-solution) in the Solutions Management user guide.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/580272)

You can also deploy a solution for debugging purposes by:

1. Navigating to the toolbar above the Studio Web designer.
2. Selecting the ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/553399) arrow next to the debugging environment.
3. Selecting **Deploy solution for testing** from the drop-down menu.