---
title: "2024.10.3"
visible: true
slug: "automation-suite-2024-10-3"
---

**Release date: April 28, 2025**

## Support for new RHEL version

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

**Release date: September 24, 2025**

## Kerberos keytab rotation does not trigger token regeneration

**Erratum - added September 24, 2025:** An issue causes Kerberos keytab rotation to not immediately regenerate authentication tokens, which may lead to temporary connectivity disruptions between services and the database.

To address the issue, you must manually trigger the Kerberos ticket renewal cronjob by running the following command:

```
kubectl delete job tgt-rotate-manual -n uipath --ignore-not-found ; kubectl create job tgt-rotate-manual --from=cronjob/kerberos-tgt-update -n uipath
```

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

## Orchestrator does not start when using user-assigned managed identity

**Erratum - added September 24, 2025:** An issue prevents the `storage.useClientID` parameter from being set when you select a user-assigned managed identity for object storage. As a result, Orchestrator cannot start in environments where access is restricted to user-assigned managed identities.

To address the issue, you must manually set the parameter in ArgoCD, as follows:

1. In the ArgoCD Orchestrator application, go to **Details** &gt; **Parameters**.
2. In the **values** text box, set `storage.isExternal : true` and save.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

## Temporary registry installation timeout

**Erratum - added September 24, 2025:** An issue causes the temporary registry installation to fail with a timeout error when connecting to `registry-1.docker.io`. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/unable-to-install-temporary-registry) section.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

## Thanos compactor stops on corrupted blocks

**Erratum - added September 24, 2025:** An issue causes the Thanos compactor to stop compacting metrics when it encounters corrupted blocks in the object store. This prevents compaction and leads to increased storage usage.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/failure-to-compact-metrics-due-to-corrupted-blocks-in-thanos) section.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

## Generating the configuration file using a GUI-based wizard

Navigating through the intricacies of a platform configuration, involving multiple flags and parameters, can at times be a challenging experience. To simplify this, we bring you the Automation Suite Installer Wizard, a new method for generating the Automation Suite `cluster_config.json` configuration file.

This GUI-centric tool guides you through the key configuration steps, prompting you to provide details about your Automation Suite installation. It requires details such as the targeted platform, environment type, storage needs, SQL database specifics, and more, subsequently generating the `cluster_config.json` file for you.

For details, refer to [Generating the configuration file using a wizard](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/generating-the-configuration-file-using-wizard).

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

In case of an Automation Suite upgrade where Process Mining is enabled and Task Mining is not enabled, then the Dapr application will be automatically uninstalled.

## Additional custom CA certificate support

You can include any additional custom CA certificate by providing the `additonal_ca_certs` key with the external CA certificate path in the `cluster_config.json` file.

## Enhanced telemetry

Enhanced Automation Suite with a high-level summarized usage telemetry feature, provided guidance on viewing the generated XML file, and added telemetry sharing with UiPath Support via the Customer Portal.

## Istio HSTS enabled by default

To enhance security, Istio HSTS is now enabled by default.

## uipathctl improvements

* You can now list all the available options for the included and excluded flags when running the prerequisite checks command. For more details about `--list-options`, refer to the [uipathctl reference guide](https://docs.uipath.com/automation-suite/automation-suite/2024.10/reference-guide/uipathctl-prereq-run).
* For better eficiency, the diagnostic checks are no longer executed during the bundle creation process. Previously, a health check was performed by default during the support bundle creation, requiring the explicit use of the `--skip-diagnose` flag to bypass it. For more details on how to run the diagnostic checks, refer to the [uipathctl reference guide](https://docs.uipath.com/automation-suite/automation-suite/2024.10/reference-guide/uipathctl-health-diagnose).

## Bug fixes

* Resolved an issue where proxy and Kerberos-based pipelines were not functioning correctly in Automation Suite 2024.10.0, 2024.10.1, and 2024.10.2. This issue has been fixed, restoring proper support for proxy and Kerberos authentication in pipelines.
* An issue related to Velero migration caused the Automation Suite in-place upgrade to 2024.10.1 and 2024.10.2 to fail when the backup was enabled. We have fixed the issue.
* An issue was causing the `node-monitor` component, which monitors the node for issues such as checking `kube-proxy` health or if `ip_forward` is enabled, and cordons the node if issues arise, to not work for specific nodes such as GPU, `task-mining`, or `as-robot`. We have fixed the issue.
* Previously, the configuration of user authentication and SQL authentication for the Automation Suite cluster was interconnected. To use either of them, you had to set both `kerberos_auth_config.enabled` and `kerberos_auth_config.enable_integrated_sql_auth` parameters to true. Currently, we allow independent configuration of only user authentication by setting `kerberos_auth_config.enabled` to true and `kerberos_auth_config.enable_integrated_sql_auth` to false. Independent SQL authentication is still not supported.
* We have fixed an issue causing the side-by-side and the in-place upgrade of Automation Suite 2022.10 or earlier to Automation Suite 2024.10.0 or later to fail when Apps was enabled and you used Kerberos authentication for the SQL Server database.
* An issue was preventing the registry cleanup command from effectively clearing the unused Docker images from all registry pods. We have fixed the issue.
* We have fixed an issue that blocked the Automation Suite upgrade on a backup-restored cluster.
* We have resolved an issue causing the `health check` command to fail in offline environments. The issue occurred due to the incorrect parsing of Istio image versions from registries containing two or more semicolons.
* We have fixed an issue that was causing Studio Web to throw a 404 error when using a proxy environment.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/security-and-compliance).

### AI Center in-cluster proxy connectivity issue

**Erratum - added December 19, 2025:** An issue prevents AI Center pods from connecting to the in-cluster object store in proxy-enabled environments. This occurs due to unsupported CIDR notations and FQDN regex patterns in the `no_proxy` configuration.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/ai-center-in-cluster-proxy-issue) section.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Prerequisite checks fail when Process Mining is enabled

