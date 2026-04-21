---
title: "Label"
visible: true
slug: "label"
---

## General

* **Text** - The display text of the control.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Clicked On** - Configure what happens when the button is clicked.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Style** - A range of six predefined options, with different **Font** attributes. You can customize any attribute. Once customized, the style selection in the dropdown changes to **Customized**. To revert to the original style, select any of the predefined header styles.
* **Background color** - The background color of the control.
* **Font** - The font attributes for the control, such as font family, size, color, alignment, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin** - The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Text` | String | Text displayed within the **Label.** |
| `Tooltip` | String | Information text which appears when the user hovers over the **Label** control. |
| `Value` | String | Value stored or extracted from the **Label**. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |