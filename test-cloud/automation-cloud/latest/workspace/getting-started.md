---
title: "Getting started with the platform"
visible: true
slug: "getting-started"
---

## Hierarchies and inheritance

The UiPath platform operates on a hierarchy system with different levels, allowing for organized and efficient setting management across multiple companies and departments, as described in the following table:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-AA2BAB8E-BEEE-4245-934E-57BA70CF2379__TABLE_RTJ_2FF_L2C" summary="">
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
   <td headers="d109981e37">
    <p>
     <strong>
      Organization
     </strong>
    </p>
   </td>
   <td headers="d109981e43">
    <p>
     An organization typically represents a single company. An
                                    organization admin manages organization settings.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d109981e37">
    <p>
     <strong>
      Tenant
     </strong>
    </p>
   </td>
   <td headers="d109981e43">
    <p>
     A tenant is a unique and separate division or department within
                                    an organization. Each tenant has its own resources, separated
                                    from other tenants within the organization.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d109981e37">
    <p>
     <strong>
      Service
     </strong>
    </p>
   </td>
   <td headers="d109981e43">
    <p>
     Services represent various UiPath web products, such as
                                    Orchestrator, Insights, or Action Center. Each service does a
                                    unique job in the automation process. The services can be
                                    assigned to a tenant for their individual automation needs.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d109981e37">
    <p>
     <strong>
      Folder
     </strong>
    </p>
   </td>
   <td headers="d109981e43">
    <p>
     Folders are a division under a tenant, and are used as containers
                                    for different resources, such as automations, robots, assets,
                                    and others. Folders provide an efficient way to manage access
                                    rights and help set fine-grained permissions.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d109981e37">
    <p>
     <strong>
      User accounts, Robot accounts, Groups, and External
                                       apps
     </strong>
    </p>
   </td>
   <td headers="d109981e43">
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

There are two primary user persona categories, administrators and non-administrators, and they encompass distinct roles and responsibilities within the platform. This page is dedicated to illustrating the typical journey taken by both personas when they first start using the platform.

The platform automatically categorizes users into different implicit user personas based on the type of license they possess. These implicit user personas are used to tailor the user experience to their specific needs and responsibilities.

* Admin users: Admin users are not mapped based on their user licenses but based on their membership in the **Administrators** user group.
* Non admin users: Non-admin users are mapped based on their user licenses.

### Admin user journey

Admin users are responsible for configuring and managing the platform settings for their organization. They have the authority to define settings, create tenants, manage licenses, and configure accounts and groups. The following table describes a common journey for admin users during the initial configuration:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Area
    </p>
   </th>
   <th>
    <p>
     Steps
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d109981e194">
    <p>
     <strong>
      Sign-up/sign in
     </strong>
    </p>
   </td>
   <td headers="d109981e197">
    <p>
     Create an account and create your organization.
    </p>
    <p>
     Sign in to access your organization.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d109981e194">
    <p>
     <strong>
      User interface
     </strong>
    </p>
   </td>
   <td headers="d109981e197">
    <p>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d109981e194">
    <strong>
     Preferences
    </strong>
   </td>
   <td headers="d109981e197">
    <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-user-preferences#managing-user-preferences">
     Customize your account preferences
    </a>
    , such as theme, language, and notifications.
   </td>
  </tr>
  <tr>
   <td headers="d109981e194">
    <p>
     <strong>
      Organization settings
     </strong>
    </p>
   </td>
   <td headers="d109981e197">
    <p>
     Configure organization-specific settings and preferences:
    </p>
    <ul>
     <li>
      <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-organization-settings#managing-organization-settings">
       Manage organization settings.
      </a>
     </li>
     <li>
      <p>
       <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/authentication-settings#understanding-authentication-models">
        Configure authentication settings
       </a>
       .
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d109981e194">
    <p>
     <strong>
      Tenants
     </strong>
    </p>
   </td>
   <td headers="d109981e197">
    <p>
     <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-tenants#managing-tenants">
      Manage tenants
     </a>
     to separate different business areas, such as departments, geographical locations, business units, etc.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d109981e194">
    <p>
     <strong>
      Services
     </strong>
    </p>
   </td>
   <td headers="d109981e197">
    <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-services#managing-services">
     Manage services
    </a>
    for each tenant.
   </td>
  </tr>
  <tr>
   <td headers="d109981e194">
    <strong>
     Access control
    </strong>
   </td>
   <td headers="d109981e197">
    <p>
     Set up user accounts, groups, and permissions for efficient collaboration and access control.
    </p>
    <p>
     You can use preconfigured groups and roles for managing access and permissions. You can also create custom groups and roles.
    </p>
    <p>
     Create accounts, add them to groups to grant permissions, and also allocate user licenses.
    </p>
    <ul>
     <li>
      <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-groups#managing-accounts-and-local-groups-for-test-cloud-and-test-cloud-public-sector">
       Manage the accounts and groups
      </a>
      for your organization.
     </li>
     <li>
      <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-access#managing-access">
       Manage access
      </a>
      .
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d109981e194">
    <p>
     <strong>
      Licensing
     </strong>
    </p>
   </td>
   <td headers="d109981e197">
    <p>
     Manage licensing for the entire organization, individual tenants, and users:
    </p>
    <ul>
     <li>
      <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/allocating-licenses-to-tenants#assigning-licenses-to-tenants">
       Allocate robot and service licenses
      </a>
      to tenants.
     </li>
     <li>
      <p>
       <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/allocating-user-licenses#assigning-user-licenses">
        Allocate user licenses
       </a>
       .
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

### Non-admin user journey

Non-admin users are focused on using the platform's services to accomplish their tasks. They don't typically have administrative privileges but need to effectively utilize the platform's features.

The following table describes a common journey for non-admin users:

| Area | Steps |
| --- | --- |
| **Sign-up/sign in** | Sign in to access the platform via SSO. |
| **User interface** | Explore the user interface. |
| **Preferences** | [Customize your account preferences](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-user-preferences#managing-user-preferences), such as theme, language, and notifications. |
| **Services/Products** | Access and utilize services within the platform according to your role and tasks. |