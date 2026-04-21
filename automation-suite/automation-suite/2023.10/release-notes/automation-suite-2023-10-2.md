---
title: "2023.10.2"
visible: true
slug: "automation-suite-2023-10-2"
---

**Release date: February 28, 2024**

## Upgrade considerations

Automation Suite 2023.4.5 and 2023.10.2 include an upgrade to Kubernetes 1.26.11. As such, when upgrading Automation Suite, you must ensure you do not downgrade Kubernetes. To do that, when moving from Automation Suite 2023.4.5 or a later minor version to the next major version, you must upgrade to 2023.10.2 at a minimum.

## Support for Microsoft SQL Server 2022

**Erratum - Added March 25, 2024:** We now support Microsoft SQL Server 2022.

## New prerequisites validation check

**Erratum - Added March 11, 2024:** For optimal cillium functionality, we have improved the prerequisites script to validate that the reverse path filtering is disabled. This new check ensures that `net.ipv4.conf.all.rp_filter` is set to `0`.

For more on the prerequisite script, see [Validating the prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/validating-the-prerequisites-for-the-installation).

## New RHEL version support

We have expanded our OS support to include RHEL 8.9, alongside existing support for 8.6 and 8.8 versions.

## Security enhancements

We continue to provide security updates and patches to address Common Vulnerabilities and Exposures (CVEs).

## Bug fixes

* **Erratum - added August 26, 2024**: We have fixed an issue causing the migration from an in-cluster objectstore to an external objectstore to fail.
* **Erratum - added May 29, 2024**: Network policies in Airflow could previously cause improper functioning of the DNS. The issue no longer occurs.
* We have fixed an issue causing the installer to wrongly ask you to provide a temporary registry whenever adding a new product to an existing Automation Suite installation. The issue caused a failure in the installation process.
* Previously, certain SQL server certificate validations within our flow were being suppressed. We have changed this practice to allow for earlier identification of potential problems.
* **Erratum - added April 15, 2025**: The issue causing the side-by-side and the in-place upgrade of Automation Suite 2022.10 or earlier to 2023.10.0 or later to fail when Apps was enabled and you used Kerberos authentication for the SQL Server database was not fixed in Automation Suite 2023.10.2. The issue is now fixed in [Automation Suite 2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).
* We have modified stored procedures to handle collation differences between the SQL server and SQL database.

## Known issues

### Upgrade failure due to overridden Insights PVC sizes

**Erratum - added December 18, 2024:** An issue causes upgrades to fail when the existing Insights PVC sizes are inadvertently overridden. To address this problem, you must manually change the PVC sizes in ArgoCD UI. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/upgrade-fails-due-to-overridden-insights-pvc-sizes) section.

This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Data loss when reinstalling or upgrading Insights following Automation Suite upgrade

Following an Automation Suite upgrade from version 2023.4 or older, reinstalling or upgrading Insights results in data loss due to an issue with Insights storage class changes. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/data-loss-when-reinstalling-or-upgrading-insights-following-automation-suite-upgrade).

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Node maintenance issue in non-HA Redis

**Erratum - added December 18, 2024**: An issue causes the `redis-cluster-0` pod to get stuck in the terminating state when you perform a node drain in non-HA Redis scenarios. To address the problem, you must force delete the pod using the following command:
```
kubectl -n redis-system delete pod redis-cluster-0 --force
```

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Unnecessary Redis DNS resolution validations during Active/Passive checks

**Erratum - added December 18, 2024**: An issue causes unnecessary Redis DNS resolution validations for `redis.<primary-fqdn>` and `redis-db.<primary-fqdn>` during Active/Passive prerequisite checks. This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Insights annotation issue blocks installer

**Erratum - added December 18, 2024**: An Insights annotation issue blocks the Automation Suite installer. We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Unintended RKE2 service upgrade on additional nodes

**Erratum - added November 26, 2024**: We have identified an issue where `exclude= rke2-*` is not added to the `/etc/yum.conf` file on nodes other than the first server. In specific environments, particularly online ones, an attempt to upgrade all components can cause an unintentional upgrade of the RKE2 service on nodes other than the first server.

To fix this issue, you must manually add `exclude=rke2-*` to the `/etc/yum.conf` file on all the nodes of your Automation Suite cluster.

### AI Center skills sync failure during side-by-side upgrade

**Erratum - added December 18, 2024:** A syntax issue causes the failure of the `aicenter skill sync` and `aicenter skill status` commands during a side-by-side upgrade.

To fix this issue, you must manually edit the syntax. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/ai-center-skills-sync-failure-during-side-by-side-upgrade) section.

### Test Automation SQL connection string is ignored

**Erratum - added October 17, 2024**: When you provide an SQL connection string under the `orchestrator.testautomation` section of the `cluster_config.json` file, the `uipathctl` binary ignores the connection string and uses the one under the `orchestrator` section instead. To address the problem, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/test-automation-sql-connection-string-is-ignored) section.

