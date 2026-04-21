---
title: "Configuring the maximum request size"
visible: true
slug: "configuring-maximum-request-size"
---

You can configure the maximum request size in the `orchestrator-customconfig` config map using a tool such as `kubectl`.

For more information on how to edit the Orchestrator custom configuration, check the [Custom Orchestrator configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-orchestrator-parameters#custom-orchestrator-configuration) section from the **Configuring Orchestrator parameters** page.

The default value for the maximum request size is 300 MB, but you can edit it in the `values.json` file. The Orchestrator deployment should restart automatically after this configuration change.

```
{
  "Kestrel": {
    "Limits": {
      "MaxRequestBodySize": 314572800
    }
  }
}
```

The `values.json` file in the `orchestrator-customconfig` config map may also contain other values, such as `AppSettings`. You must not remove any other settings when configuring the maximum request size.

```
{
  "Kestrel": {
    ...
  },
  "AppSettings": {
    ...
  }
}
```