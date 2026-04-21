---
title: "Prerequisites for using Studio Web"
visible: true
slug: "prerequisites-for-using-studio-web"
---

Before Studio Web can be used in an organization, administrators must make sure that:

* The organization is using named user licenses. If your organization is using the multiuser (concurrent) license model and you want to use Studio Web, contact UiPath<sup>®</sup> to switch to the named user model.
* [User license management](https://docs.uipath.com/automation-cloud/docs/managing-organization-settings) is enabled for the organization (not applicable to the Community plan).
* The following [services are enabled](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-services) for the tenant: **Orchestrator**, **Integration Service**.
* [Personal workspaces](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/personal-workspaces) are enabled at user or group level.
* [Running personal automations](https://docs.uipath.com/orchestrator/v0/docs/enabling-users-to-run-personal-automation) is enabled at user or group level.
* In the Orchestrator [tenant settings](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/configuring-tenant-settings), the option **Automatically configure Serverless machines in Personal Workspace for Studio Web users** is selected. If this setting is not selected or the serverless service is disabled on the tenant, users cannot run and publish projects.
* The organization allows accessing [the necessary domains](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/configuring-firewall#studio-web).
* [The SignalR (Robots) scalability setting](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/configuring-tenant-settings#scalability-tab) is enabled in the Orchestrator tenant settings.
* The [UiPath browser extension](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/using-ui-automation#using-ui-automation-for-browser-interactions) is installed (for UI Automation Cloud capabilities).