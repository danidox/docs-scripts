---
title: "Layout and Styling"
visible: true
slug: "layout-and-styling"
---

## Positioning Your Controls

You can easily create a customized page layout using the Container Layout control. This way, you can group several controls to have a specific positioning, while configuring the layout and alignment of a single control (that is, the container).

To customize the controls position within a page or a container:

1. Select the page or the container where the desired control resides.
2. In the **Style** panel, select the **Layout** (**Vertical**, **Horizontal**) and the control alignment (**Left**, **Center**, **Right**, **Stretch**, **Top**, **Middle**, **Bottom**, **Distribute**).
   :::note
   By default, controls fit themselves in one line and inherit the alignment of the parent-container.
   :::
3. (Optional) For the desired control, override the inherited alignment by selecting one of the available options. To default back to the container alignment, deselect any overridden alignment.
4. (Optional) For the desired container or page, select the **Allow wrapping** option to wrap the controls to multiple lines.

## Resizing Your Controls

Controls are automatically sized by default. Auto allows the control to take the size of the content within it. For example, if the width and height of a button control are set to `auto`, the size of the button grows or shrinks based on the text in the button.

Specific height and width can also be set. **Min Width/Height** and **Max Width/Height** are available under the three dots icon (...) in the **Size** section of the **Style** panel.

The units of measurement are `%`, `px` (pixels), and `em` (relative to the font-size of the element). For example, 3em means 3 times the size of the current font.

   ![docs image](/images/apps/apps-docs-image-94499-7be3105b.gif)

To select the units of measurement, use the dropdowns of the size fields, or type in the unit. For example, to set a width of 100 pixels, type `100px` in the **Width** field.

:::note
If no units of measurement are provided, the system defaults to pixels (px).
:::

## Customizing the Font

To change the way text appears in your app, adjust the attributes in the **Font** section, such as the font family, size, color, or style.

You can switch between RGB, HEX, and HSL color formats by clicking on the arrows next to the color value.

   ![docs image](/images/apps/apps-docs-image-91355-0795c987.webp)

## Working With Borders

Use the Border property to create a border around your control. You can define the thickness and radius of the border.

The Border section can be found in the properties of all Container controls, as well as certain Input and Display controls. The Border section has three properties:

* Border thickness
* Border color
* Corner radius.

Pixels are the unit of measurement for these attributes.

  ![docs image](/images/apps/apps-docs-image-91604-fc34a50a.webp)

## Spacing Out Controls

Controls and containers can be spaced out using the attributes in the **Margin** and **Padding** sections.

Margins provide spacing around the controls.

  ![docs image](/images/apps/apps-docs-image-95456-88f2131e.gif)

Paddings provide spacing between the control and the content within it.

  ![docs image](/images/apps/apps-docs-image-92736-6a8ec829.gif)

To detach the **Top/Bottom** and **Left/Right** values and set them independently, click the **Link** button at the right of the **Margin**/**Padding** section.

:::note
You can set the margin and padding of **Container** controls, while for the majority of the controls you can only set margin.
:::

## Changing the Background Color

You can change the background color of your controls using one of the three color formats: RGB, Hex or HSL.

To change the background color of a control, use the arrows next to the color values.

  ![docs image](/images/apps/apps-docs-image-93980-2165458a.webp)