---
title: "Text Area"
visible: true
slug: "text-area"
---

## General

* **Hint text** - The help text to be displayed at runtime.
* **Default text** - The default content to be displayed at runtime. If this property is bound to an app variable, changes to the default value will not propagate to the app variable.
* **Label** - The display text of the control.
* **Tooltip** - Tooltip to be displayed on the text area. Use this to provide additional information on the control.
* **Required** - If true, app users must provide data in the control. To mark the control as mandatory at runtime, an asterisk `*` is added after the label text.
* **Min length** - The minimum number of characters users need to input.
* **Max length** - The maximum number of characters users need to input.
* **Custom error message** - The text to be displayed if the **Required** property is set to true and the control is left empty.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Value changed** - Configure what happens when the text is changed.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Label Placement** - By default, the label is set to be displayed on top of the control, at the left side. You can place it to the left of the control, on the same line. The **Label Width** property configures how wide the label should be, and the **Space between** property sets the distance between the label and the control.
* **Background color** - The background color of the control.
* **Font** - The font attributes for the label and the input text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Label` | String | The label of the **Text Area** control, typically text displayed preceding the control. |
| `HintText` | String | Placeholder text displayed to the user over the **Text Area** control. |
| `Tooltip` | String | Information text which appears when the user hovers over the **Text Area** control. |
| `Value` | String | The currently selected value of the **Text Area** control. |
| `MinLength` | Integer | The minimum number of characters users must input. |
| `MaxLength` | Integer | The maximum number of characters users can input. |
| `Required` | Boolean | Specifies if the **Text Area** value is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the **Text Area** value is required but was not provided. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables interaction with the **Text Area** control at runtime. |
| `IsValid` | Boolean | Checks validity of the **Text Area** value. If true, indicates it is valid. |