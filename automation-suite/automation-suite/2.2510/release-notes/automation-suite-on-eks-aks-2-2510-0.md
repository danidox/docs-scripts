---
title: "2.2510.0"
visible: true
slug: "automation-suite-on-eks-aks-2-2510-0"
---

**Release date: November 11, 2025**

## What's new

### New versioning format for Automation Suite

Starting with this release, Automation Suite uses a new versioning format. The format follows the pattern `[Major].[YYMM].[Patch]`, defined as follows:

* `Major` increases when a major release is delivered.
* `YYMM` represents the year and month of the long-term support (LTS) release.
* `Patch` increments with each cumulative update (CU) after the initial LTS release.

The version format of this LTS release is `2.2510.0`. This release is the baseline for future cumulative updates.

### Introducing Test Cloud

We are excited to announce that Test Cloud is now available on-premises through the EKS/AKS deployment. This release brings the full Test Cloud experience to self-managed environments, allowing you to design, execute, and manage automated tests securely and at scale within your organization’s infrastructure.

Test Cloud enables you to design, execute, and manage automated testing at scale, while maintaining full control of your data, infrastructure, and compliance requirements.

#### Key benefits of Test Cloud

Test Cloud offers the following advantages:

* Comprehensive automation coverage: Supports varied automation types such as Citrix, Web, Desktop, SAP, Mainframe, API, and Mobile.
* Test data management: Access to diverse data sources to power data-driven testing.
* Detailed insights: Advanced analytics and reporting features for complete visibility into test performance.
* Flexible testing methods: Enables both automated and manual testing, as well as data-driven testing through services such as Data Service and Orchestrator, or generated datasets via Autopilot<sup>TM</sup>.

#### Documentation and guidance

The documentation for Test Cloud on-premises, delivered through EKS/AKS deployments is available in the following installation, admin, user, and API guides:

