---
title: "Authentication models for Test Cloud Public
            Sector"
visible: true
slug: "authentication-models-for-test-cloud-public-sector"
---

These authentication models apply only for Test Cloud Public Sector.

## The local accounts model (invitation-based)

Local user accounts represent each user's account and are internal to the UiPath platform.

The local accounts model provides a self-contained approach to authentication. It requires an invitation from an organization administrator for new users to join. It's suitable for scenarios where you want complete control over user management within your platform.
:::note
This model is compatible with the directory accounts model. If you choose to use the directory model, you can continue to create users by invitation.
:::

The process for creating a user is as follows:

1. Organization administrators must obtain the email addresses of users and use them to invite each user to join their organization. They can do this in bulk.
2. Each invited employee accepts the invitation by navigating to the link provided in the invitation email and creates a UiPath user account.

## The directory accounts model

The directory accounts model relies on a third-party directory that you integrate with the UiPath platform. This lets you reuse your company's established identity scheme in UiPath.

* **Microsoft Entra ID:** If you have a Microsoft Azure or Office 365 subscription, you can integrate Azure with the UiPath platform to use your existing users and groups from Microsoft Entra ID within UiPath.
* **SAML 2.0:** Lets you integrate the UiPath platform with your chosen identity provider (IdP). This lets your users connect to UiPath with single sign-on (SSO), using the accounts that are already registered with your IdP.

Directory user accounts are created and maintained in a directory which is external to UiPath. Directory accounts are only referenced in the UiPath platform and used as identities for your users.

### Azure Active Directory

The integration with Microsoft Entra ID can offer scalable user and access management for your organization, allowing for compliance across all the internal applications used by your employees. If your organization is using Microsoft Entra ID or Office 365, you can connect your organization directly to your Microsoft Entra ID tenant to obtain the following benefits:

* Automatic user onboarding with seamless migration
  + All users and groups from Microsoft Entra ID are readily available for any UiPath platform service to assign permissions, without the need to invite and manage Microsoft Entra ID users in the organization directory.
  + You can provide Single Sign-On for users whose corporate username differs from their email address, which is not possible with the invitation-based model.
  + All existing users with local UiPath accounts have their permissions automatically migrated to their connected Microsoft Entra ID account.
* Simplified sign-in experience
  + Users do not have to accept an invitation or create a UiPath user account to access the organization. They sign in with their Microsoft Entra ID account by selecting the Enterprise SSO option or using their organization-specific URL. If the user is already signed in to Microsoft Entra ID or Office 365, they are automatically signed in.
  + UiPath Assistant and Studio versions 20.10.3 and higher can be preconfigured to use a custom Orchestrator URL, which leads to the same seamless connection experience.
* Scalable governance and access management with existing Microsoft Entra ID groups
  + Microsoft Entra ID security groups or Office 365 groups, also known as directory groups, allow you to leverage your existing organizational structure to manage permissions at scale. You no longer need to configure permissions in services for each user.
  + You can combine multiple directory groups into one group if you need to manage them together.
  + Auditing access is simple. After you've configured permissions in all UiPath platform services using Microsoft Entra ID groups, you utilize your existing validation processes associated with Microsoft Entra ID group membership.

### SAML 2.0

This model allows you to connect the UiPath platform to your chosen identity provider (IdP) so that:

* your users can benefit from single sign-on (SSO) and
* you can manage existing accounts from your directory in the UiPath platform, without having to re-create identities.

The UiPath platform can connect to any external identity provider that uses the SAML 2.0 standard.

#### Benefits

  !['Benefits to SAML 2.0' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31215)

* Automatic onboarding of users to the UiPath platform: All users from your external identity provider are authorized to sign in to the UiPath organization with basic rights when the SAML integration is active. What this means is:
  + Users can sign in to your UIPath organization via SSO using their existing company account, as defined in the IdP.
  + Without any further setup, they become members of the **Everyone** user group, which grants them the [User organization role](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/roles#organization-level-roles) by default. To be able to work in the UiPath platform, users require roles and licenses, as appropriate for their role.
  + If you need to restrict access to only some of your users, you can define the set of users who are allowed to access the UiPath platform in your identity provider.
* User management: You can add users by directly assigning them to groups. To do this, just enter their email address when adding users to the group. Typically, organization administrators manage local accounts from the **Admin** > **Accounts & Groups** > **Users** tab. However, SAML users are [directory accounts](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-accounts#user-accounts) in the UiPath ecosystem, so they are not visible on this page. After a user has been added to a group or they have signed in at least once (which automatically adds them to the Everyone group), they are available in search in all UiPath services for direct role or license assignment.
* Attribute mapping: If you use UiPath Automation Hub, for example, you can define custom attribute mapping to propagate attributes from your identity provider to the UiPath platform. For example, when an account is first added to Automation Hub, the first name, last name, email address, job title, and department of the user are already populated.

## How authentication works

The identity of your users is verified based on your organization directory. Based on user permissions assigned through roles and groups, they can access all your UiPath cloud services with only one set of credentials. The following diagram describes the two identity models, how they work with the various user identities, and how federation can be achieved. In the invitation-based model, identity management is performed on a user reference in the organization directory, while users remain in control of their accounts. If integrated with Microsoft Entra ID, it is as simple as looking at the contents of your tenant directory in Microsoft Entra ID, depicted in the following diagram with an orange arrow.

  !['Authentication diagram using the two identity models' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30919)