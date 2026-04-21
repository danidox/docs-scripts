---
title: "Azure Marketplace deployment"
visible: true
slug: "unattended-azure-marketplace-deployment"
---

Azure Marketplace deployments allow you to deploy UiPath solutions directly from the [Azure portal](https://portal.azure.com/).

Deploying through Azure Marketplace creates a modern folder in Orchestrator. This folder comes with assigned user accounts and machine templates. The solution structure has the following naming:

* Folder: `AzureDeployed`
* User account (one for each deployed robot): `Azure-<VM Name>-<RandomString>`
* Robot account (for each user): `<VM Name>\<Machine Admin Username>`
* Machine template (one for each deployed robot): `AzureTemplate-<VMName>`

The Azure Portal wizard allows you to deploy one or more Robots. It uses a Windows Virtual Machine, which runs scripts to configure the Robot and connect it to Orchestrator. The machine, together with a Network Interface Card and a separate storage account, is deployed within a virtual network.

To deploy robots using the Azure Portal wizard:

1. On the **Basics** panel:
   ![docs image](/images/robot/robot-docs-image-446916.webp)

   1. Select the **Subscription**, the **Resource Group**, and the **Region** where you want your solution to be deployed.
   2. Provide a **Virtual Machine name**.
   3. Set the **Username** for the administrator of the virtual machine (VM).
   4. Provide the **Password** to access the VM.
   5. Specify the **Number of virtual machines with robots to be created**.
2. On the **Orchestrator Connection Info** panel:
   ![docs image](/images/robot/robot-docs-image-446921.webp)

   1. Provide the **Orchestrator URL** of an existing and licensed instance.
   2. Provide the username of the **Orchestrator admin account** that has API usage permissions.
   3. Provide the **Password** for the Orchestrator admin account.
   4. Provide the **Orchestrator Tenant Name** where the robot should connect.
   5. Select the **Robot type.**
   6. Select the **Robot version**.
3. On the **Virtual Machine Settings** panel:
   ![docs image](/images/robot/robot-docs-image-446928.webp)

   1. Set the **Virtual machine size**.
   2. Select the **Public IP Address for the VM**.
   3. Provide the **DNS Prefix for the public IP Address.**
   4. Select the **Virtual network**.
   5. Select the **Subnet** for the VM.
4. On the **Resource Tags Configuration** panel, create tags for the resources created in the deployment.