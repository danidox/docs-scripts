---
title: "Configuring process app security"
visible: true
slug: "configuring-process-app-security-"
---

To restrict the data users have access to when editing transformations, you can set the process app security type for Process Mining process apps in the `input.json` file. You can configure app security using the `app_security_mode` setting. This is an overview of the possible values of the `app_security_mode` setting.

:::note
It is recommended to use the `system_managed` option.
:::

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <tbody>
  <tr>
   <td>
    <p>
     <strong>
      Value
     </strong>
    </p>
   </td>
   <td>
    <p>
     <strong>
      Description
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td>
    <code>
     system_managed
    </code>
    (default)
   </td>
   <td>
    <p>
     A SQL user is created automatically per process app. This ensures that users editing transformations in
     <strong>
      Process Mining
     </strong>
     can only query data that belongs to the process apps for which they have edit permissions.
    </p>
    <ul>
     <li>
      <p>
       Passwords are rotated on every use.
      </p>
     </li>
    </ul>
    Note:
    <p>
     This requires SQL authentication on the
     <strong>
      Process Mining
     </strong>
     data warehouse SQL Server.
    </p>
    The SQL user used in the connection strings used to connect to the
    <code>
     AutomationSuite_ProcessMining_Warehouse
    </code>
    database must have at least the following server-level and database-level roles both during and post-installation to enable
                              per app security:
    <ul>
     <li>
      <strong>
       Server role
      </strong>
      :
      <code>
       securityadmin
      </code>
      or
      <code>
       MS_LoginManager
      </code>
      . See the official Microsoft documentation on
      <a href="https://learn.microsoft.com/en-us/azure/azure-sql/database/security-server-roles?view=azuresql#fixed-server-level-roles">
       Fixed server-level roles
      </a>
      .
     </li>
    </ul>
    <ul>
     <li>
      <strong>
       Database-level roles
      </strong>
      :
      <code>
       db_securityadmin
      </code>
      and
      <code>
       db_accessadmin
      </code>
      . See the official Microsoft documentation on
      <a href="https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver16">
       Database-level roles
      </a>
      .
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td>
    <p>
     <code>
      single_account
     </code>
    </p>
   </td>
   <td>
    <p>
     One account is created that is used for all process apps.
    </p>
    <p>
     This means that when editing transformations in
     <strong>
      Process Mining
     </strong>
     , users can query data from other process apps.
    </p>
    Note:
The SQL user used in the connection strings used to connect to the
    <code>
     AutomationSuite_ProcessMining_Warehouse
    </code>
    must have at least the following database-level roles and permissions both during and post-installation to enable per app
                              security:
    <ul>
     <li>
      <strong>
       Database-level roles
      </strong>
      :
      <code>
       db_securityadmin
      </code>
      and
      <code>
       db_accessadmin
      </code>
      . See the official Microsoft documentation on
      <a href="https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver16">
       Database-level roles
      </a>
      .
     </li>
     <li>
      <p>
       read/write access on schema, tables and views.
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/275735)

## Steps

1. Turn on SQL Authentication for the Process Mining data warehouse SQL Server. See the official Microsoft documentation on [Change server authentication mode](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/change-server-authentication-mode?view=sql-server-ver16).
2. Grant ALTER ANY LOGIN to the provisioning user of Process Mining.
3. Grant access to the `master` database to the provisioning user of Process Mining.
   :::note
   The SQL user used in the connection strings used to connect to the `master` database must have enough permissions to create login, users and roles.
   :::