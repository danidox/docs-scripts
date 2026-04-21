---
title: "2023.10.5"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-5"
---

**Release date: August 14, 2024**

## AWS Signature Version 4 support

Automation Suite now uses AWS Signature Version 4 for all S3 API requests. This impacts the use of Automation Suite with S3 servers that do not support AWS Signature Version 4.

## Bug fixes

* Running a health check would create temporary network policies that were not cleaned up when the check concluded. We have fixed the issue.
* For AI Center and Task Mining, the `ListBucket API` prerequisite check failed when using an external objectstore. However, AI Center and Task Mining do not use the `ListBucket API` permission. We have removed the unnecessary check.
* In instances with host level SAML configured, when you accessed Automation Suite through a specific &lt;Automation_Suite_URL&gt;/&lt;Organization_name&gt; URL and selected the host level SAML login option, the ACS URL was incorrectly generated using the organization ID from the URL, instead of the expected host level ACS URL. We have fixed this. The system now correctly generates the host-level ACS URL during a host level SAML login, irrespective of the specific organization URL used to access Automation Suite.
* Previously, you could not save your SMTP settings without providing a username and password, even though these details were optional. This behavior no longer occurs.

## Known issues

### Upgrade failure due to overridden Insights PVC sizes

**Erratum - added December 18, 2024:** An issue causes upgrades to fail when the existing Insights PVC sizes are inadvertently overridden. To address this problem, you must manually change the PVC sizes in ArgoCD UI. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/upgrade-fails-due-to-overridden-insights-pvc-sizes) section.

This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-7#bug-fixes).

### Failing EKS backup related to Velero version

**Erratum - added December 18, 2024**: A Velero version-related issue causes the Automation Suite on EKS backup to fail. To address the issue, you must manually modify the Velero deployment. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/eks-backup-failure-due-to-velero-version) section.

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-7#bug-fixes).

### Insights volumes created in two different zones following migration

When you migrate from Automation Suite on Linux to Automation Suite on EKS/AKS, Insights-related volumes are occasionally created in two different zones. As a result, you may encounter issues when bringing up the Insights service. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/insights-pvs-created-in-two-different-zones-following-migration).

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Test Automation SQL connection string is ignored

**Erratum - added October 17, 2024**: When you provide an SQL connection string under the `orchestrator.testautomation` section of the `input.json` file, the `uipathctl` binary ignores the connection string and uses the one under the `orchestrator` section instead. To address the problem, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting#test-automation-sql-connection-string-is-ignored) section.

### Health check fails for component that is no longer used

Running a health check on AKS results in an `[ARGOCD_REDIS_PODS]` failure for ArgoCD Redis HA. However, ArgoCD Redis HA is no longer used in Automation Suite on AKS. We fixed the issue in [Automation Suite 2023.10.6](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-6#bug-fixes).

### Pods cannot communicate with FQDN in a proxy environment

**Erratum - added October 17, 2024**: In a proxy environment, if the proxy server uses the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods cannot communicate with the FQDN. The issue causes the following error:
```
System.Net.Http.HttpRequestException: The proxy tunnel request to proxy 'http://<proxyFQDN>:8080/' failed with status code '404'.
```

To fix the issue, see [Automation Suite on EKS/AKS troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/pods-cannot-communicate-with-fqdn-via-proxy).

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

### Insights dashboards backup issue

**Erratum - added December 18, 2024** We have identified an issue with the backup logic in Automation Suite for AKS/EKS. Specifically, this defect excludes the backup of Insights dashboards. However, all historical data is successfully backed up.

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
| [Automation Hub 2023.10.5](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-5) | [Automation Ops 2023.10.5](https://docs.uipath.com/automation-ops/automation-suite/2023.10/user-guide/release-notes-2023-10-5) | [AI Center 2023.10.5](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-5) | [Action Center 2023.10.5](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-5) |
| [Task Mining 2023.10.5](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-5) | AI Computer Vision 2023.10.4 | [Insights 2023.10.5](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-5) | [Apps 2023.10.5](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/2023-10-5) |
| [Process Mining 2023.10.5](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-5) | [Document Understanding 2023.10.5](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10) | [Orchestrator 2023.10.6](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-6) |  |
|  |  | [Test Manager 2023.10.5](https://docs.uipath.com/test-suite/automation-suite/2023.10/release-notes/test-manager-2023-10-5) |  |
|  |  | [Data Service 2023.10.5](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/2023-10-5) |  |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.22.2 |
| ArgoCD | 2.10.9 |
| Prometheus | 2.53.0 |
| Grafana | 11.1.0 |
| Fluentd & Fluent-bit | logging-operator: 4.8.0  logging-operator-logging: 4.8.0 |
| Gatekeeper | 3.16.3 |
| Cert-Manager | 1.14.5 |
| Velero | 6.2.0 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/full-migration).