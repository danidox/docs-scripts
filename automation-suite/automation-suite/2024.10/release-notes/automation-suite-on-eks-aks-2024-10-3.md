---
title: "2024.10.3"
visible: true
slug: "automation-suite-on-eks-aks-2024-10-3"
---

**Release date: April 28, 2025**

## Disaster Recovery – Active/Passive deployments

**Erratum - added May 8, 2025:** We are happy to announce that Disaster Recovery in Active/Passive configuration is now supported for Automation Suite on EKS.

Now you can configure Automation Suite in a way that can withstand the complete failure of nodes, entire data centers, or even regions.

Automation Suite deployments in Active/Passive mode support the following scenarios:

* Same-region deployment
* Cross-region deployment

For details, see [Disaster Recovery – Active/Passive](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/disaster-recovery) and [Quick links](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/quick-links).

## Automation Suite Installer Wizard available in GA

We are excited to announce that the Automation Suite Installer Wizard, the new method for generating the Automation Suite `input.json` configuration file, is now generally available.

## PostgreSQL for Process Mining Airflow database

For Process Mining on Automation Suite 2024.10.3, you can now choose to use PostgreSQL for the `AutomationSuite_Airflow` database. If you choose not to use PostgreSQL and keep using Microsoft SQLServer, Process Mining on Automation Suite 2024.10.3 will run with a legacy version of Airflow.

Refer to [SQL Requirements for Process Mining](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/configuring-ms-sql-server#sql-requirements-for-process-mining) for more information on how to set up a PostgreSQL `AutomationSuite_Airflow` metadatabase.

:::important
You are recommended to move to PostgreSQL for the Airflow database, as PostgreSQL runs with the latest versions of Apache Airflow. Latest versions of Apache Airflow have various functionality, performance, and security fixes that older versions lack.
:::

## Removed Dapr dependency for Process Mining

Starting with Automation Suite 2024.10.3, Process Mining will no longer have a dependency on Dapr.

Task-Mining, however, will still continue to have a dependency on Dapr.

If you are installing Automation Suite where Process Mining is enabled and Task Mining is not enabled, then the Dapr application will not be installed.

In case of an Automation Suite upgrade where Process Mining is enabled and Task Mining is not enabled, then the Dapr application will be automatically uninstalled if it was installed by Automation Suite installer. If Dapr was user managed (installed by user), then Dapr should be uninstalled manually. For more details, refer to the [Uninstalling Dapr](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/meeting-the-process-mining-prerequisites#uninstalling-dapr) section.

## Additional custom CA certificate support

You can include any additional custom CA certificate by providing the `additonal_ca_certs` key with the external CA certificate path in the `input.json` file.

## Enhanced telemetry

Enhanced Automation Suite with a high-level summarized usage telemetry feature, provided guidance on viewing the generated XML file, and added telemetry sharing with UiPath Support via the Customer Portal.

## Istio HSTS enabled by default

To enhance security, Istio HSTS is now enabled by default.

## uipathctl improvements

* You can now list all the available options for the included and excluded flags when running the prerequisite checks command. For more details about `--list-options`, refer to the [uipathctl reference guide](https://docs.uipath.com/automation-suite/automation-suite/2024.10/reference-guide/uipathctl-prereq-run).
* For better eficiency, the diagnostic checks are no longer executed during the bundle creation process. Previously, a health check was performed by default during the support bundle creation, requiring the explicit use of the `--skip-diagnose` flag to bypass it. For more details on how to run the diagnostic checks, refer to the [uipathctl reference guide](https://docs.uipath.com/automation-suite/automation-suite/2024.10/reference-guide/uipathctl-health-diagnose).

## Bug fixes

* Due to an incorrect version of `intsvcs/oauth-token-refresh` configured at the services level, the OAuth token refresh job attempted to fetch a version that is not available in the UiPath offline registry. This led to issues during execution. This is now fixed.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights and Integration Service are not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable these services.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/security-and-compliance).

### Prerequisite checks fail when Process Mining is enabled

**Erratum - added December 19, 2025:** An issue causes the prerequisite checks to fail when Process Mining is enabled. The issue occurs due to the checks still requiring `cert-manager`, although `cert-manager` is no longer needed for Process Mining starting with Automation Suite 2024.10.3.

The failure message is a false positive and can be safely ignored.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-7#bug-fixes).

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

### Monitoring application stuck in Progressing state

After service installation, the monitoring application may remain in a Progressing state in ArgoCD.

To address this issue, you must manually sync the monitoring application with the **Replace** option:

1. In the ArgoCD UI, go to the monitoring application in the `argocd` namespace.
2. Sync the application manually with the **Replace** option selected.

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2024.10.3](https://docs.uipath.com/automation-hub/automation-suite/2024.10/user-guide/release-notes-2024-10-3) | [Automation Ops 2024.10.3](https://docs.uipath.com/automation-ops/automation-suite/2024.10/user-guide/release-notes-2024-10-3) | [AI Center 2024.10.3](https://docs.uipath.com/ai-center/automation-suite/2024.10/user-guide/release-notes-2024-10-3) | [Action Center 2024.10.3](https://docs.uipath.com/action-center/automation-suite/2024.10/user-guide/release-notes-2024-10-3) |
| [Task Mining 2024.10.3](https://docs.uipath.com/task-mining/automation-suite/2024.10/user-guide/release-notes-2024-10-3) | [AI Computer Vision 2024.10.3](https://docs-dev.uipath.com/ai-computer-vision/automation-suite/2024.10/user-guide/release-notes-2024-10-3) | [Insights 2024.10.3](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/release-notes-2024-10-3) | [Apps 2024.10.3](https://docs.uipath.com/apps/automation-suite/2024.10/release-notes/2024-10-3) |
| [Process Mining 2024.10.3](https://docs.uipath.com/process-mining/automation-suite/2024.10/user-guide/process-mining-2024-10-3) | [Document Understanding AI Center-based projects 2024.10.3](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10)  [Document Understanding modern projects 2024.10.3](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-2024-10) | [Orchestrator 2024.10.5](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-5) |  |
|  |  | [Test Manager 2024.10.3](https://docs.uipath.com/test-suite/automation-suite/2024.10/release-notes/test-manager-2024-10-3) |  |
|  |  | [Data Service 2024.10.3](https://docs.uipath.com/data-service/automation-suite/2024.10/release-notes/2024-10-3) |  |
|  |  | [Studio Web 2024.10.3](https://docs.uipath.com/studio-web/automation-suite/2024.10/release-notes/2024-10-3) |  |
|  |  | [Integration Service 2024.10.3](https://docs.uipath.com/integration-service/automation-suite/2024.10/release-notes/2024-10-3) |  |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.25.0 |
| ArgoCD | 2.14.4 |
| Prometheus | 3.2.1 |
| Grafana | 11.5.2 |
| Fluentd and Fluent-bit | logging-operator: 5.2.0  logging-operator-logging: 5.2.0 |
| Gatekeeper | 3.18.2 |
| Cert-Manager | 1.17.1 |
| Velero | 8.5.0 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/full-migration).