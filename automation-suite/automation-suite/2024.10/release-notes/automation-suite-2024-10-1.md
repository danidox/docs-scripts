---
title: "2024.10.1"
visible: true
slug: "automation-suite-2024-10-1"
---

**Release date: December 18, 2024**

## Support for new RHEL version

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

**Release date: September 24, 2025**

## Support for full migration

Full migration is now supported in Automation Suite 2024.10.1.

Compared to the full migration steps in Automation Suite 2023.10, in this version there is an additional migration step in which you can update the schema of the Insights and Orchestrator databases after previously restoring them.

Also, we implemented the following improvements in the `UiPath.OrganizationMigrationApp` tool:

* We provide an inner exception during a database connection test for enhanced error logging and debugging.
* We improved the merging process of single sign-on users (SSO) from multiple organizations to handle database conflicts more efficiently. The update also provides accurate migration success messages and prevents potential data duplication. This enhancement significantly benefits organizations utilizing the MSI to Automation Suite setup with a multi-tenant configuration and SSO.

For more details, refer to [Performing a full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/full-migration).

**Release date: December 18, 2024**

## New flags for enhanced Kerberos authentication

We have introduced new configuration flags to give you more control over the Kerberos authentication. You can now use the following flags to customize the Kerberos authentication settings:

* `kerberos_auth_config.enable_integrated_sql_auth`: This flag allows you to decouple the Kerberos authentication from the SQL authentication login, and to enable or disable Kerberos authentication for SQL across all your products.
* `<serviceGroupName>.kerberos_auth_config.enabled`: This flag allows you to control the use of Kerberos authentication for SQL authentication at product level. You must replace `<serviceGroupName>` with the name of your product.

These new flags bring changes to the priority order for SQL Kerberos authentication, as follows:

1. Kerberos authentication for SQL is enabled by default when Kerberos authentication is enabled.
2. If you set `kerberos_auth_config.enable_integrated_sql_auth` to `false`, Kerberos authentication for SQL is disabled across all your products.
3. If you set `<serviceGroupName>.kerberos_auth_config.enabled` to `false`, Kerberos SQL authentication is disabled for the specified product.

For more details on Kerberos authentication, see [Setting up Kerberos authentication](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/setting-up-kerberos-authentication).

## New prerequisite checks

We have introduced more prerequisite checks to optimize the overall experience of installing and configuring Automation Suite and to catch missing requirements earlier. Here are some highlights:

* A new validation check ensures that the `READ_COMMITTED_SNAPSHOT` option is enabled in the SQL Server database. We have implemented this check validation for Orchestrator, Apps, and Process Mining.
* We have introduced a prerequisite check in the `mirror-registry.sh` and `hydrate-registry.sh` scripts to validate the OCI compliance of the external registry before uploading images.

## Security enhancements

We continue to provide security updates and patches to address Common Vulnerabilities and Exposures (CVEs).

## Support added for Document Understanding modern projects

Document Understanding modern projects are now supported in Automation Suite on Linux for offline deployments.

## Bug fixes

