---
title: "2023.10.8"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-8"
---

**Release date: March 17, 2025**

## Removed dependency for single tenant migration

To simplify the migration process, you are no longer required to install.NET Core Desktop Runtime for 64-bit (x64) systems on your machine to run the Automation Cloud Migration Tool for a single tenant.

**Release date: February 13, 2025**

## What's new

This Automation Suite version brings various small bug fixes and improvements.

## Bug fixes

* An issue was preventing Fluentd from sending logs to remote locations due to a lack of memory buffer. We have fixed the issue.
* An issue prevented the inclusion of Insights dashboards in backups. We have fixed the issue.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/security-and-compliance).

### Velero backup fails with FailedValidation error

**Erratum - added September 24, 2025:** An issue prevents Velero scheduled backups from running successfully. A `FailedValidation` error message is displayed, indicating that no default backup location can be found. This issue occurs because the `default-bs1` backup storage location is not marked as the default. As a result, Velero cannot identify a valid backup target, and scheduled backups fail.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/velero-backup-fails-with-failedvalidation-error) section.

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-11#bug-fixes).

### Log streaming does not work in proxy setups

**Erratum - added June 26, 2025:** Log forwarding does not work in proxy setups because the proxy environment variables were not set in the logging pods. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/log-streaming-does-not-work-in-proxy-setups) section.

We fixed the issue in [Automation Suite 2023.10.10](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-10#bug-fixes).

### Licensing SQL connection error

**Erratum - added June 26, 2025:** Licensing SQL connection errors occur when the Data Source property specified both a named instance and a port.

We fixed the issue in [Automation Suite 2023.10.10](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-10#bug-fixes).

### Microsoft SQL Server 2016 exception

**Erratum - added April 15, 2025:** An issue related to AI Center causes Microsoft SQL Server 2016 to throw the following exception: `exception":"com.microsoft.sqlserver.jdbc.SQLServerException: ‘OPTIMIZE_FOR_SEQUENTIAL_KEY' is not a recognized CREATE INDEX`.

We fixed the issue in [Automation Suite 2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-9#bug-fixes).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2023.10.8](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-8) | Automation Ops 2023.10.7 | [AI Center 2023.10.8](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-8) | [Action Center 2023.10.8](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-8) |
| [Task Mining 2023.10.8](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-8) | [AI Computer Vision 2023.10.8](https://docs.uipath.com/ai-computer-vision/automation-suite/2023.10/user-guide/release-notes-2023-10-9) | [Insights 2023.10.8](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-8) | [Apps 2023.10.8](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/2023-10-8) |
| [Process Mining 2023.10.8](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-8) | [Document Understanding 2023.10.8](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10) | [Orchestrator 2023.10.9](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-9) |  |
|  |  | [Test Manager 2023.10.8](https://docs.uipath.com/test-suite/automation-suite/2023.10/release-notes/test-manager-2023-10-8) |  |
|  |  | [Data Service 2023.10.8](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/2023-10-8) |  |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.23.0 |
| ArgoCD | 2.13.3 |
| Prometheus | 3.1.0 |
| Grafana | 11.3.1 |
| Fluentd & Fluent-bit | logging-operator: 5.0.1  logging-operator-logging: 5.0.1 |
| Gatekeeper | 3.18.2 |
| Cert-Manager | 1.16.2 |
| Velero | 8.0.0 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/full-migration).