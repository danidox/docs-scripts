---
title: "Managing accounts and local groups for Test Cloud and Test Cloud Public
               Sector"
visible: true
slug: "managing-account-groups"
---

Organization administrators can view, add, edit, or remove accounts and groups for the organization from the **Accounts & local groups** page at the organization level. For general information regarding accounts and groups, refer to [Managing accounts and groups](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-accounts-and-groups#managing-accounts-and-groups).
:::note
Changing a user email address is not supported. If a user email address needs to change (for example, due to a company domain change), invite the user using their new email address, then delete the account associated with the old address.
:::

## Creating local groups

You can add new local groups if you want to define a custom mix of roles and license allocation rules to use for a particular group of accounts. For example, the ones needed by your colleagues in the Accounting department to use the UiPath platform.

1. Go to **Admin** and select the organization at the top of the panel on the left.
2. Select **Accounts & local groups**.

The **Accounts & local groups** page for the organization opens on the **User accounts** tab.
3. Select the **Local groups** tab.
4. Select **Add local group**. The **Add group** window is displayed.
5. Fill in the **Name** field.
6. In the **Names** field, type to search and then select an entry from the results to add it to the group.

Only accounts that already exist on the **User accounts** page are available.

If you enabled a [directory integration](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/authentication-models-for-test-cloud#the-directory-accounts-model), you can also search for users and groups from the linked directory.
7. Select **Add** at the bottom of the panel to create the group.

The panel displays a success message and offers the option to create a license allocation rule for the group.
8. If you want to create a license allocation rule for this group, select **Create Allocation Rule**.

Otherwise, select **Close** at the bottom of the panel and skip the remaining steps.
9. Select the checkboxes for the user licenses that you want to automatically assign to current and future members of this group.
10. Select **Save** at the bottom of the panel. Your new group is now listed in the **Local groups** page.

## Creating accounts

For information about the different account types, refer to [About accounts and groups](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-accounts#about-accounts-and-groups).

### Creating user accounts

For information about working with user accounts, refer to [Managing user accounts](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-groups#managing-user-accounts).

### Creating robot accounts

For more information about robot accounts refer to [Robot accounts](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-accounts#robot-accounts).

To create a robot account, take the following steps:

1. Navigate to **Admin** and select the organization.
2. Select **Accounts & local groups**.

The **Accounts & local groups** page for the organization opens on the **User accounts** tab.
3. Select the **Robot accounts** tab.
4. Select **Add robot account**.

The **Add Robot Account** panel opens.
5. In the **Name** field, type a descriptive name for the account.
6. Optionally, under **Group membership**, select the checkbox for groups to which you want to add the account.

Adding the account to one or more groups means it inherits any roles, user licenses, or robot settings defined for the group.
7. Select **Add**.

A success message appears and further guidance is displayed.

The robot account is added and is now visible on the **Robot accounts** page. It is also added to the groups you selected.

Continue the setup of the robot account in UiPath® Orchestrator as you would set up a user account for unattended use: [Configuring robot accounts to run unattended automations](https://docs.uipath.com/orchestrator/v0/docs/configuring-robot-accounts-to-run-unattended-automation) .

## Removing an account or group

To remove an account or group, take the following steps:

1. Go to **Admin** and select the organization at the top of the panel on the left.
2. Select **Accounts & local groups**.
3. To remove a user account, select the **User accounts** tab. Alternatively, to remove a local group, select the **Local groups** tab.
4. Look for the user account or group you want to remove, then at the right end of the row, select the three-dot button, then choose **Delete**.
5. Confirm the action in the confirmation dialog.

Alternatively, you can remove accounts and groups using the user and group profiles. For details, refer to [Managing user and group profiles](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-groups#managing-user-and-group-profiles).

## Managing user accounts

Adding users for any of the services in your organization is done from the Admin section. You cannot add users to a service from the service itself.
:::note
Changing a user email address is not supported. If a user email address needs to change (for example, due to a company domain change), invite the user using their new email address, then delete the account associated with the old address.
:::

### Inviting users
:::note
Invited users do not receive an invitation email for signing up by default. To enable this feature, administrators must set up [custom email settings.](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-system-email-notifications#using-custom-email-settings "To configure custom email settings for your own SMTP server, provide the necessary information for your SMTP configuration, as described in the following table:")
:::

With this method, you can invite up to 20 users or 20 groups at one time. If you need to invite more, use the bulk operation instead.

1. Go to **Admin** and select the organization at the top of the panel on the left.
2. Select **Accounts & local groups**.

The **Accounts & local groups** page for the organization opens on the **User accounts** tab.
3. In the top right of the tab, select **Invite users**.

The **Invite users** panel opens at the right of the window.
4. In the **Email** field, type and email address and then press **Space**.

Continue to add email addresses if you want to invite multiple users.
5. (Optional) Select the checkbox for one or more groups to which you want to add the users. Refer to [User Group Considerations](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-groups#user-group-considerations) for more information.
6. Select **Invite**.

The **Invite Users** panel closes and the invited users are displayed on the **Users** page.

In the **Last active** column, **Pending** is displayed until each user accepts the invitation and logs in.

You can continue with [assigning roles](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/role-management#direct-provisioning) and [allocating user licenses](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/allocating-user-licenses#assigning-user-licenses), even if a user hasn't accepted the invitation yet.

### Inviting users in bulk
:::note
Invited users do not receive an invitation email for signing up by default. To enable this feature, administrators must set up [custom email settings.](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-system-email-notifications#using-custom-email-settings "To configure custom email settings for your own SMTP server, provide the necessary information for your SMTP configuration, as described in the following table:")
:::

To invite up to 1000 users simultaneously, use a `.csv` file containing the users to be invited and the user groups they belong to. Using this method, you can configure distinct group settings for users. Refer to [User Group Considerations](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-groups#user-group-considerations) to choose the access control strategy best suited for your needs.

**CSV file requirements**

**[Download.CSV Example](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/Automation_Cloud/user_upload_template.csv)**

The CSV file allows for two columns. Any extra columns are not considered. The two columns must be named and populated as follows:

* email - must be populated with the email addresses of the users to be invited.
* group membership - must be populated with the user groups each user should belong to. If left empty, the user is invited with no associated parent group. It allows for multiple groups, separated by a comma (for example, "automation developers, administrators") The CSV file validation is not case sensitive. "Automation Users" and "automation users" are both valid. You can invite up to 1000 users simultaneously with one CSV file.
  !['Error summary' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30609)

1. Go to **Admin** and select the organization at the top of the panel on the left.
2. Select **Accounts & local groups**.

The **Accounts & local groups** page for the organization opens on the **Users** tab.
3. In the top right of the tab, select **Invite users in bulk**.

The **Upload CSV** dialog opens.
4. Select **Upload file** and select the CSV file to be uploaded.

Upon upload, file validation is performed:

   1. If the file meets the requirements, the upload operation is performed successfully, and the users in the CSV file are invited to the organization as part of the corresponding user groups.
   2. If the file does not meet the requirements, the **Error Summary** window is displayed with the reason for failure: `Invalid email format`, `Some or all groups were invalid`, or `API error`. Corrupted user entries are not considered and the corresponding users are not invited.

### User group considerations

#### Leveraging groups

By leveraging user groups you can grant default access to all group members without the need to set the access level for each user individually. By granting roles and permissions to groups in your services and adding users to the desired groups in Cloud Portal (be it when inviting them, or by editing them afterward), all group members inherit that access level with no further configuration required You just need to ensure the groups are referenced in the services you use.

* Default user groups (i.e. groups provided by UiPath®) are automatically referenced in newly created services, and they are configured with a set of default permissions. You can change this default configuration at any moment if you choose so.
* For services created before the User Groups feature was launched, default user groups are not referenced. They must be added manually.
* Custom user groups (i.e. your own custom groups) must be added manually to your services irrespective of when they have been created. The following table describes where you can learn about adding user groups for each service: <table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Service
    </p>
   </th>
   <th>
    <p>
     Learn
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d116304e612">
    <p>
     <strong>
      Orchestrator
     </strong>
    </p>
   </td>
   <td headers="d116304e615">
    <ul>
     <li>
      <a href="https://docs.uipath.com/orchestrator/v0/docs/assigning-roles#assigning-roles-to-a-group">
       Adding user groups at the tenant level in Orchestrator services.
      </a>
     </li>
     <li>
      <a href="https://docs.uipath.com/orchestrator/v0/docs/configuring-access-for-accounts#adding-accounts-to-a-folder">
       Adding user groups to folders in Orchestrator services.
      </a>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

#### Not leveraging groups

If you do not want to use groups, leave any user to the default **Everyone** group, which comes with no roles attached by default. This implies access control is performed on a per-user basis; users must be granted roles individually in each service.

The following tables describes where you can learn more about granting access rights to users:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Service
    </p>
   </th>
   <th>
    <p>
     Learn
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d116304e666">
    <p>
     <strong>
      Orchestrator
     </strong>
    </p>
   </td>
   <td headers="d116304e669">
    <ul>
     <li>
      <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/configuring-access-for-accounts#tenant-level-access-control">
       Granting access-rights to users at the tenant level in Orchestrator services.
      </a>
     </li>
     <li>
      <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/configuring-access-for-accounts#folder-level-access-control">
       Granting access-rights to users at the folder level in Orchestrator services.
      </a>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

### Removing users

To remove a user, select the corresponding **Delete** button in the **Users** page, and then **Delete** to confirm. Alternatively, select one or multiple users, and select the **Delete** button. The deleted user/users are no longer displayed on the **Users** page and they cannot access your organization.
:::note
* When you invite someone to join your organization, a new user account is created. Should you remove this user from your organization,
they can log in independently by creating a new organization. While they can't access your organization's data post-removal, they may still use their account in a new organization.
* You cannot delete your own user. Ask another organization administrator to perform the changes for you.
:::

### Creating custom user groups

1. In the **Accounts & local groups** page, go to the **Local groups** tab.
2. Select **Add local group**. The **Add group** window is displayed.
3. Fill in the **Name** field.
4. On the **Names** field, add users to the group. Only users that have been invited to your organization beforehand are listed.

Unlike default user groups, custom groups need to be added manually to your services to ensure the correct mapping between the group membership and the corresponding roles in those services.

## Managing user and group profiles

As an organization admin, you can manage user and group profiles from a single location that allows you to customize group memberships, handle licenses, monitor access, and update user and group info.

To access user and group profiles, navigate to **Admin** > **Accounts & local groups** > **User accounts**, then select the user account or group you want to manage.

### Managing user profiles

To manage the profile of a user account, navigate to **Admin** > **Accounts & local groups** > **User accounts**, then select the user account you want to manage. You can perform the following operations:

* In the **Group memberships** tab: View, add, or remove group memberships.
* In the **Licenses** tab: View, assign, or remove license allocation.
* In the **Access** tab: View or export details on permissions and role assignment.
* In the **Info** tab: Rename or delete local users.
  :::note
  * You cannot delete or rename directory users or the last admin.
  * An organization must always have at least one admin. If you need to
  replace the current administrator, first add the new user to the **Administrators** group (**Admin** > **Accounts & local user groups** > **User accounts** > **Group memberships** > **Add memberships**). After the new admin is assigned, open the previous administrator's account and remove their **Administrators** group membership. This ensures that the role is transferred while always keeping at least one active organization admin.
  :::

### Managing group profiles

To manage the profile of a user group, navigate to **Admin** > **Accounts & local groups** > **Local groups**, then select the group you want to manage. You can perform the following operations:

* In the **Members** tab: Add or remove users to or from a local group.
  :::note
  All local or directory users added to Test Cloud are part of the **Everyone** group. You cannot view the members in the **Everyone** group.
  :::
  :::important
  Known limitation: The search results for local group members are not displayed beyond the first page, regardless of whether the query matches the search result.
  :::
* In the **Licenses** tab: View, assign, or remove license allocation.
* In the **Access** tab: View or export access details.
* In the **Group** info tab: Rename or delete local groups.
  :::note
  You cannot delete or rename directory groups or built-in groups (**Everyone**, **Automation Users**, **Administrators**, etc.).
  :::