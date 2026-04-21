---
title: "Installing the External Secrets Operator in Kubernetes"
visible: true
slug: "installing-the-external-secrets-operator-in-kubernetes"
---

:::note
This step is required only if you want to store sensitive credentials in an external secret-management system. By default, Automation Suite includes the External Secrets Operator. If you choose not to use the bundled version, you can install your own External Secrets Operator instance by following the steps described in this section.
:::

The External Secrets Operator (ESO) is a Kubernetes operator that integrates external secret-management systems. It reads data from external APIs and automatically injects the values into Kubernetes Secrets.

Automation Suite currently supports Azure Key Vault, and we are working on bringing support for additional secret managers in future releases.

## Adding the External Secrets Helm repository

You must add the External Secrets Helm repository to your Helm installation as follows:

```
helm repo add external-secrets https://charts.external-secrets.io
```

After adding the repository, you must update your Helm repositories to fetch the latest chart information as follows:

```
helm repo update
```

## Installing the External Secrets Operator

You must deploy the External Secrets Operator using version v0.16.2 or an earlier supported release. Automation Suite supports External Secrets Operator versions from v0.10.2 up to v0.16.2.

Run the following command to install the operator:

```
helm install external-secrets \
  external-secrets/external-secrets \
  -n external-secrets \
  --create-namespace \
  --version 0.16.2
```

:::note
The External Secrets Operator requires access to the `uipath` namespace to function properly.
:::

## Verifying the installation

After installation, you must verify that the operator pods are running as follows:

```
kubectl get pods -n external-secrets
```

You should see output similar to the following example:

```
NAME                                               READY   STATUS    RESTARTS   AGE
external-secrets-7d8c9b5f9f-abc12                  1/1     Running   0          30s
external-secrets-cert-controller-6d8f7b9c-def34    1/1     Running   0          30s
external-secrets-webhook-8c9d7f6e5-ghi56           1/1     Running   0          30s
```

If all pods display a **Running** status, the installation is complete.