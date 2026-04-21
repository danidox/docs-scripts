---
title: "Step 1: Moving the Identity organization data from standalone to Automation Suite"
visible: true
slug: "moving-the-identity-organization-data-from-standalone-to-automation-suite"
---

The standalone and Automation Suite versions must be the same, or else the migration will fail due to database schema conflict issues. If you experience a compatibility failure, make sure to upgrade your standalone and Automation Suite installations to the latest version.

## Running the migration tool on Linux

Before you begin, take the following into consideration:

* Make sure you download and install .NET Runtime 6.0 before running UiPath.OrganizationMigrationApp. For details, see [Migration prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-prerequisites#net-runtime-60).
* To download UiPath.OrganizationMigrationApp, see [Migration prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-prerequisites#uipathorganizationmigrationapp).
  :::note
  Make sure to follow the general escape instructions for your Shell tool of choice. For instance, in Bash you must add `\` before special characters.
  :::

This section describes some common operations that you may need to perform using the Uipath.Organization.Migration.App tool. For details on the parameters that the Uipath.Organization.Migration.App tool supports, see [Migration tool parameters](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/moving-the-identity-organization-data-from-standalone-to-automation-suite#migration-tool-parameters).

* To move the Identity data of all tenants from standalone to Automation Suite, extract the file and run the following command:
  ```
  ./UiPath.OrganizationMigrationApp migrate -m -i '<identity database connection of the standalone product>' -j '<identity database connection of Automation Suite>' -o '<orchestrator database connection of the standalone product>' -s '<list of tenant IDs of the standalone product>' -d '<list of organization IDs of Automation Suite>' -p '<URL of Automation Suite>' -c '<OMS S2S client secret>'
  ```

  :::note
  * Make sure to add `TrustServerCertificate=True` for all SQL connections in the input.
  * The Automation Suite tenant name is the same as the original tenant name in standalone Orchestrator. This is the tenant to
  which you will migrate the standalone products.
  * If you migrate one standalone tenant to one Automation Suite organization for all tenants, you can run the command once for
  all migrations. However, if you migrate multiple standalone tenants to one Automation Suite organization, you must run the command separately for each tenant, as you may need to resolve user conflicts between the tenants. The following sample shows how to run the command separately for each tenant: assignment
  ```
  ./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant1' -d 'orgId1'
  ./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant2' -d 'orgId1'
  ./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant3' -d 'orgId1'
  ```
  For instructions on how to address user conflicts when migrating multiple standalone tenants to a single Automation Suite organization, see [Solving user conflicts](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/merging-organizations-in-automation-suite#solving-user-conflicts).
  :::
* If the operation failed in the middle, roll back the change by running the following command:
  ```
  ./UiPath.OrganizationMigrationApp migrate -m -r -i '<identity database connection of the standalone product>' -j '<identity database connection of Automation Suite>' -o '<orchestrator database connection of the standalone product>' -s '<list of tenant IDs of the standalone product>' -d '<list of organization IDs of Automation Suite>' -p '<URL of Automation Suite>' -c '<OMS S2S client secret>'
  ```
* Fix the issue according to the error message and try to move the Identity data of all tenants from standalone to Automation Suite again. For example, see the following error messages and what they mean:
  + The following error message means that the tenant is already created and the program would skip tenant creation. You do not need to do anything.
    ```
        Call to API Service failed for Method=POST, StatusCode=Conflict on url=https://ci-asaks5379291.devtest-ascloudgen-ea.infra.uipath-dev.com/organization/api/organization/0dad76a9-7d44-447a-84d6-ce713a5324d8/tenants
        Http Response Content:{"StatusCode":409,"StatusDescription":"Conflict","ErrorCode":1002,"Message":"Found duplicated tenant with requested Id b26f486f-a585-4420-83fd-f2741385b3c8 under organization 0dad76a9-7d44-447a-84d6-ce713a5324d8 (1002)"}
    ```
  + The following error message means that the Automation Suite URL is not valid. Make sure to provide the correct Automation Suite URL.
    ```
        Unhandled exception. UiPath.IdentityServer.PartitionMerge.PartitionMergeException: Can not create tenant ID with target organiztion ID 0dad76a9-7d44-447a-84d6-ce713a5324d8, tenant name tenant_0dad76a9, platform url https://ci-asaks5379291.devtest-ascloud.infra.uipath-dev.com.
         ---> System.Net.Http.HttpRequestException: No such host is known. (ci-asaks5379291.devtest-ascloud.infra.uipath-dev.com:443)
         ---> System.Net.Sockets.SocketException (11001): No such host is known.
    ```
  + The following error message means that the OMS S2S client secret is not valid. Make sure to provide the correct OMS S2S client secret.
    ```
        Call to API Service failed for Method=POST, StatusCode=BadRequest on url=https://ci-asaks5379291.devtest-ascloudgen-ea.infra.uipath-dev.com/identity_/connect/token
        Http Response Content:{"error":"invalid_client"}
    ```
  + The following error message means that there is already a tenant in the Automation Suite organization with the same tenant name as the standalone tenant name. To resolve the conflict, you must change the tenant name for the tenant in the Automation Suite organization.
    ```
    Source tenant ID: 38f03b05-3aab-422c-844b-bf3668fa54ee, target organization ID: f7d80050-9654-4f44-8a34-3a9e46380dc9, confilict tenant name: test_tenan1
    Source tenant ID: b35020b1-ee9f-4026-abd1-bb721b148e24, target organization ID: f7d80050-9654-4f44-8a34-3a9e46380dc9, confilict tenant name: test_tenant2
    Tenant name conflicts detected. You need to rename the tenant to be a different name than conflict tenant name in target organization to unblock tenant creation.
    ```

## Running the migration tool on Windows

Before you begin, take the following aspects into consideration:

* You must download and install .NET Runtime 6.0 before running UiPath.OrganizationMigrationApp. For details, see [Migration prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-prerequisites#net-runtime-60).
* To download UiPath.OrganizationMigrationApp, see [Migration prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-prerequisites#uipathorganizationmigrationapp).
  :::note
  To successfully run the UiPath.OrganizationMigrationApp tool, you must escape your SQL password if it contains special characters. For example, replace every instance of `$` with `` \`$ ``. For more guidelines on how to escape special characters in connection string passwords, refer to [Special character escape rules for connection string passwords](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-prerequisites#special-character-escape-rules-for-connection-string-passwords).
  :::

This section describes some common operations that you may need to perform using the Uipath.Organization.Migration.App tool. For details on the parameters that the Uipath.Organization.Migration.App tool supports, see [Migration tool parameters](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/moving-the-identity-organization-data-from-standalone-to-automation-suite#migration-tool-parameters).

* To move the Identity data of all tenants from standalone to Automation Suite, extract the file and run the following command.
  :::note
  * Make sure to add `TrustServerCertificate=True` for both source and destination SQL connection inputs.
  * The Automation Suite tenant name is the same as the original tenant name in standalone Orchestrator. This is the tenant to
  which you will migrate the standalone products.
  * If you migrate one standalone tenant to one Automation Suite organization for all tenants, you can run the command once for
  all migrations. However, if you migrate multiple standalone tenants to one Automation Suite organization, you must run the command separately for each tenant, as you may need to resolve user conflicts between the tenants. The following sample shows how to run the command separately for each tenant: assignment
  ```
  ./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant1' -d 'orgId1'
  ./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant2' -d 'orgId1'
  ./UiPath.OrganizationMigrationApp merge -i '&lt;identity database connection of Automation Suite&gt;' -o '&lt;restored orchestrator DB in Automation Suite connection string&gt;' -s 'tenant3' -d 'orgId1'
  ```
  For instructions on how to address user conflicts when migrating multiple standalone tenants to a single Automation Suite organization, see [Solving user conflicts](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/merging-organizations-in-automation-suite#solving-user-conflicts).
  :::
  ```
  ./UiPath.OrganizationMigrationApp migrate -m -i "<identity database connection of the standalone product>" -j "<identity database connection of Automation Suite>" -o "<orchestrator database connection of the standalone product>" -s "<list of tenant IDs of the standalone product>" -d "<list of organization IDs of Automation Suite>" -p "<URL of Automation Suite>" -c "<OMS S2S client secret>"
  ```
* If the operation failed in the middle, roll back the change by running the following command:
  ```
  ./UiPath.OrganizationMigrationApp migrate -m -r -i "<identity database connection of the standalone product>" -j "<identity database connection of Automation Suite>" -o "<orchestrator database connection of the standalone product>" -s "<list of tenant IDs of the standalone product>" -d "<list of organization IDs of Automation Suite>" -p "<URL of Automation Suite>" -c "<OMS S2S client secret>"
  ```
* Fix the issue based on the error message and try to move the Identity data of all tenants from standalone to Automation Suite again. For example, see the following error messages and what they mean:
  + The following error message means that the tenant is already created and the program would skip tenant creation. You do not need to do anything.
    ```
        Call to API Service failed for Method=POST, StatusCode=Conflict on url=https://ci-asaks5379291.devtest-ascloudgen-ea.infra.uipath-dev.com/organization/api/organization/0dad76a9-7d44-447a-84d6-ce713a5324d8/tenants
        Http Response Content:{"StatusCode":409,"StatusDescription":"Conflict","ErrorCode":1002,"Message":"Found duplicated tenant with requested Id b26f486f-a585-4420-83fd-f2741385b3c8 under organization 0dad76a9-7d44-447a-84d6-ce713a5324d8 (1002)"}
    ```
  + The following error message means that the Automation Suite URL is not valid. Make sure to provide the correct Automation Suite URL.
    ```
        Unhandled exception. UiPath.IdentityServer.PartitionMerge.PartitionMergeException: Can not create tenant ID with target organiztion ID 0dad76a9-7d44-447a-84d6-ce713a5324d8, tenant name tenant_0dad76a9, platform url https://ci-asaks5379291.devtest-ascloud.infra.uipath-dev.com.
         ---> System.Net.Http.HttpRequestException: No such host is known. (ci-asaks5379291.devtest-ascloud.infra.uipath-dev.com:443)
         ---> System.Net.Sockets.SocketException (11001): No such host is known.
    ```
  + The following error message means that the OMS S2S client secret is not valid. Make sure to provide the correct OMS S2S client secret.
    ```
        Call to API Service failed for Method=POST, StatusCode=BadRequest on url=https://ci-asaks5379291.devtest-ascloudgen-ea.infra.uipath-dev.com/identity_/connect/token
        Http Response Content:{"error":"invalid_client"}
    ```
  + The following error message means that there is already a tenant in the Automation Suite organization with the same tenant name as the standalone tenant name. To resolve the conflict, you must change the tenant name for the tenant in the Automation Suite organization.
    ```
    Source tenant ID: 38f03b05-3aab-422c-844b-bf3668fa54ee, target organization ID: f7d80050-9654-4f44-8a34-3a9e46380dc9, confilict tenant name: test_tenan1
    Source tenant ID: b35020b1-ee9f-4026-abd1-bb721b148e24, target organization ID: f7d80050-9654-4f44-8a34-3a9e46380dc9, confilict tenant name: test_tenant2
    Tenant name conflicts detected. You need to rename the tenant to be a different name than conflict tenant name in target organization to unblock tenant creation.
    ```

## Migration tool parameters

The following table describes the parameters that the Uipath.Organization.Migration.App tool supports. You can use these parameters on Linux and Windows.

Expand Table

| Parameter name | Short name | Description |
| --- | --- | --- |
| Identity database connection of the standalone product | `i` | The Identity database connection of the standalone product. If Identity and Orchestrator share the same database, then use the connection string of that database. |
| Identity database connection of Automation Suite | `j` | The Identity database connection of Automation Suite. |
| Orchestrator database connection of the standalone product | `o` | The Orchestrator database connection of the standalone product. If Identity and Orchestrator share the same database, then use the connection string of that database. |
| List of organization IDs of the standalone product | `s` | The list of organization IDs for the standalone product to merge. You must use the following format: `orgId1,orgId2,...,orgId5`.  The size of the organization ID list for both the standalone product and Automation Suite must be the same.  To get a list of organization IDs for the standalone product, run the following command on the standalone database and use `GlobalId` with the related partition / organization name on the restored database:  ``` SELECT * FROM [identity].[Partitions] ``` |
| List of organization IDs of Automation Suite | `d` | The list of organization IDs for Automation Suite. You must use the following format: `orgId1,orgId2,...,orgId5`.  The size of the organization ID list for both the standalone product and Automation Suite must be the same.  To get a list of organization IDs for Automation Suite, run the following command on the `AutomationSuite_Platform` database on the Automation Suite SQL Sever:  ``` SELECT * FROM [identity].[Partitions] ``` |
| Rollback | `r` | The parameter used to roll back a change. |
| URL of Automation Suite | `p` | The URL of Automation Suite. For example, `https://ci-asaks5380983.devtest-ascloudgen-ea.infra.uipath-dev.com/` |
| OMS S2S client secret | `c` | The client secret used to call the OMS API to create the tenant.  To get the OMS S2S client secret from the Kubernetes secret, run the following command:  ``` kubectl get secret identity-client-oms -n uipath -o "jsonpath={.data.OMSS2SClient\.ClientSecret}" | base64 -d ``` |