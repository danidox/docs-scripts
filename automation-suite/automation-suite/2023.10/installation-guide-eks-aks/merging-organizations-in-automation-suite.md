---
title: "Step 4: Merging organizations in Automation Suite"
visible: true
slug: "merging-organizations-in-automation-suite"
---

## Migration tool input

When running the UiPath.OrganizationMigrationApp tool, you must provide the following details:

* The list of organization IDs for the standalone product
* The list of organization IDs for Automation Suite

For more details, see [Migration tool parameters](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/moving-the-identity-organization-data-from-standalone-to-automation-suite#migration-tool-parameters).

:::note
Make sure to use the same organization IDs as the ones identified in [Step 1: Moving the Identity organization data from standalone to Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/moving-the-identity-organization-data-from-standalone-to-automation-suite#step-1%3A-moving-the-identity-organization-data-from-standalone-to-automation-suite).
:::

## For Linux

:::note
Make sure to follow the general escape instructions for the Shell tool of your choice. For instance, in Bash you must add `\` before special characters.
:::

To merge organizations in Automation Suite, run the following command:

```
./UiPath.OrganizationMigrationApp merge -i '<identity database connection of Automation Suite>' -o '<restored orchestrator DB in Automation Suite connection string>' -s '<list of tenant IDs of the standalone product separated by comma, e.g. tenantID1,tenantID2>' -d '<list of organization IDs of Automation Suite separated by comma, e.g. orgID1,orgID2>'
```

:::note
* Make sure to add `TrustServerCertificate=True` for both the source and destination SQL connections in the input.
* If you have multiple organization pairs to merge, make sure the organization ID sequence for the standalone product and the
organization ID sequence for Automation Suite match.
* If you migrate one standalone tenant to one Automation Suite organization for all tenants, you can run the command once for
all migrations. However, if you migrate multiple standalone tenants to one Automation Suite organization, you must run the command separately for each tenant, as you may need to resolve user conflicts between the tenants. The following sample shows how to run the command separately for each tenant: assignment
```
./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant1' -d 'orgId1'
./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant2' -d 'orgId1'
./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant3' -d 'orgId1'
```
For instructions on how to address user conflicts when migrating multiple standalone tenants to a single Automation Suite organization, see [Solving user conflicts](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/merging-organizations-in-automation-suite#solving-user-conflicts).
:::

## For Windows

To merge organizations in Automation Suite, run the following command:

```
./UiPath.OrganizationMigrationApp merge -i "<identity database connection of Automation Suite>" -o "<restored orchestrator DB in Automation Suite connection string>" -s "<list of tenant IDs of the standalone product separated by comma, e.g. tenantID1,tenantID2>" -d "<list of organization IDs of Automation Suite separated by comma, e.g. orgID1,orgID2>"
```

:::note
* Make sure to add `TrustServerCertificate=True` for both source and destination SQL connection strings in the input.
* If you migrate one standalone tenant to one Automation Suite organization for all tenants, you can run the command once for
all migrations. However, if you migrate multiple standalone tenants to one Automation Suite organization, you must run the command separately for each tenant, as you may need to resolve user conflicts between the tenants. The following sample shows how to run the command separately for each tenant: assignment
```
./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant1' -d 'orgId1'
./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant2' -d 'orgId1'
./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant3' -d 'orgId1'
```
:::

For instructions on how to address user conflicts when migrating multiple standalone product tenants to a single Automation Suite organization, see [Solving user conflicts](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/merging-organizations-in-automation-suite#solving-user-conflicts).

## Merge expectations

### Users

:::note
Only users that are originally from standalone Orchestrator have access to Orchestrator after migrating to Automation Suite.
:::

The following table provides insight into multiple migration scenarios and how they impact users:

Expand Table

| Condition | Does the source user have an email address? | Does the target user have an email address? | Is the source user email the same as the one of the target user? | Is the source username the same as the target username? | **Result** |
| --- | --- | --- | --- | --- | --- |
| 1 | ✅ | ✅ | ❌ | ❌ | The source user is moved to the target organization; the target organization user has access to standalone Orchestrator. |
| 2 | ✅ | ✅ | ❌ | ✅ | The source user is moved to the target organization; the target organization user has access to standalone Orchestrator.  After the merge, two users have the same username, and they must use the email address to login. |
| 3 | ✅ | ✅ | ✅ | ✅ or ❌ | The source user is merged with the target user; the target user has access to standalone Orchestrator. |
| 4 | ❌ | ❌ | N/A | ❌ | The source user is moved to the target organization; the target organization user has access to standalone Orchestrator. |
| 5 | ❌ | ❌ | N/A | ✅ | The source user is merged with the target user; the target user has access to standalone Orchestrator. |
| 6 | ✅ | ❌ | N/A | ❌ | The source user is moved to the target organization; the target organization user has access to standalone Orchestrator. |
| 7 | ✅ | ❌ | N/A | ✅ | You must manually configure the email address for the target user or remove the target user.  If you configure the email address, the source user is merged with the target user, and the target user has access to standalone Orchestrator.  If you remove the target user, the source user is moved to the target organization, and the target organization user has access to standalone Orchestrator. |
| 8 | ❌ | ✅ | N/A | ❌ | The source user is moved to the target organization, and the target organization user has access to standalone Orchestrator. |
| 9 | ❌ | ✅ | N/A | ✅ | You must configure the email address to be empty for the target user or remove the target user.  If you configure the email address as empty, the source user is merged with the target user, and the target user has access to standalone Orchestrator.  If you remove the target user, the source user is moved to the target organization, and the target organization user has access to standalone Orchestrator. |

### Robot users

If the source and target robot usernames are the same, the source robot user is appended the user ID and is move to the target organization.

Expand Table

| Source robot username | Target robot username | Moved source robot username |
| --- | --- | --- |
| sameRobot | sameRobot | `sameRobot_47a26d4a-2180-4fdd-8e1e-2379300a1162` |

### Groups

If the source and target robot group names are the same, the source robot user is appended a string and is moved to the target organization.

Expand Table

| Source group name | Target group name | Moved source group username |
| --- | --- | --- |
| sameGroup | sameGroup | `sameGroup_db39a5c6-f73c-4011-b40e-4ea620fe3d01` |

### Settings

If source settings and target settings have the same name, the setting value of the target is used.

## Enabling Insights after merging organizations

If you migrate Insights, log in to each organization after completing the merge and enable Insights for each tenant that previously had Insights enabled in the standalone (MSI) environment.

This step is required because the Insights database that Automation Suite uses after migration already has Insights enabled. If you skip this step, Automation Suite may enter a state where Insights appears to be enabled for a tenant, but the platform does not have the corresponding Insights instance registered.

:::note
Enable Insights in each tenant before updating the connection string. Doing so ensures that Insights is correctly linked to the migrated database and prevents configuration inconsistencies.
:::

## Solving user conflicts

Migrating multiple standalone tenants to a single Automation Suite organization may lead to user conflicts. The following sample shows an error message for such a conflict:

```
[03:18:08 WRN] We found users in the target organization have the same email as those from the source organization. If you continue, we will keep the users in the target organization, but none of the application data for the source organization users will be moved.
The format is orgId -> list of emails.
[03:18:08 WRN] 3d8d01e6-3300-4988-87db-071bd8c8e786 -> user22@test.com,user2@test.com,user4@test.com,user3@test.com
[03:18:08 WRN] We found users without emails in the target organization have the same username with the users without emails from the source organization.If you continue, we will keep the users in the target organization, but none of the application data for the source organization users will be moved.
The format is orgId -> list of usernames.
[03:18:08 WRN] 3d8d01e6-3300-4988-87db-071bd8c8e786 -> user1
[03:18:08 INF] Do you want to continue? Type (y/n)
```

You can solve user conflicts in two ways:

* Type `n` to end the merging process, then delete the users with conflicts in the Automation Suite organization and run the merging command again. By choosing this option, you lose the deleted user information.
* Type `y` to continue the merging process. By choosing this option, you replace all source user IDs with target user IDs. If a product running in Automation Suite, such as Insights, has a reference to a user ID, you lose the data for any merged user from the standalone environment. For instance, let us assume two users:
  + one user with the username `user1` and email address `user1@test.com`, from `tenant1` in a standalone environment.
  + another use with the same username and email address, from `tenant2` in a standalone environment.

If you first merge `tenant1` to an organization in Automation Suite, no conflict occurs. However, if you then merge `tenant2` to the same Automation Suite organization, a conflict occurs, as two users have the same email address, `user1@test.com`. If you type `y` to continue the merging process, you lose the user data to which the product has a reference for the user from `tenant2`.

## If organization merge failed

If the organization merge failed, check the logs. Depending on whether the Identity or the Orchestrator migration failed, take the following steps:

### Failed Identity migration

If the Identity migration failed, you can just fix the error and execute the organization merge command again. This would rollback all the changes since we have set a transaction for operations for Identity.

### Failed Orchestrator migration

If the Orchestrator migration failed, the Orchestrator database would roll back, but the Identity database would not rollback. As a result, you must restore the backup of the Identity database and replace the connection string to use the new database. After fixing the error, run organization merge command again.

If the Orchestrator migration failed, take the following steps:

1. Restore the backup of the Identity database.
   1. Right-click the database directory and select **Import Data-tier Application**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/265222)
   2. Select the backup database file.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/265227)
   3. Input the backup database name.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/265231)
   4. Wait for the process to complete.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/265236)
2. Replace the identity connection string.
   ```
   `"platform": {
       "sql_connection_str": "<dotnet connection string>",   (added line)
       "enabled": true, 
   },`
   ```
3. Fix the error and use the new platform connection string to run the merge command again.