---
title: "Variables in Apps"
visible: true
slug: "variables-in-apps"
---

Use variables to store values between pages.

:::note
You can set a default value of the variable on page load by using the **Set Value** rule in the **Loaded** event of the page.
:::

Apps supports creating variables of the following types:

* **AppsFile** - file objects specific for Apps, which handles files uploading or downloading.
  ```
  new AppsFile("https://imageURL.png")
  ```
* **Array** - arrays of primitive data types or complex objects. For example:
  + Array of strings : `New String() {"Hello", "World"}`
  + Array of AppsFile: `New AppsFile() { new AppsFile("Url1"), new AppsFile("Url2")}`
  + Array of entity type:
    ```
    new Customer() { 
    New Customer("1", "Baishali"), 
    New Customer("2", "Viswa"), 
    New Customer("3", "Evan") }
    ```
* **ChoiceSet** - stores the choice set data of an entity. For example:
  + `GetChoiceSet("Team")` - returns a ListSource with the choice set values.
  + `GetChoiceSetValue("Team", 1)` - returns the indicated choice set value.
* **DataTable** - a system data type used to store the value of a process Datatable output argument, or to create a custom Datatable, for example:
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
* **Date** - for example, `New System.DateTime (1993, 5, 31, 12, 35, 0)`.
* **DateOnly** - a specific date, without time. For example, `New System.DateOnly (2020, 04, 20)`.
* **DateTimeOffset** - a date and time, relative to UTC. This structure includes a DateTime value and an Offset property, that defines the difference between the current DateTimeOffset date and the Coordinated Universal Time (UTC). For example:
  ```
  new System.DateTimeOffset( new System.DateTime(2023, 5, 15, 7, 0, 0),
    new System.TimeSpan(-7, 0, 0) )
  // output 5/15/2023 7:00:00 AM - 07:00
  ```
* **Decimal number** - for example, `88.53`.
* **Double**
* **Guid** - the unique identifier of an entity.
* **Int16**
* **Int64**
* **List&lt;T&gt;** - for example:
  + List of strings : `New List(Of String) From {"string 1", "string 2", "string 3"}`
  + List of ListPair (for dropdown controls):
    ```
    New List(Of Customer) From { 
    New Customer("1", "Baishali"), 
    New Customer("2", "Viswa"), 
    New Customer("3", "Evan") }
    ```
* **ListSource** - used to store the result of a entity query in a variable. You need to use the syntax `ListSource(of <Entity_name>)`.
* **Nullable** - used to define a null value. By default, all reference types, such as String, are nullable, but all value types, such as Int32, are not.
  :::note
  By default, primitive data types, except String, are non-nullable. Use this variable type to set them to null. For example, if you create an app variable of type Nullable, then you can set the value to "Nothing".
  :::
* **Object** - stores any type.
* **Single** - Used to store floating-point values that do not require the full data width of Double. The default value is 0.
* **Text** (String) - for example, `"Hello world"`
* **True or false** (Boolean)
* **UInt16** - holds unsigned 16-bit (2-byte) integers ranging in value from 0 through 65,535.
* **UInt32** - holds unsigned 32-bit (4-byte) integers ranging in value from 0 through 4,294,967,295.
* **UInt64** - holds unsigned 64-bit (8-byte) integers ranging in value from 0 through 18,446,744,073,709,551,615.
* **Whole number** (Int32) - for example, `88`