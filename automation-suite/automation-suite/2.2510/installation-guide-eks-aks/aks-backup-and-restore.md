---
title: "AKS backup and restore"
visible: true
slug: "aks-backup-and-restore"
---

Azure provides backup capabilities for AKS clusters through the AKS Backup Extension, with additional protection available through Azure Files Backup for clusters that use Azure Files persistent volumes. You configure these separately, as follows:

* **AKS Backup Extension** - This is the native backup solution for AKS. It allows you to protect Kubernetes resources such as deployments, services, configmaps, secrets, and CSI-based Azure Disk persistent volumes. For details, refer to [Using the AKS Backup Extension](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/aks-backup-and-restore#using-the-aks-backup-extension).
* **Azure Files Backup** - This is required when you use Azure Files persistent volumes, because they are not included in the AKS Backup Extension. For details, refer to [Using Azure Files Backup](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/aks-backup-and-restore#using-azure-files-backup).

## Using the AKS Backup Extension

The AKS Backup Extension is the native backup solution for AKS. It protects cluster resources and CSI-based Azure Disk volumes.

To learn more about capabilities and supported scenarios, refer to [Overview](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-backup-overview) section from the official AKS documentation.

For configuration and backup steps, refer to the official AKS documentation, as follows:

* [Configure backups using the Azure portal](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-cluster-backup)
* [Configure backups using Azure CLI](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-cluster-backup-using-cli)
* [Configure backups using PowerShell](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-cluster-backup-using-powershell)

To restore backups, refer to the official AKS documentation, as follows:

* [Restore using the Azure portal](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-cluster-restore)
* [Restore using Azure CLI](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-cluster-restore-using-cli)
* [Restore using PowerShell](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-cluster-restore-using-powershell)
  :::important
  The AKS Backup Extension only supports Azure Disk CSI volumes. If your workloads use Azure Files or other volume types, you must configure a separate backup solution.
  :::
:::note
You can perform a selective backup of only UiPath-related resources by specifying namespaces labeled `created-by=uipath` when configuring backup. To list these namespaces, run the following command: assignment
```
kubectl get namespaces -l created-by=uipath -o jsonpath='{.items[*].metadata.name}'
```
:::

## Using Azure Files Backup

Azure Files persistent volumes are not included in the AKS Backup Extension. To protect these volumes, you need to configure Azure Files Backup separately.

To learn more about Azure Files Backup, refer to the official [AKS documentation](https://learn.microsoft.com/en-us/azure/backup/azure-file-share-backup-overview?tabs=snapshot).

For configuration and backup steps, refer to the official AKS documentation, as follows:

* [Back up Azure Files using the Azure portal](https://learn.microsoft.com/en-us/azure/backup/backup-azure-files?tabs=recovery-services-vault)
* [Back up Azure Files using Azure CLI](https://learn.microsoft.com/en-us/azure/backup/backup-afs-cli)
* [Back up Azure Files using PowerShell](https://learn.microsoft.com/en-us/azure/backup/backup-azure-afs-automation?tabs=snapshot)

To restore backups, refer to the official AKS documentation, as follows:

* [Restore Azure Files using the Azure portal](https://learn.microsoft.com/en-us/azure/backup/restore-afs?tabs=full-share-recovery)
* [Restore Azure Files using Azure CLI](https://learn.microsoft.com/en-us/azure/backup/restore-afs-cli)
* [Restore Azure Files using PowerShell](https://learn.microsoft.com/en-us/azure/backup/restore-afs-powershell)