### Installation fails while populating node labels

**Erratum - added October 17, 2024**: When deploying Automation Suite on AWS machines where only IMDSv2 is enabled, installation fails while populating node labels. To address the issue, see the Important note in [Optional: Enabling resilience to zonal failures in a multi-node HA-ready production cluster](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/optional-enabling-resilience-to-zonal-failures-in-a-multi-node-ha-ready-production-cluster).

### Cannot upgrade due to failed jobs in system-upgrade namespace

**Erratum - added October 17, 2024**: Upgrading Automation Suite fails due to the presence of failed jobs in the `system-upgrade` namespace. If the upgrade command fails at any stage (infra, fabric, or service upgrade), take the following steps before retrying the upgrade:
1. List the existing jobs in the `system-upgrade` namespace:
   ```
   kubectl get jobs -n system-upgrade
   ```
2. Delete the failed jobs:
   ```
   kubectl -n system-upgrade delete jobs <failed_jobs>
   ```

When running the command, replace the `<failed_jobs>` placeholder with the names of the failed jobs, separated by spaces.

We fixed the issue in [Automation Suite 2023.10.6](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-6#bug-fixes).

### Pods cannot communicate with FQDN in a proxy environment

**Erratum - added October 17, 2024**: In a proxy environment, if the proxy server uses the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods cannot communicate with the FQDN. The issue causes the following error:
```
System.Net.Http.HttpRequestException: The proxy tunnel request to proxy 'http://<proxyFQDN>:8080/' failed with status code '404'.
```

To fix the issue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/pods-cannot-communicate-with-fqdn-via-proxy) section.

### Weak ciphers in TLS 1.2

**Erratum - added August 29, 2024:** We have identified certain vulnerabilities associated with the usage of weak ciphers in TLS 1.2. For details on how to mitigate the issue, see [How to address weak ciphers in TLS 1.2](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/how-to-address-weak-ciphers-in-tls-12).

### Support bundle log collection failure

**Erratum - added August 14, 2024**: An issue affects the support bundle generation when using an external OCI registry in an offline environment. Under these conditions, the generated support bundle lacks historical logs and cannot upload to any selected external object storage. To fix this issue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/support-bundle-log-collection-failure) section.

### Upgrades fail due to Longhorn being uninstalled

**Erratum - added August 14, 2024**: Upgrading from Automation Suite 2023.10.x fails due to the Longhorn storage classes still being present. To solve the problem, you must clean up the Longhorn storage classes manually, by running the following command:
```
  for sc in $(kubectl get sc -o json | jq -r '.items[] | select(.provisioner=="driver.longhorn.io") | .metadata.name'); do
    kubectl delete sc "${sc}"
  done
```

