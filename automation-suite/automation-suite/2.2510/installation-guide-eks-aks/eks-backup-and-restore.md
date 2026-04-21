---
title: "EKS backup and restore"
visible: true
slug: "eks-backup-and-restore"
---

Amazon EKS does not include a native AWS solution for backing up and restoring cluster resources. AWS recommends using [Velero](https://velero.io/docs/v1.17/), an open-source tool for Kubernetes backup and recovery.

For more details, refer to the following AWS resources:

* [Amazon EKS backup and restore FAQs](https://repost.aws/knowledge-center/eks-cluster-back-up-restore)
* [Backing up and restoring Amazon EKS cluster resources using Velero](https://aws.amazon.com/blogs/containers/backup-and-restore-your-amazon-eks-cluster-resources-using-velero/)

Automation Suite on EKS uses two main storage types:

* **Amazon EBS (Elastic Block Store)** - This provides block-level storage for Kubernetes workloads.
* **Amazon EFS (Elastic File System)** - This provides shared file storage for workloads that require concurrent access.

To support both storage types and cross-region disaster recovery, UiPath recommends using Velero File System Backup (FSB) with Amazon S3 and Cross-Region Replication (CRR).

With this configuration, backups are stored in the designated S3 bucket, and CRR automatically replicates them to a secondary AWS region for resiliency.

## Prerequisites

Before setting up Velero, make sure the following prerequisites are met:

* Velero installation: You must deploy Velero in the EKS cluster using Helm or the Velero CLI.
* IAM permissions: You must grant the Velero service account the required permissions to write to Amazon S3.
* S3 bucket: You must create an Amazon S3 bucket with versioning enabled.

For detailed setup instructions, refer to the official [Velero File System Backup](https://velero.io/docs/v1.17/file-system-backup/#setup-file-system-backup) setup guide.

## Configuring Velero policies

Velero supports flexible policies that determine which resources and volumes are included in backups. For more information about configuring Velero backup policies, refer to the [official Velero](https://velero.io/docs/v1.17/resource-filtering/#resource-policies) documentation.

When defining a backup policy, consider the following guidelines:

* PVC exclusion: You must exclude any `PersistentVolumeClaim` (PVC) labeled with `velero.io/exclude-from-backup: "true"`. Velero skips any PVC with this label during the backup process.
* Configuring file system backup: You must apply file system backups to PVCs that use supported storage classes. The following storage classes support file system backups:
  + EFS storage class (`efs-sc`)
  + EBS storage class (`ebs-sc`)Use the following sample policy to configure exclusions and file system backups for these storage classes:
  ```
  policy: |
    version: v1
    volumePolicies:
      - conditions:
          pvcLabels:
            velero.io/exclude-from-backup: "true"
        action:
          type: skip
      - conditions:
          csi:
            driver: efs.csi.aws.com
          storageClass:
            - efs-sc
        action:
          type: fs-backup
      - conditions:
          csi:
            driver: ebs.csi.aws.com
          storageClass:
            - ebs-sc
        action:
          type: fs-backup
  ```
* Backup destination: With file system backup, all backup data is uploaded to the configured Amazon S3 bucket. If Cross-Region Replication (CRR) is enabled, backups are automatically replicated across regions for improved resiliency.

## Running backups and restores

To create a backup in Velero:

* Follow the [Velero backup](https://velero.io/docs/v1.17/file-system-backup/#to-back-up) guide.
* Configure a Backup Custom Resource (CR) to define the namespaces and resources included in the backup.

Automation Suite namespaces are automatically labeled with `created-by=uipath`. You can selectively back up only UiPath-related namespaces by including only those labeled with this key. This ensures all UiPath-specific resources are safely backed up.

For details, refer to [Velero resource filtering](https://velero.io/docs/v1.17/resource-filtering/).

To restore workloads from a backup:

* Follow the [Velero restore](https://velero.io/docs/v1.17/file-system-backup/#to-restore) guide.
* Reference a Restore Custom Resource (CR) that specifies the backup and target resources.
  :::important
  When restoring in a cluster that has the Cluster Autoscaler enabled, Velero may report partial restore failures. You might see an error such as `node-agent pod is not running in node: daemonset pod not found in running state in node`. If you encounter this issue, you must check the status of `podvolumerestore (PVR)` objects. If all PVRs show `Success`, you can consider the restore successful. For details, refer to [Velero issue #7170](https://github.com/vmware-tanzu/velero/issues/7170) and [Velero issue #9203.](https://github.com/vmware-tanzu/velero/issues/9203)
  :::