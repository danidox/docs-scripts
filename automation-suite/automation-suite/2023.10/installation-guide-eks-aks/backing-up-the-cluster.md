---
title: "Backing up the cluster"
visible: true
slug: "backing-up-the-cluster"
---

## Prerequisites

:::note
There is a known issue with the backup logic in Automation Suite for AKS/EKS versions 2023.10.0 to 2023.10.7. Specifically, this issue excludes the backup of Insights dashboards. However, all historical data is successfully backed up. To include the Insights dashboards in backup, you must reconfigure the backup solution using the script available [here](https://raw.githubusercontent.com/UiPath/automation-suite-support-tools/refs/heads/main/Scripts/GeneralTools/veleroBackupASEA/dr.sh). This script allows you to reconfigure the backup solution and create the backup. For details on how to execute the command, see this [section](https://github.com/UiPath/automation-suite-support-tools/tree/main/Scripts/GeneralTools/veleroBackupASEA).
:::

Before taking a backup, you must provide the objectstore configuration to store the backup. For this, see [Configuring the backup store](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-backup-store#configuring-the-backup-store).

## Enabling the schedule snapshot backup

When configuring the schedule snapshot backup, it is recommended to provide the schedule and retention of the backup via the `--schedule` and `--retention` flags. By default, Automation Suite takes a backup every 45 minutes after starting and retains the last seven days of snapshots.

To enable the backup at the scheduled time, run the following command:

```
./uipathctl snapshot backup enable --schedule "*/45 * * * *" --retention 168h --prefix "mysnapshot"
```

Running the snapshot backup command ensure that backups are taken in scheduled time intervals.

| **Flag** | **Description** |
| --- | --- |
| `schedule` | UNIX cron expression for schedule. This is only required if you want to enable a schedule backup.  Default value is `"*/45 * * * *"`, which means a backup is taken every 45 minutes. |
| `retention` | Retention policy in the following duration format: `Hh:Mm:Ss`. For example, `8h5m1s`. |
| `prefix` | This will prefix the snapshot backups' names with the given string. This is only used if you want to enable a scheduled backup.  The default value is a `snapshot.`  The provided string must be in lowercase. |

:::important
**Note 1:** Any cron expression provided as part of the `--schedule` parameter matches the time of the cluster node. We recommend syncing the cron expression with the scheduled backup of your external data stores (such as SQL database and objectstore). **Note 2:** Automation Suite stores only the snapshot backed up during the defined retention policy. If your retention policy has a shorter duration, you may lose essential snapshots once the retention policy applies. Similarly, if the retention policy is longer, more snapshots are stored, which may take up space on your objectstore. **Note 3:** Carefully consider the schedule setup. Taking snapshots at small intervals (for example, every 30 minutes) implies frequent backup operations, forcing you to store the last 30 minutes' data. Similarly, taking snapshots once a week can cause data loss if a disaster occurs much later than the previous backup. Therefore, we strongly recommend synchronizing the backup schedule and the retention duration with your Recovery Point Objective (RPO) requirements.
:::

## Disabling the schedule snapshot backup

To disable the scheduled backup, run the following command:

```
./uipathctl snapshot backup disable --prefix <prefix_name>
```

:::note
You must provide the prefix you used while enabling the backup via the `--prefix` parameter; however, if you did not configure any prefix while allowing the backup, provide a `snapshot` as a prefix value.
:::

## On-demand snapshot backup

To take an on-demand snapshot backup, run the following command:

```
./uipathctl snapshot backup create <snapshot_name>
```

The aforementioned command takes an optional flag:

| **Flag** | **Description** |
| --- | --- |
| `--wait` | Wait until the backup completes |

If you do not provide the `--wait` command, the command executes in the background. To view the status of your backup, check the snapshot list as described in the following section.

## Listing the existing snapshots

To list all the present snapshots, their status, and the time at which they were taken, run the following command:

```
./uipathctl snapshot list
```

Sample output:

```
NAME            STATUS           CREATION                       EXPIRATION
manualbackup1   Completed        2022-09-13 09:19:50 +0000 UTC  2023-09-13 09:19:50 +0000 UTC
manualbackup2   PartiallyFailed  2022-09-13 09:19:50 +0000 UTC  2023-09-13 09:19:50 +0000 UTC
```

## Deleting a backup

:::note
Deleting a backup consists of deleting the cluster metadata and the volume data from the backup storage server. This operation is irreversible.
:::

To delete the snapshot backups from the backup store, run the following command:

```
./uipathctl snapshot delete <snapshot_name>
```

You can retrieve the name of the snapshot that you want to delete by running the snapshot list command.

The command takes the following additional parameters:

| **Flag** | **Description** |
| --- | --- |
| `-a|--all` | Delete all snapshots. If selecting this option, then you do not need to provide the name of the snapshot. |
| `-f|--force` | Forcibly delete the snapshot without confirmation. |