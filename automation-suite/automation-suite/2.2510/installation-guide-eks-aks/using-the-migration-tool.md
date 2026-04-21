---
title: "Performing a single tenant migration"
visible: true
slug: "using-the-migration-tool"
---

You can use the UiPath Automation Cloud™ Migration Tool to automatically migrate entities from your standalone Orchestrator to the Orchestrator service in Automation Suite.

This page provides details on the type of entities being migrated, the requirements for the migration from standalone Orchestrator to Automation Suite, the specific migration procedure, and any operations that may be necessary after the migration.

## Entities being migrated

When you run the Automation Cloud Migration Tool, it automatically creates the following entities in Automation Suite to match your standalone Orchestrator setup:

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
     Not Migrated
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Settings
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Yes, with exceptions (see on the right).
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     Some settings that are exposed to the tenant on the read path cannot be modified in Automation Suite, like host logo and color.
    </p>
    <p>
     Passwords in the Settings table cannot be exported because the API removes the values from the response. As a result no passwords
                                 will be migrated. This affects email alerts (SMTP password) and external feeds with basic authentication.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Packages
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Migrates all packages and all package versions.
    </p>
    <p>
     If a package feed is external and configured with basic authentication, the credentials will need to be input after the migration
                                 completes.
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     If a package feed is external and not accessible over the internet, entities that rely on these packages are not migrated.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Libraries
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Tenant-level feeds only.
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     If a library feed is at the host level or is external and not accessible over the internet, entities that rely on these libraries
                                 are not migrated.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Calendars
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Yes
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Machines
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Yes, but if there are not enough licenses to accommodate Machine slot assignments, the Machine will be imported with all slots
                                 set to 0.
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     Machine keys are not migrated.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Folders
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    Yes
                              Note: You can choose to migrate all folders in bulk, as well as individual folders.
   </td>
   <td headers="d16204e42">
    <p>
     Personal workspace folders are not migrated.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Environments
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Yes, for classic folders.
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     N/A for modern folders.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Robots (classic)
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Yes, but if there are not enough licenses to accommodate robot creation, the robot is skipped during import.
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     Skipped when licenses run out and an error is logged for each.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Robots (modern)
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Modern robots are migrated if the user with which they are associated exists in Automation Suite and has the same email address.
    </p>
   </td>
   <td headers="d16204e42">
    <ul>
     <li>
      If the user doesn&rsquo;t exist in Automation Suite, that specific robot migration fails.
     </li>
     <li>
      Skipped when licenses run out and an error is logged for each.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Environment associations
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     The robot-environment mapping is migrated.
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Processes
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Processes are migrated. The tool may refer to these as Releases.
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Queues
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Yes
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Triggers
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Triggers are migrated, but are all set as disabled.
    </p>
   </td>
   <td headers="d16204e42">
    &nbsp;
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Assets
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <ul>
     <li>
      Boolean, Text, and Integer asset types are fully supported.
     </li>
     <li>
      Credential assets are also migrated, but a dummy password is used because passwords cannot be migrated by the tool. You will
                                    need to manually update the passwords for each credential asset after migration. Credential assets are assigned to the default
                                    credential store in Automation Suite.
     </li>
     <li>
      Per-robot values are also migrated, but if the robot wasn&rsquo;t migrated, this value is skipped and an import warning is logged.
     </li>
    </ul>
   </td>
   <td headers="d16204e42">
    <p>
     Per-user asset values in modern folders are not supported. The asset is imported with the default value or skipped if none
                                 is set.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d16204e36">
    <p>
     <strong>
      Machine associations
     </strong>
    </p>
   </td>
   <td headers="d16204e39">
    <p>
     Robot-machine mappings are migrated.
    </p>
   </td>
   <td headers="d16204e42">
    <p>
     N/A
    </p>
   </td>
  </tr>
 </tbody>
</table>

### Entities not migrated

The following entities are **not** migrated by the tool:

* Folder feeds
* Users
* Queue items
* Action catalogs
* Webhooks
* Testing entities (test sets, test cases, test executions, test schedules, test data queues)
* Logs

## Prerequisites

Before opening the tool, make the following preparations:

1. Make sure you have sufficient robot licenses in Automation Suite to match the number of robots being migrated (**Admin** &gt; **Licenses** &gt; **Robots & Services**). The tool only migrates robots as long as there are licenses available, after which it starts to skip robots.
2. You must have administrator credentials for the standalone Orchestrator and **View** permissions for all entities being migrated. If you don't have the View permission for some entities, those entities are not migrated.
3. You must be an organization administrator in Automation Suite.
4. To run the tool, you need a machine that:
   1. can connect to the standalone Orchestrator and to Automation Suite (has internet access)
   2. has the Windows operating system
