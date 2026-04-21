---
title: "2023.10.7"
visible: true
slug: "automation-suite-2023-10-7"
---

**Release date: December 18, 2024**

## Support for new RHEL version

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

**Release date: September 24, 2025**

## New flags for enhanced Kerberos authentication

We have introduced new configuration flags to give you more control over the Kerberos authentication. You can now use the following flags to customize the Kerberos authentication settings:

* `kerberos_auth_config.enable_integrated_sql_auth`: This flag allows you to decouple the Kerberos authentication from the SQL authentication login, and to enable or disable Kerberos authentication for SQL across all your products.
* `<serviceGroupName>.kerberos_auth_config.enabled`: This flag allows you to control the use of Kerberos authentication for SQL authentication at product level. You must replace `<serviceGroupName>` with the name of your product.

These new flags bring changes to the priority order for SQL Kerberos authentication, as follows:

1. Kerberos authentication for SQL is enabled by default when Kerberos authentication is enabled.
2. If you set `kerberos_auth_config.enable_integrated_sql_auth` to `false`, Kerberos authentication for SQL is disabled across all your products.
3. If you set `<serviceGroupName>.kerberos_auth_config.enabled` to `false`, Kerberos SQL authentication is disabled for the specified product.

For more details on Kerberos authentication, see [Setting up Kerberos authentication](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/setting-up-kerberos-authentication).

## New prerequisite checks

We have introduced more prerequisite checks to optimize the overall experience of installing and configuring Automation Suite and to catch missing requirements earlier. Here are some highlights:

* A new validation check ensures that the `READ_COMMITTED_SNAPSHOT` option is enabled in the SQL Server database. We have implemented this check validation for Orchestrator, Apps, and Process Mining.
* We have introduced a prerequisite check in the `mirror-registry.sh` and `hydrate-registry.sh` scripts to validate the OCI compliance of the external registry before uploading images.

## Changes to the logs forwarding method

We have changed the logs forwarding method to external tools, such as Splunk, due to the switch to `kube-logging`. Now, you can forward logs to Splunk using the OpenTelemetry Collector.

For details, see [Forwarding logs to external tools](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/forwarding-application-logs-to-external-tools).

## Support bundle enhancements

We made the following improvements to the Automation Suite support bundle:

* The support bundle now collects logs for the `uipath-auth` and `velero` namespaces.
* The support bundle now captures custom resources.

## Logging enhancement

Helm logs are now visible in the terminal output.

## Security enhancements

We continue to provide security updates and patches to address Common Vulnerabilities and Exposures (CVEs).

## Bug fixes

* **Erratum - added June 10, 2025:** In multi-node (HA) setups where Grafana is deployed with two replicas, a lack of common data sources between the replicas caused issues in user session management. This resulted in errors such as `Dashboard not found` and `Invalid dashboard UID in the request` appearing in the Grafana dashboard. We have fixed this issue.
* We have fixed an issue causing a side-by-side upgrade to fail in an offline environment when Apps was enabled.
* We have fixed an issue that caused Insights data loss when you reinstalled or upgraded Insights following an Automation Suite upgrade from version 2023.4 or older.
* We have fixed an Insights annotation issue that would block the Automation Suite installer.
* We have fixed an issue that caused log collection for RKE2 system commands to run indefinitely.
* We have fixed an issue causing the `aicenter skill sync` and `aicenter skill status` commands to fail during a side-by-side upgrade. This issue occurred due to a syntax error.
* An issue was preventing `exclude=rke2-*` from being automatically added to the `/etc/yum.conf` file on all nodes. This issue occurred particularly in online environments and caused an unintentional upgrade of the RKE2 service on nodes other than the first server. Previously, you had to manually add the exception to the `/etc/yum.conf` on all nodes. We have fixed the issue.
* We have fixed an issue causing unnecessary DNS resolution validation for `redis.<primary-fqdn>` and `redis-db.<primary-fqdn>` during Active/Passive prerequisite checks. This behavior no longer occurs.
* We have fixed an issue that occurred in non-HA Redis scenarios, where the `redis-cluster-0` pod could get stuck in a terminating state during node drain operations. This behavior no longer occurs.
* When using style attributes in the HTML tags while customizing your **Login** page, they reflected accurately in the preview. However, upon saving the changes, the style attributes were deleted automatically. Now, all style attributes used within tags persist after saving your changes.
* An issue was causing installation or upgrade failures when enabling Connaisseur during the configuration of an external OCI-compliant registry. This issue occurred when the `registries.trust.enabled` parameter was set to `true` in the `cluster_config.json` file. We have fixed the issue.
* We have fixed an issue causing the upgrade to fail due to the overriding of existing Insights PVC sizes.
* We fixed a bug that was breaking SAML2 when basic authentication was disabled, along with various other bugs.

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

