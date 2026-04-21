---
title: "2023.10.2+patch3"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-2-patch-3"
---

**Release date: April 2, 2025**

## About the patch

This release applies a patch to Automation Suite 2023.10.2. The patch addresses some issues in Apps. For more details, see the individual product release notes referenced in the [Product versions](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-2-patch-3#product-versions) section.

:::important
This fix will also be included in all future releases starting with Automation Suite 2023.10.9. We recommend that you wait for Automation Suite 2023.10.9 to get this fix.
:::

## How to apply the patch

To apply this patch, follow the instructions in [Applying a patch](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/applying-a-patch).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| Automation Hub 2023.10.2 | Automation Ops 2023.10.2 | AI Center 2023.10.2 | Action Center 2023.10.2 |
| Task Mining 2023.10.2 | AI Computer Vision 2023.10.2 | Insights 2023.10.2 | [Apps 2023.10.2-patch3](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/2023-10-2-patch3) |
| Process Mining 2023.10.2 | Document Understanding 2023.10.2 | Orchestrator 2023.10.3 |  |
|  |  | Test Manager 2023.10.2 |  |
|  |  | Data Service 2023.10.2 |  |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.20.0 |
| ArgoCD | v2.7.7 |
| Prometheus | v2.42.0 |
| Grafana | 10.2.3 |
| Fluentd & Fluent-bit | logging-operator: 4.2.1  logging-operator-logging: 4.2.1 |
| Gatekeeper | 3.12.0 |
| Cert-Manager | v1.12.3 |
| Velero | 3.1.6 |