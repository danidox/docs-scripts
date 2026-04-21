---
title: "2023.10.11"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-11"
---

**Release date: September 24, 2025**

## What's new

This Automation Suite version brings various small bug fixes and improvements.

## Bug fixes

* We have fixed an issue that prevented log forwarding when using S3 endpoints in non-AWS format (that is, without `.amazonaws.com` in the URL), as the endpoint was not in the format expected by Fluentd.
* An issue prevented Velero backups from completing successfully. A `FailedValidation` error message was displayed, indicating that no default backup location could be found. This issue occurred because Velero could not locate a default backup storage location when the `spec.default field` was missing in the `BackupStorageLocation` configuration.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/security-and-compliance).

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
| Apps | 2023.10.11 | ✅ | [Apps release notes](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/2023-10-1111) |
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

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/full-migration).