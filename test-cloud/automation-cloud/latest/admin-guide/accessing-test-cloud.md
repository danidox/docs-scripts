---
title: "Accessing Test Cloud"
visible: true
slug: "accessing-test-cloud"
---

Test Cloud allows authentication through email, single sign-on (SSO), as well as trusted third-party services such as Google, Microsoft, and LinkedIn.

The management of this ecosystem is under the control of the administrator. Administrators configure access by signing up, creating the organization and adding users. Non-admin users can sign into an organization if an administrator created the organization and configured access for them in that organization.

## License-based accessing

Given that Test Cloud is a dedicated application testing interface of Automation Cloud<sup>TM</sup>, accessing it is possible only if you follow these conditions:

1. You sign up for Test Cloud using the [Sign up for Test Cloud](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/accessing-test-cloud#signing-up-for-test-cloud) procedure.
2. After you create an organization, assign the following user licenses for yourself:
   * **App Tester - Named User**
   * **App Test Developer
     - Named User**

## Signing up for Test Cloud

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
   2. If your credentials are not associated with any existing Test Cloud or Test Cloud organization, the system initiates the sign-up process, guiding you trough creating a new organization by taking the following steps:
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
   To offer users access to the Test Cloud interface, assign yourself and other organization users, the following application testing licenses: **App Tester - Named User** and **App Test Developer - Named User**. For more information on the necessary licenses to use Test Cloud, visit [Licensing](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/licensing-test-cloud#licensing).
   :::

### After you create an organization

After you create a UiPath organization, take these steps:

1. Go to the **Admin** tab, located on the left-hand side of your newly created organization.
2. Go to **Licenses**.
3. Select **Enterprise Activation**.
4. Retrieve the license code received in the email from the UiPath team, and enter it into the **License Code** field.
5. Select **Activate**.

## Signing in to Test Cloud

To sign in to an existent Test Cloud organization, navigate to https://cloud.uipath.com. The **Sign In** window is displayed, with the following options:

* **Continue with Google**
* **Continue with Microsoft**
* **Continue with LinkedIn**
* **Continue with SSO**
* **Continue with Email**

After signing in, you will land on the Test Cloud homepage. For more information on Test Cloud's user interface, visit [Exploring the user interface](https://docs.uipath.com/test-cloud/automation-cloud/latest/admin-guide/exploring-the-test-cloud-user-interface#exploring-the-user-interface).
:::note
If you have access both to Test Cloud and Automation Cloud<sup>TM</sup>, meaning that you have both an **App Tester - Named User** or **App Test Developer - Named User** licenses assigned, as well as other Named User license assigned, then you will land on the Automation Cloud homepage. For more information on Automation Cloud's user interface, visit [Exploring the user interface](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/exploring-the-user-interface).
:::

## Signing out

To sign out, follow these steps:

1. Select the user icon from the header.
2. Select **Sign out**.