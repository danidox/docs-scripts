---
title: "Microsoft Entra ID integration for Test
               Cloud Dedicated"
visible: true
slug: "azure-ad-integration"
---

This procedure applies only for Test Cloud Dedicated

## Configuring Azure for the integration

Your organization requires an app registration in your Microsoft Entra ID tenant and some configuration so that it can view your AD members to establish account identity. The app registration details are also required to later connect your organization to your Microsoft Entra ID tenant.

**Permissions:** You must be an **administrator in Azure** to perform the tasks in this section. The following Azure administrator roles have the required privileges: Global Administrator, Cloud Application Administrator, or Application Administrator.

There are two ways to set up your Azure tenant for the integration:

* Take the following steps to manually configure an app registration for the integration.
* Use the UiPath Microsoft Entra ID scripts that we created for this task, which are available on [GitHub](https://github.com/UiPath/platform-quickstart/tree/master/azure-ad-integration): The **`configAzureADconnection.ps1`** script performs all the actions described in this section and returns the app registration details. Then you can run the **`testAzureADappRegistration.ps1`** script to make sure the app registration was successful.

To manually configure your Azure tenant, take the following steps in Azure Portal:

1. Create an app registration for Test Cloud. For details, refer to Microsoft's documentation about [Registering an application.](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#register-an-application)

During registration, select **Accounts in this organizational directory only** and set the **Redirect URI** to `https://cloud.uipath.com/identity_/signin-oidc`.

   :::note
   If you already have a registered application for your organization, there is no need to create a new one, but make sure that the app is set up as previously described.
   :::
2. Open the application's **Overview** page, copy the **Application (client) ID** and **Directory (tenant) ID**, and save them for later use:

   !['Overview page' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30649)
3. Go to the **Authentication** page of your app:
   1. Under **Redirect URIs**, select **Add URI** to add a new entry.
   2. Add `https://cloud.uipath.com/portal_/testconnection` to the **Redirect URIs** list.
   3. At the bottom, select the **ID tokens** checkbox.
   4. Select **Save**.

      !['Authentication page' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30745)
4. Go to the **Token configuration** page.
5. Select **Add Optional Claim**.
6. Under **Token type**, select **ID**.
7. Select the checkboxes for **`family_name`**, **`given_name`**, and **`upn`** to add them as optional claims:

   !['Token configuration page' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30994)
8. Go to the **API permissions** page.
9. Select **Add permission** and add the following delegated permissions from the **Microsoft Graph** category:
   * **OpenId permissions** - `email`, `openid`, `offline_access`, `profile`
   * **Group member permissions** - `GroupMember.Read.All`
   * **User permissions** - `User.Read`, `User.ReadBasic.All`, `User.Read.All` (requires administrative consent)

     !['Add permissions' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/316144)

The following table describes the API permissions:

   | Permission | What it allows you to do | What we do with it |
   | --- | --- | --- |
   | `email`, `openid`, `profile`, `offline_access`, `User.Read` | Allows Microsoft Entra ID to issue a user token to the system application | Allow users to log into the system using a Microsoft Entra ID login. This permits us to keep our user object updated, ensuring consistency of these attributes. |
   | `User.ReadBasic.All` | Reads basic properties of all users in the directory that the logged in user is allowed to view | When a user assigns permissions to other users in the directory to their resources, they are able to search these users. The functionality for access management/authorization are in the system user experience. |
   | `User.Read.All` (requires admin consent) | Reads all user properties in the directory that the logged in user is allowed to view | Your administrator may want to import these additional user properties to configure permissions or display custom information inside the system services. For Automation Hub, customers looking to obtain the full set of attributes from Microsoft Entra ID, it is necessary to grant the `User.Read.All` permission to the app. |
   | `GroupMember.Read.All` | Reads the group memberships of all the users that the signed in user has access to | If your organization is using groups to manage permissions in the system, then the platform needs to be able to list all the groups and discover the members of a group. That allows both management and enforcement of group assigned permissions. |

To learn more about UiPath's access with these permissions, refer to our [Encryption documentation](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/encryption).
10. Select the **Grant admin consent** checkbox.
    :::note
    The administrator consents on behalf of all users in the tenant active directory. This allows the application to access the data of all users, without users being prompted to consent. For more information about permissions and consent, refer to Microsoft's [Microsoft Entra ID documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent?WT.mc_id=Portal-Microsoft_AAD_RegisteredApps).
    :::
11. Go to the **Certificates & secrets** page to create a new client secret or a new certificate.
    * Option 1. Client secret. For more information about client secrets, refer to Microsoft's documentation about [Adding a new client secret](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-client-secret).
      :::note
      The created client secret is not permanent. You must update the client secret after its validity period.
      :::
    * Option 2. Certificate. The high-level steps for configuring certificates are described in [Setting up an Azure Key Vault certificate for UiPath](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/azure-ad-integration#setting-up-an-azure-key-vault-certificate-for-uipath). For more on certificates, see [Setting and retrieving a certificate from Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/certificates/quick-create-portal) in the Microsoft documentation.
12. Provide your organization administrator with the **Directory (tenant) ID**, **Application (client) ID** values. If you chose the client secret option, also share the **Client Secret** value. If you chose the certificate option, share the certificate details. This information enables the administrator to proceed with the configuration.

    !['New client secret' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30669)

### Setting up an Azure Key Vault certificate for UiPath

This section outlines the high-level steps for configuration with a certificate. You can also use a client secret. For more details about setting up certificates, check [setting and retrieving a certificate from Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/certificates/quick-create-portal) in the Microsoft documentation. Follow these high-level steps to set up a certificate:

1. Log in to Azure Key Vault and navigate to the **Certificates** section.
2. Create a certificate with the **Subject** as `CN=uipath.com` and **Content Type** as `PEM` **.**

   !['Create a certificate' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/495655)
3. After creation, download the certificate in PFX/PEM format.
4. Open the `.pem` file with a text editor. It should consist of two sections: `BEGIN PRIVATE KEY/END PRIVATE KEY` and `BEGIN CERTIFICATE/END CERTIFICATE`.
5. Create a new `.pem` file containing only the lines between `BEGIN CERTIFICATE` and `END CERTIFICATE.`
6. In the Azure portal, locate the **Certificates & secrets** tab in your App Registration and upload the new `.pem` file.
7. As part of the {Delivery option} configuration, you need to add the entire content of the downloaded `.pem` certificate from Azure Key Vault in the **Client secret or certificate** field.
   :::note
   The maximum permitted size for certificates is 10KB.
   :::

## Deploying the integration

After Azure setup is complete, you can prepare for the integration, activate it, and then clean up old accounts. The process is broken down in stages so that there is no disruption for your users.
:::note
You must be an organization administrator to perform the tasks in this section.
:::

### Clean up inactive users

When you connect UiPath to Microsoft Entra ID by activating the integration, accounts with matching email addresses are linked, so that the Microsoft Entra ID account benefits from the same permissions as the matching UiPath local account.

If your organization practices email recycling, meaning that an email address that was used in the past could be assigned to a new user in the future, this could lead to a risk of elevated access.

Let's say you once had and employee whose email address was `john.doe@example.com` and this employee had a local account where he was an organization administrator, but has since left the company and the email address was deactivated, but the user was not removed.

When a new employee who is also named John Doe joins your company, he receives the same `john.doe@example.com` email address. In such a case, when accounts are linked as part of the integration with Microsoft Entra ID, John Doe inherits organization administrator privileges.

To prevent such situations, make sure you remove all users who are no longer active from the UiPath organization before proceeding to the next step. You can skip this step if inactive email addresses are not reused in your organization.

### Activate the Microsoft Entra ID integration
:::note
**Before you begin:**
* make sure that [Azure
configuration](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/azure-ad-integration#configuring-azure-for-the-integration) is complete;
* obtain the **Directory
(tenant) ID**, **Application (client) ID**, and **Client Secret** values for UiPath's app registration in Azure from your Azure administrator.
:::
To activate the Microsoft Entra ID integration, apply the following steps in UiPath:

1. Go to **Admin** and, if not already selected, select the organization at the top of the left pane.
2. Select **Security** to open **Security Settings**.
3. On the **Authentication Settings** tab, under **Directory integration for SSO**, select **Configure SSO**.
4. Select **Microsoft Entra ID** from the SSO configuration panel.
5. Fill in the fields with the information received from your Azure administrator.
6. Select the checkbox for **I understand & accept added users and Microsoft Entra ID users with matching email addresses will have their accounts linked.**
7. Select **Test Connection** to validate the integration has been configured correctly.
8. When prompted, sign in with your Microsoft Entra ID account.

A successful sign in indicates that the integration has been configured correctly.In case it fails, ask your Azure administrator to check that Azure is correctly configured and then try again.
9. Select **Save** to activate the integration for your organization.

After you save your changes, matching accounts are automatically linked.​
10. Sign out.
11. Navigate to the organization URL (`<AccessURL>/organizationID/`) and sign in with your Microsoft Entra ID account.

Now you can work with the users and groups in the linked tenant's Microsoft Entra ID. Directory accounts and groups are not listed in either the **Users** or **Groups** pages under **Admin** - **Accounts & Groups**, you can only find them through search.

### Test the Microsoft Entra ID integration

To check that the integration is running, sign in as an organization administrator with a Microsoft Entra ID account and try to **search** for Microsoft Entra ID users and groups on any related page, such as the **Edit Group** panel in the Test Cloud (**Admin** > **Accounts and Groups** > **Groups** > **Edit**).

If you can search for users and groups that originate in Microsoft Entra ID, it means the integration is running. You can tell the type of user or group by its icon.

If you encounter an error while trying to search for users, as shown in the following example, this indicates that there is something wrong with the configuration in Azure. Reach out to your Azure administrator and ask them to check that Azure is set up as described earlier in the documentation on **Configuring Azure for the Integration**.
:::tip
Ask your Azure administrator to confirm that they selected the **Grant admin consent** checkbox during Azure configuration. This is a common cause why the integration fails.
:::

Azure administrators can use the UiPath Microsoft Entra ID test script `testAzureADappRegistration.ps1`, which is available on [GitHub](https://github.com/UiPath/platform-quickstart/tree/master/azure-ad-integration), to find and fix any configuration issues when the cause is not clear.

    !['User details' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31791)

## Completing the transition to Microsoft Entra ID

After the integration is active, we recommend that you follow the instructions in this section to ensure that user creation and group assignations are handed off to Microsoft Entra ID. This way you can build on top of your existing identity and access management infrastructure for easier governance and access management control over your UiPath resources.

### Configure groups for permissions and robots (optional)

You can do this to ensure that the Azure administrator can also onboard new users with the same permissions and robot configuration you had set up prior to the integration. They can do this by adding any new users to a Microsoft Entra ID group if the group has the required roles already assigned.

You can map your existing user groups from UiPath to new or existing groups in Microsoft Entra ID. You can do this in several ways, depending on how you use groups in Microsoft Entra ID:

* If users with the same roles in UiPath are already in the same groups in Microsoft Entra ID, the organization administrator can add these Microsoft Entra ID groups to the user groups that these users were in. This ensures that users keep the same permissions and robot setup.
* Otherwise, the Azure administrator can create new groups in Microsoft Entra ID to match the ones in UiPath and add the same users that are in the UiPath user groups. Then the organization administrator can add the new Microsoft Entra ID groups to the existing user groups to ensure the same users have the same roles.

Ensure to verify any roles specifically assigned to users, in all instances. If feasible, remove these direct role assignments, and add these users into groups already assigned with these roles.

For example, let's say the **Administrators** group in UiPath includes the users Anna, Tom, and John. These same users are also in a group in Microsoft Entra ID called **admins**. The organization administrator can add the **admins** Azure group to the **Administrators** group in UiPath. This way, Anna, Tom, and John, as members of the **admins** Microsoft Entra ID group, all benefit from the roles of the **Administrators** group in UiPath.

Because **admins** is now part of the **Administrators** group, when you need to onboard a new administrator, the Azure administrator can add the new user to the **admins** group in Azure, thus granting them administration permissions in UiPath without having to make any changes in UiPath.
:::note
Changes to Microsoft Entra ID group assignments apply in UiPath when the user logs in with their Microsoft Entra ID account, or if already logged in, within an hour.
:::

### Migrate existing users

For the permissions assigned to Microsoft Entra ID users and groups to apply, users must sign in at least one time. We recommend that, after the integration is running, you communicate to all your users to sign out of their local account and sign in again with their Microsoft Entra ID account. They can sign in with their Microsoft Entra ID account by:

* Navigating to the UiPath organization-specific URL, in which case the sign in type is already selected. The URL must include the organization ID and end in a forward slash, such as `<AccessURL>/orgID/`.
* By selecting **Enterprise SSO** on the main login page. Make sure you provide your organization-specific URL to all your users.

Migrated users receive the combined permissions directly assigned to them in UiPath along with those from their Microsoft Entra ID groups.

To set up Studio and Assistant to connect with Microsoft Entra ID accounts:

1. In Assistant, open **Preferences** and select the **Orchestrator Connection** tab.
2. Select **Sign Out**.
3. For the connection type, select **Service URL**.
4. In the **Service URL** field, add the organization-specific URL The URL must include the organization ID and end in a forward slash, such as `<AccessURL>/orgID/`. Otherwise the connection fails saying that the user does not belong to any organization.
5. Sign back in with the Microsoft Entra ID account.
:::important
Permissions from Microsoft Entra ID groups don't influence the automations from classic folders or the robots that are connected using the machine key. To operate under group-based permissions, configure the automations in modern folders and use the **Service URL** option to connect to UiPath Assistant or Studio.
:::

### Discontinue use of UiPath local accounts (optional)

We recommend that you remove the use of local accounts to maximize the core compliance and efficiency benefits of the complete integration between UiPath and Microsoft Entra ID.
:::important
Only remove **non-administrator** accounts. It is recommended to retain at least one organization administrator local account to be able to change authentication settings in the future.
:::

After all users have been migrated, you can remove the non-admin users from the **Users** tab, so that your users won't be able to sign in using their local account anymore. You can find these accounts based on their user icons.

You can also clean up individual permissions in the UiPath services, such as the Orchestrator service, and remove individual users from groups so that permissions rely exclusively on Microsoft Entra ID group membership.

## Advanced features

The following section describes a few useful pointers for advanced features you can leverage now that you have the Azure AD integration set up.

**Restrict access to your organization**

Because the integration with Azure AD is performed at the level of the Azure tenant, by default all Azure AD users can access Test Cloud. The first time an Azure AD user signs in to their UiPath organizaton, they are automatically included in the UiPath group **Everyone**, which grants them the User role in the organization which provides the basic level of access within the UiPath ecosystem.

If you want to only allow certain users to access your organization, you can activate user assignment for the UiPath app registration in Azure. This way, users need to be explicitly assigned to the app to be able to access it. For instructions, refer to [how to restrict your app to a set of users](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-restrict-your-app-to-a-set-of-users) in Microsoft's Azure AD documentation.

**Restrict access to trusted networks or devices**

If you want to only allow your users to access Test Cloud from a trusted network or a trusted device, you can use the [Azure AD Conditional Access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/plan-conditional-access) feature.

**Governance for groups in Azure AD**

If you have created groups in Azure AD for easy UiPath onboarding directly from Azure AD, as described earlier in [Configure groups for permissions and robots](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/azure-ad-integration#configure-groups-for-permissions-and-robots-(optional)), you can use the advanced security options of privileged identity management (PIM) for these groups to govern access requests for UiPath groups. For details, refer to the Microsoft documentation on [PIM](https://docs.microsoft.com/en-us/azure/active-directory/privileged-identity-management/groups-features).

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