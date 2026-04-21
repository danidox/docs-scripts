---
title: "Overriding cluster-level storage configuration"
visible: true
slug: "overriding-cluster-level-storage-configuration"
---

Orchestrator supports the following storage configurations:

* Cluster-level storage configuration;
* Orchestrator-level storage configuration.

We recommend using the cluster-level configuration paired with external storage. This allows Orchestrator to automatically detect and use the settings, eliminating the need for additional configuration.

## Configuring Azure/Amazon S3 storage buckets

To configure the Orchestrator-level storage provider, update the Orchestrator parameters by taking the following steps. For more details, see [Configuring the Orchestrator parameters](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-orchestrator-parameters#configuring-orchestrator-parameters).

1. In the configuration file, under `orchestrator`, add the `legacy_storage_provider` section that contains the storage type and connection string, as shown in the following example:
   ```
   "orchestrator": {
     "enabled": true,
     "legacy_object_storage": {
       "type": "Azure",
       "connection_string": "DefaultEndpointsProtocol=https;AccountName=usr;AccountKey=...;EndpointSuffix=core.windows.net"
     }
   }
   ```
2. Set the desired provider using the `type` parameter. The possible values are: `Azure`, `AWS`, and `Minio`. A few considerations:
   * The `storage.type` parameter values are case-sensitive;
   * FileSystem storage configuration is not supported.
3. Add the connection string for the storage provider using the `connection_string` parameter. For details on the connection strings format, see the `Storage.Location` section of [UiPath.Orchestrator.dll.config](https://docs.uipath.com/orchestrator/standalone/2023.10/installation-guide/uipath-orchestrator-dll-config#deployment).
   :::note
   Orchestrator web browser access to Amazon and Azure storage buckets could be restricted due to the same-origin policy on the provider side. To successfully access the content of such a bucket, you must configure the respective provider to allow cross-origin requests from Orchestrator. For instructions, see [CORP/CSP configuration](https://docs.uipath.com/orchestrator/automation-suite/2023.10/user-guide/cors-csp-configuration).
   :::

## Configuring SMB network share

To use network FileStore, edit the following Orchestrator ArgoCD app parameters:

* `storage.type = smb`
* `storage.smb.domain`
* `storage.smb.password`
* `storage.smb.source`
* `storage.smb.username`
* `storage.smb.size`

## Uploading files to storage

When Orchestrator uses cluster-level storage configuration, files can be uploaded to the storage using the Orchestrator Configurator Tool. To do that, use the following command:

```
./orchestrator_configurator.sh -s path
```

The subfolders from the path will be uploaded to the configured storage.

If you use an external storage configuration at the cluster level, you must indicate this by including the `--use-external-storage` flag.