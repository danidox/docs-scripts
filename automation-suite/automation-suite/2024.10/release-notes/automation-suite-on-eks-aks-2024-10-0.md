---
title: "2024.10.0"
visible: true
slug: "automation-suite-on-eks-aks-2024-10-0"
---

**Release date: November 11, 2024**

## Support for full migration

Full migration is now supported in Automation Suite 2024.10.0.

Compared to the full migration steps in Automation Suite 2023.10, in this version there is an additional migration step in which you can update the schema of the Insights and Orchestrator databases after previously restoring them.

Also, we implemented the following improvements in the `UiPath.OrganizationMigrationApp` tool:

* We provide an inner exception during a database connection test for enhanced error logging and debugging.
* We improved the merging process of single sign-on users (SSO) from multiple organizations to handle database conflicts more efficiently. The update also provides accurate migration success messages and prevents potential data duplication. This enhancement significantly benefits organizations utilizing the MSI to Automation Suite setup with a multi-tenant configuration and SSO.

For more details, refer to [Performing a full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/full-migration).

**Release date: November 11, 2024**
:::important
**Erratum - added January 23, 2025**: We have identified an issue with Integration Service on Automation Suite 2024.10.0, which can cause increased infrastructure load, if misconfigured. As a result, we have removed Integration Service from the mentioned versions. Integration Service will be available again in Automation Suite 2024.10.2. If you already use Integration Service on Automation Suite 2024.10.0, reach out to the [UiPath Product Support](https://www.uipath.com/company/contact-us/contact-technical-support) for more details.
:::

## What's new

### New products onboarded to Automation Suite

We are happy to announce the addition of Document Understanding modern projects, Integration Service, and Studio Web to our Automation Suite product portfolio. This expansion aligns with our aim to maintain parity with the functionalities offered via Automation Cloud.

If you plan to enable these new products, make sure to check out the [cross-product dependencies](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/cross-product-dependencies) and that you meet all the [prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/prerequisites-at-a-glance).

All the details about the installation and configuration of these newly onboarded products are available in the [Automation Suite on EKS/AKS Installation Guide](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/preparing-the-installation). For details on how make the most out of the functionality of these products, refer to the individual product guides:

* [Document Understanding Modern Projects User Guide](https://docs.uipath.com/document-understanding/automation-suite/2024.10/user-guide/about-document-understanding)
* [Integration Service for Automation Suite User Guide](https://docs.uipath.com/integration-service/automation-suite/2024.10/user-guide/introduction)
* [Studio Web for Automation Suite User Guide](https://docs.uipath.com/studio-web/automation-suite/2024.10/user-guide/overview)

### Introducing lite mode

In an attempt to make your start with Automation Suite easier and cost-effective, we are now introducing the lite mode. With it, you can start with fewer infrastructure requirements and when ready, transition to high availability for specific services.

By default, in lite mode, all services are non-high availability to save resources. However, if you want to enable high availability for certain services, you can do it by configuring the `profile` parameter in the `input.json` file.

A key benefit of lite mode is its resource efficiency. It offers full functionality without the need for high availability across all services. Consequently, the lite profile needs fewer resources, a value-added feature for infra-budget-conscious organizations.

Notably, lite mode is not just for small-scale operations. This mode is designed with scalability in mind, so as your needs grow, lite mode grows with you.

Lite mode is versatile, accommodating a wide array of scenarios, such as the following:

* You plan to explore the Automation Suite functionality without a significant infrastructural commitment.
* You start with a minimal setup but want the flexibility and ease of scaling up as the need arises.
* You aim to manage infrastructure cost by customizing the availability of services to your unique needs.
* You aim at smaller-scale use cases and prefer a system that operates efficiently with non-high availability services.

### Shared cluster support

To provide you with a wider range of deployment options and increase the flexibility of our offering, we are happy to announce that you can now deploy Automation Suite to a shared cluster, alongside your other software deployments. Deploying to a shared cluster comes as an alternative to the existing scenario of deploying Automation Suite to a dedicated cluster.

In addition to giving you more granular control over the installation process, the new shared cluster deployment scenario offers a host of other benefits:

* Increased flexibility and reduced time to deploy, thanks to the ability to leverage your existing standard operating procedures to install and manage applications.
* Lower total cost of ownership compared to deploying to a dedicated cluster provisioned specifically for Automation Suite.
* In a shared cluster installation scenario, you can complete the installation process without granting the Automation Suite installer cluster admin privileges, which enhances security by complying with the industry-wide principle of least privilege, enabling you to meet stringent governance standards.

Installing Automation Suite with reduced privileges requires you to install some components and perform some configuration steps before the actual Automation Suite installation. Here are the main steps that you must perform if you cannot grant admin privileges to the Automation Suite installer:

* Install and configure the Istio service mesh. For details, see [Installing and configuring the service mesh](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/installing-and-configuring-the-service-mesh).
* Create a service account and grant the necessary permissions for the Automation Suite installation. For details, see [Granting installation permissions](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/granting-installation-permissions).
* Bring your own ArgoCD. For details, see [Installing and configuring the GitOps tool](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/installing-and-configuring-the-gitops-tool).
* If you install Process Mining, you must install cert-manager and Dapr yourself. For details, see [Meeting the Process Mining prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/meeting-the-process-mining-prerequisites).
* Create and manage certificates yourself. For details, see [Certificates generated during installation](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/certificates-overview#certificates-generated-during-installation).

### Support for Bottlerocket

We have added Bottlerocket to the list of operating systems supported by Automation Suite on EKS. For more details, see [Kubernetes cluster and nodes](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/kubernetes-cluster-and-nodes).

### Support for workload identity on AKS

You can now avoid managing credentials by enabling AKS pods to use a Kubernetes identity, such as a service account. Workload identity also allows Kubernetes applications to access Azure resources securely with Microsoft Entra ID, based on annotated service accounts.

To learn more about workload identity, see [Workload identity configuration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/configuring-inputjson#workload-identity-configuration).

For details on the limitations of the feature, see [Known issues](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-0#workload-identity-support-limitations).

### Support for TLS 1.3

We now support Transport Layer Security (TLS) 1.3. This new TLS version brings several key improvements, being more secure than its predecessor, TLS 1.2, and offering speedier connections and improved performance.

To upgrade to TLS 1.3, change the value of the `istioMinProtocolVersion` parameter in the `input.json` file from `TLSV1_2` to `TLSV1_3`, then re-run the Automation Suite installation.

### FIPS 140-2 support on EKS

If you must comply with the Federal Information Processing Standard 140-2 (FIPS 140-2), we have good news for you. It is now possible to enable FIPS 140-2 on machines on which you plan to perform a new Automation Suite on EKS installation.

For more information on FIPS 140-2, see [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/security-and-compliance#fips-140-2).

For details on the limitations of the feature, see [Known issues](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-0#known-issues-fips-140-2-support-limitations).

### Support for Amazon Linux 2023

**Erratum - added January 27, 2025**: Automation Suite on EKS now supports Amazon Linux 2023 (AL2023).

### Support for EKS FIPS with AL2023 image

You can now install Automation Suite on nodes on which you enabled FIPS using the Amazon Linux 2023 (AL2023) image. This update aligns with the transition that Amazon made from AL2 to AL2023.

### [Preview] Generating the configuration file using a GUI-based wizard

Navigating through the intricacies of a platform configuration, involving multiple flags and parameters, can at times be a challenging experience. To simplify this, we bring you the Automation Suite Installer Wizard, a new method for generating the Automation Suite input.json configuration file.

This GUI-centric tool guides you through the key configuration steps, prompting you to provide details about your Automation Suite installation. It requires details such as the targeted platform, environment type, storage needs, SQL database specifics, and more, subsequently generating the input.json file for you.

Despite the wizard offering an easier way to create a configuration file, some complex configuration scenarios might not yet be covered as the tool is currently in public preview. We eagerly invite you to experiment with this tool and kindly share your feedback to help us improve this feature.

For details, see [Generating the configuration file using a wizard](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/generating-the-configuration-file-using-wizard).

### Introducing FQDN update procedure

We are excited to announce that you can now update the Fully Qualified Domain Name (FQDN) of your Automation Suite cluster.

For details about the FQDN update procedure, see [Configuring the FQDN post-installation](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/configuring-the-fqdn-post-installation).

### AWS Signature Version 4 support

Automation Suite now uses AWS Signature Version 4 for all S3 API requests. This impacts the use of Automation Suite with S3 servers that do not support AWS Signature Version 4.

### SSE-KMS support

Automation Suite now supports server-side encryption with Key Management Service (SSE-KMS) on AWS S3 buckets.

For more information on SSE-KMS, see the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).

### Support for external registries that require projects

We are happy to announce that Automation Suite now supports Harbor and other external registries that require you to create a project before pushing or pulling images from the registry.

For more details, see [Uploading the Automation Suite artifacts to the external OCI-compliant registry](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/configuring-the-oci-compliant-registry#uploading-the-automation-suite-artifacts-to-the-external-oci-compliant-registry) and [External OCI-compliant registry configuration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/configuring-inputjson#external-oci-compliant-registry-configuration).

### sfcore no longer optional

The `sfcore` component is now mandatory, and you can no longer exclude it from the Automation Suite installation. For information on how to manage optional components, see [Bring your own components](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/configuring-inputjson#bring-your-own-components).

### Apps subdomain requirement

To take full advantage of the features that Apps offers, you now must provide a unique subdomain with a Fully Qualified Domain Name (FQDN). You must make the following changes:

* Update your certificate with a Subject Alternative Name (SAN) entry for Apps. [Details...](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/certificate-requirements#tls-certificate-requirements)
* Adjust your DNS server to accommodate the new Apps subdomain. [Details...](https://docs-dev.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/networking#dns-configuration)

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

### Enhanced prerequisites check output

The prerequisites check output generated by `uipathctl` is now more user-friendly. The simplified and organized display enhances readability and gives more control over the type of info you get.

If you need more detailed information, you can use the `--verbose` flag to access the full, detailed output. If more concise information suits your needs better, simply skip the `--verbose` flag for a clear, easy-to-understand output.

For more details about prerequisites check, see [Prerequisite checks](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/prerequisite-checks).

### UiPath Automation Suite Install Sizing Calculator enhancements

We're happy to announce various fixes and improvements that ensure an even more accurate estimate of the hardware requirements for any Automation Suite deployment. The tool now takes into account the additional data disk required by Document Understanding and AI Center. Also, it now takes a single click to share the UiPath Automation Suite Install Sizing Calculator URL along with your currently selected configuration.

If you want to take the UiPath Automation Suite Install Sizing Calculator for a spin, see [Capacity planning](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/capacity-planning).

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

## Bug fixes

* We fixed an issue that caused the `uipathctl` binary to ignore any SQL connection string you provided in the `orchestrator.testautomation` section of the cluster configuration file.
* Running a health check on AKS led to an `[ARGOCD_REDIS_PODS]` failure for ArgoCD Redis HA, although ArgoCD Redis HA is no longer used in Automation Suite on AKS. The behavior no longer occurs.
* In a proxy environment, if the proxy server used the same port as the TCP port of any other service in the Istio service mesh, such as port 8080, pods could not communicate with the FQDN, and an error message was displayed. The behavior no longer occurs.
  :::note
  If you previously created a service entry according to the workaround in [Pods cannot communicate with FQDN in a proxy environment](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/pods-cannot-communicate-with-fqdn-via-proxy), we recommend that you delete the service entry after you upgrade to Automation Suite 2024.10.0 or later. To delete the service entry, use the following command: assignment
  ```
  kubectl delete serviceentry proxy -n uipath
  ```
  :::
* We have fixed an issue that prevented licenses from being allocated at the organization level.

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights and Integration Service are not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable these services.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/security-and-compliance).

### Log streaming does not work in proxy setups

**Erratum - added June 26, 2025:** Log forwarding does not work in proxy setups because the proxy environment variables were not set in the logging pods. To address the issue, refer to the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/log-streaming-does-not-work-in-proxy-setups) section.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-4#bug-fixes).

### Deployment issue on shared EKS clusters with custom namespace

**Erratum - added June 26, 2025:** An issue causes the Automation Suite deployment on a shared EKS cluster to fail if the target namespace is not `uipath`. This issue is due to the network policy incorrectly expecting the presence of a `uipath` namespace regardless of the chosen namespace.

To address the issue, you must manually create a `uipath` namespace before deploying Automation Suite.

We have fixed this issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-4#bug-fixes).

### Kubernetes upgrade failure

**Erratum - added June 26, 2025**: An issue causes the Kubernetes upgrade to fail due to an incorrect configuration in Integration Service. The upgrade failure triggers the following error message: `Cannot evict pod as it would violate the Pod’s disruption budget`.

To address the issue, you must increase the replica count of `intsvcs-periodic`deployment using the following command:

```
kubectl scale deployment intsvcs-periodic --replicas=2 -n  uipath
```

We have fixed this issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-4#bug-fixes).

### Licensing SQL connection error

**Erratum - added June 26, 2025:** Licensing SQL connection errors occur when the Data Source property specified both a named instance and a port.

We fixed the issue in [Automation Suite 2024.10.4](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-4#bug-fixes).

### Service disruptions due to automatic secret rotation

**Erratum - added May 14, 2025**: An issue causes service disruptions due to the automatic secret rotation, making services temporarily inaccessible.

To address this issue, take the following steps:

1. Restart the affected service to restore its normal functionality.
2. Navigate to the ArgoCD UI and from the platform applicatio, select **Details** &gt; **Parameters**. Edit the values to add `"secretRotation: enabled: false"` under `identity-service`. You must take this step after each Automation Suite upgrade or reinstallation.

For AI Center, all skills must be stopped and started from AI Center UI.

### OAuth token refresh issue due to incorrect version

**Erratum - added April 28, 2025:** Due to an incorrect version of `intsvcs/oauth-token-refresh` configured at the service level, the OAuth token refresh job is attempting to fetch a version that is not available in the UiPath offline registry. This causes issues during execution.

We have fixed this issue in Automation Suite [2024.10.3](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-3#bug-fixes).

### Insights dashboards and Studio Web data excluded from backups

**Erratum - added April 2, 2025:** An issue is preventing the inclusion of Insights dashboards and Studio Web data in backups. To address this issue, refer to the [Backing up the cluster](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/backing-up-the-cluster#prerequisites) page. The issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-2#bug-fixes).

### Orchestrator and AI Center require SQL Sever version 2019 and higher

**Erratum - added February 27, 2025**: For this version of Automation Suite, you need to use SQL Server version 2019 or higher for proper operation of Orchestrator and AI Center.

### Fluentd logs transmission failure

**Erratum - added February 17, 2025**: An issue prevents Fluentd from sending logs to remote locations due to a lack of memory buffer. This is due to the memory buffer limit being set to 5MB by default. To address this issue, you must increase the memory buffer limit for Fluentd to prevent disruptions or delays when transmitting logs to a remote location.

This issue is fixed in [Automation Suite 2024.10.2](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-2#bug-fixes).

### Microsoft Entra ID limitations

**Erratum - added January 20, 2025**: Insights, Studio Web, and Task Mining do not currently support Microsoft Entra ID (formerly Azure Active Directory) authentication configuration for access to SQL, storage, and other resources that support Microsoft Entra.

### Installation issue when using SQL Server version prior to 2019

**Erratum - added December 18, 2024**: Using an SQL Server version prior to 2019 causes an Automation Suite installation issue due to the Resource Catalog service not supporting SQL Server versions prior to 2019. We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-1#bug-fixes).

### Insights volumes created in two different zones following migration

When you migrate from Automation Suite on Linux to Automation Suite on EKS/AKS, Insights-related volumes are occasionally created in two different zones. As a result, you may encounter problems when bringing up the Insights service. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/insights-pvs-created-in-two-different-zones-following-migration).

We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-1#bug-fixes).

### Unable to access Automation Hub following Automation Suite upgrade

**Erratum - added December 18, 2024**: Following an upgrade to Automation Suite 2024.10, you cannot access Automation Hub due to database schema discrepancies. To address the problem, see [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/unable-to-access-automation-hub-following-upgrade-to-automation-suite-2024-10-0).

We fixed the issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-1#bug-fixes).

### Upgrade failure due to overridden Insights PVC sizes

**Erratum - added December 18, 2024:** An issue causes upgrades to fail when the existing Insights PVC sizes are inadvertently overridden. To address this problem, you must manually change the PVC sizes in ArgoCD UI. For details, see the [Troubleshooting](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/upgrade-fails-due-to-overridden-insights-pvc-sizes) section.

We fixed this issue in [Automation Suite 2024.10.1](https://docs.uipath.com/automation-suite/automation-suite/2024.10/release-notes/automation-suite-on-eks-aks-2024-10-1#bug-fixes).

### Insights dashboards backup issue

**Erratum - added December 18, 2024** We have identified an issue with the backup logic in Automation Suite for AKS/EKS. Specifically, this defect excludes the backup of Insights dashboards. However, all historical data is successfully backed up.

We are working diligently to resolve this issue. We aim to develop and implement a mitigation approach as early as possible.

If you are using Automation Suite on AKS/EKS along with UiPath Insights, this defect may affect your operations. While we address this issue, we suggest [manually exporting your dashboards](https://docs.uipath.com/insights/automation-suite/2024.10/user-guide/dashboards#exporting-and-importing-dashboards) as a preventive measure.

Note that backups are mainly used as a recovery method in the event of a disaster-level incident or in preparation for an Automation Suite upgrade. This is particularly useful if an upgrade fails and stored data needs to be restored to its previous state.

### Full migration from standalone products to Automation Suite not supported

You cannot currently perform a full migration from standalone products version 2024.10 to Automation Suite 2024.10 using the UiPath.OrganizationMigrationApp tool. We are actively working on introducing support for this scenario.

In the meantime, you can perform a single-tenant migration. For details on this migration option, refer to [Single tenant migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-openshift/using-the-migration-tool).

### Document Understanding limitations and known issues

In this release, Document Understanding modern projects are not supported in Automation Suite offline deployments and Azure Government environments.

Generative AI features, including Generative Annotation and Generative Extraction, are not currently available in Document Understanding in Automation Suite.

If Document Understanding is enabled on your tenant without the activation of Document Understanding modern projects, the Document Understanding application (accessible from the list on the left side) will not work.

For more information, refer to the [Document Understanding Release Notes](https://docs.uipath.com/document-understanding/automation-suite/2024.10/release-notes/release-notes-document-manager-2024-10-0) guide.

### Integration Service limitations

* Integration Service is not currently supported on machines with Federal Information Processing Standards 140-2 (FIPS 140-2) enabled.
* Integration Service does not currently support offline environments.

### Studio Web limitations

* Studio Web is not currently supported on machines with Federal Information Processing Standards 140-2 (FIPS 140-2) enabled.
* Autopilot™ functionalities are currently not supported.
* The default UiPath project templates are not available. You can, however, create a project from templates created by your organisation.
* Studio Web does not currently support workload identity, Azure for US Government environments, and offline environments.

### Workload identity support limitations

Studio Web, Insights, and Task Mining do not support workload identity. If you enable workload identity, you must disable these products.

### FIPS 140-2 support limitations

Studio Web, Insights, and Integration Service are not supported on FIPS 140-2. If you install Automation Suite on FIPS 140-2-enabled machines, you must disable these products.

### Forwarding logs to Splunk is currently unavailable

Forwarding infrastructure logs to Splunk is currently not possible in Automation Suite 2024.10 because the Splunk Connect plugin for Kubernetes is no longer supported. The OpenTelemetry Collector, which you can use to gather logs, is also not supported in this Automation Suite version.

For more information on managing external tools, refer to [Responsibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide/responsibility-matrix).

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
|  |  | [Studio Web 2024.10.0](https://docs.uipath.com/studio-web/automation-suite/2024.10/release-notes/2024-10-0) |  |
|  |  | [Integration Services 2024.10.0](https://docs.uipath.com/integration-service/automation-suite/2024.10/release-notes/2024-10-0) |  |

### Internal third-party component versions

This Automation Suite release bundles the following internal components:

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

| Component | Version |
| --- | --- |
| Istio | 1.23.0 |
| ArgoCD | 2.11.3 |
| Prometheus | 2.54.1 |
| Grafana | 11.1.5 |
| Fluentd and Fluent-bit | logging-operator: 4.9.1  logging-operator-logging: 4.9.1 |
| Gatekeeper | 3.17.0 |
| Cert-Manager | 1.14.5 |
| Velero | 6.2.0 |

### Migration tool version

The migration tool version you need depends on the standalone products you plan to migrate and the targeted Automation Suite version. For more details, see [Migration compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/migration-compatibility-matrix).

For instructions on migrating a standalone product to the current version of Automation Suite, see [Full migration](https://docs.uipath.com/automation-suite/automation-suite/2024.10/installation-guide-eks-aks/full-migration).