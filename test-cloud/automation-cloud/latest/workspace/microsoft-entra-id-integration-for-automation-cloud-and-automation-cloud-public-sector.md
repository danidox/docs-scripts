---
title: "Microsoft Entra ID integration for Test Cloud and Test Cloud Public
               Sector"
visible: true
slug: "microsoft-entra-id-integration-for-automation-cloud-and-automation-cloud-public-sector"
---

This procedure applies only for Test Cloud and Test Cloud Public Sector

## Getting started

### Benefits

Integrating Microsoft Entra ID integration with UiPath offers the following benefits:

* Single sign-on (SSO): Allow users to access an organization with their Microsoft Entra ID credentials.
* Simplified user management: Manage access using existing Microsoft Entra ID users and groups.
* Enhanced security: Apply Microsoft Entra ID features such as multifactor authentication, conditional access, and privileged identity management.
* Seamless transition: Migrate from local accounts without disruption, as long as email addresses match.

### Limitations and considerations

Keep the following limitations in mind when using Microsoft Entra ID integration:

* UiPath supports integration only with the Microsoft Entra ID service in the Microsoft Azure commercial cloud. The Microsoft Azure Government cloud version of Microsoft Entra ID is not supported.
* When an integration uses **delegated access only** as its access scope, Microsoft Entra ID requires the user to be present during directory evaluation. Because unattended automations and personal access tokens run without a user present, the following limitations apply:
  + Microsoft Entra ID directory users cannot inherit group-based permissions when running unattended automations or when using personal access tokens.
  + If access to the organization is restricted through Microsoft Entra ID groups, unattended robots cannot access the organization on behalf of users.These limitations apply across cloud offerings that rely on delegated access with Microsoft Entra ID.
