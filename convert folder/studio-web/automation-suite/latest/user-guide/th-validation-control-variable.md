---
title: "The Validation Control variable"
visible: true
slug: "th-validation-control-variable"
---

Each Validation Control automatically creates a variable inside the app. This variable holds the document data and you can use it in other parts of your app or automation.

The variable name follows the syntax `Var<ValidationControlName>_<PageName>`, for example `VarValidationControl_MainPage`.

The Validation Control variable allows both reading from and writing to the Validation Control.

Apps automatically manages this variable:

* Creates the variable when you add the Validation Control onto the canvas.
* Renames the variable when you rename the control.
* Deletes the variable when you remove the control.
* Prevents you from manually deleting or modifying this variable, since it is protected.
* Provides usage across different app pages, as the variable is app-scoped.

## Variable properties

The Validation Control variable includes several properties you can reference or bind:

* `Taxonomy`—Holds document schema, field definitions, and labels.
* `ExtractionResult`—Contains extracted field values, raw and validated.
* `SelectedDocumentType`—The active document type shown in the control.
* `SelectedField`—The field currently selected by the user.
* `BusinessRules`—Status of field-level validation rules.
* `IsValid`—Boolean flag to override control validity.
* `DataSource`—Holds the original `ContentValidationData` object.

## Reading data

To read the current state of the Validation Control content, use the following expressions:

* Getting the extracted results
  ```
  VarValidationControl1_MainPage.ExtractionResult
  ```

* Getting the selected document type
  ```
  VarValidationControl1_MainPage.SelectedDocumentType
  ```

* Getting the selected field and its values
  ```
  VarValidationControl1_MainPage.SelectedField.FieldValue.Value
  ```

  ```
  VarValidationControl1_MainPage.SelectedField.FieldValue.Confidence
  ```

* Getting taxonomy fields (useful for dropdowns)
  ```
  VarValidationControl1_MainPage.Taxonomy.GetFields(VarValidationControl1_MainPage.SelectedDocumentType).ToListSource
  ```
* Reading a table field value
  ```
  VarValidationControl1_MainPage.ExtractionResult.GetTableFieldValueByTableName("Invoice Items")(0)(0).Value
  ```

Where `(0)(0)` represents the cell at the intersection of the first column and the first row of the Invoice Items table.

Refer to [Document Understanding documentation](https://docs.uipath.com/activities/other/latest/document-understanding/contentvalidationdata-class#contentvalidationdata-class) for each class definition and properties.

## Writing data

To edit the values inside the Validation Control, use the **Set Variable Value** activity and reference the variable:

* Setting a field value in the **To variable** field
  ```
  VarValidationControl1_MainPage.Field("Patient Name").Value
  ```

**Set value** field: John Doe.
* Setting focus on a table cell value
  ```
  VarValidationControl1_MainPage.Field("Invoice Items").Field("Description", 0).SetFocus = true
  ```

Where `("Description", 0)` represents the cell at the intersection of the "Description" column and the first row of the Invoice Items table.

* Setting confidence or confirm flags
  ```
  VarValidationControl1_MainPage.Field("Patient Name").Confidence = 0.95
  ```

  ```
  VarValidationControl1_MainPage.Field("Patient Name").Confirm = true
  ```
* Updating a multi-value field
  ```
  VarValidationControl1_MainPage.Field("Diagnosis Code", 2).Value = "E11.9"
  ```

Where `2` represents the row number in the Diagnosis Code column.

* Deleting a field value
  ```
  VarValidationControl1_MainPage.Field("Vendor Name").DeleteValue
  ```
* Updating a table cell
  ```
  VarValidationControl1_MainPage.Field("Invoice Items").Field("Description", 0).Value = "50.00"
  ```

Where `("Description", 0)` represents the cell at the intersection of the "Description" column and the first row of the Invoice Items table.