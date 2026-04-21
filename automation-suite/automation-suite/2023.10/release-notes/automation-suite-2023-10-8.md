---
title: "2023.10.8"
visible: true
slug: "automation-suite-2023-10-8"
---

**Release date: March 17, 2025**

## Support for new RHEL version

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

**Release date: September 24, 2025**

## Removed dependency for single tenant migration

To simplify the migration process, you are no longer required to install.NET Core Desktop Runtime for 64-bit (x64) systems on your machine to run the Automation Cloud Migration Tool for a single tenant.

**Release date: February 13, 2025**

## New RHEL version supported

**Erratum - added February 17, 2025**: We have expanded our OS support to include RHEL 9.5. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

## New alert for Redis license expiration

We have added a new Prometheus alert for the expiration of internal Redis licenses. This alert has three notification levels, based on the timeframe the license is set to expire: 90, 30, or 7 days.

## Bug fixes

* **Erratum - added April 28, 2025:** We have fixed an issue causing the RKE2 certificate rotation command to run on agent nodes, even though it is not supported. This issue occurred during the Automation Suite upgrade process. Now, the RKE2 certificate rotation command runs exclusively on the server nodes during the upgrade process.
* **Erratum - added April 15, 2025:** We have fixed a Document Understanding issue that prevented you from importing files into your DM session in AI Center after upgrading to Automation Suite 2023.10.x. This issue occured due to the `du-digitizer-worker` deployment from the old Automation Suite version not being fully cleaned up after the upgrade.
* **Erratum - added February 27, 2025:** In Document Understanding, we are extending support for the Chinese, Japanese, and Korean OCR. This ensures uninterrupted use of the Chinese, Japanese, and Korean OCR, and provides an opportunity to transition to the Extended Languages OCR.
* We have fixed an issue causing the failure of agent node additions to existing clusters in offline environments. This issue occurred due to the nodes attempting to retrieve images from localhost, which led to failed prerequisite checks and the interruption of agent node initialization. Previously, you had to manually edit the `/etc/rancher/rke2/registries.yaml` file to add the registry URL.
* We have fixed an issue causing `uipathctl` to not correctly set `executeMigration` to `true`. This issue occurred when migrating from Ceph in-cluster storage to an external object storage for AI Center.
* Due to a bug in `containerd`, the deployment of ML skills was failing as a token expired before larger image downloads can be completed. This issue was addressed with a Kubernetes (RKE2) upgrade to version 1.30, eliminating instances of the `authorization failed` error during ML skill deployments.
* We have fixed an issue concerning the default `continue` setting in the `uipath-event-listener` receiver configuration in Alertmanager. After upgrading from Automation Suite 2022.10, the `continue` field value unexpectedly remained set to `false`, causing email alerts to fail. The `continue` field is now correctly set to `true`, restoring the ability to configure multiple receivers.
* We have fixed an issue that caused the proxy configuration to not work for AI Center due to unsupported CIDR notation and regular expressions (regex) in the `no_proxy` settings.
* We have fixed an issue caused by the `update_fqdn` parameter not being properly set in the `service-cluster-configurations` secret. As part of this fix, the `update_fqdn` flag is now being removed after updating the FQDN. We have also corrected the display message for running the `uipathctl rke update-fqdn` command.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/security-and-compliance).

### Kerberos keytab rotation does not trigger token regeneration

**Erratum - added September 24, 2025:** An issue causes Kerberos keytab rotation to not immediately regenerate authentication tokens, which may lead to temporary connectivity disruptions between services and the database.

To address the issue, you must manually trigger the Kerberos ticket renewal cronjob by running the following command:

```
kubectl delete job tgt-rotate-manual -n uipath --ignore-not-found ; kubectl create job tgt-rotate-manual --from=cronjob/kerberos-tgt-update -n uipath
```

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-11#bug-fixes).

### GPU enablement fails with external registries containing project names

**Erratum - added September 24, 2025:** An issue prevents GPU enablement after adding a GPU node when using external registries with project names (such as Harbor). The required pods do not start and display an `ImagePullBackoff` error.

If you are using an external registry with a project name, update the NVIDIA device plugin daemonset with the following command:

```
# Replace REGISTRY_WITH_PROJECT_NAME with the correct value (Eg. my.registry.io:443/myproject)
# Replcae TAG with the correct value. You can get this from the <installer_directory>/versions/docker-images.json file (Eg. v0.17.1)
kubectl set image daemonset/nvidia-device-plugin-daemonset \
  -n kube-system \
  nvidia-device-plugin-ctr=<REGISTRY_WITH_PROJECT_NAME>/k8s-device-plugin:<TAG>
```

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-11#bug-fixes).

### Orchestrator does not start when using user-assigned managed identity

**Erratum - added September 24, 2025:** An issue prevents the `storage.useClientID` parameter from being set when you select a user-assigned managed identity for object storage. As a result, tOrchestrator cannot start in environments where access is restricted to user-assigned managed identities.

To address the issue, you must manually set the parameter in ArgoCD, as follows:

1. In the ArgoCD Orchestrator application, go to **Details** &gt; **Parameters**.
2. In the **values** text box, set `storage.isExternal : true` and save.

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-11#bug-fixes).

### Thanos compactor stops on corrupted blocks

**Erratum - added September 24, 2025:** An issue causes the Thanos compactor to stop compacting metrics when it encounters corrupted blocks in the object store. This prevents compaction and leads to increased storage usage.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/failure-to-compact-metrics-due-to-corrupted-blocks-in-thanos) section.

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-11#bug-fixes).

### Task Mining Kerberos initialization failure

**Erratum - added June 26, 2025:** An issue causes the Task Mining service to fail to initialize in Kerberos environments. This issue occurs when the `kerberos-discoverygroup-user-keytab` secret is missing or when the `discoverygroup` app is not included in the `enabledApps` parameter of the `IntegratedAuth` app.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/task-mining-initialization-issue-in-kerberos) section.