* We have fixed an Automation Suite installation issue that occurred when using an SQL Server version prior to 2019.
* We have fixed an issue that caused Insights data loss when you reinstalled or upgraded Insights following an Automation Suite upgrade from version 2023.4 or older.
* We have fixed an issue causing the temporary registry installation to fail for RHEL 8.9. This issue occured due to the deprecated `systemd generate` command in the upstream Podman and the absence of `secontext` in Podman-generated `systemd` files.
* An issue was causing the Helm chart build to fail when the `enableSqlIntegratedAuth` parameter was set to `true` in `values.yaml` for Kerberos SQL integration. This issue occured to due incorrect indentation of certain environment variables. We have fixed the issue.
* We fixed an issue causing Automation Hub to become inaccessible after an upgrade to Automation Suite 2024.10.
* We fixed an Insights annotation issue that would block the Automation Suite installer.
* We fixed an issue causing a partial failure to restore a backup due to a Dapr sync issue.
* We have fixed an issue causing the prerequisite checks to identify hostnames with capital letters as invalid. This behavior no longer occurs. Hostnames are now validated correctly regardless of letter capitalization.
* We have fixed an issue causing the `aicenter skill sync` and `aicenter skill status` commands to fail during a side-by-side upgrade. This issue occurred due to a syntax error.
* An issue was preventing `exclude=rke2-*` from being automatically added to the `/etc/yum.conf` file on all nodes. This issue occurred particularly in online environments and caused an unintentional upgrade of the RKE2 service on nodes other than the first server. Previously, you had to manually add the exception to the `/etc/yum.conf` on all nodes. We have fixed the issue.
* An issue was causing the node removal operation to fail with an `error: no objects passed to scale` message. This issue occurred due to a name mismatch during the scaling up of the Prometheus operator. We have fixed the issue.
* You can now use custom directories for storing your pod logs. Previously, this function was unavailable due to the switch to `kube-logging`.
* We have fixed an issue that occurred in non-HA Redis scenarios, where the `redis-cluster-0` pod could get stuck in a terminating state during node drain operations. This behavior no longer occurs.
* When using style attributes in the HTML tags while customizing your **Login** page, they reflected accurately in the preview. However, upon saving the changes, the style attributes were deleted automatically. Now, all style attributes used within tags persist after saving your changes.
* We have fixed an issue causing the upgrade to fail due to the overriding of existing Insights PVC sizes.
* An issue was causing installation or upgrade failures when enabling Connaisseur during the configuration of an external OCI-compliant registry. This issue occurred when the `registries.trust.enabled` parameter was set to `true` in the `cluster_config.json` file. We have fixed the issue.
* We fixed a bug that was breaking SAML2 when basic authentication was disabled, along with various other bugs.
* You can now forward logs to external tools, such as Splunk, using the OpenTelemetry Collector. Previously, this function was unavailable due to the switch to `kube-logging`.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/security-and-compliance).

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

**Erratum - added May 14, 2025**: An issue causes service disruptions due to the automatic secret rotation, making services temporarily inaccessible.

To address this issue, take the following steps:

1. Restart the affected service to restore its normal functionality.
2. Navigate to the ArgoCD UI and from the platform applicatio, select **Details** &gt; **Parameters**. Edit the values to add `"secretRotation: enabled: false"` under `identity-service`. You must take this step after each Automation Suite upgrade or reinstallation.

For AI Center, all skills must be stopped and started from AI Center UI.

### Studio Web not accessible when using a proxy

**Erratum - added April 28, 2025:** If you are using a proxy environment and Studio Web is enabled, Studio Web is not accessible and throws a 404 error. As a workaround, you must add `studioweb-backend,studioweb-frontend,studioweb-typecache` to the `no_proxy` entry in the `input.json` file and rerun the installer.

This is fixed in Automation Suite [2024.10.3](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-3#bug-fixes).

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

### Upgrade failure due to upgrade-journal configmap

**Erratum - added February 17, 2025**: An issue affecting the upgrade-journal configmap causes the upgrade from Automation Suite 2024.10.0 to Automation Suite 2024.10.1 to fail. The address the issue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/failure-to-upgrade-to-automation-suite-2024101) section.

### Infrastructure upgrade failure due to missing server resource type

