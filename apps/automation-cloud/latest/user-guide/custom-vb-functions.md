---
title: "Custom VB functions"
visible: true
slug: "custom-vb-functions"
---

## Function: Serialize

* **Function:** `String Serialize(Object value)`
* **Description:** Returns a string representation of the specified object.
* **Example:**
  ```
  Serialize(Queues.testQueue.arg1)
  ```

## Function: Deserialize

* **Function:** `T Deserialize<T>(string obj)`
* **Description:** Returns an object of type T. Takes as input a valid JSON string representation of an object.
* **Example**:
  ```
  Deserialize(Of AppsFile)(textV)
  ```

Where `textV` is a variable of type **Text**, containing the serialized string of the object.

## Function: App.QueryParam

### For objects

* **Function:** `T? App.QueryParam<T>((string param, T? defaultValue = default(T))`
* **Description:**
  + If the query parameter is passed in the URL , the function returns that value deserialized based on generic type T.
  + If the deserialization fails or if the query parameter is not passed in the URL, then the function returns the default value.
* **Example**:
  ```
  App.QueryParam(Of AppsFile)("file", new AppsFile("https://i0.wp.com/
  imagelinkmri.com/wp-content/uploads/2021/08/imagelink-04.png"))
  ```

### For strings

* **Function:** `string App.QueryParam(string param, string? defaultValue = "")`
* **Description:**
  + If the query parameter is passed in the URL, the function returns that value as string.
  + If the query parameter is not passed in the URL, the function returns the default value.
* **Example**:
  ```
  App.QueryParam("stringVariable", "defaultText")
  ```

## Function: Add item to list

* **Function:** `List<T> AddItemToList<T>(List<T> list, T value)`
* **Description:** Given a list of type T, appends an item to the list and returns the updated list.
* **Example**:
  ```
  AddItemToList(Of String)(stringList, "AddMe")
  ```

## Function: Update list item at index

* **Function:** `List<T> UpdateListItemAtIndex<T>(List<T> list, int index, T value)`
* **Description:** Given a list of type T, updates the item at the specified index, and returns the updated list.
* **Example**:
  ```
  UpdateListItemAtIndex(Of String)(stringList, MainPage.EditGrid.RowIndex,"UpdateValue")
  ```

## Function: Delete item from list

* **Function:** `List<T> DeleteItemFromList<T>(List<T> list, int index)`
* **Description:** Given a list of type T, deletes the item at the specified index and returns the updated list.
* **Example**:
  ```
  DeleteItemFromList(Of String)(stringList, MainPage.EditGrid.RowIndex)
  ```

## Function: Fetch

