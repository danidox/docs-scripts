---
title: "Managing accounts and groups for Test Cloud Dedicated"
visible: true
slug: "managing-account-group"
---

Organization administrators can view, add, edit, or remove accounts and groups at the organization level. For general information regarding accounts and groups, refer to [Managing accounts and groups](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-accounts-and-groups#managing-accounts-and-groups).

## Adding groups

You can add new groups if you want to define a custom mix of roles and license allocation rules to use for a particular group of accounts.

1. In the **Accounts & Groups** page, navigate to the **Groups** tab.
2. Select **Add Group**. The **Add Group** window is displayed.
3. Fill in the **Name** field.
4. In the **Names** field, add users to the group. Only users that have been invited to your organization beforehand are listed.

Unlike default user groups, custom groups need to be added manually to your services to allocate roles.

## Adding accounts

### Adding user accounts

1. Go to **Admin** > **Accounts & local groups** and select the **User accounts** tab.
2. Select **Add user**. The **Add user** panel opens from the right of the window.
3. Fill in the fields with the user's details.
   * If you are integrated with an external directory, the password is not required and, if system email notifications are set up, the user receives an email with their account details and can set their own password at first login.
   * If not, you must set a password for the account. The user will need the email address (or username) and password to log in.
4. Under **Group membership**, select the checkboxes for the groups to which you want to add the user.

If your groups are properly set up, the user should already have the access they need to start working in Test Cloud.
5. Select **Save** to add the account.

The panel closes and the new account is available in the list of user accounts.

### Adding robot accounts

1. Go to **Admin** > **Accounts & local groups** and select the **Robot accounts** tab.
2. In the top right, select **Add robot account**.

The **Add robot account** panel opens at the right of the page.
3. In the **Name** field, type a descriptive name for the account.
   :::important
   Choose wisely. You cannot change the name of the robot account later. If you need to rename it, you must delete the account and create a new one with a new name.
   :::
4. Optionally, under **Group membership**, select the checkbox for groups to which you want to add the account.

Adding the account to one or more groups means it inherits any roles, user licenses, or robot settings defined for the group.
5. Select **Add**.

A success message appears at the top of the panel and further guidance is displayed.

The robot account is added and is now visible on the **Robot accounts** page. It is also added to the groups you selected.

Continue the setup of the robot account in UiPath® Orchestrator as you would set up a user account for unattended use: [Configuring robot accounts to run unattended automations](https://docs.uipath.com/orchestrator/v0/docs/configuring-robot-accounts-to-run-unattended-automation).

## Adding accounts to groups

Adding an account - either user or robot - to a group means the account inherits the roles and licenses assigned to the group.
:::note
You can [check roles](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-group#checking-the-roles-for-an-account-or-group) for a group from Orchestrator and you can [check license allocation rules for the group](https://docs.uipath.com/doc:checking-license-allocation#checking-the-licenses-allocated-to-a-group) from the Licenses page.
:::

1. Go to **Admin** **Accounts & Groups** and select the **Groups** tab.
2. Select **Edit**.
3. In the **Names** field, type to search for a user or robot account.
4. Select the account from the list of results to add it to the group.
5. Select **Save**.

## Editing an account or group

You edit accounts and groups in the same way:

1. Go to **Admin** > **Accounts & Groups** and select the appropriate tab.
2. Select **Edit**.
3. Make changes as needed.
4. Select **Save**.

## Checking the roles for an account or group

You can check the roles assigned to an account or group from UiPath Orchestrator.

To check the assigned roles, take the following steps:

1. From UiPath Orchestrator, go to **Tenant** > **Manage Access** > **Access rules**.
2. Search for a specific account or group.
3. Click **More Actions**![](https://documentationpicturerepo.blob.core.windows.net/migrated/More_VT.png) > **View Access** to view the assigned roles and permissions.

To assign roles to multiple accounts, refer to [Assigning multiple accounts](https://docs.uipath.com/orchestrator/automation-cloud-dedicated/latest/user-guide/configuring-access-for-accounts#assigning-multiple-accounts).

## Removing an account or group

1. Go to **Admin** > **Accounts & Groups**, and select the appropriate tab.
2. Select **Remove**.
3. In the dialog, confirm the action to proceed with the removal.

### Effects of removal

**For accounts**: After the account is removed, the user or service can no longer log in to Test Cloud.

**For groups**, after the group is removed:
* Any roles, licenses, or robot setup for the removed group are revoked from all user accounts that belonged to the group.
* If a user account that was a part of the removed group does not have any other roles (either directly assigned or inherited from other groups), they can still log in, but they have read-only rights.