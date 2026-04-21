---
title: "Configuring Azure Key Vault as a secretstore"
visible: true
slug: "configuring-azure-key-vault-as-a-secretstore"
---

You can configure Azure Key Vault as a secretstore using either of the following methods:

* Service Principal authentication
* Workload Identity authentication

By default, all sensitive data is defined in `input.json`. You can separate this data into two parts:

* `input.json` - contains only configuration data.
* Azure Key Vault - stores credentials securely.
  :::note
  You cannot store certificate paths or certificate-related credentials as part of the secretstore.
  :::
:::important
All credentials referenced in `input.json` must exist as secrets in the Azure Key Vault before you configure the secretstore. If any referenced credential is missing from Azure Key Vault, the installation fails.
:::

## Using Service Principal authentication

To configure Azure Key Vault as secretstore using Service Principal authentication, take the following steps:.

1. For `uipathctl` to identify that the credentials are stored in the Azure Key Vault, you must add the secretstore section to `input.json` , as shown in the following example:
   ```
   "secret_store": {
     "enabled": true,
     "provider_configs": [
       {
         "type": "azure",
         "credentials_secret_name": "azure-service-principal-secret",
         "refresh_interval": "5m",
         "name": "azure-secret-store",
         "azure_kv": {
           "vault_url": "https://eso-azure-kv.vault.azure.net/",
           "tenant_id": "d8353d2a-b153-4d17-8827-902c51f72357"
         }
       }
     ]
   }
   ```
