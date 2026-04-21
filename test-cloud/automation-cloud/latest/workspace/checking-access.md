---
title: "Checking access"
visible: true
slug: "checking-access"
---

![](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555)
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

As an **Organization Administrator** or **Tenant Administrator**, you can view all roles and permissions assigned to a user, group, robot account, or external application at the tenant, service, and folder level. This allows for streamlined management of access control, as well as effective troubleshooting and audit processes across all services within a tenant.

Currently, the following services support the **Check access** functionality:

* Action Center (dependent on Orchestrator permissions)
* Maestro (dependent on Orchestrator permissions)
* Communications Mining in IXP
* Data Fabric
* Document Understanding
* Insights
* Integration Service (dependent on Orchestrator permissions)
* Orchestrator (currently the only service that supports check access at folder level)
* Task Mining
* Test Manager

To check the assigned roles and permissions, take the following steps:

1. Navigate to **Admin**, choose the **Manage access** card, then select the **Check access** button. A new page containing a search box opens, allowing you to search for users, groups, robot accounts, and external applications.
2. In the search box, enter the name or the email address of the account you wish to investigate, and initiate the search. The resulting screen provides the following details on the account:
   * Role assignment: This area lists all the roles granted to the account you searched for. It distinctly indicates how each role has been assigned, whether through explicit setting or inheritance. You can export the data on role assignment to a CSV file.

To check the roles and permissions for Orchestrator folders, select **Orchestrator**. The **Folder access** panel appears, where you can view all the user roles and role assignments for each folder.

!['folder access' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/565676)

     :::note
     Selecting a specific role allows you to view the permissions associated with that role. If necessary, you can change the role and permission assignment using the links in the **Manage access** column. When checking the role assignment of an account, if a service is greyed out, it means that the service is disabled.
     :::
   * Permission assignment: This area lists all permissions associated with the role of the account you searched for. Note that we differentiate between the following types of permissions:
     + Standard permissions - By default, you view all CRUD (Create/Read/Update/Delete) permissions. You can also check the permissions given for specific actions.
     + Additional permissitions - You view all non-CRUD, service-specific permission.