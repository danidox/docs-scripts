---
title: "Recommendations"
visible: true
slug: "recommendations"
---

Use the following guidance to define how often to create backups and how long to retain them:

* Production environments: Configure backups every 4 hours to reduce the risk of data loss for business-critical services.
* Non-production environments: Configure backups daily to mirror production practices with reduced frequency.
* Retention: UiPath recommends keeping backups for 7 days (168 hours). Adjust this period to meet your recovery point objective (RPO) and recovery time objective (RTO).

For more information and tools to help you plan your backup strategy, refer to:

* For AKS:
  + [Troubleshoot AKS Backup](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-backup-troubleshoot)
  + [Azure Backup pricing calculator](https://azure.microsoft.com/pricing/details/backup/)
  + [AKS best practices](https://learn.microsoft.com/en-us/azure/aks/best-practices)
* For EKS:
  + [AWS Knowledge Center: EKS cluster backup and restore](https://repost.aws/knowledge-center/eks-cluster-back-up-restore)
  + [Velero File System Backup](https://velero.io/docs/v1.17/file-system-backup)
  + [Velero resource filtering](https://velero.io/docs/v1.17/resource-filtering/)