**Erratum - added February 17, 2025**: An issue causes the infrastucture upgrade process to fail with an `infra upgrade to 1.31.4 failed cannot upgrade embedded infra 1.31.4 Running prerequisite checks on all nodes...\nerror: the server doesn't have a resource type \"plan\` error message. This issue occures due to a missing server resource type.

To fix this issue, you must restart the `system-upgrade-controller` deployment in the `system-upgrade` namespace using the following command:

```
kubectl rollout restart deployment system-upgrade-controller -n system-upgrade
```

Once the restart has been successfully completed, you can re-trigger the infrastructure upgrade process.

This issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-2#bug-fixes).

### Error message while uninstalling rook-ceph post migrating to a S3 object-store

**Erratum - added February 17, 2025**: When uninstalling rook-ceph, an error message related to missing external object storage configuration is displayed. This issue occurs even though the migration is succesful. This behavior is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-2#bug-fixes).

### AI Center storage migration failure

**Erratum - added February 17, 2025**: An issue prevents `uipathctl` from correctly setting `executeMigration` to `true` during the migration process from Ceph in-cluster storage to external object storage in AI Center.

To fix this issue, you must manually set `executeMigration` to `true` in ArgoCD for AI Center and then proceed with a resync, ensuring to prune. This issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-2#bug-fixes).

### FQDN update failure due to security configuration

**Erratum - added February 17, 2025**: An issue causes the FQDN update flow to fail due to a security configuration.

To address this issue, you must use the `uipathctl` version included in Automation Suite 2024.10.2 when you update the FQDN at the infrastructure level. To download `uipathctl`, see [Installation packages download links](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/installation-packages-download-links#uipathctl).

This issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-2#bug-fixes).

### RKE2 certificate rotation command issue on agent nodes

**Erratum - added February 17, 2025**: An issue causes the RKE2 certificate rotation command to run on the agent nodes even though it is not supported. This issue occurs during the Automation Suite upgrade process.

To address this issue, you must manually edit `infra-installer.sh` and replace the `rke2 certificate rotate` command with `[[ ${NODE_ROLE} != "agent" ]] && rke2 certificate rotate` to exclude the agent nodes.

This issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-2#bug-fixes).

### In-cluster registry node addition failure in offline environment

**Erratum - added February 17, 2025**: An issue prevents the addition of a server node in offline environments with an in-cluster registry.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/server-node-joining-issue-in-offline-environments-with-in-cluster-registry) section.

This issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-2#bug-fixes).

### FQDN update failure

**Erratum - added February 17, 2025**: An issue causes the FQDN update to fail due to the `update_fqdn` parameter to not being properly set in the `service-cluster-configurations` secret.

To address this issue, you must manually remove the `update_fqdn` and `update_fqdn_state` parameters and update the `service-cluster-configurations` secret using the following command:

```
kubectl patch secret service-cluster-configurations -n uipath-infra --type=json -p='[
    {"op": "remove", "path": "/data/UPDATE_FQDN"},
    {"op": "remove", "path": "/data/UPDATE_FQDN_STATE"}
    ]'
```

This issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-2#bug-fixes).

### Full migration from standalone products to Automation Suite not supported

You cannot currently perform a full migration from standalone products version 2024.10 to Automation Suite 2024.10 using the UiPath.OrganizationMigrationApp tool. We are actively working on introducing support for this scenario.

In the meantime, you can perform a single-tenant migration. For details on this migration option, refer to [Single tenant migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-openshift/using-the-migration-tool).

### Migration from Automation Suite on Linux to Automation Suite on OpenShift not supported

You cannot currently perform a migration from Automation Suite on Linux to Automation Suite on OpenShift. We are actively working on introducing support for this scenario.

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

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.30.5+rke2r1 |
| ArgoCD | 2.12.6 |
| gatekeeper | 3.17.1 |
| rook | 1.14.6 |
| ceph | 17.2.6 |
| prometheus-pushgateway | 1.10.0 |
| cert-manager | 1.16.1 |
| kube-logging/logging-operator | 4.9.1 |
| config-reloader | v0.0.5 |
| reloader | 1.0.95 |
| velero | 1.14.1 |
| Prometheus | 2.55.1 |
| Grafana | 11.3.0 |
| velero | 1.14.1 |
| redis-operator | 7.4.6-2 |
| redis-cluster | 7.4.6-102 |
| oauth2-proxy | 7.7.1 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/full-migration).