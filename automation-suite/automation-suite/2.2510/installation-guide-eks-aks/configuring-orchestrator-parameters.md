---
title: "Configuring Orchestrator parameters"
visible: true
slug: "configuring-orchestrator-parameters"
---

## Manifest configuration

Follow these steps to edit the Orchestrator manifest configuration:

1. Edit the `input.json` file

For details, see [Configuring input.json](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#configuring-inputjson).
2. Add or edit the desired settings in the `orchestrator` section.
3. Run this command:
   ```
   uipathctl manifest apply input.json --versions versions.json --kubeconfig kubeconfig.yaml --only orchestrator
   ```

## Custom Orchestrator configuration

You can use this command to edit the Orchestrator custom configuration for both `appSettings` and `NLog`:

```
uipathctl config orchestrator
```

### Custom Orchestrator scenarios

You can modify various Orchestrator parameters using `uipathctl`. This enables the following configuration scenarios:

* [Overriding cluster-level storage configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/overriding-cluster-level-storage-configuration#overriding-cluster-level-storage-configuration)
* [Saving robot logs to Elasticsearch](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/saving-robot-logs-to-elasticsearch#saving-robot-logs-to-elasticsearch)
* [Configuring encryption key per tenant](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-encryption-key-per-tenant#configuring-encryption-key-per-tenant)
* [Configuring NLog](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-nlog#configuring-nlog)
* [Configuring credential stores](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-credential-stores#configuring-credential-stores)