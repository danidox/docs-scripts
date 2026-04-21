---
title: "Publishing, deploying, and upgrading an agentic process"
visible: true
slug: "publishing-deploying-upgrading-an-agentic-process"
---

## Publishing an agentic process

To publish an agentic process project:

1. Open the project.
2. Select **Publish** at the top of the designer.
3. In the **Publish automation** window:
   * Enter a name and description for your automation. If you are republishing a project you already published before, you can't edit the name.
   * Select where to publish:
     + **Orchestrator Personal Workspace Feed** - The automation is published to your personal workspace and will only be available to you. This is the default selection.
     + **Orchestrator Tenant Processes Feed** - The automation is published to the global tenant feed and will be available to all users assigned to folders that use the tenant feed.
   * Select a version. A version is generated automatically starting with 1.0.0 when you first publish, and then incremented automatically every time you republish.
4. Click **Publish**.

You can then access your published agentic process after deploying it in Orchestrator.

:::note
* Agentic processes published to the
**Orchestrator Personal Workspace Feed** are automatically deployed in Orchestrator and can be run immediately.
* Publishing to the **Orchestrator
Tenant Processes Feed** requires you to have a **Tenant** permission for **Packages create**, or use the predefined **Allow to be Automation Publisher** role.
* When publishing to a **Folder feed**
you will need to have a **Folder** permission for **Folder Packages create**, or use the predefined **Automation Publisher** role.
:::

Open the **Change history** panel from the ![](/images/studio-web/studio-web-docs-image-421615.webp) icon on the upper-left side of the designer to manage the versions of a published agentic process. The **Change history** panel lists project versions in chronological order starting from the current version (selected by default). Each entry in the panel contains:

* The version number.
* The last time the version was changed.
* The name of the version.
* Where the project was published.

Selecting an earlier project version opens it in the designer in read-only mode, allowing you to see what elements that particular version contained.

## Deploying an agentic process

To deploy a published agentic process project, navigate to Orchestrator and:

1. Select the Orchestrator folder you wish to deploy your project in.
2. Navigate to the **Automations** page and select the **Add process** button.
   :::note
   We recommend that you have the **Allow to be Folder Administrator** tenant role and the **Folder Administrator** role in the folder you want to deploy to.
   :::
3. Choose the agentic process project you want to deploy from the **Package Source Name** drop-down menu, followed by the version from the **Package Version** drop-down menu, and the entry process from **Entry point** drop-down menu (if available).
4. Select **Next** to advance to the **Package Requirements** page and provide any package requirements.
5. Select **Next** to advance to the **Additional Settings** page and finalize the deployment configuration.
6. Select **Create** to deploy your agentic process project.

After deployment, your process is listed in the **Processes** page. Selecting the process, then the **Edit** ![](/images/studio-web/studio-web-image-542670.webp) button opens the **Edit process** page, where you can update the process configuration, requirements, and additional settings.

To learn more about managing processes, see the [Orchestrator guide](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-processes#used-applications).

## Upgrading an agentic process

When you publish a new version of an agentic process project, the **Updates are available** ![docs image](/images/studio-web/studio-web-docs-image-542693.webp) button appears under the **Version** column in the **Automations** &gt; **Processes** page. To upgrade your published project:

1. Select the **More actions** ![docs image](/images/studio-web/studio-web-docs-image-542706.webp) button on the right of the process.
2. Select **Upgrade to latest version** from the drop-down menu.
3. In the **Update package version** window, select **Confirm**.

## Setting up robot account access

An agentic process uses the same concepts as a robot in terms of permissions. We recommend creating one robot account in the folder where the process is deployed, with the following roles:

* **Automation User** folder role.
* **Allow to be Automation User** tenant role.

These roles will have all the need permissions for the agentic process and any other automations, apps, connectors, or business rules.