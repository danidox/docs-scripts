---
title: "2023.10.6"
visible: true
slug: "automation-suite-2023-10-6"
---

**Release date: October 17, 2024**

## Support for new RHEL version

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

**Release date: September 24, 2025**

## New RHEL version supported

We have expanded our OS support to include RHEL 9.4.

## Instance Metadata Service Version 2 support

We now support Instance Metadata Service Version 2 (IMDSv2) in high-availability deployments for AWS. For more information on IMDSv2, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html).

## New kube-proxy check

We have implemented a new kube-proxy check in the Node Monitor. If kube-proxy becomes functionally unavailable due to issues such as an iptable flush, the Node Monitor will cordon the node. Once kube-proxy functions correctly again, the node will be uncordoned.

## Improved migration to Automation Suite

We made the following improvements to the migration workflows:

* When moving the Identity data of your tenants from standalone Orchestrator to Automation Suite, the tenant name in Automation Suite is now the same as the original tenant name in standalone Orchestrator. Previously, the Automation Suite tenant name was automatically generated in the `tenant_xxxxxxxx` format, where `xxxxxxxx` signified the first eight characters of the Automation Suite organization ID. For more information, see [Step 1: Moving the Identity organization data from standalone to Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/moving-the-identity-organization-data-from-standalone-to-automation-suite)
* We updated our documentation of the migration steps to clarify that you have the option to migrate multiple standalone product tenants to either a single Automation Suite organization or multiple Automation Suite organizations. For more information, see [Step 1: Moving the Identity organization data from standalone to Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/moving-the-identity-organization-data-from-standalone-to-automation-suite) and [Step 4: Merging organizations in Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/merging-organizations-in-automation-suite).

## FQDN update enhancement

We are thrilled to announce an enhancement in our Fully Qualified Domain Name (FQDN) update process. Now, you can update the cluster FQDN from a single machine, replacing the previous multi-step procedure. This update is aimed at simplifying the process, making it more user-friendly and efficient.

For more on the FQDN update process, see [Configuring the FQDN post-installation.](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/configuring-the-fqdn-post-installation)

## Bug fixes

