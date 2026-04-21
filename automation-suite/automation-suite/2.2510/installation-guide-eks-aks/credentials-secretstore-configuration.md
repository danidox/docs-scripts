---
title: "Credentials secretstore configuration"
visible: true
slug: "credentials-secretstore-configuration"
---

A secretstore in Automation Suite is an external source used to store sensitive credentials. It can be either a Kubernetes Secret or an Azure Key Vault.

To use a secretstore for credentials in Automation Suite, refer to [Using a secretstore for credentials](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/credentials-secretstore-configuration#using-a-secretstore-for-credentials).

If you are using Azure Key Vault as your external secret management system and plan to use your own External Secrets Operator, refer to [Installing the External Secrets Operator in Kubernetes](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-the-external-secrets-operator-in-kubernetes#installing-the-external-secrets-operator-in-kubernetes).

In this case, make sure to add `external-secrets` to the excluded components list, as follows:

```
"exclude_components": [
        ...
        "external-secrets"   
  ]
```

## Using a secretstore for credentials

When deploying Automation Suite, the `input.json` file typically contains several sensitive data fields and credentials in plain text. To improve security, you can store these credentials in a secret store instead of including them directly in the `input.json` file.

A secretstore acts as an external system that securely holds sensitive credentials and configuration data. When configured, Automation Suite retrieves credentials from the defined secret store during deployment.

To enable secretstore usage, add the following section to the `input.json` file:

```
"secret_store": {
    "enabled": true
}
```

When this configuration is enabled, Automation Suite reads credentials from the secretstore instead of directly from the `input.json` file.

Automation Suite supports the following secretstore types:

* [Kubernetes Secret](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-a-kubernetes-secret-as-a-secretstore#configuring-a-kubernetes-secret-as-a-secretstore)
* [Azure Key Vault](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-azure-key-vault-as-a-secretstore#configuring-azure-key-vault-as-a-secretstore)

If any credential stored in the secretstore changes, you must perform the credential update procedure. For details, refer to [Updating credentials](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/updating-credentials#updating-credentials).