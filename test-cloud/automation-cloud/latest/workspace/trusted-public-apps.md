---
title: "Trusted public apps"
visible: true
slug: "trusted-public-apps"
---

:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

The **Trusted public apps** section under **Admin** > **Security settings** > **IP restriction** allow you to keep selected [public apps](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/use-public-apps) accessible from any IP address, even when IP range restriction is enforced at the organization level.

## Overview

When **Allow only trusted IPs** is enabled, access to your organization is limited to traffic originating from trusted IP ranges that you uploaded. This restriction also applies to public apps built and deployed using UiPath Apps, which would otherwise be accessible to anyone.

From the **Trusted public apps** section administrators can explicitly allow selected Public Apps to remain publicly accessible, regardless of the IP restriction applied to the organization. All other Public Apps continue to follow the configured IP restriction rules.

Use this capability when you need to secure access to your organization while still exposing specific apps to external users.

## Before you begin

Ensure that:

* You are an Organization Administrator with permission to configure **Security Settings**.
* [IP restriction](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/restricting-access-by-ip#restricting-access-by-ip) is enabled or planned for your organization.
* You have one or more deployed public apps.
:::note
Before enforcing IP restriction, ensure that your own IP address is included in the trusted IP ranges. Otherwise, you may lock yourself out of the organization.
:::

## Adding trusted public apps

1. Go to **Admin**.
2. Ensure the organization is selected at the top of the left navigation.
3. Select **Security Settings**.
4. Open the **IP Restriction** tab.
5. In the **Trusted public apps** section, select **Add app**.
6. Select the **Tenant** where the app is deployed.
7. Select the **Public app** from the list.
8. Select **Add app**.
   ![Adding a trusted public app](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/638699)

The app is added to the **Trusted public apps** list and remains accessible from any IP address.

## Removing trusted public apps

You can remove Public Apps from the trusted list at any time.

* To remove a single app, select the **Delete** icon next to the app.
* To remove multiple apps, select them from the list and delete them in bulk.
  ![Removing trusted public apps in bulk](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/638703)

Once removed, the app becomes subject again to the organization’s IP restriction rules.