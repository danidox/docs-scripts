---
title: "Backing up and restoring the cluster"
visible: true
slug: "backing-up-and-restoring-the-cluster"
---

Automation Suite supports the backup and restore functionality to prevent data loss in various scenarios. You can configure a backup any time post-installation. Even though it is optional, enabling a backup is recommended so that you can resume from the same point in case of a disaster.

:::important
Currently, we only support restoration to the same cluster. Restoring Automation Suite to a new cluster is not supported.
:::

To use the backup and restore functionality, you must provision an additional objectstore, a backup, and a restore cluster. These concepts are defined in the following section.

## Terminology

**Objectstore** - Storage location that stores the backup data and facilitates the restoration. You must bring the objectstore to store the backup data. This objectstore must differ from the objectstore where the user files are held while using the Automation Suite cluster.

**Backup Cluster** – The cluster you set up to install Automation Suite. This is the cluster where you will enable the backup.

**Restore Cluster** – The cluster where you restore all the data from the backup cluster. This becomes the new cluster where you run Automation Suite once the restore process is complete.

## Prerequisites

:::note
This setup only enables a cluster backup, including the cluster configuration and data stored as part of the block storage. However, it does not enable the backup of any external data sources, such as the SQL database and external objectstore. You must enable the external data source backup separately. Additionally, you must ensure that you take a backup of all the databases and buckets that you provisioned during the Automation Suite installation. The data stored in FileStore and Redis ia transient and does not require to be backed up.
:::

To set up the backup and restore functionality, you must meet the following requirements:

* You must bring an additional objectstore for the backup.

  | **Kubernetes** | **Objectstore** |
  | --- | --- |
  | EKS | AWS S3 |
  | AKS | Azure Storage Account |
* The cluster you want to back up and the objectstore must be in the same region.
* During the cluster restore, you must use the same zones where you deployed Automation Suite before the disaster.
* In EKS deployments, if the original cluster uses the EBS and EFS storage classes, you must configure the restore cluster to use the same storage classes before starting the restore operation.

## Architecture

### Overview

Automation Suite leverages [Velero](https://velero.io/) to take the backup of the Kubernetes and restore it to another Kubernetes after a natural or man-made disaster.

An application-level backup in Automation Suite targets two components:

* Kubernetes objects and configurations are stored in the [etcd](https://kubernetes.io/docs/concepts/overview/components/#etcd) key/value store. Some important secrets and config maps are required to be backed up.
* Application data is stored in persistent volumes. Insights stores its data in the PVCs that must be backed up to resume to the point when the disaster happens.

etcd is a key/value store belonging to the Kubernetes Control Plane. This store is directly inaccessible and can be queried via Kubernetes API Server. Velero leverages the Kubernetes API to retrieve this data from the key/value store. Kubernetes APIs provide the flexibility to easily filter resources by namespace, resource type, or label.

Velero also takes snapshots of the cluster’s persistent volumes and restores them alongside the cluster’s objects.

### Backup and restore workflow

**Backup**

The following architecture diagram depicts how backup works in Automation Suite on EKS. Similar architecture and workflow are applicable to Automation Suite on AKS.
  ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/279755)

The backup consists of two components:

* A Velero server pod that runs in your Automation Suite cluster
* `uipathctl` command line interface (CLI) that runs on the local machine.

Whenever we issue a backup against an Automation Suite cluster, Velero performs a backup of cluster resources in the following way:

1. The `uipathctl` CLI calls the Kubernetes API server to create Velero’s backup controller object.
2. Velero's backup controller checks the backup scope via a query made to the Kube API server.
3. The backup controller queries the API Server to retrieve the etcd resources that need a backup.
4. The backup controller queries the Persistent Volume that needs a backup.
5. The backup controller compresses the retrieved Kubernetes objects into a `.tar` file and saves it in the objectstore alongside the volume back up.
   :::note
   In this process, Microsoft SQL Server (database) and external objectstore are not backed up. Since these are the external components, Velero has no control over them. For this reason, it is mandatory to enable the backup of these storage components explicitly.
   :::

**Restore**

The following architecture diagram depicts how restoring works in Automation Suite on EKS. Similar architecture and workflow are applicable to Automation Suite on AKS.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/279765)

Similarly to the backup process, whenever we issue a restore operation, the following happens:

1. The `uipathctl` CLI calls the Kubernetes API server to create a Velero’s restore controller that will restore from an existing backup.
2. Velero’s restore controller checks the restore scope via a query made to the Kube API server.
3. The restore controller retrieves the backup files from the objectstore.
4. The restore controller initiates a restore operation of the cluster configuration and persistent volume.
   :::note
   As is also the case of the backup operation, Microsoft SQL Server (Database) and external objectstore are not restored in the previous process. Since these are the external components, Velero has no control over them. That’s why it is mandatory to restore this storage component explicitly before initiating the restoration of the Automation Suite cluster.
   :::