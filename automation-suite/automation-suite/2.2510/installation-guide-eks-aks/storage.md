---
title: "Storage"
visible: true
slug: "storage"
---

In addition to Microsoft SQL Server, the Automation Suite cluster requires a storage component to store the files. Automation Suite requires the objectstore and the block/file storage, depending on the service type you choose.

## Storage estimate for each Automation Suite component

### UiPath® platform services

The following services require the storage component. These are only necessary if you have opted to enable them as part of the Automation Suite installation or later.

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Service
    </p>
   </th>
   <th>
    <p>
     Storage type
    </p>
   </th>
   <th>
    <p>
     Purpose
    </p>
   </th>
   <th>
    <p>
     Estimate
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d27941e36">
    <p>
     Orchestrator
    </p>
   </td>
   <td headers="d27941e39">
    <p>
     Objectstore
    </p>
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      <p>
       NuGet automation packages for deployed automation
      </p>
     </li>
     <li>
      <p>
       Queues and their data
      </p>
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <p>
     Typically, a package is 5 Mb, and buckets, if any, are less than 1 Mb. A mature enterprise deploys around 10 GB of packages
                                    and 12 GB of Queues.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    <p>
     Action Center
    </p>
   </td>
   <td headers="d27941e39">
    <p>
     Objectstore
    </p>
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      <p>
       Documents stored by the user in document tasks
      </p>
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <p>
     Typically, a document takes 0.15 Mb, and the forms to fill take an additional 0.15 Kb. In a mature enterprise, this can total
                                    4 GB.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    <p>
     Test Manager
    </p>
   </td>
   <td headers="d27941e39">
    <p>
     Objectstore
    </p>
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      <p>
       Attachments and screenshots stored by users
      </p>
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <p>
     Typically, all files and attachments add up to approximately 5 GB.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    <p>
     Insights
    </p>
   </td>
   <td headers="d27941e39">
    <p>
     Blockstore
    </p>
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      <p>
       Published dashboards and their metadata
      </p>
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <p>
     2 GB is required for enablement, with the storage footprint growing with the number. A well-established enterprise-scale deployment
                                    requires another few GB for all the dashboards. Approximately 10GB of storage should be sufficient.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    Integration Service
   </td>
   <td headers="d27941e39">
    Objectstore
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      Connector metadata
     </li>
     <li>
      Event triggers
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    Connectors vary in size, but installing all the available connectors should consume less than 100 MB. Trigger events vary
                                 in number based on usage, but 5 GB should be sufficient.
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    Studio Web
   </td>
   <td headers="d27941e39">
    Filestore
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      NuGet packages downloaded from specified feeds (official UiPath feed, api.nuget.org)
     </li>
     <li>
      Projects created or imported in Studio Web
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <ul>
     <li>
      NuGet packages: 220 GB
     </li>
     <li>
      User projects: 50 GB
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    <p>
     Apps
    </p>
   </td>
   <td headers="d27941e39">
    <p>
     Objectstore
    </p>
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      <p>
       Attachments that are uploaded to Apps
      </p>
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <p>
     Typically, the database takes approximately 5 GB, and a typical complex app consumes about 15 Mb.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    <p>
     AI Center
    </p>
   </td>
   <td headers="d27941e39">
    <p>
     Objectstore / Filestore
    </p>
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      <p>
       ML Packages
      </p>
     </li>
     <li>
      <p>
       Datasets for analysis
      </p>
     </li>
     <li>
      <p>
       Training Pipelines
      </p>
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <p>
     A typical and established installation will consume 8 GB for five packages and an additional 1 GB for the datasets.
    </p>
    <p>
     A pipeline may consume an additional 50 GB of block storage, but only when actively running.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    <p>
     Document Understanding
    </p>
   </td>
   <td headers="d27941e39">
    <p>
     Objectstore
    </p>
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      <p>
       ML model
      </p>
     </li>
     <li>
      <p>
       OCR model
      </p>
     </li>
     <li>
      <p>
       Stored documents
      </p>
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <p>
     In a mature deployment, 12GB will go to the ML model, 17GB to the OCR, and 50GB to all documents stored.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    <p>
     Automation Suite Robots
    </p>
   </td>
   <td headers="d27941e39">
    <p>
     Filestore
    </p>
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      <p>
       Caching the packages required to run an automation
      </p>
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <p>
     Typically, a mature enterprise deploys around 10 GB of packages.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    <p>
     Process Mining
    </p>
   </td>
   <td headers="d27941e39">
    <p>
     Objectstore
    </p>
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      <p>
       SQL files that are required to run queries in the SQL warehouse
      </p>
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <p>
     The minimal footprint is only used to store the SQL files. Approximately a GB of storage should be enough in the beginning.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    Context Grounding
   </td>
   <td headers="d27941e39">
    Objectstore, File store
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      Object store is used to store the micro front end data
     </li>
     <li>
      File store is used as a cache to process the files
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <ul>
     <li>
      Recommended object store size is 50GB
     </li>
     <li>
      Recommended pvc size is 1 TB
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    LLM Observability
   </td>
   <td headers="d27941e39">
    Objectstore
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      To store user LLM prompt inputs and outputs
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <ul>
     <li>
      Recommended size is 10GB
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27941e36">
    Solutions
   </td>
   <td headers="d27941e39">
    Filestore
   </td>
   <td headers="d27941e42">
    <ul>
     <li>
      To store solutions package bundles and package files
     </li>
    </ul>
   </td>
   <td headers="d27941e45">
    <ul>
     <li>
      Recommended size is 200GB
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

