---
title: "2024.10.7"
visible: true
slug: "automation-suite-2024-10-7"
---

**Release date: December 19, 2025**

## Support bundle command no longer requires configuration files

You can generate the support bundle using a simplified command. The paths to the configuration file (`cluster_config.json`) and the versions file (`helm-charts.json`) parameters are now optional.

For details, refer to [Generating the support bundle](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/using-support-bundle-tool#generating-the-support-bundle).

## Bug fixes

* An issue was causing the upgrade to fail during the execution of the `uipathctl rke2 upgrade` command in chained upgrade scenarios. This occurred because the posthook secret and configmap import operation was not idempotent, leading to conflicts with existing Kubernetes objects. We have fixed the issue.
* An issue prevented the `uipathctl cluster pre-upgrade` command from completing successfully in environments configured with a proxy and external objectstore, due to an error during the Insights volume migration process. We have fixed this issue.
* We have fixed an issue that caused the prerequisite checks to fail when Process Mining was enabled. The issue occurred due to the checks incorrectly treating `cert-manager` as a required component, even though it is no longer needed for Process Mining.
* An issue prevented AI Center pods from connecting to the in-cluster object store in proxy-enabled environments. The issue occurred due to unsupported CIDR notations and FQDN regex patterns in the `no_proxy` configuration. We have fixed the issue.
* This release includes the fixes delivered in [Automation Suite 2024.10.3+patch2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-3-patch-2#2024103%2Bpatch2).

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/security-and-compliance).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2024.10.7.

**Legend:**

✅ - This Automation Suite version bundles a new version of the product. New release notes are available.

❌ - This Automation Suite version bundles a previously released version of the product. No new release notes are available.

| Product | Product version | Release status | Release notes |
| --- | --- | --- | --- |
| Action Center | 2024.10.7 | ✅ | [Action Center release notes](https://docs.uipath.com/action-center/automation-suite/2024.10/user-guide/release-notes-2024-10-7) |
| AI Center | 2024.10.7 | ✅ | [AI Center release notes](https://docs.uipath.com/ai-center/automation-suite/2024.10/user-guide/release-notes-2024-10-7) |
| AI Computer Vision | 2024.10.5 | ✅ | [AI Computer Vision release notes](https://docs.uipath.com/ai-computer-vision/automation-suite/2024.10/user-guide/release-notes-2024-10-5) |
| Apps | 2024.10.7 | ✅ | [Apps release notes](https://docs.uipath.com/apps/automation-suite/2024.10/release-notes/2024-10-7) |
| Automation Hub | 2024.10.6 | ✅ | [Automation Hub release notes](https://docs.uipath.com/automation-hub/automation-suite/2024.10/user-guide/release-notes-2024-10-6) |
| Automation Ops | N/A | ❌ | N/A |
| Data Service | 2024.10.7 | ✅ | [Data Service release notes](https://docs.uipath.com/data-service/automation-suite/2024.10/release-notes/2024-10-7) |
| Document Understanding | 2024.10.7 | ✅ | [Document Understanding AI Center-based projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10#2024107)  [Document Understanding modern projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10#2024107) |
| Insights | 2024.10.7 | ✅ | [Insights release notes](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/release-notes-2024-10-7) |
| Orchestrator | 2024.10.10 | ✅ | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-10) |
| Process Mining | 2024.10.7 | ✅ | [Process Mining release notes](https://docs.uipath.com/process-mining/automation-suite/2024.10/user-guide/process-mining-2024-10-7) |
| Task Mining | 2024.10.7 | ✅ | [Task Mining release notes](https://docs.uipath.com/task-mining/automation-suite/2024.10/user-guide/release-notes-2024-10-7) |
| Test Manager | 2024.10.7 | ✅ | [Test Manager release notes](https://docs.uipath.com/test-manager/automation-suite/2024.10/release-notes/test-manager-2024-10-7) |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.34.1+rke2r1 |
| ArgoCD | 3.2.0 |
| gatekeeper | 3.20.1 |
| rook | 1.17.6 |
| ceph | 19.2.3 |
| prometheus-pushgateway | 3.4.2 |
| cert-manager | 1.19.1 |
| kube-logging/logging-operator | 6.0.3 |
| kube-logging/config-reloader | 6.0.3 |
| istio | 1.28.0 |
| velero | 1.16.2 |
| reloader | 2.2.5 |
| Prometheus | 3.7.3 |
| Grafana | 12.2.1 |
| redis-operator | 8.0.2-2 |
| redis-cluster | 8.0.2-17 |
| oauth2-proxy | 7.13.0 |