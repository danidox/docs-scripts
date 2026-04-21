---
title: "Validation Control activities"
visible: true
slug: "validation-control-activities"
---

These activities are used withting the Studio Web App Project to interact with the Validation Control at runtime.

## Set Validation Control Field Focus

Use this activity to move the user focus to a specific field inside the Validation Control UI. For example:

* When a business rule fails and you want to guide the user to fix a specific field.
* After a dropdown selection, to direct the cursor to a related field.

### Properties

* **Validation control**—Select the variable of the Validation Control that you want to interact with. This variable represents the underlying data and logic of the control, not the visual UI component itself. For example, `VarValidationControl_MainPage`.
* **Field Name**—Specify the name of the field that you want to bring into focus. It must exactly match the field name defined in your taxonomy.

### Usage example

To dynamically pass the field name a user selects from a dropdown, use this expression for the **Field Name** property:

```
string.Format("{0}", Controls.MainPage.Dropdown.SelectedItem.FieldName)
```

The dropdown field must have the data source linked to the taxonomy data, with the following expression:

```
VarValidationControl_MainPage.Taxonomy.GetFields(VarValidationControl_MainPage.SelectedDocumentType).ToListSource
```

## Save Validation Control State

Use this activity to saves the current state of the Validation Control, especially when are not expected to complete validation in one session, or when you want to persist intermediate work.

### Properties

* **Validation control**—Select the variable of the Validation Control whose state you want to save. This variable represents the underlying data and logic of the control, not the visual UI component itself. For example, `VarValidationControl_MainPage`.

### Usage example

When this activity runs:

1. The current values inside the control are saved in the background.
2. If the task is resumed or the control is reloaded with the same **ContentValidationData**, it restores the saved state.

You typically use this activity together with the **Wait for Task and Resume** activity, or as part of a multi-step validation workflow.