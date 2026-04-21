---
title: "Publishing a project"
visible: true
slug: "publishing-a-project"
---

You run projects from the project designer for debugging purposes. After your finish debugging a project and determine that the automation works as expected, you must publish it to Orchestrator in order to make it available as an automation that robots can run. By default, projects are published to your personal workspace and available only to you. If you want to make an automation available to others, publish it to the tenant processes feed or a shared folder feed instead.

When you publish a project to the personal workspace feed, a process and a trigger are automatically created in Orchestrator and the automation is added to the [Automations](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/managing-projects) page in Studio Web.

You can make changes to a project you already published and republish it as a new version of the automation. If you republish an automation you previously published to your personal workspace, it is automatically updated in Orchestrator to the latest version.

If you publish to a different feed, a process must be manually created in Orchestrator, and then updated each time you republish.

To publish a project:

1. Open the project.
2. Click **Publish** at the top of the page.
3. In the **Publish automation** window:
   * Enter a name and a description for the automation. If you are republishing a project you already published before, you can't edit the name.
   * Select where to publish:
     + **Orchestrator Personal Workspace Feed** - The automation is published to your personal workspace and will only be available to you. This is the default selection.
     + **Orchestrator Tenant Processes Feed**- The automation is published to the global tenant feed and will be available to all users assigned to folders that use the tenant feed.
     + **Orchestrator Folder Feed** - The automation is published to the selected folder feed and will be available to all users assigned to that folder.
   * Select a version. A version is generated automatically starting with 1.0.0 when you first publish, and then incremented automatically every time you republish.
4. Click **Publish**.

   ![docs image](/images/studio-web/studio-web-docs-image-398583.webp)

To manage the versions of a published project, open the **Change history** panel from the ![docs image](/images/studio-web/studio-web-docs-image-421615.webp) icon on the upper-left side of the designer. The **Change history** panel lists project versions in chronological order starting from the current version (selected by default). Each entry in the panel contains:

* The version number.
* The last time the version was changed.
* The name of the version.

Selecting an earlier project version opens it in the designer in read-only mode, allowing you to see what activities and files that particular version contained.