---
title: "Role assignments"
visible: true
slug: "role-management"
---

:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

You can manage and assign service-level roles from within each service as long as you have the appropriate permissions in the service.

For example, users with the **Administrator** role in Orchestrator can create and edit roles, and assign roles to existing accounts.

## Direct provisioning

### Assigning organization-level roles

Organization-level roles are predefined and cannot be changed.

Organization administrators can assign organization-level roles to individual accounts from **Admin > Accounts and Groups** by adding accounts to a default or custom group.
:::note
If you have linked your UiPath organization to a directory, such as Microsoft Entra ID, then it is possible to also assign organization-level roles to directory groups by adding them to groups, same as with accounts. This is not possible with local groups.
:::

### Assigning tenant-level roles

Tenant-level roles can be set at tenant level and can have granted permissions up to the service level.

**Organization Administrators** or other **Tenant Administrators** can use the **Manage Access** screen to assign tenant-level roles. Note that while **Organization Administrators** can access **Manage access** in any tenant, **Tenant Administrators** can access it only in the tenant they manage.

To view the tenant-level role definition and the permissions granted at tenant and individual service level, go to **Manage Access**, then in the **Roles** tab select the **View** button next to the role.

You can assign a tenant-level role to a user, group, robot account, or external application. To assign the role, go to **Manage acces**s, then in the **Role Assignments** tab search for the account you want to assign the role to, choose the appropriate role, then select **Assign**.

### Tenant Administrator role visibility at service level

The **Tenant Administrator** role assignment is visible both at tenant and individual service level. At the service level, the **Tenant Administrator** role has the following properties:

* It is shown with a platform role label.
* It is immutable, implying that you cannot remove the assignment at the service level.
* In some services, such as Orchestrator, there is a link next to the role that redirects you to the **Manage access** page at platform level, where you can change the tenant-level role assignments.

### Managing service-level roles

You manage and assign service-level roles from within the services. You can assign roles to groups (recommended), or to accounts that have already been added.

For information and instructions, refer to the applicable documentation, as described in the following table:

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
     Details
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d14416e158">
    <p>
     <strong>
      Orchestrator
     </strong>
    </p>
   </td>
   <td headers="d14416e161">
    <p>
     Managed from Orchestrator.
    </p>
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles">
      Learn more about roles
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e158">
    <p>
     <strong>
      Actions
     </strong>
    </p>
   </td>
   <td headers="d14416e161">
    <p>
     Managed from Orchestrator.
    </p>
    <ul>
     <li>
      For the list of permissions required, refer to
      <a href="https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/roles-and-permissions">
       Roles and
                                             permissions
      </a>
      .
     </li>
     <li>
      For instructions on assigning roles, refer to
      <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-managing-user-access">
       Assigning roles
      </a>
      .
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14416e158">
    <p>
     <strong>
      Processes
     </strong>
    </p>
   </td>
   <td headers="d14416e161">
    <p>
     Managed from Orchestrator.
    </p>
    <ul>
     <li>
      For the list of permissions required, refer to
      <a href="https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/roles-and-permissions">
       Roles and
                                             permissions
      </a>
      in the Action Center
                                       documentation.
     </li>
     <li>
      For instructions on assigning roles, refer to
      <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-managing-user-access">
       Assigning roles
      </a>
      .
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14416e158">
    <p>
     <strong>
      Data Service
     </strong>
    </p>
   </td>
   <td headers="d14416e161">
    <p>
     Managed from Data Service.
    </p>
    <ul>
     <li>
      For more information and instructions, refer to
      <a href="https://docs.uipath.com/data-service/automation-cloud/latest/user-guide/managing-access">
       User management
      </a>
      .
     </li>
     <li>
      For instructions on assigning roles, refer to
      <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-managing-user-access">
       Managing access
      </a>
      .
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14416e158">
    <p>
     <strong>
      Test Manager
     </strong>
    </p>
   </td>
   <td headers="d14416e161">
    <p>
     Managed from Test Manager.
    </p>
    <p>
     For information and instructions, refer to
     <a href="https://docs.uipath.com/test-suite/automation-cloud/latest/user-guide/managing-users-and-groups">
      User and group access
                                          management
     </a>
     .
    </p>
   </td>
  </tr>
 </tbody>
</table>

### Assigning roles to an account

If you want to control the access a certain account has in a service at a more granular level, but you do not want to add new roles to an entire group, you can explicitly add the account to the service and assign one or more service-level roles to it directly.

