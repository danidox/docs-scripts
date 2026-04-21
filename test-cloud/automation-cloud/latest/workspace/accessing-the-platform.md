---
title: "Accessing the platform"
visible: true
slug: "accessing-the-platform"
---

Test Cloud supports multiple authentication methods, depending on the cloud offering, including email and password, enterprise single sign-on (SSO), and trusted third-party identity providers such as Microsoft Entra ID, Google, or LinkedIn. Check out the following sections based on the cloud offering that you use.

## Accessing Test Cloud

Test Cloud allows authentication through email, single sign-on (SSO), as well as trusted third-party services such as Google, Microsoft, and LinkedIn.

The management of this ecosystem is under the control of the administrator. Administrators configure access by signing up, creating the organization and adding users. Non-admin users can sign into an organization if an administrator created the organization and configured access for them in that organization.

### Signing up for Test Cloud

To sign up for Test Cloud, follow these steps:

1. Visit `https://cloud.uipath.com/portal_/register?subscriptionPlan=test-trial`. The **Sign In** window is displayed.
2. Select **Sign up**. The **Create your UiPath user account** window is displayed, with the following sign-up options:
   * Option A: **Work email** and **password**
   * Option B: **Continue with Google**
   * Option C: **Continue with Microsoft**
3. **Option A**: To sign up for Test Cloud with your work email and password, take the following steps:
   1. Fill in your work email and create a password in the **Create your UiPath user account** window.
      :::note
      Password must be at least eight characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
      :::
   2. Select **Create account**. The system sends a verification code to the indicated email address. Copy the received verification code to the clipboard.
   3. Navigate back to Test Cloud, fill in the verification code in the **Verification Code** field or select **Resend** for the system to generate and send a new code to the indicated email address.
   4. Select **Continue** to validate the verification code. If it successfully validates the verification code, the system creates your user account, and the **User account successfully created window** opens.
   5. Fill out the **Display Name** and **Job Title** fields, then select **Next**.
   6. On the following window, choose your **Country** and **State/Region**, and fill in your **Business/Company Name**, then select **Next**. The **Create your cloud organization** window opens. To learn more about organizations, refer to [About organizations](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-organizations).
   7. Fill in the name of your organization.
   8. Select **Create organization**.
4. **Option B**: To sign up for Test Cloud with Google, take the following steps:
   1. Select **Continue with Google**, then wait for the **Choose an account** window to open. Select an existing account or use a different one. The system checks your credentials. If your credentials are associated with an existing organization, you are taken through the sign in process.
   2. If your credentials are not associated with any existing Test Cloud or Automation Cloud organization, the system initiates the sign-up process, guiding you trough creating a new organization by taking the following steps:
      1. Fill in the **Display name** field and select a **Country/Region** in the **Tell us a bit about yourself** window.
      2. Select **Next**. The **Create your cloud organization** window is displayed.
      3. Type in your preferred organization name in the **Cloud Organization Name** field.
      4. Select **Create organization**.
5. **Option C**: To sign up for Test Cloud with Microsoft, take the following steps:
   1. Select **Continue with Microsoft**, then wait for the **Pick an account** window to open. Select an existing account or use a different one. The system checks your credentials. If your credentials are associated with an existing organization, you are taken through the sign in process.
   2. If your credentials are not associated with any existing Test Cloud or Automation Cloud organization, the system initiates the sign-up process, guiding your through creating a new organization by taking the following steps:
      1. Fill in the **Display name** field and select a **Country/Region** in the **Tell us a bit about yourself** window.
      2. Select **Next**. The **Create your cloud organization** window is displayed.
      3. Type in your preferred organization name in the **Cloud Organization Name** field.
      4. Select **Create organization**.You have now successfully signed up and created your Test Cloud organization. You can now sign into the organization and define settings, tenants, users, and configure authentication settings to enable users to sign in under the organization.
   :::note
   To offer users access to the Test Cloud interface, assign yourself and other organization users, the following application testing licenses: **App Tester - Named User** and **App Test Developer - Named User**. For more information on the necessary licenses to use Test Cloud, visit .
   :::

#### After you create an organization

After you create a UiPath organization, take these steps:

1. Go to the **Admin** tab, located on the left-hand side of your newly created organization.
2. Go to **Licenses**.
3. Select **Enterprise Activation**.
4. Retrieve the license code received in the email from the UiPath team, and enter it into the **License Code** field.
5. Select **Activate**.

