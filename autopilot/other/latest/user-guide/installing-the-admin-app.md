---
title: "Installing the Admin App"
visible: true
slug: "installing-the-admin-app"
---

To install the Admin App:

1. Navigate to the **Apps** service in your Automation Cloud™ organization.
2. Select **Create new app**, them select **Import from file**.
3. Browse for the `Autopilot Admin App_PROD.uiapp` file on your device, select it, then select **Create**.
4. Once the app is created, replace the existing process with [the Admin App process that you deployed in Orchestrator](https://docs.uipath.com/autopilot/other/latest/user-guide/deploying-the-admin-app-process-in-your-personal-workspace):
   1. On the left-side panel, expand the **Processes** section.
   2. For the existing process, right-click and select **Replace**.
   3. Navigate to the folder where the Admin App process was deployed, and select it.
   4. Select **Replace** to return to the app.
5. In the Admin App, on the left-side panel, select **TabsPage** > **Tabs**, then activate the existing tabs by selecting them: **Custom Starter Prompts** and **Automation Properties**.
6. Connect UiPath Assistant to the same Orchestrator organization and tenant where the Admin App has been installed.
7. Test the Admin App by selecting **Preview**. This ensures there are no validation errors.
8. **Publish** the app in the selected tenant.
9. [Deploy the Admin App to a shared folder](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-apps#deploying-apps), where assigned users can access it.