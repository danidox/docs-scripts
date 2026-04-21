---
title: "Prerequisites"
visible: true
slug: "prerequisites"
---

To access Autopilot for Everyone, ensure the following prerequisites are met:

* UiPath Assistant and Robot version 2024.10.5 or above, Enterprise edition, is installed on your machine. This is not mandatory if you use Assistant web.
* The Robot is installed in User Mode. This is not mandatory if you use Assistant web.
* You sign in to Assistant using the Service URL.
* You are part of an Enterprise plan and hold a user license that enables attended automations.
* The Document Understanding service is enabled on your tenant .
  :::important
  You need AI units to enable the Document Understanding service. To have access to AI units, add the AI Center service to your tenant.
  :::
* Autopilot for Everyone is installed in your Automation Cloud™ tenant. For use in Assistant web, you must install version Autopilot for Everyone 2025.4.1.
* You have access to the Autopilot folder in the tenant.
* The [personal workspace](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/personal-workspaces#enabling-personal-workspaces) is enabled for your account.

## Roles and permissions

To interact with Autopilot for Everyone, you need the following roles and permissions:

* The [**Automation User** role](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-access#groups-and-roles) in the Autopilot folder.
* The **[Enable user to run automation](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/configuring-automation-capabilities#enabling-individual-users-to-run-personal-automations)** option is selected for your user account in Orchestrator.
* The **[personal workspace](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/personal-workspaces#enabling-personal-workspaces)** is enabled for your user account.
* The [**View** permission for **Resource Overwrites**](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-managing-user-access#permission-and-role-types) in the Autopilot folder.

## Licensing and policies

To access Autopilot for Everyone:

* Make sure you have an Automation Cloud™ Enterprise plan.
* Make sure you have a valid user license.

If the 24.10.1 Assistant policy is in place, the Autopilot for Everyone widget appears by default. To disable the widget for your organization, apply your own Automation Ops policy. 
  :::important
  Tenant-level deployments of Assistant policies do not propagate correctly to users, and prevent the Autopilot for Everyone widget from being displayed. As a temporary solution, deploy the Assistant policy directly to a user group with the intended users.
  :::
Automation Express or Autopilot Express licenses (for Flex plans), and Express User licenses (for Unified Pricing plan), allow you to execute automations only from the following Orchestrator folders:

* **Personal Workspace**—Automations created by users
* **Autopilot**—Automations installed and deployed with the Autopilot for Everyone installation
* **Tool Automations** and subfolders—Out-of-the-box automations deployed by Autopilot for Everyone administrators


:::important
If you, as an administrator, previously deployed out-of-the-box automations from the Marketplace solution, we recommend:
* reinstalling the out-of-the-box automation bundles from the Autopilot for Everyone Admin experience, and
* removing any manually deployed out-of-the-box automations.
:::

:::important
Express User licensing (for Unified Pricing plan) is not available in Automation Suite.
:::