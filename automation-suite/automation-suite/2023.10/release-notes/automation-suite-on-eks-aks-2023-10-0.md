---
title: "2023.10.0"
visible: true
slug: "automation-suite-on-eks-aks-2023-10-0"
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

For more details, see [Migrating standalone products to Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migrating-standalone-products-to-automation-suite).

**Release date: November 3, 2023**

## What's new

### Migration from Automation Suite on Linux to Automation Suite on EKS/AKS

If you are already using Automation Suite on Linux, but you now think that Automation Suite on EKS/AKS would better cater to your needs, we have good news for you. Migrating to a new installation of Automation Suite on EKS/AKS is now possible.

Note that currently you cannot migrate from Automation Suite embedded to an existing installation of Automation Suite on EKS/AKS.

For details on the requirements, required data migration operations, and step-by-step instructions, see [Migrating from Automation Suite on Linux to Automation Suite on EKS/AKS](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migrating-from-automation-suite-on-linux-to-automation-suite-on-eksaks).

### Support for offline installations

We are happy to announce that you can install Automation Suite on EKS/AKS in offline environments. That means that you can completely isolate your setup, and no internet access is needed to perform an installation.

While most of the installation flow is the same as the one for online deployments, there is one additional requirement that you must meet to carry out an offline installation. You need an OCI-compliant registry to store all the container images and binaries of the UiPath® products.

For detailed installation instructions, see [Installing Automation Suite on EKS/AKS](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/installing-automation-suite-on-eksaks).

