---
title: "Setting up PingOne as your identity provider"
visible: true
slug: "setting-up-pingone-as-your-identity-provider"
---

:::note
The instructions in this section are for a sample configuration. For more information about any IdP settings that are not covered, refer to [PingOne](https://docs.pingidentity.com/r/en-us/pingone/pingone_p1tutorial_add_a_saml_app).
:::

1. In a different browser tab, log in to the Ping One Admin Console.
2. Go to **Connections > Applications**, and select the plus icon .
3. Select **Web App**, and for **SAML** select **Configure**.
4. On the **Create App Profile** page, specify a name for your UiPath app.
5. On the **Configure SAML Connection** page, select **Manually Enter** and provide the following details:
   * **ACS URLs**: Enter the **Assertion Consumer Service URL** value you got from UiPath.
   * **Entity ID**: Enter the **Entity ID** value you got from UiPath.
   * **SLO binding**:**HTTP Redirect**
   * **Assertion Validity Duration**: Enter the number of seconds for the validity period.
6. Select **Save and Continue**.
7. On the **Map Attributes** page, add the email address:
   1. Select **+ Add Attribute**.
   2. For **Application Attribute**, enter `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`. The `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`claim is case-sensitive.
   3. Set **Outgoing Value** to **Email Address**, or the user attribute that contains the user's unique email address.
   4. Select the **Required** checkbox.
   5. Optionally add other attribute mappings. UiPath also supports the First Name, Last Name, Job Title, and Department user attributes. The attributes are case sensitive. This information is then propagated to UiPath, where it can be made available to other services, such as Automation Hub.
8. Select **Save and Close**.
9. Turn on the toggle for the UiPath app to enable the application for user access.
10. On the **Configuration** tab, copy and save the **IdP Metadata URL** value for later use.