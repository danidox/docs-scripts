---
title: "Getting started"
visible: true
slug: "getting-started-with-test-cloud"
---

This page provides an introduction to Test Cloud, and guides you in managing your application testing organization. The page shows information about the platform hierarchy, the specific application testing personas, and common user journeys.

## Hierarchies and inheritance

Test Cloud operates on the same platform capabilities as Automation Cloud. To get started with how to navigate through Test Cloud, you need to explore the hierarchy system based on which the platforms operate. The following table describes the platform layers:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-91D9E47C-665F-43DA-842F-47642A25F2F3__TABLE_NZF_FFF_L2C" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Layer
    </p>
   </th>
   <th>
    <p>
     Description
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d4821e47">
    <p>
     <strong>
      Organization
     </strong>
    </p>
   </td>
   <td headers="d4821e53">
    <p>
     An organization typically represents a single company. An
                              organization admin manages organization settings.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d4821e47">
    <p>
     <strong>
      Tenant
     </strong>
    </p>
   </td>
   <td headers="d4821e53">
    <p>
     A tenant is a unique and separate division or department within
                              an organization. Each tenant has its own resources, separated
                              from other tenants within the organization.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d4821e47">
    <p>
     <strong>
      Service
     </strong>
    </p>
   </td>
   <td headers="d4821e53">
    <p>
     Services represent various UiPath web products, such as
                              Orchestrator, Insights, or Action Center. Each service does a
                              unique job in the automation process. The services can be
                              assigned to a tenant for their individual automation needs.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d4821e47">
    <p>
     <strong>
      Folder
     </strong>
    </p>
   </td>
   <td headers="d4821e53">
    <p>
     Folders are a division under a tenant, and are used as containers
                              for different resources, such as automations, robots, assets,
                              and others. Folders provide an efficient way to manage access
                              rights and help set fine-grained permissions.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d4821e47">
    <p>
     <strong>
      User accounts, Robot accounts, Groups, and External
                                 apps
     </strong>
    </p>
   </td>
   <td headers="d4821e53">
    Identities used to assign access rights and
                           permissions.
    <ul>
     <li>
      <p>
       User accounts: Individual users with unique access based
                                    on assigned roles and licenses.
      </p>
     </li>
     <li>
      <p>
       Robot accounts: Used to run automated processes and have
                                    special permissions based on robot's role and automation
                                    requirements.
      </p>
     </li>
     <li>
      <p>
       Groups: Collections of users who share the same access,
                                    permissions, roles, and licenses.
      </p>
     </li>
     <li>
      <p>
       External apps: Third-party applications that interact
                                    with UiPath, each with its own permissions
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

## User personas

The user personas that interact with Test Cloud can be categorized as administrators and non-administrators. The primary distinction between these two user categories is that admin users are mapped based on their membership in the Administrators user group, while non-admin users are mapped based on their licenses. Both personas have distinct roles and responsibilities within the platform. The following table describes the Test Cloud-specific personas, and what classifies them as a certain user persona:

Table 1. Test Cloud user personas and their main responsibilities

| User persona | License |
| --- | --- |
| **Administrator**: Configure organization settings, user access controls, and oversee the efficient operation of the platform. | Administrators are not mapped based on license, but on their membership in the Administrators user group. For more information on organization administrators, visit [Managing organization administrators](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-organization-administrators). |
| **Application Tester**: Manages and executes tests, and handles other automated processes that contribute to the testing project management. | App Tester - Named User For more information on App Testers, visit [Test Cloud licensing](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/licensing-test-cloud#licensing). |
| **Application Test Developer**: Can perform the same tasks as an **Application Tester**, while being able to design test automations in Studio. | App Test Developer - Named User For more information on App Test Developers, visit [Test Cloud licensing](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/licensing-test-cloud#licensing). |

## User journeys

This section describes the general user journey for the two user persona categories in Test Cloud:

* **Administrators**: Responsible for configuring and managing the platform settings for their organization. They have authority to define settings, create tenants, manage licenses, and configure accounts and groups. The following areas describe a common journey for admin users during the initial configuration:
  1. Sign-up/sign-in: Create an account, and create your organization. Sign in to access your organization.
  2. User interface: Explore the user interface. For more information, visit [Exploring the user interface](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/exploring-the-test-cloud-user-interface#exploring-the-user-interface).
  3. Preferences: Customize your account preferences, such as theme, language, and notifications. For more information on platform preferences, visit [Managing user preferences](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-user-preferences).
  4. Organization settings: Configure organization-specific settings and preferences. For more information, visit [Manage organization settings](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-organization-settings) and [Configure authentication settings](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/authentication-settings).
  5. Tenants: Manage tenants to separate different business areas, such as departments, geographical locations, business units, etc. For more information, visit [Manage tenants](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-tenants).
  6. Services: Manage services for each tenant. For more information, visit [Managing services](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-services).
  7. Access control: Set up user accounts, groups, and permissions for efficient collaboration and access control. You can use preconfigured groups and roles for managing access and permissions. You can also create custom groups and roles. Create accounts, add them to groups to grant permissions, and also allocate user licenses. For more information, visit [Managing accounts and groups](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-accounts-and-groups) and [Managing access](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-access).
  8. Licensing: Manage licensing for the entire organization, individual tenants, and users. For more information, visit [Allocating licenses to tenants](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/allocating-licenses-to-tenants) and [Allocating user licenses](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/allocating-user-licenses).
* **Non-administrators**: Non-admin users are focused on using the services surfaced in Test Cloud to accomplish their application testing tasks. The following areas describe a common user journey for non-admin users:
  1. Sign-up/sign in: Sign in to access the platform via SSO.
  2. User interface: Explore the user interface.
  3. Preferences: Customize your account preferences, such as theme, language, and notifications. For more information on platform preferences, visit [Managing user preferences](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-user-preferences).
  4. Services/Products: Access and use services within the platform according to your role and tasks.

For more information on the common user journeys on the entire platform, visit [Getting started with the platform](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/getting-started).

## Migrating to Test Cloud

If you are considering migrating to Test Cloud from other UiPath platforms such as Automation Cloud, Automation Suite, or Standalone products, contact your sales representative. They can provide guidance for the following migration scenarios:

* Application testing migration: Moving your application testing processes to Test Cloud.
* Combined application testing and automation testing migration: Moving both application testing and automation testing processes to Test Cloud.
* Partial application testing migration: Moving only your application testing process to Test Cloud, while keeping automation testing on your current platform.

For recommendations on preparing for the migration to Test Cloud Dedicated, refer to [Migrate from Test Suite to Test Cloud](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/migrate-test-suite-to-test-cloud#migrate-from-test-suite-to-test-cloud)

For technical questions related to migration, reach out to the UiPath support team.