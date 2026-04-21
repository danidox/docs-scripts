---
title: "The backup setup does not work due to a failure to connect to Azure Government"
visible: true
slug: "the-backup-setup-does-not-work-due-to-a-failure-to-connect-to-azure-government"
---

## Description

Following an Automation Suite on AKS installation or upgrade, the backup setup does not work because of a failure to connect to Azure Government.

## Solution

You can fix the issue by taking the following steps:

1. Create a file named `velerosecrets.txt`, with the following contents:
   ```
   AZURE_CLIENT_SECRET=<secretforserviceprincipal>
   AZURE_CLIENT_ID=<clientidforserviceprincipal>
   AZURE_TENANT_ID=<tenantidforserviceprincipal> 
   AZURE_SUBSCRIPTION_ID=<subscriptionidforserviceprincipal>
   AZURE_CLOUD_NAME=AzureUSGovernmentCloud
   AZURE_RESOURCE_GROUP=<infraresourcegroupoftheakscluster>
   ```
2. Encode the data in the `velerosecrets.txt` file as Base64:
   ```
   export b64velerodata=$(cat velerosecrets.txt | base64)
   ```
3. Update the `velero-azure` secret in the `velero` namespace, as shown in the following example:
   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: velero-azure
     namespace: velero
   data:
     cloud: <insert the $b64velerodata value here>
   ```
4. Restart the `velero` deployment:
   ```
   kubectl rollout restart deploy -n velero
   ```