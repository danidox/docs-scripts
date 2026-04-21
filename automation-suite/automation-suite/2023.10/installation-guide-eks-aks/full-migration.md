---
title: "Performing a full migration"
visible: true
slug: "full-migration"
---

The full migration is one of two ways in which you can migrate a standalone UiPath® product to Automation Suite. This method helps you migrate Orchestrator and other products and services. For more information, see [Migration options](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migrating-standalone-products-to-automation-suite#migrating-standalone-products-to-automation-suite).

We tested the migration for Orchestrator, Action Center, and Test Automation, which share the same database, as well as Insights.

The full migration options also ensures high-fidelity data transfer between the standalone product databases and the automatically created Automation Suite databases. If you do not want to use the default Automation Suite databases, you can opt for your own migrated databases provided that you update their connection strings.

To migrate from a standalone deployment to Automation Suite, take the following steps:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <tbody>
  <tr>
   <td>
    <p>
     Description
    </p>
   </td>
   <td>
    <p>
     Instructions
    </p>
   </td>
  </tr>
  <tr>
   <td>
    <p>
     1. Upgrade your
                                 standalone deployment.
    </p>
   </td>
   <td>
    <ol>
     <li>
      Upgrade your
                                    standalone installation to a version compatible with
                                    Automation Suite. Make sure to check the
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-compatibility-matrix#migration-compatibility-matrix">
       compatibility matrix
      </a>
      .
                                    Note: If you want to migrate Test Manager, ensure that the
                                       standalone Test Manager is upgraded to the same version
                                       as the standalone Orchestrator.
     </li>
    </ol>
   </td>
  </tr>
  <tr>
   <td>
    <p>
     2. Deploy Automation
                                 Suite.
    </p>
   </td>
   <td>
    <ol>
     <li>
      Deploy the
                                    targeted Automation Suite version.
      <ul>
       <li>
        Install Automation Suite.
        <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/installing-automation-suite#installing-automation-suite">
         Details...
        </a>
       </li>
      </ul>
     </li>
    </ol>
   </td>
  </tr>
  <tr>
   <td>
    <p>
     3. Make sure you meet
                                 the requirements.
    </p>
   </td>
   <td>
    <ol>
     <li>
      <p>
       Download
                                       and install the required tools to perform the migration.
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-prerequisites#migration-prerequisites">
        Details...
       </a>
      </p>
     </li>
    </ol>
   </td>
  </tr>
  <tr>
   <td>
    <p>
     4. Follow the
                                 pre-migration steps.
    </p>
   </td>
   <td>
    <ol>
     <li>
      <p>
       Save the
                                       connection strings and tenant names.
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/saving-the-connection-strings-and-tenant-names#step-1%3A-saving-the-connection-strings">
        Details...
       </a>
      </p>
     </li>
     <li>
      <p>
       Create
                                       your organizations in Automation Suite.
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/creating-your-organizations-in-automation-suite#step-2%3A-creating-your-organizations-in-automation-suite">
        Details...
       </a>
      </p>
     </li>
    </ol>
   </td>
  </tr>
  <tr>
   <td>
    5. Follow the migration
                              steps.
   </td>
   <td>
    <ol>
     <li>
      <p>
       Use the
                                       OrganizationMigrationApp tool to move your Identity
                                       organization data from standalone to Automation Suite.
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/moving-the-identity-organization-data-from-standalone-to-automation-suite#step-1%3A-moving-the-identity-organization-data-from-standalone-to-automation-suite">
        Details...
       </a>
      </p>
     </li>
     <li>
      Restore the
                                    standalone product database to the Automation Suite SQL
                                    Server instance or a different SQL Server instance.
      <p>
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/restoring-the-standalone-product-database#step-2%3A-restoring-the-standalone-product-database">
        Details...
       </a>
      </p>
     </li>
     <li>
      <p>
       Back up
                                       the platform database in Automation Suite.
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/backing-up-the-platform-database-in-automation-suite#step-3%3A-backing-up-the-platform-database-in-automation-suite">
        Details...
       </a>
      </p>
     </li>
     <li>
      <p>
       Merge
                                       organizations in Automation Suite.
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/merging-organizations-in-automation-suite#step-4%3A-merging-organizations-in-automation-suite">
        Details...
       </a>
      </p>
     </li>
     <li>
      <p>
       Update the
                                       migrated product connection strings.
      </p>
     </li>
     <li>
      <p>
       Migrating
                                       standalone Orchestrator.
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migrating-standalone-orchestrator#step-6%3A-migrating-standalone-orchestrator">
        Details...
       </a>
      </p>
     </li>
     <li>
      <p>
       Migrating
                                       standalone Insights.
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migrating-standalone-insights#step-7%3A-migrating-standalone-insights">
        Details...
       </a>
      </p>
     </li>
     <li>
      Migrating
                                    standalone Test Manager.
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migrating-standalone-test-manager#step-8%3A-migrating-standalone-test-manager">
       Details...
      </a>
     </li>
     <li>
      <p>
       Deleting
                                       the default tenant.
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/deleting-the-default-tenant#step-9%3A-deleting-the-default-tenant">
        Details...
       </a>
      </p>
     </li>
    </ol>
   </td>
  </tr>
  <tr>
   <td>
    <p>
     6. Follow the
                                 post-migration steps.
    </p>
   </td>
   <td>
    <ol>
     <li>
      <p>
       Remove old
                                       identity cache keys.
      </p>
     </li>
     <li>
      <p>
       Update the
                                       AD integration and configuration.
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/updating-ad-integration-and-authentication#step-2%3A-updating-ad-integration-and-authentication">
        Details...
       </a>
      </p>
     </li>
     <li>
      <p>
       Validating
                                       the Insights migration.
      </p>
     </li>
     <li>
      Validating
                                    the Test Manager migration.
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/post-migration-steps#step-4%3A-validating-the-test-manager-migration">
       Details...
      </a>
     </li>
    </ol>
   </td>
  </tr>
 </tbody>
</table>