---
title: "Restricting access to a set of users"
visible: true
slug: "restricting-organization-access-to-a-set-of-users"
---

!['Enterprise' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555) This feature is only available if you are on the Enterprise licensing plan.

Tenants and services in an organizations are, by default, available to all directory users and groups who authenticate successfully.

Organization administrators can configure an organization access control policy to either allow access to all users in a directory or to restrict access to a specified list of allowed members. For any access attempt, the system checks if they are on the list of allowed entities. If they are not on the list, they are denied access and an error is raised.

Upon enabling the organization access policy, it may take up to one hour for the policy to take effect. Once in effect, users who are restricted by the policy will be denied access to all user-facing services, and services that are accessible using user tokens.

## Configuring the organization access policy

To change your access policy, follow these steps:

1. Log in as an organization administrator.
2. Navigate to the **Administration** page, make sure that the organization is selected at the top of the left pane, and then select **Security**.
3. On the **Access Restriction** tab, select the access policy for your organization.
   * **Everyone (Default):** This option allows all users and groups from your directory to sign in and access tenants and services. This option is recommended if you want to allow all users in the directory to access the organization without any additional restrictions.
   * **Only allowed members:** This option restricts access to a specific list of users and groups. Only users and groups on the allowed list will be able to sign in and access the organization, while all other users are denied access.
4. If you selected the **Only allowed members** policy, you also need to define the list of allowed members.
   :::note
   It may take up to one hour for the policy to take effect. Once in effect, users who are restricted by the policy will be denied access to all user-facing services, and services that are accessible using user tokens.
   :::

## Adding users to allowlist

The users and groups included in the allowlist are only considered when the **Only allowed members** policy is enabled.

To configure the list of members that are allowed access to the organization, follow these steps:

1. Log in as an organization administrator.
2. Navigate to the **Administration** page, make sure that the organization is selected at the top of the left pane, and then select **Security**.
3. On the **Access Restriction** tab, select **Only allowed members**. This policy restricts access to the platform to only the allowed entities. Without enabling this policy, the allowed list will have no impact on access control restrictions.
4. In the **Allowed list members** table, select **Add member**. The **Add allowed member**s window is displayed.
5. In the **Add names** field**,** enter the names or emails of the entities that are allowed access to the organization.
6. Once done, select **Add**. Once the access control policy has been configured, only the users and groups on the allowed list will be able to access the platform. Any other user who attempts to log in will be denied access.
   :::note
   It may take up to one hour for the policy to take effect. Once in effect, users who are restricted by the policy will be denied access to all user-facing services, and services that are accessible using user tokens.
   :::

## Removing users from the allowlist

The users and groups included in the allowlist are only considered when the **Only allowed members** policy is enabled.

To remove a members from the allowlist, follow these steps:

1. Log in as an organization administrator.
2. Navigate to the **Administration** page, make sure that the organization is selected at the top of the left pane, and then select **Security**.
3. On the **Access Restriction** tab, select **Only allowed members**. This policy restricts access to the platform to only the allowed entities. Without enabling this policy, the allowed list will have no impact on access control restrictions.
4. In the **Allowed list members** table, locate the member you want to remove and select the corresponding **Remove member** icon.
   :::note
   The Administrators group cannot be removed.
   :::
5. To remove multiple members, select the corresponding checkboxes and select **Remove** at the top of the table. Once the policy takes effect, the removed member is denied access to the organization.
   :::note
   It may take up to one hour for the policy to take effect. Once in effect, users who are restricted by the policy will be denied access to all user-facing services, and services that are accessible using user tokens.
   :::