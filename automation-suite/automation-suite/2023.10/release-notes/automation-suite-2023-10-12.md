---
title: "2023.10.12"
visible: true
slug: "automation-suite-2023-10-12"
---

**Release date: November 6, 2025**

This release brings security updates to address [CVE-2025-55315](https://trust.uipath.com/?tcuUid=9cfc5284-1ee2-4785-9260-468d23c3b92f).

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/security-and-compliance).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2023.10.12.

**Legend:**

✅ - This Automation Suite version bundles a new version of the product. New release notes are available.

❌ - This Automation Suite version bundles a previously released version of the product. No new release notes are available.

| Product | Product version | Release status | Release notes |
| --- | --- | --- | --- |
| Action Center | 2023.10.12 | ✅ | [Action Center release notes](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-12) |
| AI Center | 2023.10.12 | ✅ | [AI Center release notes](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-12) |
| AI Computer Vision | N/A | ❌ | N/A |
| Apps | N/A | ❌ | N/A |
| Automation Hub | N/A | ❌ | N/A |
| Automation Ops | N/A | ❌ | N/A |
| Data Service | 2023.10.12 | ✅ | [Data Service release notes](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/2023-10-12) |
| Document Understanding | 2023.10.12 | ✅ | [Document Understanding release notes](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10#20231012) |
| Insights | 2023.10.12 | ✅ | [Insights release notes](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-12) |
| Orchestrator | 2023.10.13 | ✅ | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-13) |
| Process Mining | 2023.10.12 | ✅ | [Process Mining release notes](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-12) |
| Task Mining | 2023.10.12 | ✅ | [Task Mining release notes](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-12) |
| Test Manager | 2023.10.12 | ✅ | [Test Manager release notes](https://docs.uipath.com/test-manager/automation-suite/2023.10/release-notes/test-manager-2023-10-12) |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.33.2+rke2r1 |
| ArgoCD | v3.0.11 |
| Grafana | 12.0.2 |
| ceph | 19.2.3 |
| rook-ceph | 1.17.6 |
| prometheus-pushgateway | v3.4.1 |
| cert-manager | v1.18.2 |
| rancher-istio | 105.4.0-up1.23.2 |
| rancher-monitoring-crd | 106.1.2-up69.8.2-rancher.7 |
| rancher-gatekeeper | 104.0.1-up3.13.0 |
| rancher-monitoring | 106.1.2-up69.8.2-rancher.7 |
| longhorn | 1.9.1 |
| longhorn-crd | 1.1.100 |
| reloader | v2.2.0 |
| kube-logging/logging-operator | 6.0.1 |
| kube-logging/config-reloader | 6.0.1 |
| velero | 1.16.1 |
| csi-driver-smb | v1.18.0 |
| redis-operator | v7.22.0-15 |
| redis-cluster | v7.22.0-216.focal |
| oauth2-proxy | v7.11.0 |