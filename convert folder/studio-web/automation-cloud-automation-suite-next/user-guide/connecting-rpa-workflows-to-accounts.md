---
title: "Connecting RPA workflows to your accounts"
visible: true
slug: "connecting-rpa-workflows-to-accounts"
---

Automations need to access the online applications you use in your projects. A connector is available for each supported application and service, and there can be one or more connections for each connector. Connectors and connections are managed in [UiPath Integration Service](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/introduction).

When you design RPA workflows in Studio Web, you can connect to your apps securely straight from the activities in your projects by adding new connections or selecting existing connections. Connections for your own user accounts usually reside in your personal workspace, while those for accounts that are used by multiple users are stored in shared folders.

## Selecting a connection

When you configure an activity that interacts with an online application, you must select the connection to use in that activity.

Depending on whether or not connections are already available for your user in Integration Service for the connector, one of the following may occur:

* **No connection exists** - A **Connect** button is displayed, allowing you to add a new connection. Click the button to start the authentication process and enable the required permissions. For more information, see the [Integration Service documentation](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/connectors) for the connector you want to use. When you add a new connection from Studio Web, the connection is created in your personal workspace.

  ![docs image](/images/studio-web/studio-web-docs-image-359818.webp)
* **Connections already exist** - Select a connection from the connections dropdown. Depending on the project context, either the connection that is set as the default or a connection previously used in the same project is automatically selected. Studio Web automatically checks that the current connection is valid. If you want to add a new connection, select ![](/images/studio-web/studio-web-docs-image-see-more.png) &gt; **Add new connection** next to the connections dropdown.

  ![docs image](/images/studio-web/studio-web-docs-image-359814.webp)
* **A connection is selected but is invalid** - An error message is displayed indicating that the connection has expired. To repair the connection, select **Login to connection** in the error message. This reinitiates the connection flow and, depending on the application you are connecting to, the connection is refreshed, you are prompted to re-authenticate, or configure the connection from scratch. If you want to add a new connection, select ![](/images/studio-web/studio-web-docs-image-see-more.png) &gt; **Add new connection** next to the connections dropdown.

  ![docs image](/images/studio-web/studio-web-docs-image-366308.webp)

To navigate to the Integration Service for advanced connection management, select ![](/images/studio-web/studio-web-docs-image-see-more.png) &gt; **Manage connections** next to the connection dropdown.

To view and manage the connections used in a project, open the [Data Manager](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/managing-the-data-in-a-project#managing-the-data-in-a-project).

You can view and manage the connections that are available to you from the [Automation details](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/automation-details) page in Studio Web.