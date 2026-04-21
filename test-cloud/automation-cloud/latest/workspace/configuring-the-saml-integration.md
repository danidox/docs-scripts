---
title: "Configuring the SAML integration"
visible: true
slug: "configuring-the-saml-integration"
---

![](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555) This feature is available with the Enterprise licensing plan.

By using SAML configuration in UiPath we enhance both security and efficiency in authentication. Our system uses SAML to enable Single Sign-On (SSO) via secure access tokens, allowing the UiPath platform to connect with any Identity Provider (IdP) that uses the SAML 2.0 standard.

Additionally, our SAML configuration includes Single Logout (SLO) capabilities, which enable simultaneous logouts across all your applications unified under your IdP.

The SAML Integration is designed such that it can be implemented gradually, with no disruption to existing users.
:::note
**Switching from the native Microsoft Entra ID integration to SAML integration** If you are using Microsoft Entra ID for authentication, we recommend using our native Microsoft Entra ID integration because it is more feature-rich. If you do decide to switch to SAML integration, you must manually replace role assignation done through directory groups with direct role assignation to the directory accounts so that you do not have to completely recreate your access schema.
:::

## Known limitations

* Encrypted SAML assertions from your identity provider are not supported.
* You cannot search users and groups from your identity provider. Only provisioned directory users are available for searching.
* You cannot view directory users at the organization level. Only local users appear at the organization level. Just-in-time provisioning adds directory users, so they do not show up on the **Accounts & Groups** page in UiPath.

## Prerequisites

To set up the SAML integration, you need the following:

