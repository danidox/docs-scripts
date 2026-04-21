---
title: "Switching to the secondary cluster manually in an Active/Passive setup"
visible: true
slug: "switching-to-the-secondary-cluster"
---

This section provides high-level instructions on how to manually switch the traffic to the secondary cluster in an Active/Passive setup.

To switch to the secondary Automation Suite cluster, take the following steps:

1. Turn on all the nodes of the Automation Suite cluster.
2. Bring back all products.
   1. Run `manifest apply` with all products enabled.
   2. If maintenance mode is enabled, disable it using `uipathctl maintenance disable`.
3. Wait for all the components and products to be healthy.
4. Sync the AI Center skills on the secondary cluster.
5. Restore the PVC data for Studio Web and Insights on the secondary cluster.
   1. For details, refer to [EKS backup and restore](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/eks-backup-and-restore#eks-backup-and-restore) or [AKS backup and restore](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/aks-backup-and-restore#aks-backup-and-restore).
   2. If you use Velero File System Backup (FSB), you must:
      * Before running the restore, uninstall Studio Web and Insights on the secondary cluster. For details, refer to [Managing products](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-products#managing-products).
      * After the restore completes, reinstall Studio Web and Insights.
      :::note
      This step is required because Velero must re-create the PVCs during restore, and existing PVCs would interfere with that operation. For more details, refer to:
      * [Velero Issue #8483](https://github.com/vmware-tanzu/velero/issues/8483)
      * [Velero Issue #7345](https://github.com/vmware-tanzu/velero/issues/7345)
      :::
6. Switch the traffic to the secondary cluster (update DNS/LB as per your topology)

## Bringing back the products

You can scale up the cluster and bring back all inactive products using the following command:

```
uipathctl config products scale-up
```

To scale down the cluster and switch off inactive products, refer to [Switching off inactive products](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-the-secondary-cluster#switching-off-inactive-products).

## Syncing the AI Center ML Skill

You can use the following script to re-sync the AI Center ML Skilll in the secondary cluster. The script triggers the re-sync in the background if no active sync is in progress. You can use the same script to switch back to the primary cluster.

The script syncs the skills in the background (async) and returns. The job ensures that the skills are deployed and updates the DB entry to reflect the current status.

```
uipathctl service aicenter sync-skills [skill_ids]
```

| Parameter | Description |
| --- | --- |
| `[skill_ids]` | The optional array of the skill IDs separated by space. If you provide the skill ID, then only those skills are updated; otherwise, all deployed skills are re-synced. |

Example:

```
uipathctl service aicenter sync-skills 783273-3232-3232-323 32-32-323-3232

//this will only sync the skills with ID 783273-3232-3232-323 and 32-32-323-3232
```

To monitor the skill status, you must run a different script, as shown in the following section.

## Checking the status of the AI Center ML Skill

To view the status of the AI Center ML Skill, run the following command:

```
uipathctl service aicenter sync-skill-status [skill_ids]
```

The command can return any of the following statuses:

* `InProgess` - skill deployment is in progress.
* `Failed` - skill deployment is failed.
* `OutOfSync` - skill is available in the database; however, it has yet to be deployed.
* `Available` - when the skills are deployed and available to consume.