### RKE2 certificate rotation command issue on agent nodes

**Erratum - added April 28, 2025**: An issue causes the RKE2 certificate rotation command to run on the agent nodes even though it is not supported. This issue occurs during the Automation Suite upgrade process.

To address this issue, you must manually edit `infra-installer.sh` and replace the `rke2 certificate rotate` command with `[[ ${NODE_ROLE} != "agent" ]] && rke2 certificate rotate` to exclude the agent nodes.

This issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-8#bug-fixes).

### Kubernetes upgrade failure

**Erratum - added April 15, 2025:** An issue causes the Kubernetes upgrade to fail due to a missing `certificate-injector-webhook` in `deployment.apps`. To address the issue, you must run the following command:
```
kubectl delete configmap -n uipath-infra certificate-injector-webhook-configmap --ignore-not-found
```

We fixed the issue in [Automation Suite 2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).

### Document Understanding deployment issue post-upgrade

**Erratum - added April 15, 2025:** An issue prevents you from importing files into your DM session in AI Center after upgrading to Automation Suite 2023.10.x. This issue occurs due to the `du-digitizer-worker` deployment from the old Automation Suite version not being fully cleaned up after the upgrade. Starting with Automation Suite 2023.10.0, the deployment was renamed to `du-digitizer-worker-deployment`.

To address the issue, you must navigate to the ArgoCD UI and from the `documentunderstanding` application, manually delete the old `du-digitizer-worker` deployment. After deletion, re-sync the `documentunderstanding` application.

We fixed the issue in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-8#bug-fixes).

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

### AI Center storage migration failure

**Erratum - added February 13, 2025**: An issue prevents `uipathctl` from correctly setting `executeMigration` to `true` during the migration process from Ceph in-cluster storage to external object storage in AI Center.

To fix this issue, you must manually set `executeMigration` to `true` in ArgoCD for AI Center and then proceed with a resync, ensuring to prune. This issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-8#bug-fixes).

### Email alerts configuration failure post upgrade

**Erratum - added February 13, 2025**: An issue affects the functionality of email alerts configuration and the setup of multiple receivers after upgrading from Automation Suite 2022.10. To address this issue, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/failure-to-configure-email-alerts-post-upgrade).

This issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-8#bug-fixes).

### FQDN update failure

**Erratum - added February 13, 2025**: An issue causes the FQDN update to fail due to the `update_fqdn` parameter to not being properly set in the `service-cluster-configurations` secret.

To address this issue, you must manually remove the `update_fqdn` and `update_fqdn_state` parameters and update the `service-cluster-configurations` secret using the following command:

```
kubectl patch secret service-cluster-configurations -n uipath-infra --type=json -p='[
  {"op": "remove", "path": "/data/UPDATE_FQDN"},
  {"op": "remove", "path": "/data/UPDATE_FQDN_STATE"}
]'
```

This issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-8#bug-fixes).

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

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.30.5+rke2r1 |
| ArgoCD | 2.12.6 |
| ceph | 17.2.6 |
| rook-ceph | 1.14.6 |
| prometheus-pushgateway | 1.10.0 |
| cert-manager | 1.16.1 |
| rancher-istio | 105.4.0-up1.23.2 |
| rancher-monitoring-crd | 105.1.0-up61.3.2 |
| rancher-gatekeeper | 104.0.1-up3.13.0 |
| rancher-monitoring | 105.1.0-up61.3.2 |
| longhorn | 1.6.3 |
| longhorn-crd | 1.1.100 |
| reloader | 1.0.95 |
| csi-driver-smb | 1.16.0 |
| velero | 1.14.1 |
| redis-operator | 7.4.6-2 |
| redis-cluster | 7.4.6-102 |
| oauth2-proxy | 7.7.1 |
| kube-logging/logging-operator | 4.9.1 |
| config-reloader | v0.0.5 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/full-migration).