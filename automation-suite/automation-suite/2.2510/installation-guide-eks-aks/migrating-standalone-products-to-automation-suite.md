---
title: "Migrating standalone products to Automation Suite"
visible: true
slug: "migrating-standalone-products-to-automation-suite"
---

To migrate your standalone Orchestrator data to Automation Suite, you can use the UiPath Automation Cloud™ Migration Tool. The tool helps you run a **single tenant migration** process and copy strictly the entities present in your standalone Orchestrator. The tool retrieves these entities from standalone Orchestrator over API and then writes them in Automation Suite over API.

The tool can migrate to either Automation Cloud or Automation Suite, but this guide describes the process of migrating **to Automation Suite**. For instructions on migrating to Automation Cloud, see the [Automation Cloud documentation](https://docs.uipath.com/automation-cloud/docs/using-the-migration-tool) instead.

You can only use the Automation Cloud Migration Tool if:

* your standalone Orchestrator version is 2019.10.x, 2020.10.x, 2021.4.x,, 2021.10.x, or later.
* your Automation Suite version is 2021.10.x or later.

Before you run a tenant migration, review the details from the following table to understand the scope, results, and requirements.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Category
   </th>
   <th>
    Description
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d14868e44">
    <strong>
     Scope
    </strong>
   </td>
   <td headers="d14868e46">
    <ul>
     <li>
      <p>
       <strong>
        Tenants
       </strong>
       : Only the targeted tenant.
      </p>
      <p>
       But you can run the tool multiple times to migrate several or all tenants.
      </p>
     </li>
     <li>
      <strong>
       Entities
      </strong>
      : Only migrates the Orchestrator entities listed
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/using-the-migration-tool#entities-being-migrated">
       here
      </a>
      .
     </li>
     <li>
      <strong>
       Orchestrator configurations
      </strong>
      : Some Orchestrator settings are migrated, but not all.
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/using-the-migration-tool#entities-being-migrated">
       Details...
      </a>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d14868e44">
    <strong>
     Outcome
    </strong>
   </td>
   <td headers="d14868e46">
    <p>
     All your entities are copied over to Orchestrator, but Orchestrator in Automation Suite uses the default Automation Suite
                                 configuration.
    </p>
    <p>
     To get to the same setup you had in your standalone installation, you must perform a
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2022.10/admin-guide/configuration-checklist">
      first-time configuration of Automation Suite
     </a>
     , which you can do at any time - before or after migration.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d14868e44">
    <strong>
     Prerequisites
    </strong>
   </td>
   <td headers="d14868e46">
    Supports direct migration from any supported standalone Orchestrator version 2019.4.
   </td>
  </tr>
  <tr>
   <td headers="d14868e44">
    <strong>
     Organization hierarchy
    </strong>
   </td>
   <td headers="d14868e46">
    You can migrate your tenants to the same organization, or to several organizations, as needed.
   </td>
  </tr>
 </tbody>
</table>