---
title: "Image"
visible: true
slug: "image"
---

Supported image file types are `JPEG`, `PNG`, `BMP`, `GIF`, and `WEBP`.

## General

* **Source** - The source of the image you want to display.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Clicked On** - Configure what happens when the image is clicked.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Margin** - The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## Binding a media file

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Source` | `AppsFile` | Source file of the **Image** control. |
| `Tooltip` | String | Information text which appears when the user hovers over the **Image** control. |
| `Value` | `AppsFile` | The value attached or outputted from the **Image** control. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |