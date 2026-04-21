---
title: "Radio Button"
visible: true
slug: "radio-button"
---

When you have fewer items to display, you can use the **Radio Button** control instead of the **Dropdown** control. Make sure that you have unique items bound to the control.

You can use [arrays to populate the options](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/use-arrays-to-populate-dropdown-controls) of a **Radio Button** control.

## General

* **Column** - When the list source is either of type DataTable or an array of an Object, select the specific column(for DataTable data types) or the specific property (for Object arrays).
* **Hint Text** - The help text to be displayed at runtime.
* **Default Selected Value**- The default values to be displayed at runtime.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Label** - The display text of the control.
* **Required** - If true, app users must provide data in the control. To mark the control as mandatory at runtime, an asterisk `*` is added after the label text.
* **Custom error message** - The text to be displayed if the **Required** property is set to true and the control is left empty.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Value changed** - Configure what happens when the radio button value is changed.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Label Placement** - By default, the label is set to be displayed on top of the control, at the left side. You can place it to the left of the control, on the same line. The **Label Width** property configures how wide the label should be, and the **Space between** property sets the distance between the label and the control.
* **Layout** - The layout of radio button options (vertical or horizontal). By default, it is set to horizontal. The **Allow wrapping** property to wraps the radio buttons to multiple lines, and the **Space between** property sets the distance between the radio buttons options.
* **Color** - The color of the radio button when it is selected.
* **Background color** - The background color of the control.
* **Font** - The font attributes for both the label and the input text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## VB properties

Expand Table

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | `Apps.Controls.TabularInitClass` | Information text which appears when the user hovers over the **Radio Button**. |
| `Label` | String | The label of the **Radio Button**, typically text displayed preceding the control. |
| `SelectedItem` | `Apps.Controls.TabularInitClass` | Currently selected value of the **Radio Button**. |
| `DataSource` | `Apps.Controls.ListSource(Of Apps.Controls.TabularInitClass)` | Data source for the values inside the **Radio Button**. |
| `Value` | `Apps.Controls.TabularInitClass` | Currently selected value of the **Radio Button**. |
| `Required` | Boolean | Specifies if the **Radio Button** value is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the **Radio Button** value is required but was not provided. |
| `Hidden` | Boolean | Determines the visiblity of the **Radio Button**. If set to true, hides the control at runtime. |
| `Disabled` | Boolean | Determines if the **Radio Button** is interactable. If set to true, disables interaction with the **Radio Button** at runtime. |
| `IsValid` | Boolean | Checks validity of the **Radio Button** value. If true, indicates it is valid. |