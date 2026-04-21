---
title: "Date Picker"
visible: true
slug: "date-picker"
---

## Demo

### Date Picker - date validation

#### Introduction

This app demonstrates how to create multiple date validation fields, including ones with custom error messages.

#### Demo app - try it yourself

To try the date validation fields yourself, use the demo app.

|  |
| --- |
| [Download demo app from GitHub](https://github.com/UiPath/AppsClientSample/blob/master/demo-apps/expressions/VbDateOnlyValidation.uiapp) |
| [Preview demo app in cloud](https://cloud.uipath.com/7e10edca-b5b7-4762-9e98-2ef2d8f502ab/apps_/default/run/production/2373f357-451a-4598-a85e-5067a3af53bb/6dd02387-bfa3-44ed-8998-c9f57a5e2153/IDcee6cde2d24e4b48ac6648c333aa818f/public?el=VB&origin=orchestratorFolder) |

#### Demo app - instructions to use

1. In UiPath Apps, create a new app and import the downloaded demo app.
2. You may notice some errors. To fix them, replace the referenced entities "All Data Types", "Department", "Plan", with entities in your tenant.
3. To interact with the date validation fields, preview your app.

## General

* **Hint Text** - Set the help text to be displayed at runtime.
* **Default Date** - Set a default date. If this property is bound to an app variable, changes to the default value will not propagate to the app variable.
* **Tooltip** - The text to be displayed when an app user hovers over the control. Use this to provide additional information on the control.
* **Label** - The display text of the control.
* **Required** - If true, app users must provide data in the control. To mark the control as mandatory at runtime, an asterisk `*` is added after the label text.
* **Min date** - Set the minimum date that app users can select at runtime.
* **Max date** - Set the maximum date that app users can select at runtime.
* **Custom error message** - The text to be displayed if the **Required** property is set to true and the control is left empty.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.
  :::note
  * **Date Picker** uses the `DateOnly` type. For example, you can set the **Date Picker** value to `new DateOnly(2023, 1, 25)`.
  * If you use `Date.Now()`or `DateTime.Now()` in the **Date Picker** control, you must convert this type using `System.DateOnly.FromDateTime(Now)`.
  * **Date Picker** does not support displaying or working with time values.
  :::

## Events

* **Value changed** - Configure what happens when the date is changed.

## Style

* **Control Alignment** - By default, inherits the parent alignment. A different alignment other than the parent can be set. To default back to the parent alignment, deselect the overridden options.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Label placement** - By default, the label is set to be displayed on top of the control, at the left side. You can place it to the left of the control, on the same line. The **Label Width** property configures how wide the label should be, and the **Space between** property sets the distance between the label and the control.
* **Background color** - The background color of the control. You can set a fixed color using the color picker or define a dynamic value using a VB expression.
* **Font** - The font attributes for both the label and the input text, such as font family, size, color, or style (Bold, Italic and Underline). By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin -** The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. These properties can be detached using the **Link** button at the right side of the **Margin** section.
* **Size** - The width and height of the control. By default, the size is set to `auto`. To set minimum or maximum values, click the three dot icon (...).

## Location-specific Format

To view the date in the format specific to your locale in Google Chrome, follow the steps below:

1. Go to the following address in Google Chrome: `chrome://settings/languages`.
2. Add the missing language.

   ![docs image](/images/apps/apps-docs-image-93561-b6fee1d9.webp)
3. Move the language to the top of listed languages.
4. Restart Google Chrome.
5. Re-open your app and preview it.
6. Select the date in the **Date Picker** control. The date should now be displayed in the format specific to your locale.

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `Tooltip` | String | Information text which appears when the user hovers over the **Date Picker**. |
| `Label` | String | The label of the **Date Picker**; typically the text displayed alongside it. |
| `HintText` | String | Placeholder text displayed to the user over the **Date Picker** control. |
| `MinDate` | `System.Nullable(Of System.DateOnly)` | The earliest date the user can select. |
| `MaxDate` | `System.Nullable(Of System.DateOnly)` | The latest date the user can select. |
| `Value` | `System.Nullable(Of System.DateOnly)` | The currently selected date. |
| `Required` | Boolean | Specifies if the **Date Picker** value is mandatory. |
| `RequiredErrorMessage` | String | Message displayed when the **Date Picker** value is required but was not provided. |
| `Hidden` | Boolean | Determines the visiblity of the **Date Picker** control. If true, hides the control at runtime. |
| `Disabled` | Boolean | Determines if the **Date Picker** control is interactable. If true, disables interaction with the Date Picker at runtime. |
| `IsValid` | Boolean | Checks validity of the **Date Picker** value. If true, indicates it is valid. |