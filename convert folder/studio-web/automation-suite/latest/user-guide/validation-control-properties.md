---
title: "Validation Control properties"
visible: true
slug: "validation-control-properties"
---

Validation Control properties determine how the control behaves, appears, and interacts with your document data. These properties can be set at design time in Studio Web.

## General

* **Data Source**—The main input property, of type `ContentValidationData`. It connects the control to the document data created using the **Create Document Validation Artifacts** activity. It loads extracted fields and associated metadata into the control.
* **Show document type**—Allows users to view and change the document type from a dropdown. Set it to **true** if your taxonomy includes multiple document types (such as Invoice or Purchase Order). Set it to **false** to hide the dropdown and document type.
* **Field position**—Lets you choose whether the extracted fields appear to the left or right of the document in the control.
* **Hide Fields**—Controls whether the extracted data fields are visible to the user.
* **Hidden—**If true, hides the control at runtime.
* **Disabled**—If true, makes the control read-only at runtime.

## Style

* **Control alignment**—By default, inherits the parent alignment. You can select a different alignment. To default back to the parent alignment, deselect the overridden option.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Border**—The border for the control. You can configure border **Thickness**, **Color**, and **Radius**.
* **Margin**—The margin of the control. **Top/Bottom** and **Left/Right** margin properties are grouped. To set different, separate values for **Top**, **Bottom**, **Left**, and **Right** margins, select the **Link** button at the right-hand side of the **Margin** section.
* **Size**—The **Width** and **Height** of the control. By default, the size is set to `auto`. To set minimum or maximum values, select the three dots (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## Events

Events in Validation Control let you respond to specific user actions or system triggers within your app. You can define workflows that execute when any of the following events occur:

* **On ready**—This event runs once, when the Validation Control has fully loaded. At this point, the control has:
  + Loaded the document viewer
  + Loaded the extracted data (fields and tables)
  + Loaded the taxonomyUse it to:
  + Initialize related variables
  + Display dynamic UI (for example, hide/show sections)
  + Trigger logic only after the control is fully functional
  + Run validations or format field values

* **Document type changed**—This event runs when the user selects a different document type from the dropdown in the control (if **Show Document Type** is enabled). Use it when you process multiple document types, such as Invoice and Receipt, in one app, and want to handle each differently.
* **Field selected**—This event runs when the user clicks on a field within the extracted data panel. Use it when you need to display or enable buttons or controls tied to a specific field, or to highlight the selected field location in the document.
* **Field value changed**—This event runs when the user edits, confirms, deletes, or replaces a value in any field, including table or multi-value fields. Use it when you need to recalculate dependent fields, enable/disable Submit or Save buttons, or display or enable buttons or controls tied to a specific field, or run inline business rule checks.