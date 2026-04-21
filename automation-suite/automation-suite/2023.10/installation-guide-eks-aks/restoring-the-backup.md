---
title: "Restoring the backup"
visible: true
slug: "restoring-the-backup"
---

:::note
Once a cluster is restored, the snapshot backup is not enabled. To enable it after restoration, refer to the [Enabling the backup snapshot](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/backing-up-the-cluster#enabling-the-schedule-snapshot-backup). Restoring the cluster does not restore external data sources such as SQL Server. Make sure to restore the SQL server to the relevant snapshot.
:::

To restore the cluster, take the following steps:

## Step 1: Provisioning the Kubernetes cluster

Before restoring, make sure to configure the Kubernetes cluster where you want to restore.

For details, see [Prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/backing-up-and-restoring-the-cluster#prerequisites).

## Step 2: Restoring the SQL Server and objectstore

Since SQL Server and Objectstore are external components, make sure that you restored them before restoring the Automation Suite cluster.

:::important
Changing the FQDN during the restore operation is not allowed. Make sure you preserve the FQDN for the Automation Suite cluster, the SQL server, Objectstore, Redis and Filestore.
:::

## Step 3: Providing the snapshot configuration

Provide the snapshot configuration, such as objectstore, where the backup data is stored. This configuration is similar to the one you provided during the backup configuration. For details, see [Configuring the backup store](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-backup-store#configuring-the-backup-store).

## Step 4: Selecting the snapshot to restore

To identify the backup you want to restore, see [Listing the existing snapshots](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/backing-up-the-cluster#listing-the-existing-snapshots).

Selecting the snapshot relevant to the SQL Server and Objectstore data is important. Incompatibilities may occur if there is a vast difference between the moment you take the snapshot of the Automation Suite cluster and when you take the snapshot of the external storage components.

## Step 5: Running the restore script

Make sure that Velero is installed on the newly deployed EKS cluster so that you can restore the snapshot. To install Velero on the new cluster, run the following command:

```
./uipathctl  manifest apply input.json --only velero --versions versions.json
```

To restore the selected snapshot, run the following command:

```
./uipathctl snapshot restore create <restore_name> --from-snapshot <snapshot_name>
```

The restore command requires the restore name, which you can use to get the status of the restore and debug in case of any failure.

This operation takes some time to finish and runs in the back ground. You can use the `history` command to view the status, as described in next section.

**Known issue:** In certain scenarios, the restore operation may become stuck. If the restore operation gets stuck, you should manually remove the `restore` object and subsequently retry the restore operation.

## Debugging the restore

To debug the restore operation, you can use the `history` and `log` commands.

History:

```
./uipathctl snapshot restore history

# Output Example

NAME                        STATUS      CREATED EXPIRATION 
prefix-scheduled-xx1        Completed   xx1     xx1 
prefix-scheduled-xx2        Failed      xx2     xx2
test-snapshot-xx3           Failed      xx3     xx3
```

Logs:

```
./uipathctl snapshot restore logs restore_1
```