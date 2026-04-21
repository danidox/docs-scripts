---
title: "2024.10.4+patch1"
visible: true
slug: "automation-suite-on-eks-aks-2024-10-4-patch-1"
---

**Release date: August 26, 2025**

## About this patch

This release applies a patch to Automation Suite 2024.10.4. The patch addresses some issues in Integration Service, Studio Web, and Orchestrator. For more details, see the individual product release notes referenced in the [Product versions](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-3-patch-1#product-versions) section.

:::important
This fix will also be included in all future releases starting with Automation Suite 2024.10.5. We recommend that you wait for Automation Suite 2024.10.5 to get this fix.
:::

## How to apply the patch

To apply this patch, follow the instructions in [Applying a patch](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/applying-a-patch).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.25.2 |
| ArgoCD | 3.0.0 |
| Prometheus | 3.3.0 |
| Grafana | 11.6.1 |
| Fluentd and Fluent-bit | logging-operator: 5.3.0  fluent/fluent-bit:4.0.1 |
| Gatekeeper | 3.19.1 |
| Cert-Manager | 1.17.2 |
| Velero | 9.1.0 |

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2024.10.4+patch1.

**Legend:**

✅ - This Automation Suite version bundles a new version of the product. New release notes are available.

❌ - This Automation Suite version bundles a previously released version of the product. No new release notes are available.

| Product | Product version | Release status | Release notes |
| --- | --- | --- | --- |
| Action Center | N/A | ❌ | N/A |
| AI Center | N/A | ❌ | N/A |
| AI Computer Vision | N/A | ❌ | N/A |
| Apps | N/A | ❌ | N/A |
| Automation Hub | N/A | ❌ | N/A |
| Automation Ops | N/A | ❌ | N/A |
| Data Service | N/A | ❌ | N/A |
| Document Understanding | N/A | ❌ | N/A |
| Insights | N/A | ❌ | N/A |
| Integration Service | 2024.10.4-patch1 | ✅ | [Integration Service release notes](https://docs.uipath.com/integration-service/automation-suite/2024.10/release-notes/2024-10-4-patch-1) |
| Orchestrator | 2024.10.7 | ✅ | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-7) |
| Process Mining | N/A | ❌ | N/A |
| Studio Web | 2024.10.4-patch1 | ✅ | [Studio Web release notes](https://docs.uipath.com/studio-web/automation-suite/2024.10/release-notes/2024-10-4-patch-1) |
| Task Mining | N/A | ❌ | N/A |
| Test Manager | N/A | ❌ | N/A |