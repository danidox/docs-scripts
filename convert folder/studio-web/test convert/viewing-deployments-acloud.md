---
title: "Viewing deployments"
visible: true
slug: "viewing-deployments"
---

The **Deployments** section displays the versions of the automation you published to your personal workspace feed. The section also displays shared automation versions published by you and others in the Orchestrator folders where you have access to in the currently selected tenant.

The following information is displayed for each deployment: the process name, when it was published, version, and the Orchestrator folder where the automation was published. You can also refresh the list of deployments and filter them by their location.

To start a manual or scheduled automation, select the **Run** button on the right of the deployment. If an automation is triggered by an event, the icon ![](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/StudioWeb/event-trigger.png) is displayed and you can't manually start it.

Select the ![](https://documentationpicturerepo.blob.core.windows.net/migrated/More_VT.png) **See more** menu on the right side of a deployment to view its details and configuration options in a new, resizable window on the right of the page:

#### Configure tab

Enables you to configure what data to use (if applicable):

* Input arguments defined in the automation. If an automation uses a time trigger, the provided input argument values are applied only when you manually run the automation.
* Connections and activity properties with user-level settings which you can configure in order to run the automation with your data. For example, in an automation that involves items from SharePoint lists and Outlook emails, you can select your SharePoint and Outlook connections, and which SharePoint list to use.
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/366595)

The tab is not displayed for automations that contain neither properties with user-level settings nor input arguments.

#### Details tab

Displays the following information about the automation:

* Description
* Apps used. For automations triggered by an event, the icon ![docs image](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/StudioWeb/event-trigger.png) is displayed next to the app containing the event that triggers the automation.
* When the automation was last ran
* When the automation was last published
* Last published version
* Orchestrator folder where the automation was published
* Trigger type (manual, time, or event)
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/366591)

Additional options are available in the ![docs image](https://documentationpicturerepo.blob.core.windows.net/migrated/More_VT.png) **See more** menu;

* **Show job history** - Opens the [Jobs](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/viewing-jobs) page for this particular version of the automation.
* **View this version** - Open this version of the automation in Studio Web in read-only mode.
* **View in Orchestrator** - View and manage your deployment in Orchestrator. For more information, see [Managing Processes](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-processes) in the Orchestrator guide.
* **Delete personal automation** - Deletes the deployment and its corresponding jobs.

To see additional details and configuration options for published automations, access the **Automations** page in Orchestrator. This is where you can edit advanced settings or remove processes and triggers, view and manage jobs and logs. For more information, see [About Automations](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/folders-automations) in the Orchestrator guide.

To see the full list of deployments, select the **detailed view** button next to the **Deployments** section title.
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/440843)