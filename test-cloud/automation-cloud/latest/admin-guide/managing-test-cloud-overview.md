---
title: "Overview"
visible: true
slug: "managing-test-cloud-overview"
---

This section gives an introduction to managing Test Cloud organizations in the UiPath® ecosystem. This overview covers the basic aspects of Test Cloud organizations, such as their creation, operation, and various features.

For more detailed information on the platform capabilities of Test Cloud, visit the [Automation Cloud Admin guide](https://docs.uipath.com/automation-cloud/automation-cloud/latest).

## Data security and compliance

Data security and compliance are vital in the digital world. UiPath adheres to these factors with Test Cloud and throughout the entire UiPath® Platform.

Test Cloud regularly undergoes both internal and external verifications for its several security attestations. You can find the list of these attestations and further information regarding our security practices on the UiPath website, in the [Security section](https://www.uipath.com/legal/trust-and-security/security#content-2).

UiPath can provide details about operational and security practices under a Non-Disclosure Agreement (NDA). For these details, please contact your UiPath account team.

The data security and compliance capabilities of the UiPath Platform provide data residency, encryption methods, certificates, and functional security features such as audit logging, authentication and authorization, access control, firewall configurations, and feature rollout methodology.

For more information on the data security and compliance of Test Cloud, visit [Data Security and Compliance of Automation Cloud](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/data-security-and-compliance).

### Configuring the firewall

To ensure Test Cloud and its services work as expected, you may need to configure your organization's firewall settings. If your organization's network security only allows access to specific websites, you need to establish an allow list of necessary domains based on the UiPath® products you employ and your use cases. Test Cloud and its surfaced services use the same list of allowed domains as Automation Cloud<sup>TM</sup> and its associated services. To check the list of allowed domains for Automation Cloud, visit [Configuring the firewall](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/configuring-firewall).

## Organizations

In both Automation Cloud<sup>TM</sup> and Test Cloud, an organization represents a completely isolated environment for managing your automation necessities and resources. It serves as your exclusive operating space within the UiPath Platform. Organizations are the highest layer available in Test Cloud. New sign-ups for Test Cloud always result in the creation of an organization.

You can identify organizations through the following:

1. **Unique URL**: Each organization has a unique URL. The final part of the URL, known as Account Logical Name (or `orgID`), derives automatically from the **Company Name** provided during sign-up. It is generated with certain limitations, such as no Unicode characters, spaces, and it must be unique.
2. **Organization name**: This is the **Company Name** provided at sign-up.
3. **Support ID**: Each organization has a unique support ID, used particularly when interacting with UiPath, such as when opening a Support ticket.

Test Cloud inherits these features from Automation Cloud natively, given that it is a dedicated interface of Automation Cloud and thus maintains the same URL as an Automation Cloud organization.

For more information about organizations, visit [About organizations](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-organizations).

## Authentication and security

The security structure for a UiPath organization uses the local accounts model (invitation-based). This model operates on an invitation-based mechanism, where an organization administrator invites new users to join the UiPath Platform. This method is primarily recommended for scenarios demanding total control over user management.
:::note
This model is compatible with the directory accounts model.
:::

Users get the flexibility to choose from available authentication methods. Administrators have the power to allow usage of all existing methods (Google, Microsoft, Basic Authentication), or limit it to only Google or Microsoft.

### Authentication with Google, Microsoft, LinkedIn, or personal emails:

New organizations typically employ this model by default. This model requires the administrator to send out invites to users, who can then create a UiPath user account.

Users can use their invited email address as a username and create a password, or use an existing account with Microsoft (personal, Azure AD-linked account, or Office 365 account), Google (personal or Google Workspace account), or their personal LinkedIn account to sign in to their UiPath user account.

### Authentication with Google or Microsoft only:

This authentication model requires users to sign-in using only Google or Microsoft accounts. Despite this, users must create a UiPath account using the email address, according to the invitation.

### Directory accounts model:

The directory accounts model relies on a third-party directory that you integrate with the UiPath Platform. This lets you reuse your company's established identity scheme in UiPath.

* **Azure Active Directory:** If you have a Microsoft Azure or Office 365 subscription, you can integrate Azure with the UiPath Platform to use your existing users and groups from Azure Active Directory within UiPath.
* **SAML 2.0:** Lets you integrate the UiPath Platform with your chosen identity provider (IdP). This lets your users connect to UiPath with single sign-on (SSO), using the accounts that are already registered with your IdP.

For more information on authentication and security in Test Cloud, visit [Understanding authentication models](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/authentication-settings).

## Licensing

The licensing model for Test Cloud organizations involves having [Test Cloud-specific licenses](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/licensing-test-cloud#license-types) assigned to yourself or your users.
:::important
The licenses associated with (**App Tester User - Named User** and **App Test Developer - Named User**) grant access to all the products available within Test Cloud. No additional user licenses, beyond the **App Tester User** or **App Test Developer**, are needed for accessing the products within Test Cloud.
:::

For more information on how to activate, assign, deallocate, and monitor licenses, visit [Licensing](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-licensing)[Licensing](https://docs.uipath.com/automation-suite/automation-suite/latest/admin-guide/about-licensing).

## Tenants and services

Tenants and services are core components of Test Cloud organizations. Tenants mirror the organizational structure, business flow, and information as the dimensions of your actual organization. They function as containers where services are arranged and managed for a group of users. For example, creating individual tenants for each of your departments and then determining the services you want to enable for each, based on their needs. A single instance of each of the cloud services can exist within each tenant.

### Default Tenant

When you start with an organization in Test Cloud, your first tenant, named as **DefaultTenant**, is automatically created for you.

### Multitenancy

Multitenancy facilitates automation of different departments in your company while controlling access to data per department. Also, you can configure specific settings for each of these tenants such as provisioning services and enabling/disabling them based on needs.

For more information on managing tenants and services in Test Cloud, visit [About tenants](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-tenants).

## Accounts and roles

Each user or robot within the UiPath ecosystem is granted an account, which identifies their unique position within the organization, provides specific roles and access to UiPath products, manages licensing, and sets up robot configuration.

### Account Types

Within Test Cloud you can create two types of accounts:

* **User accounts**: Use these types of accounts to identify a person. You can assign licenses, roles, and add these accounts to groups. There are two types of user accounts:
  + **Local users**: These accounts are linked to a UiPath account. This type of account is created within Test Cloud and it is also managed from there by an organization administrator. Users own the account itself, but organization administrators can work with the reference of it to edit, delete, or manage roles and group memberships for it.
  + **Directory users**: These accounts are defined outside of the UiPath Platform, in a cloud active directory such as Azure Active Directory.
* **Robot accounts**: These operate unattended, back-office processes that are not associated with any specific user account.

### Groups

A group is a collection of users or accounts that are managed together for effective administration. They can be formed based on similar access rights, licensing needs, and UiPath functionality. Groups simplify the application of changes to a large number of users at once and can be assigned additional roles if required. The types of groups are:

* **Local Groups**: Created within the UiPath Platform and managed there.
* **Directory Groups**: Defined outside of UiPath, within a linked directory and can be managed in the UiPath Platform like local groups.

### Inheritance

An account is granted roles, licenses, and robot configurations through its membership in a group. Various aspects, such as access to service, licenses, and roles are allocated based on the account’s association with the group. If an account is associated with multiple groups, it gains all permissions.

## AI Trust Layer

The AI Trust Layer brings administration and strict governance capabilities to generative AI features and agents across all UiPath® products. Aimed to ensure data confidentiality and security in every interaction, AI Trust Layer keeps your data restricted within the UiPath® environment. For more information, visit [About AI Trust Layer](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-ai-trust-layer).

## External applications

Enhance and expand your UiPath platform's capabilities with external OAuth applications. These extend the functional range of UiPath, accessing UiPath resources securely without the risk of sharing your credentials. These applications interact seamlessly with UiPath's Identity Server and its varied resources under secure OAuth frameworks. To learn more about registering these apps, visit [OAuth apps](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/authorizing-external-applications).

## Notifications

Stay updated about your actions and their outcomes with notifications. Keep track of user or administrative actions within your organization account through both in-app, and email notifications. For more details on enabling and managing notifications, visit [About notifications](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-notifications).

## Logging

Logging is an important tool for various tasks like debugging issues, reporting trends, and enhancing security and performance. Test Cloud, along with other cloud services, uses different types of logs based on their unique requirements. For a thorough walkthrough on the uses and management of logs, visit [About logs](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-logs).