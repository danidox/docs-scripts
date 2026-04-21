---
title: "Installation fails when Velero is enabled"
visible: true
slug: "installation-fails-when-velero-is-enabled"
---

## Description

The Automation Suite installation might fail when Velero is enabled.

## Solution

To fix the issue, take the following steps:

1. Make sure Helm 3.14 runs on the jumpbox or laptop used for installing Automation Suite.
2. Extract the configuration values of the failed Helm chart, which in this case is Velero:
   ```
   helm -n velero get values velero > customvals.yaml
   ```
3. Add the missing image pull secret in the `customvals.yaml` file, under the `.image.imagePullSecrets` path:
   ```
   image:
     imagePullSecrets:
     - uipathpullsecret
   ```
4. If Velero has already been installed, uninstall it:
   ```
   helm uninstall -n velero velero
   ```
5. Create a new file called `velerosecrets.txt`. Populate it with your specific information, as shown in the following example:
   ```
   AZURE_CLIENT_SECRET=<secretforserviceprincipal>
   AZURE_CLIENT_ID=<clientidforserviceprincipal>
   AZURE_TENANT_ID=<tenantidforserviceprincipal> 
   AZURE_SUBSCRIPTION_ID=<subscriptionidforserviceprincipal>
   AZURE_CLOUD_NAME=AzurePublicCloud
   AZURE_RESOURCE_GROUP=<infraresourcegroupoftheakscluster>
   ```
6. Encode the `velerosecrets.txt` file:
   ```
   export b64velerodata=$(cat velerosecrets.txt | base64)
   ```
7. Create the `velero-azure` secret in the `velero` namespace. Include the following content:
   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: velero-azure
     namespace: velero
   data:
     cloud: <put the $b64velerodata value here>
   ```
8. Reinstall Velero:
   ```
   helm install velero -n velero <path to velero - 3.1.6 helm chart tgz> -f customvals.yaml
   ```