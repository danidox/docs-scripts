---
title: "My notifications"
visible: true
slug: "my-notifications"
---

You can manage your notifications using the **My Notification** view from the **Notifications** settings page. For details, refer to [Notification settings](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/exploring-the-user-interface#notifications-panel).

## Events

Events serve as triggers for notifications. The action events that generate notifications are:

* **App Shared** - an app has been shared
* **App Duplicated** - an app has been duplicated successfully
* **App Duplicated Failed** - duplicating an app has failed
* **App migrated** - an app has been migrated from the legacy expression language to VB expressions
* **App migration failed** - migrating an app to the VB expression language has failed

### Severity

You can also subscribe to app events based on their severity, such as **Success** or **Error**.

## Viewing and accessing notifications

You can access notifications through the **Notifications** panel only.

To access the **Notifications** panel, go to the top navigation bar and select the bell ![Bell icon](/images/apps/apps-bell-icon-bell_icon_notifications_panel-01b4ec1a.png) icon. The **Notifications** panel displays notifications ordered by date, in descending order. The **Notifications** panel displays notifications from newest to oldest.

To access a specific notification, select the desired notification frame.

### Filtering notifications

While you're in the **Notifications** panel, you can further filter the notifications, so you can view certain notifications first. To filter the notifications that you receive in the **Notifications** panel:

1. Open the **Notifications** panel.
2. Select the **Service** dropdown and then select the service for which you want to view notifications.
3. Select the **Severity** dropdown and then select the severity of the notifications that you want to view.

## Displaying only unread notifications

To display unread notifications, select the **Unread only** checkbox in the **Notifications** panel.

## Marking all notifications as read

To mark all notifications as read:

* In the **Notifications** panel, select **More Action on All Notifications** at the bottom of the **Notifications panel** and then select **Mark all as read**.

## Clearing all notifications

To clear all notifications from the Notifications panel:

* In the **Notifications panel**, select **More Action on All Notifications** at the bottom of the **Notifications panel** and then select **Clear all**.

## Deleting notifications

You can delete notifications individually. To delete a notification:

1. Go to a notification from the **Notifications** panel and select **Action on Notification**!['Action on notification' image](/images/apps/apps-action-on-notification-image-vertical_ellipsis_notifications_panel_icon-57ccbf15.png).
2. Select **Delete**.

Selecting **Delete** permanently deletes a notification.

## Subscribing to events

You can subscribe to certain events to receive notifications about them. Subscribe to events in the **Notifications** settings page. Visit [Notification settings](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/exploring-the-user-interface#notifications-settings-page) to learn more.

:::note
The **Automation Cloud** column is visible for services with in-app notifications enabled. The **Email** column is visible for services with email notifications enabled.
:::
**Subscribing to an event:**
1. Go to the **Notifications** settings page.
2. Go to a service tab and then go to the **Automation Cloud** or **Email** column.
3. Select the checkbox that is inline with the event that you want to subscribe to.

If you want to receive both in-app and email notifications on an event, then select both checkboxes under **Automation Cloud** and **Email** column.

**Subscribing to all events:**
1. Go to the **Notifications** settings page.
2. Go to a service tab and then go to the **Automation Cloud** or **Email** column.
3. Select the **Automation Cloud** or **Email** checkbox to subscribe to notifications on all events.

## Unsubscribing from events

To stop receiving notifications, you can unsubscribe from certain events. You can unsubscribe from events from the **Notifications** panel or from the **Notifications** settings page.

:::note
The **Automation Cloud** column is visible for services with in-app notifications enabled. The **Email** column is visible for services with email notifications enabled.
:::
**Unsubscribing from the Notifications panel**:
1. Access the **Notifications** panel.
2. Go to a notification and select the **Action on Notification**![docs image](/images/apps/apps-action-on-notification-image-vertical_ellipsis_notifications_panel_icon-57ccbf15.png) menu.
3. Select **Unsubscribe from &lt;event&gt;.**

**Unsubscribing from the Notification settings page**:
1. Go to the **Notification** settings page.
2. Go to a service tab and then go to the **Automation Cloud** column.
3. Deselect the checkbox that is inline with the event that you want to unsubscribe from. If you want to unsubscribe from both in-app and email notifications for an event, then deselect both checkboxes under **Automation Cloud** and **Email**.

**Unsubscribing from all events**
1. Go to the **Notifications** settings page.
2. Go to a service tab and then go to the **AutomationCloud** or **Email** column.
3. Deselect the **Automation Cloud** or **Email** checkbox to unsubscribe from notifications about all events.
   :::warning
   Unsubscribing from all the events of a service, via both **Automation Cloud** and **Email**, generates the following warning: "You’re not subscribed to receive any notifications from this service."
   :::

The **Restore default subscriptions** option restores the default subscriptions for notifications received both on **Automation Cloud** and **Email**.