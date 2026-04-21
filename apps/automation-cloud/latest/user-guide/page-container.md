---
title: "Page Container"
visible: true
slug: "page-container"
---

Use the **Page Container** control to add another App page within the current page.

![docs image](/images/apps/apps-docs-image-92496-77464eed.gif)

## General

* **Page** - The page to import within this control.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Clicked on** - Configure what happens when the control is clicked.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Margin**- The margin of the layout. By default, a margin of 0px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Padding** - The padding of the layout. By default, a padding of 0px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Padding** section. **Border** - Sets the border for the container. Border Thickness, Border Color, and Corner Radius can be configured for the border.
* **Margin**- The margin of the layout. By default, a margin of 0px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Padding** - The padding of the layout. By default, a padding of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Padding** section.
* **Size** - The width and height of the layout. By default, the **Width** is set to `100%` , while the **Height** is set to `auto`. To set minimum or maximum values, click the three dot icon (...).
  :::important
  Referencing the same page within the page where the **Page container** control is placed creates a circular reference and crashes the app at runtime.
  :::

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |