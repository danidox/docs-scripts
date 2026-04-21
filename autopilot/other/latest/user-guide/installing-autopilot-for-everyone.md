---
title: "Installing Autopilot for Everyone"
visible: true
slug: "installing-autopilot-for-everyone"
---

To install Autopilot for Everyone:

1. Navigate to the **Admin** section in your Automation Cloud™ organization.
2. Select the **AI Trust Layer** card, and switch to the **Autopilot for Everyone** tab.
3. From the **Tenant *** dropdown menu, select the tenant where you want to install and deploy Autopilot for Everyone. A list of installation prerequisites is displayed. Make sure you check all the prerequisites items, otherwise you may encounter issues while using Autopilot.
4. Once you select a tenant, the **Install** button becomes active. Select it to install the latest version of Autopilot for Everyone.

The installation might take some time, as UiPath performs the following actions:

* Downloads the Autopilot for Everyone package.
* Deploys the package as a solution in the **Solutions** tab in Orchestrator tenant.
* Creates the Autopilot root folder inside the selected tenant.<sup>1</sup>
* Installs [Clipboard AI](https://docs.uipath.com/autopilot/other/latest/everyone-user-guide/pasting-operations-with-clipboard-ai). <sup>2</sup>
* Adds the **Administrator** and **Automation Users** groups to the Autopilot folder, and grants them **Enable personal automation** and **Personal workspace** privileges.
* Adds the **Autopilot for Everyone - Serverless** machine template to the Autopilot folder.

<sup>1</sup> The installation experience for Public Sector customers only installs the Autopilot process in the Autopilot folder.

<sup>2</sup> ClipboardAI capabilities are unavailable for Public Sector and Automation Suite customers.

When the installation completes, the configuration sections become active.


:::important
To interact with Autopilot for Everyone, you must restart Assistant standalone. Select **Quit** and then relaunch Assistant.
:::