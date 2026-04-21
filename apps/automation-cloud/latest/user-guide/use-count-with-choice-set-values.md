---
title: "Use Count with Choice Set values"
visible: true
slug: "use-count-with-choice-set-values"
---

You can build an app to count the values from a **Table** field that is of the type **Choice Set**.

In this example, we will use the **Count** function to get the total count of **Choice Set** values and display all possible choices in a **Table.**

## Procedure

To do this, you first need to prepare an entity with a **Choice Set** field.

1. Open an existing application or create a new one.
2. Add the entity containing the **Choice Set** field to your app:
   1. Select **Add any,** then **Entity.**
   2. Select your active tenant, then the entity containing the **Choice Set** field.
   3. Select **Add.**
3. Add two **variables** to your app, and bind them to your **entity** and **choice set:**
   1. Select **Add any,** then **Variable.**
   2. Give the variable a name. Under **Type,** open the dropdown menu, and specify the variable type as the name of the entity you added in step 2.
   3. Add another variable to your app by repeating step 3a, but specify its type as `ListSource` of `ChoiceSet`**.**
4. Add a **Table** and **Label** to your app:
   1. Select **Add control.**
   2. Select **Display.**
   3. Drag the **Table** to an area in your app.
   4. Add a **Label** to your app by repeating steps 4a and 4b.
5. Configure the **Table**:
   1. In the **Properties** panel, under **Columns,** select the **Delete Column** button. Repeat this once to leave only one column in the **Table.**
   2. Select the **Column heading** field to open its properties.
   3. Under **Name,** select **Column heading.** The **Expression editor** opens.
   4. Replace **"Column heading"** with **"DisplayName",** then select **Save.**
   5. In the **Source** field, select **Open resources,** then **Expression editor.**
   6. Add "**DisplayName",** then select **Save.**
6. Bind the **Table** and **Label** to your entity and **Choice Set**:
   1. Select the **Table**.
   2. In the **Properties** panel, select the **Additional resources** button adjacent to the **Data source** field.
   3. Select the **Expression editor,** then add the following: `GetChoiceSet("choice_set")`, where `choice_set` is the name of the **choice set** you want to use.
   4. Select the **Label.**
   5. In the **Properties** panel, select the **Text** field.
   6. Replace "**Label"** with the following: `MainPage.Table.DataSource.data.Count.ToString()`

### Result

When you preview or run the app, the total number of values in the **Choice Set** displays in the **Label** control, and the total number of choices displays in the **Table.**