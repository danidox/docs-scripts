---
title: "Check the current user group"
visible: true
slug: "check-the-current-user-group"
---

You can use controls in your app to check the group to which the current user belongs.

1. Open an existing app, or create a new one.
2. Select **Add control** to add a new control to your app, then **Input.**
3. Select the **Dropdown** and drag it to an area in your app.
4. In the **Properties** panel, select **Data source,** then **Expression editor.**
5. Add the following expression: `CurrentUser.Groups.ToListSource`
6. Select **Save.**