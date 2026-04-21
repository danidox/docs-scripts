---
title: "Set an external context using query parameters"
visible: true
slug: "setting-an-external-context-using-query-parameters"
---

You can set an external context to your app. This is especially helpful when starting the app from within a robotic process automation (RPA) process, or if you want your app to have a particular behavior only in a certain context. You can set the external context in two ways: when debugging your app or after publishing your app.

## Test an external context while debugging an app

If you want to test how your app works with an external context, you can do this while debugging the app.

1. Enable query parameters in your app:
   1. Open a new or existing app.
   2. In the Project Explorer, select your app.
   3. In the **Properties** panel, select the **Enable query parameters** option.
2. Configure a control to reference your query parameter:
   1. Select the **Toolbox** menu.
   2. In the **Display** section**,** select **Label** and drag it into your app. The **Properties** panel opens.
   3. In the **Text** field, select the **Open resources for Text** button.
   4. Select **Expression editor.**
   5. Add `App.QueryParam("name")`, then select **Save**.
3. Debug your app and specify a query parameter:
   1. Select **Debug on cloud** or **Debug step-by-step** to begin debugging your app. The **Enter query parameter** window opens.
   2. In the **String query parameter** field, add a string, such as this placeholder: `name=john`

When you debug the app, the **Label** displays the text specified using the query parameter `name`.

## Set an external context after publishing an app

Once you deployed the app, you can set a query parameter at the end of the URL of the deployed app.

Add the query parameter after the `&uts=true` part at the end of the URL, with an additional `&` symbol, as in the following example: `&uts=true&name=john`. The behavior is the same regardless of how you add the query parameter.