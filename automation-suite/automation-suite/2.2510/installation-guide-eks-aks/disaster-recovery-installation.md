---
title: "Disaster recovery: Active/Passive  configurations"
visible: true
slug: "disaster-recovery-installation"
---

:::important
Active/Passive mode is currently available only for EKS.
:::

:::note
Some Automation Suite products are not supported in Disaster Recovery - Active/Passive . You can install these products while installing the primary cluster only. For details, see [Disaster recovery - Active/Passive](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery#disaster-recovery---active%2Fpassive "This article walks you through the core concepts and architecture of Automation Suite disaster recovery, covering Active/Passive deployments.").
:::
The disaster recovery configuration requires that you install the two Automation Suite clusters separately. To install both the primary and secondary clusters in an Active/Passive deployment, you must configure the following `input.json` parameters:

* For Active/Passive deployments: configure the parameters listed in the following table.

| Parameter | Description |
| --- | --- |
| `fqdn` | It represents the FQDN that, at the time of installation, points to the load balancer of the primary cluster.  For details, refer to [DNS routing logic](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/overview-active-passive-active-active-deployments#load-balancer-and-dns-configuration). |
| `cluster_fqdn` | It represents the cluster-specific FQDN (DNS) that points to the load balancer of the cluster you set up using the `input.json` file.  For details, refer to [DNS routing logic](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/overview-active-passive-active-active-deployments#load-balancer-and-dns-configuration). |
| `multisite.enabled` | It indicates that Automation Suite must be configured to work multi-site. It must be set to `true`. |
| `multisite.primary` | It indicates that this cluster is a primary cluster and must be set to `true`. It defaults to `false` to denote the secondary cluster. |
| `multisite.other_kube_config` | It indicates the base64-encoded kubeconfig file of another cluster. While installing the primary Automation Suite cluster, this value is unavailable and can be left as is. However, you must provide the value when rebuilding the primary automation suite later during recovery. |

## Multi-site configuration

This page describes how to set up a multi-site configuration with a primary and secondary cluster. The primary cluster is active and the secondary cluster is passive.

1. In the configuration for the primary cluster option, the `enabled` option must be set to true.
   ```
     "multisite": {
       "enabled": true,
       "primary": true
     }
   ```
2. In the configuration for the secondary cluster, the `primary` option must be set to false:
   ```
     "multisite": {
       "enabled": true,
       "primary": false,
       "other_kube_config": "[base64 encoded kubeconfig]"
     }
   ```

You must supply the primary kubeconfig in base64 encoded string.
3. Services that are not compatible with being in a passive state must be disabled. For more details on services that do not support Active/Passive mode, refer to the [Disaster recovery
   - Active/Passive](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery#disaster-recovery---active%2Fpassive "This article walks you through the core concepts and architecture of Automation Suite disaster recovery, covering Active/Passive deployments.") page.
4. Ensure the certificates are consistent across the primary and secondary cluster, as this is not automatically checked or enforced.