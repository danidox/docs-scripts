---
title: "Accessing Automation Suite"
visible: true
slug: "accessing-automation-suite"
---

## Enabling kubectl

Before running any kubectl commands, make sure you have downloaded and installed [kubectl](https://kubernetes.io/docs/tasks/tools/) on your client machine. This allows you to run commands for retrieving passwords and configuration details for the cluster.

For more details on how to configure and use kubectl, refer to the following resources:

* for AKS:
  + [Cli documentation (az aks)](https://learn.microsoft.com/en-us/cli/azure/aks?view=azure-cli-latest#az-aks-get-credentials)
  + [Quickstart Example: Deploy an AKS Cluster Using Azure CLI](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli)
* for EKS:
  + [Connect kubectl to an EKS cluster by creating a kubeconfig file](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html)

## Managing certificates

:::important
The installation process generates self-signed certificates on your behalf. You should replace them with certificates signed by a trusted Certificate Authority (CA) as soon as installation completes. For instructions, see [Managing certificates](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-the-certificates#managing-the-certificates).
:::

If you try to access the cluster with a web browser, and the certificates are not from a trusted CA, then you will see a warning in the browser. You can rectify this by importing and trusting the cluster SSL certificate on the client computer running the browser.

To manage certificates, take the following steps:

1. To retrieve the current certificate, run the following command:
   * On Linux:
     ```
     kubectl get secret -n istio-system istio-ingressgateway-certs -o jsonpath='{.data.ca\.crt}' | base64 --decode | openssl x509 -text -noout
     ```
   * On Windows (PowerShell):
     ```
     (kubectl get secret -n istio-system istio-ingressgateway-certs -o jsonpath='{.data.ca\.crt}') | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($_)) }
     ```
2. To update the certificates, see [Managing certificates](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/managing-the-certificates#managing-the-certificates).

## Accessing Automation Suite general interface

:::note
You need to accept the self-signed certificate in the web browser to be able to access a cluster that is still configured with self-signed certificates.
:::

The general-use Automation Suite user interface serves as a portal for both organization administrators and organization users. It is a common organization-level resource from where everyone can access all of your Automation Suite areas: administration pages, platform-level pages, product-specific pages, and user-specific pages.

To access Automation Suite, take the following steps:

1. Go to the following URL:

`https://<FQDN>`
2. Switch to the **Default** organization.
3. The username is **orgadmin**.
4. Retrieve the password using the following command:
   ```
   kubectl get secret platform-service-secrets -n uipath -o jsonpath='{.data.identity\.hostAdminPassword}' | base64 --decode ; echo
   ```
   :::note
   Using the same command to retrieve the organization admin and the host admin passwords is by design. This is because the two passwords are initially the same. If **Change password on the first login** is set to **Required** at the host level, the organization administrator must set a new password when they log in for the first time.
   :::

## Accessing host administration

The host portal is for system administrators to configure the Automation Suite instance. The settings that you configure from this portal are inherited by all your organizations, and some can be overwritten at the organization level.

To access host administration, take the following steps:

1. Go to the following URL:

`https://${INPUT_JSON_FQDN}`
2. Switch to the **Host** organization.
3. The username is **admin**.
4. Retrieve the password using the following command:
   ```
   kubectl get secret platform-service-secrets -n uipath -o jsonpath='{.data.identity\.hostAdminPassword}' | base64 --decode ; echo
   ```
   :::note
   Using the same command to retrieve the organization admin and the host admin passwords is by design. This is because the two passwords are initially the same. If **Change password on the first login** is set to **Required** at the host level, the organization administrator must set a new password when they log in for the first time.
   :::

## Accessing ArgoCD

You can use the ArgoCD console to have an overview of the cluster, configurations, applications status, and health, all via a user-friendly UI.

To access the ArgoCD account using a username and password, take the following steps:

1. Access the following URL: `https://alm.${CONFIG_CLUSTER_FQDN}`.
2. Enter the following username: **admin**.
3. Access your password:
   ```
   kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d ; echo
   ```

## Accessing monitoring

Automation Suite uses Prometheus, Grafana, and Alert Manager to provide cluster management tools out of the box. This helps you manage the cluster and access monitoring and troubleshooting.

For details on how to use monitoring tools in Automation Suite, see [Using the monitoring stack](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/using-the-monitoring-stack#using-the-monitoring-stack).

You can access the Automation Suite monitoring tools individually using the following URLs:

Expand Table

| **Application** | **Tool** | **URL** | **Example** |
| --- | --- | --- | --- |
| Metrics | Prometheus | `https://monitoring.<FQDN>/metrics` | `https://monitoring.automationsuite.mycompany.com/metrics` |
| Dashboard | Grafana | `https://monitoring.<FQDN>/grafana` | `https://monitoring.automationsuite.mycompany.com/grafana` |
| Alert Management | Alert Manager | `https://monitoring.<FQDN>/alertmanager` | `https://monitoring.automationsuite.mycompany.com/alertmanager` |

### Authentication

To access Prometheus and Alert Manager, the username is **admin**.

To retrieve the password for Prometheus and Alert Manager, use the following command:

```
kubectl get  secret -n uipath dex-static-credential -o jsonpath='{.data.password}' | base64 -d ; echo
```

To access Grafana dashboard, the username is **admin**.

To retrieve the password for Grafana, use the following command:

```
kubectl get secret -n monitoring grafana-creds -o jsonpath='{.data.admin-password}' | base64 -d ; echo
```

## Accessing service database connection strings

You can access the database connection strings for each service as follows:

```
kubectl -n uipath get secret aicenter-secrets -o jsonpath='{.data.sqlConnectionString}' | base64 --decode
kubectl -n uipath get secret orchestrator-secrets -o jsonpath='{.data.sqlConnectionString}' | base64 --decode
kubectl -n uipath get secret automation-hub-secrets -o jsonpath='{.data.sqlConnectionString}' | base64 --decode
kubectl -n uipath get secret automation-ops-secrets -o jsonpath='{.data.sqlConnectionString}' | base64 --decode
kubectl -n uipath get secret insights-secrets -o jsonpath='{.data.sqlConnectionString}' | base64 --decode
kubectl -n uipath get secret platform-service-secrets -o jsonpath='{.data.sqlConnectionString}' | base64 --decode
kubectl -n uipath get secret test-manager-secrets -o jsonpath='{.data.sqlConnectionString}' | base64 --decode
```