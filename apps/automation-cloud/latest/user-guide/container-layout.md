---
title: "Container Layout"
visible: true
slug: "container-layout"
---

**Use Container Layouts** to create a complex app layout.

When a container layout control is added, a single container is available by default. To add more simple containers, click the "+" icon that border the existing containers.

To reposition a container within the layout, drag and drop the container to the desired position.

To resize containers, drag the container corner.

To delete a container, select it and use the **Delete** key on your keyboard. Alternatively, in the tree view, right-click the container and select **Delete**.

:::note
If you use the container layout as the root control in a page, when the page is opened as a pop-up, the container layout will automatically receive a minimum width of 300 pixels.
:::

![docs image](/images/apps/apps-docs-image-288218-d7c30d69.gif)

The container layout control has two sets of properties:

* One set for the container layout
* One set for every container within the layout
  :::note
  We recommend using **Container Layout** controls at a page level, for structuring the page into different sections. For aligning and positioning controls within a page, use **Container** controls.
  :::
:::important
For an easy maintenance and consistency between design time and runtime, avoid nesting container layouts.
:::

## Container Layout Properties

### General

* **Hidden** - If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

### Events

No events.

### Style

* **Background color** - The background color of the layout.
* **Font** - The font family for the container layout. All the containers within the layout share the same font family.
* **Margin**- The margin of the layout. By default, a margin of 0px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Padding** - The padding of the layout. By default, a padding of 0px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Padding** section.
* **Size** - The width and height of the layout. Be default, the **Width** is set to 100px, while the **Height** is set to `auto`, to allow the layout to expand based on the containers inside.

### VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |

## Container Properties

### General

* **Tooltip** - Tooltip to be displayed on the container. Use this to provide additional information on the control.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

### Events

* **Clicked on** - Configure what happens when the container is clicked.

### Style

* **Layout** - Determine how the controls within the container are positioned:
  + **Horizontal/Vertical** - The orientation of controls.
  + **Alignment**- The alignment of controls within the container.
  + **Allow wrapping** - If selected, wraps the controls in the container.
  + **Allow scrolling** - If selected, allows scrolling inside the container.

:::note
To enable **Allow wrapping**, the container must have a fixed height (vertical layout) or a fixed width (horizontal layout).
:::

* **Background Color** - The background color of the container.
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Font** - The font family for the container layout. All the controls within the container share the same font family. By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin**- The margin of the layout. By default, a margin of 0px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Padding** - The padding of the layout. By default, a padding of 0px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Padding** section.
* **Advanced -** Displays the flex properties of the control.
  + **Flex basis -** Sets the original size of a flex item before the extra space is distributed or taken away (`px`, `%`, `em`, `auto`).
  + **Flex grow** - When extra space is available, this values dictates how much a flex item should grow relative to the rest of the items.
  + **Flex shrink** - When the space is not enough, this value dictates how much a flex item should shrink compared to the other items. For details, refer to [Mozilla Developer Network documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/flex).