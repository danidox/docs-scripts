---
title: "Converting an existing installation to multi-site setup"
visible: true
slug: "converting-an-existing-installation-to-multi-site-setup"
---

You can convert an existing installation into multi-site by taking the following steps:

1. Convert the standalone Automation Suite cluster into the primary cluster. For details, see [Converting a standalone cluster into a primary cluster.](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/converting-an-existing-installation-to-multi-site-setup#converting-a-standalone-cluster-into-a-primary-cluster)
2. Install secondary Automation Suite cluster. For details, see [Disaster Recovery - Installing the secondary cluster](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-the-secondary-cluster#disaster-recovery---installing-the-secondary-cluster).
   :::note
   Ensure that the certificates are the same on the primary and secondary clusters. This check is not performed or enforced automatically.
   :::

## Converting a standalone cluster into a primary cluster

To convert an existing Automation Suite cluster into a primary cluster of the multi-site deployment, take the following steps:

1. Update `input.json`. Add or update `fqdn`, `cluster_fqdn`, and enable `multisite`.
   ```
   "fqdn" : "<global traffic manager fqdn>"
   "cluster_fqdn": "<fqdn of the primary cluster>",

   "multisite": {
       "enabled": true,
       "primary": true
    }
   ```

For details, see the following documentation: [Advanced installation experience.](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery-installation#disaster-recovery%3A-active%2Fpassive-configurations) Update the TLS certificate [section](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#certificate-configuration) to configure the new certificate, ensuring it meets the requirements outlined in the section.
   :::note
   It is recommended to keep the FQDN of your existing Automation Suite setup to avoid reconfiguring all your robots.
   :::
2. Reapply the manifest by running the following command:
   ```
   uipathctl manifest apply input.json --versions versions.json
   ```

Refer to [Installing Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-automation-suite#installing-automation-suite).