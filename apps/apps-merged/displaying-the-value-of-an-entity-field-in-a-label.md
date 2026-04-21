---
title: "Displaying the value of an entity field in a label"
visible: true
slug: "displaying-the-value-of-an-entity-field-in-a-label"
---

To display values of fields from an entity within labels or other display controls in your app using VB expressions, follow these steps:

1. Go to the app where you want to add this feature.
2. Click **Add any** from the dropdown arrow next to **Add control.** Select **Entity**.
   :::note
   If you already have an entity added to your app, you can skip this step.
   :::
3. Create a new **AppVariable** and assign the entity to it.
   * For holding a list of entity records, add an app variable of the type **ListSource**, then select your entity using the dropdown menu.
   * For retrieving a single entity record, add an app variable of the type &lt;Entity&gt;, where &lt;Entity&gt; is the name of your entity.
4. In the **MainPage**, go to the **Events** section in the property panel. Add a **Loaded** rule**.**
5. Add a **Set Value** rule.
6. In the **Item To Set** field**,** select your AppVariable using the lookup panel.
7. In the **Value** field**,** use the query builder to construct your query.
   :::note
   You can find more information on how to construct a query in [the Query builder page](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/the-query-builder). If you are assigning a value to an **AppVariable** of the type &lt;Entity&gt;, use the query builder [to generate the expression](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/using-autopilot-to-generate-vb-expressions). Replace any Fetch function with FetchOne instead.
   :::
8. Add a **Label** control.
9. In the **Text** field, add the following expression:
   * If the variable you created was of the type &lt;Entity&gt;, holding a single entity record, use `variableName.ColumnName.`
   * For a variable holding multiple entity records, use `variableName.data(<Index>).ColumnName`, where `variableName` is the name of your variable from which you want to retrieve data.

The app displays the value of an entity field at runtime.