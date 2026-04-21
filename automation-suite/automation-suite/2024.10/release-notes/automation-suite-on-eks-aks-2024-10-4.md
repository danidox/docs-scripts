---
title: "2024.10.4"
visible: true
slug: "automation-suite-on-eks-aks-2024-10-4"
---

**Release date: June 26, 2025**

## Changes to the patching procedure

The procedure for applying patches now includes an additional step that requires you to download and use the corresponding `uipathctl` patch version before proceeding with the patch.

For more details, refer to [Applying a patch](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/applying-a-patch).

## Deprecation of UiPath managed backup

Starting with Automation Suite 2025.10, if you are using Automation Suite on AWS EKS or Azure AKS, you will need to leverage the [AWS](https://aws.amazon.com/blogs/containers/backup-and-restore-your-amazon-eks-cluster-resources-using-velero/) or [Azure](https://learn.microsoft.com/en-us/azure/backup/azure-kubernetes-service-cluster-backup) managed backup solution for backups. This allows you to unify your cloud backup strategy. The backup solution previously managed by UiPath will no longer be available.

## Bug fixes

* We have fixed an issue causing the Automation Suite deployment on a shared EKS cluster to fail when using a namespace different from `uipath`. The network policy helm chart now correctly handles custom namespaces.
* An issue was causing the Kubernetes upgrade to fail due to an incorrect configuration in Integration Service. The upgrade failure triggered the following error message: `Cannot evict pod as it would violate the Pod’s disruption budget`. We have fixed the issue.
* Log forwarding did not work in proxy setups because the proxy environment variables were not set in the logging pods. We have fixed the issue.
* Licensing SQL connection errors occurred when the Data Source property specified both a named instance and a port. We have fixed the issue.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights and Integration Service are not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable these services.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/security-and-compliance).

### Prerequisite checks fail when Process Mining is enabled

**Erratum - added December 19, 2025:** An issue causes the prerequisite checks to fail when Process Mining is enabled. The issue occurs due to the checks still requiring `cert-manager`, although `cert-manager` is no longer needed for Process Mining starting with Automation Suite 2024.10.3.

The failure message is a false positive and can be safely ignored.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-7#bug-fixes).

### Velero backup fails with FailedValidation error

**Erratum - added September 24, 2025:** An issue prevents Velero scheduled backups from running successfully. A `FailedValidation` error message is displayed, indicating that no default backup location can be found. This issue occurs because the `default-bs1` backup storage location is not marked as the default. As a result, Velero cannot identify a valid backup target, and scheduled backups fail.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/velero-backup-fails-with-failedvalidation-error) section.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-5#bug-fixes).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2024.10.4](https://docs.uipath.com/automation-hub/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [Automation Ops 2024.10.4](https://docs.uipath.com/automation-ops/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [AI Center 2024.10.4](https://docs.uipath.com/ai-center/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [Action Center 2024.10.4](https://docs.uipath.com/action-center/automation-suite/2024.10/user-guide/release-notes-2024-10-4) |
| [Task Mining 2024.10.4](https://docs.uipath.com/task-mining/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [AI Computer Vision 2024.10.4](https://docs-dev.uipath.com/ai-computer-vision/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [Insights 2024.10.4](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/release-notes-2024-10-4) | [Apps 2024.10.4](https://docs.uipath.com/apps/automation-suite/2024.10/release-notes/2024-10-4) |
| [Process Mining 2024.10.4](https://docs.uipath.com/process-mining/automation-suite/2024.10/user-guide/process-mining-2024-10-4) | [Document Understanding AI Center-based projects 2024.10.4](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10)  [Document Understanding modern projects 2024.10.4](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10) | [Orchestrator 2024.10.6](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-6) |  |
|  |  | [Test Manager 2024.10.4](https://docs.uipath.com/test-suite/automation-suite/2024.10/release-notes/test-manager-2024-10-4) |  |
|  |  | [Data Service 2024.10.4](https://docs.uipath.com/data-service/automation-suite/2024.10/release-notes/2024-10-4) |  |
|  |  | [Studio Web 2024.10.4](https://docs.uipath.com/studio-web/automation-suite/2024.10/release-notes/2024-10-4) |  |
|  |  | [Integration Service 2024.10.4](https://docs.uipath.com/integration-service/automation-suite/2024.10/release-notes/2024-10-4) |  |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.25.2 |
| ArgoCD | 3.0.0 |
| Prometheus | 3.3.0 |
| Grafana | 11.6.1 |
| Fluentd and Fluent-bit | logging-operator: 5.3.0  fluent/fluent-bit:4.0.1 |
| Gatekeeper | 3.19.1 |
| Cert-Manager | 1.17.2 |
| Velero | 9.1.0 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/full-migration).