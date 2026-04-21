---
title: "Configuring encryption key per tenant"
visible: true
slug: "configuring-encryption-key-per-tenant"
---

To configure the encryption key per tenant, take the following steps:

1. Update the Orchestrator parameters. In the configuration file, under `orchestrator`, add the `encryption_key_per_tenant` section. For more details, see [Configuring Orchestrator parameters](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-orchestrator-parameters#configuring-orchestrator-parameters).
   ```
   "orchestrator": {
     "enabled": true,
     "encryption_key_per_tenant": {
         "certificate_base_64": "",
         "certificate_password": "",
         "client_id": "",
         "directory_id": "",
         "vault_address": ""
     }
   }
   ```

You must convert the certificate to base64 before using it as a parameter override. To do that, run the following command:

   * PowerShell
     ```
     [convert]::ToBase64String((Get-Content -path "path_to_certificate" -Encoding byte))
     ```
   * Shell
     ```
     base64 [_path_to_certificate_]
     ```
2. Apply the new configuration, and then wait for the Orchestrator ArgoCD app to synchronize.
3. Enable the EncryptionKeyPerTenant feature by setting the following keys in `appSettings`:
   ```
   "EncryptionKeyPerTenant.Enabled": "true", "EncryptionKeyPerTenant.KeyProvider": "AzureKeyVault",
   ```

For more on updating `appSettings`, see [Configuring appSettings](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-appsettings#configuring-appsettings).

   :::note
   SMTP settings in Identity Server are not encrypted with the per-tenant key. After enabling encryption key per tenant, make sure to re-enter the SMTP password in the Automation Suite portal.
   :::