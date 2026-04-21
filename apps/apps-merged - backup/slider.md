---
title: "Slider"
visible: true
slug: "slider"
---

## General

* **Minimum value** - The lowest value of the control.
* **Maximum value** - The highest value of the control.
* **Slide increment** - The step value used to increase/decrease.
* **Default value** - The default value to be displayed at runtime.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Label -** The display text of the control.
* **Required** - If true, app users must provide data in the control. To mark the control as mandatory at runtime, an asterisk `*` is added after the label text.
* **Custom error message** - The text to be displayed if the **Required** property is set to true and the control is left empty.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Value changed** - Configure what happens when the value on the slider changes.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::

* **Label Placement** - By default, the label is set to be displayed on top of the control, at the left side. You can place it to the left of the control, on the same line. The **Label Width** property configures how wide the label should be, and the **Space between** property sets the distance between the label and the control.
* **Color** - The color of the slider line and the bubble.
* **Background color** - The background color of the control.
* **Font** - The font attributes for both the label text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...).

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **Slider**. |
| `Label` | String | The label of the **Slider**, typically text displayed preceding the control. |
| `MinValue` | Integer | The minimum value the **Slider** can have. |
| `MaxValue` | Integer | The maximum value the **Slider** can have. |
| `SlideIncrement` | Integer | The value of the increment when moving the **Slider**. If set to 10, for example, the **Slider** will increment from 10 to 20 directly. |
| `Value` | Integer | Currently selected value of the **Slider**. |
| `Required` | Boolean | Specifies if the **Slider** value is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the **Slider** value is required but was not provided. |
| `Hidden` | Boolean | Determines the visiblity of the **Slider**. If set to true, hides the control at runtime. |
| `Disabled` | Boolean | Determines if the **Slider** is interactable. If set to true, disables interaction with the Dropdown at runtime. |
| `IsValid` | Boolean | Checks validity of the **Slider** value. If true, indicates it is valid. |