---
title: "2024.10.3+patch2"
visible: true
slug: "automation-suite-on-eks-aks-2024-10-3-patch-2"
---

**Release date: December 15, 2025**

## About this patch

This release applies a patch to Automation Suite 2024.10.3. The patch addresses some issues in Action Center and Document Understanding. For more details, see the individual product release notes referenced in the [Product versions](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-3-patch-2#product-versions) section.

:::important
This fix will also be included in all future releases starting with Automation Suite 2024.10.7. We recommend that you wait for Automation Suite 2024.10.7 to get this fix.
:::

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
| Automation Hub 2024.10.3 | Automation Ops 2024.10.3 | AI Center 2024.10.3 | [Action Center 2024.10.3-patch2](https://docs.uipath.com/action-center/automation-suite/2024.10/user-guide/release-notes-2024-10-3patch2) |
| Task Mining 2024.10.3 | AI Computer Vision 2024.10.3 | Insights 2024.10.4 | Apps 2024.10.3 |
| Process Mining 2024.10.3 | [Document Understanding AI Center-based projects 2024.10.3-patch2](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-document-manager-2024-10-3patch2) | Orchestrator 2024.10.5 |  |
|  |  | Test Manager 2024.10.3 |  |
|  |  | Data Service 2024.10.3 |  |
|  |  | Studio Web 2024.10.3 |  |
|  |  | Integration Service 2024.10.3 |  |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.25.0 |
| ArgoCD | 2.14.4 |
| Prometheus | 3.2.1 |
| Grafana | 11.5.2 |
| Fluentd and Fluent-bit | logging-operator: 5.2.0  logging-operator-logging: 5.2.0 |
| Gatekeeper | 3.18.2 |
| Cert-Manager | 1.17.1 |
| Velero | 8.5.0 |