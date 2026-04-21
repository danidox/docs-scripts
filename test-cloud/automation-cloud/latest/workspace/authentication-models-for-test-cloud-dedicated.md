---
title: "Authentication models for Test Cloud Dedicated"
visible: true
slug: "authentication-models-for-test-cloud-dedicated"
---

These authentication models apply only for Test Cloud Dedicated.

## The local accounts model

Local user accounts represent each user's account and are internal to UiPath. In this model, an organization administrator adds new users to the organization. It's suitable for scenarios where you want complete control over user management within UiPath.

In UiPath, SSO settings are provisions that can be implemented at both the host level and the organization level.

SSO settings at the host level are used across all organizations tied to the host. This means any SSO settings you adjust on this level are applied to each organization under the host's umbrella.

The SSO settings that can be managed at the host level include basic sign-in, Microsoft Entra ID SSO, and SAML SSO. Specific settings, such as the basic sign-in, can be overriden at the organization level.
:::note
This model is compatible with the directory accounts model.
:::

## The directory accounts model

The directory accounts model relies on a third-party directory that you integrate with UiPath platform. This lets you reuse your company's established identity scheme. Directory accounts are created and maintained in a directory which is external to the UiPath platform; they are only referenced in the UiPath platform and used as identities.

In UiPath, directory integration models can be configured at both the host and the organization levels.

* At the host level, directory integration options include SAML 2.0 and Active Directory. These settings are applied consistently to all organizations under the host.
* At the organization level, UiPath allows organization admins to override the host-level settings using either SAML 2.0 and Microsoft Entra ID integration.

Active Directory is essential in coordinating authentication and access management policies for most companies. When establishing directory integration, your identity provider serves as the single source of truth for user identities.

By allowing settings at both the host and organization levels, UiPath's directory model effectively provides a balance of consistency and flexibility. It allows the use of unified directory integration services across the host while also providing custom settings at the organization level when necessary.

## Authentication levels and inheritance

Choosing the identity provider for your organization affects the way users sign in, and how user and group accounts are created and managed. In Test Cloud, administrators can choose the authentication and related security settings either globally (host level) for all organizations at once, or for each organization:

