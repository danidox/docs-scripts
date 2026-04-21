---
title: "Roles"
visible: true
slug: "roles"
---

Roles are a collection of permissions and represent a more granular layer for managing user access, following the broader option of maintaining access through groups. You can add roles to either groups so that all member accounts inherit them, or to individual accounts.

Accounts and groups typically have an organization-level role and one or more service-level roles.

## Types of roles

The following types of roles can include several permissions at either organization level, or at service level:

* The built-in role is a predefined role that has specific permissions set by the platform. These roles can be used to grant users or groups the necessary permissions to perform certain operations.
* The custom role is a role that an organization administrator creates to meet the specific needs of their organization. This is particularly useful role for when none of the available built-in roles perfectly match the access a user or group should have.

## Scopes and categories

A scope is a specific level in the organizational hierarchy that serves as a boundary for certain actions, permissions, and objects. A scope can be an organization, a tenant, a service, or a folder, each with its own set of role assignments.
:::note
The **Manage access** menu is available within all possible scopes, descending from the organization level down to the project level.
:::
A category is a parameter for a custom role that you define for each scope, determining whether you apply the role within the same scope, or within a lower-level scope.

## Types of roles based on scopes and permissions

A role is defined by multiple permissions. Permissions can be specific to a certain scope.
:::note
The organization administrator role is a special role that grants access to all scopes: organization, tenant, service, and folder.
:::

The following types roles are based on scopes and permissions:

* The organization level role is a type of role you create at organization scope. This role type consists of permissions that apply exclusively within the organization scope. Organization-level roles:
  + Can be created only at the organization level.
  + Can include only permissions associated with organization-level products and services, such as:
    - Manage Access
    - Apps
    - Automation Ops
    - Insights (organization-level dashboards)
  + Can be assigned only at the organization level.
  + Cannot currently include permissions for tenant-level products (such as IXP or Document Understanding).
  + Cannot currently manage licensing quotas or other tenant-scoped licensing configurations.
* The global tenant role is a type of role you create at organization scope. You can apply this role type to all tenants within the organization. You can apply this role type to all tenants within the organization, but assignment is performed at tenant or service level. Global-tenant roles:
  + Are created at the organization level.
  + Can include permissions associated with organization-level products, as well as supported tenant-level products, such as:
    - IXP
    - Document Understanding
  + If created with IXP permissions, the role becomes visible in all tenants within the organization.
  + Can be assigned only at tenant or service level (not at organization level).
* The cross-service role is a type of role you create at tenant scope. This role type contains permissions from multiple services simultaneously.
* The service role is a type of role you create at service scope. This role type contains permissions from certain services.
* The project or folder role is a type of role you create at service scope that you exclusively assign at project or folder scope.

The following table classifies scopes, role types based on scopes and permissions, and examples of roles:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Scope
    </p>
   </th>
   <th>
    <p>
     Types of roles based on scopes and permissions
    </p>
   </th>
   <th>
    <p>
     Examples of roles
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d65063e132" rowspan="2">
    <p>
     Organization
    </p>
   </td>
   <td headers="d65063e135">
    <p>
     Organization level roles
    </p>
   </td>
   <td headers="d65063e138">
    <p>
     Insights Dashboard Viewer
    </p>
    <p>
     Organization Administrator
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d65063e135">
    <p>
     Global tenant roles
    </p>
   </td>
   <td headers="d65063e138">
    Note: A global tenant role can be created using the custom role functionality.
   </td>
  </tr>
  <tr>
   <td headers="d65063e132">
    <p>
     Tenant
    </p>
   </td>
   <td headers="d65063e135">
    <p>
     Cross-service roles
    </p>
   </td>
   <td headers="d65063e138">
    <p>
     Tenant Administrator
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d65063e132" rowspan="2">
    <p>
     Service
    </p>
   </td>
   <td headers="d65063e135">
    <p>
     Service roles
    </p>
   </td>
   <td headers="d65063e138">
    <p>
     Orchestrator Administrator
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d65063e135">
    <p>
     Folder or project roles
    </p>
   </td>
   <td headers="d65063e138">
    <p>
     Folder Administrator
    </p>
   </td>
  </tr>
 </tbody>