**Erratum - added December 19, 2025:** An issue causes the prerequisite checks to fail when Process Mining is enabled. The issue occurs due to the checks still requiring `cert-manager`, although `cert-manager` is no longer needed for Process Mining starting with Automation Suite 2024.10.3.

The failure message is a false positive and can be safely ignored.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Pre-upgrade command fails with proxy and external objectstore

**Erratum - added December 19, 2025:** An issue prevents the `uipathctl cluster pre-upgrade` command from completing successfully in environments configured with a proxy and external objectstore. The issue occurs due to an error during the Insights volume migration process.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Upgrade failure during posthook import in chained upgrades

**Erratum - added December 19, 2025:** An issue causes the upgrade to fail during the execution of the `uipathctl rke2 upgrade` command in chained upgrade scenarios. This issue occurs due to the posthook secret and configmap import operation not being idempotent, which leads to conflicts with existing Kubernetes objects.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/upgrade-failure-during-posthook-import) section.

We fixed the issue in [Automation Suite 2024.10.7](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-7#bug-fixes).

### Backup operations fail with PartiallyFailed status

**Erratum - added December 19, 2025:** An issue causes backup operations to fail with a `PartiallyFailed` status when the objectstore is in-cluster (rook-ceph).

The backup logs show errors similar to following example:

```
ERROR: insights/app/workdir/2025-10-01-04/.config/chromium/Crash Reports/settings.dat: Failed to copy: failed to open source object: operation error S3: GetObject, https response error StatusCode: 404
```

You can view the backup logs by running the following command:

```
./bin/velero backup logs <backup name>
```

To address the issue you must contact UiPath Support.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-4#bug-fixes).

### Registry certificates not fully updated in offline scenarios

**Erratum - added September 24, 2025:** An issue causes the `uipathctl config tls-certificates` command to update only the internal certificate, while missing the certificate required by Argo CD to trust the in-cluster registry in offline scenarios.

To address the issue, you must run the following command to explicitly update the ArgoCD registry certificate in internal–external registry scenarios:

```
./bin/uipathctl config argocd ca-certificates update --cacert [PATH]
```

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Uploading large Document Understanding bundles causes node instability

**Erratum - added July 17, 2025:** An issue causes nodes to become unresponsive when uploading large Document Understanding offline bundles. The issue occurred due to image layers being loaded into memory in parallel, leading to high memory consumption and out-of-memory (OOM) errors.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/node-becomes-unresponsive-oom-during-large-document-understanding-bundle-upload) section.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-4#bug-fixes).

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

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Orchestrator does not start when using user-assigned managed identity

**Erratum - added September 24, 2025:** An issue prevents the `storage.useClientID` parameter from being set when you select a user-assigned managed identity for object storage. As a result, Orchestrator cannot start in environments where access is restricted to user-assigned managed identities.

To address the issue, you must manually set the parameter in ArgoCD, as follows:

1. In the ArgoCD Orchestrator application, go to **Details** &gt; **Parameters**.
2. In the **values** text box, set `storage.isExternal : true` and save.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Task Mining Kerberos initialization failure

**Erratum - added June 26, 2025:** An issue causes the Task Mining service to fail to initialize in Kerberos environments. This issue occurs when the `kerberos-discoverygroup-user-keytab` secret is missing or when the `discoverygroup` app is not included in the `enabledApps` parameter of the `IntegratedAuth` app.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/task-mining-initialization-issue-in-kerberos) section.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-4#bug-fixes).

