---
title: "Checkbox"
visible: true
slug: "checkbox"
---

## General

* **Label** - The display text of the control.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Checked (Default)** - Default value of the checkbox at runtime.
* **Checkbox position** - Change the position of checkbox (left/right) with respect to the label.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Value changed** - Configure what happens when the checkbox is selected/deselected.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Color** - The color of the checkbox when it is checked.
* **Background color** - The background color of the control.
* **Font**- The font attributes, such as font family, size, color, style (Bold, Italic and Underline), or text alignment. By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin**- The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...).

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **Checkbox**. |
| `Label` | String | The label of the **Checkbox**; typically the text displayed alongside it. |
| `Value` | Boolean | Represents the state of the **Checkbox**. If set to true, the **Checkbox** is checked. |
| `Hidden` | Boolean | Determines the visiblity of the **Checkbox**. If set to true, hides the control at runtime. |
| `Disabled` | Boolean | Determines if the **Checkbox** is disabled. If set to true, disables interaction with the **Checkbox** at runtime. |
| `Required` | Boolean | Specifies if the **Checkbox** value is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the **Checkbox** value is required but was not provided. |
| `IsValid` | Boolean | Checks validity of the **Checkbox** value. If true, indicates it is valid. |