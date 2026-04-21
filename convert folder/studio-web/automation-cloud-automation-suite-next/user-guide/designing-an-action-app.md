---
title: "Designing an action app"
visible: true
slug: "designing-an-action-app"
---

You can add an action to your app project, allowing your app to be part of an automation which you can access from Actions.

1. Add an action to your app:
   1. Open an existing app or create a new one.
   2. Select the **Project Explorer,** then the **+** symbol.
   3. Select **Action** to add an action to your app, then **Continue.** The schema editor opens.

The schema contains a **Submit** outcome and one input property by default. To add additional properties, use the **Add property** option. To add additional outcomes, select the **+** symbol in the **Outcomes** section.

   ![docs image](/images/studio-web/studio-web-docs-image-525295.webp)
2. Map the input property to an input control:
   1. Select **Toolbox,** then **Input.**
   2. Select the **Button** control and drag it in your app.
   3. In the **Properties** panel, select **Events,** then in **Clicked on,** select **Define automation.**
   4. Add a **Submit Action** activity to your app. The outcome property automatically maps to **Submit.**
3. Publish your app:
   1. Select **Publish.** The Publish dialog opens.
   2. Enter a descriptive name for your app, then select **Publish.**
4. Deploy your app:
   1. Go to Orchestrator, and select **Automations.**
   2. Select **Apps,** then **Deploy app.**
   3. Locate the **App** field in **Source overview,** then select the app you published in the previous steps, then **Deploy.**

The action app is deployed, and you can add it to an automation.