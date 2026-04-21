---
title: "Other troubleshooting"
visible: true
slug: "general-troubleshooting"
---

If you encounter general issues while configuring or using Automation Suite, refer to the following:

* [The backup setup does not work due to a failure to connect to Azure Government](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/the-backup-setup-does-not-work-due-to-a-failure-to-connect-to-azure-government#the-backup-setup-does-not-work-due-to-a-failure-to-connect-to-azure-government)
* [Pods in the uipath namespace stuck when enabling custom node taints](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/pods-in-the-uipath-namespace-not-running-when-enabling-custom-node-taints#pods-in-the-uipath-namespace-stuck-when-enabling-custom-node-taints)
* [Unable to launch Automation Hub and Apps with proxy setup](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/unable-to-launch-automation-hub-and-apps-with-proxy-setup#unable-to-launch-automation-hub-and-apps-with-proxy-setup)
* [Pods cannot communicate with FQDN in a proxy environment](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/pods-cannot-communicate-with-fqdn-via-proxy#pods-cannot-communicate-with-fqdn-in-a-proxy-environment)
* [Test Automation SQL connection string is ignored](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/test-automation-sql-connection-string-is-ignored#test-automation-sql-connection-string-is-ignored)
* [EKS backup failure due to Velero version](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/eks-backup-failure-due-to-velero-version#eks-backup-failure-due-to-velero-version)
* [Velero backup fails with FailedValidation error](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/general-troubleshooting#velero-backup-fails-with-failedvalidation-error)
* [Accessing FQDN returns RBAC: access denied error](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/general-troubleshooting#accessing-fqdn-returns-rbac%3A-access-denied-error)

## Velero backup fails with FailedValidation error

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

## Accessing FQDN returns RBAC: access denied error

### Description

Accessing an FQDN may return the following error:

```
RBAC: access denied
```

This issue occurs because the FQDN and its relevant URL access are routed via Istio. Istio relies on a WASM plugin to route the request to the appropriate destination pod.

If the WASM plugin image is missing in the registry, internal or external, Istio blocks the URL access and returns a `RBAC: access denied` error.

### Solution

To address this issue, you must ensure that the registry is hydrated and the WASM plugin image exists in registry.

To check the WASM plugin image, run teh folowing command:

```
kubectl get wasmplugin -A -o yaml | grep url
```

The output will be similar to the one from the following example:

```
url: oci://testing.azurecr.io/istio-wasm-plugin:2024.10.3
```

In the example above, the WASM plugin image is `istio-wasm-plugin:2024.10.3`. You must check if this image is present in your registry or not.