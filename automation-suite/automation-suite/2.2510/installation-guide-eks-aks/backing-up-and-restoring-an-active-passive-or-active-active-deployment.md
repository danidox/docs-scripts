---
title: "Guidelines on backing up and restoring an Active/Passive  deployment"
visible: true
slug: "backing-up-and-restoring-an-active-passive-or-active-active-deployment"
---

:::note
For detailed instructions on how to back up and restore Automation Suite, see [Backing up and restoring the cluster.](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/backing-up-and-restoring-the-cluster#backing-up-and-restoring-the-cluster)
:::

## Backing up the cluster

* You must back up only the primary cluster and external storage (SQL and Objectstore).
* It is not mandatory to take a backup of the secondary cluster. Instead, you can choose to take a backup of the secondary. However, you can still use the primary cluster to set up the secondary cluster.

## Restoring the primary cluster

* If the primary cluster goes down, you must use the backup to restore it.
* If configuration changes were made on the secondary cluster while the primary cluster was down, follow these steps to ensure the restored primary reflects the latest configuration:
  + Merge configurations from the primary and secondary clusters to create an updated `input.json` that includes all changes made on the secondary after the primary went down.
  + Apply any required updates to parameters that are specific to the primary cluster.
  + Restore the primary cluster using the merged `input.json` file.

## Restoring the secondary cluster

* If the secondary cluster’s backup is unavailable, you can restore it from the primary cluster by taking the following steps:
  1. Generate the `input.json` from the primary cluster.
  2. Update the `input.json` with the specific value of the secondary cluster.
  3. Install the secondary cluster.
* If the backup for the secondary cluster is available, you can restore the secondary cluster from the backup.