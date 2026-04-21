---
title: "About migrating to a cloud offering"
visible: true
slug: "about-migrating-to-automation-cloud"
---

If you want to move to a cloud offering, you can migrate the most of your data from your existing setup to your new organization.

With a cloud offering, you gain access to multiple services that you can conveniently manage in a centralized manner and always stay up to date with the latest features, without the hassle of installation or maintenance.
:::note
Feature availability depends on the cloud offering you use. For details, refer to the [feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

## Setup before migration

Before starting the migration process, take the following steps, as described in the table, to set up a cloud offerinh:

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
     <strong>
      Step
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Operation
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Notes
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d80011e43">
    <p>
     1
    </p>
   </td>
   <td headers="d80011e47">
    <p>
     Sign in to your organization or sign up for Test Cloud.
    </p>
   </td>
   <td headers="d80011e51">
    For details on how to sign in, refer to .
                                 Note:
    <p>
     For Flex licensing users, create an organization using the
                                       Pro Trial plan. This plan allows you to complete a
                                       successful migration. Do not use other plans for setting up
                                       an organization for migration purposes.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80011e43">
    <p>
     2
    </p>
   </td>
   <td headers="d80011e47">
    <p>
     <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-organization-settings#managing-organization-settings">
      Manage your organization settings
     </a>
     .
    </p>
   </td>
   <td headers="d80011e51">
    Configure your organization name, site URL, and language.
   </td>
  </tr>
  <tr>
   <td headers="d80011e43">
    <p>
     3
    </p>
   </td>
   <td headers="d80011e47">
    <p>
     <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-tenants#managing-tenants">
      Create tenants
     </a>
     .
    </p>
   </td>
   <td headers="d80011e51">
    <p>
     If you want to match your on-premises configuration, create a tenant for each of your on-premises tenants, and provision the
                                    same services as in on premises.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80011e43">
    <p>
     4
    </p>
   </td>
   <td headers="d80011e47">
    <p>
     <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-groups#managing-user-accounts">
      Invite users
     </a>
     .
    </p>
   </td>
   <td headers="d80011e51">
    To add users to your organization, navigate to the Test Cloud Administration.
   </td>
  </tr>
  <tr>
   <td headers="d80011e43">
    <p>
     5
    </p>
   </td>
   <td headers="d80011e47">
    <p>
     <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/allocating-user-licenses#assigning-user-licenses">
      Allocate user licenses
     </a>
     .
    </p>
   </td>
   <td headers="d80011e51">
    Ensure users have the necessary licenses to use UiPath products and features.
                                 Note:
    <p>
     To obtain a license key for migration that extends your trial period, contact
     <a href="https://www.uipath.com/company/contact-us/cloud-platform-technical-support">
      support
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80011e43">
    <p>
     6
    </p>
   </td>
   <td headers="d80011e47">
    <a href="https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-access#managing-access">
     Assign roles to users
    </a>
    for each of the services, as needed.
   </td>
   <td headers="d80011e51">
    <p>
     For the Orchestrator service, we provide
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/default-roles">
      default roles
     </a>
     that include the necessary permissions for the main user personas.
    </p>
    <p>
     You can also
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-roles#creating-a-role">
      create custom roles
     </a>
     to replicate the same access model as in your on-premises Orchestrator.
    </p>
   </td>
  </tr>
 </tbody>
</table>

## Migrating UiPath products

To migrate services to a cloud offering, refer to the provided documentation links for existing processes and tools. While most services have migration tools available, some might require manual steps or additional support. Reach out to our [support team](https://www.uipath.com/company/contact-us/cloud-platform-technical-support) for more details.

To check product availability across delivery models, refer to our [Product availability](https://docs.uipath.com/overview/other/latest/overview/product-availability) documentation.

The following table describes the product and service migration available resources.

Legend:

✅ - Available

❌ - Not available

N/A - Not applicable

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Product/Service
    </p>
   </th>
   <th>
    <p>
     Automation Suite deployment availability
    </p>
   </th>
   <th>
    <p>
     Automation Suite to Test Cloud
                                    migration - available resources
    </p>
   </th>
   <th>
    <p>
     Standalone deployment availability
    </p>
   </th>
   <th>
    <p>
     Standalone to Test Cloud
                                    migration - available resources
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d80011e200">
    <p>
     <strong>
      Orchestrator
     </strong>
    </p>
   </td>
   <td headers="d80011e203">
    <p>
     ✅
    </p>
   </td>
   <td headers="d80011e206">
    <ul>
     <li>
      <p>
       <a href="https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/using-the-migration-tool">
        Migration Tool
       </a>
      </p>
     </li>
     <li>
      <p>
       <a href="https://marketplace.uipath.com/listings/orchestrator-manager">
        Orchestrator Manager
       </a>
      </p>
     </li>
    </ul>
   </td>
   <td headers="d80011e212">
    <p>
     ✅
    </p>
   </td>
   <td headers="d80011e215">
    <ul>
     <li>
      <p>
       <a href="https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/using-the-migration-tool">
        Migration Tool
       </a>
      </p>
     </li>
     <li>
      <p>
       <a href="https://marketplace.uipath.com/listings/orchestrator-manager">
        Orchestrator Manager
       </a>
      </p>
     </li>
     <li>
      <p>
       <a href="https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/manual-migration">
        Manual Migration
       </a>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d80011e200">
    <strong>
     Insights
    </strong>
   </td>
   <td headers="d80011e203">
    <p>
     ✅
    </p>
   </td>
   <td headers="d80011e206">
    <p>
     ❌
    </p>
   </td>
   <td headers="d80011e212">
    <p>
     ✅
    </p>
   </td>
   <td headers="d80011e215">
    <ul>
     <li>
      <a href="https://docs.uipath.com/insights/standalone/2023.10/user-guide/migrating-from-on-premises-to-cloud">
       Migrating from on-premises to cloud
      </a>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d80011e200">
    <p>
     <strong>
      Action Center
     </strong>
    </p>
   </td>
   <td headers="d80011e203">
    <p>
     ✅
    </p>
   </td>
   <td headers="d80011e206">
    <p>
     ❌
    </p>
   </td>
   <td headers="d80011e212">
    <p>
     ✅
    </p>
   </td>
   <td headers="d80011e215">
    <p>
     ❌
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d80011e200">
    <p>
     <strong>
      Test Manager
     </strong>
    </p>
   </td>
   <td headers="d80011e203">
    <p>
     ✅
    </p>
   </td>
   <td headers="d80011e206">
    <ul>
     <li>
      <a href="https://docs.uipath.com/test-suite/automation-cloud/latest/user-guide/export-project">
       Export
      </a>
      /
      <a href="https://docs.uipath.com/test-suite/automation-cloud/latest/user-guide/import-project">
       Import
      </a>
      process
     </li>
    </ul>
   </td>
   <td headers="d80011e212">
    <p>
     ✅
    </p>
   </td>
   <td headers="d80011e215">
    <ul>
     <li>
      <a href="https://docs.uipath.com/test-suite/automation-cloud/latest/user-guide/export-project">
       Export
      </a>
      /
      <a href="https://docs.uipath.com/test-suite/automation-cloud/latest/user-guide/import-project">
       Import
      </a>
      process
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>