### Agent node addition failure in offline environments

**Erratum - added June 26, 2025:** An issue causes the addition process of agent nodes in offline environments to fail. Agent node additions require the temporary registry to be running. To address the issue, you must re-enable the temporary registry to successfully join the agent node.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-4#bug-fixes).

### Frequent restarts in uipath namespace due to secret mismatch

**Erratum - added June 26, 2025:** An issue causes frequent restarts of deployments in the `uipath` namespace due to inconsistent `istio-ingressgateway-certs` secrets between the `istio-system` and `docker-registry` namespaces.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/frequent-restart-issue-in-uipath-namespace-deployments-during-offline-installations) section.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-4#bug-fixes).

### Log streaming does not work in proxy setups

**Erratum - added June 26, 2025:** Log forwarding does not work in proxy setups because the proxy environment variables were not set in the logging pods. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/log-streaming-does-not-work-in-proxy-setups) section.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-4#bug-fixes).

### Installation fails due to CA certificates with large policy OIDs

**Erratum - added June 26, 2025**: An issue causes the Automation Suite installation to fail when using Certificate Authority (CA) certificates that include a `CertificatePolicies` section with policy OID values exceeding 4 bytes. This issue prevents Automation Suite from recognizing these CA certificates, interrupting the installation process.

To address the issue, you must either ensure that the policy OID values within the `CertificatePolicies` section do not exceed 4 bytes, or avoid using CA generators that add the `CertificatePolicies` section to the certificates.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-4#bug-fixes).

### Process Mining portal fails to load

**Erratum - added June 26, 2025**: After upgrading from Process Mining in Automation Suite 2024.10.2 to 2024.10.3, the Process Mining portal may fail to load the process apps. An HTTP Error (400) error message is displayed when attemptimg to access the Process Mining portal.

The issue can occur when `VersionSetJson` is set to

```
{
    "Main": "6.13.0", 
    "Extra": ["6.17.0"]
}
```

in the `DetailsJson` in the Process Mining `AutomationSuite_ProcessMining_Metadata` database, which breaks JSON serialization for the `SemVersion` object.

To solve the issue, execute the query that replaces `"Extra": ["6.17.0"]` with `"Extra": []` in `DetailsJson` field in `Ingestions` table.

:::important
You need to have write access to the Process Mining `AutomationSuite_ProcessMining_Metadata` production database.
:::
We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-4#bug-fixes).

### Licensing SQL connection error

**Erratum - added June 26, 2025:** Licensing SQL connection errors occur when the Data Source property specified both a named instance and a port.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-4#bug-fixes).

### Service disruptions due to automatic secret rotation

**Erratum - added June 26, 2025**: To address this issue, you can edit the `cluster_config.json` file to disable secret rotation in the platform configuration. This change will persist through Automation Suite upgrades and reinstalls.

Take the following steps:

1. Update the `platform` section in the `cluster_config.json` file as shown in the following example:
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
   ./bin/uipathctl manifest apply /opt/UiPathAutomationSuite/cluster_config.json --versions ./versions/helm-charts.json
   ```

**Erratum - added May 14, 2025**: An issue causes service disruptions due to the automatic secret rotation, making services temporarily inaccessible.

To address this issue, take the following steps:

1. Restart the affected service to restore its normal functionality.
2. Navigate to the ArgoCD UI and from the platform applicatio, select **Details** &gt; **Parameters**. Edit the values to add `"secretRotation: enabled: false"` under `identity-service`. You must take this step after each Automation Suite upgrade or reinstallation.

For AI Center, all skills must be stopped and started from AI Center UI.

### Garbage collection fails during registry cleanup

**Erratum - added September 24, 2025:** An issue prevents garbage collection from executing correctly during in-cluster registry cleanup. This may result in unused images not being cleaned up as expected.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/how-to-clean-up-unused-docker-images-from-registry-pods) section.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

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

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.31.4+rke2r1 |
| ArgoCD | v2.14.4 |
| gatekeeper | 3.18.2 |
| rook | 1.16.1 |
| ceph | 19.2.0 |
| prometheus-pushgateway | v3.0.0 |
| cert-manager | v1.17.1 |
| kube-logging/logging-operator | 5.2.0 |
| kube-logging/config-reloader | v0.0.7 |
| istio | 1.25.0 |
| velero | 1.15.2 |
| reloader | v2.0.0 |
| Prometheus | v3.2.1 |
| Grafana | 11.5.2 |
| redis-operator | v7.8.4-9 |
| redis-cluster | v7.8.4-95.focal |
| oauth2-proxy | v7.8.1 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/full-migration).