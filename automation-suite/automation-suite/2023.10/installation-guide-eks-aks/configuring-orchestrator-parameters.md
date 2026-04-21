---
title: "Configuring Orchestrator parameters"
visible: true
slug: "configuring-orchestrator-parameters"
---

You can modify various Orchestrator parameters using `uipathctl`. This enables the following configuration scenarios:

* [Overriding cluster-level storage configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/overriding-cluster-level-storage-configuration#overriding-cluster-level-storage-configuration)
* [Saving robot logs to Elasticsearch](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/saving-robot-logs-to-elasticsearch#saving-robot-logs-to-elasticsearch)
* [Configuring encryption key per tenant](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-encryption-key-per-tenant#configuring-encryption-key-per-tenant)

To do that, edit the `input.json` file, add or edit the settings under the `orchestrator` section, then run the following command:

```
./uipathctl manifest apply input.json --versions versions.json --kubeconfig kubeconfig.yaml --only orchestrator
```

For details on `input.json`, see [Configuring input.json](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#configuring-inputjson).

For details, on the Orchestrator-specific configuration, see [Orchestrator configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#orchestrator-specific-configuration).