### Shared suite services

The following shared suite services require the storage component. These are only necessary if you opted to install them as part of the Automation Suite installation.

| Service | Storage type | Purpose | Estimate |
| --- | --- | --- | --- |
| Monitoring | Block storage | Kubernetes and infrastructure related metrics data | Approximately around 100 GB to store the last ten days of monitoring data |
| Logging | Block storage | Application running logs | About 20 GB to keep the previous few days of the logs |

## Objectstore

Automation Suite supports the following objectstores:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" data-condition="(AutomationSuiteFlavor=AutomationSuiteOnEKSAKS)" id="GUID-FD44AC9B-FB5F-4CF9-AF67-657A48ED6BE1__TABLE_OBV_DQV_VCC" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Kubernetes
    </p>
   </th>
   <th>
    <p>
     Objectstore
    </p>
   </th>
   <th>
    <p>
     Supported authentication
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d27941e360">
    <p>
     EKS
    </p>
   </td>
   <td headers="d27941e363">
    <p>
     Amazon S3
    </p>
   </td>
   <td headers="d27941e366">
    <ul>
     <li>
      <p>
       AWS Instance Profile
      </p>
     </li>
     <li>
      <p>
       Access Key and Secret Key
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d27941e360">
    <p>
     AKS
    </p>
   </td>
   <td headers="d27941e363">
    <p>
     Azure Storage (blob)
    </p>
   </td>
   <td headers="d27941e366">
    <ul>
     <li>
      <p>
       Account Key
      </p>
     </li>
     <li>
      <p>
       Workload Identity
       <sup>
        *
       </sup>
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

<sup>*</sup>Insights currently does not support workload identity for authentication.

### Configuring the CORS policy

Additionally, you may have to enable the following CORS policy at the storage account/bucket level if you face any CORS-related error during the S3 connection while using the Automation Suite cluster.

Make sure to replace `{{fqdn}}` with the FQDN of the Automation Suite cluster in the following CORS policy.

The following sample shows the CORS policy in JSON format:

