---
title: "Switch"
visible: true
slug: "switch"
---

## General

* **Label -** The display text of the control.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **On (default)** - The default position of the switch at runtime.
* **Label position** - The position of the label (left/right) with respect to switch.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Value changed** - Configure what happens when the switch is toggled.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::

* **Color** - The color of the switch control when it is turned on.
* **Background color** - The background color of the control.
* **Font** - The font attributes for both the label text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...).

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **Switch**. |
| `Value` | String | Text displayed on the **Switch** control. |
| `Label` | String | The label of the **Switch**, typically text displayed preceding the control. |
| `Hidden` | Boolean | If true, hides the **Switch** control at runtime. |
| `Disabled` | Boolean | If true, disables interaction with the **Switch** control at runtime. |