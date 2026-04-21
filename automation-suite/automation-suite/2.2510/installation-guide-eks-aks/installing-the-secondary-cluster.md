---
title: "Disaster recovery - Installing the secondary cluster"
visible: true
slug: "installing-the-secondary-cluster"
---

:::important
Active/Passive mode is currently available only for EKS.
:::

To install the secondary Automation Suite cluster in an Active/Passive deployment, take the following steps.

1. Generate or copy the `input.json` file from the primary Automation Suite cluster. For more details, see [Generating or copying the configuration file of the primary cluster](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-the-secondary-cluster#generating-or-copying-the-configuration-file-of-the-primary-cluster).
2. Update the `input.json` file with the parameters specific to the secondary Automation Suite cluster.
3. Resume the Automation Suite installation.
4. Switch off inactive products if you use an Active/Passive configuration.

## Generating or copying the configuration file of the primary cluster

Generate a new `input.json` file or copy it from the primary cluster.

```
uipathctl manifest get-revision >> /path/to/new/input.json
```

## Updating the configuration file

Update the `input.json` file with the parameters specific to the secondary Automation Suite cluster by taking the following steps:

1. Turn off the unsupported products.

Set all the products that are not supported in multi-site to `false`.

   * For an Active/Passive configuration, disable the products that do not support Active/Passive. For details on Active/Passive support at product level, refer to the table in [Disaster recovery - Active/Passive](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery#disaster-recovery---active%2Fpassive "This article walks you through the core concepts and architecture of Automation Suite disaster recovery, covering Active/Passive deployments."). The following example shows how to disable products:
     ```
     {
       "autopiloteveryone": {
         "enabled": false
       },
       "automationsolutions": {
         "enabled": false
       } 
     }
     ```:::note
Make sure that you enable the `platform` service as shown in the following example: assignment
   ```
   "platform": {
   "enabled": true
   },
   ```
   :::
2. Update the `input.json` file with the parameters specific to the secondary cluster. You must provide the kubeconfig of the primary cluster, as it is required for the secondary cluster to access the configurations made on the primary cluster.
   ```
   "fqdn" : "<global traffic manager fqdn>"
   "cluster_fqdn": "<fqdn of the secondary cluster>",

   "multisite": {
       "enabled": true,
       "primary": false,
       "other_kube_config": "[base64 encoded kubeconfig]"
    }
   ```

For details, see [Advanced installation experience](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery-installation#disaster-recovery%3A-active%2Fpassive-configurations).

## Resume the installation

Once the parameters in the previous step are provided or modified in the `input.json`, you can resume the installation. For details, refer to [Installing Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-automation-suite#installing-automation-suite).

:::note
You must perform the Automation Suite installation using the `uipathctl` installer. Note that you do not need to generate a new `input.json`.
:::

## Switching off inactive products

If you deployed Automation Suite in Active/Passive mode, you can scale down the cluster and switch off inactive products using the following command.

```
uipathctl config products scale-down
```

To scale up the cluster and bring back inactive products, refer to [Bringing back the products](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/switching-to-the-secondary-cluster#bringing-back-the-products).