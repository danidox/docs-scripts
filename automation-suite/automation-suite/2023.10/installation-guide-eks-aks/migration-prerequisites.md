---
title: "Migration prerequisites"
visible: true
slug: "migration-prerequisites"
---

Before starting the migration, make sure you meet the following prerequisites:

## .NET Runtime 6.0

.NET Runtime 6.0 or later is required to run the UiPath.OrganizationMigrationApp tool. You must download and install it before running UiPath.OrganizationMigrationApp.

### Linux

If.NET Runtime 6.0 or later is not present, [download and install.NET Runtime for Linux](https://docs.microsoft.com/dotnet/core/install/linux?WT.mc_id=dotnet-35129-website) before using UiPath.OrganizationMigrationApp.

To install.NET Runtime 6.0 on RHEL, run the following command:

```
sudo yum install dotnet-sdk-6.0 -y
```

### Windows

The UiPath.OrganizationMigrationApp tool requires.NET Runtime 6.0 at a minimum. If.NET Runtime 6.0 and beyond is not present, [download and install.NET Runtime 6.0 for Windows](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-aspnetcore-6.0.11-windows-x64-installer) before using UiPath.OrganizationMigrationApp.

## Orchestrator bucket creation setting

To ensure that Orchestrator buckets are automatically created with the correct CORS policy, you must run the following command. The command requires the `jq` utility to be installed on your machine.

```
rm -f values.json && rm -f appsettings.json
kubectl -n uipath get cm orchestrator-customconfig -o jsonpath='{.data.values\.json}' | jq '.' > values.json
jq '.AppSettings' values.json > appsettings.json
jq '.["Storage.CreateBucket.OnTenantCreation.Enabled"] = "true"' appsettings.json > temp.json && mv -f temp.json appsettings.json
uipathctl config orchestrator update-config --app-settings appsettings.json
```

To install `jq`, use one of the following options:

* Option 1: Run the following command:
  ```
  yum install -y epel-release yum install -y jq
  ```
* Option 2: Run the following commands:
  ```
  shell
  curl https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/j/jq-1.6-2.el7.x86_64.rpm --output /tmp/jq-1.6-2.el7.x86_64.rpm
  yum localinstall /tmp/jq-1.6-2.el7.x86_64.rpm
  ```

:::warning
Failing to enable the Orchestrator setting that ensures buckets are automatically created with the correct CORS policy causes issues with downloading from storage buckets, which you must address by making manual updates to the CORS policy.
:::

To confirm that the setting has been enabled, run the following command:

```
kubectl -n uipath get cm orchestrator-customconfig -o jsonpath='{.data.values\.json}' | jq
```

If the setting has been enabled, the command should return the following response:

```
{
  "AppSettings": {
    "Storage.CreateBucket.OnTenantCreation.Enabled": "true"
  }
}
```

## UiPath.OrganizationMigrationApp

The UiPath.OrganizationMigrationApp tool helps you perform operations such as move the Identity data of all tenants from standalone to Automation Suite and merge organizations.

To download UiPath.OrganizationMigrationApp, see [Downloading the installation packages](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/downloading-the-installation-packages#uipathorganizationmigrationapp).

To see which UiPath.OrganizationMigrationApp version is compatible with your environment, see [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-compatibility-matrix#migration-compatibility-matrix).

## Tool for managing Microsoft SQL Server

You must download and install SQL Server Management Studio (SSMS) or a similar tool for managing Microsoft SQL Server. This tool helps you restore the Orchestrator database to the Automation Suite SQL Server instance or a different SQL Server instance.

1. Download and install [SQL Server Management Studio](https://aka.ms/ssmsfullsetup).
2. Log into the standalone SQL Server using the standalone SQL connection string.
3. Open port `1433` for the source and target database.

## Special character escape rules for connection string passwords

In most instances, connection passwords are encapsulated within a single quotation mark (`'`). However, when the password includes special characters such as `` ` `` or `$`, a different approach is required.

In these cases, the password must be formatted as `` \`"<password>\`" ``, replacing `<password>` with the actual password. Moreover, you must also adhere to the escape rules as detailed in the following table:

| **Original format in ADUC** | **Escaped format in PowerShell string** |
| --- | --- |
| `cn=James $ Smith` | `` "cn=James `$ Smith" `` |
| `cn=Sally Wilson + Jones` | `"cn=Sally Wilson \+ Jones"` |
| `cn=William O'Brian` | `"cn=William O'Brian"` |
| `` cn=William O`Brian `` | ``` "cn=William O``Brian" ``` |
| `cn=Richard #West` | `"cn=Richard #West"` |
| `cn=Roy Johnson$` | `"cn=Roy Johnson$"` |

### Example

Assume that the original password is `7'8:<=XMe$y[@vC?_4ZeY8c-~y'W!1dU4gnczuf'/p>j<I`. Adhering to the special character escape rules, it becomes: ```` Password=\`"7'8:<=XMe`$y[@vC?_4ZeY8c-~y'W!1dU4```gnczuf'/p>```j<I\`" ````.

The full command, with the password configured in destination connection string, looks as follows:

```
./UiPath.OrganizationMigrationApp.exe migrate -a -m -s "Server=tcp:abc.com,1433;Initial Catalog=UiPath_20230531;Persist Security Info=False;User ID=username;Password=asiodhyf;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;" -d "Server=tcp:cde.net,1433;Initial Catalog=AutomationSuite_Platform;Persist Security Info=False;User Id=testadmin@sfdev3980732-sql.database.windows.net;Password=\`"7'8:<=XMe`$y[@vC?_4ZeY8c-~y'W!1dU4```gnczuf'/p>```j<I\`""
```

:::note
Ensure that the command only gets executed on a machine that has authorized access to the RDS database.
:::

## Administrator group configuration requirement

Before starting the migration, you must add the Administrator group in every tenant.

If you are performing an organization merge and the Administrator group is not added in all tenants, you can lock yourself out of the Orchestrator instance after the merge completes.

Adding the Administrator group in each tenant ensures that administrative access is preserved throughout the migration and merge process.

## Test Manager migration script

The Test Manager migration script (`testmanager_migrator.sh`) helps you to perform multiple automatic operations for migrating various configurations and files, such as:

* Execute `kubectl` operations, such as updating secrets and configurations maps.
* Perform ArgoCD synchronizations via the CLI.
* Override configuration settings and restart deployments.
* Add storage files to the Ceph object store.
* Restore and update the `DataEncryptionKey` in the Kubernetes secrets from the MSI instance.
* Synchronize Test Manager in ArgoCD.
* Migrate folders or files from a Windows file store to the destination object store, creating the required directory hierarchy in the bucket defined by Kubernetes secrets.

### Environment requirements to run the Test Manager migration script

To successfully run the Test Manager migration script you need to ensure you meet the following environment requirements:

* Configure `kubectl` with a connection to the Automation Suite cluster.
  :::important
  Ensure that `kubeconfig` is set as an environment variable.
  :::
* Install the `jq` utility using the following command `yum install jq`.
* Install the `argocd` CLI. Visit [Installing Argo CD](https://argo-cd.readthedocs.io/en/stable/cli_installation/#download-with-curl) for more information.
* Install Rclone. Visit the [RClone documentation](https://rclone.org/install/) for more information.
  :::note
  Minimum required version for Rclone is 1.56.0.
  :::

:::note
If your Identity is managed in Azure, then make sure you run the script using an Azure machine.
:::

### Common Test Manager migration script commands

Check the following commands that you can perform using the Test Manager migration script:

```
 ./testmanager_migrator.sh -d -y \
  -k \"enc key value\" \
  -s blobstoragefolder
    -k|--encryption-key
        The value of the encryption key that will override the key generated during installation.
    -s|--storage-folder
        The location of the storage folder on the local disk.
    -is-|--use-incluster-storage
        Use in cluster Ceph object store.
    -d|--dry-run
        Do not update Test Manager with the new values
    -y|--accept-all
        Do not prompt for confirmation of actions
```