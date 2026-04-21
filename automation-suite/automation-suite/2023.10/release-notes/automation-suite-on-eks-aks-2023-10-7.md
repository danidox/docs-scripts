---
title: "2023.10.7"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-7"
---

**Release date: December 18, 2024**

## Changes to the logs forwarding method

We have changed the logs forwarding method to external tools, such as Splunk, due to the switch to `kube-logging`. Now, you can forward logs to Splunk using the OpenTelemetry Collector if you opted for the Prometheus Grafana stack.

For details, see [Forwarding logs to external tools](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/forwarding-logs-to-external-tools).

## Support bundle enhancements

We made the following improvements to the Automation Suite support bundle:

* The support bundle now collects logs for the `uipath-auth` and `velero` namespaces.
* The support bundle now captures custom resources.

## Bug fixes

* We have fixed an issue that was preventing you from migrating from Automation Suite on Linux to Automation Suite on EKS/AKS in an offline environment with Apps enabled.
* We have fixed an issue that caused Insights volumes to be created in two different zones following migration from Automation Suite on Linux to Automation Suite on EKS/AKS.
* We have fixed an issue causing Automation Suite on EKS backup to fail due to a Velero version-related problem. Previously, you had to manually modify the Velero deployment.
* We have fixed an issue causing the upgrade to fail due to the overriding of existing Insights PVC sizes.
* We fixed a bug that was breaking SAML2 when basic authentication was disabled, along with various other bugs.

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

### Insights dashboards excluded from backups

**Erratum - added April 2, 2025:** An issue is preventing the inclusion of Insights dashboards in backups. To address this issue, refer to the [Backing up the cluster](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/backing-up-the-cluster#prerequisites) page. The issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-8#bug-fixes).

### Fluentd logs transmission failure

**Erratum - added February 13, 2025**: An issue prevents Fluentd from sending logs to remote locations due to a lack of memory buffer. To address this issue, you must add a memory limit for Fluentd to prevent disruptions or delays when transmitting logs to a remote location.

This issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-8#bug-fixes).

### Microsoft Entra ID limitations

**Erratum - added January 20, 2025**: Insights and Task Mining do not currently support Microsoft Entra ID (formerly Azure Active Directory) authentication configuration for access to SQL, storage, and other resources that support Microsoft Entra.

### AI Center limitation

* AI Center and Document Understanding do not work in Automation Suite EKS environments with proxy enabled.
* AI Center and Task Mining do not work in Automation Suite EKS environments with proxy enabled.

### Insights dashboards backup issue

We have identified an issue with the backup logic in Automation Suite for AKS/EKS. Specifically, this defect excludes the backup of Insights dashboards. However, all historical data is successfully backed up.

We are working diligently to resolve this issue. We aim to develop and implement a mitigation approach as early as possible.

If you are using Automation Suite on AKS/EKS along with UiPath Insights, this defect may affect your operations. While we address this issue, we suggest [manually exporting your dashboards](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/dashboards#exporting-and-importing-dashboards) as a preventive measure.

Note that backups are mainly used as a recovery method in the event of a disaster-level incident or in preparation for an Automation Suite upgrade. This is particularly useful if an upgrade fails and stored data needs to be restored to its previous state.

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2023.10.7](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-7) | [Automation Ops 2023.10.7](https://docs.uipath.com/automation-ops/automation-suite/2023.10/user-guide/release-notes-2023-10-7) | [AI Center 2023.10.7](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-7) | [Action Center 2023.10.7](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-7) |
| [Task Mining 2023.10.7](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-7) | [AI Computer Vision 2023.10.7](https://docs.uipath.com/ai-computer-vision/automation-suite/2023.10/user-guide/release-notes-2023-10-7) | [Insights 2023.10.7](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-7) | [Apps 2023.10.7](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/2023-10-7) |
| [Process Mining 2023.10.7](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-7) | [Document Understanding 2023.10.7](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10) | [Orchestrator 2023.10.8](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-8) |  |
|  |  | [Test Manager 2023.10.7](https://docs.uipath.com/test-suite/automation-suite/2023.10/release-notes/test-manager-2023-10-7) |  |
|  |  | [Data Service 2023.10.7](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/2023-10-7) |  |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.23.0 |
| ArgoCD | 2.12.6 |
| Prometheus | 2.55.1 |
| Grafana | 11.3.1 |
| Fluentd & Fluent-bit | logging-operator: 4.10.0  logging-operator-logging: 4.10.0 |
| Gatekeeper | 3.17.1 |
| Cert-Manager | 1.16.1 |
| Velero | 7.2.2 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/full-migration).