* [EKS/AKS installation guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/automation-suite-overview)
* [Admin guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/about-the-automation-suite-experience)
* [Test Cloud user guide](https://docs.uipath.com/test-cloud/automation-suite/2.2510/user-guide/about-test-cloud)
* [API guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/api-guide/about-this-guide)

This means that Automation Suite and Test Cloud share content across the release notes, installation, admin, and API guides.

### New products onboarded to Automation Suite

We are happy to announce the addition of Solutions and Autopilot for Everyone to our Automation Suite product portfolio. This expansion aligns with our aim to maintain parity with the functionalities offered via Automation Cloud.

If you plan to enable these new products, make sure to check out the [cross-product dependencies](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/automation-suite-products) and that you meet all the [prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/prerequisites-at-a-glance).

All the details about the installation and configuration of these newly onboarded products are available in the [Automation Suite on EKS/AKS Installation Guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/preparing-the-installation). For details on how make the most out of the functionality of these products, refer to the individual product guides:

* [Solutions For Automation Suite User Guide](https://docs.uipath.com/solutions-management/automation-suite/2.2510/user-guide/solutions-management-overview)
* [Autopilot for Everyone User Guide](https://docs.uipath.com/autopilot/other/latest/user-guide/about-autopilot-for-everyone)

### Introducing AI Trust Layer

We are excited to announce the launch of the **AI Trust Layer** in Automation Suite — your centralized control center for managing and governing all AI-related operations across the UiPath ecosystem, deployed entirely within your own infrastructure.

The AI Trust Layer provides a unified administrative and auditing interface for all UiPath GenAI capabilities and any Bring Your Own Model (BYOM) integrations you configure. It delivers the same governance, observability, and compliance features available in Automation Cloud, while ensuring that all data and model traffic remain contained within your private environment.

**Key capabilities and benefits**
* Comprehensive AI oversight – Monitor AI model-related operations and ensure transparency across all AI activities in your organization through a centralized auditing panel.
* Enhanced governance – Regulate your AI operations effectively with fine-grained control over AI policies, model usage, and governance rules.
* Usage insights – Gain a clear picture of AI utilization through the **Usage Summary** tab, helping you make data-driven decisions about how AI is used across teams.
* Autopilot for Everyone management – Manage and oversee Autopilot usage across your organization from a single interface.
* Bring your own model (BYOM) support – Use the **LLM Configurations** tab to integrate and manage your own large language models within the UiPath ecosystem.
* Improved administrative efficiency – Streamline control, auditing, and compliance workflows to ensure your AI operations remain secure, transparent, and well-governed.

For more details, refer to [AI Trust Layer](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/about-ai-trust-layer).

### Introducing Context Grounding

The [Context Grounding service](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/about-context-grounding) is now available in Automation Suite. This is a platform service that enhances UiPath generative AI experiences by enriching prompts with relevant, contextual information before they reach the large language model (LLM) using retrieval-augmented generation (RAG). With Context Grounding indexes, you can integrate your own data to achieve more accurate and reliable GenAI results.

You can create and manage indexes directly in Orchestrator, or through the UiPath GenAI Activities.

To use Context Grounding, configure your own LLM connection to an AI provider through the AI Trust Layer.

### Disaster Recovery – Active/Passive deployments

We are happy to announce that Disaster Recovery in Active/Passive configuration is now supported for Automation Suite on EKS.

Now you can configure Automation Suite in a way that can withstand the complete failure of nodes, entire data centers, or even regions.

Automation Suite deployments in Active/Passive mode support the following scenarios:

* Same-region deployment
* Cross-region deployment

For details, see [Disaster Recovery – Active/Passive](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery) and [Quick links](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/quick-links).

### Support for IPv6 and dual-stack configuration

Automation Suite now supports deployments using IPv6 and dual-stack (IPv4 and IPv6) networking.

This enhancement allows Automation Suite services and ingress components to run in environments that use IPv6-only or mixed IPv4/IPv6 networks.

For configuration details, refer to the [Networking](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/networking) section.

### Cloud provider–managed backup and restore

Automation Suite now uses the cloud provider’s managed backup solution for backup and restore operations. You must configure backups through the corresponding AWS or Azure managed services. Previously, backups were managed through the UiPath-provided backup solution.

This change aligns Automation Suite with native cloud capabilities and helps unify your organization’s backup and recovery strategy across environments.

For details, refer to [Backing up and restoring the cluster](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/backing-up-and-restoring-the-cluster).

### Secretstore support for credential management

You can now deploy Automation Suite using a secretstore to securely store and manage credentials instead of including them in the `input.json` file. This enhancement improves security and simplifies credential management during deployment.

To use a secretstore, you must have an external secrets operator configured. By default, Automation Suite includes a bundled external secrets operator. The operator synchronizes secrets from external secret management systems to the cluster, making them available for use during deployment.

You can also bring your own external secrets operator. For details, refer to [Installing the External Secrets Operator in Kubernetes](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-the-external-secrets-operator-in-kubernetes).

You can use secretstore types such as Kubernetes Secret or Azure Key Vault. When you configure a secretstore, `uipathctl` automatically retrieves the required credentials during deployment.

For details, refer to [Credentials secretstore configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#credentials-secretstore-configuration).

### Admin

#### User and group profiles

#### Unified profiles for audit and troubleshooting

We are happy to announce that we have introduced a unified view where you can check and manage all the necessary information about your user accounts and local groups. We refer to this view as user and group profiles.

User and group profiles are the solution you need to easily audit and troubleshoot your user or group configurations. Unlike before, you can now perform a wide array of operations from one single location: customize group memberships, handle licenses, monitor access, and update user and group info.

Currently, user and group profiles are available for **Organization Admin**s only.

#### How to use user and group profiles

To access user and group profiles, navigate to **Admin** &gt; **Accounts & local groups**, choose either the **User accounts** or the **Local groups** tab, then select the user account or local group you want to manage. A new window opens, allowing you to view or update your user or group configurations.

The following image shows some of the options you have for managing user profiles:
  ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/520512/500199)

For a comprehensive list of all the operations you can perform using the new user and group profiles, refer to [Managing user group and profiles.](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/managing-accounts-and-groups#managing-user-and-group-profiles)

#### Introducing the tenant administrator role

#### First cross-service role

We are excited to announce the **Tenant Administrator** role in Automation Suite.

This new cross-service role enables you to delegate responsibilities more efficiently by designating users, groups, robot accounts, or external applications to manage all resources within a given tenant.

You can now delegate tasks such as role assignment, licensing management, service provisioning, and more, to a **Tenant Administrator** without worrying about them having access to any other resources within your organization.

Ideal for RPA CoE Directors and IT Administrators, the **Tenant Administrator** role allows reassigning some tasks from an **Organization Administrator** to a tenant-level role.

#### Benefits of the Tenant Administrator role

If you are curious about the benefits of the new **Tenant Administrator** role, here they are:

* Enhanced operational efficiency: This new role reduces the time required to set up the admin for tenant-level operations;
* Reduced workload for **Organization Administrators**: It eases the burden on the Organization Administrators;
* Improved security: Since fewer users have maximum permissions, there is greater control on access rights.

You will be pleased to learn that the **Tenant Administrator** role is just the first tenant-level role we plan to introduce. Our goal is to allow you to manage cross-service roles from a central location.

#### Known limitations

The **Tenant Administrator** role is currently affected by the following known limitations, which we are actively working on overcoming:

* Only the following services support the **Tenant Administrator** role: Orchestrator (includes Actions, Processes, Integration Service), Data Service, Document Understanding, Task Mining, Test Manager. The rest of the tenant-level services are currently not supported, and users with only the Tenant Administrator role cannot access these services.
* The **Tenant Administrator** cannot access organization-level menus from the interface.
* On the **Admin &gt; Tenants &gt; Services** screen, the **Tenant Administrator** can view enabled services, but cannot add or remove services.
* On the **Admin &gt; Tenants &gt; Manage access** screen, the **Tenant Administrator** can view tenants they do not administer. However, if the **Tenant Administrator** accesses these tenants, they cannot perform any actions.

For more details on the new Tenant Administrator role and how to assign it, refer to [Tenant-level roles](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/roles#tenant-level-roles).

#### Tenant picker enhancements

We are pleased to present a new design, and functionality for the platform tenant picker.

The enhancements include a search box for easy navigation when you have multiple tenants, and the region in which each tenant's data resides.

Figure 1. Tenant picker data residency
  ![Tenant picker data residency](https://docs.uipath.com/api/binary/automation-suite/2/520512/611764)

#### Centralized access management

We are excited to introduce the centralized access management initiative. Centralized access management provides you with streamlined access management processes and enhanced customization capabilities. These features allow you to easily manage roles and permissions across your organization, improving efficiency, compliance, and troubleshooting.
  !['Centralized access management' image](https://docs.uipath.com/api/binary/automation-suite/2/520512/565020)

Explore the following key areas we updated and discover their new features:

#### Compliance and auditing

* **Export role assignments via API, or the UI**You can now export roles and role assignments for all products and services across the platform via API, or via the user interface (UI) by selecting the **Download role assignments** button in the **Accounts & local groups** menu. This feature simplifies audits, compliance, and reporting by providing a centralized view of role assignments across your environment. For more information, refer to [Export user role assignments](https://docs.uipath.com/automation-suite/automation-suite/2.2510/api-guide/export-user-role-assignments) for API instructions, or [Exporting role assignments](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/role-management#exporting-role-assignments) for UI instructions.
* **Check access folder support**Check access enables Organization Administrators and Tenant Administrators to easily review the roles and permissions assigned to users, groups, accounts, and external applications across both tenant and service level. Folder-level support is also available. You can view which roles are associated with specific folders, providing a more complete and accurate representation of access permissions across the platform. Additionally, all permission details can be exported to a CSV file for further review and reporting. To use the feature, go to **Admin** &gt; **Manage access** &gt; **Check access**, then search for any account to review its roles and permissions. For more information, refer to [Checking access](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/checking-access).

#### Centralization

* **Custom roles**Custom roles are now available at organization, tenant, and service levels. You can define new roles using a combination of permissions from one or multiple services within a tenant, ensuring tailored access control for their specific role needs. For more information, refer to [Custom roles](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/roles#custom-roles).
* **Tenant Admin role**This new cross-service role enables greater efficiency in delegating responsibilities, as users, groups, robot accounts, or external applications can manage all resources within a designated tenant. If you are an Organization Administrator, you can now delegate responsibilities such as role assignment, licensing management, and service provisioning to a **Tenant Administrator**, decreasing concerns over undesired access to other resources within your organization. For more details on the new **Tenant Administrator** role and how to assign it, refer to [Tenant-level roles](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/roles#tenant-level-roles).
* **Insights dashboard viewer role**The **Insights dashboard viewer** role is a new role at organization level that enables you to assign specific and more granular access to Insights dashboards at organization level, without having to grant users with full organization administrator privileges. This role targets access to dashboards, providing you with more control and flexibility in sharing insights across the organization. For more information, refer to [Organization-level roles](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/roles#organization-level-roles).
* **Tenant types and tagging**You can now choose the tenant type for your tenant when you create a new one by selecting **Production**, **Staging** or **Development** from the **Environment type** section in the **Create a new tenant** UI wizard. This capability makes tenant management more intuitive, freeing you from the hassle of maintaining strict naming conventions for your tenants. Additionally, this feature allows you to tag tenants based on their purpose, and streamlines administrative tasks. For more information, refer to [Adding tenants](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/managing-tenants#adding-tenants).

#### Consistency

* **The Manage access menu**We have redesigned the **Manage access** menu to ensure a consistent look across all platform levels: organization, tenant, and service. Regardless of the platform level you work at, you experience the same interface for managing roles and role assignments. This consistent approach reduces friction when navigating between different scopes and enhances overall usability. For more information, refer to [Manage access user interface based on scope](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/role-management#manage-access-user-interface-based-on-scope).

#### Redesigned left rail for enhanced navigation

In our continuous efforts to enhance your user experience, we are excited to announce a redesigned left rail in Automation Cloud to ensure you can easily access key parts of the platform.

The new left rail is custom-tailored, displaying only your favorite services and modules, which you can effortlessly personalize. All accessible services that you have access to are still available, but in order to see them, you need to expand the left rail.

To add a service to favorites, hover over it and select the gray **Favorites** icon next to the service name. To remove a service from favorites, use the orange **Favorites** icon.

Figure 2. New left-rail with favorites section
  ![New left-rail with favorites section](https://docs.uipath.com/api/binary/automation-suite/2/520512/613824)

For a comprehensive description of the new navigation experience, refer to [The left rail](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/exploring-the-user-interface#the-left-rail).

Enjoy navigating through the revised design!

### Licensing

#### Unified Pricing, an innovative licensing model

We are excited to announce Unified Pricing, our enhanced licensing model that brings new licensing plans, user licenses, and an innovative credit-based approach. These features make it a compelling alternative to the existing Flex licensing model.

#### Key benefits

Unified Pricing introduces the following new features:

* **Credit-based approach**: Under Unified Pricing, all licensing consumption units - such as AI Units, App Units, Robot Units, API Calls, and Agent Units - are consolidated into a single unit, the Platform Unit. This simplification allows for easier understanding and tracking.
* **Enhanced flexibility**: With Unified Pricing, you can easily reallocate Platform Units based on your changing project needs. Now that multiple UiPath services consume Platform Units, you are no longer constrained to pre-defined uses for the acquired units. This allows you to shift your focus and resources where your projects need them the most, whenever you require.

#### Who can benefit

Currently, you can acquire Unified Pricing licensing plans for Automation Cloud products, Automation Suite products, and desktop products. This new licensing model caters to the needs of both existing and new customers.

If you want to continue with your existing Flex licensing model, you are free to make that choice. However, if you are currently operating under the Flex model and wish to switch to Unified Pricing, remember that this transition will require that you ensure user license management is enabled and you re-assign licenses. For more guidance, reach out to your Sales representative.

#### Additional resources

For comprehensive information on the user SKUs available in Unified pricing, refer to [UiPath Licensing](https://licensing.uipath.com/).

For guidance on how to select the optimal licensing model tailored to your needs, refer to the [Overview guide](https://docs.uipath.com/overview/other/latest/overview/commercial-licensing-plans).

For specifics related to the newly introduced Unified Pricing plans, user licenses, and Platform Units on the platform-level, refer to the [Automation Suite admin guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/about-licensing).

For information on the consumption logic applicable to each UiPath product, detailed user guides for each product are available.

#### Improved tenant-level license tracking and assignment

You can now monitor the quantity of runtimes that are currently in use by a tenant, in addition to the number of licenses that are available for allocation. You can check this new value in the **Edit license allocation** panel for the selected tenant, by choosing the **Licenses** card in the **Admin** section.

This new feature helps you avoid the re-assignment of licenses already in use, by making it easier to count and assign the remaining licenses. For details, refer to [License overallocation](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/license-overallocation).

The following image shows the **Edit license allocation panel**, where you can view the number of both available and in-use licenses.
  ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/520512/526939)

#### Introducing quotas per user group

We are excited to announce a new enhancement to our user licensing management system: quotas per user groups. This feature allows organization administrators to control the number of user licenses a group can acquire. In essence, users belonging to each group can now acquire licenses up to the set quota. This streamlines the allocation and overall management of licenses across multiple business units within your organization.

#### Key benefits

With quotas per user groups, you can enjoy the following benefits:

* Elevated control: As an organization administrator, you can restrict the number of user licenses a group can acquire, which gives you better control of licenses across your organization.
* Enhanced efficiency: As an administrator, you can control the number of licenses allocated to specific groups of users. This allows for more targeted license management compared to managing licenses via group allocation only. Administrators can use this mechanism, and combined with permissions, they can restrict the access of a group of users to specific tenants and a specific number of licenses.

#### Usage notes

When you are adding or editing a license allocation rule for a group, you, as an organization administrator, can now control the quotas per user group. For more information, refer to [Managing license allocation rules](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/allocating-user-licenses#managing-license-allocation-rules).

As you navigate the new feature, there are some key points to keep in mind:

* Minimum quota: The minimum quota value that can be set is 1. If a quota is set to 0, an error message will guide you towards a valid action.
* Unlimited upper quota: We do not set an upper limit to quota. Setting the quota higher than the available licenses simply means users can acquire up to the maximum available licenses. However, note that this is not a recommended configuration.
* Lowering quota: If you attempt to set a quota that is lower than the number of licenses already acquired by a group, an error message will appear suggesting the need to adjust existing allocations. For details, refer to [Deallocating directly assigned licenses](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/deallocating-licenses-from-users#deallocating-directly-assigned-licenses).

This enhancement is designed to simplify the task of managing licenses within your organization.

### Identity

#### Manage UiPath's signing certificate for SAML authentication requests via API

If your identity provider (IdP) does not support automatically consuming updates from UiPath's SAML metadata URL, and you require signed authentication requests or responses, you will not be able to reliably update verification certificates in your IdP. In this case, you can now upload your own verification certificate via API endpoints, and ensure you meet your IT requirements for signed SAML requests or responses. For step-by-step information on uploading a verification certificate, visit [Managing UiPath signing certificate for SAML authentication requests](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/managing-uipath-signing-certificate-for-saml-authentication-requests).

#### API support for managing OAuth external applications

You can now use APIs to automate client secret rotation for external applications. This helps meet security requirements by reducing the risks associated with secrets used on a long term, or with manually rotated secrets.

The new APIs allow you to:

* List and manage OAuth external client applications.
* Create, update, and delete secrets for OAuth external applications.
* Generate secrets using fine-grained scopes.

For more details, visit [External client APIs](https://docs.uipath.com/automation-suite/automation-suite/2.2510/api-guide/external-client).

#### User consent management

Administrators can create consent prompts for users logging into the organization. This feature ensures each user is acquainted and in compliance with your organization's policies before stepping into your UiPath ecosystem.

See how to [configure consent prompts.](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/configuring-system-prompts)

#### Support for restricting access to organizations

We are happy to announce that you can now easily manage the user access to your organizations. The new functionality gives you more control over which devices from your network can access specific organizations in Automation Cloud. You can now prevent unauthorized access to specific organizations, even from company-controlled devices.

This enhancement mitigates the risk of misused resources and unauthorized data access. Experience the extra layer of security that this feature ensures by providing consistent control over your UiPath environment.

For details on how to make the most of this feature, see [Restricting access to organizations](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/restricting-access-to-organizations).

#### Deprecated API endpoint

The `/identity_/api/User/{userId}/loginAttempts` endpoint has been deprecated. Switch to using the `/{organization_name}/portal_/api/auditLog` endpoint for audit logs.

## Improvements

### Istio HSTS enabled by default

To enhance security, Istio HSTS is now enabled by default.

### uipathctl improvements

* You can now list all the available options for the included and excluded flags when running the prerequisite checks command. For more details about `--list-options`, refer to the [uipathctl reference guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/reference-guide/uipathctl-prereq-run).
* For better eficiency, the diagnostic checks are no longer executed during the bundle creation process. Previously, a health check was performed by default during the support bundle creation, requiring the explicit use of the `--skip-diagnose` flag to bypass it. For more details on how to run the diagnostic checks, refer to the [uipathctl reference guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/reference-guide/uipathctl-health-diagnose).

### Additional custom CA certificate support

You can include any additional custom CA certificate by providing the `additonal_ca_certs` key with the external CA certificate path in the `input.json` file.

### Enhanced EKS disaster recovery support

We have extended disaster recovery support for EKS environments. The following products and services can now run on the secondary (passive) cluster during a failover:

* Automation Hub
* Integration Service
* Insights
* Process Mining
* Studio Web
* LLM gateway
* LLM observability
* ECS

For details, refer to [Disaster recovery - Active/Passive](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery).

### Enhanced telemetry and configuration insights

We are now including high-level summarized telemetry in Automation Suite support bundle, providing insights into environment configuration, resource utilization, and command execution. We also include guidance on how to view the generated XML file and enabled telemetry sharing with UiPath Support via the Customer Portal.

### New alert for Redis license expiration

We have added a new Prometheus alert for the expiration of internal Redis licenses. This alert has three notification levels, based on the timeframe the license is set to expire: 90, 30, or 7 days.

### Improved configuration for RWX StorageClass selection

We have added a new field in the `input.json` file to define the StorageClass supporting ReadWriteMany (RWX) access mode.

This addition improves clarity and ensures that components requiring PersistentVolumeClaims (PVCs) with ReadWriteMany (RWX) access mode, such as Studio Web and ECS, use the appropriate RWX-enabled StorageClass.

For details, refer to [Configuring input.json](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson).

## Removals

### Full migration option no longer available

The full migration option to move standalone product data to Automation Suite is no longer available. The single tenant migration method, powered by the Automation Cloud™ Migration Tool, is now the only supported way to transfer Orchestrator entities.

For details, refer to the [Migration and upgrade](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-standalone-products-to-automation-suite) section.

### Task Mining no longer available in Automation Suite on EKS/AKS 2.2510

Unassisted Task Mining is a deprecated feature and will be removed on December 1, 2025. As Task Mining in Automation Suite only consists of Unassisted Task Mining, the implies that Task Mining is no longer available in Automation Suite 2.2510.

If Task Mining was installed in a previous version of Automation Suite, it will no longer be visible after upgrading to version 2.2510.

:::important
Internally, Task Mining depended on the Dapr service, which also has been removed. After successfully upgrading or migrating from a version of Automation Suite that had Task Mining enabled, make sure to delete the Task Mining node, database, and storage, or adjust the nodes for internal use cases by updating taints and tolerations as needed.
:::

## Bug fixes

* An issue prevented Velero backups from completing successfully. A `FailedValidation` error message was displayed, indicating that no default backup location could be found. This issue occurred because Velero could not locate a default backup storage location when the `spec.default field` was missing in the `BackupStorageLocation` configuration.
* We have fixed an issue where Automation Suite installations failed due to Certificate Authority (CA) certificates not being recognized. The issue occurred when the `CertificatePolicies` section included policy OID values exceeding 4 bytes.
* This release brings security updates to address [CVE-2025-55315](https://trust.uipath.com/?tcuUid=9cfc5284-1ee2-4785-9260-468d23c3b92f).

## Known issues

### FIPS 140-2 support limitations

**Erratum - added January 22, 2026:** Insights and Integration Service are not supported on Automation Suite deployments that run on FIPS 140-2-enabled machines. To remain compliant with FIPS 140-2 requirements, you must disable these services.

For details, refer to [Security and compliance](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/security-and-compliance).

### Prerequisite checks fail when Process Mining is enabled

**Erratum - added December 19, 2025**: An issue causes the prerequisite checks to fail when Process Mining is enabled. The issue occurs due to the checks incorrectly identifying `cert-manager` as a required component, even though it is no longer needed for Process Mining.

The failure message is a false positive and can be safely ignored.

We fixed the issue in [Automation Suite 2.2510.1](https://docs.uipath.com/automation-suite/automation-suite/2.2510/release-notes/automation-suite-on-eks-aks-2-2510-1#bug-fixes).

### Kerberos authentication limitations

**Erratum - added December 19, 2025:** Kerberos-based authentication is currently not supported for the following products:
* Integration Service
* Autopilot for Everyone
* AI Trust Layer (LLM Gateway, LLM Observability, Context Grounding)

We are working on bringing Kerberos support to upcoming Automation Suite releases.

Meanwhile, you can use alternative authentication mechanisms such as basic authentication or workload identity–based authentication.

### SQL check failure with workload identity enabled

An issue may cause the prereq check and health diagnose commands to report a failure for the SQL check. This issue can occur in environments where workload identity is enabled for Apps, Automation Hub, and Integration Service.

### Context Grounding not available in EKS environments with IPV 6 enabled

The Context Grounding service is not available in EKS environments with IPV6 enabled. This issue directly impacts the GenAI activities that use Context Grounding and Autopilot for Everyone.

## Deprecation timeline

We recommend that you regularly check the [deprecation timeline](https://docs.uipath.com/overview-guide/docs/deprecation-timeline#automation-suite) for any updates regarding features that will be deprecated and removed.

## Bundling details

### Product versions

The following table outlines the release status, version, and release notes for all UiPath products deployed under Automation Suite 2.2510.0.

**Legend:**

✅ - This Automation Suite version bundles a new version of the product. New release notes are available.

❌ - This Automation Suite version bundles a previously released version of the product. No new release notes are available.

| Product | Product version | Release status | Release notes |
| --- | --- | --- | --- |
| Action Center | 2.2510.0 | ✅ | [Action Center release notes](https://docs.uipath.com/action-center/automation-suite/2.2510/user-guide/release-notes-2-2510-0) |
| AI Center | 2.2510.0 | ✅ | [AI Center release notes](https://docs.uipath.com/ai-center/automation-suite/2.2510/user-guide/release-notes-2-2510-0) |
| AI Computer Vision | 2.2510.0 | ✅ | [AI Computer Vision reelase notes](https://docs.uipath.com/ai-computer-vision/automation-suite/2.2510/user-guide/release-notes-2-2510-0) |
| Apps | 2.2510.0 | ✅ | [Apps release notes](https://docs.uipath.com/apps/automation-suite/2.2510/release-notes/2-2510-0) |
| Automation Hub | 2.2510.0 | ✅ | [Automation Hub release notes](https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/release-notes-2-2510-0) |
| Automation Ops | 2.2510.0 | ✅ | [Automation Ops release notes](https://docs.uipath.com/automation-ops/automation-suite/2.2510/user-guide/release-notes-2-2510-0) |
| Autopilot for Everyone | 2025.9.3 | ✅ | [Autopilot for Everyone release notes](https://docs.uipath.com/autopilot/other/latest/release-notes/2025-7-1) |
| Data Service | 2.2510.0 | ✅ | [Data Service release notes](https://docs-dev.uipath.com/data-service/automation-suite/2.2510/release-notes/2-2510-0) |
| Document Understanding |  | ✅ | [Document Understanding AI Center-based projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2.2510/release-notes/release-notes-22510)  [Document Understanding modern projects release notes](https://docs.uipath.com/document-understanding/automation-suite/2.2510/release-notes/release-notes-22510) |
| Insights | 2.2510.0 | ✅ | [Insights release notes](https://docs.uipath.com/insights/automation-suite/2.2510/user-guide/release-notes-2-2510-0) |
| Integration Service | 2.2510.0 | ✅ | [Integration Service release notes](https://docs.uipath.com/integration-service/automation-suite/2.2510/release-notes/2-2510-0) |
| Solutions | 2.2510.0 | ✅ | [Solutions release notes](https://docs.uipath.com/solutions-management/automation-suite/2.2510/release-notes/solutions-in-automation-suite-release-notes) |
| Orchestrator | 2.2510.0 | ✅ | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-suite/2.2510/release-notes/2-2510-0) |
| Process Mining | 2.2510.0 | ✅ | [Process Mining release notes](https://docs.uipath.com/process-mining/automation-suite/2.2510/user-guide/process-mining-2-2510) |
| Studio Web | 2.2510.0 | ✅ | [Studio Web release notes](https://docs.uipath.com/studio-web/automation-suite/2.2510/release-notes/2-2510-0) |
| Test Manager | 2.2510.0 | ✅ | [Test Manager release notes](https://docs.uipath.com/test-manager/automation-suite/2.2510/release-notes/test-manager-2-2510) |

### Internal third-party component versions

For the Kubernetes versions that each Automation Suite version supports, see [Kubernetes compatibility](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/compatibility-matrix#kubernetes-compatibility).

This Automation Suite release bundles the following internal components:

| Component | Version |
| --- | --- |
| Istio | 1.26.3 |
| ArgoCD | 3.1.5 |
| Prometheus | 3.5.0 |
| Grafana | 12.0.2 |
| Fluentd and Fluent-bit | logging-operator: 6.0.3  fluent/fluent-bit: 4.0.3 |
| Gatekeeper | 3.20.0 |
| Cert-Manager | 1.18.2 |
| Velero | 10.0.10 |