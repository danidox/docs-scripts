---
title: "Adding an action to your app"
visible: true
slug: "using-action-apps"
---

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::

* The **App creator** role allows you to create and edit action apps.
* To see the list of action apps in UiPath Apps Studio, you must be the **Co-author** for the desired app.

Add an action to your app and deploy it to Orchestrator as follows:

1. Go to the Apps homepage and select the app where you want to add an action.
2. Select **Add any** from the dropdown arrow next to **Add control**, and select **Action.**
   :::note
   You can only add one action per app.
   :::
3. A disclaimer notifies you that once you deploy the app, you must access it via Action Center. Select **Continue.** The **Action Properties** schema window opens automatically.

   ![docs image](/images/apps/apps-docs-image-439910-5f1dc163.webp)
4. To add an additional property of any type, select any **Add property** option. To add an additional outcome, select the **plus** symbol below the **Outcomes** section.
   :::note
   * The schema contains one **Submit** outcome by default and one input property by default.
   * You can edit the property name, change the property data type or make a property required. Complex data types, like objects,
   also support sub-properties.
   :::
   :::important
   Property names must adhere to the VB naming conventions.
   :::
5. You must map inputs and in/out properties to input controls in your app. If your app does not already contain an input control, add one now by selecting **Add control.**
   :::note
   * If an input or an in/out property is required, it should be mapped to an [input control](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/input-controls).
   * Outcomes should be mapped to a [**Submit Action** rule](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/rule-submit-action).
   :::
6. Add a **button** by selecting, then dragging it into your app.
7. Select the **button** to highlight it.
8. In the **Designer panel,** select **Events**.
9. Select **Create rule.** The rule configuration window opens.
10. Type **Submit action** into the search field, then select the **Submit action** rule.
11. In the **Action outcome** dropdown, select the outcome you wish to map to the **Click** event of the button, such as **Submit.**
12. Once you finished editing your app, select **Publish.** The **What's next** window opens automatically.
13. Select **Deploy now.** A new Orchestrator page opens automatically.
    :::note
    If you have multiple folders in your tenant, you can select the folder you want to deploy the app to.
    :::
14. In Orchestrator, select **Automations.**
15. Select **Apps.**
16. Select the **Deploy app** button, then select your app to deploy your app.

The app is deployed to Orchestrator and ready to be used in your automations.