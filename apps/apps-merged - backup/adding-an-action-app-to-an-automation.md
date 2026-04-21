---
title: "Adding an action app to an automation"
visible: true
slug: "adding-an-action-app-to-an-automation"
---

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::

* You should already have an action app and deployed it to Orchestrator. If not, refer to [Adding an action to your app](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/adding-an-action-to-your-app).
* To see the list of action apps in UiPath Studio, you must be the **Co-author** for the desired app.

Add an action app to an automation in Studio as follows:

1. Go to Studio**.**
2. Select **New project.** The automation trigger selection window opens.
3. Select the **Manual automation** trigger. The automation design page opens.
4. Select the **Persistence** activities package.
5. In the search field, type **Create App Task**. Select the task to add it to your workflow.
   :::note
   Using **Create App Task,** you can pass default values to the action properties.
   :::
6. In the **Title** field, give the task a title.
7. Select an action app you deployed to Orchestrator.
   :::note
   * If your app version changed recently, select the **extra options** button in the **Apps** field, and select **Refresh** to use the most recent version of your app.
   * For an app to be available to the **Create App Task** activity, it must be an action app and it must be deployed to Orchestrator.
   * The automation should run from the same folder in which the action app was deployed. You can specify the folder name in **Create App Task.**
   :::
8. Go to **Actions** to access Action Center.
9. The **My Actions** tab shows your new automation. Select the checkbox next to it.
10. Select the additional options button, then select **Assign to self.**

The action app is ready to be used inside Action Center.