---
title: "Divider"
visible: true
slug: "divider"
---

A **Divider** control is a line used to visually separate various sections in your app.

## General

* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

No events.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Style** - The thickness and color of the divider.
* **Padding** - The padding of the control. By default, a padding of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Padding** section.
* **Size** - The length of the divider. By default, it is set to `100%`.
  :::note
  By default, the divider is a horizontal line. To form a vertical **Divider**, add a container control, set the layout to horizontal, then add the divider.
  :::

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |