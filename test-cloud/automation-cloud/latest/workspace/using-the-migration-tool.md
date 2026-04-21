---
title: "Using the Automation Cloud Migration Tool"
visible: true
slug: "using-the-migration-tool"
---

The Automation Cloud Migration Tool is a desktop application designed to simplify the process of migration from one deployment option to another. The tool automates various migration steps, making it easier to transition either your standalone or Automation Suite Orchestrator to Test Cloud, Test Cloud Dedicated, Test Cloud Public Sector, or Test Cloud for on-premises.

Instructions on this page apply for migrating your on-premises Orchestrator, either standalone or via Automation Suite, to a cloud offering.
:::note
Feature availability depends on the cloud offering you use. For details, refer to the [feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

## Before you begin

When planning your migration from on-premises Orchestrator to a cloud offering, it is advisable that you take the following steps:

1. [Upgrade](https://docs.uipath.com/overview/other/latest/overview/product-lifecycle#operate) to a supported on-premises Orchestrator version.
2. [Migrate from classic to modern folders](https://docs.uipath.com/orchestrator/standalone/2023.4/user-guide/migrating-from-classic-folders-to-modern-folders), as [classic folders](https://docs.uipath.com/overview/other/latest/overview/classic-folders-removal) have restrictions in cloud offerings, meaning that they do not exist in UiPath cloud offerings.
3. Run the migration tool to migrate from on-premises Orchestrator to the desired cloud offering.
:::note
* While other sequences are technically possible, this is the most common approach.
* The Automation Cloud Migration Tool operates independently and does not conform to our standard [Product Lifecycle](https://docs.uipath.com/overview/other/latest/overview/product-lifecycle).
:::

## Requirements

To use the migration tool, you must meet the following criteria:

* Your standalone Orchestrator version must be supported. For specific version details, refer to our [Product Lifecycle](https://docs.uipath.com/overview/other/latest/overview/product-lifecycle) documentation.
* You need an active license for a cloud offering. For more information, refer to our [Licensing](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-licensing#about-licensing) documentation.
* For Flex licensing, you need a Pro, Pro Trial, or Enterprise license in Automation Cloud. While you can use the tool during a Pro Trial for evaluation, some limitations may apply, such as tenant and robot license restrictions. For more information, refer to our [Licensing](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-licensing) documentation.

## Prerequisites

Before opening the Automation Cloud Migration Tool, make the following preparations:

1. Depending on your cloud offering, check that the Enterprise or Enterprise Trial licensing plan is active (**Admin** > **Licenses**).
2. Make sure you have sufficient [robot licenses](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-licensing) to match the number of robots being migrated (**Admin** > **Licenses** > **Robots & Services**). The tool migrates robots as long as there are licenses available, after which it starts to skip robots.
3. Make sure you have administrator credentials for the environment you migrate from.
4. Make sure you have **View** permission for all entities being migrated. If you do not have the **View** permission for some entities, those entities will not be migrated.
5. Make sure you are an [organization administrator](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-accounts) in Automation Cloud to register the tool as an external application.
6. Make sure the machine you run the Automation Cloud Migration Tool on meets the following requirements:
   1. Can connect to standalone Orchestrator, Orchestrator in a cloud offering, or Orchestrator in Automation Suite.
   2. Can access the cloud offering (has internet access and a [supported browser](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/software-requirements#browser-compatibility));
   3. Runs the Windows operating system.
7. [Download the migration tool](https://download.uipath.com/CloudMigration/UiPath.AutomationCloudMigrationTool.zip) on the machine that meets the requirements in the previous step.

## Entities migrated by the migration tool

When using the migration tool, the following entities, as described in the table, are automatically created in the cloud offering to mirror your Orchestrator setup:

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
     Entity
    </p>
   </th>
   <th>
    <p>
     Migrated
    </p>
   </th>
   <th>
    <p>
     Not migrated
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d11267e200">
    <p>
     Settings
    </p>
   </td>
   <td headers="d11267e203">
    <p>
     Yes, with exceptions
    </p>
   </td>
   <td headers="d11267e206">
    Some on-premises settings, such as passwords and certain settings exposed to tenants
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Packages
    </p>
   </td>
   <td headers="d11267e203">
    All packages and package versions
   </td>
   <td headers="d11267e206">
    <p>
     Entities that rely on external package feeds requiring authentication
    </p>
    Note:
    <p>
     Authentication is required after migration is completed for external package feeds configured with basic authentication
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Libraries
    </p>
   </td>
   <td headers="d11267e203">
    Tenant-level feeds only
   </td>
   <td headers="d11267e206">
    Entities that rely on libraries with host-level configurations or inaccessible external libraries
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Calendars
    </p>
   </td>
   <td headers="d11267e203">
    <p>
     Yes
    </p>
   </td>
   <td headers="d11267e206">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Machines
    </p>
   </td>
   <td headers="d11267e203">
    <p>
     Yes
    </p>
    Note:
    <p>
     Potential machine slot assignments limitations due to missing licenses
    </p>
   </td>
   <td headers="d11267e206">
    <p>
     Machine keys
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Folders
    </p>
   </td>
   <td headers="d11267e203">
    Yes
                                 Note: You can choose to migrate all folders in bulk, as well as individual folders.
   </td>
   <td headers="d11267e206">
    Personal workspace folders
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Environments
    </p>
   </td>
   <td headers="d11267e203">
    Yes, for classic folders.
   </td>
   <td headers="d11267e206">
    <p>
     N/A
    </p>
    <p>
     (for modern folders)
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Robots (classic)
    </p>
   </td>
   <td headers="d11267e203">
    <p>
     Yes
    </p>
    Note:
    <p>
     Potential robot creation limitations due to missing licenses.
    </p>
   </td>
   <td headers="d11267e206">
    Skipped when licenses run out, with an error logged for each skipped robot
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Robots (modern)
    </p>
   </td>
   <td headers="d11267e203">
    <p>
     Yes
    </p>
    Note:
    <p>
     If certain conditions are met, robots are associated with an on-premises user that has an email
                                       address, and that same email was already invited to a UiPath
                                       cloud offering and is associated to a user.
    </p>
   </td>
   <td headers="d11267e206">
    <p>
     Skipped when licenses run out, with an error logged for each skipped robot.
    </p>
    <p>
     Fails if a user in a UiPath cloud offering does not exist.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Environment associations
    </p>
   </td>
   <td headers="d11267e203">
    The robot-environment mapping
   </td>
   <td headers="d11267e206">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Processes
    </p>
   </td>
   <td headers="d11267e203">
    <p>
     Yes
    </p>
    Note:
    <p>
     The migration tool may refer to processes as releases
    </p>
   </td>
   <td headers="d11267e206">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Queues
    </p>
   </td>
   <td headers="d11267e203">
    <p>
     Yes
    </p>
   </td>
   <td headers="d11267e206">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Triggers
    </p>
   </td>
   <td headers="d11267e203">
    <p>
     Yes, but they are set as disabled
    </p>
   </td>
   <td headers="d11267e206">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Assets
    </p>
   </td>
   <td headers="d11267e203">
    Certain asset types are fully supported, with some considerations for credential assets
   </td>
   <td headers="d11267e206">
    Per-user asset values in modern folders
   </td>
  </tr>
  <tr>
   <td headers="d11267e200">
    <p>
     Folder feeds
    </p>
   </td>
   <td headers="d11267e203">
    <p>
     Yes
    </p>
   </td>
   <td headers="d11267e206">
    <p>
     N/A
    </p>
   </td>
  </tr>
 </tbody>
</table>

## Entities not migrated by the migration tool

The migration tool does not migrate the following entities:

* User and robot accounts
* Role assignments
* Queue items
* Action catalogs
* Webhooks
* Testing entities (test sets, test cases, test executions, test schedules, test data queues)
* Storage buckets
* Logs
* Tasks

## Registering the migration tool as an external application

The migration tool must connect to the Orchestrator service API in the cloud offering, to create the migrated entities. It uses the OAuth flow for this and, therefore, must be registered as an external application.

To register the Automation Cloud Migration Tool as an external application, take the following steps:

1. Add the tool as a new external application by following the instructions in [Adding an external application](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-external-applications#adding-an-external-application). Make sure to use the following configuration:
   * **Type**: Non-confidential
   * **Resources**: Orchestrator API
   * **User scopes**: `OR.Folders`, `OR.Settings`, `OR.Robots`, `OR.Machines`, `OR.Execution`, `OR.Assets`, `OR.Users`, `OR.Jobs`, and `OR.Queues`.
   * **Redirect URL**: `http://127.0.0.1:8888/auth/`
2. Save the **Application ID** for later use.

## Running the migration tool

The migration tool can migrate one tenant at a time. You can run the tool for each of your tenants. With each run, the tool performs the following operations:

* Connects to your on-premises Orchestrator to export entities for the given tenant.
* Connects to the cloud offering to import and create the migrated entities in Orchestrator.

For more information about entities that are subject to migration, refer to [Entities migrated by the migration tool](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/using-the-migration-tool#entities-migrated-by-the-migration-tool).

1. Extract the `.zip` file you downloaded for the tool, and then run the `.exe` tool.
2. To choose your export environment, take one of the following steps:
   * Select **On-premises MSI**, if you migrate from standalone Orchestrator.
   * Select **Automation Suite** to connect to the external application and fill in the export input form, if you migrate from Automation Suite Orchestrator.

     ![docs image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/549380)
3. Fill in the information to allow the tool to connect to your on-premises Orchestrator.
   !['Connect to on-premises Orchestrator' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/404831)

   !['Connect to Automation Suite' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/404835)

   :::note
   Ensure that the credentials you provide are for an administrator account that also has **View** permissions on all the entities you want to migrate.
   :::
4. Select **Start Export** to connect to your source environment and download the setup information. The export begins and may take a while to complete.
   !['Exporting data from on-premises Orchestrator' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/383648)

When finished, the export summary lists all entities that were successfully exported. You can select **Open File** to view the local file created for the export summary, which includes a few more details.

   !['Successfully exported on-premises Orchestrator data' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/383652)
5. Select **Home** to return to the first screen of the migration tool.
6. For the activation method, this time choose **Connect to Automation Cloud**.
7. Fill in the information to allow the tool to connect to the cloud offering to upload the setup information. The following table describes the necessary fields to connect to the cloud offering.
   !['Connect to Automation Cloud' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/404840)

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Field
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
   <td headers="d11267e642">
    <p>
     <strong>
      Client Application Id
     </strong>
    </p>
   </td>
   <td headers="d11267e648">
    <p>
     The
     <strong>
      Application ID
     </strong>
     value associated with the
                                          external application registration in the cloud
                                          offering.
    </p>
    <p>
     You can find this value on the
     <strong>
      Admin
     </strong>
     &gt;
     <strong>
      External Applications
     </strong>
     page.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d11267e642">
    <p>
     <strong>
      Organization Name
     </strong>
    </p>
   </td>
   <td headers="d11267e648">
    <p>
     The organization-specific part of your cloud offering
                                          URL. Organization administrators can find this
                                          information in the
     <strong>
      URL
     </strong>
     field in
     <strong>
      Admin
     </strong>
     &gt;
     <strong>
      Organization Settings
     </strong>
     .
    </p>
    Note: You do
                                          not need to include the full URL, but only the editable
                                          part, which is specific to your organization. For
                                          example, if the URL is
    <code>
     https://cloud.uipath.com/
    </code>
    <code>
     myOrgName
    </code>
    ,
                                          add
    <code>
     myOrgName
    </code>
    to the field.
   </td>
  </tr>
  <tr>
   <td headers="d11267e642">
    <p>
     <strong>
      Tenant Name
     </strong>
    </p>
   </td>
   <td headers="d11267e648">
    <p>
     The exact name of the cloud offering tenant where you
                                          want to add the migrated information. The migrated data
                                          will be visible in the Orchestrator service associated
                                          to that tenant.
    </p>
   </td>
  </tr>
 </tbody>
</table>
8. Select **Start Import** to connect to the cloud offering and start to migrate the information to the target Orchestrator service.

The import begins and may take a while to complete.

To connect to the cloud offering using OAuth, a user with the adequate permissions for the scopes added when you registered the external application must log in to the cloud offerinh. When they do, a new window opens with a success message, if the OAuth flow was successful.

   !['Success message' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/391023)

When finished, the import summary lists all entities that were successfully imported into the Orchestrator service in the cloud offering.

   !['Import summary message' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/383695)

Anything that was not imported is listed as an error and partial imports are listed as warnings. You can select **View Report** for more details about exactly which entities encountered an error or warning.
9. When ready, select **Done** to close the tool.
:::tip
If needed, you can run the tool again to migrate data for additional tenants.
:::

## Post-migration tasks

Because the Automation Cloud Migration Tool cannot migrate all data, there are some final tasks that you must perform manually.

1. In the cloud offering, select the tenant that was the import target, and open Orchestrator. Check that folders and entities were successfully migrated. You can use the import summary to check the specific items that had warnings or errors.
2. [Allocate robot and service licenses](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/allocating-licenses-to-tenants#assigning-licenses-to-tenants) for Orchestrator. Machines are created and licensed while available licenses exist, but after licenses run out, machines continue to be created without licenses, so you must update them to allocate the adequate number of licenses.
3. Manually upload any library feeds that the tool did not migrate.
4. If any robots were skipped during export or import, manually create them.
5. Create any webhooks, task catalogs, credential stores, or other information that the tool does not migrate. The section [Entities migrated by the migration tool](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/using-the-migration-tool#entities-migrated-by-the-migration-tool) also includes a list of what the tool does not migrate.
6. Manually [connect robots](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/connecting-robots-to-orchestrator#section-connecting-the-robot-to-orchestrator) to the cloud Orchestrator service.
7. Manually enable triggers as needed.
8. Check any locations in Orchestrator where a password is required and add it: robots, settings, and credential assets.

## Getting help

If you need assistance with an issue encountered during export, import, or after import, open a [support ticket](https://www.uipath.com/company/contact-us/cloud-platform-technical-support) and include the following files:

* Log file (in the **logs** sub-folder)
* Export report file (in the **MigrationAssets** sub-folder)
* Import report file (in the **MigrationAssets** sub-folder)

In addition to the previous files, it would be helpful to know the following:

* The version of your on-premises Orchestrator;
* Your cloud offering organization and tenant names.