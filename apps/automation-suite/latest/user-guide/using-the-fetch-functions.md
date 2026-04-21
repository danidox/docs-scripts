---
title: "Using the Fetch functions"
visible: true
slug: "using-the-fetch-functions"
---

The following are two examples of how to apply the Fetch and FetchOne functions in practice.

## Using Fetch to retrieve entity records in Edit Grid controls

Use the [Fetch](https://docs.uipath.com/apps/automation-suite/latest/user-guide/custom-vb-functions#function%3A-fetch "This function is used by the Query builder. Refer to The Fetch function for more details on this function, and how to use it in practice.") function to retrieve all entity records from a Data Service entity, in conjunction with a tabular control such as **Edit Grid.**

1. Add an entity to your app:
   1. Select **Add any.**
   2. Select **Entity.**
   3. Select a tenant.
   4. Select the entity you want to add to your app, then **Add.**
2. Add an **Edit Grid** control to your app:
   1. Select **Add control.**
   2. Select **Display.**
   3. Select **Edit Grid**, and drag it to an area in your app.
3. Bind the **Edit Grid** control to your entity:
   1. In the **Properties** panel, on the **General** tab, select the **Additional resources** button adjacent to **Data source.**
   2. Select **Query builder.**
   3. Select the entity you want to use, then **Save.** The system automatically prepares a `Fetch` VB expression.
4. Preview or run your app.

When you preview your app, the **Edit Grid** control is populated with all of the records from your entity.

## Using the FetchOne VB function to retrieve an entity record and display it in a Label control

Use the [FetchOne](https://docs.uipath.com/apps/automation-suite/latest/user-guide/custom-vb-functions#function%3A-fetch-one "This function is used by the query builder, and should not be confused with the Fetch function. Refer to The Fetch function for details on the differences between these two functions, and how to use them in practice.") function to retrieve a single record from a Data Service entity and use it in display controls, such as the **Label** control, in your apps.

1. Add an entity to your app:
   1. Select **Add any.**
   2. Select **Entity.**
   3. Select a tenant.
   4. Select the entity you want to add to your app, then **Add.**
2. Add a **Label** to your app:
   1. Select **Add control.**
   2. Select **Display.**
   3. Select **Label,** and drag it to an area in your app.
3. Add a **variable** to your app:
   1. Select **Add any.**
   2. Select **Variable.**
   3. Give your variable a name.
   4. Under **Type,** select your entity, then **Save.**
4. Add a rule to the main page of your app:
   1. Select the main page of your app.
   2. In the **Properties** panel, select **Events.**
   3. Under **Loaded,** select **Create rule.**
5. Bind the rule to your variable:
   1. Select **Set value.**
   2. Under **Item to set,** select the variable you added in step 3.
   3. Select **Value**, then **Query builder.**
   4. Select your entity, then **Save.** The system automatically prepares a `Fetch` VB expression.
   5. Under **Value,** select the expression, then replace `Fetch` with `FetchOne`.
6. Bind the **Label** to the variable:
   1. Select the **Label** you added in step 2.
   2. In the **Properties** panel, select the **Open resources** button adjacent to the **Text** field.
   3. Select **Expression editor.**
   4. In the **Expression editor,** add the name of your entity followed by the name of a field in your entity. Separate the two with a period:

`Entity.Field`
7. Preview or run your app.

When you run the app, the **Label** is automatically populated with a single record from the entity field you specified.