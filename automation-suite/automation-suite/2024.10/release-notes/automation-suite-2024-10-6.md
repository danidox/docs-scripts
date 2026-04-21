---
title: "2024.10.6"
visible: true
slug: "automation-suite-2024-10-6"
---

**Release date: November 6, 2025**

This release brings security updates to address [CVE-2025-55315](https://trust.uipath.com/?tcuUid=9cfc5284-1ee2-4785-9260-468d23c3b92f).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/security-and-compliance).

### AI Center in-cluster proxy connectivity issue

**Erratum - added December 19, 2025:** An issue prevents AI Center pods from connecting to the in-cluster object store in proxy-enabled environments. This occurs due to unsupported CIDR notations and FQDN regex patterns in the `no_proxy` configuration.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/ai-center-in-cluster-proxy-issue) section.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Prerequisite checks fail when Process Mining is enabled

**Erratum - added December 19, 2025:** An issue causes the prerequisite checks to fail when Process Mining is enabled. The issue occurs due to the checks still requiring `cert-manager`, although `cert-manager` is no longer needed for Process Mining starting with Automation Suite 2024.10.3.

The failure message is a false positive and can be safely ignored.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Upgrade failure during posthook import in chained upgrades

**Erratum - added December 19, 2025:** An issue causes the upgrade to fail during the execution of the `uipathctl rke2 upgrade` command in chained upgrade scenarios. This issue occurs due to the posthook secret and configmap import operation not being idempotent, which leads to conflicts with existing Kubernetes objects.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/upgrade-failure-during-posthook-import) section.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Pre-upgrade command fails with proxy and external objectstore

**Erratum - added December 19, 2025:** An issue prevents the `uipathctl cluster pre-upgrade` command from completing successfully in environments configured with a proxy and external objectstore. The issue occurs due to an error during the Insights volume migration process.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

## Bundling details

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2024.10.6.

**Legend:**

✅ - This Automation Suite version bundles a new version of the product. New release notes are available.

❌ - This Automation Suite version bundles a previously released version of the product. No new release notes are available.

| Product | Product version | Release status | Release notes |
| --- | --- | --- | --- |
| Action Center | 2024.10.6 | ✅ | [Action Center release notes](https://docs.uipath.com/action-center/automation-suite/2024.10/user-guide/release-notes-2024-10-6) |
| AI Center | 2024.10.6 | ✅ | [AI Center release notes](https://docs.uipath.com/ai-center/automation-suite/2024.10/user-guide/release-notes-2024-10-6) |
| AI Computer Vision | N/A | ❌ | N/A |
| Apps | N/A | ❌ | N/A |
| Automation Hub | N/A | ❌ | N/A |
| Automation Ops | N/A | ✅ | N/A |
| Data Service | 2024.10.6 | ✅ | [Data Service release notes](https://docs.uipath.com/data-service/automation-suite/2024.10/release-notes/2024-10-6) |
| Document Understanding | 2024.10.6 | ✅ | [Document Understanding AI Center-based projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10#2024106)  [Document Understanding modern projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10#2024106) |
| Insights | 2024.10.6 | ✅ | [Insights release notes](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/release-notes-2024-10-6) |
| Orchestrator | 2024.10.9 | ✅ | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-9) |
| Process Mining | 2024.10.6 | ✅ | [Process Mining release notes](https://docs.uipath.com/process-mining/automation-suite/2024.10/user-guide/process-mining-2024-10-6) |
| Task Mining | 2024.10.6 | ✅ | [Task Mining release notes](https://docs.uipath.com/task-mining/automation-suite/2024.10/user-guide/release-notes-2024-10-6) |
| Test Manager | 2024.10.6 | ✅ | [Test Manager release notes](https://docs.uipath.com/test-manager/automation-suite/2024.10/release-notes/test-manager-2024-10-6) |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.33.2+rke2r1 |
| ArgoCD | v3.0.11 |
| gatekeeper | 3.20.0 |
| rook | 1.17.6 |
| ceph | 19.2.3 |
| prometheus-pushgateway | v3.4.1 |
| cert-manager | v1.18.2 |
| kube-logging/logging-operator | 6.0.1 |
| kube-logging/config-reloader | 6.0.1 |
| istio | 1.26.3 |
| velero | 1.16.1 |
| reloader | v2.2.0 |
| Prometheus | v3.5.0 |
| Grafana | 12.0.2 |
| redis-operator | v7.22.0-15 |
| redis-cluster | v7.22.0-216.focal |
| oauth2-proxy | v7.11.0 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/full-migration).