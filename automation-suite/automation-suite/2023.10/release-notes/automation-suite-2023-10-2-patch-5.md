---
title: "2023.10.2+patch5"
visible: true
slug: "automation-suite-2023-10-2-patch-5"
---

**Release date: September 1, 2025**

## About this patch

This release applies a patch to Automation Suite 2023.10.2. The patch addresses some issues in Document Understanding. For more details, see the individual product release notes referenced in the [Product versions](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-2-patch-5#product-versions) section.

:::important
This fix will also be included in all future releases starting with Automation Suite 2023.10.11. We recommend that you wait for Automation Suite 2023.10.11 to get this fix.
:::

After applying the patch, you must update the following applications in ArgoCD to enable server-side generation of unique IDs:

* For **documentunderstanding**, set `du-digitizer.useServiceGeneratedUniqueIds` to `true`.
* For **aistorage**, set `useServiceGeneratedUniqueIds` to `true`.

## How to apply the patch

To apply this patch, follow the instructions in [Applying a patch](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/applying-a-patch).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2023.10.2+patch5.

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
| Document Understanding | 2023.10.2-patch5 | ✅ | [Document Understanding release notes](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-document-manager-automation-suite-2023-10-2-patch5) |
| Insights | N/A | ❌ | N/A |
| Orchestrator | N/A | ❌ | N/A |
| Process Mining | N/A | ❌ | N/A |
| Test Manager | N/A | ❌ | N/A |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.26.11 |
| ArgoCD | 2.7.7 |
| logging-operator | 4.1.0 |
| logging-operator-logging | 4.1.0 |
| gatekeeper | 3.12.0 |
| rook-ceph | 1.9.4 |
| prometheus-pushgateway | 2.1.6 |
| cert-manager | 1.12.3 |
| rancher-istio | 102.2.0-up1.17.2 |
| rancher-logging | 102.0.1-up3.17.10 |
| rancher-logging-crd | 102.0.1-up3.17.10 |
| rancher-monitoring-crd | 102.0.1-up40.1.2 |
| rancher-gatekeeper-crd | 102.1.0-up3.12.0 |
| rancher-gatekeeper | 100.2.0-up3.8.1 |
| rancher-monitoring | 102.0.1-up40.1.2 |
| longhorn | 1.4.3 |
| longhorn-crd | 1.1.100 |
| reloader | 0.0.129 |
| csi-driver-smb | 1.10.0 |
| velero | 3.1.6 |
| redis-operator | 7.2.4-7 |
| redis-cluster | 7.2.4-64 |