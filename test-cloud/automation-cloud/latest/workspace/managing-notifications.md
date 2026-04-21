---
title: "Managing notifications"
visible: true
slug: "managing-notifications"
---

You can manage notifications for your organization in the **Manage Notification** view from the **Notifications** settings page.

Only **Organization Admins** can manage the notifications for a user group or organization.

## Subscribing external AD group to events

Here is how to subscribe an entire external AD group to events for email notifications. Only notifications about events that impact user groups are sent to external AD groups.

**Prerequisites**: For users from the external AD group to receive email notifications, perform the following steps:
1. Access the external AD user group account in Outlook.
2. Go to **Group Settings**, and then **Edit Group**.
3. Select **Let people outside the organization email the group**.
1. In the organization **Preferences**, go to the **Notification** settings page.
2. Change the view from **My Notification** to **Manage Notification**.
3. Select **Add user group**, to add an external AD group as a notification profile.
4. Search the name of the external AD group you added inside your tenant and select it.
5. Select **Configure**.
6. Go to a service tab (**Actions**, for example), and choose the default events the external group should be subscribed to.
7. Select the checkboxes under **Email** to choose the default events the users in the external group are subscribed to.
8. After you finish the configuration, select **Save**.
   :::note
   When configuring notifications for an external [Active Directory (AD) user group](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/account-types#directory-users) of type [Security group](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/compare-groups?view=o365-worldwide), users within this group will not receive email notifications.
   :::

## Configuring default subscriptions

You can configure default notification subscriptions at the group level by setting the notification preferences for either:

* **The Default group**, which every user is associated with.
* **A local user group** defined in your organization.
  :::important
  Although users and user groups (including those provisioned through external Active Directory (AD) or Azure Active Directory (AAD)) are defined at the **organization level**, notification subscriptions are configured and applied at the **tenant level**. This means the same user or group can have different notification subscriptions in different tenants. For details, see [About notifications](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-notifications#about-notifications).
  :::

The Default group is not an actual user group. It acts as a system-wide template that defines baseline notification settings for users who have not configured their own preferences within the curent tenant.

You configure default subscriptions for user groups in: **Organization Preferences > Notifications > Manage Notification view > Alerting Group Configuration** tab.

From there, you can:

* Edit the **Default group**
* Add a **local user group** and configure its notification preferences

You can configure default subscriptions only for user groups available in **Administration > Accounts and local groups**.

**How default subscriptions work**:

The following rules determine how default subscriptions are applied within a tenant:

* The **Default group acts as the baseline** for all users in that tenant.
* If a user has not customized their notification preferences, the Default group settings apply in that tenant.
* If a user has customized their notification preferences, their personal settings apply, except for mandatory subscriptions.
* If a local user group does not have default notification subscriptions configured in **Alerting Group Configuration**, the Default group settings apply to that group in the current tenant.
* Mandatory subscriptions configured in the Default group cannot be changed by users. Only organization administrators can modify them. These rules apply to all users, including users provisioned through external Active Directory (AD) groups.

**To configure default notifications**:
1. In the organization **Preferences**, go to the Notification settings page.
2. Change the view from **My Notification** to **Manage Notification**.
3. Select the **Alerting Group Configuration** tab.
4. Choose one of the following:
   * To edit the Default group, select **Edit**.
   * To configure a new user group:
     1. Select **Add user group**.
     2. Select the desired group.
     3. Select **Configure**.
5. Open each service tab (**Actions**, for example).
6. Select the default events users should be subscribed to.
7. Optionally configure event visibility: Select the visibility icon next to an event to hide or unhide it.
8. Configure subscription behavior:
   1. Select the checkboxes under **Mandatory** to enforce subscriptions that users cannot change.
   2. Select the checkboxes under **Automation Cloud** and **Email** to define default delivery channels.

### Tips

* Users are **not required** to belong to a user group.

When a notification is sent directly to a user:

* If the user has customized preferences, **their personal settings apply** in that tenant.
* If the user has not customized preferences, **the Default group settings apply** in that tenant.
* Mandatory settings always override personal preferences.

If a user belongs to multiple user groups, their effective subscription is the combined set (union) of:

* All assigned group subscriptions in that tenant
* Their personal preferences in that tenant

## Customizing email notifications for your organization

As an administrator, take the following steps to personalize the appearance of email notifications for your organization.

1. In the organization's **Preferences**, go to the **Notification Settings** page.
2. Switch the view from **My Notification** to **Manage Notification**.
3. Go to the **Email Configuration** tab where you can customize an email template to align with your organization's needs.
4. Select **Apply at account level** to apply the changes as well to the notifications sent for the portal.
5. Under **Sender Logo** you can customize the email logo using the following options:
   1. Select **Replace Image** to upload a logo that's specific to your organization.

You can upload `PNG` images of up to 40KB.
   2. Select the download icon to download the current logo image.
   3. Select the delete icon to delete the current logo, and remove it from the email notifications.
6. Under **Sender Name**, enter the name that you want to appear as the sender of the email notifications.
7. Under **Sender ID**, enter the email address you want to show as the sender of the email notification.
8. Under **Email digest frequency**, choose the frequency at which your organization receives summary emails that show multiple notifications.
   :::note
   Email digest is available only for Orchestrator.
   :::

Email digest triggers when users in your organization subscribe to events.

Select one of the following options:

   1. **10 minutes**
   2. **30 minutes**
   3. **Once a day** - sent every 24 hours based on the timezone in which our service is running.
   4. **Twice a day** - sent every 12 hours based on the timezone in which our service is running.
9. Select **Save** to apply the customizations.

## Customizing Slack notifications

As an administrator, take the following steps to configure the Slack notifications for your organization:

1. In the organization's **Preferences**, go to the **Notification Settings** page.
2. Switch the view from **My Notification** to **Manage Notifications**.
3. 
   :::note
   Using Slack for notifications consumes purchased API units.
      :::
Go to the **Slack Configuration** tab where you can customize the Slack connection to align with your organization's needs.
4. Toggle the **Enable Slack notifications**. Select **Enable** in the displayed pop-up.
5. Select **Add connection**.

You are redirected to the **Connect to Slack** page. Your organization is then connected to Slack, allowing Notification Service to interact with the Slack data on your behalf.
6. Select **Connect**.
7. Choose the Slack connection from the drop-down list. You specify the connection on which you want to receive notifications on.
8. Select the Slack channel that Notification Service uses to send you notifications for a particular product, by following these steps:
   1. Go to **Alerting Group Configuration** > **Default** > **Edit**.
   2. Select the tab for the product for which you want to configure the Slack channel.
   3. Select on the Slack settings icon !['Slack' icon](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/443460) from the Slack column.
   4. In the pop-up, select the Slack channel, from the drop-down list.
9. Optionally check the **Apply Slack settings to the entire organization** box to override existing organization Slack settings. Select **Save**.

## Viewing all organization notifications

You can view all the notifications that your organization received in the **Notifications** page. The **Notifications** page allows you to filter notifications, based on the service they notify you about, their severity, and the time when you received them.

To explore your organization's notifications:

1. Open the **Notifications panel**.
2. In the top-right, select the **Notifications page**!['Notifications page icon' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/311087) icon.

### Filtering your organization's notifications

1. Navigate to the **Notifications** page.
2. Search for a keyword inside the **Search** bar.
3. Select **Service** and filter notifications based on the service they notify about.
4. Select **Severity** and filter notifications based on their severity.
5. Select **Timestamp** and filter notifications based on the time they were sent.

### Viewing only unread notifications

1. Navigate to the **Notifications** page.
2. Select **Unread only** in the top-right.

### Unsubscribing from tenant or event

From the **Notifications** page you can unsubscribe from the event or tenant that a notification was received.

1. Hover over a notification.
2. Select **Show more actions**.
3. Choose to unsubscribe from:
   1. The event that you're notified about.
   2. The tenant where the event took place.

### Deleting notifications

To delete notifications select **Show more actions**![](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/311157) and then **Delete**.

## Receiving notifications per folder
:::note
This option is only available for Orchestrator notifications.
:::

You can use the **Receive notifications for folders** drop-down list to select the folders or subfolders for which you would like to be alerted.

In addition to that, you can select the **Include folders that I get added to later** option to make sure that, if you are added to a folder, you do not miss any notifications pertaining to it.