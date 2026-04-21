---
title: "Common VB expressions for Validation Control"
visible: true
slug: "common-vb-expressions-for-validation-control"
---

## Getting the whole Extraction Result

To return the extraction result object, currently rendered by the control:

* Using the Validation Control element
  ```
  MainPage.ValidationControl.ExtractionResult
  ```
* Using the Validation Control variable
  ```
  AppVariable.VarValidationControl.ExtractionResult
  ```

For example:

* Getting the field value by field name:
  ```
  AppVariable.VarValidationControl_MainPage.ExtractionResult.GetFieldByFieldName("Invoice Number").Values(0).Value
  ```
* Getting the field value by field index:
  ```
  AppVariable.VarValidationControl_MainPage.ExtractionResult.ResultsDocument.Fields(0).Values(0).Value
  ```
* Getting the list of all field names displayed in the Validation Control
  ```
  AppVariable.VarValidationControl.ExtractionResult.GetFields().Select(Function(f) f.FieldName)
  ```

Here is the list of methods you can use to read data from ExtractionResult:

* `.GetDocumentType()`
* `.GetField()`
* `.GetFieldByFieldName()`
* `.GetFields()`
* `.GetFieldValidatorNotes()`
* `.GetFieldValidatorNotesByFieldName()`
* `.GetSimpleFieldValues()`
* `.GetSimpleFieldValuesByFieldName()`
* `.GetTable()`
* `.GetTableByTableName()`
* `.GetTableFieldValue()`
* `.GetTableFieldValueByTableName()`
* `.GetValueCount()`
* `.GetValueCountByFieldName()`

## Getting the taxonomy used by the control

To inspect document types, fields, or display properties:

* Using the Validation Control element
  ```
  MainPage.ValidationControl.Taxonomy
  ```
* Using the Validation Control variable
  ```
  AppVariable.VarValidationControl.Taxonomy
  ```

For example:

* Getting the list of fields in a taxonomy and save it as a source for a dropdown control:
  ```
  AppVariable.VarValidationControl_MainPage.Taxonomy.GetFields(VarValidationControl_MainPage.SelectedDocumentType).ToListSource
  ```

Here is the list of methods you can use to read data from Taxonomy:

* `.GetFields()`

## Getting the selected document type, as String

To bind UI elements to the curently chosen document type:

* Using the Validation Control element
  ```
  MainPage.ValidationControl.SelectedDocumentType
  ```
* Using the Validation Control variable
  ```
  AppVariable.VarValidationControl.SelectedDocumentType
  ```

## Getting the selected field object

* Using the Validation Control element
  ```
  MainPage.ValidationControl.SelectedField
  ```
* Using the Validation Control variable
  ```
  AppVariable.VarValidationControl.SelectedField
  ```

You can further access `SelectedField` properties, such as `.Field.FieldName`, `.Field.FieldType`, or `.Field.ValidatorNotes`.

For example:

* Getting the selected field value:
  ```
  AppVariable.VarValidationControl_MainPage.SelectedField.Field.FieldValue
  ```

You can further access selected field value properties, such as `.FieldValue.Value`, `.FieldValue.Confidence`, `.FieldValue.OperatorConfirmed`.
* Getting the selected field all values:
  ```
  AppVariable.VarValidationControl_MainPage.SelectedField.Field.Values
  ```
* Getting the selected field first value:
  ```
  AppVariable.VarValidationControl_MainPage.SelectedField.Field.Values(0).Value
  ```
* Getting the selected field data type:
  ```
  AppVariable.VarValidationControl_MainPage.SelectedField.Field.FieldType.ToString
  ```
* Getting the selected field index:
  ```
  AppVariable.VarValidationControl_MainPage.SelectedField.FieldValueIndex.ToString
  ```

## Getting the Validation Control properties

To read Validation Control properties:

* Using the Validation Control element
  ```
  MainPage.ValidationControl.<PROPERTY NAME>
  ```
* Using the Validation Control variable
  ```
  Controls.MainPage.ValidationControl.<PROPERTY NAME>
  ```

## Reading a field value from a table

* Reading field value from a table
  ```
  AppVariable.VarValidationControl_MainPage.ExtractionResult.GetTableFieldValueByTableName(<TABLENAME>)(<COLUMN INDEX>)(<ROW INDEX>).Value
  ```

For example:

  ```
  AppVariable.VarValidationControl_MainPage.ExtractionResult.GetTableFieldValueByTable Name("Invoice Items")(0)(0).Value
  ```

## Setting focus on a table cell

* Using the **Set Variable Value** activity with the following expression in the **Set value** field
  ```
  AppVariable.VarValidationControl_MainPage.Field("Invoice Items").Field("Description", 0).SetFocus
  ```