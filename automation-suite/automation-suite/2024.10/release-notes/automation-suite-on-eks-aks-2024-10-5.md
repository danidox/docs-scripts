---
title: "2024.10.5"
visible: true
slug: "automation-suite-on-eks-aks-2024-10-5"
---

**Release date: September 24, 2025**

## Enhanced support for Azure backup store configuration in AKS

We have added support for using a storage account access key when configuring the backup store in AKS. This addition provides an alternative to service principal–based authentication, offering more flexibility without affecting existing configurations.

For more details, refer to [Providing the backup store configuration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/configuring-the-backup-store#aks).

## AI Units usage metrics available in support bundle tool

The Automation Suite support bundle tool now collects AI Units usage metrics if you use AI Center.

## Bug fixes

* We have fixed an issue that prevented log forwarding when using S3 endpoints in non-AWS format (that is, without `.amazonaws.com` in the URL), as the endpoint was not in the format expected by Fluentd.
* An issue prevented Velero backups from completing successfully. A `FailedValidation` error message was displayed, indicating that no default backup location could be found. This issue occurred because Velero could not locate a default backup storage location when the `spec.default field` was missing in the `BackupStorageLocation` configuration.
* We fixed an issue in Integration Service and Orchestrator where outgoing network requests did not respect environment proxy settings. This caused Jira and Slack connections to fail in EKS/AKS deployments with proxy configurations.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights and Integration Service are not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable these services.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/security-and-compliance).

### Prerequisite checks fail when Process Mining is enabled

**Erratum - added December 19, 2025:** An issue causes the prerequisite checks to fail when Process Mining is enabled. The issue occurs due to the checks still requiring `cert-manager`, although `cert-manager` is no longer needed for Process Mining starting with Automation Suite 2024.10.3.

The failure message is a false positive and can be safely ignored.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-7#bug-fixes).

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
| Document Understanding |  | ✅ | [Document Understanding AI Center-based projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10#2024105)  [Document Understanding modern projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10#2024105) |
| Insights | 2024.10.5 | ✅ | [Insights release notes](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/release-notes-2024-10-5) |
| Integration Service | 2024.10.5 | ✅ | [Integration Service release notes](https://docs.uipath.com/integration-service/automation-suite/2024.10/release-notes/2024-10-5) |
| Orchestrator | 2024.10.8 | ✅ | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-8) |
| Process Mining | 2024.10.5 | ✅ | [Process Mining release notes](https://docs.uipath.com/process-mining/automation-suite/2024.10/user-guide/process-mining-2024-10-5) |
| Studio Web | 2024.10.5 | ✅ | [Studio Web release notes](https://docs.uipath.com/studio-web/automation-suite/2024.10/release-notes/2024-10-5) |
| Task Mining | 2024.10.5 | ✅ | [Task Mining release notes](https://docs.uipath.com/task-mining/automation-suite/2024.10/user-guide/release-notes-2024-10-5) |
| Test Manager | 2024.10.5 | ✅ | [Test Manager release notes](https://docs.uipath.com/test-manager/automation-suite/2024.10/release-notes/test-manager-2024-10-5) |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.26.3 |
| ArgoCD | 3.0.11 |
| Prometheus | 3.5.0 |
| Grafana | 12.0.2 |
| Fluentd and Fluent-bit | logging-operator: 6.0.1  fluent/fluent-bit: 4.0.3 |
| Gatekeeper | 3.20.0 |
| Cert-Manager | 1.18.2 |
| Velero | 10.0.10 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/full-migration).