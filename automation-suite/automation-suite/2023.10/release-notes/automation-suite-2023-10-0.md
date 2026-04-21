---
title: "2023.10.0"
visible: true
slug: "automation-suite-2023-10-0"
---

**Release date: April 25, 2024**

## Changes to license-related tenant limitations

If you have a license that includes any of the following services, you will be happy to know that, upon license update, they can now be enabled on 100 tenants each:

* Automation Hub
* Process Mining
* Test Manager
* Insights

**Release date: November 22, 2023**

## New UiPath.OrganizationMigrationApp version released

We have released a new version of UiPath.OrganizationMigrationApp, the tool helping you migrate from a standalone product to Automation Suite. The new version of the tool now enables you to migrate to Automation Suite 2023.10.0.

For more details, see [Migrating standalone products to Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migrating-standalone-products-to-automation-suite).

**Release date: November 3, 2023**

## What's new

### Kerberos authentication changes

**Erratum - added August 14, 2024**: We no longer support updating the Kerberos authentication using the CLI tool. As an alternative, you can update the Kerberos authentication using the method described in [Configuring Kerberos authentication via cluster_config.json](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/setting-up-kerberos-authentication#configuring-kerberos-authentication-via-cluster_configjson).

### Streamlined installation experience

We have revamped our installation experience to ensure that all installation modes, regardless of whether they are online/offline or single-node/multi-node, share similar steps and leverage the same commands. These improvements are aimed at creating a more consistent and seamless installation experience for all users.

Note that now the interactive installer serves a slightly different purpose as you can use it only to generate the `cluster_config.json` file, but it does not perform the actual installation.

For more details, see the following documentation:

* [Hardware and software requirements](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/hardware-and-software-requirements)
* [Manual: Preparing the installation](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/preparing-the-installation)
* [Manual: Installing Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/manual-installing-automation-suite)

### Introducing side-by-side upgrades

You can now perform an Automation Suite upgrade using parallel clusters. This new upgrade method is called side-by-side upgrade, and it allows you to switch traffic from the old Automation Suite cluster (often referred to as the blue deployment in the industry) to the new cluster (the green deployment). One of the benefits of this approach is that your current environment is not impacted by the upgrade operation in any way. In addition to that, if you encounter issues during upgrade, you can easily roll back to the old deployment.

For extensive requirements, an upgrade matrix, and instructions, see [Performing a side-by-side upgrade](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/performing-a-side-by-side-upgrade).

Side-by-side upgrades are the preferred method for upgrading your Automation Suite instance due to its efficiency and less risk of disruptions to workflow operations.

### In-place upgrades enhancements

As an alternative to the side-by-side upgrade mechanism, you can use the in-place upgrade method to move from one Automation Suite version to another. If you have ever upgraded Automation Suite in the past, then you should be familiar with this method.

What is specific to this upgrade process is that it keeps your settings and data intact on the same hardware. There is only one cluster involved, which means that you should rely on backup and restore operations in case you want to revert to a previous state.

While this is the upgrade mechanism we have been using until now, you should know that we have considerably reduced its complexity. The in-place upgrade is now the same for both online and offline scenarios. Moreover, while previously you had to choose between an automated and a manual upgrade process, the way we designed the upgrade flow makes this distinction irrelevant. So there is one single set of instructions for all of you. As a result of this improvement, we have removed from our offering the `uipathctl.sh` tool, which used to help you perform an automation upgrade.

For extensive requirements, an upgrade matrix, and instructions, see [Performing a in-place upgrade](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/performing-an-in-place-upgrade).

### Migration from Automation Suite on Linux to Automation Suite on EKS/AKS

If you are already using Automation Suite on Linux, but you now think that Automation Suite on EKS/AKS would better cater to your needs, we have good news for you. Migrating to a new installation of Automation Suite on EKS/AKS is now possible.

Note that currently you cannot migrate from Automation Suite embedded to an existing installation of Automation Suite on EKS/AKS.

For details on the requirements, required data migration operations, and step-by-step instructions, see [Migrating from Automation Suite on Linux to Automation Suite on EKS/AKS](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migrating-from-automation-suite-on-linux-to-automation-suite-on-eksaks).

### Stabilization and quality enhancement through Longhorn removal

In our continuous mission to improve stability and quality, we have implemented an alternative mechanism to Longhorn. This change outlines a direct integration of data and volumes with the disk attached to server machines, leading to several implications:

* Insights, Docker registry, and monitoring applications now exclusively run on server nodes.
* External objectstore buckets for Insights can now be configured. For details, see [External Objectstore configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/external-objectstore-configuration).
* We have added support for NFSv3.
* Once the upgrade process is completed without migrating from Longhorn, a cluster restored from a backup would not have Longhorn.
* AI Center pipeline requires additional storage. The pipeline operates on the machine where the extra AI Center disk has been mounted, which could either be a server or agent machine.

### Introducing uipathctl

As part of an initiative to unify our CLI tools, we are introducing `uipathctl`. Currently, the main purposes of the new tool are to help you diagnose and troubleshoot issues affecting your Automation Suite installation, perform a side-by-side upgrade, migrate from Automation Suite on Linux to Automation Suite on EKS/AKS, migrate to an external OCI-compliant registry, and generate the `cluster_config.json` file.

Stay tuned and watch `uipathctl` become the go-to tool in many other scenarios.

### Objectstore access without pre-signed URLs

The latest release introduces the capability to disable access via pre-signed URLs, enhancing the authority over your external objectstore.

Please note, once this setting is enabled, it is irreversible and applies globally. Individual product-level alterations are not possible.

Take into account that this particular configuration does not support Task Mining and specific activities including **Write Storage Text, Upload Storage File, List Storage Files, Read Storage Text, Download Storage File**, and **Delete Storage File**.

### Enhanced features for external Docker registry

We have made substantial enhancements to the external Docker registry. You can now benefit from these new functionalities:

* Your external Docker registry can be equipped with its private certificate, giving you an additional layer of security.
* In addition to the usage of a mirror registry script, which requires internet access to copy the Automation Suite artifacts, we now support the `hydrate-registry.sh` script. This script will take an offline tar bundle, unpack it, and upload its content directly to the external Docker registry, providing more flexibility and options for managing your registry.

### Split offline bundle for customers with restricted network access

To better accommodate those with restrictive network access, we have introduced a split `as.tar.gz` file, which you can use to perform an offline installation. The offline bundle is split into 52 parts for easier downloading, and you can reassemble it once all parts are downloaded.

Please note, the option to download the full `as.tar.gz` file in one go continues to remain available for those with sufficient bandwidth.

For more information on how to download and merge these split files, visit our [official documentation](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/installation-packages-download-links#split-astargz).

### New RHEL version supported

You can now install Automation Suite on machines running Red Hat Enterprise Linux (RHEL) 8.8.

:::important
RHEL kernel version kernel-4.18.0-477.10.1.el8_8 is affected by [an issue](https://access.redhat.com/solutions/7014646) that interrupts the installation or management of the Automation Suite cluster. Make sure that none of the Automation Suite nodes uses this kernel version either pre- or post-installation. You can update the kernel version by running the following command: assignment
```
dnf install -y kernel kernel-tools kernel-tools-libs
```
:::

### SELinux support

All Automation Suite versions support out-of-the-box SELinux, with default policies enabled.

### IMDSv2 support

We now support IMDSv2 for connecting with the AWS S3 using the instance profile.

### Deprecation of ArgoCD UI documentation

To ensure adherence to best practices and maintain the stability of your operations, we are steering away from the use of the ArgoCD UI as a means to change settings or parameters.

Instead, we are emphasizing the recommendation to use the `cluster_config.json` file for these purposes. This move aims to maintain a consistent source of truth for your configurations.

However, you can continue to use the ArgoCD UI to troubleshoot, see logs, or other similar operations.

### Changes to Kerberos auth configuration

**Erratum - added August 17, 2024**: We have updated the Kerberos authentication configuration process. Instead of using the `configureUiPathAS.sh` script or the CLI tool, you can now configure the authentication using the `cluster_config.json` file. For details, see [Configuring Kerberos authentication via cluster_config.json](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/setting-up-kerberos-authentication#configuring-kerberos-authentication-via-cluster_configjson).

### Licensing news

#### Audit log messages change

The audit data message displayed when a user is removed by an administrator, and their licenses are consequently deallocated, has been improved for clarity. You can now expect to see this in such cases: `User <administrator_name> deallocated all licenses of user(s) <user_names>`.

#### AI Units allocation

AI units can now also be allocated at the tenant level. This is done from the license allocation window corresponding to the desired tenant in the **Admin** section.

#### License allocation endpoints

Two new endpoints are available for allocating licenses from the API:

* `GET/api​/account​/{accountId}​/user-license​/group​/{groupId}` - call this endpoint to retrieve a list of all available user licenses for creating or editing a group.
* You need **View** permission on **License** to use this endpoint.
* `PUT/api/account/{accountId}/user-license/group/{groupId}` - call this endpoint to allocate or update a group rule.
* You need **Write** permission on **License** to use this endpoint.

### Introducing the Citizen Developers user group

We're excited to announce the latest enhancement to our platform's access control capabilities — the introduction of a new user group: Citizen Developers. This new group is defined at the organization level and will be seamlessly integrated across all services within the platform.

With the Citizen Developers group, citizen developers can access resources pertinent to their work without any unnecessary access clutter, leading to reduced overhead for your administrators.

To learn more about how the user group is integrated into the various services within the platform, refer to the product documentation.

### Custom attribute mapping for AAD

While our existing AAD integration offers automatic attribute mapping, this release introduces the ability for organizations to use custom attribute mappings.

We're launching with custom mapping support for the **Business unit** attribute which allows you to map attributes like organization divisions with the Business Unit field in the UiPath® platform. This mapping can enhance the contextual understanding of users in your organization and can help integrate user identities with services such as Automation Hub.

You can map the **Business unit** attribute based on Azure AD attributes or via SAML.

### End of life for the Deployment Assistant

We are discontinuing support for the Deployment Assistant. This will allow us to focus on further developing and refining tools that bring you greater benefits.

We encourage all users to delve into our official documentation to understand the existing tools and features. Please share your feedback on our official documentation; your input is essential in helping us continually enhance and fine-tune our offerings to best serve your needs.

## Improvements

### Improved troubleshooting experience

We have introduced a new CLI tool helping you troubleshoot and debug Automation Suite. The new tool is called `uipathtools` and contains a subset of `uipathctl` capabilities specific to health commands. To make sure you have access to mitigation steps in a timely manner, we plan to provide updates to `uipathtools` at a higher cadence than our standard releases.

The `uipathtools` and `uipathctl` CLI tools are here to provide all the diagnostics functionalities of the old Automation Suite Diagnostics tool, `diagnostics-report.sh`, which we have removed from our offering.

### Improved SSO authentication

We have updated the process for enabling Single Sign-On (SSO) for ArgoCD, which now involves using a Dex configuration file and specified parameters.

Read more details in [our documentation](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/enabling-sso-for-argocd).

## Bug fixes

* **Erratum January 2024:** The replica cleanup script would incorrectly reclaim storage on the nodes. For more details, see the [Storage reclamation patch](https://docs.uipath.com/automation-suite/automation-suite/2022.4/installation-guide/storage-reclamation-patch) troubleshooting article.
* Previously, both scheduled and on-demand backups would fail after one hour of timeout. Now you can extend the timeout interval to three hours. For details, see [Enabling the snapshot backup](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/configuring-the-cluster-snapshot-backup#enabling-the-snapshot-backup) and [On-demand snapshot backup](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/configuring-the-cluster-snapshot-backup#on-demand-snapshot-backup).
* On some occasions, the `configureUiPathAS.sh` script did not properly update or read the ODBC connection strings. This behavior no longer occurs.
* A failure would occur when trying to rerun the Automation Suite installer 90 days after the first execution. The installer generated self-signed certificates with a 90-day validity, and rerunning it prompted the revalidation of the already expired certificates.

## Admin bug fixes

* Automation Express licenses were available for allocation in on-premises deployments, despite them being solely intended for cloud environments. The issue is now fixed.
* Data Service units were not granted to organizations that had **Action Center - Named User** licenses. The issue is now fixed.
* When you deleted an organization, its licenses were not released. Now, any licenses allocated to an organization go back to the license pool once the organization is deleted.
* The `minLevel` NLog setting in the config map was not being honored. The default `minLevel` is "Info" indicating that logs of "Info" severity and above should have been logged. However, the `minLevel` was not being considered, and logs with lower severity levels, specifically "Trace" and "Debug," were also being written to the logs.
* Previously, there was an issue where well-known SIDs were inadvertently included when retrieving security groups, leading to unexpected behavior. Well-known SIDs are no longer included when fetching security groups, ensuring smoother and more predictable functionality.
* After upgrading to version 2022.10.1 or later, logging into the host tenant, then logging out, and subsequently switching to a different tenant resulted in redirection back to the previous log-out location instead of the selected tenant. Now, after logging out and switching tenants, you will be correctly redirected to the selected tenant's page instead of the previous log-out location.

## Known issues

### Upgrade failure due to overridden Insights PVC sizes

**Erratum - added December 18, 2024:** An issue causes upgrades to fail when the existing Insights PVC sizes are inadvertently overridden. To address this problem, you must manually change the PVC sizes in ArgoCD UI. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/upgrade-fails-due-to-overridden-insights-pvc-sizes) section.

This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Data loss when reinstalling or upgrading Insights following Automation Suite upgrade

**Erratum - added December 18, 2024:** Following an Automation Suite upgrade from version 2023.4 or older, reinstalling or upgrading Insights results in data loss due to an issue with Insights storage class changes. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/data-loss-when-reinstalling-or-upgrading-insights-following-automation-suite-upgrade).

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

### Unnecessary ListBucket API prerequisite check fails for external objectstore

**Erratum - added August 14, 2024:** For AI Center and Task Mining, the `ListBucket API` prerequisite check fails when using an external objectstore. However, AI Center and Task Mining do not use the `ListBucket API` permission. We removed the unnecessary check in [Automation Suite 2023.10.5](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-5#bug-fixes).

### Cannot enable SSO for ArgoCD

**Erratum - added August 14, 2024**: You cannot enable SSO for ArgoCD due to an issue with the Dex image versions. We fixed the issue in [Automation Suite 2023.10.5](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-5#bug-fixes).

### snapshot-controller-crds pod in CrashLoopBackOff state after upgrade

**Erratum - added August 14, 2024**: An issue causes the `snapshot-controller-crds` pod to remain in the CrashLoopBackOff state after upgrade. This occurs due to a conflict between the newly installed `snapshot-controller` and the existing one during the RKE2 upgrade. To fix the issue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/snapshot-controller-crds-pod-in-crashloopbackoff-state-after-upgrade) section.

### Migration from in-cluster objectstore to external objectstore fails

**Erratum - added August, 2024:** Migrating from an in-cluster objectstore to an external objectstore fails due to a configuration issue. Therefore, you must not attempt a migration from the Ceph in-cluster objectstore to an external objectstore in this version of Automation Suite. We fixed the issue in Automation Suite 2023.10.2, where you can safely migrate from Ceph to an external objectstore.

### Components fail when using external object storage with proxy environment

**Erratum - added July 24, 2024:** Using an external storage with a proxy environment causes Orchestrator, the Automation Suite Support Bundle Tool, Prometheus, Thanos, Fluentd, etc. to fail. We fixed the issue in Automation Suite 2023.10.3.

### Support bundle generated with incorrect FQDN for AKS on Azure Government

When generating the support bundle, an incorrect FQDN is used for AKS on Azure Government. We fixed the issue in Automation Suite 2023.10.4.

### Network policies in Airflow may cause improper functioning of DNS

**Erratum - added June 3, 2024**: Ocassionally the network policies for Airflow prevent the DNS from working correctly. To prevent the issue, run the following command.
```
sudo networkPolicyTool.sh --createNetworkPolicy ./Configs/networkPolicyTool/airflow.yaml --add
```

To install Network Policy Tool, follow the instructions in this troubleshooting article: [Network Policy Tool](https://github.com/UiPath/automation-suite-support-tools/tree/main/Scripts/GeneralTools/networkPolicyDebugTool#airflow-fix-2344-and-below-and-23101-and-below). This issue is fixed in Automation Suite 23.10.3.

### Single-node upgrade fails at the fabric stage

**Erratum - added May 20, 2024:​​** On single-node deployments with in-cluster storage, upgrades from version 2022.4.1 or older fail at the fabric stage due to a rook-ceph​​ migration issue. To prevent the issue, follow the instructions in [Single-node upgrade fails at the fabric stage​​.](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/single-node-upgrade-fails-at-the-fabric-stage)

### Issues related to CephMgrIsAbsent alerts

**​Erattum - added April 19, 2024​​:** False positive CephMgrIsAbsent alerts are displayed even though there are no storage issues. This issue is fixed in Automation Suite 23.10.3.

### Error message while uninstalling rook-ceph post migrating to a S3 object-store

**Erratum - added April 19, 2024**: When uninstalling rook-ceph, an error message related to missing external object storage configuration is displayed. This issue occurs even though the migration is succesful. This behavior is fixed in Automation Suite 23.10.3.

### Issues affecting Ceph metrics and alerts

**Erratum - added April 19, 2024:** In certain situations, Ceph metrics and alerts are missing from the monitoring dashboards. To fix the issue, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/missing-ceph-rook-metrics-from-monitoring-dashboards) section.

### Collation differences between SQL server and SQL database not supported

​**Erratum - added February 28, 2024:​​** Stored procedures do not support collation differences between the SQL server and SQL database. To avoid any potential problems, you must ensure that the collation settings of both SQL server and SQL database are identical.

### Upgrade fails due to MongoDB to SQL Server migration

**Erratum - added February 28, 2024**: We have identified an issue impacting the side-by-side and the in-place upgrade of Automation Suite 2022.10 or earlier to Automation Suite 2023.10.0 or later. Due to a faulty migration from MongoDB to SQL Server, the upgrade operation fails if you have Apps enabled and use Kerberos authentication for the SQL Server database.

**Erratum - added April 15, 2025:** The recommended solution is to upgrade to [Automation Suite 2023.10.9](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-9#bug-fixes).

### Installation failure when adding new products to existing Automation Suite

**Erratum - added February 28, 2024**: Whenever trying to add a new product to an existing Automation Suite installation, the installer wrongly asks you to provide a temporary registry, causing a failure in the installation process.

To solve the problem, use the following workaround:

1. Make sure the temporary registry is up.
2. Change the readinessProbe setting of the docker registry StatefulSet by running the following command:
   ```
   kubectl patch statefulset docker-registry -n docker-registry --type json -p '[{"op": "replace", "path": "/spec/template/spec/containers/0/readinessProbe", "value": {"httpGet":{"scheme":"HTTPS", "path": "/", "port": 5000}}}]'
   ```

### Issues affecting log forwarding to government cloud storage

**Erratum - added December 19, 2023**: You cannot forward Fluentd and Fluent Bit logs to Azure and AWS government cloud storage.

We recommend using Splunk and [forwarding application logs there](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/forwarding-application-logs-to-splunk).

### Zombie processes after performing an offline installation

**Erratum - added December 19, 2023**: After performing an offline installation, the Docker registry readiness probes trigger zombie processes.

To fix the issue, run the following command after performing a 2023.10.0 offline installation to update the existing readiness probes. This step is not required for online installations.

```
kubectl patch statefulset docker-registry -n docker-registry --type json -p  '[{"op": "replace", "path": "/spec/template/spec/containers/0/readinessProbe", "value": {"exec":{"command":["sh","-c", "[ -f /var/lib/registry/ready ] || { echo \"Registry is not seeded\"; exit 1; } "]}}}]'
```

### After Disaster Recovery Dapr is not working properly for Process Mining and Task Mining

After a Disaster Recovery, Dapr is not restored properly, and the certificates needed by dapr to provide services for Process Mining and Task Mining are incorrect. The dapr, processmining, and taskmining applications appear to be healthy first, but will then go back to progressing state and the environment becomes unstable. When logging in to Process Mining or Task Mining, the application may not load, or return unexpected errors.

See [Process Mining troubleshooting](https://docs-staging.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/process-mining-troubleshooting) for a description of the steps you should take to resolve the issue.

### Document Understanding Out of the Box Packages versions missing

In certain situations, the Out of the Box Packages installer can fail. If this happens, some ML Package versions will be missing in Document Understanding. To fix this, you can either trigger the ArgoCD sync, or wait until the ArgoCD sync triggers the installer automatically to reinstall the packages.

### Character not allowed when setting connection string for Document Understanding

When setting the connection strings manually in the configuration file, Document Understanding database passwords cannot start with `{` for PYODBC.

### AI Center provisioning failure after upgrading to 2023.10

When upgrading from 2023.4.3 to 2023.10, you run into issues with provisioning AI Center.

The system shows the following exception, and the tenant creation fails: `"exception":"sun.security.pkcs11.wrapper.PKCS11Exception: CKR_KEY_SIZE_RANGE`

To resolve this issue, you need to perform a rollout restart of the `ai-trainer` deployment. To do this, run the following command:

```
kubectl -n uipath rollout restart deploy ai-trainer-deployment
```

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
| [Automation Hub 2023.10.0](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/release-notes-2023-10) | [Automation Ops 2023.10.0](https://docs.uipath.com/automation-ops/automation-suite/2023.10/user-guide/release-notes-2023-10-0) | [AI Center 2023.10.0](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/202310) | [Action Center 2023.10.0](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/release-notes-2023-10-0) |
| [Task Mining 2023.10.0](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/release-notes-2023-10) | AI Computer Vision 2023.4.3 | [Insights 2023.10.0](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/release-notes-2023-10) | [Apps 2023.10.0](https://docs.uipath.com/apps/automation-suite/2023.10/release-notes/release-notes-2023-10-0) |
| [Process Mining 2023.10.0](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-2023-10) | [Document Understanding 2023.10.0](https://docs.uipath.com/document-understanding/automation-suite/2023.10/release-notes/release-notes-2023-10#2023100) | [Orchestrator 2023.10.0](https://docs.uipath.com/orchestrator/automation-suite/2023.10/release-notes/release-notes-2023-10-0) |  |
|  |  | [Test Manager 2023.10.0](https://docs.uipath.com/test-suite/automation-suite/2023.10/user-guide/test-manager-2023-10) |  |
|  |  | [Data Service 2023.10.0](https://docs.uipath.com/data-service/automation-suite/2023.10/release-notes/release-notes-2023-10-0) |  |

### Internal component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.26.5 |
| ArgoCD | 2.7.7 |
| logging-operator | 3.17.10 |
| logging-operator-logging | 3.17.10 |
| gatekeeper | 3.11.0 |
| rook-ceph | 1.9.4 |
| prometheus-pushgateway | 2.1.6 |
| cert-manager | 1.12.3 |
| rancher-istio | 102.2.0-up1.17.2 |
| rancher-logging | 102.0.1-up3.17.10 |
| rancher-logging-crd | 102.0.1-up3.17.10 |
| rancher-monitoring-crd | 102.0.1-up40.1.2 |
| rancher-gatekeeper-crd | 100.2.0-up3.8.1 |
| rancher-gatekeeper | 100.2.0-up3.8.1 |
| rancher-monitoring | 102.0.1-up40.1.2 |
| longhorn | 1.4.3 |
| longhorn-crd | 1.1.100 |
| reloader | 0.0.129 |
| csi-driver-smb | 1.8.0 |
| velero | 3.1.6 |
| redis-operator | 6.2.18-41 |
| redis-cluster | 6.2.18-65 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/full-migration).