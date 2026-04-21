---
title: "Provisioning Automation Suite Robots fails"
visible: true
slug: "provisioning-automation-suite-robots-fails"
---

## Description

The failure occurs mainly on FIPS enabled nodes when using Azure Files with the NFS protocol.

During the Automation Suite on AKS installation, creating the PVC for Automation Suite Robots `asrobots-pvc-package-cache` fails.

## Potential issue

This happens because the AKS cluster cannot connect to Azure Files.

For example, the following error message may be displayed:

```
failed to provision volume with StorageClass "azurefile-csi-nfs": rpc error: code = Internal desc = update service endpoints failed with error: failed to get the subnet ci-asaks4421698 under vnet ci-asaks4421698: &{false 403 0001-01-01 00:00:00 +0000 UTC {"error":{"code":"AuthorizationFailed","message":"The client '4c200854-2a79-4893-9432-3111795beea0' with object id '4c200854-2a79-4893-9432-3111795beea0' does not have authorization to perform action 'Microsoft.Network/virtualNetworks/subnets/read' over scope '/subscriptions/64fdac10-935b-40e6-bf28-f7dc093f7f76/resourceGroups/ci-asaks4421698/providers/Microsoft.Network/virtualNetworks/ci-asaks4421698/subnets/ci-asaks4421698' or the scope is invalid. If access was recently granted, please refresh your credentials."}}}
```

## Solution

To overcome this issue, you need to grant Automation Suite access to the Azure resource

1. In Azure, navigate to the AKS resource group, then open the desired virtual network page. For example, in this case, the virtual network is `ci-asaks4421698`.
2. From the **Subnets** list, select the desired subnet. For example, in this case, the subnet is `ci-asaks4421698`.
3. At the top of the subnets list, select **Manage Users**. The **Access Control** page opens.
4. Select **Add role assignment**.
5. Search for the **Network Contributor** role.
6. Select **Managed Identity**.
7. Switch to the**Members** tab.
8. Select **Managed Identity**, then select **Kubernetes Service**.
9. Select the name of the AKS cluster.
10. Select **Review and Assign**.