---
title: "Table"
visible: true
slug: "table"
---

## Demos

### Table: working with entities

#### Introduction

This app shows how to work with entities using the **Table** control.

#### Demo app - try it yourself

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/5703d81733eb42c934762af0be3ec8e50139b2e5/demo-apps/controls/table/TableEntity_DemoApp.zip) |
| [Preview demo app in cloud](https://cloud.uipath.com/7e10edca-b5b7-4762-9e98-2ef2d8f502ab/apps_/default/run/production/2373f357-451a-4598-a85e-5067a3af53bb/6dd02387-bfa3-44ed-8998-c9f57a5e2153/IDb5de11f1363941e997d0edb458685b17/public) |

#### Demo app - instructions to use

1. Download the zip file with the demo app. It contains:
   * Schema.json - the schema for the entities the app uses
   * TableEntity_DemoApp.uiapp - the UiPath Apps file
2. In UiPath Data Service, import the Schema.json file. Make sure to import both **Entities** (Country and Employees) and **Choice Sets** (Gender and Skills).
3. Populate your entities and choice sets with data.
4. In UiPath Apps, create a new app and import the downloaded app.
5. You may notice some errors. To fix them, replace the referenced Employees entity with the one you recently imported in step 2.
6. Preview the app and interact with the data in the **Table**.

## General

* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Columns** - The table columns you want to display in the table. Expanding each **Column heading** exposes the following column properties:
  + **Name** - The display name of the column header. Gets populated automatically.
  + **Source** - The source of the referenced column.
* **Add new column** - Add new columns to your data by clicking the plus "+" icon.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.
* **Sortable** - If selected, the table columns can be sorted.

## Events

* **Value changed** - Configure what happens when the value is changed.
  :::note
  We do not offer a **Row selected** event for the **Table** control. As an alternative, we recommend using the **Custom List** control
  :::

## Style

* **Control Alignment** - By default, it is set to **Stretch**. A different alignment can be set.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Background color** - The background color for the **Table header** and **Table body**.
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Font** - The font attributes for both the **Column header** and **Column body** text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin** - The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the **Width** is set to `auto`, and the **Height** is set to `200px`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.
  :::note
  Virtual scrolling enhances the performance by loading only the relevant items in the viewport at runtime. This only works when a height is configured and not set to **auto**. If the **Height** property is set to **auto**, the size of the control at runtime and during design time may not match. This happens because the control height depends on the number of rows returned at runtime, while in design time the control is empty. For any control with dynamic data, such as tables, dropdowns, or lists, we recommend configuring a fixed height for an improved performance.
  :::

## Keyboard Shortcuts

For improved accessibility, you can use the following keyboard shortcuts in the columns list from the **General** tab in the configuration panel:

* **Up** and **Down** arrow keys to change the selected column.
* **Alt**+**Up** arrow key to move the selected column up.
* **Alt**+**Down** arrow key to move the selected column down.

## Using DataTable in Table controls

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

### Table

1. Navigate to the **General** tab of your **Table** control.
2. In the **Data source** field of the control, open the expression editor, and write the following expression:
   ```
   Processes.<process_name>.<datatable_output_argument>.ToListSource
   ```

For example:

   ```
   Processes.Process_A.out_dt1.ToListSource
   ```

The table columns should reflect the columns of the DataTable object.

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `SelectedItem` | `Apps.Controls.TabularInitClass` | Currently selected item in the control. |
| `DataSource` | `Apps.Controls.ListSource(Of Apps.Controls.TabularInitClass)` | Data source for the values inside the **Table** control. |
| `Tooltip` | String | Information text which appears when the user hovers over the control. |
| `Value` | `Apps.Controls.TabularInitClass` | The currently selected value of the control. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |