---
title: "Migrating standalone products to Automation Suite"
visible: true
slug: "migrating-standalone-products-to-automation-suite"
---

For migrating your standalone product data to Automation Suite, you can follow one of the two processes available:

[A) full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/full-migration#performing-a-full-migration) or

[B) single tenant migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/using-the-migration-tool#performing-a-single-tenant-migration)

You must choose one process to use, you cannot use both.

This page describes the differences between the two options to help you choose which one to use.

## How each process works

Both processes are for moving your data from the standalone installation of Orchestrator to the Orchestrator service in Automation Suite, but there are some differences.

The **full installation migration** process essentially links your standalone Orchestrator database to Automation Suite, so all the data it includes is available in Automation Suite. You should use this method if, in addition to Orchestrator, you also want to migrate other products and services.

The full migration option ensures high-fidelity data transfer between the standalone product databases and the automatically created Automation Suite databases. If you do not want to use the default Automation Suite databases, you can opt for your own migrated databases provided that you update their connection strings.

The **single tenant migration** process, on the other hand, uses the Automation Cloud™ Migration Tool to strictly copy the entities present in your standalone Orchestrator. The tool retrieves them from standalone Orchestrator over API and then writes them in Automation Suite over API.

## Differences between the migration options

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    &nbsp;
   </th>
   <th>
    Full installation migration
   </th>
   <th>
    <p>
     Single tenant migration
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d11083e70">
    <p>
     <strong>
      Scope
     </strong>
    </p>
   </td>
   <td headers="d11083e71">
    <ul>
     <li>
      <strong>
       Tenants
      </strong>
      : All tenants.
     </li>
     <li>
      <strong>
       Entities
      </strong>
      : Everything that is stored in the database - for example machines, user-machine mappings, and role assignments.
     </li>
     <li>
      <strong>
       Orchestrator configurations
      </strong>
      : Orchestrator in Automation Suite is configured exactly as it was in your standalone installation.
     </li>
    </ul>
   </td>
   <td headers="d11083e73">
    <ul>
     <li>
      <strong>
       Tenants
      </strong>
      : Only the targeted tenant.
      <p>
       But you can run the tool multiple times to migrate several or all tenants.
      </p>
     </li>
     <li>
      <strong>
       Entities
      </strong>
      : Only migrates the Orchestrator entities listed
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/using-the-migration-tool#entities-being-migrated">
       here
      </a>
      .
     </li>
     <li>
      <strong>
       Orchestrator configurations
      </strong>
      : Some Orchestrator settings are migrated, but not all.
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/using-the-migration-tool#entities-being-migrated">
       Details...
      </a>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d11083e70">
    <p>
     <strong>
      Outcome
     </strong>
    </p>
   </td>
   <td headers="d11083e71">
    <p>
     Orchestrator in Automation Suite contains exactly the same data and is configured in exactly the same way as your standalone
                                 Orchestrator.
    </p>
   </td>
   <td headers="d11083e73">
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
   <td headers="d11083e70">
    <p>
     <strong>
      Prerequisites
     </strong>
    </p>
   </td>
   <td headers="d11083e71">
    <p>
     Requires that you upgrade standalone Orchestrator to a version that matches the targeted Automation Suite version.
    </p>
   </td>
   <td headers="d11083e73">
    <p>
     Supports direct migration from any supported standalone Orchestrator version 2019.4.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11083e70">
    <p>
     <strong>
      Organization hierarchy
     </strong>
    </p>
   </td>
   <td headers="d11083e71">
    You have two options:
    <ul>
     <li>
      Create one Automation Suite organization for each standalone tenant. For example, if you have
                                          three standalone tenants, the result of the migration
                                          will be three Automation Suite organizations with one
                                          tenant each, as illustrated in the following image:
      <br/>
      <button>
       <img alt="docs image" src="https://docs.uipath.com/api/binary/automation-suite/2/309203/483850"/>
      </button>
      <br/>
     </li>
     <li>
      Create a single Automation Suite organization containing
                                          multiple standalone tenants, as illustrated in the
                                          following image:
      <br/>
      <button>
       <img alt="docs image" src="https://docs.uipath.com/api/binary/automation-suite/2/309203/483846"/>
      </button>
      <br/>
      Note: When migrating multiple
                                             standalone tenants to one Automation Suite
                                             organization, you may encounter user conflicts. For
                                             details on how to manage such conflicts, see
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/merging-organizations-in-automation-suite#solving-user-conflicts">
       Solving user conflicts
      </a>
      .
     </li>
    </ul>
   </td>
   <td headers="d11083e73">
    <p>
     You can migrate your tenants to the same organization, or to several organizations, as needed.
    </p>
   </td>
  </tr>
 </tbody>
</table>

## Combined migration scenario for testing

Although typically you can only use one migration option or the other, this sample scenario describes a use case where you could use both.

If you intend to perform the full migration, the Automation Cloud Migration Tool can support the migration process by allowing you to more easily set up a test environment in Automation Suite with production data that you can use for end-to-end testing.

If you want to first test Automation Suite and would like to do so on your actual Orchestrator data, here is what the full process might look like:

1. Deploy Automation Suite in a test or development environment.
2. Migrate partial data from standalone Orchestrator to Automation Suite using the Cloud Migration Tool. See [Single tenant migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/using-the-migration-tool#performing-a-single-tenant-migration) for instructions. This allows you to perform a proof-of-concept or trial on a real dataset. At this point, you have your Orchestrator data, but you are using the default Automation Suite and Orchestrator configurations. You can, for example, readily test run a process, but you cannot readily log in with an SSO account.
3. With the partial migration complete, validate critical scenarios and use cases and address any issues.
4. Upgrade the test environment for standalone Orchestrator to the desired version. Follow the instructions in [Updating using the Windows installer](https://docs.uipath.com/installation-and-upgrade/docs/updating-using-the-windows-installer) and make sure to put the environment in read-only mode.
5. Perform a test migration to Automation Suite following the [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/full-migration#performing-a-full-migration) instructions.
6. Redirect all test users and robots to the new Automation Suite test environment.
7. Address any issues during and after the migration, validate the process end-to-end.
8. Deploy Automation Suite in a production environment.
9. Upgrade you production environment for standalone Orchestrator to the desired version. Follow the instructions in [Updating using the Windows installer](https://docs.uipath.com/installation-and-upgrade/docs/updating-using-the-windows-installer) and make sure to put the environment in read-only mode.
10. Perform the full production migration to Automation Suite following the [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/full-migration#performing-a-full-migration) instructions.
    :::important
    This overwrites the previously migrated data, which is lost. With this migration, all your custom configurations are applied, and your Orchestrator entities are also migrated. You should see the same information in Automation Suite as you do in your standalone Orchestrator.
    :::
11. Redirect all production users and robots to the new Automation Suite production environment.

## Frequently asked questions

### Can I migrate only some of my tenants using the full installation migration?

If needed, you can discard tenants from standalone Orchestrator that you no longer need (for example, testing tenants). If you do not [create an organization and tenant pair](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/pre-migration-steps#pre-migration-steps) for a tenant from your standalone installation, it is not available in Automation Suite. The data for any discarded tenants is still migrated to the new database, but the tenants are not accessible from the user interface.

:::important
**We recommend caution when using this approach** because this operation is irreversible and you cannot later add any of the discarded tenants to Automation Suite.
:::