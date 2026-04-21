---
title: "Textbox"
visible: true
slug: "textbox"
---

## Demos

### Textbox: discovering specific properties

#### Introduction

This app shows how to leverage the properties of a **Textbox** control.

#### Demo app - try it yourself

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/master/demo-apps/controls/textbox/Textbox_Control_Demo_App.uiapp) |
| [Preview demo app in cloud](https://cloud.uipath.com/7e10edca-b5b7-4762-9e98-2ef2d8f502ab/apps_/default/run/production/2373f357-451a-4598-a85e-5067a3af53bb/6dd02387-bfa3-44ed-8998-c9f57a5e2153/IDf24bfd467325416ba57c292f73351c84/public?el=VB&origin=orchestratorFolder) |

#### Demo app - instructions to use

1. In UiPath Apps, create a new app and import the downloaded demo app.
2. Preview the app to interact with the properties of the **Textbox** control.

## General

* **Hint text** - The help text to be displayed at runtime.
* **Default text** - The default content to be displayed at runtime. If this property is bound to an app variable, changes to the default value will not propagate to the app variable.
  + To update values in app variables, you should use a **Set Value** rule.
* **Tooltip** - Tooltip to be displayed on the text area. Use this to provide additional information on the control.
* **Label** - The display text of the control.
* **Thousands separator** - Adds a separator for numeric controls, allowing you to display large numbers in a more readable format (for example, `1,000` instead of `1000`).
* **Prefix** - Adds a currency prefix option for numeric textboxes, letting you display a static prefix (such as `$` or `USD`) to the left of the number. The prefix accepts free text of up to 3 characters.
* **Required** - If true, app users must provide data in the control. To mark the control as mandatory at runtime, an asterisk `*` is added after the label text.
* **Min length** - The minimum number of characters users need to input.
* **Max length** - The maximum number of characters users need to input.
* **Pattern (Regex)** - The Regex expression used to validate different input patterns. Use forward slashes `/ /` to wrap the Regex expression, for example `/{REGEX}/`. If an invalid Regex is provided, no validations are performed at runtime. Check the following examples for valid Regex expressions:

  | Regex expression | What is validates |
  | --- | --- |
  | `/\d/` | Text should contain digits |
  | `/^\d*$/` | Text should be only digits |
  | `/\w/` | Text should contain word characters (It always matches the ASCII characters `[A-Za-z0-9_])` |
  | `/[A-G]/` | Text should contain characters from `A` to `G` |
  | `/^C\d{7}$/` | Text should start with letter `C` followed by 7 numeric characters. |
  | `/^.{6,10}$/` | Text should be between `6` and `10` . |
  | `/[A-H0-5_@?]/` | Text contains only characters from `A` to `H`, `0` to `5`, `_`, `@`, and `?` |
  | `/^4[0-9]{12}(?:[0-9]{3})?$/` | Text is a credit card number from Visa. |
  | `/^3[47][0-9]{13}$/` | Text is a credit card number from American Express. |
  | `/^5[1-5][0-9]{14}|^(222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)[0-9]{12}$/` | Text is a credit card number from MasterCard. |
  | `/^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{4}$/` | Text is a phone number with optional country code, optional special characters and whitespace. |
  | `/^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/(\d{4})$/` | Text is a valid birthdate in the `DD/MM/YYYY` format. |
* **Custom error message** - The text to be displayed if the **Required** property is set to true and the control is left empty.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

## Events

* **Value changed** - Configure what happens when the text is changed.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Label Placement** - By default, the label is set to be displayed on top of the control, at the left side. You can place it to the left of the control, on the same line. The **Label Width** property configures how wide the label should be, and the **Space between** property sets the distance between the label and the control.
* **Background color** - The background color of the control. You can set a fixed color using the color picker or define a dynamic value using a VB expression.
* **Font** - The font attributes for the label and the input text, such as font family, size, color, or style (Bold, Italic and Underline) or text alignment. By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `AllowDomain` | List(Of String) | List of allowed domains. |
| `BlockDomain` | List(Of String) | List of blocked domains. |
| `Type` | String | - |
| `PatternRegex` | String | Retrieves the regular expression (regex) provided in the **General** properties of the control. Used for validating user input. |
| `Label` | String | The label of the **Textbox** control, typically text displayed preceding the control. |
| `HintText` | String | Placeholder text displayed to the user over the **Textbox** control. |
| `Tooltip` | String | Information text which appears when the user hovers over the control. |
| `Value` | String | The currently selected value of the **Textbox** control. |
| `MinLength` | Integer | The minimum number of characters users must input. |
| `MaxLength` | Integer | The maximum number of characters users can input. |
| `Required` | Boolean | Specifies if the **Textbox** value is mandatory. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables interaction with the control at runtime. |
| `IsValid` | Boolean | Checks validity of the **Textbox** value. If true, indicates it is valid. |