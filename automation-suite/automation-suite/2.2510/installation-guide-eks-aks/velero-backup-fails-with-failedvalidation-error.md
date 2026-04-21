---
title: "Velero backup fails with FailedValidation error"
visible: true
slug: "velero-backup-fails-with-failedvalidation-error"
---

When attempting to run a scheduled backup in Automation Suite on EKS/AKS, Velero may return the following error:

```
Phase: FailedValidation
Validation errors: an existing backup storage location was not specified at backup creation time and the server default default does not exist.
Error: BackupStorageLocation.velero.io "default" not found
```

This occurs due to the `default-bs1` `BackupStorageLocation` not being marked as default in the Velero configuration.

To address the issue, take the following steps:

1. Verify the backup storage locations configured for Velero:
   ```
   kubectl get backupstoragelocations -n velero
   ```

Confirm whether the **DEFAULT** column is empty.
2. Edit the backup storage location to set the default value:
   ```
   kubectl edit backupstoragelocation default-bs1 -n velero
   ```
3. Under the `spec` section, add the following line:
   ```
   default: true
   ```
4. Save the changes.
5. Restart the Velero pods to apply the configuration:
   ```
   kubectl delete pod -n velero --all
   ```

Alternatively, perform a rolling restart:

   ```
   kubectl -n velero rollout restart deploy/velero
   ```
6. Verify the fix:
   ```
   kubectl get backupstoragelocations -n velero
   ```

Confirm that the `PHASE` is **Available** and the **DEFAULT** column shows `Yes`.