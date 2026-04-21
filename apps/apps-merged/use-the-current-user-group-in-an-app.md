---
title: "Use the current user group in an app"
visible: true
slug: "use-the-current-user-group-in-an-app"
---

You can use events to display different content in your app based on whether or not the user is in a specified group. This example demonstrates showing different messages to the user based on whether or not they are in a particular group.

1. Open an existing app, or create a new one.
2. Add a **Button** control to your app, and associate a rule with it:
   1. Select **Add control** to your app, then **Input.**
   2. Select the **Button** and drag it to an area in your app.
   3. In the **Properties** panel, select **Events.**
   4. Under **Clicked on**, select **Edit rule.**
   5. Select **Add a new rule.**
3. Configure the rule:
   1. Select **If-Then-Else.**
   2. Select the **If** field, and add the following expression: `CurrentUser.Groups.where(function(x)x.Contains("Group3")).Count >0`.
   3. Under **Then,** select **Show message.**
   4. In the **Type** dropdown, select **Success.**
   5. Under **Else,** select **Show message.**
   6. In the **Type** dropdown, select **Warning.**
4. Save your app.

When you run the app and select the button, the system displays a success message if the user is part of Group3. The system displays a warning message if the user is not part of the specified group.