We fixed the issue in [Automation Suite 2023.10.10](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-10#bug-fixes).

### Agent node addition failure in offline environments

**Erratum - added June 26, 2025:** An issue causes the addition process of agent nodes in offline environments to fail. Agent node additions require the temporary registry to be running. To address the issue, you must re-enable the temporary registry to successfully join the agent node.

We fixed the issue in [Automation Suite 2023.10.10.](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-10#bug-fixes)

### Installation fails due to CA certificates with large policy OIDs

**Erratum - added June 26, 2025:** An issue causes the Automation Suite installation to fail when using Certificate Authority (CA) certificates that include a `CertificatePolicies` section with policy OID values exceeding 4 bytes. This issue prevents Automation Suite from recognizing these CA certificates, interrupting the installation process.

To address the issue, you must either ensure that the policy OID values within the `CertificatePolicies` section do not exceed 4 bytes, or avoid using CA generators that add the `CertificatePolicies` section to the certificates.

We fixed the issue in [Automation Suite 2023.10.10.](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-10#bug-fixes)

### RKE2 custom configuration overwrite during upgrade

**Erratum - added June 26, 2025:** An issue causes the custom changes made to the RKE2 configuration file (`/etc/rancher/rke2/config.yaml`) to be overwritten during upgrades.

To address the issue, you must reapply your custom changes to the configuration file after each upgrade.

We fixed the issue in [Automation Suite 2023.10.10](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-10#bug-fixes).

### Licensing SQL connection error

**Erratum - added June 26, 2025:** Licensing SQL connection errors occur when the Data Source property specified both a named instance and a port.

We fixed the issue in [Automation Suite 2023.10.10.](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-10#bug-fixes)

### Microsoft SQL Server 2016 exception

**Erratum - added April 15, 2025:** An issue related to AI Center causes Microsoft SQL Server 2016 to throw the following exception: `exception":"com.microsoft.sqlserver.jdbc.SQLServerException: ‘OPTIMIZE_FOR_SEQUENTIAL_KEY' is not a recognized CREATE INDEX`.

We fixed the issue in [Automation Suite 2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).

### Kubernetes upgrade failure

**Erratum - added April 15, 2025:** An issue causes the Kubernetes upgrade to fail due to a missing `certificate-injector-webhook` in `deployment.apps`. To address the issue, you must run the following command:
```
kubectl delete configmap -n uipath-infra certificate-injector-webhook-configmap --ignore-not-found
```

We fixed the issue in [Automation Suite 2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).

### Orchestrator database validation issue

**Erratum - added April 15, 2025:** An issue prevents the installer from automatically creating and validating the Orchestrator database. The issue occurs even though the `sql.create_db` parameter is set to `true` in `cluster_config.json`.

To address the issue you must manually edit `/opt/UiPathAutomationSuite/UiPath_Installer/Prerequisite_Checks/scripts/validation.json` and set `advancedDbConfig.connectionStringParameter` to `""`, under `"service": "orchestrator"`, as shown in the following example:

```
"advancedDbConfig": [{
        "dbName": "AutomationSuite_Orchestrator_test",
        "connectionStringParameter": "",
        "optionalCommands":["ALTER DATABASE AutomationSuite_Orchestrator SET READ_COMMITTED_SNAPSHOT ON;"]
      }]
```

We fixed the issue in [Automation Suite 2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).

### Incomplete Docker registry cleanup process

**Erratum - added April 15, 2025:** An issue prevents the registry cleanup command from effectively clearing the unused Docker images from all registry pods. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/how-to-clean-up-unused-docker-images-from-registry-pods) section.

We fixed the issue in [Automation Suite 2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).

### Upgrade fails due to MongoDB to SQL Server migration

**Erratum - added April 15, 2025:** We have identified an issue impacting the side-by-side and the in-place upgrade of Automation Suite 2022.10 or earlier to Automation Suite 2023.10.0 or later. Due to a faulty migration from MongoDB to SQL Server, the upgrade operation fails if you have Apps enabled and use Kerberos authentication for the SQL Server database.

The recommended solution is to upgrade to [Automation Suite 2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).

### Kube-proxy health check not working

**Erratum - added April 15, 2025:** The `node-monitor` component, which monitors the node for issues such as checking `kube-proxy` health or if `ip_forward` is enabled, and cordons the node if issues arise, is not working for specific nodes such as GPU, `task-mining`, or `as-robot`. We have fixed this issue in Automation Suite [2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).

### Kerberos tickets do not automatically renew

**Erratum - added April 15, 2025**: Kerberos tickets fail to automatically renew after cluster restoration, requiring manual sync of the Windows Auth app.

This issue is fixed in Automation Suite [2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).

### Service upgrade fails during pre-service script execution

**Erratum - added April 15, 2025:** While you upgrade from older versions to 2023.10.x, the service upgrade script can abruptly end with non-zero exit code. This issue occurs when one of the pre-upgrade script, namely `scale-down-insights-looker-deployment.sh`, fails in certain scenarios. To address this issue, refer to .

The issue is fixed in [Automation Suite 2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).

### Same requirement for enabling user and SQL authentication

**Erratum - added March 24, 2025**: The configuration of user authentication and SQL authentication for the Automation Suite cluster is interconnected. To use either of them, currently you must set both `kerberos_auth_config.enabled` and `kerberos_auth_config.enable_integrated_sql_auth` parameters to true.

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

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.31.4+rke2r1 |
| ArgoCD | 2.13.3 |
| Grafana | 11.1.0 |
| ceph | 19.2.0 |
| rook-ceph | 1.16.1 |
| prometheus-pushgateway | 2.15.0 |
| cert-manager | 1.16.2 |
| rancher-istio | 105.4.0-up1.23.2 |
| rancher-monitoring-crd | 105.1.1-up61.3.2 |
| rancher-gatekeeper | 104.0.1-up3.13.0 |
| rancher-monitoring | 105.1.1-up61.3.2 |
| longhorn | 1.7.2 |
| longhorn-crd | 1.1.100 |
| reloader | 1.2.1 |
| kube-logging/logging-operator | 5.0.1 |
| kube-logging/config-reloader | 0.0.6 |
| velero | 1.15.2 |
| csi-driver-smb | 1.16.0 |
| redis-operator | 7.8.2-6 |
| redis-cluster | 7.8.2-60 |
| oauth2-proxy | 7.8.1 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/full-migration).