5. Download the tool on the mentioned machine from [this link](https://download.uipath.com/CloudMigration/UiPath.AutomationCloudMigrationTool.zip).
6. Register the tool as an external application in the target Automation Suite organization.

### Registering the tool as an external application

The migration tool needs to connect to the Orchestrator service API in Automation Suite to create the migrated entities. It uses the OAuth flow for this and therefore must be registered in Automation Suite as an external application.

1. Follow [these instructions](https://docs.uipath.com/automation-suite/automation-suite/2022.10/admin-guide/managing-external-applications) to add the tool as a new external application with the following specifics:
   * **Type**: Non-confidential
   * **Resources**: Orchestrator API
   * **User scopes**: OR.Folders, OR.Settings, OR.Robots, OR.Machines, OR.Execution, OR.Assets, OR.Users, OR.Jobs, and OR.Queues.
   * **Redirect URL**: `http://127.0.0.1:8888/auth/`
2. Save the **Application ID** for later use.

## Running the tool

The tool can migrate one tenant at a time. You can run the tool multiple times for each of your tenants.

With each run, the tool:

1. Connects to your standalone Orchestrator to export entities for the given tenant.
2. Connects to Automation Suite to import and create the migrated entities in the Orchestrator tenant.

For more information about entities that are subject to migration, see [Entities Being Migrated](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/using-the-migration-tool#entities-being-migrated).

To run the tool:

1. Extract the ZIP file you downloaded for the tool and then run the tool EXE.
2. For the activation method, choose **Connect to On-Premises**:
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/205743)
3. Fill in the information to allow the tool to connect to your standalone Orchestrator:
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/206399)

Make sure that the credentials you provide are for an administrator account that also has **View** permissions on all the entities you want to migrate.
4. Select **Start Export** to connect to your standalone Orchestrator and download the setup information.The export begins and may take a while to complete:
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/206727)

When finished, the export summary lists all entities that were successfully exported:
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/205823)

You can select **Open File** to view the local file created for the export summary, which includes a few more details.
5. Select **Home** to return to the first screen.
6. For the activation method, this time choose **Connect to Automation Suite**.
7. Fill in the information to allow the tool to connect to Automation Suite to upload the setup information:
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/206407)

Expand Table

   | Field | Details |
   | --- | --- |
   | **Automation Suite URL** | The **URL** where Automation Suite is hosted, including the protocol and ending with a slash (`/`).  You can pick up this URL from your browser address bar while in Automation Suite, but do not include the part of the URL beginning with the organization name. For example, if the URL in your browser is `https://mySite.com/docs/Migration/orchestrator_/?tid=34&fid=82`, with `docs` being the organization name, you must specify only `https://mySite.com/` in this field. |
   | **Client Application Id** | The **Application ID** value associated with the external application registration in Automation Suite.  You can find this value on the **Admin** &gt; **External Applications** page. |
   | **Organization Name** | The organization-specific part of your Automation Suite URL. Organization administrators can find this information in the **Organization Name** field under **Admin** &gt; **Organization Settings**.  You do not need to include the full URL, only the editable part, which is specific to your organization. For example, if the URL is `https://mySite.com/``myOrgName`, add `myOrgName` to the field. |
   | **Tenant Name** | The exact name of the Automation Suite tenant where you want to add the migrated information. The migrated data will be visible in the specified Orchestrator tenant. |
8. Select **Start Import** to connect to Automation Suite and start to migrate the information to the target Orchestrator tenant.

The import begins and may take a while to complete:
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/206795)

To connect to Automation Suite using OAuth, a user with the adequate permissions for the scopes added when you [registered the external application](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/using-the-migration-tool#performing-a-single-tenant-migration) must log in to Automation Suite. When they do, a new window opens with a success message if the OAuth flow was successful:
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/206683)

When finished, the import summary lists all entities that were successfully imported into the Orchestrator tenant in Automation Suite:
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/206867)

Anything that was not imported is listed as an error and partial imports are listed as warnings. You can select **View Report** for more details about exactly which entities encountered an error or warning.
9. When ready, select **Done** to close the tool.
   :::tip
   If needed, you can run the tool again to migrate data for additional tenants.
   :::

## Post-migration tasks

Because the tool cannot migrate everything, there are some final tasks that you must perform manually to obtain the same setup as you had in your standalone Orchestrator.

1. In Automation Suite, log in to the organization of the tenant that was the import target and then open Orchestrator.
2. Check that folders and entities were successfully migrated.

You can use the import summary to check the specific items that had warnings or errors.
3. Allocate robot and service licenses for Orchestrator.

During import, machines are created and licensed while available licenses exist. After licenses run out, machines continue to be created without licenses, so you must update any such machines to allocate the adequate number of licenses.

   :::note
   If you migrated without activating your Automation Suite license, at this stage you need to activate it to continue with the setup.
   :::
4. Manually upload any library feeds that the tool did not migrate.
5. If any robots were skipped during export or import, manually create them.
6. Create any webhooks, task catalogs, credential stores, or other information that the tool does not migrate.

The section [Entities being migrated](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/using-the-migration-tool#entities-being-migrated) includes a list of what the tool does not migrate.
7. Manually connect robots to the Automation Suite Orchestrator service.
8. Manually enable triggers as needed.

While the tool migrates triggers, they are all disabled and you must manually enable them.
9. Check any locations in Orchestrator where a password is required and add it: Robots, Settings, and Credential Assets.

## Getting help

If you need assistance with an issue encountered during export, import, or after import, open a [Support ticket](https://www.uipath.com/company/contact-us/contact-technical-support) and include the following files:

* Log file (in the **logs** sub-folder)
* Export report file (in the **MigrationAssets** sub-folder)
* Import report file (in the **MigrationAssets** sub-folder)

In addition to these files, it would be helpful to know:

* The version of your standalone Orchestrator
* Your Automation Suite organization and tenant names.