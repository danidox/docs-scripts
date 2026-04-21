---
title: "2023.10.2+patch4"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-2-patch-4"
---

**Release date: May 21, 2025**

## About this patch

This release applies a patch to Automation Suite 2023.10.2. The patch addresses a cache validation issue that was preventing you from immediately receiving permissions when granted the App Creator role in Apps. With this patch, the issue has been fixed.

:::important
This fix will also be included in all future releases starting with Automation Suite 2023.10.9.
:::

## How to apply the patch

To apply this patch, follow the instructions in [Applying a patch](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/applying-a-patch).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

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