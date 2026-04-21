---
title: "Use tabular controls with Data Service entities in app projects"
visible: true
slug: "using-tabular-controls-with-data-service-entities-in-app-projects"
---

You can query or edit Data Service entities in tabular controls, such as the **Custom List, Dropdown, Edit Grid, Multiselect Dropdown,** and **Table** controls. Use the **Data source** property of the respective tabular control to create a workflow and bind it to your entity. Then, use events to define automations to perform other operations on your entity.

## Configuring the data source for Query Entity Records activities for all tabular controls

:::note
This procedure is applicable to all tabular controls, and uses the **Query Entity Records** activity.
:::

1. Add a tabular control, for example, **Edit Grid,** to your app:
   1. Create a new app, or open an existing one.
   2. In the left-hand side panel, select **Toolbox.**
   3. In the **Display** controls section, select **Edit Grid** and drag it into your app.
2. Configure the **Data source** of the **Edit Grid** control:
   1. In the **Properties** panel, select **Create workflow.** The project canvas opens and the system automatically adds a **Query Entity Records** activity to the workflow.
   2. In the dropdown **Entity** field, select the entity you wish to query.

:::note
If you are using the **Dropdown** control, you also need to configure the **Column** property of the control using the name of the entity field you want to display in the control.
:::

## Configuring the data source for Update Entity Record activities for Edit Grid

:::note
This procedure is applicable only to **Edit Grid,** and uses the **Update Entity Records** activity. Before beginning this procedure, make sure you completed the previous steps:
* You added an **Edit Grid** control to your app.
* You configured the **Edit Grid** data source using a **Query Entity Records** activity.
:::

1. Build an automation to update your Data Service entity:
   1. In the **Properties** panel, select **Events.**
   2. Under **Row modified,** select **Define automation.** The project canvas opens.
   3. Add an **Update Entity Record** activity from the Data Service activity package.
   4. In the dropdown **Entity** field, select the entity you want to update records for.
2. Configure the activity:
   1. In the **Record Id** field, select the **Resources** button, then **Expression editor.**
   2. Add the following expression: `MainPage.EditGrid.SelectedItem.Id`.
   3. Configure additional fields as necessary. For example, if your entity contains a field called **Name,** select the **Resources** button next to the **Name** field and add the following expression: `MainPage.EditGrid.SelectedItem.Name`.