For information about the available roles and instructions, refer to the documentation for the target service, as previously described.

## Auto-provisioning

Through auto-provisioning, any directory account can be set up with access and rights for using the UiPath platform directly from the external identity provider (IdP).

Auto-provisioning requires a one-time setup after you enable an integration with a third-party IdP: Microsoft Entra ID or other IdPs that are connected used SAML integration.

## Manage access user interface based on scope

The **Manage access** user interface (UI) keeps a consistent appearance across all scopes.

The following table illustrates how the Manage access UI looks like for each scope:

| Scope | Manage access UI |
| --- | --- |
| Organization | !['Organization scope manage access' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/564206) |
| Tenant | !['tenant scope manage access' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/564210) |
| Service | !['Service scope manage access' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/564214) |
| Project | !['Project scope manage access' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/564218) |

## Assigning organization-level roles

As an organization administrators, you can navigate to **Manage access** at organization level to assign tenant-level roles.

To view the role definition and the permissions granted, take the following steps:

1. Navigate to **Manage access**.
2. In the **Roles** tab, select the **View** button next to the role.

You can assign an organization-level role to a user, group, robot account, or external application. To assign a role, take the following steps:

1. Navigate to **Manage access**, then
2. in the **Role assignments** tab, search for the account you want to assign the role to and choose the appropriate role.
3. Select **Assign**.

## Assigning tenant-level roles

Tenant-level roles can be assigned at tenant level and can have granted permissions up to the service level.

**Organization Administrators** or other **Tenant Administrators** can view the **Manage access** screen.
:::note
While **Organization Administrators** can access manage the access in any tenant, **Tenant Administrators** can manage access only in the tenant they manage.
:::
To view the tenant-level role definition and the permissions granted at tenant and individual service level, take the following steps:

1. Navigate to **Manage access**.
2. In the **Roles** tab, select the **View** button next to the role.

You can assign a tenant-level role to a user, group, robot account, or external application. To assign the role, take the following steps:

1. Navigate to **Manage access**.
2. In the **Role assignments** tab, select **Assign role**.
3. Search for the account you want to assign the role to and choose the appropriate role.
4. Select **Assign** to confirm the assignment.

### Tenant Administrator role visibility at service level

The **Tenant Administrator** role assignment is visible both at tenant and individual service level. At the service level, the **Tenant Administrator** role has the following properties:

* It is shown with a platform role label.
* It is immutable, implying that you cannot remove the assignment at the service level.
* In some services, such as Orchestrator, there is a link next to the role that redirects you to the **Manage access** page at platform level, where you can change the tenant-level role assignments.

## Assigning and managing service-level roles

You can manage and assign service-level roles from within the services. You can assign roles to groups (recommended), or to accounts that have already been added.

For information and instructions, refer to the applicable documentation, as described in the following table:

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
     Details
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Orchestrator
      </p>
      <ul>
       <li>
        <p>
         Action Center
        </p>
       </li>
       <li>
        <p>
         Processes
        </p>
       </li>
       <li>
        <p>
         Context Grounding
        </p>
       </li>
       <li>
        <p>
         Solutions
        </p>
       </li>
       <li>
        <p>
         Integration Service
        </p>
       </li>
       <li>
        <p>
         Maestro
        </p>
       </li>
      </ul>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Orchestrator.
    </p>
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles">
      Learn more about roles
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Actions
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Orchestrator.
    </p>
    <ul>
     <li>
      For the list of permissions required, refer to
      <a href="https://docs.uipath.com/action-center/docs/roles-and-permissions">
       Roles and permissions
      </a>
      .
     </li>
     <li>
      For instructions on assigning roles, refer to
      <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/assigning-roles">
       Assigning roles
      </a>
      .
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Processes
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Orchestrator.
    </p>
    <ul>
     <li>
      For the list of permissions required, refer to
      <a href="https://docs.uipath.com/action-center/docs/roles-and-permissions">
       Roles and permissions
      </a>
      in the Action Center documentation.
     </li>
     <li>
      For instructions on assigning roles, refer to
      <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/assigning-roles">
       Assigning roles
      </a>
      .
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Automation Hub
      </p>
      <ul>
       <li>
        <p>
         Automation Store
        </p>
       </li>
      </ul>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Automation Hub.
    </p>
    <p>
     For more information about which roles are required and
                                    instructions for assigning them, refer to
     <a href="https://docs.uipath.com/automation-hub/docs/roles-description-and-matrix">
      Role description and
                                          matrix
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       AutomationOps
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from AutomationOps.
    </p>
    <p>
     For more information, refer to
     <a href="https://docs.uipath.com/automation-ops/automation-cloud/latest/USER-GUIDE/automation-ops-user-roles">
      AutomationOps user roles
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       AI Center
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Orchestrator.
    </p>
    <p>
     For information about the roles required to use AI Center, refer
                                    to
     <a href="https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/ai-center-access-control">
      AI Center access control
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Apps
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Orchestrator.
    </p>
    <p>
     For more information, refer to
     <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/orchestrator-permissions">
      Orchestrator permissions
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Data Fabric
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Data Fabric.
    </p>
    <ul>
     <li>
      For more
                                       information and instructions, refer to
      <a href="https://docs.uipath.com/data-service/automation-cloud/latest/user-guide/managing-access">
       User
                                             management
      </a>
      .
     </li>
     <li>
      For
                                       instructions on assigning roles, refer to
      <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-managing-user-access">
       Managing
                                             access
      </a>
      .
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Document Understanding&trade;
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Document Understanding.
    </p>
    <p>
     For more information about which roles are required and
                                    instructions for assigning them, refer to
     <a href="https://docs.uipath.com/document-understanding/automation-cloud/latest/user-guide/role-based-access-control">
      Role-based access
                                          control
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Insights
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Insights.
    </p>
    <p>
     For more information, refer to
     <a href="https://docs.uipath.com/insights/automation-cloud/latest/user-guide/granting-permissions">
      Granting permissions
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       IXP
      </p>
      <ul>
       <li>
        <p>
         Communications Mining
        </p>
       </li>
      </ul>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from IXP.
    </p>
    <p>
     For more information, refer to
     <a href="https://docs.uipath.com/ixp/automation-cloud/latest/overview/managing-access#roles-and-their-underlying-permissions">
      Roles and their underlying
                                       permissions
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Process Mining
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Process Mining.
    </p>
    <p>
     For more information, refer to
     <a href="https://docs.uipath.com/process-mining/automation-cloud/latest/user-guide/setting-up-the-users#user-management-in-process-mining">
      User management in Process Mining
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Studio Web
      </p>
      <ul>
       <li>
        <p>
         Agents
        </p>
       </li>
      </ul>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Studio Web.
    </p>
    <p>
     For more information, refer to
     <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/managing-access-to-studio-web">
      Managing access to Studio Web
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Task Mining
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed using Test Cloud
                                    organization-level roles. For information about the rights that
                                    organization-level roles grant in Task Mining, refer to
     <a href="https://docs.uipath.com/task-mining/automation-cloud/latest/user-guide/managing-access">
      Managing access and roles
     </a>
     in the
                                    Task Mining documentation.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e526">
    <ul>
     <li>
      <p>
       Test Manager
      </p>
     </li>
    </ul>
   </td>
   <td headers="d14416e529">
    <p>
     Managed from Test Manager.
    </p>
    <p>
     For information and instructions, refer to
     <a href="https://docs.uipath.com/test-suite/automation-cloud/latest/user-guide/managing-users-and-groups">
      User and group access management
     </a>
     .
    </p>
   </td>
  </tr>
 </tbody>
</table>

### Assigning roles to an account

If you want to control the access a certain account has in a service at a more granular level, but you do not want to add new roles to an entire group, you can explicitly add the account to the service and assign one or more service-level roles to it directly.

For information about the available roles and instructions, refer to the documentation for the target service, as previously described.

## Assigning folder- or project-level roles

Depending on the service you use, you can assign:

* folder roles from Orchestrator.
* project roles from:
  + Document Understanding
  + IXP
  + Test Manager
  + Task Mining

