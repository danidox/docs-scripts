---
title: "2024.10.0+patch1"
visible: true
slug: "automation-suite-on-eks-aks-2024-10-0-patch-1"
---

**Release date: February 4, 2025**

## About this patch

This release applies a patch to Automation Suite on EKS/AKS 2024.10.0. The patch addresses some issues in Integration Service. For more details, see the individual product release notes referenced in the [Product versions](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-0-patch-1#product-versions) section.

After applying the patch, if the `intsvs-queue-healthcheck` job fails, take the following steps:

1. Delete any existing instances of Integration Service deployments which depend on the queues:
   1. To get an output of the changes that will be made to the cluster, run the following command:
      ```
      kubectl -n uipath get deploy -l argocd.argoproj.io/instance=integrationservices --show-labels | grep 'helm.sh/chart=gallupx\-'  | awk '{print $1}' | xargs -r kubectl delete deploy --dry-run=client -n uipath
      ```
   2. To apply the changes to the cluster, run the following command:
      ```
      kubectl -n uipath get deploy -l argocd.argoproj.io/instance=integrationservices --show-labels | grep 'helm.sh/chart=gallupx\-'  | awk '{print $1}' | xargs -r kubectl delete deploy
      ```
2. Create the required queues in the storage account. For details, see the [Storage](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/storage#queues) section.
3. Delete the current `intsvs-queue-healthcheck` job and re-sync the application, by running the following commands.
   ```
   kubectl delete job intsvcs-queue-healthcheck -n uipath
   argocd app sync integrationservices
   ```

You can also re-sync the application from the ArgoCD UI.

## How to apply the patch

To apply this patch, follow the instructions in [Applying a patch](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/applying-a-patch).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| Automation Hub 2024.10.0 | Automation Ops 2024.10.0 | AI Center 2024.10.0 | Action Center 2024.10.0 |
| Task Mining 2024.10.0 | AI Computer Vision 2024.10.0 | Insights 2024.10.0 | Apps 2024.10.0 |
| Process Mining 2024.10.0 | Document Understanding AI Center-based projects 2024.10.0  Document Understanding modern projects 2024.10.0 | Orchestrator 2024.10.0 |  |
|  |  | Test Manager 2024.10.0 |  |
|  |  | Data Service 2024.10.0 |  |
|  |  | Studio Web 2024.10.0 |  |
|  |  | [Integration Service 2024.10.0-patch1](https://docs.uipath.com/integration-service/automation-suite/2024.10/release-notes/2024-10-0-patch-1) |  |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

| Component | Version |
| --- | --- |
| Istio | 1.23.0 |
| ArgoCD | 2.11.3 |
| Prometheus | 2.54.1 |
| Grafana | 11.1.5 |
| Fluentd and Fluent-bit | logging-operator: 4.9.1  logging-operator-logging: 4.9.1 |
| Gatekeeper | 3.17.0 |
| Cert-Manager | 1.14.5 |
| Velero | 6.2.0 |