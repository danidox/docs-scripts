---
title: "Dropdown"
visible: true
slug: "dropdown"
---

## General

* **Column** - When the list source is either of type DataTable or an array of an Object, select the specific column (for DataTable data types) or the specific property (for Object arrays).
* **Hint Text** - The help text to be displayed at runtime.
* **Default Selected Value**- The default value to be displayed at runtime.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Label** - The display text of the control.
* **Required** - If true, app users must provide data in the control. To mark the control as mandatory at runtime, an asterisk `*` is added after the label text.
* **Custom error message** - The text to be displayed if the **Required** property is set to true and the control is left empty.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.
  :::note
  You can use [arrays to populate the options](https://docs.uipath.com/apps/automation-suite/latest/user-guide/use-arrays-to-populate-dropdown-controls) of a **Dropdown** control.
  :::

## Events

* **Value changed** - Configure what happens when the value in the dropdown is changed.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Label Placement** - By default, the label is set to be displayed on top of the control, at the left side. You can place it to the left of the control, on the same line. The **Label Width** property configures how wide the label should be, and the **Space between** property sets the distance between the label and the control.
* **Background color** - The background color of the control.
* **Font** - The font attributes for both the label and the input text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...).

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **Dropdown**. |
| `Label` | String | The label of the **Dropdown** input field, text displayed preceding the control. |
| `HintText` | String | Placeholder text displayed to the user over the **Dropdown** control. |
| `SelectedItem` | `Apps.Controls.TabularInitClass` | Currently selected item in the **Dropdown** control. |
| `DataSource` | `Apps.Controls.ListSource(Of Apps.Controls.TabularInitClass)` | Data source for the values inside the **Dropdown** control. |
| `Value` | `Apps.Controls.TabularInitClass` | The currently selected value of the **Dropdown**. |
| `Required` | Boolean | Specifies if the **Dropdown** value is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the **Dropdown** value is required but was not provided. |
| `Hidden` | Boolean | Determines the visiblity of the **Dropdown** control. If set to true, hides the control at runtime. |
| `Disabled` | Boolean | Determines if the **Dropdown** control is interactable. If set to true, disables interaction with the **Dropdown** at runtime. |
| `IsValid` | Boolean | Checks validity of the **Dropdown** value. If true, indicates it is valid. |