For more information, refer to the table in [Assigning and managing service-level roles](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/role-management#assigning-and-managing-service-level-roles).

## Exporting role assignments

To export role assignments, take the following steps:

1. Navigate to **Admin** at organization level.
2. Select **Accounts & local groups**.
3. Select **Download role assignments** for the roles you want to export.

The following table describes the fields from the role assignments file.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-FAB9FF99-5B15-4FA2-9596-DB5299826761__TABLE_ICK_RK1_XGC" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Field
   </th>
   <th>
    Description
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d14416e991">
    Id
   </td>
   <td headers="d14416e994">
    The unique identifier of the role assignment.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    RoleName
   </td>
   <td headers="d14416e994">
    The role name as displayed in the interface.
    <p>
     For example,
     <strong>
      Folder
                                    Administrator
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    RoleId
   </td>
   <td headers="d14416e994">
    The unique identifier of the role.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    RoleDescription
   </td>
   <td headers="d14416e994">
    The role description, as displayed in the interface.
    <p>
     For example,
     <strong>
      Folder Administrator
     </strong>
    </p>
    <p>
     For example,
     <strong>
      Folder
                                    Administrator
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    RoleType
   </td>
   <td headers="d14416e994">
    The role type, as defined by the user or the system:
    <ul>
     <li>
      <strong>
       Custom
      </strong>
      : Role defined by a user.
     </li>
     <li>
      <strong>
       BuiltIn
      </strong>
      : Role present by default Administration
                                    portal.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    RoleAssignmentType
   </td>
   <td headers="d14416e994">
    The role assignment type when it was created, which can be one of the
                              following two options:
    <ul>
     <li>
      <strong>
       Custom
      </strong>
      : Assignment made by the user.
     </li>
     <li>
      <strong>
       BuiltIn
      </strong>
      : Assignment made by default in the Administration
                                    portal.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    Scope
   </td>
   <td headers="d14416e994">
    The scope is a specific level in the organizational hierarchy that
                              serves as a boundary for certain actions, permissions, and objects. A
                              scope can be one of the following hierarchical options, represented as
                              IDs:
    <ul>
     <li>
      Organization
     </li>
     <li>
      Tenant
     </li>
     <li>
      Service
     </li>
     <li>
      Folder
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    ScopeWithDisplayNames
   </td>
   <td headers="d14416e994">
    The scope is a specific level in the organizational hierarchy that
                              serves as a boundary for certain actions, permissions, and objects. A
                              scope can be one of the following hierarchical options:
    <ul>
     <li>
      Organization
     </li>
     <li>
      Tenant
     </li>
     <li>
      Service
     </li>
     <li>
      Folder
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    ServiceName
   </td>
   <td headers="d14416e994">
    The name of the UiPath service that the role belongs to.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    SecurityPrincipalId
   </td>
   <td headers="d14416e994">
    The unique identifier for the identity of a user, group, etc.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    SecurityPrincipalType
   </td>
   <td headers="d14416e994">
    The identity type of a user, group, or robot.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    SecurityPrincipalEmail
   </td>
   <td headers="d14416e994">
    The email of the user. This field is blank in case the identity is
                              not a user.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    SecurityPrincipalDisplayName
   </td>
   <td headers="d14416e994">
    The name of the identity. This field is blank in case of directory
                              users.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    InheritedFromGroupName
   </td>
   <td headers="d14416e994">
    The group name from which the role assignment is inherited.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    InheritedFromGroupId
   </td>
   <td headers="d14416e994">
    Group identifier from which the role assignment is inherited.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    TenantName
   </td>
   <td headers="d14416e994">
    The name of the tenant where the assignment is made. This field is
                              blank in case of organization-level assignments.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    OrganizationName
   </td>
   <td headers="d14416e994">
    The name of the organization where the assignment is made.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    OrganizationId
   </td>
   <td headers="d14416e994">
    The identifier of the organization where the assignment is
                              made.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    TenantId
   </td>
   <td headers="d14416e994">
    The identifier of the tenant where the assignment is made. This field
                              is blank in case of organization-level assignments.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    CreatedBy
   </td>
   <td headers="d14416e994">
    The unique identifier of the user who creates the assignment.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    CreatedByDisplayName
   </td>
   <td headers="d14416e994">
    The name of the user who creates the assignment.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    CreatedOn
   </td>
   <td headers="d14416e994">
    The timestamp when the role is assigned.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    FolderName
   </td>
   <td headers="d14416e994">
    The name of the folder associated with the assignment.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    FolderKey
   </td>
   <td headers="d14416e994">
    The unique identifier of the folder associated with the
                              assignment.
   </td>
  </tr>
  <tr>
   <td headers="d14416e991">
    ProjectId
   </td>
   <td headers="d14416e994">
    The ID of the project (for example, Document Understanding or IXP)
                              associated with the assignment.
   </td>
  </tr>
 </tbody>
</table>