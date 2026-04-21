---
title: "Table"
visible: true
slug: "table"
---

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

## VB properties

Expand Table

| VB property | Data type | Description |
| --- | --- | --- |
| `SelectedItem` | `Apps.Controls.TabularInitClass` | Currently selected item in the control. |
| `DataSource` | `Apps.Controls.ListSource(Of Apps.Controls.TabularInitClass)` | Data source for the values inside the **Table** control. |
| `Tooltip` | String | Information text which appears when the user hovers over the control. |
| `Value` | `Apps.Controls.TabularInitClass` | The currently selected value of the control. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |