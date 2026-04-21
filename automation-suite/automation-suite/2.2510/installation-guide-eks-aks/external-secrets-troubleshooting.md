---
title: "External Secrets troubleshooting"
visible: true
slug: "external-secrets-troubleshooting"
---

## Overview

This section provides troubleshooting steps for resolving issues related to the External Secrets Operator and secretstore configuration in Automation Suite.

To identify and resolve synchronization or authentication issues between your cluster and the external secret provider, follow the steps described in this section.

## Verify External Secrets pod status and logs

Begin by checking that the External Secrets Operator pods are running correctly.

If the pods are not in a **Running** state or show repeated restarts, review their logs for any errors related to authentication, permissions, or misconfiguration.

To check the status of the External Secrets pods and view their logs, run:

```
kubectl get pods -A | grep external-secrets
kubectl logs -f <pod-name> -n <namespace>
```

For example, to view logs from a specific pod, run:

```
kubectl logs -f external-secrets-7d8c9b5f9f-abc12 -n external-secrets
```

## Inspect SecretStore and ExternalSecret objects

If the pods are running correctly, verify that the SecretStore and ExternalSecret resources are properly configured and synchronized.

These resources define how external secrets are retrieved and stored, so any misconfiguration can prevent successful synchronization.

* **Check ExternalSecret resources** Start by reviewing the ExternalSecret objects in your cluster. This helps confirm that the resources are correctly linked to their SecretStore and that the sync status is valid.
  + To display and inspect your ExternalSecret resources, run the following commands:
    ```
    kubectl get externalsecrets -A
    kubectl describe externalsecret <externalsecret-name> -n <namespace>
    ```
  + For example, to review a specific ExternalSecret in the `uipath` namespace:
    ```
    kubectl describe externalsecret azure-secret-store -n uipath
    ```
* **Check SecretStore resources** Inspect the associated SecretStore configuration. This resource defines the connection details for your secret provider (such as Azure Key Vault), and errors here can block secret synchronization.
  + To review the SecretStore definitions, use the following commands:
    ```
    kubectl get secretstores -A
    kubectl describe secretstore <secretstore-name> -n <namespace>
    ```
  + For example, to examine a SecretStore configuration in the `uipath` namespace:
    ```
    kubectl describe secretstore azure-secretstore -n uipath
    ```
* **Check events related to External Secrets** Review any Kubernetes events related to the External Secrets Operator. These events can reveal synchronization failures, permission issues, or provider misconfigurations.
  + To view related events, run the following command:
    ```
    kubectl get events -A | grep external-secrets
    ```

When reviewing the event output, look for:
    - Error messages in the **Status** section
    - Conditions indicating whether `Ready: True`
    - Warnings or synchronization failures in the **Events** section

## Verify Secret Store credentials

If you are using Azure Key Vault as your secret provider, ensure that the credentials and configuration are valid and up to date.

Incorrect credentials or missing permissions are common causes of synchronization failures.

* **Authentication credentials**
  + Confirm that the `clientId`, `clientSecret`, and `tenantId` values are correct.
  + Ensure the service principal has the required permissions for the Key Vault.
* **Key Vault access policies**
  + Verify `Get` and `List` permissions for secrets.
  + Ensure the Key Vault firewall settings allow access from your cluster.
* **Workload identity configuration (if applicable)**
  + Check that federated credentials are correctly configured.
  + Ensure the associated service account has the necessary annotations.
* **Key Vault URI**
  + Verify that the `vaultUrl` in your SecretStore configuration is correct.

Example format:

    ```
    https://<key-vault-name>.vault.azure.net/
    ```

## Verify service principal permissions

If your deployment uses a service principal, confirm that it has access to retrieve secrets from Azure Key Vault.

To list the secrets accessible to your service principal, run:

```
az keyvault secret list --vault-name <key-vault-name>
```

## Common configuration issues

Review the following common issues and corresponding error messages to help diagnose the problem.

Expand Table

| Issue | Possible cause | Example / error output |
| --- | --- | --- |
| Secret not found in cluster | Missing Kubernetes secret | `Warning InvalidProviderConfig 3s (x4 over 8s) secret-store cannot get Kubernetes secret "azure-service-principal-secret" from namespace "uipath": secrets "azure-service-principal-secret" not found` |
| Invalid credentials | Incorrect client ID, client secret, or tenant ID | `error processing spec.data[0] (key: external-object-storage-account-key-10176524), err: azure.BearerAuthorizer#WithAuthorization: Failed to refresh the Token for request ... StatusCode=400` |
| Missing Key Vault object | Key not present in Azure Key Vault | `external-secrets error processing spec.data[0] (key: external-object-storage-account-key), err: Secret does not exist` |

To further investigate these issues, review the controller logs or describe the related resources:

```
kubectl describe externalsecret <name> -n <namespace>
kubectl describe secretstore <name> -n <namespace>
```