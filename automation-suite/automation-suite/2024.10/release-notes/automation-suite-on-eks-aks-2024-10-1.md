---
title: "2024.10.1"
visible: true
slug: "automation-suite-on-eks-aks-2024-10-1"
---

**Release date: December 18, 2024**

## Support for full migration

Full migration is now supported in Automation Suite 2024.10.1.

Compared to the full migration steps in Automation Suite 2023.10, in this version there is an additional migration step in which you can update the schema of the Insights and Orchestrator databases after previously restoring them.

Also, we implemented the following improvements in the `UiPath.OrganizationMigrationApp` tool:

* We provide an inner exception during a database connection test for enhanced error logging and debugging.
* We improved the merging process of single sign-on users (SSO) from multiple organizations to handle database conflicts more efficiently. The update also provides accurate migration success messages and prevents potential data duplication. This enhancement significantly benefits organizations utilizing the MSI to Automation Suite setup with a multi-tenant configuration and SSO.

For more details, refer to [Performing a full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/full-migration).

**Release date: December 18, 2024**
:::important
**Erratum - added January 23, 2025**: We have identified an issue with Integration Service on Automation Suite 2024.10.1, which can cause increased infrastructure load, if misconfigured. As a result, we have removed Integration Service from the mentioned versions. Integration Service will be available again in Automation Suite 2024.10.2. If you already use Integration Service on Automation Suite 2024.10.1, reach out to the [UiPath Product Support](https://www.uipath.com/company/contact-us/contact-technical-support) for more details.
:::

## Improvements

* Studio Web is now supported on machines with Federal Information Processing Standards 140-2 (FIPS 140-2) enabled.
* Studio Web now supports workload identity.
* Integration Service and Studio Web now support offline environments.

## Bug fixes

* We have fixed an Automation Suite installation issue that occurred when using an SQL Server version prior to 2019.
* We have fixed an issue that caused Insights volumes to be created in two different zones following migration from Automation Suite on Linux to Automation Suite on EKS/AKS.
* We have fixed an issue causing Automation Hub to become inaccessible after an upgrade to Automation Suite 2024.10.
* When using style attributes in the HTML tags while customizing your **Login** page, they reflected accurately in the preview. However, upon saving the changes, the style attributes were deleted automatically. Now, all style attributes used within tags persist after saving your changes.
* We have fixed an issue causing the upgrade to fail due to the overriding of existing Insights PVC sizes.
* We fixed a bug that was breaking SAML2 when basic authentication was disabled, along with various other bugs.
* You can now forward logs to external tools, such as Splunk, using the OpenTelemetry Collector if you have opted for the Prometheus Grafana stack. Previously, this function was unavailable due to the switch to `kube-logging`.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights and Integration Service are not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable these services.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/security-and-compliance).

### Log streaming does not work in proxy setups

**Erratum - added June 26, 2025:** Log forwarding does not work in proxy setups because the proxy environment variables were not set in the logging pods. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/log-streaming-does-not-work-in-proxy-setups) section.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-4#bug-fixes).

### Deployment issue on shared EKS clusters with custom namespace

**Erratum - added June 26, 2025:** An issue causes the Automation Suite deployment on a shared EKS cluster to fail if the target namespace is not `uipath`. This issue is due to the network policy incorrectly expecting the presence of a `uipath` namespace regardless of the chosen namespace.

To address the issue, you must manually create a `uipath` namespace before deploying Automation Suite.

We have fixed this issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-4#bug-fixes).

### Kubernetes upgrade failure

**Erratum - added June 26, 2025**: An issue causes the Kubernetes upgrade to fail due to an incorrect configuration in Integration Service. The upgrade failure triggers the following error message: `Cannot evict pod as it would violate the Pod’s disruption budget`.

To address the issue, you must increase the replica count of `intsvcs-periodic`deployment using the following command:

```
kubectl scale deployment intsvcs-periodic --replicas=2 -n  uipath
```

We have fixed this issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-4#bug-fixes).

### Licensing SQL connection error

**Erratum - added June 26, 2025:** Licensing SQL connection errors occur when the Data Source property specified both a named instance and a port.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-4#bug-fixes).

### Service disruptions due to automatic secret rotation

**Erratum - added May 14, 2025**: An issue causes service disruptions due to the automatic secret rotation, making services temporarily inaccessible.

To address this issue, take the following steps:

1. Restart the affected service to restore its normal functionality.
2. Navigate to the ArgoCD UI and from the platform applicatio, select **Details** &gt; **Parameters**. Edit the values to add `"secretRotation: enabled: false"` under `identity-service`. You must take this step after each Automation Suite upgrade or reinstallation.

