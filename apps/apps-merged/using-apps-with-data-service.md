---
title: "Using Apps With Data Service"
visible: true
slug: "using-apps-with-data-service"
---

## Background information

:::note
* A maximum of 1000 records for any filter are retrieved at runtime.
* After the entity data is loaded, the data is refreshed only when a rule is executed. Any changes made to the entity via processes,
or other means, do not automatically update in Apps. Make sure to explicitly refresh the data in these scenarios.
* The `in` operator only supports primitive data types, such as: `string`, `number`, `boolean`, `null`.
The `in` operator is not supported in Data Service scenarios using `choice-set`. You can use the `contains` operator instead, but only for one input.
:::

## Overview

Before starting this example, make sure that you have the proper permissions from Data Service. For more information, check the [Data Service - Managing Access](https://docs.uipath.com/data-service/automation-cloud/latest/user-guide/managing-access) page.

For the purpose of this example, we will use an entity called **Customer** with the following fields:

* Address
* Address 2
* City
* Email
* Name
* Phone
* Plan
* State
* Postal Code

## Filter Customer by State

Use the **[Function: Fetch](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/custom-vb-functions#function%3A-fetch "This function is used by the Query builder. Refer to The Fetch function for more details on this function, and how to use it in practice.")** function to retrieve multiple entity records. Additionally, use the **[Query builder](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/the-query-builder#the-query-builder "Gets the number of records for an entity, for example SystemUsers.For example, for the Edit Grid control:")** to filter the retrieved records. In this example, we apply a filter to the **Customer** entity, so the search only returns customers from the state of Washington.

Refer to [**The Fetch function**](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/the-query-builder#the-fetch-function "Gets the number of records for an entity, for example SystemUsers.For example, for the Edit Grid control:") for more details.

:::note
If you want to retrieve a single record, use the **[FetchOne](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/custom-vb-functions#function%3A-fetch-one "This function is used by the query builder, and should not be confused with the Fetch function. Refer to The Fetch function for details on the differences between these two functions, and how to use them in practice.")** function instead.
:::

1. Open an existing application, or create a new one.
2. Add a **Table** control to your app:
   1. Select **Add control.**
   2. Select **Display.**
   3. Drag the **Table** control to an area in your app**.**
3. Add an entity to your app:
   1. Select the **Add any**![docs image](/images/apps/apps-docs-image-Add_Any_icon-1117ace3.png) icon from the top of the canvas.
   2. Select **Entity**.
   3. Select a tenant.
   4. Select the entity you want to add to your app, then **Add.**
4. Bind the entity to the **Table** control:
   1. In the **General** tab of the **Properties** panel, select the **Additional resources** button adjacent to **Data source.**
   2. Select **Query builder.**
   3. Select the entity you want to use, then **Add condition.**
   4. Select a field from the dropdown menu, then an operator, such as **`=`**.
   5. Enter the string by which you want to filter the records, surrounded by quotation marks.

For example, if you only want customer records from the state of Washington, add `"WA"` as a value.
5. Use the **Expression editor** to apply a filter under specific conditions:
   1. In the **Query builder**, select the **Open resources** button, then **Expression editor.**
   2. Write an expression containing a condition. For example, you can use an IF condition to only apply a filter when a **Dropdown** control on the main page of the app is not blank and contains a user-specified value:
      ```
      Fetch(of Customer)(  
      If(  
      MainPage.Dropdown is Nothing,  
      Nothing,  
      createFilterGroup(New QueryFilter(){addFilter("State", "contains", MainPage.Dropdown.Value)}, Nothing, 0)),  
      Nothing, Nothing, Nothing, New ExpansionFieldOption( {addExpansionFieldOption("CreatedBy", New String(){"Id","Name"}), addExpansionFieldOption("UpdatedBy", New String(){"Id","Name"})})
      ```

When you preview or run the app, the query executes and retrieves the filtered records.

## Sort Customers

Use the **Query builder** to apply sorting options to your search.

1. Open an existing application, or create a new one.
2. Add a **Table** control to your app:
   1. Select **Add control.**
   2. Select **Display.**
   3. Drag the **Table** control to an area in your app**.**
3. Add an entity to your app:
   1. Select the **Add any**![docs image](/images/apps/apps-docs-image-Add_Any_icon-1117ace3.png) icon from the top of the canvas.
   2. Select **Entity**.
   3. Select a tenant.
   4. Select the entity you want to add to your app, then **Add.**
4. Bind the entity to the **Table** and apply a sorting rule:
   1. In the **General** tab of the **Properties** panel, select the **Additional resources** button adjacent to **Data source.**
   2. Select **Query builder.**
   3. Select **Additional settings.**
   4. In the **Sort by field,** add the field by which you want to sort, such as **Name**.
   5. The **Sort ascending** field is set to **true** by default. Select the field, then enter **False** to sort the results in descending order.
5. Preview or run your app. When you preview or run your app, the **Table** displays records from the **Name** field in your entity, in alphabetically descending order.

## Using entities with Edit Grid

You can use the **Edit Grid** control to display entity records in your app, and perform CRUD operations on your entity using this control.

Refer to [Using Fetch to retrieve entity records in Edit Grid controls](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/using-the-fetch-functions#using-fetch-to-retrieve-entity-records-in-edit-grid-controls) and [Using entities with Edit Grid controls](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/edit-grid#using-entities-with-edit-grid-controls) for more details and practical examples related to the **Edit Grid** control.