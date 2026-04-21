---
title: "Rich Text Editor"
visible: true
slug: "rich-text-editor"
---

Use the **Rich Text Editor** control to allow users to compose rich text from your app. This text can then be used as email content, marketing content, and more.

## Design Time

### General

* **Hint text** - The help text to be displayed at runtime.
* **Default text** - The default content to be displayed at runtime. If this property is bound to an app variable, changes to the default value will not propagate to the app variable.
  + To update values in app variables, you should use a **Set Value** rule.
* **Label** - The display text of the control.
* **Required** - If true, app users must provide data in the control. To mark the control as mandatory at runtime, an asterisk `*` is added after the label text.
* **Custom error message** - The text to be displayed if the **Required** property is set to true and the control is left empty.
* **Hidden**- If true, hides the control at runtime.
* **Read only** - If true, you cannot add text at runtime, but the existing content is displayed and cannot be edited.

### Events

* **Value changed** - Configure what happens when the content is changed.

### Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Label Placement** - By default, the label is set to be displayed on top of the control, at the left side. You can place it to the left of the control, on the same line. The **Label Width** property configures how wide the label should be, and the **Space between** property sets the distance between the label and the control.
* **Font** - The font attributes for the label text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.
  :::note
  When the control alignment is set to **Stretch** and the parent control is set to **Allow wrapping**, the **Rich Text Editor** control does not stretch to the full height. To avoid this, you can remove the **Stretch** alignment or provide an explicit height for the control.
  :::

## Runtime

### Overview

Use this control to compose rich text straight from the app in runtime.

  ![docs image](/images/apps/apps-docs-image-94108-026cf2f6.webp)

:::note
If you select the **Read-only** box during runtime, the interface of the **Rich Text Editor** changes: the editing controls are hidden and you cannot add new text or edit the existing one. ![docs image](/images/apps/apps-docs-image-92236-14a8c6f9.gif)
:::

### Interface

The interface provides useful capabilities, such as:

* Font styling - Personalize the font. You can choose from the following options:
  + Bold
  + Italic
  + Underline
  + Bullet list - Create a bullet list.
  + Numbered list - Create a numbered list.
  + Table - Create a table. You can change the style of the table (size, alignment, background color, border) by selecting **Table properties** from the dropdown menu.
  + Font family
  + Font size
  + Text color
  + Text background color
* Alignment - Align the content from the **Rich Text Editor** control.
  + Align left - Align the text with a left edge.
  + Align right - Align the text with a right edge.
  + Align center - Align the text between two edges.
  + Justify - Increase the space between words to fill the entire line so that it is aligned with both the left and right edges.
* Decrease and Increase indent - Increase or decrease the space between the left and right margin of a paragraph.
* Line height - Change the space between two rows.
* Superscript and Subscript - Format the text so that it is either slightly above (superscript) or below (subscript) the normal line of type.
* Clear formatting - Remove all the formatting on a block of selected text, a paragraph, or the whole text.
* Insert/edit image - Insert an image from a Storage bucket.
* Blockquote - Indicate the quotation of a large selection of text from another source.
* Horizontal line - Insert a horizontal line.
* Insert/edit link - Insert or edit a public URL. You can also configure it to open in the same window or in a new window.
* Undo and Redo - Undo any changes or redo them if needed.

## Keyboard Shortcuts

:::important
Currently the `CTRL+C` and `CTRL+V` keyboard shortcuts do not work on Windows machines for embed or image pop-ups displayed in the **Rich Text Editor** control. Use `CTRL+SHIFT+C` and `CTRL+SHIFT+V` instead.
:::

You can use the following keyboard shortcuts to reach the control's toolbar:

| **Task** | **PC (non-macOS)** | **macOS** |
| --- | --- | --- |
| Focus or jump to menu bar | **ALT**+**F9** | **Option**+**F9** |
| Focus or jump to toolbar | **ALT**+**F10** | **Option**+**F10** |

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **Rich Text Editor**. |
| `HintText` | String | Placeholder text displayed inside the **Rich Text Editor**. |
| `Label` | String | The label of the **Rich Text Editor**, typically text displayed preceding the control. |
| `ReadOnly` | Boolean | If true, the **Rich Text Editor** is read-only at runtime. |
| `Value` | String | Currently selected value of the **Rich Text Editor**. |
| `Required` | Boolean | Specifies if the **Rich Text Editor** value is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the **Rich Text Editor** value is required but was not provided. |
| `Hidden` | Boolean | Determines the visiblity of the **Rich Text Editor**. If set to true, hides the control at runtime. |
| `Disabled` | Boolean | Determines if the **Rich Text Editor** is interactable. If set to true, disables interaction with the **Rich Text Editor** at runtime. |
| `IsValid` | Boolean | Checks validity of the **Rich Text Editor** value. If true, indicates it is valid. |