We fixed the issue in [Automation Suite 2023.10.5](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-5#bug-fixes).

### Unnecessary ListBucket API prerequisite check fails for external objectstore

**Erratum - added August 14, 2024:** For AI Center and Task Mining, the `ListBucket API` prerequisite check fails when using an external objectstore. However, AI Center and Task Mining do not use the `ListBucket API` permission. We removed the unnecessary check in [Automation Suite 2023.10.5](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-5#bug-fixes).

### Cannot enable SSO for ArgoCD

**Erratum - added August 14, 2024**: You cannot enable SSO for ArgoCD due to an issue with the Dex image versions. We fixed the issue in [Automation Suite 2023.10.5](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-5#bug-fixes).

### snapshot-controller-crds pod in CrashLoopBackOff state after upgrade

**Erratum - added August 14, 2024**: An issue causes the `snapshot-controller-crds` pod to remain in the CrashLoopBackOff state after upgrade. This occurs due to a conflict between the newly installed `snapshot-controller` and the existing one during the RKE2 upgrade. To fix the issue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/snapshot-controller-crds-pod-in-crashloopbackoff-state-after-upgrade) section.

### Components fail when using external object storage with proxy environment

**Erratum - added July 24, 2024:** Using an external storage with a proxy environment causes Orchestrator, the Automation Suite Support Bundle Tool, Prometheus, Thanos, Fluentd, etc. to fail. We fixed the issue in Automation Suite 2023.10.3.

### Issue with saving custom configurations in email settings

**Erratum - added July 3, 2024**: When configuring the email settings, you cannot save any custom configurations due to an issue with form validation. The **Save** button incorrectly appears grayed out, despite filling in all the required fields correctly. As a workaround, you can make a PUT request to the `/identity_/api/setting` endpoint.

Use the appropriate access token and make sure the request body contains the necessary details. Also make sure that `Email.Smtp.UseDefaultCredentials` is set to `True`, like in the following example:

```
{
    "Settings": [
        {
            "Key": "Email.Smtp.Host",
            "Value": "SendGrid"
        },
        {
            "Key": "Email.Smtp.Port",
            "Value": "587"
        },
        {
            "Key": "Email.Smtp.UserName",
            "Value": ""
        },
        {
            "Key": "Email.Smtp.Domain",
            "Value": ""
        },
        {
            "Key": "Email.Smtp.FromEmail",
            "Value": "no-reply@uipath.com"
        },
        {
            "Key": "Email.Smtp.FromDisplayName",
            "Value": "UiPath Platform"
        },
        {
            "Key": "Email.Smtp.EnableSsl",
            "Value": "true"
        },
        {
            "Key": "Email.Smtp.UseDefaultCredentials",
            "Value": "true"
        },
        {
            "Key": "Email.Smtp.Password",
            "Value": ""
        },
        {
            "Key": "Email.Smtp.ConnectionTimeout",
            "Value": "180000"
        }
    ],
    "PartitionGlobalId": ""
}
```

### Support bundle generated with incorrect FQDN for AKS on Azure Government

When generating the support bundle, an incorrect FQDN is used for AKS on Azure Government. We fixed the issue in Automation Suite 2023.10.4.

### CrashLoopBackOff error due to mismatched host admin password

**Erattum - added June 25, 2024:** An issue is causing a CrashLoopBackOff error because the host admin password does not match with the one in the `platform-service-secrets`. This issue occurs when the host admin is updated and no longer matches the one in the `platform-service-secrets`. To fix this, the password in the `platform-service-secrets`must be updated to match the new admin password.

### Error message while uninstalling rook-ceph post migrating to a S3 object-store

**Erratum - added April 19, 2024**: When uninstalling rook-ceph, an error message related to missing external object storage configuration is displayed. This issue occurs even though the migration is succesful. This behavior is fixed in Automation Suite 23.10.3.

### Issues affecting Ceph metrics and alerts

**Erratum - added April 19, 2024**: In certain situations, Ceph metrics and alerts are missing from the monitoring dashboards. To fix the issue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/missing-ceph-rook-metrics-from-monitoring-dashboards) section.

### Issues related to CephMgrIsAbsent alerts

**Erattum - added April 19, 2024**: False positive CephMgrIsAbsent alerts are displayed even though there are no storage issues. This issue is fixed in Automation Suite 23.10.3.

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

### Email alerts configuration failure post upgrade

**Erratum - added February 13, 2025**: An issue affects the functionality of email alerts configuration and the setup of multiple receivers after upgrading from Automation Suite 2022.10. To address this issue, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/failure-to-configure-email-alerts-post-upgrade).

This issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-8#bug-fixes).

### Upgrade failure due to default organization initialization

**Erratum - added June 26, 2025:** An issue causes the upgrade to fail when upgrading from Automation Suite 2022.10 or older to versions 2023.10.0 through 2023.10.2. The issue occurs due to an unknown socket error in the `platform-services-initialize-default-organization-job`, which prevents the default organization from initializing.

We fixed the issue in [Automation Suite 2023.10.3.](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-3#bug-fixes)

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2023.10.2](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [Automation Ops 2023.10.2](https://docs.uipath.com/automation-ops/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [AI Center 2023.10.2](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [Action Center 2023.10.2](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-2) |
| [Task Mining 2023.10.2](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [AI Computer Vision 2023.10.2](https://docs.uipath.com/ai-computer-vision/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [Insights 2023.10.2](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10-2) | [Apps 2023.10.2](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/release-notes-2023-10-2) |
| [Process Mining 2023.10.2](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10-2) | [Document Understanding 2023.10.2](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10) | [Orchestrator 2023.10.3](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/2023-10-3) |  |
|  |  | [Test Manager 2023.10.2](https://docs.uipath.com/test-suite/automation-suite/2023.10/release-notes/test-manager-2023-10-2) |  |
|  |  | [Data Service 2023.10.2](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/release-notes-2023-10-2) |  |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.26.11 |
| ArgoCD | 2.7.7 |
| logging-operator | 4.1.0 |
| logging-operator-logging | 4.1.0 |
| gatekeeper | 3.12.0 |
| rook-ceph | 1.9.4 |
| prometheus-pushgateway | 2.1.6 |
| cert-manager | 1.12.3 |
| rancher-istio | 102.2.0-up1.17.2 |
| rancher-logging | 102.0.1-up3.17.10 |
| rancher-logging-crd | 102.0.1-up3.17.10 |
| rancher-monitoring-crd | 102.0.1-up40.1.2 |
| rancher-gatekeeper-crd | 102.1.0-up3.12.0 |
| rancher-gatekeeper | 100.2.0-up3.8.1 |
| rancher-monitoring | 102.0.1-up40.1.2 |
| longhorn | 1.4.3 |
| longhorn-crd | 1.1.100 |
| reloader | 0.0.129 |
| csi-driver-smb | 1.10.0 |
| velero | 3.1.6 |
| redis-operator | 7.2.4-7 |
| redis-cluster | 7.2.4-64 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/full-migration).