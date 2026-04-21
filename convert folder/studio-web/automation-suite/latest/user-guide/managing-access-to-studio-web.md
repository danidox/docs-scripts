---
title: "Managing access to Studio Web"
visible: true
slug: "managing-access-to-studio-web"
---

Studio Web uses role-based access control. The following roles are available:

* **Studio Web Administrator** enables users to:
  + Design, run, and publish projects, start and manage published automations.
  + Manage roles.
  + Author templates.
  + Enable Studio Web in the organization.
* **Studio Web Contributor** enables users to:
  + Design, run, and publish projects, start and manage published automations.
* **Organization Template Author** enables users to:
  + Design, run, and publish projects, start and manage published automations.
  + Author templates.

:::note
The **Studio Web Contributor** role is assigned to all the default user groups, including the **Everyone** user group that includes all the users invited to an Automation Cloud organization. If you don't want everyone to have access to Studio Web, remove the role assignment for the group.
:::

## Managing role assignments

Administrators can manage role assignments at user or group level.

To view and manage role assignments:

1. In Automation Cloud, select **Studio** from the left-side menu.
2. On the upper-right side of any Studio page, select the ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/503614) **Manage access** button.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/623624)

The Manage access page opens and displays a table with current user and group role assignments. You can search in the list of assignments and filter by role.

## Assigning roles

1. On the Manage access page:
   * To edit current role assignments for a user or group, click the pencil button on the right side of that user or group.
   * To assign roles to a new user or group, select **Assign roles** above the table that displays current assignments.
2. In the **Assign roles** window,
   * If you are assigning roles to a new user or group, select the user or group. Start typing names or email addresses to find matches from the organization.
   * Select which roles to assign.
3. Click **Save**.

## Deleting role assignments

On the Manage access page, click the **Delete** button on the right side of a user of group, and then select **Delete** again in the confirmation dialog.