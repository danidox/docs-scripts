---
title: "Edit Grid"
visible: true
slug: "edit-grid"
---

The **Edit Grid** control allows you to list, edit, paginate, or search tabular records.

## Demos

### Edit Grid: working with entities

#### Introduction

This app shows how to work with entities using the **Edit Grid** control.

#### Demo app - try it yourself

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/5703d81733eb42c934762af0be3ec8e50139b2e5/demo-apps/controls/edit-grid/EditGridEntity_DemoApp.zip) |
| [Preview demo app in cloud](https://cloud.uipath.com/7e10edca-b5b7-4762-9e98-2ef2d8f502ab/apps_/default/run/production/2373f357-451a-4598-a85e-5067a3af53bb/6dd02387-bfa3-44ed-8998-c9f57a5e2153/IDcf47b6a5eb4c4558b069de6f21806e2d/public) |

#### Demo app - instructions to use

1. Download the zip file with the demo app. It contains:
   * Schema.json - the schema for the entities the app uses
   * EditGridEntity_DemoApp.uiapp - the UiPath Apps file
2. In UiPath Data Service, import the Schema.json file. Make sure to import both **Entities** (Country and Employees) and **Choice Sets** (Gender and Skills).
3. Populate your entities and choice sets with data.
4. In UiPath Apps, create a new app and import the downloaded app.
5. You may notice some errors. To fix them, replace the referenced Employees entity with the one you recently imported in step 2.
6. Preview the app and interact with the data in the **Edit Grid**.

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

## Using DataTable in Edit Grid controls

Make sure you already have a DataTable object in your app.

DataTables objects can be defined as input, output, or input/output arguments of a process. To use these DataTable objects, you need to reference the process where they are used as arguments.

:::note
DataTable only supports primitives in a column. Complex type arguments in a column do not function in DataTable.
:::

Say you have a process named "Process_A", which has the DataTable objects as arguments:

|  |  |
| --- | --- |
| Input arguments | in_dt1 |
| Output arguments | out_dt1 |
| Input/Output arguments | inout_dt |

### Edit Grid

1. Navigate to the **General** tab of your **Edit Grid** control.
2. In the **Data source** field of the control, open the expression editor, and write the following expression:
   ```
   Processes.<process_name>.<datatable_output_argument>.ToListSource
   ```

For example:

   ```
   Processes.Process_A.out_dt1.ToListSource
   ```
3. To perform operations on the DataTable rows, such as adding, editing, or deleting:
   1. Make sure the **Editable**, **Add rows**, and **Delete rows** properties are set to **true**.

   ![docs image](/images/apps/apps-docs-image-371833-8aa96811.webp)
   2. Switch to the **Events** tab of the **Edit Grid** control, then configure the corresponding rules:
      1. To add rows, click **Create rule** for **Row added**, then use the **Set Value** rule:

         |  |  |
         | --- | --- |
         | Item To Set | ``` Processes.<process_name>.<datatable_output_parameter> ``` For example: ``` Processes.Process_A.out_dt1 ``` |
         | Value | ``` Processes.<process_name>.<datatable_output_parameter>.AddRow(MainPage.EditGrid.NewItem) ``` For example: ``` Processes.Process_A.out_dt1.AddRow(MainPage.EditGrid.NewItem) ``` |
      2. To delete rows, click **Create rule** for **Row deleted**, then use the **Set Value** rule:

         |  |  |
         | --- | --- |
         | Item To Set | ``` Processes.<process_name>.<datatable_output_parameter> ``` For example: ``` Processes.Process_A.out_dt1 ``` |
         | Value | ``` Processes.<process_name>.<datatable_output_parameter>.DeleteRowAt(MainPage.EditGrid.RowIndex) ``` For example: ``` Processes.Process_A.out_dt1.DeleteRowAt(MainPage.EditGrid.RowIndex) ``` |
      3. To modify rows, click **Create rule** for **Row modified**, then use the **Set Value** rule:

         |  |  |
         | --- | --- |
         | Item To Set | ``` Processes.<process_name>.<datatable_output_parameter> ``` For example: ``` Processes.Process_A.out_dt1 ``` |
         | Value | ``` Processes.<process_name>.<datatable_output_parameter>.UpdateRowAt(MainPage.EditGrid.RowIndex, MainPage.EditGrid.SelectedItem) ``` For example: ``` Processes.Process_A.out_dt1.UpdateRowAt(MainPage.EditGrid.RowIndex, MainPage.EditGrid.SelectedItem) ``` |

## Using entities with Edit Grid controls

The following example shows how to bind an entity to an **Edit Grid** control, then perform CRUD operations using the control and entity-specific rules.

The entity used is called "Employee", and has the following fields:

* Name
* Age
* Date of birth
* Gender
* Team
* Date of Joining
* IsFullTime
* Skills

### Displaying entity records

1. Create a new VB app, then add the Employee entity to the app.
2. Add the **Edit Grid** control to the app.
3. In the **Data source** field of the **Edit Grid** control, use the **Query builder** and select the Employee entity. The columns of the control are automatically populated with the fields of the entity.
4. For every column, make sure that the **Edit mode view** dropdown is set to the correct data type, as follows:

   | Option | Description |
   | --- | --- |
   | Date of Birth | Date Picker |
   | Age | Textbox |
   | Name | Texbox |
   | Gender | Dropdown |
   | Team | Dropdown |
   | Date of Joining | Date Picker |
   | IsFullTime | Checkbox |
   | Skills | Multi select |

Gender and Team are entity choices sets. When you select **Dropdown** in the **Edit mode view** for these columns, two new properties are displayed: **List Source** and **Column**.
5. To fetch the options in a choice set:
   1. In the **List source** field, use the following syntax
      ```
      GetChoiceSet("Choiceset Name")
      ```

For example, for Gender and Team columns, the **List source** field should have:

      * Gender - `GetChoiceSet("Gender")`
      * Team - `GetChoiceSet("Team")`
   2. In the **Column** field, write `"Name"`.

![docs image](/images/apps/apps-docs-image-294892-41a083b3.webp)

Skills is an entity choice set that allows multiple selection. When you select **Multi select** in the **Edit mode view** for these columns, two new properties are displayed: **List Source** and **Column**.
6. Configure the Skills column as you did for Gender and Team.
7. Go to the **Event** tab of the **Edit Grid** control.
8. For the **Row added** event, create the following rule:
   1. Add the **Create Entity Record** rule.
   2. In the **Which entity should the record be created in?**, select the Employee entity.
   3. In the **Values to set** field, update the following:
      * **Name** property - `MainPage.EditGrid.NewItem.Name`
      * **Date of Joining** property - `MainPage.EditGrid.NewItem.Dateofjoining`
      * **Age** property - `MainPage.EditGrid.NewItem.Age`
      * **Gender** property - `MainPage.EditGrid.NewItem.Gender`
      * **Team** property - `MainPage.EditGrid.NewItem.Team`
      * **IsFullTime** property - `MainPage.EditGrid.NewItem.Isfulltime`
      * **Skills** property - `MainPage.EditGrid.NewItem.Skills`
9. For the **Row modified** event, create the following rule:
   1. Add the **Update Entity Record** rule.
   2. In the **Which entity's record should be updated?**, select the Employee entity.
   3. In the **Entity record Id**, write the following expression:
      ```
      MainPage.EditGrid.SelectedItem.Id
      ```
   4. In the **Values to set** field, update the following:
      * **Name** property - `MainPage.EditGrid.SelectedItem.Name`
      * **Date of Joining** property - `MainPage.EditGrid.SelectedItem.Dateofjoining`
      * **Age** property - `MainPage.EditGrid.SelectedItem.Age`
      * **Gender** property - `MainPage.EditGrid.SelectedItem.Gender`
      * **Team** property - `MainPage.EditGrid.SelectedItem.Team`
      * **IsFullTime** property - `MainPage.EditGrid.SelectedItem.Isfulltime`
      * **Skills** property - `MainPage.EditGrid.SelectedItem.Skills`
10. For the **Row deleted** event, create the following rule:
    1. Add the **Delete Entity Record** rule.
    2. In the **Which entity record should be deleted?**, select the Employee entity.
    3. In the **Entity record Id**, write the following expression:
       ```
       MainPage.EditGrid.SelectedItem.Id
       ```
11. Preview your app and interact with the **Edit Grid** various capabilities such as pagination, search, add new row, update row, or delete rows.

### Using relationships in Edit Grid controls

To use entity fields of type Relationship in an **Edit Grid** control:

1. In the **Edit mode view** field, set the relationship fields as a **Dropdown**.
2. In the subsequent **List source** property, use the follwoing expression:
   ```
   Fetch(of <entity_name>)(Nothing, Nothing, Nothing, Nothing, New ExpansionFieldOption(){addExpansionFieldOption("CreatedBy", New String(){"Id","Name"}), addExpansionFieldOption("UpdatedBy", New String(){"Id","Name"})})
   ```
3. In the subsequent **Column** property, write `"Name"`.
4. In entity-related rules, such as **Create**, **Update**, or **Delete Entity Records**, pass the ID of the relationship field as follows:
   ```
   MainPage.EditGrid.SelectedItem.<entity_name>.Id
   ```