* User account management: You can only manage directory users and groups in Microsoft Entra ID. These accounts appear in your organization only when you search for them or assign permissions.
* Application custom keys: Microsoft Entra ID integration uses the OIDC protocol but does not support application custom keys passed through the `appid` query parameter, as described in [Microsoft's access tokens documentation](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens#validating-tokens).
* You must not name your local UiPath groups the same as Microsoft Entra ID directory groups. Doing so can lead to conflicts in permission evaluation and group-based access assignment.

### Before you begin

Before you configure Microsoft Entra ID integration, ensure that you have the following:

* An organization with an Enterprise license, in either the Standard or Enterprise tier.
* An organization that meets one of the following licensing requirements:
  + Unified Pricing: Requires an Enterprise or Standard plan
  + Flex: Requires an Enterprise plan, either the Standard or Enterprise tier
* Administrator permissions in the organization.
* Coordination with a Microsoft Entra ID administrator who has one of the following roles:
  + [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)
  + [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)
  + Any role that can grant administrator consent to Microsoft Entra ID applications
* A Microsoft Entra ID account that uses the same email address as your UiPath administrator account (for testing)
* A supported version of UiPath Studio and Assistant, as specified in the [product lifecycle documentation](https://docs.uipath.com/overview/other/latest/overview/product-lifecycle).

## Step 1: Preparing your organization for account linking

When you enable the Microsoft Entra ID integration, UiPath automatically links accounts that have matching email addresses. The first time a user signs in with Microsoft Entra ID, UiPath creates a directory user account and assigns it the same permissions as the matching local account.
:::important
Before you enable the Microsoft Entra ID integration, remove any inactive users from the organization. This helps prevent permission escalation if those email addresses are reassigned to different users in your organization.
:::

## Step 2: Configuring the Microsoft Entra ID integration
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

This Microsoft Entra ID integration supports both delegated access and app-only access models, using a combination of the [OAuth 2.0 authorization code grant flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow#request-an-id-token-as-well-or-hybrid-flow) and [OAuth 2.0 client credentials flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-client-creds-grant-flow).

Configuring the Microsoft Entra integration allows UiPath to do the following:

* Sign in users with Microsoft Entra ID credentials.
* Read user profiles and group memberships from your Microsoft Entra ID directory.
* Apply access controls based on Microsoft Entra ID group assignments.

To integrate with Microsoft Entra ID, you must set up a Microsoft Entra ID application that represents your organization in your Microsoft Entra ID tenant.

### Configuration methods

To integrate with Microsoft Entra ID, you must configure the Microsoft Entra ID application that represents your organization in your Microsoft Entra ID tenant.

You can choose one of the following configuration methods:

* (Recommended) Automated setup: Use the UiPath-managed Microsoft Entra ID application ([multi-tenant model](https://learn.microsoft.com/en-us/entra/identity-platform/application-model#multitenant-apps)) for the following benefits:
  + No secrets or certificates to manage.
  + Quick and reliable setup.
  + UiPath maintains the Microsoft Entra ID application for you.
* Manual setup with a custom Microsoft Entra ID application registration: Use your own Microsoft Entra ID application and manage its configuration manually, with the following considerations:
  + You must create and manage application credentials.
  + Credentials expire and require periodic updates.
  + If credentials are not updated before they expire, users are blocked from signing in.

You can choose one of the following access scopes:

* **Delegated and app-only access** (Recommended): Allows UiPath services to evaluate group membership both when the user is present and in offline scenarios, such as unattended automations.
* **Delegated access**: Restricts group evaluation to interactive sessions. Permissions can only be validated when the user is actively signed in.

### About the UiPath-managed Microsoft Entra ID application

UiPath uses a pre-registered, multi-tenant Microsoft Entra ID application. This removes the need to create and maintain your own application registration and credentials. The details of this application are:

* Name: UiPath Entra ID Integration
* Client ID: `4ca9aa42-b0ea-4ceb-b2b1-17fa40827280`
* Application scopes:
  + Entra ID: `email`, `openid`, `profile`, `GroupMember.Read.All`, `User.Read`, `User.ReadBasic.All`, `User.Read.All` (optional).
  + CMK Entra ID integration: `email`, `openid`, `profile`, and `offline access`.
* Redirect URI: `<AccessURL>/portal/grant-consent`
* Consent URLs (for admin approval): If you see a *Needs admin approval* message, a Microsoft Entra ID administrator can grant tenant-wide consent using the Microsoft admin-consent endpoint:
  + **Delegated** access (Delegated): `https://login.microsoftonline.com/{tenant}/adminconsent?client_id=4ca9aa42-b0ea-4ceb-b2b1-17fa40827280&redirect_uri=https%3A%2F%2Fcloud.uipath.com%2Fportal%2Fgrant-consent`
  + **Delegated and app-only access** (Delegated + Application): `https://login.microsoftonline.com/{tenant}/adminconsent?client_id=4ca9aa42-b0ea-4ceb-b2b1-17fa40827280&redirect_uri=https%3A%2F%2Fcloud.uipath.com%2Fportal%2Fgrant-consent`The URL is the same format for both options; the difference is the permissions included in the consent based on the access scope you selected. The redirect URI must match the application's configured redirect URI exactly.
    :::note
    Replace {tenant} with your tenant ID, tenant domain, or use common (depending on your organization's policy).
    :::

### Automated setup with UiPath-managed Microsoft Entra ID application (Recommended)

To configure Microsoft ID integration using the UiPath-managed application, consent must be granted by a Microsoft Entra ID administrator before completing setup in your organization.

Use this method if you want to simplify configuration and avoid managing secrets or certificates. UiPath recommends this approach for most organizations.

#### 1. Grant Microsoft Entra ID consent

Have a Microsoft Entra ID administrator grant consent by navigating to one of the following URLs and signing in. During sign-in, the administrator must select Consent on behalf of your organization, and then select Accept.

Use the URL that corresponds to the access scope you plan to configure in your organization:

* 
:::note

If your Microsoft Entra ID tenant allows consent requests, an organization administrator can use these URLs to trigger a consent request. In this case, a Microsoft Entra ID administrator must approve the request before the configuration can continue.
  :::
* **Delegated and app-only access (Recommended)**:
* **Delegated access only**:

After consent is granted for **Delegated and app-only access**, the Microsoft Entra ID administrator must share the following value with the organization administrator: **Directory (tenant) ID**. This value is required to complete the configuration.

#### 2. Configure the integration in your organization

As an organization administrator, complete the setup as follows:

1. In your organization, go to **Admin > Security > Authentication Settings > Directory integration and single sign-on (SSO)**.
2. Select **Microsoft Entra ID**.
3. Choose **UiPath managed multi-tenant application (Recommended)**.
4. Select the access scope for which consent was granted:
   * **Delegated and app-only access (Recommended)**: Provides full group evaluation, including unattended scenarios.
   * **Delegated access**: Limits evaluations to sessions where the user is present.
     :::note
     Delegated and app-only access is available only for Test Cloud. For more details on feature availability, refer to [Feature availability](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability)
     :::
5. If you selected **Delegated and app-only access**, enter the **Directory (tenant) ID** provided by your Microsoft Entra ID administrator.
6. Check **I understand & accept that existing users and Microsoft Entra ID users with matching email addresses will have their accounts linked**.
7. Select Save to activate the integration.

A successful activation indicates that the integation is configured correctly. If activation fails, verify that consent was granted properly and try again.
:::note
If you use Automation Hub and want to populate the **City**, **Job Title**, and **Department** fields from Microsoft Entra ID, request additional permissions. Ask your Microsoft Entra ID administrator to grant admin consent using an [elevated admin consent URL](https://login.microsoftonline.com/common/oauth2/v2.0/authorize?scope=email+GroupMember.Read.All+openid+profile+User.Read+User.ReadBasic.All+User.Read.All&prompt=select_account&response_type=code&redirect_uri=https://cloud.uipath.com/portal_/testconnection&state=1234&client_id=4ca9aa42-b0ea-4ceb-b2b1-17fa40827280) that includes the required scopes.
:::

### Manual setup with custom Microsoft Entra ID application registration

If you prefer to configure your own Microsoft Entra ID application instead of using the UiPath managed multi-tenant application, take the following steps. This option requires managing your own credentials and maintaining them over time.
:::important
Credentials created through manual setup will expire periodically. You must renew them before expiration to avoid service disruptions. To reduce this operational overhead, consider using the [automated setup with UiPath managed Entra ID application](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/microsoft-entra-id-integration-for-automation-cloud-and-automation-cloud-public-sector#automated-setup-with-uipath-managed-microsoft-entra-id-application-(recommended)).
:::

#### Configuring Microsoft Entra ID

As a Microsoft Entra ID administrator, you can configure the application using either a PowerShell script or the Microsoft Entra admin center.

**Option A: Using the PowerShell scripts**

If you want to automate the setup process with minimal manual configuration, take the following steps:

1. Download the [Microsoft Entra ID configuration scripts](https://github.com/UiPath/platform-quickstart/tree/master/azure-ad-integration).
2. Run `configAzureADconnection.ps1` to automatically set up your Entra tenant.
3. Run `testAzureADappRegistration.ps1` to verify the setup.

**Option B: Using the Microsoft Entra admin center**

If you prefer to manually configure the application registration through the user interface, take the following steps:

1. Create the app registration:
   1. Go to **[Microsoft Entra admin center](https://entra.microsoft.com/) > App registrations > New registration**.
   2. Set a preferred name.
   3. Choose **Accounts in this organizational directory only**.
   4. Set the **Redirect URI** to `<AccessURL>/identity_/signin-oidc`.
2. Configure authentication:
   1. Navigate to **Authentication**.
   2. Add the following redirect URI: `<AccessURL>/portal_/testconnection`.
   3. Under **Implicit grant and hybrid flows**, select **ID tokens**. This integration leverages the [Microsoft hybrid flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow#request-an-id-token-as-well-or-hybrid-flow).
   4. Save your changes.
3. Add token claims:
   1. Go to **Token configuration > Add optional claim**.
   2. Select **ID** as the token type.
   3. Choose the following claims: `family_name`, `given_name`, and `upn`.

These claims are used to update user information upon sign-in.
   4. Save your changes.
4. Set API permissions:
   1. Go to **API permissions > Add permission**.
   2. Select **Microsoft Graph**.
   3. Under **What type of permissions does your application require?** Select the permission types based on the UiPath access scope you wish to configure. Before selecting permissions, consider the following:
      * While you can configure only **Delegated** access, we recommend using a combined **Delegated** and **Application** access.
      * The tables below list the required permissions for each access scope you want to configure. Some permissions appear in both lists, but they must be added separately because their permission types differ.
        :::note
        To use properties such as `City`, `Job Title`, and `Department` in Automation Hub, the `User.Read.All` permission is required.
        :::
        + For Test Cloud: Regardless of the access scope you want to configure, you must add the following permissions from the **Delegated** permissions menu:

          | Microsoft Entra ID permission | Permission type | Purpose |
          | --- | --- | --- |
          | `email`, `openid`, `profile`, `offline_access`, and `User.Read` | Delegated | Allows users to sign in with Microsoft Entra ID and enables Test Cloud to retrieve claims in the authorization request. |
          | `User.ReadBasic.All` or `User.Read.All` | Delegated | Allows Test Cloud to search for users in Microsoft Entra ID, assign permissions, and keep user attributes updated. |
          | `GroupMember.Read.All` | Delegated | Allows Test Cloud to evaluate group membership and enforce directory group-based access controls. |
      * If you want to configure the **Delegated and app-only access** scope, you must also add the following permissions from the **Application** permissions menu:

        | Microsoft Entra ID permission | Permission type | Purpose |
        | --- | --- | --- |
        | `User.ReadBasic.All` or `User.Read.All` | Application | Allows Test Cloud to search for users in Microsoft Entra ID, assign permissions, and keep user attributes updated in unattended automations. |
        | `GroupMember.Read.All` | Application | Allows Test Cloud to evaluate group membership and enforce directory group-based access controls in unattended automations. |
      * For Test Cloud Public Sector, use the following permissions:
        + OpenID permissions: `email`, `openid`, `offline_access`, `profile`.
        + User permissions: `User.Read`, `User.ReadBasic.All`, or `User.Read.All`.
        + Group permissions: `GroupMember.Read.All`.
   4. Select **Grant admin consent for (your organization)**. This step allows the application to access data for all users without requiring individual consent prompts. For more information, refer to Microsoft documentation.
5. Create credentials: You can use either a **client secret** or a **certificate**:
   * To create a client secret:
     1. Go to **Certificates & secrets**.
     2. Select **New client secret**, then save the secret value.
   * To create a certificate:
     1. Open a new tab and go to **Azure Key Vault**.
     2. Create a certificate:
        + Subject: `CN=uipath.com`
        + Content type: `PEM`
        + Maximum size: Less than 10 KB
     3. Download the certificate in `.pem` format.
     4. Open the `.pem` file in a text editor and locate the section between **BEGIN CERTIFICATE** and **END CERTIFICATE**.
     5. Create a new `.pem` file that contains only this certificate section.
     6. In the **Microsoft Entra admin center**, go to **Certificates & secrets**, and upload the new `.pem` file.
     7. Keep the `.pem` file. You will need it to complete the integration in your organization.
        :::note
        Most credential types eventually expire. To prevent user sign-in issues, update the configuration before credentials expire. To avoid this overhead, use the [automated setup with the UiPath-managed Microsoft Entra ID application](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/microsoft-entra-id-integration-for-automation-cloud-and-automation-cloud-public-sector#automated-setup-with-uipath-managed-microsoft-entra-id-application-(recommended)).
        :::
6. Collect the following integration details and share them with your organization administrator:
   * Application (client) ID
   * Directory (tenant) ID
   * Client secret or certificate

#### Activating the integration in your organization

As an organization administrator, use the values provided by the Microsoft Entra ID administrator to complete the setup in your organization by taking the following steps:

1. Go to **Admin > Security > Authentication Settings > Directory integration and single sign-on (SSO)**.
2. Select **Microsoft Entra ID**.
3. Choose **Custom application registration ID and secret**.
4. Select your desired access scope:
   * **Delegated and app-only access** (Recommended): Provides full group evaluation, including for unattended scenarios.
   * **Delegated access**: Limits evaluations to sessions where the user is present.
5. Enter the following values provided by your Entra ID administrator:
   * Directory (tenant) ID
   * Application (client) ID
   * Client secret or certificate
6. Check **I understand & accept that existing users and Microsoft Entra ID users with matching email addresses will have their accounts linked**.
7. Select **Test Connection**, then sign in with your Microsoft Entra ID account.
   * A successful sign-in indicates that the integration has been configured correctly.
   * If the sign-in fails, ask your Microsoft Entra ID administrator to verify the configuration and try again.
8. Select **Save** to activate the integration.

## Step 3: Using and verifying the integration

After you activate the Microsoft Entra ID integration, verify that it works by signing in with a directory user account and confirming access to Microsoft Entra ID users and groups. To do that, take the following steps:

1. Sign out of your local account.
2. Sign in with your directory user account using one of the following methods:
   * Navigate to your organization-specific URL: https://cloud.uipath.com`/{organizationName}/`.
   * Or go to the main login page at https://cloud.uipath.com and select **Continue with Enterprise SSO**.
     :::note
     To confirm that you signed in with a directory account, go to the Test Cloud home page at https://cloud.uipath.com`{organizationName}/portal_/home`. If you do not see a warning about being signed in with a local user account, you are successfully signed in with a directory user account.
     :::
3. Navigate to **Accounts & local groups** and attempt to add directory users or groups from Microsoft Entra ID to a local group. Microsoft Entra ID users and groups have distinct icons to differentiate them from local accounts.
   :::note
   Microsoft Entra ID users and groups are not listed by default on the **User accounts** or **Local groups** pages. You can find them only by using the search function.
   :::

## Step 4: Completing the transition

### Step 4.1: Configuring group permissions

To allow directory users to inherit permissions based on their group membership, add the relevant Microsoft Entra ID groups to local groups in your organization.

For example, add your **UiPath Admins** Entra ID group to the **Administrators** group in your organization.

We recommend removing individual user permissions and relying on directory group membership to simplify permission management as your organization scales.

### Step 4.2: Migrating existing users

To ensure users inherit permissions assigned through Microsoft Entra ID group membership in your organization, Studio, and Assistant, take the following steps:

For your organization:

Ask users to sign out and sign in using their directory accounts in one of the following ways:

* Navigate to your organization-specific URL: `<AccessURL>/{organizationName}/`.
* Or select **Continue with Enterprise SSO** on the main login page.

For Studio and Assistant:

1. Open UiPath Assistant.
2. Navigate to **Preferences** > **Orchestrator Connection**.
3. Sign out of the current session.
4. Set the connection type to **Service URL**.
5. Enter the organization URL: `<AccessURL>/{organizationName}/`.
6. Sign in using your Microsoft Entra ID account.

### Step 4.3: Phasing out local accounts

We recommend removing local user accounts to ensure consistency and simplify the user experience.

Users who continue signing in with local accounts instead of their directory accounts face the following limitations:

* They do not inherit directory group permissions.
* They cannot search for or assign users or groups from the Microsoft Entra ID directory.

The following table summarizes the expected behavior for linked local and directory accounts:

| Capability | Linked local user account | Linked directory user account |
| --- | --- | --- |
| Inherit permissions assigned directly to the user | YES | YES |
| Inherit permissions assigned to directory groups | NO | YES |
| Search for and assign directory users and groups permissions or resources in your organization | NO | YES |
:::important
If you use the manual setup for Microsoft Entra ID integration, you must maintain at least one local user account with admin privileges to manage the integration.
:::

## Advanced configuration

### Restricting access to specific users

By default, all users in your Microsoft Entra ID tenant can access your Test Cloud organization. To restrict access to specific users or groups, take the following steps:

1. In the Microsoft Entra admin center, go to the application you created for the integration in [Step 2: Configuring the Microsoft Entra ID integration](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/microsoft-entra-id-integration-for-automation-cloud-and-automation-cloud-public-sector#step-2%3A-configuring-the-microsoft-entra-id-integration).
2. Go to **Enterprise applications** > **Properties**.
3. Set **User assignment required?** to **Yes**.
4. In **Users and groups**, assign the users or groups who should have access.

All users and groups from your tenant remain searchable in Test Cloud, but only those assigned to the application can sign in. For more details, refer to the [Microsoft documentation on user assignment](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/assign-user-or-group-access-portal?pivots=portal).

### Implementing network restrictions

Use Microsoft Entra ID Conditional Access policies to restrict access based on the following criteria:

* Network location (for example, corporate network only)
* Device compliance
* Risk level

For details on how to configure these policies, see the [Microsoft documentation on Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview).

### Managing privileged access

For Microsoft Entra ID groups used to manage UiPath admin access, implement the following access management practices:

* Enable **Privileged Identity Management (PIM)** in Microsoft Entra ID.
* Configure just-in-time access and approval workflows.
* Set up **regular access reviews** to validate membership and permissions.

For configuration guidance, refer to the [Microsoft documentation on Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure).

## FAQs

### What changes for my users after the integration?

After the integration, users can sign in with their Microsoft Entra ID accounts and retain their existing permissions. If local user accounts are still active, both sign-in methods remain available.

To sign in with a directory account, users can do one of the following:

* Go to the organization-specific URL: `<AccessURL>{organizationName}/`
* On the main login page, select **Continue with Enterprise SSO**.

### Why can I not search for users or groups after configuring the integration?

If you signed in using a local user account instead of your directory account, you will not be able to search for users or groups in your organization.

To understand the differences between local and directory accounts, refer to [Phasing out local accounts](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/microsoft-entra-id-integration-for-automation-cloud-and-automation-cloud-public-sector#step-43%3A-phasing-out-local-accounts).

To resolve the issue, ensure that you are signed in with your Microsoft Entra ID account.

### Do I need to reassign permissions?

No, you do not need to reassigning permissions. When accounts are linked, your organization automatically applies existing permissions to the corresponding Microsoft Entra ID account. Directory user accounts receive permissions from both direct assignments and directory group memberships.

### What Microsoft Entra ID attributes are mapped to UiPath directory user accounts, and when are they updated?

UiPath maps only a limited set of Microsoft Entra ID attributes to directory user accounts. The following table summarizes the available attributes.

All user attributes are updated during sign-in and when users are searched or assigned access to resources in your UiPath organization.

| UiPath organization attributes | Microsoft Entra ID attributes | Purpose |
| --- | --- | --- |
| **Username** | `user.userPrincipalName` | Unique identifier. This property is required when a user is created, and it cannot be cleared during updates. |
| **Display name** | `user.displayName` | The user’s full name, typically a combination of first and last name. This property is required when a user is created, and it cannot be cleared during updates. |
| **First name** | `user.givenName` | The user’s first name. |
| **Last name** | `user.surName` | The user’s last name. |
| **Email** | `user.Mail` | The user’s email address This property is required when a user is created, and it cannot be cleared during updates. |
| **Job title**<sup>1</sup> | `user.JobTitle` | The user's job title. |
| **Department**<sup>1</sup> | `user.Department` | The user’s department. |
| **City**<sup>1</sup> | `user.City` | The user’s city. |
| **Company name**<sup>1</sup> | `user.CompanyName` | The user’s company name. |

<sup>1</sup>Automation Hub is the only service that leverages the **City**, **Job Title**, **Department**, and **Company name** values from Microsoft Entra ID. If you require these attributes, you must request for a higher privileged permission, as documented in [Configuring the Microsoft Entra ID integration](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/microsoft-entra-id-integration-for-automation-cloud-and-automation-cloud-public-sector#step-2%3A-configuring-the-microsoft-entra-id-integration).
:::note
For descriptions of Microsoft Entra ID attributes, refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0).
:::

### How quickly do Microsoft Entra ID group membership changes apply?

Changes to Microsoft Entra ID group membership take effect at the next sign-in or within one hour for users who are already signed in.

### Can I revert to local accounts after integration?

Yes, you can revert to local accounts after integrating with Microsoft Entra ID. An organization administrator must complete the following steps:

1. Re-invite the local user accounts.
2. Migrate all directory group–based permissions to direct assignments on the corresponding local accounts.
3. Ask users to sign out and then sign in with their local user account.

### Can I migrate from Microsoft Entra ID integration to SAML integration?

Yes, you can migrate from Microsoft Entra ID integration to SAML integration. An organization administrator must ensure that both identity systems use the same email address for each user. The administrator must also migrate all permissions assigned through Microsoft Entra ID groups to SAML provisioning rules.

### Why does the integration use the Microsoft Entra ID's hybrid OAuth 2.0 authorization code grant flow?

UiPath uses the hybrid flow to obtain the ID token from the authorization endpoint and to reduce authentication latency, as described in [Microsoft Entra ID documentation](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow#request-an-id-token-as-well-or-hybrid-flow).