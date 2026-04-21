---
title: "2023.10.6"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-6"
---

**Release date: October 17, 2024**

## Support for Amazon Linux 2023

**Erratum - added January 27, 2025**: Automation Suite on EKS now supports Amazon Linux 2023 (AL2023).

## Introducing FQDN update procedure

We are excited to announce that you can now update the Fully Qualified Domain Name (FQDN) of your Automation Suite cluster.

For details about the FQDN update procedure, see [Configuring the FQDN post-installation](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-the-fqdn-post-installation).

## Improved migration to Automation Suite

We made the following improvements to the migration workflows:

* When moving the Identity data of your tenants from standalone Orchestrator to Automation Suite, the tenant name in Automation Suite is now the same as the original tenant name in standalone Orchestrator. Previously, the Automation Suite tenant name was automatically generated in the `tenant_xxxxxxxx` format, where `xxxxxxxx` signified the first eight characters of the Automation Suite organization ID. For more information, see [Step 1: Moving the Identity organization data from standalone to Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/moving-the-identity-organization-data-from-standalone-to-automation-suite)
* We updated our documentation of the migration steps to clarify that you have the option to migrate multiple standalone product tenants to either a single Automation Suite organization or multiple Automation Suite organizations. For more information, see [Step 1: Moving the Identity organization data from standalone to Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/moving-the-identity-organization-data-from-standalone-to-automation-suite) and [Step 4: Merging organizations in Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/merging-organizations-in-automation-suite).
* We updated our documentation of the post-migration steps to clarify that you can clean up the old Redis keys for both Orchestrator and Identity from the cloud-based Redis console. For more information, see [Removing old cache keys](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/removing-old-cache-keys).

## Bug fixes

* Running a health check on AKS led to an `[ARGOCD_REDIS_PODS]` failure for ArgoCD Redis HA, although ArgoCD Redis HA is no longer used in Automation Suite on AKS. The behavior no longer occurs.
* In a proxy environment, if the proxy server used the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods could not communicate with the FQDN, and an error message was displayed. The behavior no longer occurs.
  :::note
  If you previously created a service entry according to the workaround in [Pods cannot communicate with FQDN in a proxy environment](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/pods-cannot-communicate-with-fqdn-via-proxy), we recommend that you delete the service entry after you upgrade to Automation Suite 2023.10.6 or later. To delete the service entry, use the following command: assignment
  ```
  kubectl delete serviceentry proxy -n uipath
  ```
  :::

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

### Cannot migrate between Automation Suite flavors when Apps is enabled

**Erratum - added December 18, 2024**: In an offline environment, you cannot migrate from Automation Suite on Linux to Automation Suite on EKS/AKS when Apps is enabled. The issue occurs due to a version discrepancy affecting the `business-apps/ba-migration-k8-utils` image.

To address the problem, update the existing version for the `business-apps/ba-migration-k8-utils` image in the `versions.json` file from 2023.10.4 to 2023.10.6 before running the migration command.

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-7#bug-fixes).

### Insights volumes created in two different zones following migration

**Erratum - added December 18, 2024**: When you migrate from Automation Suite on Linux to Automation Suite on EKS/AKS, Insights-related volumes are occasionally created in two different zones. As a result, you may encounter issues when bringing up the Insights service. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/insights-pvs-created-in-two-different-zones-following-migration).

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Failing EKS backup related to Velero version

**Erratum - added December 18, 2024**: A Velero version-related issue causes the Automation Suite on EKS backup to fail. To address the issue, you must manually modify the Velero deployment. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/eks-backup-failure-due-to-velero-version) section.

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-7#bug-fixes).

### Upgrade failure due to overridden Insights PVC sizes

**Erratum - added December 18, 2024:** An issue causes upgrades to fail when the existing Insights PVC sizes are inadvertently overridden. To address this problem, you must manually change the PVC sizes in ArgoCD UI. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/upgrade-fails-due-to-overridden-insights-pvc-sizes) section.

This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-7#bug-fixes).

### Insights dashboards backup issue

**Erratum - added December 18, 2024** We have identified an issue with the backup logic in Automation Suite for AKS/EKS. Specifically, this defect excludes the backup of Insights dashboards. However, all historical data is successfully backed up.

We are working diligently to resolve this issue. We aim to develop and implement a mitigation approach as early as possible.

If you are using Automation Suite on AKS/EKS along with UiPath Insights, this defect may affect your operations. While we address this issue, we suggest [manually exporting your dashboards](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/dashboards#exporting-and-importing-dashboards) as a preventive measure.

Note that backups are mainly used as a recovery method in the event of a disaster-level incident or in preparation for an Automation Suite upgrade. This is particularly useful if an upgrade fails and stored data needs to be restored to its previous state.

### Test Automation SQL connection string is ignored

**Erratum - added October 17, 2024**: When you provide an SQL connection string under the `orchestrator.testautomation` section of the `input.json` file, the `uipathctl` binary ignores the connection string and uses the one under the `orchestrator` section instead. To address the problem, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting#test-automation-sql-connection-string-is-ignored) section.

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2023.10.6](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-6) | Automation Ops 2023.10.5 | [AI Center 2023.10.6](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-6) | [Action Center 2023.10.6](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-6) |
| [Task Mining 2023.10.6](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-6) | [AI Computer Vision 2023.10.6](https://docs.uipath.com/ai-computer-vision/automation-suite/2023.10/user-guide/release-notes-2023-10-6) | [Insights 2023.10.6](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-6) | [Apps 2023.10.6](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/2023-10-6) |
| [Process Mining 2023.10.6](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-6) | [Document Understanding 2023.10.6](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10#2023106) | [Orchestrator 2023.10.7](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-7) |  |
|  |  | [Test Manager 2023.10.6](https://docs.uipath.com/test-suite/automation-suite/2023.10/release-notes/test-manager-2023-10-6) |  |
|  |  | [Data Service 2023.10.6](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/2023-10-6) |  |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.23.0 |
| ArgoCD | 2.11.3 |
| Prometheus | 2.54.1 |
| Grafana | 11.1.5 |
| Fluentd & Fluent-bit | logging-operator: 4.9.1  logging-operator-logging: 4.9.1 |
| Gatekeeper | 3.17.0 |
| Cert-Manager | 1.14.5 |
| Velero | 6.2.0 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/full-migration).