For AI Center, all skills must be stopped and started from AI Center UI.

### OAuth token refresh issue due to incorrect version

**Erratum - added April 28, 2025:** Due to an incorrect version of `intsvcs/oauth-token-refresh` configured at the service level, the OAuth token refresh job is attempting to fetch a version that is not available in the UiPath offline registry. This causes issues during execution.

We have fixed this issue in Automation Suite [2024.10.3](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-3#bug-fixes).

### Insights dashboards and Studio Web data excluded from backups

**Erratum - added April 2, 2025:** An issue is preventing the inclusion of Insights dashboards and Studio Web data in backups. To address this issue, refer to the [Backing up the cluster](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/backing-up-the-cluster#prerequisites) page. The issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-2#bug-fixes).

### Orchestrator and AI Center require SQL Sever version 2019 and higher

**Erratum - added February 27, 2025**: For this version of Automation Suite, you need to use SQL Server version 2019 or higher for proper operation of Orchestrator and AI Center.

### Fluentd logs transmission failure

**Erratum - added February 17, 2025**: An issue prevents Fluentd from sending logs to remote locations due to a lack of memory buffer. This is due to the memory buffer limit being set to 5MB by default. To address this issue, you must increase the memory buffer limit for Fluentd to prevent disruptions or delays when transmitting logs to a remote location.

This issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-2#bug-fixes).

### Microsoft Entra ID limitations

**Erratum - added January 20, 2025**: Insights, Studio Web, and Task Mining do not currently support Microsoft Entra ID (formerly Azure Active Directory) authentication configuration for access to SQL, storage, and other resources that support Microsoft Entra.

### Full migration from standalone products to Automation Suite not supported

You cannot currently perform a full migration from standalone products version 2024.10 to Automation Suite 2024.10 using the UiPath.OrganizationMigrationApp tool. We are actively working on introducing support for this scenario.

In the meantime, you can perform a single-tenant migration. For details on this migration option, refer to [Single tenant migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-openshift/using-the-migration-tool).

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
| [Automation Hub 2024.10.1](https://docs.uipath.com/automation-hub/automation-suite/2024.10/user-guide/release-notes-2024-10-1) | [Automation Ops 2024.10.1](https://docs.uipath.com/automation-ops/automation-suite/2024.10/user-guide/release-notes-2024-10-1) | [AI Center 2024.10.1](https://docs.uipath.com/ai-center/automation-suite/2024.10/user-guide/release-notes-2024-10-1) | [Action Center 2024.10.1](https://docs.uipath.com/action-center/automation-suite/2024.10/user-guide/release-notes-2024-10-1) |
| [Task Mining 2024.10.1](https://docs.uipath.com/task-mining/automation-suite/2024.10/user-guide/release-notes-2024-10-1) | [AI Computer Vision 2024.10.1](https://docs.uipath.com/ai-computer-vision/automation-suite/2024.10/user-guide/release-notes-2024-10-1) | [Insights 2024.10.1](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/release-notes-2024-10-1) | [Apps 2024.10.1](https://docs.uipath.com/apps/automation-suite/2024.10/release-notes/2024-10-1) |
| [Process Mining 2024.10.1](https://docs.uipath.com/process-mining/automation-suite/2024.10/user-guide/process-mining-2024-10-1) | [Document Understanding AI Center-based projects 2024.10.1](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-document-manager-2024-10-1)  [Document Understanding modern projects 2024.10.1](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/document-understanding-modern-2024-10-1) | [Orchestrator 2024.10.2](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-2) |  |
|  |  | [Test Manager 2024.10.1](https://docs.uipath.com/test-suite/automation-suite/2024.10/release-notes/test-manager-2024-10-1) |  |
|  |  | [Data Service 2024.10.1](https://docs.uipath.com/data-service/automation-suite/2024.10/release-notes/2024-10-1) |  |
|  |  | [Studio Web 2024.10.1](https://docs.uipath.com/studio-web/automation-suite/2024.10/release-notes/2024-10-1) |  |
|  |  | [Integration Service 2024.10.1](https://docs.uipath.com/integration-service/automation-suite/2024.10/release-notes/2024-10-1) |  |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

| Component | Version |
| --- | --- |
| Istio | 1.23.0 |
| ArgoCD | 2.12.6 |
| Prometheus | 2.55.1 |
| Grafana | 11.3.0 |
| Fluentd and Fluent-bit | logging-operator: 4.10.0  logging-operator-logging: 4.10.0 |
| Gatekeeper | 3.17.1 |
| Cert-Manager | 1.16.1 |
| Velero | 7.2.2 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/full-migration).