---
title: "2023.10.12+patch1"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-12-patch-1"
---

**Release date: December 4, 2025**

## About this patch

This release applies a patch to Automation Suite 2023.10.12. The patch addresses some issues in Document Understanding. For more details, see the individual product release notes referenced in the [Product versions](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-12-patch-1#product-versions) section.

## How to apply the patch

To apply this patch, follow the instructions in [Applying a patch](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/applying-a-patch).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2023.10.12+patch1.

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
| Document Understanding | 2023.10.12-patch1 | ✅ | [Document Understanding release notes](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-ml-packages-2023-10-12patch1) |
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
| Istio | 1.26.3 |
| ArgoCD | 3.0.11 |
| Prometheus | 3.5.0 |
| Grafana | 12.0.2 |
| Fluentd & Fluent-bit | logging-operator: 6.0.1  fluent/fluent-bit: 4.0.3 |
| Gatekeeper | 3.20.0 |
| Cert-Manager | 1.18.2 |
| Velero | 10.0.10 |