* **Erratum - added May 21, 2025**: For offline Automation Suite installations using the external docker registry, the [uipathctl health check command](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/running-the-diagnostics-tool#health-check) did not work in Automation Suite versions 2023.10.0 to 2023.10.5 due to a known issue. This issue has been fixed.
* If you resized the `rook-ceph` OSD PV, the new size did not persist following an Automation Suite upgrade. Now, the upgrade automatically inherits and retains the updated `rook-ceph` OSD PV size.
* We fixed an issue where the installation or upgrade failed on AWS machines where only IMDSv2 was enabled.
* We have fixed an issue causing Automation Suite upgrades to fail due to the presence of failed jobs in the `system-upgrade` namespace.
* In a proxy environment, if the proxy server used the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods could not communicate with the FQDN, and an error message was displayed. The behavior no longer occurs.
  :::note
  If you previously created a service entry according to the workaround in [Pods cannot communicate with FQDN in a proxy environment](https://docs.uipath.com/automation-suite/automation-suite/2023.10/pods-cannot-communicate-with-fqdn-via-proxy), we recommend that you delete the service entry after you upgrade to Automation Suite 2023.10.6 or later. To delete the service entry, use the following command: assignment
  ```
  kubectl delete serviceentry proxy -n uipath
  ```
  :::
* We have fixed a `uipathctl`-related issue that caused registry configuration corruption during upgrades. Previously, a port in the helm URL of `cluster_config.json` was treated as an external registry, leading to an omission in `registries.yaml`. Now,`insecure_skip_verify: true` is correctly included in`registries.yaml`, regardless of whether or not a port is present in the helm URL.
* We fixed several bugs that caused issues during setup when AI Center was connected to an external Orchestrator and Identity Service, in the following situations:
  + During the installation of Orchestrator certificates for trusted communication.
  + When setting up an Identity Service client for Document Manager.
  + When configuring an Identity Service client for metering services.
* We have fixed an issue where shutting down the `rke2-server` service without executing `rke2-killall.sh` could lead to intermittent not ready reports from agent machines.
* We have fixed an issue that caused problems during the upgrade process if you had resized the Docker-registry PVC used by your in-cluster Docker registry. Now, the new size is accurately recognized and considered during the upgrade process.
* We have fixed an issue causing Redis recovery job failures when the ArgoCD admin password gets updated in the UI without also updating the Kubernetes secrets. The fix includes special handling for this scenario. We recommend to update the Kubernetes secrets at the same time when you update the ArgoCD admin password in the UI to avoid any other unexpected issues. For more details on how to properly update the ArgoCD admin password, refer to [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/12001#solution).

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

### Grafana dashboard error

**Erratum - added June 10, 2025:** In multi-node (HA) setups, Grafana runs with two replicas, but there is no common data source between the replicas, causing issues in user session management. Errors like `Dashboard not found` and `Invalid dashboard UID in the request` appear in the Grafana dashboard.

As a workaround, since Grafana is not a critical application, you can reduce the replica count to one by performing the following steps:

1. Modify the helm parameter for the `fabric-installer` application. This automatically triggers the sync operation for `fabric-installer` application.
   ```
   kubectl patch   application fabric-installer -n argocd    --type='json'  -p='[{"op": "add", "path": "/spec/source/helm/parameters/-", "value": {"name": "global.rancherMonitoring.grafana.replicas", "value": "1"}}]'
   ```
2. Sync the `rancher-monitoring` application from ArgoCD UI.

We have fixed this issue in Automation Suite [2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

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

### Side-by-side upgrade failure when Apps is enabled

**Erratum - added December 18, 2024**: In an offline environment, performing a side-by-side upgrade to Automation Suite 2023.10.6 results in a failure if Apps is enabled. The issue occurs due to a version discrepancy affecting the `business-apps/ba-migration-k8-utils` image.

To address the problem, update the existing version for the `business-apps/ba-migration-k8-utils` image in the `versions.json` file from 2023.10.4 to 2023.10.6 before running the migration command.

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Data loss when reinstalling or upgrading Insights following Automation Suite upgrade

**Erratum - added December 18, 2024:** Following an Automation Suite upgrade from version 2023.4 or older, reinstalling or upgrading Insights results in data loss due to an issue with Insights storage class changes. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/data-loss-when-reinstalling-or-upgrading-insights-following-automation-suite-upgrade).

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Node maintenance issue in non-HA Redis

**Erratum - added December 18, 2024**: An issue causes the `redis-cluster-0` pod to get stuck in the terminating state when you perform a node drain in non-HA Redis scenarios. To address the problem, you must force delete the pod using the following command:
```
kubectl -n redis-system delete pod redis-cluster-0 --force
```

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Insights annotation issue blocks installer

**Erratum - added December 18, 2024**: An Insights annotation issue blocks the Automation Suite installer. We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### RKE2 log collector runs indefinitely

**Erratum - added December 18, 2024**: The RKE2 log collector runs indefinitely for some system commands. We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Upgrade failure due to overridden Insights PVC sizes

**Erratum - added December 18, 2024:** An issue causes upgrades to fail when the existing Insights PVC sizes are inadvertently overridden. To address this problem, you must manually change the PVC sizes in ArgoCD UI. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/upgrade-fails-due-to-overridden-insights-pvc-sizes) section.

This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### AI Center skills sync failure during side-by-side upgrade

**Erratum - added December 18, 2024:** A syntax issue causes the failure of the `aicenter skill sync` and `aicenter skill status` commands during a side-by-side upgrade.

To fix this issue, you must manually edit the syntax. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/ai-center-skills-sync-failure-during-side-by-side-upgrade) section.

### Unnecessary Redis DNS resolution validations during Active/Passive checks

**Erratum - added December 18, 2024**: An issue causes unnecessary Redis DNS resolution validations for `redis.<primary-fqdn>` and `redis-db.<primary-fqdn>` during Active/Passive prerequisite checks. This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Unintended RKE2 service upgrade on additional nodes

**Erratum - added November 26, 2024**: We have identified an issue where `exclude= rke2-*` is not added to the `/etc/yum.conf` file on nodes other than the first server. In specific environments, particularly online ones, an attempt to upgrade all components can cause an unintentional upgrade of the RKE2 service on nodes other than the first server.

To fix this issue, you must manually add `exclude=rke2-*` to the `/etc/yum.conf` file on all the nodes of your Automation Suite cluster.

### Test Automation SQL connection string is ignored

**Erratum - added October 17, 2024**: When you provide an SQL connection string under the `orchestrator.testautomation` section of the `cluster_config.json` file, the `uipathctl` binary ignores the connection string and uses the one under the `orchestrator` section instead. To address the problem, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/test-automation-sql-connection-string-is-ignored) section.

### Longhorn REST API endpoint upgrade/reinstall error

An issue causes a `Failed to set Longhorn RestApi Endpoint` error when you upgrade (reinstall) the cluster from a version earlier than Automation Suite 23.10.0.

To fix the issue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/longhorn-rest-api-endpoint-upgradereinstall-error) section.

### Enabling Connaisseur causes installation or upgrade failures

An issue causes installation or upgrade failures when enabling Connaisseur during the configuration of an external OCI-compliant registry. The issue occurs when you set the `registries.trust.enabled` parameter to `true` in the `cluster_config.json` file.

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

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.30.5 |
| ArgoCD | 2.11.3 |
| gatekeeper | 3.16.0 |
| rook-ceph | 1.14.6 |
| prometheus-pushgateway | 2.12.0 |
| cert-manager | 1.14.5 |
| rancher-istio | 104.4.0-up1.22.1 |
| rancher-logging | 103.0.0-up3.17.10 |
| rancher-logging-crd | 103.0.0-up3.17.10 |
| rancher-monitoring-crd | 104.1.0-up57.0.3 |
| rancher-gatekeeper-crd | 103.1.0-up3.13.0 |
| rancher-gatekeeper | 103.1.0-up3.13.0 |
| rancher-monitoring | 104.1.0-up57.0.3 |
| longhorn | 1.6.2 |
| longhorn-crd | 1.1.100 |
| reloader | 1.0.95 |
| csi-driver-smb | 1.16.0 |
| velero | 6.2.0 |
| redis-operator | 7.4.6-2 |
| redis-cluster | 7.4.6-22 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/full-migration).