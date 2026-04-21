---
title: "Button"
visible: true
slug: "button"
---

**Button** is an interactive element that allows users to trigger actions within an App. Use the **Button** to facilitate user interactions such as submitting data, navigating between screens, or executing workflows.

## General

* **Text** - The display text of the control.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Icon** - Icon to be displayed on the button. Double-click an icon from the **Resources** list to use it.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Clicked on** - Configure what happens when the button is clicked.

## Style

* **Control alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Style** - A range of five predefined options, with different **Background color**, **Border**, and **Font** attributes. You can customize any attribute. Once customized, the style selection in the dropdown changes to **Customized**. To revert to the original style, select any of the predefined button styles.
* **Margin**- The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...).

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **Button**. |
| `Value` | String | Text displayed on the **Button**. |
| `Hidden` | Boolean | If true, hides the **Button** at runtime. |
| `Disabled` | Boolean | If true, disables interaction with the **Button** at runtime. |
| `AccessibleLabel` | String | A description of the control, used by accessibility technologies such as screen readers. |