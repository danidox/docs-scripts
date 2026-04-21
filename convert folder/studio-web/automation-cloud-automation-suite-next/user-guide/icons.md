---
title: "Icon Controls"
visible: true
slug: "icons"
---

Apps in Studio Web offers a number of commonly used icons which you can add to your app.

## General

* **Tooltip** - The text to be displayed when an app user hovers over the icon. Use this to provide additional information on the control.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Clicked On** - Configure what happens when the icon is clicked.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Background color** - The background color of the icon.
* **Border** - The border for the icon. Border **Thickness** and **Color** can be configured.
* **Font** - The font attributes for the icon, such as font size and color.
* **Margin** - The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Hidden` | Boolean | If true, hides the **Icon** control at runtime. |
| `Disabled` | Boolean | If true, disables the **Icon** control at runtime. |
| `Tooltip` | String | Information text which appears when the user hovers over the control. |