This function is used by the **Query builder**. Refer to [The Fetch function](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/the-query-builder#the-fetch-function "Gets the number of records for an entity, for example SystemUsers.For example, for the Edit Grid control:") for more details on this function, and how to use it in practice.

:::important
The `Fetch()` function is asynchronous and does not support chaining. To display an entity record in a control**,** bind the control data source to the entity using the **Query builder**. Refer to [Using the Fetch functions](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/using-the-fetch-functions#using-the-fetch-functions) for a practical example.
:::

* **Function:** `ListSource<T> Fetch<T>(FilterGroup group = null, PaginationProps paginationProps = null, SortOption[] sortOptions = null, string[] selectedFields = null, ExpansionFieldOption[] expansionFieldOptions = null )`
* **Description:** Returns all the records of an entity object, according to the mentioned parameters.
* **Example**:
  ```
  Fetch(of AlexEntity)(createFilterGroup(Nothing, New FilterGroup(){createFilterGroup(New QueryFilter(){addFilter(MainPage.EditGrid.SearchColumn, "contains", MainPage.EditGrid.SearchTerm)}, Nothing, 0)}, 0), New PaginationProps(MainPage.EditGrid.PageStart, MainPage.EditGrid.PageLimit), New SortOption(){addSortOption(MainPage.EditGrid.SortColumn, Not(Not(MainPage.EditGrid.isDescending)))}, Nothing, New ExpansionFieldOption(){addExpansionFieldOption("CreatedBy", New String(){"Id","Name"}), addExpansionFieldOption("UpdatedBy", New String(){"Id","Name"})})
  ```

## Function: Fetch one

This function is used by the query builder, and should not be confused with the Fetch function. Refer to [The Fetch function](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/the-query-builder#the-fetch-function "Gets the number of records for an entity, for example SystemUsers.For example, for the Edit Grid control:") for details on the differences between these two functions, and how to use them in practice.

:::important
The `FetchOne()` function is asynchronous and does not support chaining. To display entity records in a control**,**, use an app variable and the [Set Value](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/rule-set-values#rule%3A-set-value) rule. Refer to [Using the Fetch functions](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/using-the-fetch-functions#using-the-fetch-functions) for a practical example.
:::

* **Function:** `T FetchOne<T>(FilterGroup group = null, PaginationProps paginationProps = null, SortOption[] sortOptions = null, string[] selectedFields = null, ExpansionFieldOption[] expansionFieldOptions = null)`
* **Description:** Returns a single record of an entity object, according to the mentioned parameters.
* **Example**:
  ```
  FetchOne(of Employee)(
          createFilterGroup(new QueryFilter(){addFilter(
              MainPage.EditGrid.SearchColumn,"contains",MainPage.EditGrid.SearchTerm)}),
              new PaginationProps(MainPage.EditGrid.PageStart, MainPage.EditGrid.PageLimit),
              new SortOption(){
                  addSortOption(
                      MainPage.EditGrid.SortColumn,MainPage.EditGrid.isDescending)
                  }
  )
  ```

## Function: Create filter group

This function is used by the **Query builder**.

* **Function:** `FilterGroup createFilterGroup(QueryFilter[] queryFilters, FilterGroup[] groups = null, int isAnd = 0)`
* **Description:** Given an array of query filters and filter groups, generates a filter group.
* **Example**:
  ```
  createFilterGroup(Nothing, New FilterGroup(){createFilterGroup(New QueryFilter(){addFilter(MainPage.EditGrid.SearchColumn, "contains", MainPage.EditGrid.SearchTerm)}, Nothing, 0)}, 0)
  ```

## Function: Add filter

This function is used by the **Query builder**.

* **Function:** `QueryFilter addFilter(string columnName, string colOperator, string value)`
* **Description:** Given a column name, operator and value, generates a query filter.
* **Example**:
  ```
  addFilter(MainPage.EditGrid.SearchColumn, "contains", MainPage.EditGrid.SearchTerm)
  ```

## Function: Add sort option

This function is used by the **Query builder**.

* **Function:** `SortOption addSortOption(string columnName, bool isDescending = false)`
* **Description:** Given a column name and a sorting value, generates and sorts a query filter.
* **Example**:
  ```
  addSortOption(MainPage.EditGrid.SortColumn, Not(Not(MainPage.EditGrid.isDescending)))}
  ```

## Function: Get choice set

:::important
* The `GetChoiceSet()` function is asynchronous and does not support chaining.
* The entity hosting the choice set must be added to your app.
:::

* **Function:** `ListSource<ChoiceSet> GetChoiceSet(string choiceSetName)`
* **Description:** Given the name of a Data Service choice set, returns all the values in the choice set.
* **Example**:
  ```
  GetChoiceSet("Gender")
  ```

## Function: Get choice set value

:::important
* The `GetChoiceSet()` function is asynchronous and it does not support chaining.
* The entity hosting the choice set must be added to your app.
:::

* **Function:** `string GetChoiceSetValue(string choiceSetName, int numberId)`
* **Description:** Given the name of a Data Service choice set and the index of a choice set option, returns the specified option.
* **Example**:
  ```
  GetChoiceSetValue("Gender", 0)
  ```

## Function: Build data table

* **Function:** `DataTable BuildDataTable(DataTable dt, DataColumn[] columns, List<Object> rowData, bool clear=false)`
* **Description:** Loads a data table with columns and rows in the **Set Value** rule and returns the updated data table.

If the `clear` parameter is true, it clears the content in the columns and the rows of the data table.
* **Example**:
  ```
  BuildDataTable(
      New DataTable("TestDT"), 
      New DataColumn(){ New DataColumn("Name"), New DataColumn("Age")},
      New List(Of Object) From { 
          AddDataRow(New Object(){"Baishali", "30"}), 
          AddDataRow(New Object(){"Viswa", "33"}) 
      },
      True
  )
  ```

## Function: Add row

* **Function:** `AddRow(DataRow row)`
* **Description:** DataTable extension method that adds the specified row to a data table and returns the updated instance.
* **Example**:
  ```
  dt.AddRow(row)
  ```

## Function: Delete row

* **Function:** `DeleteRowAt(int index)`
* **Description:** DataTable extension method that deletes the row at the specified index in a data table and returns the updated instance.
* **Example**:
  ```
  dt.DeleteRowAt(2)
  ```

## Function: Update row at

* **Function:** `UpdateRowAt(int index, DataRow row)`
* **Description:** DataTable extension method that updates the row at the specified index with the new row data and returns the updated data table.
* **Example**:
  ```
  dt.UpdateRowAt(2, row)
  ```

## Function: Update cell at (using column index)

* **Function**: `UpdateCellAt(int rowIndex, int columnIndex, object value)`
* **Description**: DataTable extension method that updates the cell of the datatable at the specified row index and column index.
* **Example**:
  ```
  dt.UpdateCellAt(0, 2, "Hi")
  ```

## Function: Update cell at (using column name)

* **Function**: `UpdateCellAt(int rowIndex, string columnName, object value)`
* **Description**: DataTable extension method that updates the cell of the datatable at the specified row index and column name.
* **Example**:
  ```
  dt.UpdateCellAt(0, "Greetings", "Hi")
  ```