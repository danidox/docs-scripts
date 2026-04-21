---
title: "2024.10.5"
visible: true
slug: "automation-suite-2024-10-5"
---

**Release date: September 24, 2025**

## AI Units usage metrics available in support bundle tool

The Automation Suite support bundle tool now collects AI Units usage metrics if you use AI Center.

## New RHEL version supported

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

## Bug fixes

* We have fixed an issue that caused the temporary registry installation to fail with a timeout error when connecting to `registry-1.docker.io`.
* We have fixed an issue that prevented log forwarding when using S3 endpoints in non-AWS format (that is, without `.amazonaws.com` in the URL), as the endpoint was not in the format expected by Fluentd.
* We have fixed an issue causing a delay in Kerberos keytab rotation, which prevented immediate regeneration of authentication tokens and occasionally disrupted database connectivity for services.
* We have fixed an issue where the `uipathctl config tls-certificates` command did not update the registry certificates in ArgoCD for the in-cluster registry in offline scenarios.
* An issue prevented the required pods from being created when enabling GPU after adding a GPU node. This issue occurred only when using external registries with project names ( such as Harbor). We have fixed the issue.
* An issue prevented the installer from setting the `storage.useClientID` parameter when you selected a user-assigned managed identity for object storage. As a result, Orchestrator did not use your configured client ID, and in environments where access was restricted to user-assigned managed identities, Orchestrator could not start. We have fixed the issue.
* We have fixed an issue that prevented garbage collection from running during in-cluster registry cleanup.
* An issue caused the Thanos compactor to stop metrics block compaction in the object store due to a race condition in Prometheus. This led to increased storage usage in the Ceph bucket. We have fixed the issue.
* An issue caused the pre-upgrade process to stall when deleting the `rook-ceph-object-store`application. This issue occurred due to the `CephObjectStore` resource not finalizing, which prevented completion of the upgrade workflow. We fixed the issue.

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

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2024.10.5.

**Legend:**

✅ - This Automation Suite version bundles a new version of the product. New release notes are available.

❌ - This Automation Suite version bundles a previously released version of the product. No new release notes are available.

| Product | Product version | Release status | Release notes |
| --- | --- | --- | --- |
| Action Center | 2024.10.5 | ✅ | [Action Center release notes](https://docs.uipath.com/action-center/automation-suite/2024.10/user-guide/release-notes-2024-10-5) |
| AI Center | 2024.10.5 | ✅ | [AI Center release notes](https://docs.uipath.com/ai-center/automation-suite/2024.10/user-guide/release-notes-2024-10-5) |
| AI Computer Vision | N/A | ❌ | N/A |
| Apps | 2024.10.5 | ✅ | [Apps release notes](https://docs.uipath.com/apps/automation-suite/2024.10/release-notes/2024-10-5) |
| Automation Hub | 2024.10.5 | ✅ | [Automation Hub release notes](https://docs.uipath.com/automation-hub/automation-suite/2024.10/user-guide/release-notes-2024-10-5) |
| Automation Ops | 2024.10.5 | ✅ | [Automation Ops release notes](https://docs.uipath.com/automation-ops/automation-suite/2024.10/user-guide/release-notes-2024-10-5) |
| Data Service | 2024.10.5 | ✅ | [Data Service release notes](https://docs.uipath.com/data-service/automation-suite/2024.10/release-notes/2024-10-5) |
| Document Understanding | 2024.10.5 | ✅ | [Document Understanding AI Center-based projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10#2024105)  [Document Understanding modern projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10#2024105) |
| Insights | 2024.10.5 | ✅ | [Insights release notes](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/release-notes-2024-10-5) |
| Orchestrator | 2024.10.8 | ✅ | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-8) |
| Process Mining | 2024.10.5 | ✅ | [Process Mining release notes](https://docs.uipath.com/process-mining/automation-suite/2024.10/user-guide/process-mining-2024-10-5) |
| Task Mining | 2024.10.5 | ✅ | [Task Mining release notes](https://docs.uipath.com/task-mining/automation-suite/2024.10/user-guide/release-notes-2024-10-5) |
| Test Manager | 2024.10.5 | ✅ | [Test Manager release notes](https://docs.uipath.com/test-manager/automation-suite/2024.10/release-notes/test-manager-2024-10-5) |

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