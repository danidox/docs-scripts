---
title: "2023.10.9"
visible: true
slug: "automation-suite-2023-10-9"
---

**Release date: April 15, 2025**

## Support for new RHEL version

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

**Release date: September 24, 2025**

## Additional custom CA certificate support

Previously, you could update only ArgoCD CA certificates via the `./bin/uipathctl config argocd ca-certificates update --cacert [PATH]` command. For details, refer to the [Managing the external OCI-compliant registry certificate](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/managing-the-certificates#managing-the-external-oci-compliant-registry-certificate) section.

Now, you can add any additional custom CA certificate for Docker registries in online environments during initial install time. You can do this by providing the `registry_ca_cert` key with the external CA certificate path in the `cluster_config.json` file. For details, refer to the [External OCI-compliant registry configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/external-oci-compliant-registry-configuration) page.

## PostgreSQL for Process Mining Airflow database

For Process Mining on Automation Suite 2023.10.9, you can now choose to use PostgreSQL for the `AutomationSuite_Airflow` database. If you choose not to use PostgreSQL and keep using Microsoft SQLServer, Process Mining on Automation Suite 2023.10.9 will run with a legacy version of Airflow.

Refer to [SQL Requirements for Process Mining](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/configuring-ms-sql-server#sql-requirements-for-process-mining) for more information on how to set up a PostgreSQL `AutomationSuite_Airflow` metadatabase.

:::important
You are recommended to move to PostgreSQL for the Airflow database, as PostgreSQL runs with the latest versions of Apache Airflow. Latest versions of Apache Airflow have various functionality, performance, and security fixes that older versions lack.
:::

## Removed Dapr dependency for Process Mining

Starting with Automation Suite 2023.10.9, Process Mining will no longer have a dependency on Dapr.

Task-Mining, however, will still continue to have a dependency on Dapr.

If you are installing Automation Suite where Process Mining is enabled and Task Mining is not enabled, then the Dapr application will not be installed.

In case of an Automation Suite upgrade where Process Mining is enabled and Task Mining is not enabled, then the Dapr application will be automatically uninstalled.

## Enhanced telemetry

Enhanced Automation Suite with a high-level summarized usage telemetry feature, provided guidance on viewing the generated XML file, and added telemetry sharing with UiPath Support via the Customer Portal.

## Istio HSTS enabled by default

To enhance security, Istio HSTS is now enabled by default.

## Optional Docker pull secret value

The `registries.docker.pull_secret_value` field, which needs to be provided in the `cluster_config.json` file, is now optional.

## Bug fixes

* **Erratum - added April 15, 2025:** An issue related to AI Center caused Microsoft SQL Server 2016 to throw the following exception: `exception":"com.microsoft.sqlserver.jdbc.SQLServerException: ‘OPTIMIZE_FOR_SEQUENTIAL_KEY' is not a recognized CREATE INDEX`. We have fixed the issue.
* An issue caused the service upgrade script to abruptly end with non-zero exit code when upgrading from lower versions to 2023.10.x. This issue occurred when one of the pre-upgrade script, namely `scale-down-insights-looker-deployment.sh`, failed in certain scenarios. This issue is now fixed.
* Kerberos tickets failed to automatically renew after cluster restoration. This issue is now fixed, expired Kerberos tickets are now automatically detected and restored.
* An issue was causing the `node-monitor` component, which monitors the node for issues such as checking `kube-proxy` health or if `ip_forward` is enabled, and cordons the node if issues arise, to not work for specific nodes such as GPU, `task-mining`, or `as-robot`. We have fixed the issue.
* We have fixed an issue causing the side-by-side and the in-place upgrade of Automation Suite 2022.10 or earlier to Automation Suite 2023.10.0 or later to fail when Apps was enabled and you used Kerberos authentication for the SQL Server database.
* Previously, the configuration of user authentication and SQL authentication for the Automation Suite cluster was interconnected. To use either of them, you had to set both `kerberos_auth_config.enabled` and `kerberos_auth_config.enable_integrated_sql_auth` parameters to true. Currently, we allow independent configuration of only user authentication by setting `kerberos_auth_config.enabled` to true and `kerberos_auth_config.enable_integrated_sql_auth` to false. Independent SQL authentication is still not supported.
* An issue was preventing the registry cleanup command from effectively clearing the unused Docker images from all registry pods. We have fixed the issue.
* An issue was preventing the installer from automatically creating and validating the Orchestrator database. The issue occurred even though the `sql.create_db` parameter was set to `true` in `cluster_config.json`. We have fixed the issue.
* An issue was causing the Kubernetes upgrade to fail due to a missing `certificate-injector-webhook` in `deployment.apps`. We have fixed the issue.

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

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2023.10.9](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-9) | [Automation Ops 2023.10.9](https://docs.uipath.com/automation-ops/automation-suite/2023.10/user-guide/release-notes-2023-10-9) | [AI Center 2023.10.9](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-9) | [Action Center 2023.10.9](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-9) |
| [Task Mining 2023.10.9](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-9) | [AI Computer Vision 2023.10.9](https://docs.uipath.com/ai-computer-vision/automation-suite/2023.10/user-guide/release-notes-2023-10-9) | [Insights 2023.10.9](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-9) | [Apps 2023.10.9](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/2023-10-9) |
| [Process Mining 2023.10.9](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-9) | [Document Understanding 2023.10.9](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10) | [Orchestrator 2023.10.10](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-10) |  |
|  |  | [Test Manager 2023.10.9](https://docs.uipath.com/test-suite/automation-suite/2023.10/release-notes/test-manager-2023-10-9) |  |
|  |  | [Data Service 2023.10.9](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/2023-10-9) |  |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.31.4+rke2r1 |
| ArgoCD | v2.14.4 |
| Grafana | 11.1.0 |
| ceph | 19.2.0 |
| rook-ceph | 1.16.1 |
| prometheus-pushgateway | v3.0.0 |
| cert-manager | v1.17.1 |
| rancher-istio | 105.4.0-up1.23.2 |
| rancher-monitoring-crd | 105.1.3-up61.3.2 |
| rancher-gatekeeper | 104.0.1-up3.13.0 |
| rancher-monitoring | 105.1.3-up61.3.2 |
| longhorn | 1.7.3 |
| longhorn-crd | 1.1.100 |
| reloader | v2.0.0 |
| kube-logging/logging-operator | 5.2.0 |
| kube-logging/config-reloader | v0.0.7 |
| velero | 1.15.2 |
| csi-driver-smb | v1.16.0 |
| redis-operator | v7.8.4-9 |
| redis-cluster | v7.8.4-95.focal |
| oauth2-proxy | v7.8.1 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/full-migration).