---
title: "Permission Management"
visible: true
slug: "permission-management"
---

Roles at the tenant and folder level are managed in Orchestrator.

Roles at the app level are managed in UiPath Apps.

To allow multiple users in your organization to run an app, you need to deploy the app to an Orchestrator folder, then assign the Everyone default group to the specific folder.

## Managing permissions at folder-level

Apps are always published to an Orchestrator tenant, similarly to processes.

To manage folder-level permissions for apps, first you need to [deploy those apps to an Orchestrator folder](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-apps#deploying-apps).

For more information on managing permissions for apps at folder level, check the [Apps](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-apps) section from the Orchestrator guide.

## Managing permissions at organization-level

Apps are always published to an Orchestrator tenant, similarly to processes.

For more information on managing permissions for apps at the tenant level, check the [Apps](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-apps) section from the Orchestrator guide.

You can control the visibility of the services and tenants that are available to your users, based on their permissions. To learn more about this feature, visit [Managing tenant and service visibility](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-tenant-and-service-visibility).

### Organization-level roles

An organization admin can assign Apps users the following organization-level roles:

* **App Creator** - grants **Create** permissions on Apps.
* **Apps Administrator** - grants **Read** and **Create** permissions on Apps, and **Update** permissions on Owners and Permissions.

#### App Creator role

The **App Creator** role allows users to create or collaborate on apps. Users with this role can:

* See and update all the apps they have created (they are owners).
* See and update all the apps that have been shared with them (they are co-authors).

Members of **Everyone** and **Administrators** default groups are automatically assigned the **App Creator** role. For other default or custom groups, explicit assignment of the **App Creator** role is necessary.

#### Apps Administrator role

The **Apps Administrator** role allows users to manage apps extensively. Users with this role can:

* Create apps.
* See all the apps in the organization, both created by them and by other users.
* Update their own apps and apps shared with them.
* Change the owner of any app in the organization.
* Manage the access and roles of apps users.

Members of the **Administrators** default group are automatically assigned the **App Administrator** role. For other default or custom groups, explicit assignment of the **App Administrator** role is necessary.

:::note
The **Apps Administrator** role overrides the **App Creator** role.
:::

#### Custom roles

Custom service roles are user-defined permission sets that allow you to tailor access controls to your specific needs, offering more granular control than default roles.

To create custom roles at Apps service-level:

1. Navigate to **Access management**, and select the **Roles** tab.
2. To configure your new custom role, select **Create role**.
3. Write a name for the new custom role and, optionally, a description.
4. At the next step, assign standard or additional permissions to your role.

#### Roles comparison

To grasp the capabilities of each Apps role at a glance, refer to the following table:

| Operations | App Creator | App Administrator |
| --- | --- | --- |
| Create, view, update, share, or delete own apps | Yes | Yes |
| View and update shared apps | Yes | Yes |
| View unshared apps (of other users) | No | Yes |
| Update or delete unshared apps (of other users) | No | No |
| Delete shared apps | No | No |
| Change the owner of an app | No | Yes |
| Manage access for other users | No | Yes |

### Assigning roles

Users with the **Apps Administrator** role can access the **Access management** page. Only organization admins can assign Apps roles.

To assign roles to users:

1. Navigate to the **Access management** page in UiPath Apps.

   ![docs image](/images/apps/apps-docs-image-301568-4268799d.webp)
2. On the **Role assignments** tab, click the **Assign role** button in the top right corner. The **Assign roles** panel opens.
3. In the **Add users/groups/apps** field, type the name of the users, groups, or apps to which you want to assign the role. As you type, a dropdown displays the available options, allowing you to make the relevant selections.

   ![docs image](/images/apps/apps-docs-image-301572-4e192de6.webp)
4. In the **Role(s)** field, select the role you want to grant to the previous selection of users, groups, or apps.
5. Click **Assign**.

### Changing the owner of an app

Users with the **Apps Administrator** role can change the owner of an app.

Transferring app ownership uses the following scenario:

1. User A initially owns the app.
2. The Apps Administrator switches ownership to User B.
3. As a result, User B becomes the owner, while User A assumes a co-author role.
4. Now, the Apps Administrator transfers ownership to User C.
5. Consequently, User C becomes the owner, and User B joins User A in the co-authors list.
6. Moving forward, the Apps Administrator reverts ownership to User A.
7. User A is removed from the co-authors list and regains ownership. Meanwhile, User C joins the co-authors list alongside User B.

To change the owner of an app:

1. Navigate to the the **Build** tab.
2. On the card of the desired app, click **More Options**.
3. Select **Change owner**. The **Assign a new owner** wizard opens.
4. In the **Search users** field, type the name or the email of the new owner, then select it.
5. A pop-up message asks for confirmation. To proceed, click **Confirm**. Otherwise, click **Cancel**.
6. Click **Assign**.

As an app owner or a co-author, to see the list of previous owners:

1. Open the app.
2. Go to **App settings**, and switch to the **Manage access** tab. The list displays all users with the co-author role for the current app.

   ![docs image](/images/apps/apps-docs-image-301583-e2bfc158.webp)

## Managing permissions at app-level

At app-level, you can invite collaborators and grant them the **Co-Author** role, which allows previewing and editing the selected app.

To run an app, you first need to [deploy it to an Orchestrator folder](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-apps#deploying-apps).

### Adding Collaborators to the App

1. Navigate to the app homescreen by selecting the ![docs image](/images/apps/apps-docs-image-Settings-bed4ab35.png) gear icon at the top of the right-hand panel.
2. Select the **Manage access** tab.
3. Select the **Assign role** button.
4. Type the user's name in the **Search users and groups** textbox.
   * If the user/group is not shown, they may not be part of the organization. Refer to[Adding a user to an organization](https://docs.uipath.com/orchestrator/v2022.10/docs/managing-users).
5. Set the role to **Co-Author (can edit and run)**.

   ![docs image](/images/apps/apps-docs-image-91712-525c0812.webp)

:::important
Adding groups to Apps may take up to 60 minutes to apply. Alternatively, group members can log out and log in again to see the apps that were assigned to them.
:::