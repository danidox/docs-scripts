---
title: "Managing organization settings"
visible: true
slug: "managing-organization-settings"
---

Organization settings are broadly-applicable and impact everyone who the UiPath platform. Settings can impact all tenants, all services, and all users, except where options exist to customize more granularly.

## Accessing organization settings

If you are an organization administrator, you can access the **Admin** space, which includes the organization settings.

**To access organization settings**
* From the **App launcher** (top left corner), select **Admin**. You are then redirected to the organization settings page.
* If you are already browsing the **Admin** pages, select your organization name at the top of the panel on the left:
  !['Accessing organization settings' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/390937)

## Changing the organization name or URL

### Changing the organization name

1. Go to **Admin**, select your organization, and then select **Settings**. The **Settings** page for the organization opens.
2. In the **Organization Name** field, you can edit the name of your organization.

You can enter up to 30 characters of any type, but the last character cannot be an underscore `_`.
:::important
For Test Cloud Dedicated environments, when you change the organization name, the URL is automatically changed based on the new organization name. For more information on the behavior of the feature, refer to [Feature availability](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

### Changing the organization URL

For Test Cloud and Test Cloud Public Sector, follow these steps to change the organization URL:

1. In the **URL** field, you can modify the URL for your organization. The formatting rules for a URL are:
   * Up to 15 lowercase alphabetical or numeric characters
   * Start with a letter
   * No spaces or special characters are allowed.

     !['General tab' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/31001)
2. When you're finished editing, select **Save Changes** to apply the new name or URL..

### Changing the URL

Changing the **URL** for your organization (also known as your `Account Logical Name`) greatly impacts the entities that used the previous URL.

* Robots configured at the services level are disconnected. If you change the URL, you need to [reconnect your robots](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/connecting-robots-to-orchestrator) , entering the new URL.
* Bookmarks containing the organization URL don't work anymore. You must send the new URL to your users.
* User invites that were sent before the URL change are no longer valid. You must [send new invites](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-groups#inviting-users) for the colleagues who haven’t joined yet.
* Mobile Orchestrator users are disconnected. Send them the new URL to connect again.

### After Changing Your Site URL

The **URL** is also known as your Account Logical Name or organization-specific URL. Changing the URL greatly impacts the entities that were using the previous URL:

* Robots configured at the service level are disconnected. If you change the URL, you need to reconnect your robots, entering the new URL.
* Bookmarks containing the organization URL don't work anymore. You must share the new URL with all your users.
* Mobile Orchestrator users are disconnected. Send them the new URL to connect again.

## Changing localization settings

You can change the language either globally, with the change being propagated to all the users accessing your organization, or at a local level, for yourself only. The default language is **English**.
:::note
In some cases, you might need to refresh the page or log out and then log back in so that all elements on the page are localized.
:::

### Global language settings

You can change the language used for system emails sent by Test Cloud and other services to your users.

If a service has a different language setting for system emails, that setting takes precedence.

  !['Organization settings' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30761)

### User language settings

Each user can localize the user interface for themselves by selecting the desired language from the **Preferences** page. For details, refer to [Selecting the user language](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-user-preferences#managing-user-preferences).

For details about the supported languages across our products, refer to [Localization Support](https://docs.uipath.com/overview-guide/docs/localization-support) .

## Adding your company logo

**Before you begin**: Adding your company logo is only available for the following licensing plans:
* Unified Pricing: Application Testing Standard, Application Testing Standard Trial, Application Testing Enterprise. For details on licensing plan availability, refer to [Unified Pricing licensing plan framework](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/unified-pricing-licensing-plan-framework#unified-pricing%3A-licensing-plan-framework).

You can display your own company logo in the header:

  !['Company logo with light or dark theme' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/390949)

**To add your logo**
1. Go to **Admin**, select your organization, and then select **Settings**.

The **Settings** page for the organization opens.
2. Under **Company Logo**, select **Upload light theme logo** and select the logo image.

You can upload an image file with a size of up to 3000 x 3000 pixels. We support formats that allow for transparent pixels, such as PNG. The image is automatically resized proportionally to a maximum width of 151 pixels.
3. If your logo does not look good against a dark background, select **Upload dark theme logo** to also add an alternative image to use when users select the dark theme.
   !['Company logo settings' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30729)
4. Select **Save** to add your logo.

The appropriate logo for your current theme appears in the header.

## Finding your support ID

### Overview

The Support ID uniquely identifies your organization. You must provide this ID if you want to:

* [Contact sales](https://www.uipath.com/company/contact-us) to request an upgrade to the Enterprise plan.
* [Contact support](https://www.uipath.com/company/contact-us/cloud-platform-technical-support) for Enterprise plans. For other plans, use the [UiPath® Community Forum](https://forum.uipath.com/).

### Viewing your support ID

To view your support ID:

* Select the help icon ![](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/404023) in the header. Select the copy icon ![](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/404038) to copy your support ID.
* Go to **Admin**. The support ID is visible in the bottom left corner of the page.

## Hiding services

You can control which products and services are visible to users by hiding navigation items and homepage areas. This helps limit access to unused services and simplifies the user interface.

When a service is hidden, the navigation icon is removed for all non-administrator users. Users can still access the service by using a direct URL. Organization administrators continue to see all services.

The same configuration also controls visibility of certain homepage areas.
:::important
The UI Customization feature is only available for the following plans:
* Unified Pricing: Application Testing
Standard, Application Testing Trial, Application Testing Enterprise Pro, Pro Trial and Enterprise users.
:::

1. Go to **Admin**, select your organization, and then select **Settings**. The organization settings page opens.
2. Select the **Advanced** tab.
3. In the **UI Customization** section, review the list of available services and areas.
   !['UI customization' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/573839)

Each item indicates how visibility changes when it is hidden, such as removing the left navigation icon or removing a homepage link.
4. Select the toggle for each service or area that you want to hide or show. A confirmation dialog opens.
   :::note
   When you hide **Downloads**, the platform removes the Downloads link from both the help menu in the header and the homepage widget. Access through direct navigation is not available.
   :::
5. Confirm the change. The toggle updates to show the current state (**Shown** or **Hidden**).
6. Select **Save Changes** to apply the configuration.
   :::note
   If you hide Apps, provide users with the direct URL if they still need access. Navigation to the service is no longer available.
   :::

Hidden items are no longer visible in navigation for your users, only organization administrators can continue to view them. Shown items are visible in navigation to all users.

## Changing the license management option

User license management allows you to get more out of user licenses because one license can be used across all tenants. When this setting is disabled, user licenses are bound to the tenant to which they are allocated.

For more information about this option, refer to [User license management](https://docs.uipath.com/overview-guide/docs/license-management-options#user-license-management).

## Moving cloud organization data to a different region

To schedule data moves to a new region, contact [UiPath Support](https://www.uipath.com/company/contact-us/cloud-platform-technical-support) to request enabling this feature for your cloud organization. TOPLEVELNOTEMARKER
:::note
This feature is available only if your cloud offering supports multiple regions.
:::

### Before you begin

Review the following information before requesting a tenant region change:

#### Planning and scheduling

1. Depending on the services used by your tenant, the move may require multiple days to complete. Move date(s) are determined based on required version compatibility across regions.
2. A four-hour maintenance window is allocated for the region change. The average downtime is typically less than 30 minutes, but this can vary depending on tenant size. In rare cases, particularly for very large tenants, the move may take longer.
3. During the scheduled downtime window, the tenant is temporarily inaccessible.
4. Any running jobs are paused during the move and automatically resume after completion.
5. If you have scheduled or suspended robot jobs, temporarily disable them during the downtime window to help ensure a smooth migration.
6. Notify your cloud organization members in advance about the scheduled downtime window.

#### Scope and impact

1. Changing a tenant’s region does not affect the region of other tenants or the organization.
2. To move multiple tenants, submit and schedule region changes individually for each tenant.
3. To schedule a move for the entire organization, follow the [Performing a cloud organization data move](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-organization-settings#performing-a-cloud-organization-data-move) procedure.
4. For additional details about data behavior, see [Organization and tenant services data](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/data-residency-cloud#organization-and-tenant-services-data).

#### Data considerations

1. The **Change tenant region** wizard migrates service data only. It does not change the tenant region itself.
2. Only supported services are available for migration.
3. Services that are not supported must be recreated or manually reconfigured in the new region.
4. Some services may require additional configuration after migration.
5. Robot execution logs are retained for 30 days. Export logs in advance if you need to preserve them. For details, see [Robot logs](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-logs#classic-logs-robot-logs).
6. If your processes are integrated with UiPath Apps, you must update references after the move. See [Replacing a process](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/replacing-a-process-referenced-in-an-app) for guidance.
7. Insights can be moved to a new region. However, historical data backfilling is supported only within 30 days after moving Orchestrator. If Orchestrator is moved more than 30 days before Insights, Insights is moved without historical data, and only limited data is available after migration.

### Performing a cloud organization data move

To schedule a move for the data of your organization services to a new target region, take the following steps:

1. Go to your organization **Admin**.
2. Select **Settings** and the **Advanced** tab.
3. Under **Region**, select **Change region**.

The **Change organization region** wizard opens.

Follow the three steps in the **Change organization region** wizard to proceed: select the region, select the downtime window, and confirm the details.

   !['Change organization region wizard' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/427816)
4. Select the region

Select a target region from the **Organization target region** dropdown.

Review the services available to move.

   :::note
   Region availability and data move capabilities vary depending on the specific service. If a service you want to move is not available for scheduling, contact [UiPath Support](https://www.uipath.com/company/contact-us/cloud-platform-technical-support).
   :::

Select **Next**.
5. Select the downtime window

Select a preferred time from the **Downtime window** dropdown that has the least impact on your operations.
   :::note
   A downtime window is automatically assigned and will be used if you do not select a preferred window.
   :::

Select **Next**.
6. Confirm the details

Review the details before requesting to move the operational metadata for your organization alongside organization services.

Select **Schedule**.

The status for your organization region in **Admin**, then **Settings**, and **Advanced** tab page changes to **Region change scheduled**.

   !['Region change scheduled' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/427822)
7. Select **Region change scheduled** to display the details for your organization move.
   !['Organization migration schedule' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/427826)
8. To check the new organization region, once the service and metadata move is performed, navigate to **Admin**, then **Settings**, **Advanced**, and **Region**.

### Canceling a cloud organization data move

If you scheduled the move by mistake or need to cancel for any reason before the move of any services starts, take the following steps:

1. Navigate to **Admin**, **Settings**, **Advanced**.
2. In the **Region** section, select **Region change scheduled**.
3. Select **Cancel request**.
4. Select **Confirm**.

If you need assistance with canceling your region change, contact [UiPath Support](https://www.uipath.com/company/contact-us/cloud-platform-technical-support).

## Deleting your organization
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

Depending on your cloud offering, if you want to delete an organization, you can:

* Delete the data for a specific organization as an organization administrator.
* Reach out to [UiPath support team](https://www.uipath.com/company/contact-us/cloud-platform-technical-support) and raise a ticket to delete an organization.
:::note
Local users in Test Cloud that were members of the deleted organization are not deleted as part of this operation. Users can continue to use their accounts to log in to the UiPath Forum, Academy, or any other organizations of which they are members.
:::

### Deleting organizations

If you are an organization admin, you can delete your organization and its data. Depending on the cloud offering, take the following steps to delete an organization:

* Test Cloud
  + **Non-enterprise organizations** To delete an organization for which you have an active Community, Free, or Pro Trial license, you can delete the organization yourself by following the steps in the [Community, Free, and Pro Trial organizations](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-organization-settings#community%2C-free%2C-and-pro-trial-organizations) procedure, or by filling out the [Trust and Security](https://www.uipath.com/legal/trust-and-security/report) form to submit your deletion request.
  + **Enterprise organizations** To delete an organization for which you have an active enterprise license, you must fill out the [Trust and security](https://www.uipath.com/legal/trust-and-security/report) form to submit your deletion request.
* Test Cloud Public Sector: Fill out the [Trust and security](https://www.uipath.com/legal/trust-and-security/report) form to submit your deletion request.
* Test Cloud Dedicated: Reach out to [UiPath support team](https://www.uipath.com/company/contact-us/cloud-platform-technical-support) and raise a ticket to delete an organization.

#### Non-enterprise organizations

If you are the organization administrator for an organization on the Community, Free, or Pro Trial licensing plan, you can delete the organization yourself.

When you delete an organization, the platform first performs a soft delete. The organization, services, and data become inaccessible to all users. For seven days, you can undo the deletion, but UiPath does not guarantee full data recovery. After the seven-day grace period, the data is no longer accessible.

To delete an organization:

* Go to **Admin**, select your organization, and then select **Settings**.
* Select the **Advanced** tab.
* At the bottom of the page, select **Delete**.
* In the **Delete Organization** dialog, select a reason for deletion and then select **Continue**.
* Enter the organization name exactly as shown, including punctuation and capitalization, and then select **Delete**.

If tenant operations are still in progress, such as enabling a tenant, the deletion cannot proceed. Wait for the operation to finish and then try again.

After deletion, the organization is no longer accessible, and the platform signs you out. The organization administrator receives a confirmation email with instructions to undo the deletion within seven days, if needed.