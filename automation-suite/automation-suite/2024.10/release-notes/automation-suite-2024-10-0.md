---
title: "2024.10.0"
visible: true
slug: "automation-suite-2024-10-0"
---

**Release date: November 11, 2024**

## Support for new RHEL version

We have expanded our OS support to include RHEL 9.6. For details on the supported RHEL versions, see [Compatibility Matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/hardware-and-software-requirements#rhel-compatibily-matrix).

**Release date: September 24, 2025**

## Support for full migration

Full migration is now supported in Automation Suite 2024.10.0.

Compared to the full migration steps in Automation Suite 2023.10, in this version there is an additional migration step in which you can update the schema of the Insights and Orchestrator databases after previously restoring them.

Also, we implemented the following improvements in the `UiPath.OrganizationMigrationApp` tool:

* We provide an inner exception during a database connection test for enhanced error logging and debugging.
* We improved the merging process of single sign-on users (SSO) from multiple organizations to handle database conflicts more efficiently. The update also provides accurate migration success messages and prevents potential data duplication. This enhancement significantly benefits organizations utilizing the MSI to Automation Suite setup with a multi-tenant configuration and SSO.

For more details, refer to [Performing a full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/full-migration).

**Release date: November 11, 2024**

## What's new

### Document Understanding modern projects onboarded to Automation Suite

We are happy to announce the addition of Document Understanding modern projects to our Automation Suite product portfolio. This expansion aligns with our aim to maintain parity with the functionalities offered via Automation Cloud.

If you plan to enable Document Understanding modern projects, make sure to check out the [cross-product dependencies](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/cross-product-dependencies) and that you meet all the [prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/hardware-and-software-requirements#prerequisites-at-a-glance). Note that Document Understanding modern projects require [additional resources](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/hardware-and-software-requirements#individual-products%3A-hardware-requirements), so make sure to take that into account when enabling this product.

All the details about the installation and configuration of these newly onboarded products are available in the [Automation Suite on Linux Installation Guide](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/hardware-and-software-requirements). For details on how make the most out of the functionality of these products, refer to [Document Understanding Modern Projects User Guide](https://docs.uipath.com/document-understanding/automation-suite/2024.10/user-guide/about-document-understanding).

### Introducing lite mode

In an attempt to make your start with Automation Suite easier and cost-effective, we are now introducing the lite mode. With it, you can start with fewer infrastructure requirements and when ready, transition to high availability for specific services.

By default, in lite mode, all services are non-high availability to save resources. However, if you want to enable high availability for certain services, you can do it by configuring the `profile` parameter in the `cluster_config.json` file or through the use of our interactive installer.

A key benefit of lite mode is its resource efficiency. It offers full functionality without the need for high availability across all services. Consequently, the lite profile needs fewer resources, a value-added feature for infra-budget-conscious organizations.

Notably, lite mode is not just for small-scale operations. This mode is designed with scalability in mind, so as your needs grow, lite mode grows with you.

Lite mode is versatile, accommodating a wide array of scenarios, such as the following:

* You plan to explore the Automation Suite functionality without a significant infrastructural commitment.
* You start with a minimal setup but want the flexibility and ease of scaling up as the need arises.
* You aim to manage infrastructure cost by customizing the availability of services to your unique needs.
* You aim at smaller-scale use cases and prefer a system that operates efficiently with non-high availability services.

### Unifying command line operations with uipathctl

We are thrilled to share that `uipathctl` extends its role in Automation Suite, as part of our initiative to unify our CLI tools. `uipathctl` heads toward becoming a stronger and a more convenient single entry point for all your tasks within Automation Suite.

This streamlines your installation and configuration of Automation Suite and creates a more integrated experience.

As a result, `uipathctl` replaces the following scripts and assimilates their functionalities:

* `install-uipath.sh`, previously used to install and customize Automation Suite .
* `configureUiPathAS.sh`, previously used to perform operations within the Automation Suite cluster, such as the certificate management, as well as the configuration of objectstore, registry, and monitoring tools.
* `configureUiPathDisks.sh`, previously used to configure disks and mounting points for your new Automation Suite cluster, as well as resize data disks post-installation.
* `validateUiPathReadiness.sh`, previously used to validate and install the RPM packages and to validate the prerequisite checks required when installing Automation Suite.
* `orchestrator_configurator.sh`, previously used to configure files and settings within the Orchestrator deployment in Automation Suite, such as adding storage files, credential store plugins, NLog extensions, and changing `appSettings`.

We look forward to sharing further enhancements with you.

For more details on the commands you can run, see [uipathctl](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/uipathctl).

### RHEL supported versions

**Erratum - added November 21, 2024:** We have expanded our OS support to include RHEL 8.8, 8.9, 8.10, 9.2, and 9.4 versions.

Red Hat no longer supports RHEL 8.6. As a result, we have removed it from the list of compatible RHEL versions.

:::important
**Erratum - added February 17, 2025:** RHEL kernel version `kernel-4.18.0-477.10.1.el8_8` is affected by [an issue](https://access.redhat.com/solutions/7014646) that interrupts the installation or management of the Automation Suite cluster. Make sure that none of the Automation Suite nodes uses this kernel version either pre- or post-installation. You can update the kernel version by running the following command: assignment
```
dnf install -y kernel kernel-tools kernel-tools-libs
```
:::

### AWS Signature Version 4 support

Automation Suite now uses AWS Signature Version 4 for all S3 API requests. This impacts the use of Automation Suite with S3 servers that do not support AWS Signature Version 4.

### SSE-KMS support

Automation Suite now supports server-side encryption with Key Management Service (SSE-KMS) on AWS S3 buckets.

For more information on SSE-KMS, see the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).

### Support for TLS 1.3

We now support Transport Layer Security (TLS) 1.3. This new TLS version brings several key improvements, being more secure than its predecessor, TLS 1.2, and offering speedier connections and improved performance.

For details on how to upgrade from TLS 1.2 to TLS 1.3, refer to [How to address weak ciphers in TLS 1.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/how-to-address-weak-ciphers-in-tls-12).

### Support for external registries that require projects

We are happy to announce that Automation Suite now supports Harbor and other external registries that require you to create a project before pushing or pulling images from the registry.

For more details, see [Uploading the Automation Suite artifacts to the external OCI-compliant registry](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/configuring-the-oci-compliant-registry#uploading-the-automation-suite-artifacts-to-the-external-oci-compliant-registry) and [External OCI-compliant registry configuration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/external-oci-compliant-registry-configuration).

### New prerequisite checks

We have added more prerequisite checks to optimize the overall experience of installing and configuring Automation Suite and to catch missing requirements earlier. Here are some highlights:

* Automation Suite now checks if the external objectstore supports POST requests to buckets via pre-signed URLs. Document Understanding requires POST request support to download files from the buckets.
* We have introduced a new prerequisite check for configurations using a single node RKE2 with in-cluster storage. An additional disk of a minimum 512GB is now required to store Ceph data backups. To partition the disk for Ceph, you must use the following command:
  ```
  ./bin/uipathctl rke2 disk --backup-disk-name <disk-name>
  ```
* A new prerequisite check validates that you have enough disk space to enable Document Understanding modern projects. This check verifies disk space availability on the `/datadisk/registry` and `/var/lib/rancher` disks.

### Instance Metadata Service Version 2 support

We now support Instance Metadata Service Version 2 (IMDSv2) in high-availability deployments for AWS. For more information on IMDSv2, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html).

### Apps subdomain requirement

To take full advantage of the features that Apps offers, you now must provide a unique subdomain with a Fully Qualified Domain Name (FQDN). You must make the following changes:

* Update your certificate with a Subject Alternative Name (SAN) entry for Apps. [Details...](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/certificate-requirements#server-certificate-requirements)
* Adjust your DNS server to accommodate the new Apps subdomain. [Details...](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/configuring-the-dns)

### Automatic rotation for identity token-signing certificates

Automation Suite 2024.10 introduces automatic identity token-signing certificate rotation. This feature automates the lifecycle of your signing keys, offering enhanced security and reducing the need for manual certificate management.

If you're deploying Automation Suite 2024.10 for the first time, this feature is enabled by default. The option for manual management of signing certificates remains available, and those who prefer manual control or have specific operational requirements can disable automatic certificate rotation.

For users upgrading to 2024.10 from an older version, automatic management is disabled by default but can be enabled if desired.

For details on how to enable or disable automatic certificate rotation, see [Automatic certificate rotation](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/managing-the-certificates#automatic-certificate-rotation) in the Automation Suite on Linux documentation, or [Automatic certificate rotation](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/managing-the-certificates#automatic-certificate-rotation) in the Automation Suite on AKS/EKS documentation.

### Licensing news

#### New consumables monitoring option

You can now monitor license allocation in a more granular fashion, with the help of the new **Consumables** tab. It is available in the administration section, at the organization and the tenant level, and it breaks down the allocation and the usage of licensed consumption units, such as AI Units, Robot Units, and API calls.

#### Introducing SAP Transport Units

A new type of service consumption unit, named [SAP Transport Units](https://docs-staging.uipath.com/overview/other/latest/overview/service-licensing#sap-transport-units), is now available. It is used to license the [SAP Change Impact Analysis](https://docs.uipath.com/test-suite/automation-cloud/latest/user-guide/change-impact-analysis) feature within Test Manager.

#### Changes to license-related tenant limitations

If you have a license that includes any of the following services, you will be happy to know that they can now be enabled on an unlimited number of tenants:

* Automation Hub
* Process Mining
* Test Manager
* Insights

#### Removing the license overallocation banner

Up until now, when the number of licenses allocated to your services exceeded the number of licenses available for your organization, a warning banner was displayed. However, it did not provide any clear overallocation information, nor did it offer action items for solving the issue.

As such, in an effort to enhance user experience and eliminate any distractions, we have decided to remove it. You can still find all relevant details by checking the allocation drawer.

#### Licensing Process Mining through AI units

Process Mining is now licensed through AI units, just like several of our AI products.

For details on consumption, see the [License](https://docs.uipath.com/process-mining/automation-cloud/latest/user-guide/pm-enabling-the-service-in-automation-cloud#license) page in the Process Mining guide.

#### Deprecating license activation from the host portal

We are striving to better support the ever evolving commercial offering of the UiPath® platform, and, as part of that, we are [deprecating](https://docs.uipath.com/overview/other/latest/overview/deprecation-timeline#automation-suite) the option to activate licenses from the host portal. To help ease the transition, we have added a warning banner notifying administrators of the deprecation, and providing best practices for license activation.

Please rest assured that this in no way affects the functionality, and that you can still activate licenses from the host portal until the feature is [removed](https://docs.uipath.com/overview/other/latest/overview/deprecation-timeline#automation-suite-upcoming-removals).

### Personal access tokens (PATs)

We are excited to introduce personal access tokens (PATs). PATs provide developers with an efficient and secure method to obtain tokens with user-scoped access. PATs can limit risk when working with applications or automations that do not allow for other authentication mechanisms, or where you do not want to provide your credentials. If the app is compromised, you simply revoke the PAT.

:::note
Personal Access Tokens are only available for local users.
:::

The core capabilities:

* Users removed from an organization will have their associated PATs automatically revoked to prevent unauthorized access.
* Organization administrators can manage issued PATs, enabling easy revocation of access when necessary.

For detailed information on implementing PATs, please refer to the docs on [personal access tokens](https://docs.uipath.com/automation-suite/automation-suite/2024.10/api-guide/personal-access-tokens).

### Managing personal access tokens

Personal access tokens (PATs) can be managed by organization administrators. PATs can limit risk when working with applications or automations that do not allow for other authentication mechanisms, or where you do not want to provide your credentials. If the app is compromised, you simply revoke the PAT.

:::note
Personal Access Tokens are only available for local users and managed by organization administrators.
:::

Organization administrators can manage issued PATs, enabling easy revocation of access when necessary.

For detailed information on managing PATs, please refer to [Managing PATs](https://docs.uipath.com/automation-suite/automation-suite/2024.10/admin-guide/external-applications-personal-access-tokens).

## Improvements

### In-place upgrade enhancements

To ensure a more secure stack and minimize common vulnerabilities and exposures, we’ve increased the frequency of Kubernetes updates.

Typically, Kubernetes requires sequential version upgrades, which can mean multiple intermediate steps to upgrade to your target Automation Suite version. In Automation Suite 2024.10, we’ve introduced chained Kubernetes upgrades, allowing you to reach your target Automation Suite version directly, without intermediate jumps. The entire process is handled seamlessly in the background.

You can now upgrade from, for instance, Automation Suite 2023.10.2 to 2024.10.0, progressing through multiple Kubernetes versions automatically. The enhancement ensures a secure stack, with an even smoother upgrade experience.

To accommodate this improvement, you should know that we have made several modifications in the upgrade workflow. These changes include updates to existing steps or new additions, such as the following ones:

* Running the prerequisite checks, separately for infrastructure and services;
* Migrating Longhorn workloads to local PV, shifting MongoDB data to SQL, and moving Ceph to a Helm-based deployment, before the actual upgrade;
* Installing the services and shared components to their target version.

Also, one additional change is that, where applicable, you now use `uipathctl` for the in-place upgrade commands.

For more details, see [Performing an in-place upgrade](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/performing-an-in-place-upgrade).

### Extended support for Active/Active deployments

We have extended the list of products that you can deploy in Active/Active mode. Previously, this feature was only available for Orchestrator, but we have now also included the following products to give you more flexibility:

* Action Center
* AI Center
* Apps
* Automation Ops
* Automation Suite Robots
* Computer Vision
* Data Service
* Document Understanding
* Test Manager

For details, refer to [Disaster recovery - Active/Passive and Active/Active](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/disaster-recovery).

### Simplified installation process for enhanced efficiency

We have improved our installation experience by reducing the number of steps required by the installation process. Now, this process involves two main parts, namely the infrastructure installation and the cluster installation. With these improvements to the installation flow, you can expect considerably reduced installation time.

### Enhanced shared components management using OSS base

We are excited to announce a significant improvement focused on the management of shared components.

In previous versions, we relied heavily on a component delivery system provided by Rancher. While effective, this approach has its challenges, notably dealing with inconsistent component versions.

Now, we have shifted towards an Open-Source Software (OSS) base for our component management. Furthermore, we leverage `uipathctl` for installing and upgrading components.

This strategic shift not only simplifies the shared components installation process but also provides the ability to manage each component individually. Moreover, you can also expect improved time efficiency in the reinstallation process for individual components.

### Enhanced backup and restore flow

We have enhanced the configuration instructions for the external NFS server to ensure a smoother backup and restore experience. We now include guidance to create a subdirectory at the `/asbackup/asetcdbackup` location or your equivalent NFS mount path, in order to prevent any potential mounting issues. For details on the updated commands, refer to [Configuring the mount path](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/setting-up-the-external-nfs-server#step-2%3A-configuring-the-mount-path).

### Images cleanup for in-cluster Docker registry

You can now effortlessly remove obsolete images post-upgrade. This capability is specifically designed for offline setups with an in-cluster Docker registry. For more details, see [Performing post-upgrade operations](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/performing-post-upgrade-operations).

### UiPath Automation Suite Install Sizing Calculator enhancements

We're happy to announce various fixes and improvements that ensure an even more accurate estimate of the hardware requirements for any Automation Suite deployment. The tool now takes into account the additional data disk required by Document Understanding and AI Center. Also, it now takes a single click to share the UiPath Automation Suite Install Sizing Calculator URL along with your currently selected configuration.

If you want to take the UiPath Automation Suite Install Sizing Calculator for a spin, see [Capacity planning](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/capacity-planning).

### FQDN update enhancement

We are thrilled to announce an enhancement in our Fully Qualified Domain Name (FQDN) update process. Now, you can update the cluster FQDN from a single machine, replacing the previous multi-step procedure. This update is aimed at simplifying the process, making it more user-friendly and efficient.

For more on the FQDN update process, see [Configuring the FQDN post-installation.](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/configuring-the-fqdn-post-installation)

### Istio dashboards management

The Istio-related dashboards are switched off by default. If you need to use these dashboards, you must enable them through additional configuration steps within the ArgoCD UI. However, be aware that enabling these dashboards could impact Istio performance.

For more details about Istio dashboards, see [Monitoring the network](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/dashboards-and-metrics#monitoring-the-network).

### Enhanced prerequisites check output

The prerequisites check output generated by `uipathctl` is now more user-friendly. The simplified and organized display enhances readability and gives more control over the type of info you get.

If you need more detailed information, you can use the `--verbose` flag to access the full, detailed output. If more concise information suits your needs better, simply skip the `--verbose` flag for a clear, easy-to-understand output.

For more details about prerequisites check, see [Prerequisite checks](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/validating-the-prerequisites-for-the-installation#overview).

### Security enhancements

We continue to provide security updates and patches to address Common Vulnerabilities and Exposures (CVEs).

### SAML SSO improvements

We've rolled out some significant updates geared towards improving SAML SSO. Here's a quick overview of what's new:

1. **Switching between entity ID formats:** When getting the UiPath details for the identity provider setup, you can now change between the legacy entity id format (without the organization ID), and the new format that includes the organization ID.
2. **Custom unique identifier:** We've introduced the option to set custom attributes for unique identification. This feature is particularly beneficial if :
   * An email address is not allocated to your users.
   * An email address cannot serve as a unique identifier (they are not unique in the identity provider).
   :::important
   Once you've set a **Unique Identifier**, changing it can result in a loss of previously recognized users, as the system might not be able to identify them anymore.
   :::
3. **Signing authentication requests:** This feature allows UiPath sign all SAML authentication requests. This is useful if your identity provider requires signed authentication requests.
4. **Single logout:** Our SAML configuration now includes Single Logout (SLO) capabilities, which enable simultaneous logouts across all your applications unified under your identity provider.

### High contrast theme option

We have introduced a high contrast theme that ensures enhanced contrast for a set of UI elements.

For more information, refer to [Selecting the theme](https://docs.uipath.com/automation-suite/automation-suite/2024.10/admin-guide/managing-user-preferences#selecting-the-theme).

### Service visibility in the UI

You can now manage the visibility of three new services in the left navigation bar, in order to customize the UI for each user:

* Automation Hub
* AI Center
* Process Mining

For more information, see the [Hide unused services](https://docs.uipath.com/automation-suite/automation-suite/2024.10/admin-guide/managing-organization-settings#hiding-unused-services) documentation.

### Optional Docker pull secret value

**Erratum - added April 28, 2025:** The `registries.docker.pull_secret_value` field, which needs to be provided in the `cluster_config.json` file, is now optional.

## Bug fixes

* **Erratum - added December 18, 2024**: If you resized the `rook-ceph` OSD PV, the new size did not persist following an Automation Suite upgrade. Now, the upgrade automatically inherits and retains the updated `rook-ceph` OSD PV size.
* We fixed an issue that caused the `uipathctl` binary to ignore any SQL connection string you provided in the `orchestrator.testautomation` section of the cluster configuration file.
* We fixed an issue where the installation or upgrade failed on AWS machines where only IMDSv2 was enabled.
* In a proxy environment, if the proxy server used the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods could not communicate with the FQDN, and an error message was displayed. The behavior no longer occurs.
  :::note
  If you previously created a service entry according to the workaround in [Pods cannot communicate with FQDN in a proxy environment](https://docs.uipath.com/automation-suite/automation-suite/2023.10/pods-cannot-communicate-with-fqdn-via-proxy), we recommend that you delete the service entry after you upgrade to Automation Suite 2024.10.0 or later. To delete the service entry, use the following command: assignment
  ```
  kubectl delete serviceentry proxy -n uipath
  ```
  :::
* We have fixed a `uipathctl`-related issue that caused registry configuration corruption during upgrades. Previously, a port in the helm URL of `cluster_config.json` was treated as an external registry, leading to an omission in `registries.yaml`. Now, `insecure_skip_verify: true` is correctly included in`registries.yaml`, regardless of whether or not a port is present in the helm URL.
* We have fixed an issue where shutting down the`rke2-server` service without executing `rke2-killall.sh` could lead to intermittent not ready reports from agent machines.
* We have fixed an issue causing upgrades from Automation Suite 2023.10.x to fail due to the Longhorn storage classes still being present after uninstalling Longhorn.
* We have fixed an issue that caused the support bundle to not include historical logs and to not upload to the configured external object store. This issue occured in offline environments using an external OCI registry.
* We have fixed an issue causing the `snapshot-controller-crds` pod to remain in the CrashLoopBackOff state after an RKE2 upgrade. This issue occurred due to a conflict between the newly installed `snapshot-controller` and the existing one during the RKE2 upgrade.
* We have fixed an issue that prevented you from enabling SSO for ArgoCD due to a Dex image version discrepancy.
* We have fixed an issue that prevented licenses from being allocated at the organization level.
* We have fixed an issue that caused problems during the upgrade process if you had resized the Docker-registry PVC used by your in-cluster Docker registry. Now, the new size is accurately recognized and considered during the upgrade process.

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

### Agent node addition failure in offline environments

**Erratum - added June 26, 2025:** An issue causes the addition process of agent nodes in offline environments to fail. Agent node additions require the temporary registry to be running. To address the issue, you must re-enable the temporary registry to successfully join the agent node.

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

### Orchestrator and AI Center require SQL Sever version 2019 and higher

**Erratum - added February 27, 2025**: For this version of Automation Suite, you need to use SQL Server version 2019 or higher for proper operation of Orchestrator and AI Center.

### AI Center storage migration failure

**Erratum - added February 17, 2025**: An issue prevents `uipathctl` from correctly setting `executeMigration` to `true` during the migration process from Ceph in-cluster storage to external object storage in AI Center.

To fix this issue, you must manually set `executeMigration` to `true` in ArgoCD for AI Center and then proceed with a resync, ensuring to prune. This issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-2#bug-fixes).

### Error message while uninstalling rook-ceph post migrating to a S3 object-store

**Erratum - added February 17, 2025**: When uninstalling rook-ceph, an error message related to missing external object storage configuration is displayed. This issue occurs even though the migration is succesful. This behavior is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-2#bug-fixes).

### FQDN update failure due to security configuration

**Erratum - added February 17, 2025**: An issue causes the FQDN update flow to fail due to a security configuration.

To address this issue, you must use the `uipathctl` version included in Automation Suite 2024.10.2 when you update the FQDN at the infrastructure level. To download `uipathctl`, see [Installation packages download links](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/installation-packages-download-links#uipathctl).

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

### Installation issue when using SQL Server version prior to 2019

**Erratum - added December 18, 2024**: Using an SQL Server version prior to 2019 causes an Automation Suite installation issue due to the Resource Catalog service not supporting SQL Server versions prior to 2019. We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Data loss when reinstalling or upgrading Insights following Automation Suite upgrade

**Erratum - added December 18, 2024**: Following an Automation Suite upgrade from version 2023.4 or older, reinstalling or upgrading Insights results in data loss due to an issue with Insights storage class changes. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/data-loss-when-reinstalling-or-upgrading-insights-following-automation-suite-upgrade).

We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Temporary registry installation fails for RHEL 8.9

**Erratum - added December 18, 2024**: An issue causes the temporary registry installation to fail on RHEL 8.9. This issue occurs due to the deprecated `systemd generate` command in the upstream Podman and the missing `secontext` from the Podman-generated `systemd` files, which obstruct `systemd` from accessing the necessary files. To address the problem, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/temporary-registry-installation-failure-on-rhel-89) section.

We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Helm chart build failure due to SQL integration parameter

**Erratum - added December 18, 2024**: An issue causes the Helm chart build to fail when you set the `enableSqlIntegratedAuth` parameter to `true` in `values.yaml` for Kerberos SQL integration. This issue occurs due to incorrect indentation of certain environment variables.

We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Node maintenance issue in non-HA Redis

**Erratum - added December 18, 2024**: An issue causes the `redis-cluster-0` pod to get stuck in the terminating state when you perform a node drain in non-HA Redis scenarios. To address the problem, you must force delete the pod using the following command:
```
kubectl -n redis-system delete pod redis-cluster-0 --force
```

We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Node removal issue due to incorrect scaling operation naming

**Erratum - added December 18, 2024**: An isssue causes node removal operations to fail with an `error: no objects passed to scale` message. This issue occurrs due to a name mismatch during the scaling up of the Prometheus operator. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/node-removal-failure-due-to-incorrect-scaling-operation-naming).

We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Unable to access Automation Hub following Automation Suite upgrade

**Erratum - added December 18, 2024**: Following an upgrade to Automation Suite 2024.10, you cannot access Automation Hub due to database schema discrepancies. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/unable-to-access-automation-hub-following-upgrade-to-automation-suite-2024100).

We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Insights annotation issue blocks installer

**Erratum - added December 18, 2024**: An Insights annotation issue blocks the Automation Suite installer. We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Partial failure to restore backup due to Dapr sync issue

**Erratum - added December 18, 2024**: Attempting to restore a backup results in a partial failure due to a Dapr sync issue. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/partial-failure-to-restore-backup-in-automation-suite-2024-10-0).

We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Case sensitivity issue in hostname validation

**Erratum - added December 18, 2024:** An issue causes the prererequisite checks to incorrectly identify hostnames with capital letters as invalid. To address this problem, you must use lowercase letters for hostnames. We fixed this issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Upgrade failure due to overridden Insights PVC sizes

**Erratum - added December 18, 2024:** An issue causes upgrades to fail when the existing Insights PVC sizes are inadvertently overridden. To address this problem, you must manually change the PVC sizes in ArgoCD UI. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/upgrade-fails-due-to-overridden-insights-pvc-sizes) section.

We fixed this issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-2024-10-1#bug-fixes).

### Unintended RKE2 service upgrade on additional nodes

**Erratum - added November 26, 2024**: We have identified an issue where `exclude= rke2-*` is not added to the `/etc/yum.conf` file on nodes other than the first server. In specific environments, particularly online ones, an attempt to upgrade all components can cause an unintentional upgrade of the RKE2 service on nodes other than the first server.

To fix this issue, you must manually add `exclude=rke2-*` to the `/etc/yum.conf` file on all the nodes of your Automation Suite cluster.

### Full migration from standalone products to Automation Suite not supported

You cannot currently perform a full migration from standalone products version 2024.10 to Automation Suite 2024.10 using the UiPath.OrganizationMigrationApp tool. We are actively working on introducing support for this scenario.

In the meantime, you can perform a single-tenant migration. For details on this migration option, refer to [Single tenant migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-openshift/using-the-migration-tool).

### Migration from Automation Suite on Linux to Automation Suite on OpenShift not supported

**Erratum - added December 18, 2024**: You cannot currently perform a migration from Automation Suite on Linux to Automation Suite on OpenShift. We are actively working on introducing support for this scenario.

### Document Understanding limitations and known issues

In this release, Document Understanding modern projects are not supported in Automation Suite offline deployments and Azure Government environments.

Generative AI features, including Generative Annotation and Generative Extraction, are not currently available in Document Understanding in Automation Suite.

If Document Understanding is enabled on your tenant without the activation of Document Understanding modern projects, the Document Understanding application (accessible from the list on the left side) will not work.

For more information, refer to the [Document Understanding Release Notes](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-document-manager-2024-10-0) guide.

### Split as.tar.gz not available

Split `as.tar.gz` is currently not available. You can use [full as.tar.gz](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/installation-packages-download-links#full-astargz) in the meantime.

### Enabling Connaisseur causes installation or upgrade failures

An issue causes installation or upgrade failures when enabling Connaisseur during the configuration of an external OCI-compliant registry. The issue occurs when you set the `registries.trust.enabled` parameter to `true` in the `cluster_config.json` file.

### Forwarding logs to Splunk is currently unavailable

Forwarding infrastructure logs to Splunk is currently not possible in Automation Suite 2024.10 because the Splunk Connect plugin for Kubernetes is no longer supported. The OpenTelemetry Collector, which you can use to gather logs, is also not supported in this Automation Suite version.

For more information on managing external tools, refer to [Responsibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/responsibility-matrix).

### Custom directory for pod logs not working

You cannot currently use custom directories for storing your pod logs. This is due to the switch to kube-logging.

### External service monitoring not enabled by default

When using kube Prometheus for service monitoring, the `ServiceMonitor` file is not tracked by default. This issue specifically affects services such as Redis or Istio when attempting to enable the `monitoringConfigure.enableEnhancedMonitoring` field.

To address the issue, you must manually add an explicit `release: monitoring` label to the `ServiceMonitor` YAML configuration file, as shown in the following configuration sample.

```
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: istio-component-monitor
  namespace: {{ .Values.monitoringConfigure.namespaces.istio }}
  labels:
    monitoring: istio-components
    release: monitoring
spec:
  jobLabel: istio
  targetLabels: [app]
  selector:
    matchExpressions:
    - {key: istio, operator: In, values: [pilot]}
  namespaceSelector:
    any: true
  endpoints:
  - port: http-monitoring
    interval: 15s
```

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

To find out what has changed on each Automation Suite product, visit the following links.

If the product is greyed out, this new Automation Suite version does not bring any changes to it.

| **DISCOVER** | **BUILD** | **MANAGE** | **ENGAGE** |
| --- | --- | --- | --- |
| [Automation Hub 2024.10.0](https://docs.uipath.com/automation-hub/automation-suite/2024.10/user-guide/release-notes-2024-10) | [Automation Ops 2024.10.0](https://docs.uipath.com/automation-ops/automation-suite/2024.10/user-guide/release-notes-2024-10-0) | [AI Center 2024.10.0](https://docs.uipath.com/ai-center/automation-suite/2024.10/user-guide/release-notes-2024-10-0) | [Action Center 2024.10.0](https://docs.uipath.com/action-center/automation-suite/2024.10/user-guide/release-notes-2024-10-0) |
| [Task Mining 2024.10.0](https://docs.uipath.com/task-mining/automation-suite/2024.10/user-guide/release-notes-2024-10) | [AI Computer Vision 2024.10.0](https://docs.uipath.com/ai-computer-vision/automation-suite/2024.10/user-guide/release-notes-2024-10-0) | [Insights 2024.10.0](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/release-notes-2024-10) | [Apps 2024.10.0](https://docs.uipath.com/data-service/automation-suite/2024.10/release-notes/2024-10-0) |
| [Process Mining 2024.10.0](https://docs.uipath.com/process-mining/automation-suite/2024.10/user-guide/process-mining-2024-10) | [Document Understanding AI Center-based projects 2024.10.0](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-document-manager-2024-10-0)  [Document Understanding modern projects 2024.10.0](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/document-understanding-modern-2024-10-0) | [Orchestrator 2024.10.0](https://docs.uipath.com/orchestrator/automation-suite/2024.10/release-notes/2024-10-0) |  |
|  |  | [Test Manager 2024.10.0](https://docs.uipath.com/test-suite/automation-suite/2024.10/release-notes/test-manager-2024-10-0) |  |
|  |  | [Data Service 2024.10.0](https://docs.uipath.com/apps/automation-suite/2024.10/release-notes/2024-10-0) |  |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| RKE2 | 1.30.5 |
| ArgoCD | 2.11.3 |
| gatekeeper | 3.17.0 |
| rook | 1.14.6 |
| ceph | 17.2.6 |
| prometheus-pushgateway | 2.12.0 |
| cert-manager | 1.14.5 |
| Istio | 1.23.0 |
| kube-logging/logging-operator | 4.9.1 |
| Prometheus | 2.54.1 |
| Grafana | 11.1.5 |
| velero | 6.2.0 |
| redis-operator | 7.4.6-2 |
| redis-cluster | 7.4.6-22 |
| oauth2-proxy | 7.6.0 |