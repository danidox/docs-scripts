---
title: "Configuring fine-grained access for confidential apps"
visible: true
slug: "configuring-access-for-external-apps"
---

As an administrator, you can configure fine-grained tenant or folder permissions for **confidential** apps, by assigning them to folders or tenants in Orchestrator. An external app gets the permissions required to perform particular operations in a folder or tenant through one or more roles.

An app gets the union of all organization and tenant scopes defined for it.

For example, Finance and HR are the two tenants in your organization. Your external app has the `OR.Machines.Read` scope at the organization level, and **View** permissions on Folders in the Finance tenant, and nothing defined for the HR tenant in Orchestrator. The following table offers an overview of your app's scope and what it can access:

| Tenant | Scope |
| --- | --- |
| HR | `OR.Machines.Read` |
| Finance | `OR.Machines.Read` `OR.Folders.Read` |
:::note
External apps need to be assigned directly to a specific tenant and folder, instead of using group assignments.
:::

## Adding external apps to a tenant

To grant access to a tenant for an external app or a group of external apps, follow these steps in Orchestrator:

1. Go to **Tenant** > **Manage Access**. The **Manage Access** page is displayed.
2. Select **Assign roles** > **External app**. The **Assign roles to an external app** window is displayed.
   !['Assign roles to an external app' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/229789)
3. In the **Search for an external app** drop-down, search for the object you want to add.
4. Under **Roles**, select the role(s) for this object.
5. Select **Assign**.

## Assigning external apps to a folder

To grant access to a folder for an external app or a group of external apps, follow these steps in Orchestrator:

1. Go to **Tenant** > **Folders**. The **Folders** page is displayed.
2. From the **Folders** page, in the **Manage Folders** pane, select the folder you want to manage. The folder and its contents are displayed on the right-hand dashboard.
3. Select **Assign accounts/group/external app**. The **Assign account/group/external app** window is displayed.
   !['Assign account/group/external app' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/232105)
4. In the **Account, group, or external app** drop-down, search for the object you want to add.
5. Under **The Roles for the account/group**, select the role(s) for this object.
6. Select **Assign**. The selected object is now in the folder and can access it according to its role.

## Removing Assignments

### Removing external apps from a tenant

To remove tenant access for an external app or a group of external apps, follow these steps in Orchestrator:

1. Go to **Tenant** > **Manage Access**. The **Manage Access** page is displayed.
2. Select **More Actions** > **Remove** for the object you want to remove from the tenant and any other folders where it's been explicitly assigned. A confirmation window is displayed.
   !['Removing external apps from a tenant' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/229785)
3. Select **Yes** to confirm. The removed app is removed from the tenant.

### Unassigning external apps from a folder

To remove folder access for an external app or a group of external apps, follow these steps in Orchestrator:

1. Go to **Tenant** > **Folders**. The **Folders** page is displayed.
2. From the **Folders** page, in the **Manage Folders** pane, select the folder you want to manage. The folder and its external apps are displayed on the right-hand dashboard.
   !['Unassigning external apps from a folder' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/227195)
3. Select **More Actions** > **Unassign** for the object you want to remove from the folder. A confirmation window is displayed.
4. Select **Yes** to confirm. The object is unassigned from the folder.

## Checking external apps assignments

To view all the assignments of an external app or external app group in a tenant, follow these steps in Orchestrator:

1. Go to **Tenant** > **Manage Access** in the tenant where you want to check the app assignments. The **Manage Access** page is displayed.
2. Select **More Actions** > **Check roles and permissions** for the object you want to check assignments for. The **Check Roles** window is displayed showing a list of all the roles for the object at the tenant and folder levels.
   !['Checking external apps assignments' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/231586)