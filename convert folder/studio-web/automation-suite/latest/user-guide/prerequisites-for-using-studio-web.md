---
title: "Prerequisites for using Studio Web"
visible: true
slug: "prerequisites-for-using-studio-web"
---

Before Studio Web can be used in an organization, administrators must make sure that:

* The organization is using named user licenses. If your organization is using the multiuser (concurrent) license model and you want to use Studio Web, contact UiPath<sup>®</sup> to switch to the named user model.
* [User license management](https://docs.uipath.com/automation-suite/automation-suite/2024.10/admin-guide/about-licensing) is enabled for the organization (not applicable to the Community plan).
* The following [services are enabled](https://docs.uipath.com/automation-suite/automation-suite/2024.10/admin-guide/managing-services) for the tenant: **Orchestrator**, **Integration Service**.
* [Personal workspaces](https://docs.uipath.com/orchestrator/automation-suite/2024.10/user-guide/personal-workspaces) are enabled at user or group level.
* [Running personal automations](https://docs.uipath.com/orchestrator/automation-suite/2024.10/user-guide/configuring-automation-capabilities) is enabled at user or group level.
* In the Orchestrator [tenant settings](https://docs.uipath.com/orchestrator/automation-suite/2024.10/user-guide/configuring-tenant-settings-tenant-level), the option **Automatically configure Serverless machines in Personal Workspace for Studio Web users** is selected. If this setting is not selected or the serverless service is disabled on the tenant, users cannot run and publish projects.
* [The SignalR (Robots) scalability setting](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/configuring-tenant-settings#scalability-tab) is enabled in the Orchestrator tenant settings.
* Automation Suite Robots are enabled.