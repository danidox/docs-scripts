---
title: "2024.10.2"
visible: true
slug: "automation-suite-on-eks-aks-2024-10-2"
---

**Release date: 17 February 2025**

## Support for full migration

Full migration is now supported in Automation Suite 2024.10.2.

Compared to the full migration steps in Automation Suite 2023.10, in this version there is an additional migration step in which you can update the schema of the Insights and Orchestrator databases after previously restoring them.

Also, we implemented the following improvements in the `UiPath.OrganizationMigrationApp` tool:

* We provide an inner exception during a database connection test for enhanced error logging and debugging.
* We improved the merging process of single sign-on users (SSO) from multiple organizations to handle database conflicts more efficiently. The update also provides accurate migration success messages and prevents potential data duplication. This enhancement significantly benefits organizations utilizing the MSI to Automation Suite setup with a multi-tenant configuration and SSO.

For more details, refer to [Performing a full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/full-migration).

**Release date: March 17, 2025**

## Removed dependency for single tenant migration

To simplify the migration process, you are no longer required to install.NET Core Desktop Runtime for 64-bit (x64) systems on your machine to run the Automation Cloud Migration Tool for a single tenant.

**Release date: February 17, 2025**

## Support added for Document Understanding modern projects

Document Understanding modern projects are now supported in Automation Suite on AKS offline deployments and Azure Government environments.

## Bug fixes

* **Erratum - added June 26, 2025:** We have fixed an issue where Automation Suite installations failed due to Certificate Authority (CA) certificates not being recognized. The issue occurred when the `CertificatePolicies` section included policy OID values exceeding 4 bytes.
* **Erratum - added February 25, 2025:** We fixed an issue which caused increased infrastructure load, if misconfigured. This issue impacted users who had Integration Service enabled on Automation Suite for EKS/AKS, versions 2024.10.0 and 2024.10.1, and did not have storage queues created.
* An issue was preventing Fluentd from sending logs to remote locations due to a lack of memory buffer. We have fixed the issue.
* An issue prevented the inclusion of Insights dashboards and Studio Web data in backups. We have fixed the issue.

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

**Erratum - added June 26, 2025**: To address this issue, you can edit the `input.json` file to disable secret rotation in the platform configuration. This change will persist through Automation Suite upgrades and reinstalls.

Take the following steps:

1. Update the `platform` section in the `input.json` file as shown in the following example:
   ```
   "platform": {
     "enabled": true,
     "advanced_configuration": {
       "identity-service": {
         "secretRotation": {
           "enabled": false
         }
       }
     }
   }
   ```
2. After applying this configuration, you must reinstall your Automation Suite deployment to ensure the change takes effect:
   ```
   uipathctl manifest apply input.json --versions versions.json
   ```

**Erratum - added May 14, 2025**: An issue causes service disruptions due to the automatic secret rotation, making services temporarily inaccessible.

To address this issue, take the following steps:

1. Restart the affected service to restore its normal functionality.
2. Navigate to the ArgoCD UI and from the platform applicatio, select **Details** &gt; **Parameters**. Edit the values to add `"secretRotation: enabled: false"` under `identity-service`. You must take this step after each Automation Suite upgrade or reinstallation.

For AI Center, all skills must be stopped and started from AI Center UI.

### OAuth token refresh issue due to incorrect version

**Erratum - added April 28, 2025:** Due to an incorrect version of `intsvcs/oauth-token-refresh` configured at the service level, the OAuth token refresh job is attempting to fetch a version that is not available in the UiPath offline registry. This causes issues during execution.

We have fixed this issue in Automation Suite [2024.10.3](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-3#bug-fixes).

### Orchestrator and AI Center require SQL Sever version 2019 and higher

**Erratum - added February 27, 2025**: For this version of Automation Suite, you need to use SQL Server version 2019 or higher for proper operation of Orchestrator and AI Center.

### Full migration from standalone products to Automation Suite not supported

You cannot currently perform a full migration from standalone products version 2024.10 to Automation Suite 2024.10 using the UiPath.OrganizationMigrationApp tool. We are actively working on introducing support for this scenario.

In the meantime, you can perform a single-tenant migration. For details on this migration option, refer to [Single tenant migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-openshift/using-the-migration-tool).

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2024.10.2](https://docs.uipath.com/automation-hub/automation-suite/2024.10/user-guide/release-notes-2024-10-2) | Automation Ops 2024.10.1 | [AI Center 2024.10.2](https://docs.uipath.com/ai-center/automation-suite/2024.10/user-guide/release-notes-2024-10-2) | [Action Center 2024.10.2](https://docs.uipath.com/action-center/automation-suite/2024.10/user-guide/release-notes-2024-10-2) |
| [Task Mining 2024.10.2](https://docs.uipath.com/task-mining/automation-suite/2024.10/user-guide/release-notes-2024-10-2) | [AI Computer Vision 2024.10.2](https://docs-dev.uipath.com/ai-computer-vision/automation-suite/2024.10/user-guide/release-notes-2024-10-2) | [Insights 2024.10.2](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/release-notes-2024-10-2) | [Apps 2024.10.2](https://docs.uipath.com/apps/automation-suite/2024.10/release-notes/2024-10-2) |
| [Process Mining 2024.10.2](https://docs.uipath.com/process-mining/automation-suite/2024.10/user-guide/process-mining-2024-10-2) | [Document Understanding AI Center-based projects 2024.10.2](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10)  [Document Understanding modern projects 2024.10.2](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10) | [Orchestrator 2024.10.3](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-3) |  |
|  |  | [Test Manager 2024.10.2](https://docs.uipath.com/test-suite/automation-suite/2024.10/release-notes/test-manager-2024-10-2) |  |
|  |  | [Data Service 2024.10.2](https://docs.uipath.com/data-service/automation-suite/2024.10/release-notes/2024-10-2) |  |
|  |  | [Studio Web 2024.10.2](https://docs.uipath.com/studio-web/automation-suite/2024.10/release-notes/2024-10-2) |  |
|  |  | [Integration Service 2024.10.2](https://docs.uipath.com/integration-service/automation-suite/2024.10/release-notes/2024-10-2) |  |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

| Component | Version |
| --- | --- |
| Istio | 1.23.0 |
| ArgoCD | 2.13.3 |
| Prometheus | 3.1.0 |
| Grafana | 11.4.0 |
| Fluentd and Fluent-bit | logging-operator: 5.0.1  logging-operator-logging: 5.0.1 |
| Gatekeeper | 3.18.2 |
| Cert-Manager | 1.16.2 |
| Velero | 8.3.0 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/full-migration).