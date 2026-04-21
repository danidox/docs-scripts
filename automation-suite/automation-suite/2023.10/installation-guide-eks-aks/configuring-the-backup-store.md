---
title: "Configuring the backup store"
visible: true
slug: "configuring-the-backup-store"
---

## Providing the backup store configuration

To back up and restore your cluster, you must provide the location of the cluster snapshots to the Automation Suite cluster via `input.json`.

Make the following changes to your `input.json` before enabling a scheduled backup or taking an on-demand backup. Follow either the EKS or AKS configuration described in the following sections, as applicable.

You can provide this information during the installation of the Automation Suite cluster or later, as a post-installation operation, while enabling or taking the backup of the cluster.

### EKS

`input.json` sample

```
"snapshot": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "<s3_bucket_used_for_backup>",
      "storage_type": "s3",
      "region": "<s3_bucket_region>"
    }
}
```

`input.json` parameters

| **Key** | **Value** |
| --- | --- |
| `bucket_name` | The name of the S3 bucket for storing the snapshot |
| `arn` | ARN for connecting with the S3.  If the node has the necessary permissions to connect to the backup objectstore, then the ARN is not needed. Otherwise, make sure to create an IAM role with the necessary permissions and add the ARN. |
| `region` | The region where the S3 is present. |

### AKS

`input.json` sample

```
"snapshot" : {
  "external_object_storage": {
    "client_secret": "<azure_service_principal_client_secret>", 
    "resource_group": "<azure_resource_group_with_storage_account>", 
    "auth_mode": "ServicePrincipal", 
    "account_name": "<azure_account_name>", 
    "bucket_name": "<azure_container_name>",
    "client_id": "<azure_service_principal_id>",
    "subscription_id": "<azure_subscription_id>",
    "cloud_name": "AzurePublicCloud"
  },
  "aks_infra_resource_group":"<azure_infra_resource_group>"
}
```

`input.json` parameters

| **Key** | **Value** |
| --- | --- |
| `bucket_name` | Name of the container in Azure Storage Account for storing the snapshot |
| `resource_group` | Resource group in which the target Azure Storage Account for storing snapshot is present. |
| `auth_mode` | Must be set to `ServicePrincipal` |
| `client_id` | Client ID for service principal authentication |
| `client_secret` | Client Secret for the service principal-based authentication |
| `account_name` | Name of the Azure Storage Account where the snapshot is backed up |
| `cloud_name` | Default value `AzurePublicCloud`  Change to one of the followin,g as applicable: `AzureUSGovernmentCloud`, `AzureChinaCloud`, `AzureGermanCloud` |
| `subscription_id` | Subscription ID where the Azure Storage Account for storing backup is stored. |
| `aks_infra_resource_group` | Resource group where the machines and other resources for the AKS cluster are created. This is usually made and managed by Azure and starts with `MC_`  While other values can remain the same during backup and restore, this value will be changed during restoration. This must be the new Resource Group where the Kubernetes resources of the new AKS cluster are provisioned. |

:::note
To create a service principal for authentication in azure, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/aks/hybrid/backup-workload-cluster).
:::

## Applying the backup store configuration

After making the changes to the `input.json`, as described in the previous section, run the following command to apply the configuration:

```
./uipathctl  manifest apply input.json --only velero --versions versions.json
```