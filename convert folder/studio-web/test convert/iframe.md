---
title: "IFrame"
visible: true
slug: "iframe"
---

Use the **IFrame** control to embed other application into your apps. Doing so, you can reuse various features instead of building the functionality again in Apps Studio.

:::note
Apps does not render websites with iFrames that have the response header `X-Frame-Options` to either `deny` or `sameorigin`. This restriction is ensured by the source website and there is no workaround in this case.
:::

## General

* **Source** - The source of the object you want to embed in the **IFrame** control.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

No events.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Margin** - The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Source` | String (URL) | Source URL which the app renders in the **IFrame** control. |
| `Hidden` | Boolean | If true, hides the **IFrame** control at runtime. |
| `Disabled` | Boolean | If true, disables interaction with the **IFrame** control at runtime. |