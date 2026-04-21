---
title: "Configuring credential stores"
visible: true
slug: "configuring-credential-stores"
---

The following secure stores are already available in Orchestrator:

* Azure Key Vault
* CyberArk CCP
* HashiCorp Vault
* Thycotic Secret Server
* Beyond Trust
* AWS Secrets Manager

Any credential store plugin you choose to use must be Linux-compatible.

To disable the default plugins, set the `Plugins.SecureStores.Default` key as an empty string in the `appsettings.json` file. See [Configuring appSettings](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-appsettings#configuring-appsettings) for details.