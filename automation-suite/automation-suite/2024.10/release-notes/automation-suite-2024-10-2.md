---
title: "2024.10.2"
visible: true
slug: "automation-suite-2024-10-2"
---

**Release date: 17 February 2025**

## Support for new RHEL version

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

**Release date: September 24, 2025**

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

## New RHEL version supported

We have expanded our OS support to include RHEL 9.5. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

## New alert for Redis license expiration

We have added a new Prometheus alert for the expiration of internal Redis licenses. This alert has three notification levels, based on the timeframe the license is set to expire: 90, 30, or 7 days.

## Bug fixes

* We have fixed an issue causing a failure while uninstalling rook-ceph due to missing external object storage configuration. The error message was displayed even though the migration was successful. The behavior no longer occurs.
* We have fixed an issue causing the failure of agent node additions to existing clusters in offline environments. This issue occurred due to the nodes attempting to retrieve images from localhost, which led to failed prerequisite checks and the interruption of agent node initialization. Previously, you had to manually edit the `/etc/rancher/rke2/registries.yaml` file to add the registry URL.
* An issue was causing the infrastructure upgrade process to fail with an `infra upgrade to 1.31.4 failed cannot upgrade embedded infra 1.31.4 Running prerequisite checks on all nodes...\nerror: the server doesn't have a resource type \"plan\` error message. This issue occurred due to a missing server resource type. We have fixed the issue.
* We have fixed an issue causing `uipathctl` to not correctly set `executeMigration` to `true`. This issue occurred when migrating from Ceph in-cluster storage to an external object storage for AI Center.
* We have fixed an issue causing the update FQDN flow to fail due to a security configuration. The behavior no longer occurs.
* We have fixed an issue causing the RKE2 certificate rotation command to run on agent nodes, even though it is not supported. This issue occurred during the Automation Suite upgrade process. Now, the RKE2 certificate rotation command runs exclusively on the server nodes during the upgrade process.
* An issue prevented the addition of a server node in an offline environment with in-cluster registry. We have fixed the issue.
* We have fixed an issue that caused the proxy configuration to not work for AI Center due to unsupported CIDR notation and regular expressions (regex) in the `no_proxy` settings.
* We have fixed an issue caused by the `update_fqdn` parameter not being properly set in the `service-cluster-configurations` secret. As part of this fix, the `update_fqdn` flag is now being removed after updating the FQDN. We have also corrected the display message for running the `uipathctl rke update-fqdn` command.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/security-and-compliance).

### AI Center in-cluster proxy connectivity issue

**Erratum - added December 19, 2025:** An issue prevents AI Center pods from connecting to the in-cluster object store in proxy-enabled environments. This occurs due to unsupported CIDR notations and FQDN regex patterns in the `no_proxy` configuration.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/ai-center-in-cluster-proxy-issue) section.

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

### Kerberos keytab rotation does not trigger token regeneration

**Erratum - added September 24, 2025:** An issue causes Kerberos keytab rotation to not immediately regenerate authentication tokens, which may lead to temporary connectivity disruptions between services and the database.

To address the issue, you must manually trigger the Kerberos ticket renewal cronjob by running the following command:

```
kubectl delete job tgt-rotate-manual -n uipath --ignore-not-found ; kubectl create job tgt-rotate-manual --from=cronjob/kerberos-tgt-update -n uipath
```

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

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

### Temporary registry installation timeout

**Erratum - added September 24, 2025:** An issue causes the temporary registry installation to fail with a timeout error when connecting to `registry-1.docker.io`. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/unable-to-install-temporary-registry) section.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Thanos compactor stops on corrupted blocks

**Erratum - added September 24, 2025:** An issue causes the Thanos compactor to stop compacting metrics when it encounters corrupted blocks in the object store. This prevents compaction and leads to increased storage usage.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/failure-to-compact-metrics-due-to-corrupted-blocks-in-thanos) section.

We fixed the issue in [Automation Suite 2024.10.5](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-5#bug-fixes).

### Uploading large Document Understanding bundles causes node instability

**Erratum - added July 17, 2025:** An issue causes nodes to become unresponsive when uploading large Document Understanding offline bundles. The issue occurred due to image layers being loaded into memory in parallel, leading to high memory consumption and out-of-memory (OOM) errors.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/node-becomes-unresponsive-oom-during-large-document-understanding-bundle-upload) section.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-4#bug-fixes).

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

### Studio Web not accessible when using a proxy

**Erratum - added April 28, 2025:** If you are using a proxy environment and Studio Web is enabled, Studio Web is not accessible and throws a 404 error. As a workaround, you must add `studioweb-backend,studioweb-frontend,studioweb-typecache` to the `no_proxy` entry in the `input.json` file and rerun the installer.

This is fixed in Automation Suite [2024.10.3](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-3#bug-fixes).

### Health check failure in offline environments

**Erratum - added April 28, 2025:** An issue causes the `health check` command to fail in offline environments when parsing Istio image versions from registries containing two or more semicolons. However, you can disregard the error message as it results in a false positive.

We fixed the issue in [Automation Suite 2024.10.3](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-3#bug-fixes).

### Blocked upgrade on backup-restored cluster

**Erratum - added April 28, 2025:** An issue blocks the Automation Suite upgrade on a backup-restored cluster. For a successful upgrade, remove all labels from the service apps.

We fixed the issue in [Automation Suite 2024.10.3](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-3#bug-fixes).

### Incomplete Docker registry cleanup process

**Erratum - added April 28, 2025:** An issue prevents the registry cleanup command from effectively clearing the unused Docker images from all registry pods. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/how-to-clean-up-unused-docker-images-from-registry-pods) section.

We fixed the issue in [Automation Suite 2024.10.3](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-3#bug-fixes).

### Upgrade fails due to MongoDB to SQL Server migration

**Erratum - added April 28, 2025:** We have identified an issue impacting the side-by-side and the in-place upgrade of Automation Suite 2022.10 or earlier to Automation Suite 2024.10.0 or later. Due to a faulty migration from MongoDB to SQL Server, the upgrade operation fails if you have Apps enabled and use Kerberos authentication for the SQL Server database.

The recommended solution is to upgrade to [Automation Suite 2024.10.3](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-3#bug-fixes).

### Kube-proxy health check not working

**Erratum - added April 28, 2025:** The `node-monitor` component, which monitors the node for issues such as checking `kube-proxy` health or if `ip_forward` is enabled, and cordons the node if issues arise, is not working for specific nodes such as GPU, `task-mining`, or `as-robot`. We have fixed this issue in Automation Suite [2024.10.3](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-3#bug-fixes).

### Proxy and Kerberos pipelines not functioning correctly

**Erratum - added April 28, 2025:** Proxy and Kerberos pipelines are not functioning correctly, leading to authentication and support issues.

### Same requirement for enabling user and SQL authentication

**Erratum - added March 24, 2025**: The configuration of user authentication and SQL authentication for the Automation Suite cluster is interconnected. To use either of them, currently you must set both `kerberos_auth_config.enabled` and `kerberos_auth_config.enable_integrated_sql_auth` parameters to true.

### Upgrade fails due to Velero migration issue

**Erratum - added March 3, 2025**: An issue related to Velero migration causes the Automation Suite in-place upgrade to fail when the backup is enabled. The address the issue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/upgrade-fails-velero-migration-issue) section.

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

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.31.4+rke2r1 |
| ArgoCD | 2.13.3 |
| gatekeeper | 3.18.2 |
| rook | 1.16.1 |
| ceph | 19.2.0 |
| prometheus-pushgateway | 2.15.0 |
| cert-manager | 1.16.2 |
| kube-logging/logging-operator | 5.0.1 |
| kube-logging/config-reloader | 0.0.6 |
| istio | 1.24.2 |
| velero | 1.15.2 |
| reloader | 1.2.1 |
| Prometheus | 3.1.0 |
| Grafana | 11.4.0 |
| redis-operator | 7.8.2-6 |
| redis-cluster | 7.8.2-60 |
| oauth2-proxy | 7.8.1 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/full-migration).