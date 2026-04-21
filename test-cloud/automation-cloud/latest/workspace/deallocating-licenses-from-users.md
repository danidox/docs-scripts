---
title: "Deallocating user licenses"
visible: true
slug: "deallocating-licenses-from-users"
---

:::note
The information on this page refers to options that are only applicable if user license management is enabled for your organization.
:::

## Deallocating directly assigned licenses

For licenses that have been directly assigned to a user, you must edit the user to remove the license.

1. Go to **Admin** and select the organization at the top of the panel on the left.
2. Select **Licenses**.

The **Licenses** page for the organization opens on the **Users** tab.
3. At the bottom of the page, select **License Allocations to Users** to expand the section.
4. Optionally type in the search box to find the user from which you want to deallocate licenses.
5. At the right end of the row, select the **Edit license allocation** icon:
   !['Edit license allocation' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30849)

The **Edit License Allocation** panel opens at the right of the window.
6. Clear the checkboxes for licenses that you want to deallocate.
7. Select **Save** at the bottom of the panel to apply your changes.

### Preventing a user from acquiring a license

If you want to prevent a user from acquiring any license, either inherited from a group or allocated directly:

In the **Edit License Allocation** panel, select the **Allocate to User** option and clear all the checkboxes.

## Deallocating licenses inherited from groups

### Editing the group allocation rule
:::note
Editing the license allocation rule of a group changes the licenses of all group members.
:::

1. Go to **Admin** > **Organization** > **Licenses**.

The **Licenses** page for the organization opens on the **Users** tab.
2. At the bottom of the page, select **License Allocations to Groups** to expand the section.
3. Optionally type in the search box to find the group.
4. At the right end of the row, select the **Edit group allocation rule** icon.

The **Edit Group Allocation Rule** panel opens at the right of the window.
5. Select or clear checkboxes so that only those for the licenses you want group members to have are selected.
6. Select Save at the bottom of the panel to apply your changes.

The licenses for all group members are updated according to your changes.

### Releasing the license
:::note
Releasing a user's license does not prevent the user from re-acquiring it the next time they log in.
:::

1. Go to **Admin** > **Organization** > **Licenses**.

The **Licenses** page for the organization opens on the **Users** tab.
2. At the bottom of the page, select **License Allocations to Groups** to expand the section.
3. Optionally type in the search box to find the group.
4. At the right end of the row, select the **Group members with license inheritance** icon.

The **License inheritance from group** panel opens at the right of the window.
5. For the user whose license you want to release, select **Release license**.

### Removing a user from a group
:::important
Apart from removing their license, removing a user from a group also removes the roles and robot configuration they inherited from the group.
:::

1. Go to **Admin** > **Organization** > **Accounts & Groups** page.
2. Select the **Groups** tab.
3. At the right of the row, select the **Edit** icon.

The **Edit Group** panel opens at the right of the window.
4. Remove the user from the **Add names** field.
5. Select **Save** at the bottom of the panel.