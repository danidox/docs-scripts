---
title: "Custom List"
visible: true
slug: "custom-list"
---

**Custom List** is a dynamic, template-based control, which incorporates various controls with exceptional flexibility. Far from a standard list control, the **Custom List** allows even more controls within the layout, making it ideal for tasks such as creating an effective email listing grid.

## Properties

**Custom List** has two sets of properties: one for the main control, and one for the template within it.

To toggle between the properties of a **Custom List** and its **Template**, simply click on the control in the canvas or select it from the tree view on the left.

## ThisRow

Use the `ThisRow` keyword to represent each row of the custom list data.

To bind values from the Data source to individual controls within the **Custom List**, use the `ThisRow` keyword.

## Limitations

* Due to performance considerations, several controls cannot be included within a **Custom List:**
  + **Edit Grid**
  + **Table**
  + **Custom List**
  + **Custom HTML**
  + **Tabs**
  :::note
  For list-based controls that exceed four items, we recommend using **Dropdown** controls.
  :::

* Directly referencing **Custom List** controls, such as `MainPage.Header`, is not permitted, despite the control name being found by the IntelliSense.
* Dragging controls between the context of a **Custom List** and other container controls may cause invalid expressions, some visible only when you preview the app. This is because the bindings within the context of the **Custom List** (using the `ThisRow` keyword) become invalid outside the **Custom List**.

## General

### Custom List

* **Hidden** - If set to true, hides the control during the runtime.
* **Disabled** - If set to false, app users can interact with the list. If set to true, the list is in a read-only state.

### Template

* **Tooltip** - Tooltip to be displayed on the template. Use this to provide additional information on the template.
* **Hidden**- If set to true, hides the control during the runtime.
* **Disabled** - If set to false, app users can interact with the template. If set to true, the template is in a read-only state.

## Events

### Custom List

* **Row selected** - Configure what happens when the app user selects a row (that is, a control within a template) in the **Custom List**. Configure what happens when the value is changed.

### Template

* **Clicked on** - Configure what happens when the template is clicked.

## Style

### Custom List

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Layout** - Customize the templates position within the custom list:
  + **Vertical** - templates are arranged vertically
  + **Horizontal** - templates are arranged horizontally
  + **Grid** - templates are arranged in a grid format
  + **Space between** (pixels only) - the spacing between templates, when they are arranged in a **Vertical** or **Horizontal** layout.
  + **Horizontal** / **Vertical gap** - the horizontal and vertical spacing between templates, when they are arranged in a **Grid** layout.
  + **Template Width** - the width of the template.
  + **Template Height** - the height of the template.
  :::note
  * In a **Horizontal** layout, **Width** is set in pixels and **Height** in pixels, `%`, `em`, or `auto`.
  * In a **Vertical** layout, **Height** is in pixels and **Width** can be pixels, `%`, `em`, or `auto`.
  * In a **Grid** layout, both **Height** and **Width** must be in pixels. Relative units such as `%`, `em` or `auto` cannot be used.
  :::
* **Margin** - The margin of the layout. By default, a margin of 4 px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The **Width** and **Height** of the custom list, in pixels. Default values:
  + In a **Horizontal** layout: **Width** 800 px, **Height** auto
  + In a **Vertical** layout: **Width** auto, **Height** 400 px
  + In a **Grid** layout: **Width** 800 px, **Height** 400 pxTo set minimum or maximum values, click the three dot icon (...).

### Template

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Layout** - Determine how the controls within the template are positioned:
  + **Horizontal/Vertical** - The orientation of controls.
  + **Alignment**- The alignment of controls within the template.
  + **Allow wrapping** - If selected, wraps the controls in the template.
  + **Allow scrolling** - If selected, allows scrolling inside the template. To enable **Allow Scrolling**, the template must have a fixed height (vertical layout) or fixed width (horizontal layout).
* **Background Color** - The background color of the template.
* **Border** - The border for the control. Border **Thickness**, **Color**, and **Radius** can be configured.
* **Font** - The font family for the template. All the controls within the template share the same font family. By default, the template inherits the font family of the Custom List.
* **Margin**- The margin of the layout. By default, a margin of 0 px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Padding** - The padding of the template. By default, a padding of 16 px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Padding** section.
* **Advanced -** Displays the flex properties of the control.
  + **Flex basis -** Sets the original size of a flex item before the extra space is distributed or taken away (`px`, `%`, `em`, `auto`).
  + **Flex grow** - When extra space is available, this values dictates how much a flex item should grow relative to the rest of the items.
  + **Flex shrink** - When the space is not enough, this value dictates how much a flex item should shrink compared to the other items. For details, refer to [Mozilla Developer Network documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/flex).

## VB properties

Expand Table

| Property name | Data type | Access permissions | Example |
| --- | --- | --- | --- |
| `Disabled` | Boolean | Read/Write | If true, disables the control at runtime. |
| `Hidden` | Boolean | Read/Write | If true, hides the control at runtime. |
| `SelectedItemIndex` | Integer | Read only | Returns the index of the currently selected row:  ``` MainPage.CustomList.SelectedItemIndex ``` |
| `ThisRow` | The same as the **Data Source** field. | Read only | Refers to the current record of the Data Source. Use it to configure fields within the **Custom List**. |