**JSON**
```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "POST",
            "GET",
            "HEAD",
            "DELETE",
            "PUT"
        ],
        "AllowedOrigins": [
            "https://{{fqdn}}"
        ],
        "ExposeHeaders": [
            "etag",
            "x-amz-server-side-encryption",
            "x-amz-request-id",
            "x-amz-id-2"
        ],
        "MaxAgeSeconds": 3000
    }
]
```

The following sample shows the CORS policy in XML format:

**XML**
```
<CORSConfiguration>
 <CORSRule>
   <AllowedOrigin>{{fqdn}}</AllowedOrigin>
   <AllowedMethod>HEAD</AllowedMethod>
   <AllowedMethod>GET</AllowedMethod>
   <AllowedMethod>PUT</AllowedMethod>
   <AllowedMethod>POST</AllowedMethod>
   <AllowedMethod>DELETE</AllowedMethod>
   <AllowedHeader>*</AllowedHeader>
  <MaxAgeSeconds>3000</MaxAgeSeconds>
  <ExposeHeader>x-amz-server-side-encryption</ExposeHeader>
  <ExposeHeader>x-amz-request-id</ExposeHeader>
  <ExposeHeader>x-amz-id-2</ExposeHeader>
  <ExposeHeader>etag</ExposeHeader>
 </CORSRule>
</CORSConfiguration>
```

### Configuration