### Signing in to Test Cloud

To sign in to an existent Test Cloud organization, navigate to https://cloud.uipath.com. The **Sign In** window is displayed, with the following options:

* **Continue with Google**
* **Continue with Microsoft**
* **Continue with LinkedIn**
* **Continue with SSO**
* **Continue with Email**
:::note
If you have access both to Test Cloud and Automation Cloud<sup>TM</sup>, meaning that you have both an **App Tester - Named User** or **App Test Developer - Named User** licenses assigned, as well as other Named User license assigned, then you will land on the Automation Cloud homepage. For more information on Automation Cloud, refer to [About Automation Cloud](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/introduction).
:::

### Signing out

To sign out, follow these steps:

1. Select the user icon from the header.
2. Select **Sign out**.

## Accessing Test Cloud Public Sector

Test Cloud supports federated user management, allowing authentication through trusted third-party services such as Microsoft Entra ID, and other SSO providers.

The management of this ecosystem is under the administrator's control. Administrators configure access by signing up, creating the organization and adding users. Non-admin users can sign into an organization as long as an administrator has created the organization and configured access for them in that organization.

### Signing in to Test Cloud

To sign in to the Test Cloud, follow these steps:

1. Navigate to [**govcloud.uipath.us**](http://govcloud.uipath.us/) **.** The **Sign In** window is displayed, with the following options:
   * **Continue with Microsoft**
   * **Continue with SSO**
   * **Continue with Email.**
2. Option 1. Select **Continue with Microsoft** if you previously signed up to your organization using Microsoft Entra ID and you need to log in to your organization to perform maintenance on SSO settings.
   1. Selecting **Continue with Microsoft** directs you to the **Pick an Account** window managed by Microsoft. Select an existing account or use a different one.
   2. The system validates your credentials. If you are a member of one organization, the system redirects you to the Automation Cloud™ Public Sector **Homepage**. If you are a member of multiple organizations, the system shows you all the organizations you are a member of and enables you to select one. If you are not a member of any organizations, the system doesn't recognize your credentials, so it guides you through the sign-up process.
3. Option 2. Select **Continue with SSO** if your organization was already set up for SSO using your organization's identity provider. This is the preferred option for regular usage of UiPath.
   1. Selecting **Continue with SSO** leads you to the **Sign In with Enterprise SSO** page.
   2. You are asked to fill in your organization's URL. If the URL matches with a known organization, and you are a member, the system signs you in through your assigned provider.
      :::note
      Multi-factor authentication might apply.
      :::
   3. The system validates your credentials. If you are a member of one organization, the system redirects you to the Automation Cloud™ Public Sector **Homepage**. If you are a member of multiple organizations, the system shows you all the organizations you are a member of and enables you to select one. If you are not a member of any organizations, the sign-in fails.
4. Option 3. Select **Continue with Email** to sign in with email and password**.** Use this option to manage the organization without having to authenticate with the organization's identity provider, for example for seting up SSO for the first time.
   1. Fill in the **Email** and **Password**.
      :::note
      Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
      :::
   2. The system validates your credentials. If you are a member of one organization, the system redirects you to the Automation Cloud™ Public Sector **Homepage**. If you are a member of multiple organizations, the system shows you all the organizations you are a member of and enables you to select one. If you are not a member of any organizations, the sign-in fails.

### Signing up with Microsoft SSO

If your company uses Microsoft for authentication, you can sign up for Test Cloud using Microsoft SSO, by following these steps:

1. Navigate to [**govcloud.uipath.us**](http://govcloud.uipath.us/). The **Sign In** window opens.
2. Select **Continue with Microsoft** to use Microsoft SSO. This takes you to Microsoft's **Pick an Account** window.
3. Choose an existing account or opt for using a different one. The system checks your credentials. If your credentials are associated with an existing organization, you are taken through the sign in process. Refer to details about the [sign in](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/accessing-the-platform#accessing-test-cloud-public-sector-signing-in-to-test-cloud) process.
4. If credentials are not associated with any existing Automation Cloud™ Public Sector organization, the system initiates the sign-up process, guiding you through creating a new organization:
   1. Fill out the requested details: **Display Name** and **Job Title**, then select **Next**.
   2. On the next window, choose your **Country** and **State/Region**, and input your **Business/Company Name**, then select **Next**.
   3. On the **Create your cloud organization** window, write the name of your organization and enter the license code obtained from UiPath.
   4. Select **Create Organization**. You have now successfully signed up and created your organization on Automation Cloud™ Public Sector. You can now define [organization settings](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-organization-settings), [tenants](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-tenants), [services](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-services), and configure [authentication settings](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/authentication-settings) to enable users to sign in under that organization.

### Signing up with email and password

If your company does not use Microsoft for authentication, you can sign up for Test Cloud using basic authentication credentials - your email and password.

Follow these steps:

1. Navigate to [**govcloud.uipath.us**](http://govcloud.uipath.us/). The **Sign In** window opens by default, allowing users with an existing Test Cloud account to sign in.
2. Select **Sign up** to create a new user account. The **Create a user account window** opens.
3. Select **Continue with Email** to use your chosen email and password for your account. The **Email** and **Password** fields expand.
4. Fill in the chosen email address and password and select **Continue**. The system sends a verification code to the chosen email address. Copy the received verification code to the clipboard.
5. Back to Test Cloud, fill in the verification code on the **Verification Code** field or select **Resend** for the system to generate and send a new code to the chosen email address.
6. Select **Continue** to validate the verification code. If it successfully validates the verification code, the system creates your user account and the **User account successfully created window** opens.
7. Fill out the requested details: **Display Name** and **Job Title**, then select **Next.**
8. On the next window, choose your **Country** and **State/Region**, and input your **Business/Company Name**, then select **Next**. The **Create your cloud organization** window opens.
9. Write the name of your organization and upload the license file obtained through the [activation of a UiPath license](https://docs.uipath.com/automation-cloud-public-sector/automation-cloud-public-sector/latest/admin-guide/activating-your-license#activating-your-enterprise-license) code flow.
10. Select **Create Organization**. You have now successfully signed up and created your Test Cloud organization. You can now define organization settings, tenants, users, and configure authentication settings to enable users to sign in under that organization.

### Signing up for a new organization with an existing account

To create an additional Test Cloud organization using an existing UiPath account, follow these steps:

1. Navigate to https://govcloud.uipath.us/portal_/signup.
2. Sign in using your existing account credentials. Once successfully logged in, the system initiates the sign up process, guiding you to create a new organization.
3. Fill out the requested details: **Display Name** and **Job Title**, then select **Next.**

   !['User account successfully created' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/332332)
4. On the next window, choose your **Country** and **State/Region**, and input your **Business/Company Name**, then select **Next**.

   !['Just a few more details' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/332336)
5. On the **Create your cloud organization** window, write the name of your organization and upload the license file obtained through the [activation of a UiPath license code](https://docs.uipath.com/automation-cloud-public-sector/automation-cloud-public-sector/latest/admin-guide/activating-your-license#activating-your-enterprise-license).
6. Select **Create Organization**. You have now successfully signed up and created your organization on Test Cloud. You can now define organization settings, tenants, services, and configure authentication settings to enable users to sign in under that organization.

### Signing out

To sign out, take the following steps:

1. Select the user icon from the header.
2. Select **Sign out**.

## Accessing Test Cloud Dedicated

Test Cloud supports user management, allowing authentication through trusted third-party services such as Microsoft Entra ID, and other SSO providers.

The management of this ecosystem is under the administrator's control. Administrators configure access by adding users. Non-admin users can sign into an organization as long as an administrator has configured access for them in that organization.

### Logging in

To sign in to Test Cloud, take the following steps:

1. Navigate to `https://cloud.uipath.com`. Here you must use the custom URL that you chose for your dedicated instance.
2. Option 1. In the **Login** window, fill in the **Organization name**, **Username or email**, and **Password** fields.
   1. For the **Organization name**, type the name of your organization to access that specific organization portal. If a different organization is already set, select **Change** next to its name to specify a different organization name .

      !['Change organization name to log in' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/510055)
   2. In the **Username or email** and **Password** fields, type your credentials.
   3. Select **Log in**.
3. Option 2. Select **Continue with Enterprise SSO** if your organization was already set up for SSO using your organization's identity provider.

   ![docs image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/546369)

### Signing out

To sign out, take the following steps:

1. Select the user icon from the header.
2. Select **Sign out**.