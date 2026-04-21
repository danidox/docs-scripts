---
title: "2023.10.4+patch3"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-4-patch-3"
---

**Release date: October 13, 2025**

## About this patch

This release applies a patch to Automation Suite 2023.10.4. The patch addresses some issues in Automation Hub. For more details, see the individual product release notes referenced in the [Product versions](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-4-patch-3#product-versions) section.

:::important
This fix will also be included in all future releases starting with Automation Suite 2023.10.12. We recommend that you wait for Automation Suite 2023.10.12 to get this fix.
:::

## How to apply the patch

To apply this patch, follow the instructions in [Applying a patch](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/applying-a-patch).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2023.10.4+patch3.

**Legend:**

✅ - This Automation Suite version bundles a new version of the product. New release notes are available.

❌ - This Automation Suite version bundles a previously released version of the product. No new release notes are available.

| Product | Product version | Release status | Release notes |
| --- | --- | --- | --- |
| Action Center | N/A | ❌ | N/A |
| AI Center | N/A | ❌ | N/A |
| AI Computer Vision | N/A | ❌ | N/A |
| Apps | N/A | ❌ | N/A |
| Automation Hub | 2023.10.4-patch3 | ✅ | [Automation Hub release notes](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-4-patch-3) |
| Automation Ops | N/A | ❌ | N/A |
| Data Service | N/A | ❌ | N/A |
| Document Understanding | N/A | ❌ | N/A |
| Insights | N/A | ❌ | N/A |
| Orchestrator | N/A | ❌ | N/A |
| Process Mining | N/A | ❌ | N/A |
| Task Mining | N/A | ❌ | N/A |
| Test Manager | N/A | ❌ | N/A |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.21.2 |
| ArgoCD | 2.10.9 |
| Prometheus | 2.51.2 |
| Grafana | 10.4.2 |
| Fluentd & Fluent-bit | logging-operator: 4.6.0  logging-operator-logging: 4.6.0 |
| Gatekeeper | 3.16.0 |
| Cert-Manager | 1.14.5 |
| Velero | 6.2.0 |