To configure the objectstore, see [External Objectstore Configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#external-objectstore-configuration).

:::note
Since the containers are created within the scope of the Azure Storage Account, it is recommended to have a separate container for each service. Similarly, in AWS, it is highly recommended to have a dedicated bucket for each service installed on Automation Suite. However, if the bucket is created globally, you may face limitations in providing the dedicated bucket for each service. In this case, you can configure a single bucket and use it for all purposes.
:::

The Automation Suite installer supports creating the containers/buckets if you provide `make` permissions. Alternatively, you can provision the required containers/buckets before installation and their information to the installer.

#### Required buckets for Integration Service

In an AKS installation, you must create multiple blob storage buckets in Azure Storage. This step is not required in an EKS installation, which uses single buckets.

You must create the following buckets manually prior to installation:

* `gallupx-poller-data`
* `gallupx-job-engine-state`
* `gallupx-notification-objects`
* `gallupx-webhook`
* `gallupx-execution-trace`

### Storage requirements

| Storage | Requirement |
| --- | --- |
| Objectstore | 500 GB |

The size of the objectstore depends on the size of the deployed and running automation. Therefore, it can be challenging to provide an accurate objectstore estimate initially during the installation. You can start with an objectstore size of 350 GB to 500 GB. To understand the usage of the objectstore, see [Storage estimate for each Automation Suite component](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/storage#storage-estimate-for-each-automation-suite-component).

:::note
* As your automation scales, you may need to account for the increase in your
objectstore size.
:::

## Block storage

Block storage must have CSI drivers configured with the Kubernetes storage classes.

The following table provides details of the block storage, storage class, and provisioner:

| Cloud / Kubernetes | Storage | StorageClass | Provisioner |
| --- | --- | --- | --- |
| AWS | EBS Volumes | `ebs-sc` | `ebs.csi.aws.com` |
| Azure | Azure Manage Disk | `managed-premium`  Premium LRS Disk | `disk.csi.azure.com` |

### Configuration

You can follow the official guides from [AWS](https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html) and [Azure](https://learn.microsoft.com/en-us/azure/aks/azure-disk-csi) to create a storage class in your EKS and AKS clusters.

You must pass the name of the storage class you created for your cluster to the `storage_class` parameter in the `input.json` file.

:::note
* Sometimes, the EKS or AKS cluster installs the CSI driver and provides the storage
class. If these storage classes are not configured, you must configure them before the Automation Suite installation.
* You must make the storage class for the block storage the default one, as shown in the following example.
:::

#### Example

The following example shows how to configure the storage class and how to provide it to `input.json` file during installation:

Expand Table

| Configuration | `input.json` | `StorageClass` |
| --- | --- | --- |
| Azure | ``` {   "storage_class": "managed_premium" } ``` | ``` allowVolumeExpansion: true apiVersion: storage.k8s.io/v1 kind: StorageClass metadata:   creationTimestamp: "2023-06-15T09:34:17Z"   labels:     addonmanager.kubernetes.io/mode: EnsureExists     kubernetes.io/cluster-service: "true"     storageclass.kubernetes.io/is-default-class: "true"   name: managed-premium parameters:   cachingmode: ReadOnly   kind: Managed   storageaccounttype: Premium_LRS provisioner: disk.csi.azure.com reclaimPolicy: Delete volumeBindingMode: WaitForFirstConsumer ``` |
| AWS | ``` {   "storage_class": "ebs-sc" } ``` | ``` allowVolumeExpansion: true apiVersion: storage.k8s.io/v1 kind: StorageClass metadata:   name: ebs-sc   annotations:    storageclass.kubernetes.io/is-default-class: "true" provisioner: ebs.csi.aws.com reclaimPolicy: Delete volumeBindingMode: WaitForFirstConsumer ``` |

### Storage requirements

| Configuration | Requirement |
| --- | --- |
| Block storage | 50 GB |

The size of the block store depends on the size of the deployed and running automation. Therefore, it can be challenging to provide an accurate estimate initially during the installation. You can start with a block storage size of 50 GB. To understand the usage of the block store, see [Storage estimate for each Automation Suite component](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/storage#storage-estimate-for-each-automation-suite-component).

:::note
As your automation scales, you may need to account for the increase in your block storage size.
:::

## File storage

File storage must have CSI drivers configured with the Kubernetes storage classes.

| Cloud / Kubernetes | Storage | StorageClass | Provisioner |
| --- | --- | --- | --- |
| AWS | EFS | `efs-sc` | `efs.csi.aws.com` |
| Azure | Azure Files | `azurefile-csi-premium`* | `file.csi.azure.com` |

* Use the `azurefile-csi-premium` storage class for Studio Web on AKS.
* It is recommended to configure ZRS (or replication) for Studio Web storage to ensure high availability.
* Worker node disks should have at least 2300 IOPS, and the **StorageCluster** should be configured using the **Performance Profile** and **SKU Profile** with a minimum of 5000 IOPS.

### Configuration

You can follow the official guides from [AWS](https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html) and [Azure](https://learn.microsoft.com/en-us/azure/aks/azure-disk-csi) to create a storage class in your EKS and AKS clusters.

You must pass the name of the storage class you created for your cluster to the `storage_class_single_replica` parameter in the `input.json` file.

:::note
Sometimes, the EKS or AKS cluster installs the CSI driver and provides the storage class. If this storage class is not configured, you must configure it before the Automation Suite installation.
:::

#### Example

The following example shows how to configure the storage class and how to provide it to `input.json` during the installation:

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
    <p>
     Configuration
    </p>
   </th>
   <th>
    <p>
     <code>
      input.json
     </code>
    </p>
   </th>
   <th>
    <p>
     <code>
      StorageClass
     </code>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d27941e897">
    <p>
     Azure
    </p>
   </td>
   <td headers="d27941e900">
    <button>
     assignment
    </button>
    <pre>{
  "storage_class_single_replica": "azurefile-csi-premium"
}</pre>
   </td>
   <td headers="d27941e904">
    <button>
     assignment
    </button>
    <pre>allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  labels:
    addonmanager.kubernetes.io/mode: EnsureExists
    kubernetes.io/cluster-service: "true"
  name: azurefile-csi
mountOptions:
- mfsymlinks
- actimeo=30
- nosharesock
- dir_mode=0700
- file_mode=0700
- uid=1000
- gid=1000
- nobrl
- cache=none
parameters:
  skuName: Standard_LRS
provisioner: file.csi.azure.com
reclaimPolicy: Delete
volumeBindingMode: Immediate</pre>
   </td>
  </tr>
  <tr>
   <td headers="d27941e897">
    Azure
   </td>
   <td headers="d27941e900">
    <button>
     assignment
    </button>
    <pre>{
  "storage_class_name_with_rwx_support": "managed-rwx"
}</pre>
   </td>
   <td headers="d27941e904">
    <button>
     assignment
    </button>
    <pre>apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: managed-rwx
provisioner: file.csi.azure.com
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
parameters:
  storageaccounttype: Standard_LRS
  enableLargeFileShares: "true"</pre>
   </td>
  </tr>
  <tr>
   <td headers="d27941e897">
    <p>
     AWS
    </p>
   </td>
   <td headers="d27941e900">
    <button>
     assignment
    </button>
    <pre>{
  "storage_class_single_replica": "efs-sc"
}</pre>
   </td>
   <td headers="d27941e904">
    <button>
     assignment
    </button>
    <pre>allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: efs-sc
parameters:
  basePath: /dynamic_provisioning
  directoryPerms: "700"
  fileSystemId: $(EFS_ID)
  gidRangeEnd: "2000"
  gidRangeStart: "1000"
  provisioningMode: efs-ap
provisioner: efs.csi.aws.com
reclaimPolicy: Delete
volumeBindingMode: Immediate</pre>
    Note:
Replace
    <code>
     $(EFS_ID)
    </code>
    with the actual File Share ID you created while provisioning infrastructure.
   </td>
  </tr>
  <tr>
   <td headers="d27941e897">
    AWS
   </td>
   <td headers="d27941e900">
    <button>
     assignment
    </button>
    <pre>{
  "storage_class_name_with_rwx_support": "efs-sc-rwx"
}</pre>
   </td>
   <td headers="d27941e904">
    <button>
     assignment
    </button>
    <pre>allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: efs-sc-rwx
parameters:
  basePath: /dynamic_provisioning
  directoryPerms: "700"
  fileSystemId: $(EFS_ID)
  gidRangeEnd: "2000"
  gidRangeStart: "1000"
  provisioningMode: efs-ap
provisioner: efs.csi.aws.com
reclaimPolicy: Delete
volumeBindingMode: Immediate</pre>
    Note: Replace
    <code>
     $(EFS_ID)
    </code>
    with the actual File Share ID you created while provisioning infrastructure.
   </td>
  </tr>
 </tbody>
</table>

:::note
Storage class for the file share must have the required permissions set to 700 for the directory and files. Additionally, `UID` and `GID` must be set to 1000 in Azure, and `gidRangeStart` and `gidRangeEnd` to 1000 and 2000, respectively, in AWS.
:::

### Storage requirements

| Storage | Requirement |
| --- | --- |
| File storage | 510 GB |

The size of the file store depends on the size of the deployed and running automation. Therefore, it can be challenging to provide an actual estimate initially, during the installation. However, you should expect approximately 510 GB of storage size to be enough to run ten concurrent training pipelines and for Automation Suite Robots. To understand the usage of the filestore, see [Storage estimate for each Automation Suite component](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/storage#storage-estimate-for-each-automation-suite-component).

:::note
As your automation scales, you may need to account for an increase in the size of your file storage.
:::

## Queues

You must manually create the following queues in your cloud provider prior to installation. These queues are required to support events and webhooks.

* `gallupx-debug-engine-tasks`
* `gallupx-engine-tasks`
* `gallupx-cron-tasks`
* `gallupx-tick-tasks`
* `gallupx-event-tasks`
* `gallupx-notification-tasks`
* `gallupx-webhook-engine-tasks`
* `gallupx-fps-engine-tasks`

For Automation Suite on EKS, you must manually add a specific prefix to the queues, as shown in the following examples:

* `<queuePrefix>-gallupx-debug-engine-tasks`
* `<queuePrefix>-gallupx-engine-tasks`
* `<queuePrefix>-gallupx-cron-tasks`
* `<queuePrefix>-gallupx-tick-tasks`
* `<queuePrefix>-gallupx-event-tasks`
* `<queuePrefix>-gallupx-notification-tasks`
* `<queuePrefix>-gallupx-webhook-engine-tasks`
* `<queuePrefix>-gallupx-fps-engine-tasks`

The `queuePrefix` value must match the value of the mandatory `queue_prefix` parameter used in [EKS input.json](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/eks-inputjson-example#eks-inputjson-example).

If you use Amazon Simple Queue Service (SQS), you need to create eight additional dead-letter queues (DLQs). You need to associate each DLQ with its corresponding primary queue.

You need to configure each queue except `gallupx-engine-tasks` with the following settings:

* Message retention period: 14 days
* Maximum message size: 256 KB
* Dead-letter queue: Enabled
* Default visibility timeout: 30 seconds

You need to configure the `gallupx-engine-tasks` queue with the same settings, except:

* Default visibility timeout: 15 minutes

You must have 18 queues in total, nine primary queues and nine associated dead-letter queues, as shown in the following example:

```
prefix-gallupx-core  
prefix-gallupx-core-deadletter  
prefix-gallupx-cron-tasks  
prefix-gallupx-cron-tasks-deadletter  
prefix-gallupx-debug-engine-tasks  
prefix-gallupx-debug-engine-tasks-deadletter  
prefix-gallupx-engine-tasks  
prefix-gallupx-engine-tasks-deadletter  
prefix-gallupx-event-tasks  
prefix-gallupx-event-tasks-deadletter  
prefix-gallupx-fps-engine-tasks  
prefix-gallupx-fps-engine-tasks-deadletter  
prefix-gallupx-notification-tasks  
prefix-gallupx-notification-tasks-deadletter  
prefix-gallupx-tick-tasks  
prefix-gallupx-tick-tasks-deadletter  
prefix-gallupx-webhook-engine-tasks  
prefix-gallupx-webhook-engine-tasks-deadletter
```

## Backup and restore

To back up the Automation Suite cluster, you need an additional objectstore to back up the cluster configuration and user data.

The following table describes the supported storage for the backup:

| Kubernetes | Objectstore |
| --- | --- |
| EKS | AWS S3 |
| AKS | Azure Storage Account |

:::note
A separate objectstore is recommended for storing the backup.
:::

## Storage authentication

### Workload identity-based access to your storage account from AKS

For general information on workload identity, see [Workload identity configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#workload-identity-configuration).

To set up your storage account to use workload identity, run the following commands:

```
az role assignment create --assignee $userAssignedManagedIdentityObjectId --role "Storage Account Contributor" --scope "/subscriptions/$($infraJson.subscription_id)/resourceGroups/$(TARGET_RG)/providers/Microsoft.Storage/storageAccounts/$(STORAGE_ACCOUNT_NAME)"
az role assignment create --assignee $userAssignedManagedIdentityObjectId --role "Storage Blob Data Owner" --scope "/subscriptions/$($infraJson.subscription_id)/resourceGroups/$(TARGET_RG)/providers/Microsoft.Storage/storageAccounts/$(STORAGE_ACCOUNT_NAME)"
az role assignment create --assignee $userAssignedManagedIdentityObjectId --role "Storage Queue Data Contributor" --scope "/subscriptions/$($infraJson.subscription_id)/resourceGroups/$(TARGET_RG)/providers/Microsoft.Storage/storageAccounts/$(STORAGE_ACCOUNT_NAME)"
```

The following sample shows a valid `input.json` configuration for an Azure storage account:

```
"external_object_storage": {
  "enabled": true,
  "storage_type": "azure",
  "account_name": "storaccid5730469",
  "azure_fqdn_suffix": "core.windows.net",
  "use_managed_identity": false,
  "use_workload_identity": true
},
```