* A licensing plan of type Enterprise. For more details on licensing plans, refer to [Unified Pricing licensing plan framework](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/unified-pricing-licensing-plan-framework#unified-pricing%3A-licensing-plan-framework).
* Administrator permissions in both the UiPath organization and your third-party identity provider. If you don't have administrator permissions in your identity provider, you can work with an administrator to complete the setup process.
* UiPath® Studio and UiPath Assistant version 2020.10.3 or later, so that you can set them up to use the [recommended deployment](https://docs.uipath.com/robot/standalone/latest/admin-guide/setting-up-interactive-sign-in).

## Step 1. Clean up inactive user accounts

If your organization recycles email addresses, it is important to remove all inactive user accounts before you configure the SAML Integration.

When you enable the integration, local accounts present in UiPath can be linked with the directory account in the external identity provider that uses the same email address. This account linking occurs when the directory account user with the email address signs in for the first time. The identity from your identity provider inherits all roles from the local account, so that the transition is seamless. Because of this, with inactive local accounts present in UiPath, there is a risk that local accounts and directory accounts are mismatched, which can lead to unintended elevation of permissions.

To remove inactive user accounts:

1. Log into UiPath as an organization administrator.
2. Go to **Admin**, select your organization, and then select **Accounts & Groups**. The **Accounts & Groups** page for the organization opens on the **Users** tab.
3. Select the column header for the **Last active** column to reorder users so that the ones with the oldest date for last login are shown at the top. The **Last active** column show the user's last login date. **Pending** in this column means the user never logged in.
4. Select the **Delete** icon at the end of the row to remove the local account for that user.
   !['Delete local account' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31779)
5. In the confirmation dialog, select **Delete** to confirm deleting the account from UiPath. The user account is removed from the page.
6. Continue to delete all inactive user accounts in your organization.

## Step 2. Configure the SAML integration

Now, you must configure both UiPath and your identity provider (IdP) for the integration.

### Step 2.1. Obtain SAML service provider details

1. Log in to UiPath as an organization administrator.
2. Go to **Admin**, select your organization, and then select **Security**. The **Security Settings** page for the organization opens on the **Authentication Settings** tab.
3. Under **Directory configuration for SSO,** select **Configure SSO**. The **SSO configuration** window opens, describing the advantages and prerequisites for the integration.
4. From the two SSO options, select **SAML 2.0**. The **SAML SSO configuration** page opens on the **Configure identity provider** tab.
5. In the top section of the page, you can find the UiPath information needed to configure your identity provider: **Metadata URL**, **Assertion consumer service URL**, **Entity ID**. Copy and save them for configuring the identity provider.
   :::important
   We highly recommend using the UiPath **metadata URL** as part of your identity provider configuration process. This enables automatic updates whenever we initiate rotations for our signing certificates, ensuring uninterrupted operation of the platform.
   :::

   !['Configure Identity provider'](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/457811)
6. The entity ID contains the organization ID by default. You can change the format to use the global identifier (no organization ID) by using the **Change entity ID format** option. Then, on the **Change entity ID format** window, in the **Entity ID format** drop-down, select **Org specific identifier** to use the format containing the organization id, or **Global identifier** to use the format that does not contain the organizaiton id. We recommend using the organization specific identifier, because it allows you to enroll multiple UiPath organizations in your identity provider, if you ever want to.

Keep this browser tab open for later.

### Step 2.2. Configure your identity provider

You can connect to any third-party identity provider (IdP) that uses the SAML 2.0 standard. While configuration may vary depending on your chosen IdP, we have validated the configuration for using either Okta or PingOne, which you can use as reference to configure the integration.

[Setting up Okta as your identity provider.](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/setting-up-okta-as-your-identity-provider#setting-up-okta-as-your-identity-provider)

[Setting up PingOne as your identity provider.](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/setting-up-pingone-as-your-identity-provider#setting-up-pingone-as-your-identity-provider)

For other identity providers, we recommend that you follow their integration documentation.

### Step 2.3. Configure UiPath cloud offering

To enable your UiPath cloud offering as a service provider that recognizes your identity provider, take the following steps:

1. Return to the **SAML SSO configuration** tab in the organization
2. In the second section of the **Configure identity provider** page, you can view the fields necessary to configure the identity provider. In the **Metadata URL** field, enter the metadata URL of your identity provider. This enables UiPath to regularly fetch and update data from your identity provider, streamlining the SAML configuration process for the long term.
   :::important
   We highly recommend using the **metadata URL** during SAML configuration. This enables UiPath to regularly fetch and update data from your identity provider, preventing you from having to manually update the Identity provider's signing certificate in UiPath when it is rotated.
   :::

   !['Configure identity provider' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/457811)
3. Select **Fetch data**. When complete, the **Sign-on URL**, **Identity Provider Entity ID**, and **Signing certificate** fields are populated with the IdP information.
4. Even though it's not the recommended method, you can choose to manually enter the SAML details of your identity provider on the **Sign-on URL**, **Identity Provider Entity ID**, and **Signing certificates** fields.
5. To manually enter multiple certificates, paste them into the **Signing certificate** field in base64 encoding, enclosed by the begin and end certificate indicators, and separated by a new line character. For example, having two certificates, you should use the following format:
   ```
   -----BEGIN CERTIFICATE-----
   <base64 encoded certificate retrieved from SAML metadata URL or SAML admin>
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   <base64 encoded certificate retrieved from SAML metadata URL or SAML admin>
   -----END CERTIFICATE-----
   ```

!['Signing certificate fiels' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/253932)
6. Select **Next** in the bottom right corner to move to the next step. You are taken to the **Map attributes & complete** tab. Mapping attributes, referred to as "claims", link user details between your identity provider and UiPath. This ensures user data, like an email or username, matches across both systems.
7. By default the email address is used as the users' identifier. If you want the option to set up a unique identifier that is not an email address, contact UiPath support. Otherwise, follow these steps:
   1. The **Email** field becomes mandatory and you cannot change it.
   2. Fill in the **Allowed Domains** section with the domains from which you want to allow users to sign in. Enter all of the domains that are supported by the configured identity provider. Separate multiple domains using commas.
      :::note
      You can enter a maximum number of 100 domains.
      :::
   3. Under **Attribute Mapping**, fill in the **Display Name** field with the attribute from your IdP that you want to show in your organization as the name for users. You can use the **First Name** and **Last Name** attributes.
   4. Optionally, add new mappings, by specifying the respective claim from the identity provider and the corresponding attribute in your organization.
8. If you contact UiPath support to set up a unique identifier for a user, the **Enable the custom unique identifier** option appears. The following steps apply only if you are using Test Cloud and Test Cloud Public Sector. For Test Cloud Dedicated, the support team handles the enablement of custom unique identifier.
   :::warning
   Before enabling a unique identifier that is not an email address, review the following known implications:
   * Orchestrator requires
   a unique email address for assigning roles. Users with different unique identifiers but the same email address cannot be assigned roles in Orchestrator. Alternatively, if the user has a unique identifier but no email address, then they can be assigned permissions in Orchestrator.
   * You cannot link
   accounts based on emails, if the user has a unique identifier.
   * Users will not
   receive emails from the UiPath platform if their email field is left blank.
   * Once you have set a
   **Unique Identifier** claim name, changing it can result in a loss of previously recognized users, as the system might not be able to identify them anymore. As such, the UI restricts changing the **Unique Identifier** claim once it's been set. To change it, you need to delete and recreate your entire configuration.
   :::

   1. Select **Enable the custom unique identifier** to set up a unique identifier that is not an email

This can help if, for example, your users do not all have email accounts or if their email address is not unique.
   2. It is mandatory to enter the unique identifier of your users in the **Unique identifier** field. This is the claim UiPath uses to identify users when they sign in.
   3. In the **Display Name** field, enter the claim by which your users can be recognized when logging in.
   4. It becomes optional to enter the **Email** field for your users.
   5. The **Allowed email address domains** field is grayed out and not available for input. This is because the system doesn't use the email as the unique identifier anymore, making this field irrelevant.
   6. Optionally, add new mappings, by specifying the respective claim from the identity provider and the corresponding attribute in UiPath.
9. Once you have set up the attributes, configure the **Allow unsolicited authentication response** and **SAML binding type** fields.
   1. **Allow unsolicited authentication response**: Enable if you want to be able to navigate to the UiPath platform from the IdP dashboard.
   2. **SAML binding type**: Select how the SAML configuration should communicate, via the HTTP user agent. Select **HTTP redirect** to use URL parameters, or **HTTP post** to use an HTML form with base64-encoded content.
10. If your identity provider requires UiPath to sign all SAML authentication requests, select the **Sign Authentication Request** option. Check with your identity provider to determine if this feature needs to be enabled. UiPath commonly updates its signing keys. For example, UiPath rotates the signing certificate every two weeks. If you have activated the **Sign Authentication Request** feature, make sure your IdP regularly syncs with UiPath by continually downloading the updated keys from UiPath's metadata URL.
11. Select **Test and Save** to finish configuring the integration.

### Step 2.4. Check that the integration is running

To validate the SAML SSO integration is working properly:

1. Open up an incognito browser window.
2. Navigate to your cloud organization URL.
3. Check the following:
   1. Are you prompted to sign in with your SAML identity provider?
   2. Are you able to successfully sign in?
   3. If you are signing in with an email address that matches an existing user account, do you have the appropriate permissions?

### Step 2.5. Configure provisioning rules (optional)

If you use claims in your IdP, you can leverage them as conditions in a provisioning rule so that users are automatically provisioned with the right licenses and roles when they sign in to an organization. Provisioning rules are evaluated when a user signs in. If the user account meets the conditions for a rule, it is automatically added to the local UiPath group associated with the rule. For example, an administrator can configure a rule to provision users directly into the Automation Users group using these settings: **Claim**=**group**, **Relationship**=**is**, **Value**=**Automation User**.

#### 2.5.1 Set up provisioning groups

In UiPath, adding an account to a group means the account inherits the licenses, roles, and robot configuration defined for the group, if any.

By grouping similar account types (e.g., developers or testers), you can streamline user onboarding process to the organization. Just make sure that in the IdP you set up similar accounts in the same way.

This way, you set up the group once, and then replicate the setup by adding accounts to the group when needed. If the setup for a particular group of accounts needs to change, you only need to update the group once and the changes apply for all accounts in the group.

To set up a group for a provisioning rule:

1. [Create a new local group](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-groups#creating-local-groups) in your organization. If you want, you can use one of your existing groups instead of creating a new one.
2. (Optional and requires [user license management](https://docs.uipath.com/overview-guide/docs/what-is-my-licensing-model) enabled) If accounts in this group need user licenses, [set up license allocation rules for the group](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/allocating-user-licenses#managing-license-allocation-rules). If you are using an existing group, [check license allocation for the group](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/allocating-user-licenses#viewing-existing-rules) to make sure the right licenses are being allocated. If not, either change allocations, or consider creating a new group.
3. Assign tenant roles and optionally complete robot setup for the group. For instructions, refer to [Assigning roles to a group](https://docs.uipath.com/orchestrator/v0/docs/assigning-roles#assigning-roles-to-a-group) . If you are using an existing group, [check the roles](https://docs.uipath.com/orchestrator/v0/docs/assigning-roles#checking-assigned-roles) currently assigned to the group to make sure they are adequate for the type of account you will add to the group. If not, either edit the roles assigned to this group, or consider creating a new group.
4. Add the group to folders and assign folder roles, as needed. For instructions, refer to [Managing folder access](https://docs.uipath.com/orchestrator/docs/managing-folders#managing-folder-access).

Now you can use this group in a provisioning rule.

#### 2.5.2. Create a provisioning rule for a group
:::note
Ensure the claim associated with the SAML provisioning rule is sent to the SAML payload by configuring it in the SAML application.
:::

After the SAML integration is configured and after you have set up a group:

1. Go to **Admin**, select your organization, and then select **Security**. The **Security Settings** page for the organization opens on the **Authentication Settings** tab.
2. Under the **SAML SSO** option, select **View Provisioning Rules**. The **SAML SSO Provisioning Rules** page opens, where your existing rules are listed.
3. In the top right corner of the page, select **Add rule**. The **Add new rule** page opens.
4. Under **Basic details**, fill in the **Rule Name** field and optionally fill in the **Description** field.
5. Under **Conditions**, select **Add rule**. A row of fields for a new condition is added. Together, they define the criteria that an account must meet at sign in to be added to a group (chosen later).
   !['Conditions' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30757)
6. In the **Claim** field, type the name of the claim, as it appears in the IdP. The field is case-sensitive.
7. From the **Relationship** list, select how the claim relates to the value. The following options are available, as described in the table:

   | Relationship | Condition requirement | Example |
   | --- | --- | --- |
   | **is** | exact match, case sensitive | `Department is RPA` requires that the value for the `Department` claim be `RPA`.  The condition is not met if the value is `RPADev`, for example. This relationship works for multi-valued claims. For example, if `administrator` and `developer` values are sent under the `Group` claim, then `Group is administrator` would be a valid relationship. |
   | **is not** | anything except specified value, case sensitive | For `Department is not ctr`, any account is added to the group unless `Department` has the value `ctr`.  The condition is met if the department is `Ctr` or `electr`. |
   | **contains** | includes, does not require an exact match, case sensitive | `Department contains RPA` requires that the value for the `Department` claim include `RPA`.  The condition is met if the value is `RPADev`, `xRPAx`, or `NewRPA`, for example. |
   | **not contains** | excludes, does not require an exact match, case sensitive | For `Department not contains ctr`, any account is added to the group unless the `Department` value includes `ctr`.  Accounts for which the department is `ctr` or `electr`, for example, are not added to the group. |
   | **is case insensitive** | exact match, not case sensitive | `Department is case insensitive RPA` requires that the value for the `Department` claim be `rpa`, in any capitalization.  The condition is met if the value is `rpa`, for example. The condition is not met if the value is `crpa`. |
   | **contains case insensitive** | includes, does not require an exact match, not case sensitive | `Department contains case insensitive RPA` requires that the value for the `Department` claim include `RPA`, in any capitalization.  The condition is met if the value is `rpa`, `cRPA`, or `rpA`, for example. |
8. In the **Value** field, type the value that is needed to meet the condition.
9. If you want to add another condition, select **Add rule** to add a new condition row.

When you add multiple conditions, **all** conditions must be met for the provisioning rule to apply. For example, if you define the rules `Department is RPA` and `Title is Engineer`, only users that are both in the RPA department and have the title Engineer are added to the specified groups. An account for which the department is RPA, but the title is QA is not added to the groups.
10. Under **Assign to groups**, in the **Add Groups** box, start typing the name of a group and then select a group from the list of results. Repeat to add more groups, if needed. When the conditions are met, accounts are automatically added to these groups when they login.
11. Select **Save** in the bottom right corner to add the rule.

With a rule in place, whenever a user logs in and their account meets the conditions specified for a rule, their account is added to the provisioning groups attached to the rule, and their account is set up to work in UiPath.

#### Sample SAML payload fragment

```
<Attribute 
   Name="groups"> 
<AttributeValue 
          xmlns:xs="http://www.w3.org/2001/XMLSchema"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:type="xs:string">ProcessAutomation-Developer</AttributeValue>
```

### SAML attribute mapping

When configuring the SAML directory integration, organization administrators can define which attributes from their IdP should be mapped to the system user attributes. Afterwards, when a user logs in via the SAML directory integration, the system reads the claims that are passed into the ACS payload and map the value to their correspondent system attributes. TOPLEVELNOTEMARKER
:::note
* Your IdP must be configured to pass in these claims in the ACS payload.
* Ensure the attribute names configured in the IdP match the attribute mapping settings in the organization administrator portal.
:::
For example, if this is the user structure in your IdP, an organization administrator can set up the following attribute mapping settings to have this information populated in the system user object.

```
{  
    "displayname": "John Doe",  
    "fname": "John",  
    "lname": "Doe",  
    "jobtitle": "Hardware Engineer",  
    "dpt": "Engineering",  
    "city": "Phoenix" 
}
```

!['SAML Attribute Mapping' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/495432)

When a user in this organization logs in via the SAML directory integration, their user object is updated to reflect this setting.

```
{  
    "Display Name": "John Doe",  
    "First Name": "John",  
    "Last Name": "Doe",  
    "Job Title": "Hardware Engineer",  
    "Department": "Engineering",  
    "City": "Phoenix" 
}
```

## Step 3. Transition your users to SAML SSO

Make sure you provide your organization-specific URL for the UiPath organization to all your users.
:::note
After switching to SAML integration, the Microsoft Entra ID integration is disabled. Microsoft Entra ID group assignments no longer apply, so UiPath group membership and the permissions inherited from Microsoft Entra ID are no longer respected.
:::

To sign in to UiPath with SAML SSO, users can:

* navigate to your organization-specific URL. The URL must include the organization ID and end in a forward slash, such as `<AccessURL>/orgID`.
* navigate to `<AccessURL>`, select **Continue with SSO** on the Login page, then provide their organization-specific URL.

To sign in to UiPath Studio and UiPath Assistant using SAML SSO, users must configure Assistant as follows:

1. In Assistant, open **Preferences** and select the **Orchestrator Connection** tab.
2. Select **Sign Out**.
3. For the connection type, select **Service URL**.
4. In the **Service URL** field, add the organization-specific URL.

The URL must include the organization ID and end in a forward slash, such as `<AccessURL>/orgID`. Otherwise, the connection fails saying that the user does not belong to any organization.
5. Sign back in with SAML SSO.

## Step 4. Configure permissions and robots

This is only required for new users who have not used a certain UiPath offering before and therefore did not have a local account set up for them in the specific UiPath offering when the integration was enabled.

You can add new users to UiPath groups by their email address (as used in the external IdP). Once a user has been assigned to a group or they have signed in, they will be available through search for role assignment across all UiPath services.

## Step 5. Discontinue use of local accounts (optional)

After all users have transitioned to SAML SSO and new users are set up, we recommend that you remove all local user accounts that are not administrator accounts. This ensures that users can no longer sign in with their local account credentials and they have to sign in with SAML SSO.

You can identify local user accounts based on their icons.

A local account can be useful:

* To manage SAML integration issues (e.g., updating an expired certificate) or if changing authentication settings - an account with the organization administrator role is recommended.