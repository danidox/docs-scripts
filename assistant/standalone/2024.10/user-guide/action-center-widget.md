---
title: "Action Center Widget"
visible: true
slug: "action-center-widget"
---

The Action Center widget helps you see and complete your Action Center tasks directly from UiPath Assistant.

## Prerequisites

To use the Action Center widget, the following conditions must be met:

* UiPath Assistant connected to a tenant that has UiPath Action Center enabled.
* At least one **Pending**, **Unassigned** or **Compete** action in Action Center in the last 30 days for the Assistant to display the My Actions section.
* An Assistant Product Policy must be deployed via Automation Ops, with the Action Center enabled.
* When using the on premises version of Action Center, you must manually configure the Action Center URL in the `actionCenterUrl` parameter of the `agent-settings.json` file.
  :::note
  To find the value of the `Action_Center_URL` from the `env.json file`:
  * Navigate to the Installation Folder.
  * Go to `ActionCenter/Actions/environments/env.json`.
  * From the `PostLogoutRedirectUri` key, retrieve the correct `Action_Center_URL`.
  The format for the `PostLogoutRedirectUri` is `Action Center URL"/actions`. For example, if the `PostLogoutRedirectUri` is `https://action-center.loadbalancer.uipath.com:447/actions`, then the corresponding Action Center URL is `https://action-center.loadbalancer.uipath.com:447`.
  :::

## How to Use It

On the Launchpad, under **My Actions**, you can find the total count of your unassigned, pending, and completed actions for the last 30 days.

If you are using Assistant in a single column, your **Actions** will be displayed under **My Actions**.

Click on the total count number to go to the related category in the Action Center portal. In the Action Center portal, you can see the expanded view of your actions, and perform your tasks. You can filter actions by several criteria, and you can search for actions using the search bar in the upper left corner.