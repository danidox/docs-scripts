---
title: "Container"
visible: true
slug: "container"
---

A container holds controls and other containers within it and aligns them similarly.

## General

* **Tooltip** - Tooltip to be displayed on the container. Use this to provide additional information on the control.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Clicked on** - Configure what happens when the container is clicked.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Layout** - Determine how the controls within the container are positioned:
  + **Horizontal/Vertical** - The orientation of controls.
  + **Alignment**- The alignment of controls within the container.
  + **Allow wrapping** - If selected, wraps the controls in the container.
  + **Allow scrolling** - If selected, allows scrolling inside the container. To enable **Allow Scrolling**, the container must have a fixed height (vertical layout) or fixed width (horizontal layout).
  :::note
  To enable Allow wrapping, the container must have a fixed height (vertical layout) or a fixed width (horizontal layout).
  :::
* **Background Color** - The background color of the container.
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Font** - The font family for the container layout. All the controls within the container share the same font family. By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin**- The margin of the layout. By default, a margin of 0px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Padding** - The padding of the layout. By default, a padding of 0px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Padding** section.
* **Size** - The width and height of the container. By default, **Width** and **Height** are set to `auto`. To set custom values, clear the `auto` option, then enter the values of your choice and the unit of measure (`px`, `%`, `em`).

To take up the remaining available space, select the `fill` option in the dropdown. The fill option is available:
  + for **Height**, when the control layout is set to **Vertical**
  + for **Width**, when the control layout is set to **Horizontal**To set minimum and maximum sizes, click the three dots icon to expand **Min and max sizes.**
* **Advanced -** Displays the flex properties of the control.
  + **Flex basis -** Sets the original size of a flex item before the extra space is distributed or taken away (`px`, `%`, `em`, `auto`).
  + **Flex grow** - When extra space is available, this values dictates how much a flex item should grow relative to the rest of the items.
  + **Flex shrink** - When the space is not enough, this value dictates how much a flex item should shrink compared to the other items. For details, refer to [Mozilla Developer Network documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/flex).

:::important
If the container size has fixed values and if the controls within it occupy more space than the fixed value, then **Justify - Middle**, **Justify - Bottom** do not apply in a vertical orientation, and **Justify - Center**, **Justify - Right** do not apply in a horizontal orientation.
:::

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **Button**. |
| `Value` | String | Text displayed on the **Button**. |
| `Hidden` | Boolean | If true, hides the **Button** at runtime. |
| `Disabled` | Boolean | If true, disables interaction with the **Button** at runtime. |
| `AccessibleLabel` | String | A description of the control, used by accessibility technologies such as screen readers. |