</table>

## Groups and roles

In the following table you can view the roles that are assigned to accounts when they are added to a group. For example, adding an account to the **Administrators** default group grants them the **Organization Administrator** role for the organization and the **Administrator** role within your services. This user can manage both organization-level roles from **Admin**, then select **Accounts and Groups**, as well as service-level roles.

| Group membership | Organization-level role | Service-level roles for Orchestrator |
| --- | --- | --- |
| Administrators | Organization Administrator | [Administrator](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles#administrator-role) |
| Automation Users | User | [Automation User](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles#automation-user) at folder level <sup>1</sup>  [Allow to be Automation User](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles#allow-to-be-automation-user) at tenant level |
| Automation Developers | User | [Automation User](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles#automation-user) at folder level <sup>1</sup>  [Folder Administrator](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles#folder-administrator) at folder level <sup>1</sup>  [Allow to be Automation User](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles#allow-to-be-automation-user) at tenant level  [Allow to be Folder Administrator](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles#allow-to-be-folder-administrator) at tenant level |
| Everyone | User | No roles. |
| Automation Express | User | [Allow to be Automation User](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles#allow-to-be-automation-user) at tenant level |
| [Custom group] | User | No roles by default, but you can [add roles to the group](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/role-management#role-assignments)  as needed. |

<sup>1</sup> The roles are assigned to the **Shared** modern folder, if it exists.
:::note
For information about roles across UiPath services, refer to [Role management](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/role-management#role-assignments).
:::

## Organization-level roles

The organization level represents the highest level of scope.

At organization level, the **Organization Administrator**, **User**, and **Insights Dashboard Viewer** roles are available. You cannot change these roles.

Organization administrators have permission to modify organization-level settings, such as security, Single Sign-On (SSO), and licensing settings. Therefore, the number of organization-level roles is limited. Additionally, organization administrators can grant organization-level permissions, as well as cascade down to tenant-, service-, and folder-level permissions.

Organization-level roles also include organization-level service permissions for services such as Apps and AutomationOps.
:::note
Licensing quota management is available through tenant-level roles (for example, the Tenant Administrator role).
:::

### Organization administrator role

This role grants access to every organization- and service-level feature within the organization. An account with this role can perform all administrative actions for the organization, such as creating or updating tenants, managing accounts, viewing organization audit logs, and so on. There can be multiple accounts with this role.

The organization administrator and the **Tenant Admin** roles are the only roles that allow access to the **Admin** section.

The first organization administrator for any given organization is appointed when the organization is created.
:::note
The organization administrator role is not an assignable role. To have this role assigned to you, you need to be part of the **Administrators** group.
:::

To grant this role to others, the organization administrator can add user accounts to the **Administrators** group, which is one of the [default groups](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-accounts#default-local-groups).

The organization administrator role includes the following organization-level permissions, which cannot be changed, as described in the following table:

| Areas subject to permissions | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- |
| Usage charts and graphs | ✅ | ❌ | ❌ | ❌ |
| Tenants | ✅ | ✅ | ✅ | ✅ |
| Accounts and groups | ✅ | ✅ | ✅ | ✅ |
| Security settings | ✅ | ✅ | ❌ | ❌ |
| External applications | ✅ | ✅ | ✅ | ✅ |
| Licenses | ✅ | ✅ | ❌ | ❌ |
| API keys | ✅ | ❌ | ✅ | ❌ |
| Resource center (Help) | ✅ | ❌ | ❌ | ❌ |
| Audit logs | ✅ | ❌ | ❌ | ❌ |
| Organization settings | ✅ | ✅ | ❌ | ❌ |

### User role

This is the basic level of access within the UiPath ecosystem. Local user accounts automatically become members of the **Everyone** [group](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-accounts#groups), which grants them the **User** role.

This role is granted to all accounts that are in the default groups **Everyone**, **Automation Users**, or **Automation Developers**.

This role provides read-only access to pages, such as the **Home** page, **Resource Center** (if available).

The users can view and access the provisioned services for their current tenant. However, the content they can view and the actions they can perform within each service depends on the service-level roles assigned to their account.
:::note
All platform users are part of the **Everyone** group by default, regardless if they are local or directory users.
:::

To grant access to everyone to a specific service, the users need to have the **Everyone** group mapped at service level. For example, if you want to grant all users access to view ideas in Automation Hub, you can assign the **Everyone** group to a role in Automation Hub.

The available services that currently incorporate this mapping into roles and grant minimal rights within them are:

* Studio Web
* Apps
* Test Manager

### Insights dashboard viewer role
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

The **Insights Dashboard Viewer** role is a built-in role that grants access to organization-level dashboards in Insights and is assigned by the organization administrator.
:::note
Before assigning the **Insights Dashboard Viewer** role, you must ensure that users have access to the Insights service within any tenant of the organization.
:::

To assign the **Insights Dashboard Viewer** role, take the following steps:

1. Ensure that the user has access to Insights on any of their given tenants within the organization.
2. Navigate to **Admin**, then select **Manage access** at organization level.
3. On the **Role assignments** tab, select **Assign role**.
4. In the **Names** field, search for the user you want to assign a role to.
5. In the **Roles** field, check the **Insights Dashboard Viewer** box.
6. Select the **Assign** button to assign the role.

## Tenant-level roles

Tenant-level roles control the access rights of accounts within the tenant settings and configuration area. They also define the permitted actions within each of the UiPath services in a given tenant.

Most of the tenant-level roles in the platform are cross-service roles as they grant permissions across multiple services within a particular tenant.

Currently, **Tenant Administrator** is the only built-in role available at the tenant level.

### Tenant Administrator role

The **Tenant Administrator** role allows you to effectively delegate responsibilities. The role grants access to manage all resources<sup>1</sup> in the tenant, allowing operations such as role assignment, licensing management, and service provisioning.

The **Tenant Administrator** role can be assigned to multiple accounts.

<sup>1</sup>The following services support the **Tenant Administrator** role:

* Orchestrator (includes Actions, Processes, Integration Service)
* Data Service
* Document Understanding
* Task Mining
* Test Manager

#### Tenant Administrator role permissions

The following tables describe the Tenant Administrator role permissions:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th colspan="2" rowspan="2">
    Resource
   </th>
   <th colspan="5">
    Permissions
   </th>
   <th rowspan="2">
    Description
   </th>
  </tr>
  <tr>
   <th>
    View
   </th>
   <th>
    Create
   </th>
   <th>
    Delete
   </th>
   <th>
    Read
   </th>
   <th>
    Update
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d65063e874" rowspan="3">
    Centralized Access
   </td>
   <td headers="d65063e874">
    Administration page
   </td>
   <td headers="d65063e877 d65063e886">
    ✅
   </td>
   <td headers="d65063e877 d65063e889">
    ❌
   </td>
   <td headers="d65063e877 d65063e892">
    ❌
   </td>
   <td headers="d65063e877 d65063e895">
    ❌
   </td>
   <td headers="d65063e877 d65063e898">
    ❌
   </td>
   <td headers="d65063e880" rowspan="3">
    Grants permissions to centralized access, roles and
                                       role assignments.
   </td>
  </tr>
  <tr>
   <td headers="d65063e874">
    Role
   </td>
   <td headers="d65063e877 d65063e886">
    ❌
   </td>
   <td headers="d65063e877 d65063e889">
    ✅
   </td>
   <td headers="d65063e877 d65063e892">
    ✅
   </td>
   <td headers="d65063e877 d65063e895">
    ✅
   </td>
   <td headers="d65063e877 d65063e898">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e874">
    Role assignments
   </td>
   <td headers="d65063e877 d65063e886">
    ❌
   </td>
   <td headers="d65063e877 d65063e889">
    ✅
   </td>
   <td headers="d65063e877 d65063e892">
    ✅
   </td>
   <td headers="d65063e877 d65063e895">
    ✅
   </td>
   <td headers="d65063e877 d65063e898">
    ✅
   </td>
  </tr>
 </tbody>
</table>

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th colspan="2" rowspan="2">
    Resource
   </th>
   <th colspan="7">
    Permissions
   </th>
   <th rowspan="2">
    Description
   </th>
  </tr>
  <tr>
   <th>
    View
   </th>
   <th>
    Create
   </th>
   <th>
    Delete
   </th>
   <th>
    Read
   </th>
   <th>
    Update
   </th>
   <th>
    Edit
   </th>
   <th>
    Manage
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d65063e1008">
    Data
                                       Fabric
   </td>
   <td headers="d65063e1008">
    Permission
   </td>
   <td headers="d65063e1011 d65063e1020">
    ❌
   </td>
   <td headers="d65063e1011 d65063e1023">
    ❌
   </td>
   <td headers="d65063e1011 d65063e1026">
    ❌
   </td>
   <td headers="d65063e1011 d65063e1029">
    ❌
   </td>
   <td headers="d65063e1011 d65063e1032">
    ❌
   </td>
   <td headers="d65063e1011 d65063e1036">
    ❌
   </td>
   <td headers="d65063e1011 d65063e1039">
    ✅
   </td>
   <td headers="d65063e1014">
    Grants administrator permissions and is equivalent
                                       to the Data Fabric Administrator role.
   </td>
  </tr>
 </tbody>
</table>

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th colspan="2" rowspan="2">
    Resource
   </th>
   <th colspan="4">
    Permissions
   </th>
   <th rowspan="2">
    Description
   </th>
  </tr>
  <tr>
   <th>
    Create
   </th>
   <th>
    Delete
   </th>
   <th>
    Read
   </th>
   <th>
    Update
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d65063e1106" rowspan="12">
    Document Understanding
   </td>
   <td headers="d65063e1106">
    Classifier
   </td>
   <td headers="d65063e1109 d65063e1118">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1121">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ✅
   </td>
   <td headers="d65063e1112" rowspan="12">
    Grants administrator permissions and is equivalent
                                       to the Document Understanding Administrator role.
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Data Set Export
   </td>
   <td headers="d65063e1109 d65063e1118">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1121">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Documents
   </td>
   <td headers="d65063e1109 d65063e1118">
    ❌
   </td>
   <td headers="d65063e1109 d65063e1121">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1124">
    ❌
   </td>
   <td headers="d65063e1109 d65063e1127">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Document Type
   </td>
   <td headers="d65063e1109 d65063e1118">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1121">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Extractor
   </td>
   <td headers="d65063e1109 d65063e1118">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1121">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Monitor Processed Documents
   </td>
   <td headers="d65063e1109 d65063e1118">
    ❌
   </td>
   <td headers="d65063e1109 d65063e1121">
    ❌
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Monitor Processed Documents Detail
   </td>
   <td headers="d65063e1109 d65063e1118">
    ❌
   </td>
   <td headers="d65063e1109 d65063e1121">
    ❌
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Monitor Project Performance
   </td>
   <td headers="d65063e1109 d65063e1118">
    ❌
   </td>
   <td headers="d65063e1109 d65063e1121">
    ❌
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Project
   </td>
   <td headers="d65063e1109 d65063e1118">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1121">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Project Version
   </td>
   <td headers="d65063e1109 d65063e1118">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1121">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Project Version Label
   </td>
   <td headers="d65063e1109 d65063e1118">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1121">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1106">
    Tenant Settings
   </td>
   <td headers="d65063e1109 d65063e1118">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1121">
    ❌
   </td>
   <td headers="d65063e1109 d65063e1124">
    ✅
   </td>
   <td headers="d65063e1109 d65063e1127">
    ✅
   </td>
  </tr>
 </tbody>
</table>

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th colspan="2" rowspan="2">
    Resource
   </th>
   <th colspan="7">
    Permissions
   </th>
   <th rowspan="2">
    Description
   </th>
  </tr>
  <tr>
   <th>
    View
   </th>
   <th>
    Create
   </th>
   <th>
    Delete
   </th>
   <th>
    Read
   </th>
   <th>
    Update
   </th>
   <th>
    Edit
   </th>
   <th>
    Manage
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d65063e1390">
    Licensing
   </td>
   <td headers="d65063e1390">
    Quota
   </td>
   <td headers="d65063e1393 d65063e1402">
    ❌
   </td>
   <td headers="d65063e1393 d65063e1405">
    ❌
   </td>
   <td headers="d65063e1393 d65063e1408">
    ❌
   </td>
   <td headers="d65063e1393 d65063e1411">
    ❌
   </td>
   <td headers="d65063e1393 d65063e1414">
    ❌
   </td>
   <td headers="d65063e1393 d65063e1418">
    ❌
   </td>
   <td headers="d65063e1393 d65063e1421">
    ✅
   </td>
   <td headers="d65063e1396">
    Grants permissions to manage quotas.
   </td>
  </tr>
 </tbody>
</table>

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th colspan="2" rowspan="2">
    Resource
   </th>
   <th colspan="4">
    Permissions
   </th>
   <th rowspan="2">
    Description
   </th>
  </tr>
  <tr>
   <th>
    View
   </th>
   <th>
    Create
   </th>
   <th>
    Delete
   </th>
   <th>
    Edit
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d65063e1488" rowspan="18">
    Orchestrator
   </td>
   <td headers="d65063e1488">
    Action Design
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
   <td headers="d65063e1494" rowspan="18">
    Grants administrator permissions and is equivalent
                                       to the Orchestrator Administrator role.
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Alerts
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    App Versions
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Audit
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Background Tasks
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ❌
   </td>
   <td headers="d65063e1491 d65063e1506">
    ❌
   </td>
   <td headers="d65063e1491 d65063e1509">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Libraries
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    License
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Machines
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Packages
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Robots
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Roles
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Settings
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Solution Deployments
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Solution Packages
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Tags
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Units
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Users
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1488">
    Webhooks
   </td>
   <td headers="d65063e1491 d65063e1500">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1503">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1506">
    ✅
   </td>
   <td headers="d65063e1491 d65063e1509">
    ✅
   </td>
  </tr>
 </tbody>
</table>

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" data-condition="(Deployment=Cloud)" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th colspan="2" rowspan="2">
    Resource
   </th>
   <th colspan="4">
    Permissions
   </th>
   <th rowspan="2">
    Description
   </th>
  </tr>
  <tr>
   <th>
    View
   </th>
   <th>
    Assign
   </th>
   <th>
    Remove
   </th>
   <th>
    Edit
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d65063e1875" rowspan="2">
    Task Mining
   </td>
   <td headers="d65063e1875">
    Manage Access
   </td>
   <td headers="d65063e1878 d65063e1887">
    ✅
   </td>
   <td headers="d65063e1878 d65063e1890">
    ❌
   </td>
   <td headers="d65063e1878 d65063e1893">
    ❌
   </td>
   <td headers="d65063e1878 d65063e1896">
    ✅
   </td>
   <td headers="d65063e1881" rowspan="2">
    Grants administrator permissions and is equivalent
                                       to the Task Mining Administrator role.
   </td>
  </tr>
  <tr>
   <td headers="d65063e1875">
    Role
   </td>
   <td headers="d65063e1878 d65063e1887">
    ❌
   </td>
   <td headers="d65063e1878 d65063e1890">
    ✅
   </td>
   <td headers="d65063e1878 d65063e1893">
    ✅
   </td>
   <td headers="d65063e1878 d65063e1896">
    ❌
   </td>
  </tr>
 </tbody>
</table>

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th colspan="2" rowspan="2">
    Resource
   </th>
   <th colspan="15">
    Permissions
   </th>
   <th rowspan="2">
    Description
   </th>
  </tr>
  <tr>
   <th>
    View
   </th>
   <th>
    Create
   </th>
   <th>
    Delete
   </th>
   <th>
    Read
   </th>
   <th>
    Update
   </th>
   <th>
    Edit
   </th>
   <th>
    Assign
   </th>
   <th>
    Toggle
   </th>
   <th>
    AutomatedExecution
   </th>
   <th>
    CreateAndUnlinkDefects
   </th>
   <th>
    ExecutePerformanceTest
   </th>
   <th>
    ManualExecution
   </th>
   <th>
    OverrideTestResult
   </th>
   <th>
    SmartTestGeneration
   </th>
   <th>
    TestExecutionAssignment
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d65063e1995" rowspan="10">
    Test Manager
   </td>
   <td headers="d65063e1995">
    Performance
                                       Scenarios
   </td>
   <td headers="d65063e1998 d65063e2007">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2010">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2013">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2016">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2019">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2023">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2026">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2029">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2032">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2035">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2038">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2042">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2045">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2048">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2051">
    ❌
   </td>
   <td headers="d65063e2001" rowspan="10">
    Grants administrator permissions and is equivalent
                                       to the Test Manager administrator role.
   </td>
  </tr>
  <tr>
   <td headers="d65063e1995">
    Project
   </td>
   <td headers="d65063e1998 d65063e2007">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2010">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2013">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2016">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2019">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2023">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2026">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2029">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2032">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2035">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2038">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2042">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2045">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2048">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2051">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1995">
    Project Settings
   </td>
   <td headers="d65063e1998 d65063e2007">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2010">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2013">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2016">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2019">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2023">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2026">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2029">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2032">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2035">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2038">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2042">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2045">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2048">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2051">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1995">
    Prompt
   </td>
   <td headers="d65063e1998 d65063e2007">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2010">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2013">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2016">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2019">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2023">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2026">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2029">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2032">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2035">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2038">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2042">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2045">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2048">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2051">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1995">
    Requirement
   </td>
   <td headers="d65063e1998 d65063e2007">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2010">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2013">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2016">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2019">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2023">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2026">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2029">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2032">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2035">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2038">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2042">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2045">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2048">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2051">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1995">
    Role
   </td>
   <td headers="d65063e1998 d65063e2007">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2010">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2013">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2016">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2019">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2023">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2026">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2029">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2032">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2035">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2038">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2042">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2045">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2048">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2051">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1995">
    Task Permissions
   </td>
   <td headers="d65063e1998 d65063e2007">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2010">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2013">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2016">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2019">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2023">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2026">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2029">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2032">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2035">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2038">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2042">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2045">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2048">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2051">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d65063e1995">
    Test Case
   </td>
   <td headers="d65063e1998 d65063e2007">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2010">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2013">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2016">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2019">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2023">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2026">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2029">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2032">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2035">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2038">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2042">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2045">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2048">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2051">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1995">
    Test Execution
   </td>
   <td headers="d65063e1998 d65063e2007">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2010">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2013">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2016">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2019">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2023">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2026">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2029">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2032">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2035">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2038">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2042">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2045">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2048">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2051">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d65063e1995">
    Test Set
   </td>
   <td headers="d65063e1998 d65063e2007">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2010">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2013">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2016">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2019">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2023">
    ✅
   </td>
   <td headers="d65063e1998 d65063e2026">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2029">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2032">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2035">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2038">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2042">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2045">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2048">
    ❌
   </td>
   <td headers="d65063e1998 d65063e2051">
    ❌
   </td>
  </tr>
 </tbody>
</table>

To view the available Tenant Administrator role permissions, take the following steps:

1. Navigate to **Admin**.
2. Select **Manage access** at organization level.
3. Select the **Roles** tab.
4. In the **Role Name** column, select the **Tenant Administrator** role. You can now view the **Tenant Administrator** role permissions in the expanded panel.
   ![Tenant Administrator role detailed permissions](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/616579)

### Known limitations

The following known limitations affect the tenant-level roles:

* The rest of the tenant-level services are currently not supported, and users that only hold the Tenant Administrator role cannot access these services.
* The **Tenant Administrator** cannot access organization-level menus from the interface.
* On the **Admin > Tenants > Services** screen, the **Tenant Administrator** can view enabled services, but cannot add or remove services.
* On the **Admin > Tenants > Manage access** screen, the **Tenant Administrator** can view tenants they do not administer. However, if they access these tenants, they cannot perform any actions.

## Service-level roles

Service-level roles control access rights and permitted actions within each of your UiPath services, such as the Orchestrator service, or Data Fabric. The permissions for each service are managed within the service itself, not from the organization **Admin** page.

To grant permissions for a service to accounts, you can perform the following actions:

* In the selected service, assign service-level roles to a [group](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-accounts#groups) to grant those roles to all member accounts.
* Add accounts to a group that already has the required service-level roles by navigating to **Admin**, then select **Accounts and Groups**.
* In the selected service, [assign roles to an account](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/role-management#assigning-and-managing-service-level-roles).

For the following services, you can create and manage some services-level roles that are external to the service, at platform level:

* Apps
* Automation Ops
* Document Understanding
* IXP

## Folder- or project-level roles

The folder or project is a scope you manage at service level.

Folder- and project-level roles define the set of permissions assigned to users, determining their ability to access, manage, and interact with specific resources and functionalities within automation workflows.

Depending on the service you use, you can assign folder- or project-level roles, as follows:

* Folder roles:
  + Orchestrator
* Project roles:
  + Document Understanding
  + IXP
  + Test Manager
  + Task Mining

## Custom roles

![](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555)
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

### Custom service roles

Custom service roles are user-defined permission sets that allow you to tailor access controls to your specific needs, offering more granular control than default roles.

To create custom roles at service level, navigate to **Manage access** at service level, where you can define roles, and select your preferred scope and permissions.

Currently, you can create custom service roles for the following services:

* Apps
* Document Understanding
* IXP
* Studio Web

### Custom cross-service roles

Custom cross-service roles are user-defined roles that grant tailored permissions across multiple UiPath services, allowing you to enforce consistent, fine-grained access control platform-wide.

To create custom roles at tenant level, navigate to **Manage access** at tenant level, where you can define roles, and select your preferred scope and permissions.

### Platform-related permissions

When creating custom roles, in addition to service-specific permissions, you can assign permissions related to platform-level functionality, such as Authorization, or Licensing.

Platform-related permissions are available for custom roles created at both the organization and tenant levels.

The following sections list the available platform permissions.

#### Organization-level platform permissions

* **Standard permissions**:
  + Authorization/Action: Allows users to view the available authorization actions (permissions) when creating or viewing a custom role.
  + Authorization/Role: Allows users to view, create, edit, or delete custom roles on the **Roles** tab in **Manage access**.
  + Authorization/Role assignment: Allows users to view, create, update, or delete role assignments on the **Role assignments** tab in **Manage access**.
* **Additional permissions**:
  + Authorization/Roles assignment - Allows users to export role assignment data from the user interface.

#### Tenant-level platform permissions

* **Standard permissions**:
  + Authorization/Action: Allows users to view the available authorization actions (permissions) when creating or viewing a custom role.
  + Authorization/Role: Allows users to view, create, edit, or delete custom roles on the **Roles** tab in **Manage access**.
  + Centralized access: Allows users to access both **Roles** and **Role assignments** tabs within a tenant.
  + Authorization/Role assignment: Allows users to view, create, update, or delete role assignments on the **Role assignments** tab in **Manage access**.
* **Additional permissions**:
  + Authorization/Roles assignment - Allows users to export role assignment data from the user interface at the tenant level.
  + Licensing - Manage quotas for a tenant in Licensing: Allows users to view and manage tenant licensing quotas, such as license allocation limits and usage.