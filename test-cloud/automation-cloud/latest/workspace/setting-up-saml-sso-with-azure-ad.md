---
title: "Setting up SAML SSO with Microsoft Entra ID"
visible: true
slug: "setting-up-saml-sso-with-azure-ad"
---

You can use the Azure portal to enable SSO for an Enterprise application that you added to your Microsoft Entra ID tenant.

After you configure SSO, your users can sign in by using their Microsoft Entra ID credentials.
:::important
If your users are in Microsoft Entra ID, but you cannot use the Microsoft Entra ID integration instructions to configure Microsoft Entra ID to your UiPath® organization, configuring Microsoft Entra ID as a SAML-based identity provider may be an option. This is due to restrictions around giving permissions to read user details and group memberships of all UiPath users. The [Microsoft Entra ID native integration](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration) is recommended due to its advanced features. If however, you switch to SAML, you must manually replace role assignation done through directory groups with direct role assignation to the directory accounts to keep your access schema without having to recreate it from scratch.
:::

## Managing claims

**UiPath** requires either the `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` or the `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn` claims to be sent by the SAML identity provider. The `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` claim is case-sensitive.

If both claims are sent in the ACS payload, then UiPath will prioritize the `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` claim.

By default, the application in Microsoft Entra ID is configured to send the `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` claim, with the user's email address as the value for the claim.

If you are switching from or planning to switch to [Microsoft Entra ID directory integration](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration), please note:

* The value passed in the prioritized claim is used by UiPath as a unique identifier and is used to link any existing local users (using the local user's email address) to this directory user in Microsoft Entra ID.
* For a smooth switch between Microsoft Entra ID and SAML directory integration, it is recommended you pass in both of these claims with the appropriate user values. The following configuration is an example:
  !['Managing claims' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/309238)

## Enabling SAML SSO for an application

1. Log into the [Azure portal](https://portal.azure.com/#home) using one of the roles listed in the prerequisites.
2. Go to Microsoft Entra ID, then select **Enterprise applications**. The **All applications** page opens that lists the applications in your Microsoft Entra ID tenant. Search for and then select the application that you want to use. For example, **UiPath**.
   :::note
   To create an application for SSO, follow the steps in [Create application for SSO](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/setting-up-saml-sso-with-azure-ad#create-application-for-sso).
   :::
3. From the left sidebar in the **Manage** section, select **Single sign-on** to open the **SSO editing** page.
4. Select SAML to open the **SSO configuration** page. After the application has been configured, users can sign into it using their Microsoft Entra ID tenant credentials.
5. Under the **Basic SAML Configuration** section, select **Edit**.
6. Fill out the **Entity ID** and **Assertion Consumer Service (ACS) URL** fields based on the values provided in the SAML configuration settings in the portal.
   !['Data to be configured in IdP' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/310434)

   !['Basic SAML configuration' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/310438)
7. Select **Save**.
8. Copy the **App Federation Metadata Url**.
9. Navigate to the **UiPath Administration** portal and go to the **SAML Configuration** page.
10. Paste the **App Federation Metadata Url** in the **Metadata URL** field.
11. Select **Fetch data** to have the system request user-related info from the identity provider.

## Setting up claims for automatic provisioning

1. Log into the [Azure portal](https://portal.azure.com/#home) using one of the roles listed in the prerequisites.
2. Go to Microsoft Entra ID, then select **Enterprise applications**. The **All applications** page opens that lists the applications in your Microsoft Entra ID tenant. Search for and then select the application that you want to use. For example, **UiPath**.
   :::note
   To create an application for SSO, follow the steps in [Create application for SSO](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/setting-up-saml-sso-with-azure-ad#create-application-for-sso).
   :::
3. From the left sidebar in the **Manage** section, select **Single sign-on** to open the **SSO editing** page.
4. Select **Edit** in the **Attributes & Claims** section of the **SSO editing** page.
   !['Attributes and claims' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/309301)
5. Select **Add a group claim** to configure the groups that you want to send to UiPath.
   :::note
   To set advanced configurations, choose from the **Advanced Settings** dropdown.
   :::
6. Select **Save**.
7. To finish the configuration, follow the [Step 2.5. Configure provisioning rules (optional)](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-the-saml-integration#step-25-configure-provisioning-rules-(optional)) steps from our public documentation.
:::note
If a customer prefers to use **UPN**, you can navigate to the **Attributes & Claims** section and change the value for the **emailaddress** attribute.
:::

## Create application for SSO

1. Log into the [Azure portal](https://portal.azure.com/#home) using one of the roles listed in the prerequisites.
2. Go to Microsoft Entra ID, then select **Enterprise applications**.The **All applications** page opens that lists the applications in your Microsoft Entra ID tenant.
3. Select **New Application** > **Create your own application**.
4. Give your application a name. For example, **UiPath**.
5. Select **Integrate any other application that you don't find in the gallery (Non-gallery)**.
6. Select **Create**.