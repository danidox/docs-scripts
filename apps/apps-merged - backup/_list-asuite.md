---
title: "List"
visible: true
slug: "list"
---

## General

* **List Source** - The source for the items to be displayed in the list. Valid data types are Data Table and Object Array. Once you fetch the data source, the table automatically detects the data columns.
* **Column** - When the list source is either of type DataTable or an array of an Object, select the specific column (for DataTable data types) or the specific property (for Object arrays).
* **Default Selected Value**- The default value to be displayed at runtime.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Value changed** - Configure what happens when the value is changed.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Background color** - The background color of the control.
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Font** - The font attributes for the control, such as font family, size, or color. By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin** - The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `180x200px`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.
  :::note
  Virtual scrolling enhances the performance by loading only the relevant items in the viewport at runtime. This only works when a height is configured and not set to **auto**. If the **Height** property is set to **auto**, the size of the control at runtime and during design time may not match. This happens because the control height depends on the number of rows returned at runtime, while in design time the control is empty. For any control with dynamic data, such as tables, dropdowns, or lists, we recommend configuring a fixed height for an improved performance.
  :::

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **List** control. |
| `Value` | `Apps.Controls.TabularInitClass` | The currently selected value within the **List.** |
| `SelectedItem` | `Apps.Controls.TabularInitClass` | Currently selected item in the **List** control. |
| `DataSource` | `Apps.Controls.ListSource(Of Apps.Controls.TabularInitClass)` | Data source for the values inside the **List**. |
| `Required` | Boolean | Specifies if a **List** selection is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the **List** selection is required but was not provided. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |