---
title: "Textbox (Email)"
visible: true
slug: "textbox-email"
---

## General

* **Hint text** - The help text to be displayed at runtime.
* **Default text** - The default content to be displayed at runtime. If this property is bound to an app variable, changes to the default value will not propagate to the app variable.
  + To update values in app variables, you should use a **Set Value** rule.
* **Tooltip** - Tooltip to be displayed on the text area. Use this to provide additional information on the control.
* **Label** - The display text of the control.
* **Required** - If true, app users must provide data in the control. To mark the control as mandatory at runtime, an asterisk `*` is added after the label text.
* **Allow domain** - The domains to be allowed by the validation using the `@company.com` format. You can add several domains as an expression array. For example, to allow UiPath and Gmail domains, use `{"uipath.com", "gmail.com"}`.
* **Block domain** - The domains to be blocked by the validation using the `@company.com` format. You can add several domains as an expression array. For example, to block UiPath and Gmail domains, use `{"uipath.com", "gmail.com"}`..
* **Custom error message** - The text to be displayed if the **Required** property is set to true and the control is left empty.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Value changed** - Configure what happens when the email is changed.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Label Placement** - By default, the label is set to be displayed on top of the control, at the left side. You can place it to the left of the control, on the same line. The **Label Width** property configures how wide the label should be, and the **Space between** property sets the distance between the label and the control.
* **Background color** - The background color of the control. You can set a fixed color using the color picker or define a dynamic value using a VB expression.
* **Font** - The font attributes for the label and the input text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `AllowDomain` | List(Of String) | List of allowed email domains. |
| `BlockDomain` | List(Of String) | List of blocked email domains. |
| `PatternRegex` | String | Retrieves the regular expression (regex) provided in the **General** properties of the control. Used for validating user input. |
| `Label` | String | The label of the **Textbox Email** control, typically text displayed preceding the control. |
| `HintText` | String | Placeholder text displayed to the user over the **Textbox Email** control. |
| `Tooltip` | String | Information text which appears when the user hovers over the control. |
| `Value` | String | The currently selected value of the **Textbox** **Email** control. |
| `Required` | Boolean | Specifies if the **Textbox Email** value is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the **Textbox Email** value is required but was not provided. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables interaction with the control at runtime. |
| `IsValid` | Boolean | Checks validity of the **Textbox Email** value. If true, indicates it is valid. |