For details on the deployment types and architecture, see [Deployment scenarios](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/deployment-scenarios#offline-deployment).

### Support for enabling FIPS 140-2 on AKS nodes

If you must comply with the Federal Information Processing Standard 140-2 (FIPS 140-2), we are happy to announce that you can now install Automation Suite on AKS nodes with FIPS 140-2 enabled.

We have prepared a set of instructions for you to easily enable FIPS 140-2 on the [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/security-and-compliance#fips-140-2) page.

### Enhanced features for external Docker registry

We have made substantial enhancements to the external Docker registry. You can now benefit from these new functionalities:

* Your external Docker registry can be equipped with its private certificate, giving you an additional layer of security.
* In addition to the usage of a mirror registry script, which requires internet access to copy the Automation Suite artifacts, we now support the `hydrate-registry.sh` script. This script will take an offline tar bundle, unpack it, and upload its content directly to the external Docker registry, providing more flexibility and options for managing your registry.

### Objectstore access without pre-signed URLs

You can configure your external objectstore in a way that does not allow access via pre-signed URLs. To do that, you just need to set the `external_object_storage.disable_pre_signed_url` flag to `true` in the `input.json` file during installation. Note that changing the value of this flag at a later point is not possible.

Before disabling pre-signed URL access, take into account that this is a global configuration, and you cannot override it at the product level. Aside from that, Task Mining and a series of activities do not support this configuration.

For more details, see [External object store configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#external-objectstore-configuration).

### Bring your own Istio

You can now choose who provisions and manages the Istio component. While previously it was us that bundled Istio in Automation Suite, you can now bring the component yourself. If you choose the latter, you are responsible for ensuring the Istio component is supported. For details, see the [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix).

### Custom namespace labels

You can now define your own labels in the namespace created by the `uipathctl` installer. For configuration instructions, see [Configuring input.json](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#custom-namespace-label-configuration).

### Custom taints and tolerations

We now support custom taints and tolerations on the cluster nodes in Automation Suite on EKS/AKS. For configuration instructions, see [Configuring input.json](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-inputjson#custom-node-toleration-configuration).

### New requirements for running prerequisite and health checks/tests

The prerequisite and health checks/tests run in the `uipath-check` namespace. You must either allow the creation of the `uipath-check` namespace or create it yourself before running the checks/tests. In addition to this, some checks/tests require that you allow the communication between the `uipath-check` and `uipath` namespaces, or that you enable the use of `hostNetwork`.

### IMDSv2 support

We now support IMDSv2 for connecting with the AWS S3 using the instance profile.

### Custom attribute mapping for AAD

While our existing AAD integration offers automatic attribute mapping, this release introduces the ability for organizations to use custom attribute mappings.

We're launching with custom mapping support for the **Business unit** attribute which allows you to map attributes like organization divisions with the Business Unit field in the UiPath® platform. This mapping can enhance the contextual understanding of users in your organization and can help integrate user identities with services such as Automation Hub.

You can map the **Business unit** attribute based on Azure AD attributes or via SAML.

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

## Improvements

### Improved troubleshooting experience

We have introduced a new CLI tool helping you troubleshoot and debug Automation Suite. The new tool is called `uipathtools` and contains a subset of `uipathctl` capabilities specific to health commands. To make sure you have access to mitigation steps in a timely manner, we plan to provide updates to `uipathtools` at a higher cadence than our standard releases.

### uipathctl certification

The `uipathctl` binaries for Windows and MacOS are now signed with the `uipath.com` certificate, and no warning is shown when running them.

### Prerequisites and health check enhancements

We have made significant improvements in the area of prerequisites and health checks. These enhancements are designed to make your experience smoother and more efficient. Here's what's new:

* **Improved Storage Class prerequisite:** The StorageClass prerequisite, which previously took a considerable amount of time, has been significantly optimized. You will now experience faster execution, reducing setup time for your deployments.
* **Streamlined tests and checks:** All tests and checks have been consolidated into the "uipath-check" namespace, providing a more organized and efficient testing environment.
* **Enhanced post-test handling:** Following test execution, the namespace and pods may remain active for a brief period. This is done to ensure you have ample time to review logs in case of any failures, enabling more effective troubleshooting.
* **New Kube-API connectivity check:** We have introduced a new check to verify kube-api connectivity from every node, enhancing the reliability of your environment. We have introduced a check that verifies continuous connectivity for 15 seconds by retrieving server version from the kube-api server from each node.
* **Improved capacity checks:** Capacity checks have been optimized to provide a more accurate representation of your cluster's capacity by disregarding pending pods when calculating pod limits. This ensures that the reported capacity aligns with your actual operational resources.

## Admin bug fixes

* Automation Express licenses were available for allocation in on-premises deployments, despite them being solely intended for cloud environments. The issue is now fixed.
* Data Service units were not granted to organizations that had **Action Center - Named User** licenses. The issue is now fixed.
* When you deleted an organization, its licenses were not released. Now, any licenses allocated to an organization go back to the license pool once the organization is deleted.
* The `minLevel` NLog setting in the config map was not being honored. The default `minLevel` is "Info" indicating that logs of "Info" severity and above should have been logged. However, the `minLevel` was not being considered, and logs with lower severity levels, specifically "Trace" and "Debug," were also being written to the logs.
* Previously, there was an issue where well-known SIDs were inadvertently included when retrieving security groups, leading to unexpected behavior. Well-known SIDs are no longer included when fetching security groups, ensuring smoother and more predictable functionality.
* After upgrading to version 2022.10.1 or later, logging into the host tenant, then logging out, and subsequently switching to a different tenant resulted in redirection back to the previous log-out location instead of the selected tenant. Now, after logging out and switching tenants, you will be correctly redirected to the selected tenant's page instead of the previous log-out location.

## Known issues

### Upgrade failure due to overridden Insights PVC sizes

**Erratum - added December 18, 2024:** An issue causes upgrades to fail when the existing Insights PVC sizes are inadvertently overridden. To address this problem, you must manually change the PVC sizes in ArgoCD UI. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/upgrade-fails-due-to-overridden-insights-pvc-sizes) section.

This issue is fixed in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-7#bug-fixes).

### Insights volumes created in two different zones following migration

When you migrate from Automation Suite on Linux to Automation Suite on EKS/AKS, Insights-related volumes are occasionally created in two different zones. As a result, you may encounter issues when bringing up the Insights service. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/insights-pvs-created-in-two-different-zones-following-migration).

We fixed the issue in [Automation Suite 2023.10.7](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-2023-10-7#bug-fixes).

### Configuring app security for Process Mining apps

**Erratum - added December 13, 2024**: When configuring process app security using the `app_security_mode` setting, the `single_account` value is not available.

### Test Automation SQL connection string is ignored

**Erratum - added October 17, 2024**: When you provide an SQL connection string under the `orchestrator.testautomation` section of the `input.json` file, the `uipathctl` binary ignores the connection string and uses the one under the `orchestrator` section instead. To address the problem, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting#test-automation-sql-connection-string-is-ignored) section.

### Pods cannot communicate with FQDN in a proxy environment

**Erratum - added October 17, 2024**: In a proxy environment, if the proxy server uses the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods cannot communicate with the FQDN. The issue causes the following error:
```
System.Net.Http.HttpRequestException: The proxy tunnel request to proxy 'http://<proxyFQDN>:8080/' failed with status code '404'.
```

To fix the issue, see [Automation Suite on EKS/AKS troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/pods-cannot-communicate-with-fqdn-via-proxy).

### Temporary network policies not getting cleaned up after health check

**Erratum - added August 14, 2024**: Running a health check creates temporary network policies that are not cleaned up when the check concludes. We fixed the issue in [Automation Suite 2023.10.5](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-5#bug-fixes).

### Unnecessary ListBucket API prerequisite check fails for external objectstore

**Erratum - added August 14, 2024**: For AI Center and Task Mining, the `ListBucket API` prerequisite check fails when using an external objectstore. However, AI Center and Task Mining do not use the `ListBucket API` permission. We removed the unnecessary check in [Automation Suite 2023.10.5](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-5#bug-fixes).

### The backup setup does not work due to a failure to connect to Azure Government

**Erratum - added June 25, 2024**: Following an Automation Suite on AKS installation or upgrade, the backup setup does not work because of a failure to connect to Azure Government. You can fix the issue by taking the steps described in [Automation Suite on EKS/AKS troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting#the-backup-setup-does-not-work-due-to-a-failure-to-connect-to-azure-government).

### Issues affecting Grafana dasboards

**Erratum - added April 19, 2024**: An issue is causing a 404 error when trying to create or import a dashboard in Grafana.

To solve the problem, you need to manually edit the dashboard URL by adding an extra `/dashboard` between the existing `/dashboard` and `/new` or `/import`.

### Issues affecting log forwarding to government cloud storage

**Erratum December 19, 2023**: You cannot forward Fluentd and Fluent Bit logs to Azure and AWS government cloud storage.

We recommend using Splunk and [forwarding application logs there](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/forwarding-application-logs-to-splunk).

### Task Mining and Automation Suite Robots in degraded state after restore from a backup

Occasionally, performing a restore operation in Automation Suite on AKS might cause Task Mining and Automation Suite Robots applications to go in degraded state with the following error:

```
  Warning  FailedAttachVolume  106s (x30 over 46m)  attachdetach-controller  AttachVolume.Attach failed for volume "pvc-358781ec-d9be-4b54-9099-4a44bdc59294" : rpc error: code = NotFound desc = Volume not found, failed with error: Retriable: false, RetryAfter: 0s, HTTPStatusCode: 403, RawError: {"error":{"code":"AuthorizationFailed","message":"The client '29683acd-8bb9-4041-a725-5afc5804535c' with object id '29683acd-8bb9-4041-a725-5afc5804535c' does not have authorization to perform action 'Microsoft.Compute/disks/read' over scope '/subscriptions/b65b0225-ce9b-4a79-9dd9-c00071d40d64/resourceGroups/MC_ci-asaks4489877_ci-asaks4489877_centralus/providers/Microsoft.Compute/disks/restore-755f25c3-ddf0-4d7f-b81c-5379ec6b4720' or the scope is invalid. If access was recently granted, please refresh your credentials."}}
```

To fix the issue, provide the mentioned client the necessary permissions to access your environment.

### After Disaster Recovery Dapr is not working properly for Process Mining and Task Mining

After a Disaster Recovery, Dapr is not restored properly, and the certificates needed by dapr to provide services for Process Mining and Task Mining are incorrect. The dapr, processmining, and taskmining applications appear to be healthy first, but will then go back to progressing state and the environment becomes unstable. When logging in to Process Mining or Task Mining, the application may not load, or return unexpected errors.

See [Process Mining troubleshooting](https://docs-staging.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/process-mining-troubleshooting) for a description of the steps you should take to resolve the issue.

### Document Understanding Out of the Box Packages versions missing

In certain situations, the Out of the Box Packages installer can fail. If this happens, some ML Package versions will be missing in Document Understanding. To fix this, you can either trigger the ArgoCD sync, or wait until the ArgoCD sync triggers the installer automatically to reinstall the packages.

### Character not allowed when setting connection string for Document Understanding

When setting the connection strings manually in the configuration file, Document Understanding database passwords cannot start with `{` for PYODBC.

### Unable to launch Automation Hub and Apps with proxy setup

If you are using a proxy setup, you may run into issues when trying to launch Automation Hub and Apps.

See [Automation Suite on EKS/AKS troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting#unable-to-launch-automation-hub-and-apps-with-proxy-setup) for a description of the steps you should take to resolve the issue.

### AI Center provisioning failure after upgrading to 2023.10​

When upgrading from 2023.4.3 to 2023.10, you run into issues with provisioning AI Center.​

The system shows the following exception, and the tenant creation fails:

```
"exception":"sun.security.pkcs11.wrapper.PKCS11Exception: CKR_KEY_SIZE_RANGE​​​
```

To resolve this issue, you need to perform a rollout restart of the ai-trainer​​ deployment. To do this, run the following command:​

```
kubectl -n uipath rollout restart deploy ai-trainer-deployment
```

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights is not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable Insights.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/security-and-compliance).

### Velero backup fails with FailedValidation error

**Erratum - added September 24, 2025:** An issue prevents Velero scheduled backups from running successfully. A `FailedValidation` error message is displayed, indicating that no default backup location can be found. This issue occurs because the `default-bs1` backup storage location is not marked as the default. As a result, Velero cannot identify a valid backup target, and scheduled backups fail.

To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/velero-backup-fails-with-failedvalidation-error) section.

We fixed the issue in [Automation Suite 2023.10.11](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-11#bug-fixes).

### Log streaming does not work in proxy setups

**Erratum - added June 26, 2025:** Log forwarding does not work in proxy setups because the proxy environment variables were not set in the logging pods. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/log-streaming-does-not-work-in-proxy-setups) section.

We fixed the issue in [Automation Suite 2023.10.10](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-10#bug-fixes).

### Licensing SQL connection error

**Erratum - added June 26, 2025:** Licensing SQL connection errors occur when the Data Source property specified both a named instance and a port.

We fixed the issue in [Automation Suite 2023.10.10](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-10#bug-fixes).

### Insights dashboards excluded from backups

**Erratum - added April 2, 2025:** An issue is preventing the inclusion of Insights dashboards in backups. To address this issue, refer to the [Backing up the cluster](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/backing-up-the-cluster#prerequisites) page. The issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-8#bug-fixes).

### Fluentd logs transmission failure

**Erratum - added February 13, 2025**: An issue prevents Fluentd from sending logs to remote locations due to a lack of memory buffer. To address this issue, you must add a memory limit for Fluentd to prevent disruptions or delays when transmitting logs to a remote location.

This issue is fixed in [Automation Suite 2023.10.8](https://docs.uipath.com/automation-suite/automation-suite/2023.10/release-notes/automation-suite-on-eks-aks-2023-10-8#bug-fixes).

### Microsoft Entra ID limitations

**Erratum - added January 20, 2025**: Insights and Task Mining do not currently support Microsoft Entra ID (formerly Azure Active Directory) authentication configuration for access to SQL, storage, and other resources that support Microsoft Entra.

### Insights dashboards backup issue

**Erratum - added December 18, 2024** We have identified an issue with the backup logic in Automation Suite for AKS/EKS. Specifically, this defect excludes the backup of Insights dashboards. However, all historical data is successfully backed up.

We are working diligently to resolve this issue. We aim to develop and implement a mitigation approach as early as possible.

If you are using Automation Suite on AKS/EKS along with UiPath Insights, this defect may affect your operations. While we address this issue, we suggest [manually exporting your dashboards](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/dashboards#exporting-and-importing-dashboards) as a preventive measure.

Note that backups are mainly used as a recovery method in the event of a disaster-level incident or in preparation for an Automation Suite upgrade. This is particularly useful if an upgrade fails and stored data needs to be restored to its previous state.

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

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

| Component | Version |
| --- | --- |
| Istio | 1.18.0 |
| ArgoCD | v2.7.7 |
| Prometheus | v2.42.0 |
| Grafana | 10.1.1 |
| Fluentd & Fluent-bit | logging-operator: 4.1.0  logging-operator-logging: 4.1.0 |
| Gatekeeper | 3.12.0 |
| Cert-Manager | v1.12.3 |
| Velero | 3.1.6 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/full-migration).