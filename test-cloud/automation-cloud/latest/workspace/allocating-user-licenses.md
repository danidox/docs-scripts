---
title: "Assigning user licenses"
visible: true
slug: "allocating-user-licenses"
---

:::note
The instructions on this page are only applicable if [user license management](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/user-license-management#user-license-management) is **enabled** for your organization. If user license management is **disabled**, user licenses are not assigned to user accounts directly. Instead, they are [assigned to tenants](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/allocating-licenses-to-tenants#assigning-licenses-to-tenants), in the same way as you assign robot and service licenses. User licenses are then consumed by users in that tenant on a first-come-first-serve basis.
:::

## Assignment options

You can assign user licenses to the accounts of your users in one of two ways:

### Using license allocation rules

This is an option that lets you perform setup one time and not have to worry about allocating licenses in the future.

To automatically assign user licenses, you must:

1. Set up a license allocation rule for a group.
2. Add user accounts to the group to grant the licenses in the allocation rule.

If your groups are already configured for the main user roles, adding a user to a group lets you set up that user's account with everything they need for working in the UiPath platform.

When added to a group, a user inherits the licenses granted by the group's license allocation rule.
:::note
But make sure your groups are set up according to the needs for each set of users because group members also inherit the service-level roles that are assigned to the group throughout the different tenants and services, and the robot configuration defined for the group in UiPath® Orchestrator.
:::

The [default groups](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/roles#groups-and-roles) that we provide are pre-configured with all these settings for the main automation personas. You can customize these groups, or create additional groups with custom settings.

### Assigning licenses to users

You can also assign user licenses to a user account directly.
:::important
Direct license allocation overwrites any licenses that the user account inherited from the groups to which they belong so that they can only use the directly-assigned licenses. Other group-inherited settings are not affected.
:::

## Managing license allocation rules

If you want to automatically assign one or more user licenses to accounts when they are added to a group, you can set up a license allocation rule for a group.

### Viewing existing rules

1. Go to **Admin**, select the organization, and then select **Licenses**.
2. At the bottom of the page, select **License Allocations to Groups** to expand that section:

   !['License allocation to groups' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30893)

   :::important
   A warning icon next to the group name indicates that the group has more licenses allocated than are available. You must either reduce the number of allocated licenses for that group or purchase additional licenses.
   :::

All the groups that currently have a license allocation rule set up are listed in this section, along with the types of user licenses that the rules assign.

   !['License allocation to groups' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30717)

### Editing a license allocation rule

To edit a license allocation rule, take the following steps:

1. Select the **Edit group allocation rule** icon at the right end of the row:

   !['Edit group allocation rule' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30865)

The **Edit Group Allocation Rule** panel opens at the right of the window.
2. Select the checkboxes for the licenses you want to assign, or deselect the ones you no longer want to assign.
3. Optionally, configure a quota to control the number of licenses a group can acquire.
   * If you enable a quota, the minimum value is 1.
   * There is no upper quota limit. However, setting the quota higher than the number of available licenses means users can acquire up to the maximum number of available licenses.
   * If you attempt to set a quota that is lower than the number of licenses already acquired by a group, an error message appears suggesting the need to adjust existing allocations.
4. Select **Save** at the bottom of the panel. If needed, select **Refresh** to refresh the table to notice your changes.

### Adding a license allocation rule

1. Select **Create Allocation Rule**.

   !['Create allocation rule' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30709)
2. In the **Add groups** box, type to search for the name of a group and then select the group from the search results.
3. Select the checkboxes for the licenses you want to assign to members of this group.
4. Optionally, configure a quota to control the number of licenses a group can acquire.
   * If you enable a quota, the minimum value is 1.
   * There is no upper quota limit. However, setting the quota higher than the number of available licenses means users can acquire up to the maximum number of available licenses.
   * If you attempt to set a quota that is lower than the number of licenses already acquired by a group, an error message appears suggesting the need to adjust existing allocations.
5. Select **Save** at the bottom of the panel. If needed, select **Refresh** to refresh the table to notice your new rule.

All current members of this group now have the selected licenses allocated to them, within the limit of licenses available for your organization.
:::important
Any licenses inherited by a user via a group are released after 3 months of user inactivity.
:::

## Managing licenses allocated to users

Another way to allocate user licenses from your organization's pool is to allocate the license directly to specific users.
:::note
This method of allocating user licenses is also known as **direct allocation**.
:::
:::important
When you allocate a license to a user, any licenses they inherited from group allocation rules are released and the user retains only those licenses that are assigned directly.
:::

### Viewing allocated user licenses

1. Go to **Admin**, select the organization, and then select **Licenses**.
2. At the bottom of the page, select **License Allocations to Users** to expand that section:

   !['License allocations to users' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30969)

   :::important
   A warning icon next to the group name indicates that the group has more licenses allocated than are available in your organization. To resolve this issue, edit the license allocation rule and select one of the available license types.
   :::

All the users that currently have a license directly allocated to them are listed in this section, along with the types of user licenses assigned to them.

   !['License allocation to users' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31627)

### Allocating licenses to users

1. Select **Allocate Licenses**.

   !['Allocate licenses' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30957)

The **Allocate Licenses** panel opens at the right of the window.
2. In the **Add users** box, type to search for a user and then select the user from the search results.

You can add multiple users if you want to allocate the same licenses to all users.
3. Select the checkboxes for the licenses that you want to allocate to the selected users.
4. Select **Save** at the bottom of the panel.
5. If needed, select **Refresh** to refresh the table to notice the new users.

### Editing a user's licenses

1. Select the **Edit license allocation** icon at the right end of the row:

   !['Edit license allocation' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30953)

The **Edit license allocation** panel opens at the right of the window.
2. Edit the user's allocated licenses:
   * To remove the allocated licenses and allow the user to inherit licenses from group memberships, if any, select **Use Group allocation rule**.
     :::note
     For Test Cloud, If a user previously had a direct license allocation, simply switching them to group allocation and removing the direct allocation will not take effect immediately. The user must disconnect and reconnect their UiPath Assistant for the changes to apply.
     :::
   * To change the licenses assigned to the user, under **Allocate to User**, select only the checkboxes for the licenses they should have.
3. Select **Save** at the bottom of the panel.
4. If needed, select **Refresh** to refresh the table.

The **Licenses** column is updated and now shows the updated list of licenses for the user.