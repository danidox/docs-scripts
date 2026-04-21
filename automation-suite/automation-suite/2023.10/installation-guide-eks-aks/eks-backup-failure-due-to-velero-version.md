---
title: "EKS backup failure due to Velero version"
visible: true
slug: "eks-backup-failure-due-to-velero-version"
---

## Description

The Automation Suite on EKS backup fails due to a Velero version-related issue.

## Solution

To address the issue, you must manually modify the Velero deployment:

1. Download the Velero chart from the registry and move it into the appropriate directory, by using the following command:
   ```
   helm pull oci://<registry_url>/vendor/velero --version 6.2.0 -d . --untar
   ```
2. Manually override the `credentials.useSecret` field in the Velero configuration, by using the following command:
   ```
   helm upgrade velero ./velero -n velero --set credentials.useSecret=false  --reuse-values
   ```