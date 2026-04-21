---
title: "Setting up Okta as your identity provider"
visible: true
slug: "setting-up-okta-as-your-identity-provider"
---

:::note
The instructions in this section are for a sample configuration. For more information about any IdP settings that are not covered, refer to [Okta](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm) .
:::

1. In a different browser tab, log in to the Okta Admin Console.
2. Go to **Applications > Applications**, select **Create App Integration**, and select **SAML 2.0** as the sign-on method.
3. In the **General Settings** page, specify a name for the app you are integrating with, namely UiPath.
4. On the **Configure SAML** page, fill in the **General** section as follows:
   1. **Single sign-on URL**: Enter the **Assertion Consumer Service URL** value you got from the UiPath platform.
   2. Select the **Use this for Recipient URL and Destination URL** checkbox.
   3. **Audience URI**: Enter the **Entity ID** value you got from UiPath.
   4. **Name ID Format**: Select **EmailAddress**
   5. **Application Username**: Select **Email**
5. For **Attribute Statements**, add the following:
   1. **Name**: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`. The `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`claim is case-sensitive.
   2. Leave the **Name Format** as **Unspecified**.
   3. Set **Value** to `user.email`, or the user attribute that contains the user's unique email address
   4. Optionally add other attribute mappings. UiPath also supports the First Name, Last Name, Job Title, and Department user attributes. This information is then propagated to UiPath, where it can be made available to other services, such as Automation Hub.
6. On the **Feedback** page, select the option you prefer.
7. Select **Finish**.
8. On the **Sign On** tab, in the **Settings** section, under **View Setup Instructions**, copy the **Identity Provider metadata URL** value and save it for later.
9. On the **Application** page for UiPath, select the newly created application.
10. On the **Assignments** tab, select **Assign > Assign to People**, and then select the users that you want to allow to use SAML authentication for UiPath. The newly added users are displayed on the **People** tab.