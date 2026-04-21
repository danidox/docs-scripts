---
title: "2023.10.5"
visible: true
slug: "automation-suite-2023-10-5"
---

**Release date: August 14, 2024**

## New RHEL versions support

We have expanded our OS support to include RHEL 8.10 and 9.2, alongside existing support for 8.6, 8.8, and 8.9 versions.

## AWS Signature Version 4 support

Automation Suite now uses AWS Signature Version 4 for all S3 API requests. This impacts the use of Automation Suite with S3 servers that do not support AWS Signature Version 4.

## Optimized AI Center disk management

We have improved the `configureUiPathDisks.sh` script capabilities to give you more flexibility when managing AI Center storage. With this improvement, you can use the `--aicenter-disk-name` parameter to increase AI Center storage, whether you add a new disk or expand an existing one.

For more details, see [Configuring the AI Center disk on selected machines](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/configuring-the-disks#configuring-the-ai-center-disk-on-selected-machines).

## Images cleanup for in-cluster Docker registry

You can now effortlessly remove obsolete images post-upgrade. This capability is specifically designed for offline setups with an in-cluster Docker registry. For more details, see [Performing post-upgrade operations](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/performing-post-upgrade-operations).

## Security enhancements

We continue to provide security updates and patches to address Common Vulnerabilities and Exposures (CVEs).

## Bug fixes

* **Erratum - added February 27, 2025**: We have fixed several bugs in AI Center when connected to an external Orchestrator and Identity Service. These bugs were specifically causing issues during setup in the following situations:
  + During the installation of Orchestrator certificates for trusted communication.
  + When setting up an Identity Service client for Document Manager.
  + When configuring an Identity Service client for metering services.
* We have fixed an issue causing upgrades from Automation Suite 2023.10.x to fail due to the Longhorn storage classes still being present after uninstalling Longhorn.
* For AI Center and Task Mining, the `ListBucket API` prerequisite check failed when using an external objectstore. However, AI Center and Task Mining do not use the `ListBucket API` permission. We have removed the unnecessary check.
* We have fixed an issue that prevented you from enabling SSO for ArgoCD due to a Dex image version discrepancy.
* We have addressed some issues in Apps, including certain operations failing in proxy environments and the legacy image control continuing to show a spinner after loading has completed.
* We have addressed an issue preventing some document validation tasks from being displayed accurately in Action Center.
* We have fixed an issue causing installation failures in certain conditions due to telemetry check errors. Previously, in case of failure, you had to manually set the telemetry check as optional and restart the installation. Now, a telemetry check failure only displays a warning and does not disrupt the installation process. This makes telemetry checks optional by default and ensures smooth, uninterrupted installations.
* We have fixed an issue causing the `snapshot-controller-crds` pod to remain in the CrashLoopBackOff state after an RKE2 upgrade. This issue occurred due to a conflict between the newly installed `snapshot-controller` and the existing one during the RKE2 upgrade.
* We have fixed an issue that caused the support bundle to not include historical logs and to not upload to the configured external object store. This issue occured in offline environments using an external OCI registry.
* In instances with host level SAML configured, when you accessed Automation Suite through a specific &lt;Automation_Suite_URL&gt;/&lt;Organization_name&gt; URL and selected the host level SAML login option, the ACS URL was incorrectly generated using the organization ID from the URL, instead of the expected host level ACS URL. We have fixed this. The system now correctly generates the host-level ACS URL during a host level SAML login, irrespective of the specific organization URL used to access Automation Suite.
* Previously, you could not save your SMTP settings without providing a username and password, even though these details were optional. This behavior no longer occurs.

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

### uipathctl health check command

**Erratum - added May 21, 2025:** For offline Automation Suite installations using the external docker registry, the [uipathctl health check command](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/running-the-diagnostics-tool#health-check) does not work due to a known issue. This issue has been fixed in [Automation Suite 2023.10.6](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-6#bug-fixes).

As a workaround, you can download the uipathctl binary from Automation Suite 2023.10.6 and use it to run the uipathctl health check command.

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

### ML skill deployment failure due to token expiry

**Erratum - added February 13, 2025:** Due to a `containerd` issue, the deployment of ML skills fails as a token expires before larger image downloads can be completed, especially under conditions of slower network connectivity.

To address this isssue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/failed-ml-skill-deployment-due-to-token-expiry) section.

### Email alerts configuration failure post upgrade

**Erratum - added February 13, 2025**: An issue affects the functionality of email alerts configuration and the setup of multiple receivers after upgrading from Automation Suite 2022.10. To address this issue, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/failure-to-configure-email-alerts-post-upgrade).

This issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-8#bug-fixes).

### Data loss when reinstalling or upgrading Insights following Automation Suite upgrade

**Erratum - added December 18, 2024:** Following an Automation Suite upgrade from version 2023.4 or older, reinstalling or upgrading Insights results in data loss due to an issue with Insights storage class changes. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/data-loss-when-reinstalling-or-upgrading-insights-following-automation-suite-upgrade).

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Insights annotation issue blocks installer

**Erratum - added December 18, 2024**: An Insights annotation issue blocks the Automation Suite installer. We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Node maintenance issue in non-HA Redis

**Erratum - added December 18, 2024**: An issue causes the `redis-cluster-0` pod to get stuck in the terminating state when you perform a node drain in non-HA Redis scenarios. To address the problem, you must force delete the pod using the following command:
```
kubectl -n redis-system delete pod redis-cluster-0 --force
```

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### RKE2 log collector runs indefinitely

**Erratum - added December 18, 2024**: The RKE2 log collector runs indefinitely for some system commands. We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### AI Center skills sync failure during side-by-side upgrade

**Erratum - added December 18, 2024:** A syntax issue causes the failure of the `aicenter skill sync` and `aicenter skill status` commands during a side-by-side upgrade.

To fix this issue, you must manually edit the syntax. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/ai-center-skills-sync-failure-during-side-by-side-upgrade) section.

### Unnecessary Redis DNS resolution validations during Active/Passive checks

**Erratum - added December 18, 2024**: An issue causes unnecessary Redis DNS resolution validations for `redis.<primary-fqdn>` and `redis-db.<primary-fqdn>` during Active/Passive prerequisite checks. This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Upgrade failure due to overridden Insights PVC sizes

**Erratum - added December 18, 2024:** An issue causes upgrades to fail when the existing Insights PVC sizes are inadvertently overridden. To address this problem, you must manually change the PVC sizes in ArgoCD UI. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/upgrade-fails-due-to-overridden-insights-pvc-sizes) section.

This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Unintended RKE2 service upgrade on additional nodes

**Erratum - added November 26, 2024**: We have identified an issue where `exclude= rke2-*` is not added to the `/etc/yum.conf` file on nodes other than the first server. In specific environments, particularly online ones, an attempt to upgrade all components can cause an unintentional upgrade of the RKE2 service on nodes other than the first server.

To fix this issue, you must manually add `exclude=rke2-*` to the `/etc/yum.conf` file on all the nodes of your Automation Suite cluster.

### Test Automation SQL connection string is ignored

**Erratum - added October 17, 2024**: When you provide an SQL connection string under the `orchestrator.testautomation` section of the `cluster_config.json` file, the `uipathctl` binary ignores the connection string and uses the one under the `orchestrator` section instead. To address the problem, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/test-automation-sql-connection-string-is-ignored) section.

### OSD PV resize does not persist after upgrade

If you resize the `rook-ceph` OSD PV, the new size does not persist following an Automation Suite upgrade.

### Installation fails while populating node labels

**Erratum - added October 17, 2024**: When deploying Automation Suite on AWS machines where only IMDSv2 is enabled, installation fails while populating node labels. To address the issue, see the Important note in [Optional: Enabling resilience to zonal failures in a multi-node HA-ready production cluster](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/optional-enabling-resilience-to-zonal-failures-in-a-multi-node-ha-ready-production-cluster).

### Cannot upgrade due to failed jobs in system-upgrade namespace

**Erratum - Added October 17, 2024**: We accidentally documented this issue as fixed in Automation Suite 2023.10.5. However, the behavior persists. We fixed the issue in [Automation Suite 2023.10.6](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-6#bug-fixes).

Upgrading Automation Suite fails due to the presence of failed jobs in the `system-upgrade` namespace. If the upgrade command fails at any stage (infra, fabric, or service upgrade), take the following steps before retrying the upgrade:

1. List the existing jobs in the `system-upgrade` namespace:
   ```
   kubectl get jobs -n system-upgrade
   ```
2. Delete the failed jobs:
   ```
   kubectl -n system-upgrade delete jobs <failed_jobs>
   ```

When running the command, replace the `<failed_jobs>` placeholder with the names of the failed jobs, separated by spaces.

### Pods cannot communicate with FQDN in a proxy environment

**Erratum - added October 17, 2024**: In a proxy environment, if the proxy server uses the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods cannot communicate with the FQDN. The issue causes the following error:
```
System.Net.Http.HttpRequestException: The proxy tunnel request to proxy 'http://<proxyFQDN>:8080/' failed with status code '404'.
```

To fix the issue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/pods-cannot-communicate-with-fqdn-via-proxy) section.

