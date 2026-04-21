---
title: "Adding a connection to your app"
visible: true
slug: "adding-a-connection-to-your-app"
---

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::

Connections allow UiPath Apps to integrate with external third-party services using **Integration Service**. This is similar to adding other integrations, such as Entities or Queues.

To add a connection to your app, follow these steps:

1. Before designing your app, go to **Integration Service.** The **Connectors** tab automatically opens.
2. You can either select a pre-existing connector or build a custom one using the **Build your connector** option**.**
3. Select the connector you want to add to your app.
4. To add the connection to your tenant, click the **Connect to** button.
5. In the new window, add the relevant credentials, or choose the option relevant to you. Select **Connect**.
6. Depending on the connection, you may be redirected to an external site requesting your consent to build the required permissions. Select **Allow** where relevant.
7. If the connection was successful, you should be returned to the **Connections** page in **Integration Service**. Your new connection should be visible in the table, with the **Connected** status.
8. Go to the app where you want to add a **Connection.**
9. Select **Add any** from the dropdown arrow next to **Add control.** Select **Connection.**
10. Select the tenant containing the connection you added in step 7.
11. Select the connection you wish to add to the app, then click **Add.**
12. The connection is now available in the **Connections** tab. You can immediately use the connection in your app.