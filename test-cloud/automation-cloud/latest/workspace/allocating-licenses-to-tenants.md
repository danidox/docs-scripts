---
title: "Assigning licenses to tenants"
visible: true
slug: "allocating-licenses-to-tenants"
---

This article walks you through the steps for allocating robot and service licenses from your organization's license pool to tenant license pools.

You can assign licenses to tenants when you create a tenant or for an existing tenant, by going to the tenant's **Licenses** page, as described on this page.
:::note
If user license management is disabled from [organization settings](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-organization-settings#changing-the-license-management-option), you must also assign user licenses to your tenants, in the same way as you assign robot and service licenses. If this is the case for your organization, follow the instructions on this page to manage your user licenses as well.
:::

## Assigning licenses to an existing tenant

You can view and manage the licenses that are assigned to each tenant separately.

For each tenant:

1. Go to **Admin** and select the tenant in the panel on the left.
2. Select **Licenses**.

The **Licenses** page for the selected tenant opens.
3. In the top right, select **Edit allocation**.

Robot licenses (in the Orchestrator section) and service licenses for the services in this tenant are displayed, grouped by the service.

If user license management is disabled, user licenses are also available in this panel.
4. Edit the values to change how many licenses of each type to assign to this tenant.
5. (Optional - for Studio Web users) Enable the **License fallback** option if you would like extra robot units to be retrieved from the tenant pool and assigned to Studio Web users once their robot units run out. This is only available for automations run from Personal Workspaces.
6. When finished, select **Save** at the bottom of the panel.

The panel closes and the **Licenses** page shortly refreshes to display the updated license quantities.

### How many runtimes to allocate

Although license management is typically performed from the administration interfaces, in Orchestrator you do work with a particular type of license: the **runtime**, which is a service license for robot use.

Runtimes are the licenses you need to run unattended automations. You allocate runtimes when you create a machine object in Orchestrator.

There are two aspects to know when allocating runtimes:

* **Number of runtimes**: You can assign a custom number of runtimes to a machine template, which determine the number of processes that can run at the same time on a machine. The number required runtimes is given by the number of jobs you want to allow to be executed at the same time on this machine; it is not impacted by the number of robots on the machine. Let's say you have a machine template with 10 Production (Unattended) runtimes allocated to it. For **each** workstation that is connected using the machine key of that template, 10 Production (Unattended) runtimes are reserved from the available licenses at the tenant level, allowing for executing 10 jobs at the same time. From these reserved runtimes, a runtime is only in use during job execution. So if you connect 4 machines to Orchestrator using that template, you need and reserve 40 runtimes at the tenant level. With, for example, 25 jobs running, 25 out of the 40 reserved runtimes are in use, leaving 15 runtimes that are reserved, but unused.
* **Types of runtimes**: The [types of runtimes](https://docs.uipath.com/overview/other/latest/overview/service-licensing#types-of-runtimes) that are assigned to a machine object determine the types of processes that can run on that machine.