### AI Center issues with external Orchestrator and Identity Service

**Erratum - added September 11, 2024**: There are several bugs in AI Center when connected to an external Orchestrator and Identity Service, causing issues during setup in the following situations:
* During the installation of Orchestrator certificates for trusted communication.
* When setting up an Identity Service client for Document Manager.
* When configuring an Identity Service client for metering services.

### Weak ciphers in TLS 1.2

**Erratum - added August 29, 2024:** We have identified certain vulnerabilities associated with the usage of weak ciphers in TLS 1.2. For details on how to mitigate the issue, see [How to address weak ciphers in TLS 1.2](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/how-to-address-weak-ciphers-in-tls-12).

### Intermittent not ready reports from agent machines

**Erratum - added October 17, 2024:** An issue causes agent machines to intermittently report as not ready when the `rke2-server` service is shut down without executing the `rke2-killall.sh` script. We fixed this issue in [Automation Suite 2023.10.6](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-6#bug-fixes).

### Registry configuration corruption during upgrades

**Erratum - added October 17, 2024:** An issue causes the corruption of the registry configuration during the upgrade process. The issue occurs when `uipathctl` mistakenly processes ports in helm URLs as external registries, excluding the `insecure_skip_verify: true` parameter from the `registries.yaml` file. To overcome this issue, you must manually include the parameter in your `registries.yaml` file. We fixed this issue in [Automation Suite 2023.10.6](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-6#bug-fixes).

### Resized PVC upgrade issue

**Erratum - added October 17, 2024:** An issue is causing problems in the upgrade process if you have resized the Docker-Registry PVC used by your in-cluster Docker registry. Specifically, the resized PVC is not accurately recognized during upgrades. We fixed this issue in [Automation Suite 2023.10.6](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-6#bug-fixes).

### Redis failures due to inconsistent password updates

**Erratum - added October 17, 2024:** An issue is causing Redis recovery job failures when you update the ArgoCD admin password directly through the UI without simultaneously updating the Kubernetes secrets as well. To prevent the issue, we highly recommend that each time you change the ArgoCD admin password via the UI, ensure that you update the Kubernetes secrets at the same time. For more details on how to properly update the ArgoCD admin password, refer to [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/12001#solution).

### Enabling Connaisseur causes installation or upgrade failures

**Erratum - added October 17, 2024:** An issue causes installation or upgrade failures when enabling Connaisseur during the configuration of an external OCI-compliant registry. The isssue occurs when you set the `registries.trust.enabled` parameter to `true` in the `cluster_config.json` file.

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2023.10.5](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-5) | [Automation Ops 2023.10.5](https://docs.uipath.com/automation-ops/automation-suite/2023.10/user-guide/release-notes-2023-10-5) | [AI Center 2023.10.5](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-5) | [Action Center 2023.10.5](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-5) |
| [Task Mining 2023.10.5](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-5) | AI Computer Vision 2023.10.4 | [Insights 2023.10.5](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-5) | [Apps 2023.10.5](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/2023-10-5) |
| [Process Mining 2023.10.5](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-5) | [Document Understanding 2023.10.5](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10) | [Orchestrator 2023.10.6](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-6) |  |
|  |  | [Test Manager 2023.10.5](https://docs.uipath.com/test-suite/automation-suite/2023.10/release-notes/test-manager-2023-10-5) |  |
|  |  | [Data Service 2023.10.5](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/2023-10-5) |  |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.28.7 |
| ArgoCD | 2.10.9 |
| logging-operator | 4.6.0 |
| logging-operator-logging | 4.6.0 |
| gatekeeper | 3.16.0 |
| rook-ceph | 1.9.4 |
| prometheus-pushgateway | 2.12.0 |
| cert-manager | 1.14.5 |
| rancher-istio | 103.3.0-up1.21.1 |
| rancher-logging | 103.0.0-up3.17.10 |
| rancher-logging-crd | 103.0.0-up3.17.10 |
| rancher-monitoring-crd | 103.1.0-up45.31.1 |
| rancher-gatekeeper-crd | 103.1.0-up3.13.0 |
| rancher-gatekeeper | 103.1.0-up3.13.0 |
| rancher-monitoring | 103.1.0-up45.31.1 |
| longhorn | 1.5.5 |
| longhorn-crd | 1.1.100 |
| reloader | 1.0.95 |
| csi-driver-smb | 1.14.0 |
| velero | 6.2.0 |
| redis-operator | 7.4.2-12 |
| redis-cluster | 7.4.2-129 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/full-migration).