2. Create a Kubernetes secret that stores the Azure Service Principal credentials, as shown in the following example:
   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: azure-service-principal-secret
   type: Opaque
   stringData:
     clientId: <client-id>
     clientSecret: <client-secret>
   ```
3. Deploy the secret in the `uipath` namespace using the following command:
   ```
   kubectl apply -f azure-service-principal-secret -n uipath
   ```
4. Update the credential values in `input.json` to reference secrets stored in Azure Key Vault using the following format:
   ```
   vault/<vault-name>/<key-stored-in-the-vault>
   ```

Where:
   * `vault` – static keyword.
   * `vault-name` – the value of `secret_store.provider_configs[i].name` (for example, `azure-secret-store`).
   * `key-stored-in-the-vault` – the name of the secret as stored in Azure Key Vault.Before the change, your credentials might look like this:
   ```
   "admin_username": "admin",
   "admin_password": "password",
   ```

After updating them to reference Azure Key Vault, they should look like this:

   ```
   "admin_username": "vault/azure-secret-store/admin-username-1234",
   "admin_password": "vault/azure-secret-store/admin-password-1234",
   ```

The following image shows the secrets stored in Azure Key Vault.

![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/609687)

The following sample displays an `input.json` configuration with credentials stored in Azure Key Vault.

```
{
  "admin_password": "vault/azure-secret-store/admin-password-1234",
  "admin_username": "vault/azure-secret-store/admin-username-1234",
  "apps": {
    "enabled": true,
    "external_object_storage": {
      "account_key": "vault/azure-secret-store/apps-external-object-storage-account-key-1234",
      "account_name": "as-storage-account",
      "azure_fqdn_suffix": "core.windows.net",
      "bucket_name": "uipath-as-platform",
      "create_bucket": true,
      "enabled": true,
      "region": "us-east-1",
      "storage_type": "azure",
      "use_instance_profile": true
    }
  },
  "exclude_components": [],
  "external_object_storage": {
    "account_key": "vault/azure-secret-store/external-object-storage-account-key-1234",
    "account_name": "as-storage-account",
    "azure_fqdn_suffix": "core.windows.net",
    "create_bucket": true,
    "enabled": true,
    "region": "us-east-1",
    "storage_type": "azure",
    "use_instance_profile": true
  },
  "fabric": {
    "redis": {
      "hostname": "redis-cache.mycompany.com",
      "password": "vault/azure-secret-store/fabric-redis-password-1234",
      "port": 6380,
      "tls": true
    }
  },
  "fqdn": "automationsuite.mycompany.com",
  "infra": {
    "docker_registry": {}
  },
  "ingress": {
    "gateway_selector": {
      "istio": "ingressgateway"
    },
    "service_annotations": {
      "service.beta.kubernetes.io/azure-load-balancer-internal": "false",
      "service.beta.kubernetes.io/azure-load-balancer-ipv4": "ip-address"
    }
  },
  "install_type": "online",
  "integrationservices": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    }
  },
  "istioMinProtocolVersion": "TLSV1_3",
  "kubernetes_distribution": "aks",
  "orchestrator": {
    "enabled": true,
    "external_object_storage": {
      "account_key": "vault/azure-secret-store/orchestrator-external-object-storage-account-key-1234",
      "account_name": "os-storage-account",
      "azure_fqdn_suffix": "core.windows.net",
      "bucket_name": "uipath-as-orchestrator",
      "create_bucket": true,
      "enabled": true,
      "region": "us-east-1",
      "storage_type": "azure",
      "use_instance_profile": true
    },
    "sql_connection_str": "vault/azure-secret-store/orchestrator-sql-connection-str-1234",
    "testautomation": {
      "enabled": true
    },
    "updateserver": {
      "enabled": true
    }
  },
  "platform": {
    "enabled": true
  },
  "pod_identity": {
    "aks_managed_identity_client_id": "client-id",
    "enabled": true
  },
  "postgresql_connection_string_template_sqlalchemy_pyodbc": "vault/azure-secret-store/postgresql-connection-string-template-sqlalchemy-pyodbc-1234",
  "profile": "ha",
  "proxy": {
    "enabled": true,
    "http_proxy": "\u003c\u003chttp://\u003cPROXY-SERVER-IP\u003e\u003e:\u003cPROXY-PORT\u003e",
    "https_proxy": "\u003c\u003chttp://\u003cPROXY-SERVER-IP\u003e\u003e:\u003cPROXY-PORT\u003e",
    "no_proxy": "paste list from Configuring the cluster section"
  },
  "registries": {
    "docker": {
      "password": "",
      "pull_secret_name": "registry-credentials",
      "url": "registry.uipath.com",
      "username": ""
    },
    "helm": {
      "password": "",
      "url": "registry.uipath.com",
      "username": ""
    }
  },
  "secret_store": {
    "enabled": true,
    "secret_name": "",
    "provider_configs": [
      {
        "type": "azure",
        "credentials_secret_name": "azure-service-principal-secret",
        "is_default": true,
        "refresh_interval": "5m",
        "name": "azure-secret-store",
        "azure_kv": {
          "vault_url": "https://eso-azure-kv.vault.azure.net/",
          "tenant_id": "d8353d2a-b153-4d17-8827-902c51f72357",
          "managed_identity_id": null
        },
        "aws_kv": {
          "role_arn": null
        },
        "hashicorp_kv": {}
      }
    ]
  },
  "snapshot": {
    "aks_infra_resource_group": "MC_ci-asaks4002399_ci-asaks4002399_eastus",
    "enabled": true,
    "external_object_storage": {
      "account_name": "storaccid2547865",
      "auth_mode": "ServicePrincipal",
      "bucket_name": "uipath-backup",
      "client_id": "1fbd7d95-5f8c-4f70-90a6-fdf20310d10e",
      "client_secret": "vault/azure-secret-store/snapshot-external-object-storage-client-secret-1234",
      "cloud_name": "AzurePublicCloud",
      "resource_group": "ci-asaks4002399",
      "storage_type": "azure",
      "subscription_id": "b65b0225-ce9b-4a79-9dd9-c00071d40d64",
      "tenant_id": "d8353d2a-b153-4d17-8827-902c51f72357"
    }
  },
  "sql_connection_string_template": "vault/azure-secret-store/sql-connection-string-template-1234",
  "sql_connection_string_template_jdbc": "vault/azure-secret-store/sql-connection-string-template-jdbc-1234",
  "sql_connection_string_template_odbc": "vault/azure-secret-store/sql-connection-string-template-odbc-1234",
  "sql_connection_string_template_sqlalchemy_pyodbc": "vault/azure-secret-store/sql-connection-string-template-sqlalchemy-pyodbc-1234",
  "storage_class": "managed-premium",
  "storage_class_single_replica": "azurefile-csi",
  "test_manager": {
    "enabled": true,
    "external_object_storage": {
      "bucket_name": "uipath-as-platform"
    }
  },
  "tolerations": []
}
```

## Using Workload Identity authentication

You can configure Azure Key Vault as a secretstore using Workload Identity authentication instead of a Service Principal.

Workload Identity allows Kubernetes pods to access Azure resources without storing credentials in Kubernetes secrets.

Depending on your setup, you can either use the global workload identity that applies to all components or configure a separate workload identity specifically for Azure Key Vault, as follows:

* Use global workload identity
  ```
  "pod_identity": {
    "aks_managed_identity_client_id": "managed-identity-id",
    "enabled": true
  },
  "secret_store": {
    "enabled": true,
    "provider_configs": [
      {
        "type": "azure",
        "refresh_interval": "5m",
        "name": "azure-secret-store",
        "azure_kv": {
          "vault_url": "https://eso-azure-kv.vault.azure.net/"
        }
      }
    ]
  }
  ```
* Use a separate workload identity for Azure Key Vault
  ```
  "secret_store": {
    "enabled": true,
    "provider_configs": [
      {
        "type": "azure",
        "refresh_interval": "5m",
        "name": "azure-secret-store",
        "azure_kv": {
          "vault_url": "https://eso-azure-kv.vault.azure.net/",
          "managed_identity_id": "managed-identity-id"
        }
      }
    ]
  }
  ```

### Configuring managed identity for External Secrets Operator

To enable the External Secrets Operator to access Azure Key Vault using workload identity, take the following steps:

1. Perform the steps described in the [Workload identity configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#workload-identity-configuration) to provide federated credentials to the required service accounts.
2. In addition to step 3 of the Workload Identity configuration, run the following command to create federated credentials for the External Secrets Operator:
   ```
   create_federated_credentials "uipath" "external-secrets"
   ```
3. Assign the required roles to the managed identity so it can access secrets in Azure Key Vault:
   ```
   # Export the following variables with your correct values
   export SUBSCRIPTION_ID="<your-subscription-id>"
   export TARGET_RG="<your-resource-group-name>"
   export VAULT_NAME="<your-key-vault-name>"
   export USER_ASSIGNED_MANAGED_IDENTITY_OBJECT_ID="<your-managed-identity-object-id>"

   # Assign Key Vault roles to the managed identity
   az role assignment create --assignee $USER_ASSIGNED_MANAGED_IDENTITY_OBJECT_ID --role "Key Vault Secrets User" --scope "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$TARGET_RG/providers/Microsoft.KeyVault/vaults/$VAULT_NAME"
   az role assignment create --assignee $USER_ASSIGNED_MANAGED_IDENTITY_OBJECT_ID --role "Key Vault Reader" --scope "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$TARGET_RG/providers/Microsoft.KeyVault/vaults/$VAULT_NAME"
   ```

## Configuring external OCI-compliant private registry

When using a private registry, if you do not want to configure the registry credentials in `input.json`, you can provide them as a Kubernetes secret instead, as shown in the following example:

```
"registries": {
  "docker": {
    "pull_secret_name": "registry-credentials",
    "url": "sfbrdevhelmweacr.azurecr.io"
  }
}
```

Create the Kubernetes secret that stores the registry credentials, as shown in the following example:

```
apiVersion: v1
kind: Secret
metadata:
  name: registry-credentials
type: Opaque
data:
  url: base64Encode(sfbrdevhelmweacr.azurecr.io)
  username: base64Encode(<registry-username>)
  password: base64Encode(<registry-password>)
```

Apply the secret in the `uipath` namespace using the following command:

```
kubectl apply -f registry-credentials.yaml -n uipath
```