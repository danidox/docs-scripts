---
title: "Edit Grid"
visible: true
slug: "edit-grid"
---

The **Edit Grid** control allows you to list, edit, paginate, or search tabular records.

## Demo: Edit Grid

Download the [Apps_Tables_Cheatsheet.zip](https://github.com/UiPath/AppsClientSample/blob/master/demo-apps/controls/edit-grid/Apps_Tables_Cheatsheet.zip) demo app and import it into UiPath Studio Web to see an example of how the Edit Grid control can be used to build a Table cheatsheet for displaying and updating data.

## General

* **Add new column** - Add new columns to your data by clicking the plus "+" icon.
* **Hidden** - If true, hides the control at runtime.
* **Editable** - If false, marks the control as read-only.
* **Add rows** - If true, allows app users to add new rows at runtime. If false, users cannot add new rows.
* **Delete rows** - If true, allows app users to delete rows. If false, users cannot delete rows.
* **Search** - If true, exposes a built-in search capability.
  :::note
  The **Date Picker** in the **Edit Grid** does not support editing column types which contain time values. Configure the column in your **Data Service** entity using the **Exclude time** option to avoid errors in your data. If you need to include a time column, set the **Edit mode view** option of the column to the **Textbox** type.
  :::

## Events

* **Row selected** - Configure what happens when a row is selected.
* **Row added** - Configure what happens when a row is added.
* **Row modified** - Configure what happens when a row is modified.
* **Row deleted** - Configure what happens when a row is deleted.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Background color** - The background color for the **Grid header** and **Grid body**.
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Font** - The font attributes for both the **Column header** and **Column body** text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin** - The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## VB properties

Expand Table

| VB property | Data type | Description |
| --- | --- | --- |
| `SelectedItem` | `Apps.Controls.TabularInitClass` | References the currently selected item in the control. |
| `DataSource` | `Apps.Controls.ListSource(Of Apps.Controls.TabularInitClass)` | References the data source for the values inside the Table control. |
| `NewItem` | `Apps.Controls.TabularInitClass` | References the item being created by the **Add row** option. The **Row added** event references this property. |
| `Editable` | Boolean | Determines if the **Edit Grid** is editable. |
| `AddRows` | Boolean | Determines if rows can be added to the **Edit Grid.** |
| `DeleteRows` | Boolean | Determines if rows can be deleted from the **Edit Grid.** |
| `RowIndex` | Integer | References the index of the row for update and delete operations. Should be used for process integration where there entire dataset is in-memory. |
| `Search` | Boolean | Enables or disables the search function. If true, search is enabled. |
| `Value` | `Apps.Controls.TabularInitClass` | The currently selected value of the control. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |

## Converting complex data to AppsDataSource

To convert a data table or a complex data type to a AppsDataSource: save the data table to a variable, then use the `.ToListSource` method that converts data from data table to AppsDataSource.

1. Save the data to a variable of type DataTable. For example, name the variable "dt".
2. In the **Data source** field of table controls, use the following expression:
   ```
   dt.ToListSource()
   ```

Generically, complex objects can be converted to AppsDataSource by using the syntax:

```
Processes.ALLDATATYPES.out_datatable.ToListSource()
```

## Using entities with Table and Edit Grid controls

Check out [Use tabular controls with Data Service entities in app projects](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/using-tabular-controls-with-data-service-entities-in-app-projects "You can query or edit Data Service entities in tabular controls, such as the Custom List, Dropdown, Edit Grid, Multiselect Dropdown, and Table controls. Use the Data source property of the respective tabular control to create a workflow and bind it to your entity. Then, use events to define automations to perform other operations on your entity.") for more information on how to use entities with Table and Edit Grid controls.

:::note
* Formatting dates is not supported using **Table** and **Edit grid** controls. When using date columns, the **DateTime** type is displayed without additional formatting (shown as raw values). In contrast, **DateOnly** type columns are automatically formatted based on the user’s browser locale and language settings.
* When working with entities, it is recommended to use the **Create Workflow** option to enable pagination. Using an Entity App variable as **Data source** is not advised, as it creates a local copy of the data and does not support pagination from Data Fabric.
:::