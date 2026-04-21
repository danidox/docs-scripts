---
title: "2023.10.11"
visible: true
slug: "automation-suite-2023-10-11"
---

**Release date: September 24, 2025**

## AI Units usage metrics available in support bundle tool

The Automation Suite support bundle tool now collects AI Units usage metrics if you use AI Center.

## New RHEL version supported

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

## Bug fixes

* We have fixed an issue that prevented log forwarding when using S3 endpoints in non-AWS format (that is, without `.amazonaws.com` in the URL), as the endpoint was not in the format expected by Fluentd.
* We have fixed an issue causing a delay in Kerberos keytab rotation, which prevented immediate regeneration of authentication tokens and occasionally disrupted database connectivity for services.
* An issue prevented the required pods from being created when enabling GPU after adding a GPU node. This issue occurred only when using external registries with project names ( such as Harbor). We have fixed the issue.
* An issue prevented the installer from setting the `storage.useClientID` parameter when you selected a user-assigned managed identity for object storage. As a result, Orchestrator did not use your configured client ID, and in environments where access was restricted to user-assigned managed identities, Orchestrator could not start. We have fixed the issue.
* We have fixed an issue that prevented garbage collection from running during in-cluster registry cleanup.
* An issue caused the Thanos compactor to stop metrics block compaction in the object store due to a race condition in Prometheus. This led to increased storage usage in the Ceph bucket. We have fixed the issue.
* We have fixed an issue in Document Understanding where document imports could fail with Primary key violation errors caused by duplicate sequential IDs in SQL Server. Now, multi-page document imports complete reliably.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/security-and-compliance).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2023.10.11.

**Legend:**

✅ - This Automation Suite version bundles a new version of the product. New release notes are available.

❌ - This Automation Suite version bundles a previously released version of the product. No new release notes are available.

| Product | Product version | Release status | Release notes |
| --- | --- | --- | --- |
| Action Center | 2023.10.11 | ✅ | [Action Center release notes](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-11) |
| AI Center | 2023.10.11 | ✅ | [AI Center release notes](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-11) |
| AI Computer Vision | N/A | ❌ | N/A |
| Apps | 2023.10.11 | ✅ | [Apps release notes](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-11) |
| Automation Hub | 2023.10.11 | ✅ | [Automation Hub release notes](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-11) |
| Automation Ops | N/A | ❌ | N/A |
| Data Service | 2023.10.11 | ✅ | [Data Service release notes](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/2023-10-11) |
| Document Understanding | 2023.10.11 | ✅ | [Document Understanding release notes](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10#20231011) |
| Insights | 2023.10.11 | ✅ | [Insights release notes](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-11) |
| Orchestrator | 2023.10.12 | ✅ | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-12) |
| Process Mining | 2023.10.11 | ✅ | [Process Mining release notes](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-11) |
| Task Mining | 2023.10.11 | ✅ | [Task Mining release notes](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-11) |
| Test Manager | 2023.10.11 | ✅ | [Test Manager release notes](https://docs.uipath.com/test-manager/automation-suite/2023.10/release-notes/test-manager-2023-10-11) |

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

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/full-migration).