* **Global authentication settings (host level):** As a system administrator, you can choose the authentication and related default security settings for your installation at the host level. We call these host authentication and security settings, and they are inherited by all organizations as default. [Learn to configure host authentication and security settings.](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/authentication-models-for-test-cloud-dedicated#global-authentication-settings-(host-level))
* **Organization-level authentication settings:** As an organization administrator, you can choose the authentication and related security settings for your organization. Some settings are inherited from the host level, but you can override them if different settings should apply for your organization. [Learn to configure organization-level authentication and security settings.](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-organizations#about-organizations)

The following table describes the authentication and related security settings for host levels for all organizations at once, or for each organization:

| **Authentication settings** | **Microsoft Entra ID host level** | **Microsoft Entra ID org level** | **SAML host level** | **SAML org level** |
| --- | --- | --- | --- | --- |
| Single Sign On | Yes | Yes | Yes | Yes |
| Automatic just-in-time user provisioning | No | Yes | No | Yes |
| Automatic just-in-time claims based provisioning rules | No | No | No | Yes |
| Directory integration to search users and groups | No | Yes | No | No |

### Global authentication settings (host level)

You can configure an external identity provider to control how your users sign in. These settings apply to all organizations.

The following table provides an overview of the different host-level external providers available:

| External Provider Integration | Authentication | Directory Search | Administrators Provisioning |
| --- | --- | --- | --- |
| Microsoft Entra ID | Administrators can use SSO with Microsoft Entra ID using the OpenID Connect protocol | Not supported | Users must be manually provisioned into the UiPath organization with an email address matching their Microsoft Entra ID account. |
| SAML 2.0 | Users can use SSO with any Identity Provider that supports SAML | Not supported | Users must be manually provisioned into the UiPath organization with a username/email/external provider key (as configured in their external identity provider configuration) matching their SAML account. |
:::note
**Differences between integrating Microsoft Entra ID at host-level and organization-level**: The host-level functionality only enables SSO. The organization-level Microsoft Entra ID integration enables SSO, directory search, and automatic user provisioning.
:::

### Organization authentication

#### Microsoft Entra ID model

The integration with Microsoft Entra ID offers scalable user and access management for your organization, allowing for compliance across all the internal applications used by your employees. If your organization is using Microsoft Entra ID or Office 365, you can connect it directly to your Microsoft Entra ID tenant to obtain the following benefits:

**Automatic user onboarding with seamless migration**
* All users and groups from Microsoft Entra ID are readily available for any service to assign permissions, without the need to invite and manage Microsoft Entra ID users in the organization directory.
* You can provide SSO for users whose corporate username differs from their email address, which is not possible with the invitation model.
* All existing users with UiPath® user accounts have their permissions automatically migrated to their connected Microsoft Entra ID account.

**Simplified sign-in experience**
* Users do not have to accept an invitation or create a UiPath user account to access the organization as in the default model. They sign in with their Microsoft Entra ID account by selecting the Enterprise SSO option or using their organization-specific URL. If the user is already signed in to Microsoft Entra ID or Office 365, they are automatically signed in.
* UiPath Assistant and Studio versions 20.10.3 and higher can be preconfigured to use a custom organization URL, which leads to the same seamless connection experience.

**Scalable governance and access management with existing Microsoft Entra ID groups**
* Microsoft Entra ID security groups or Office 365 groups, also known as directory groups, allow you to leverage your existing organizational structure to manage permissions at scale. You no longer need to configure permissions in services for each user.
* You can combine multiple directory groups into one UiPath group if you need to manage them together.
* Auditing UiPath access is simple. After you've configured permissions in all Orchestrator services using Microsoft Entra ID groups, you utilize your existing validation processes associated with Microsoft Entra ID group membership.
  :::note
  While on the Microsoft Entra ID model, you can continue to use all the features of the default model. But to maximize the benefits, we recommend relying exclusively on centralized account management from Microsoft Entra ID.
  :::
If you would like to use Microsoft Entra ID as the identity provider for your organization, follow the instructions in [Setting up the Microsoft Entra ID integration](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/azure-ad-integration#microsoft-entra-id-integration-for-test-cloud-dedicated).

#### SAML model

This model allows you to connect to your chosen identity provider (IdP) so that:

* your users can benefit from SSO and
* you can manage existing accounts from your directory in your organization, without having to re-create identities.

UiPath offerings can connect to any external identity provider that uses the SAML 2.0 standard to obtain the following benefits:

**Automatic onboarding of users**

All users from your external identity provider are authorized to sign in with basic rights when the SAML integration is active. What this means is:

* Users can sign in to your organization via SSO using their existing company account, as defined in the IdP.
* Without any further setup, they are able to access the organization by default. To be able to work in the organization, users require roles and licenses, as appropriate for their role.

**User management**

You can add users by directly assigning them to groups, to do this all you have to do is enter their email address when adding users to the group.

Typically, administrators manage local accounts from **Admin** > organization > **Accounts & Groups** > **Users** tab. But SAML users are directory accounts, so they are not visible on this page.

After a user has been added to a group or they have signed in at least once (which automatically adds them to the Everyone group), they are available in search in all services for direct role or license assignment.

**Attribute mapping**

If you use UiPath Automation Hub, you can define custom attribute mapping to propagate attributes from your identity provider into Test Cloud. For example, when an account is first added to Automation Hub, the first name, last name, email address, job title, and department of the user are already populated.

  !['Benefits of SAML model' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/228466)

#### Setup

Administrators can configure and enable the SAML integration for your entire organization from **Admin** > **Security Settings** > **Authentication Settings**.

For instructions, refer to.

#### **Transitioning from the Microsoft Entra ID integration to the SAML integration**

After switching to the SAML integration, the Microsoft Entra ID integration is disabled. Microsoft Entra ID group assignments no longer apply, so Orchestrator group membership and the permissions inherited from Microsoft Entra ID are no longer respected.