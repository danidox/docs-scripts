---
title: "Legacy versus VB expressions"
visible: true
slug: "legacy-versus-vb-expressions"
---

This section lists the common use cases for binding app elements, and how you can achieve the binding using legacy and VB expressions.

## Using static string URLs in Image controls

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Legacy </p> </th>
   <th> <p> VB </p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
      <ol>
        <li> <p> Add the <strong>Image</strong> control. </p> </li>
        <li> Set the <strong>URL/Value binding</strong> property to <code>https://path/to/the/image_file.jpg</code> </li>
      </ol>
<p>Note: <p> Base64 images are also supported. </p></p></td>
   <td>
      <ol>
        <li> <p> Add the <strong>Image</strong> control. </p> </li>
        <li> Set the <strong>Source</strong> property to <code>new AppsFile("https://path/to/the/image_file.jpg")</code> </li>
      </ol>
<p>Note: <p> Base64 images are also supported. </p></p></td>
  </tr>
 </tbody>
</table>

## Using the File field of an entity in Image controls

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Legacy </p> </th>
   <th> <p> VB </p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
      <ol>
        <li> <p> In your app, reference the entity that holds the desired file. </p> </li>
        <li> <p> Bind the entity to a <strong>Table</strong> control. </p> </li>
        <li> <p> Add the <strong>Image</strong> control. </p> </li>
        <li> <p> Set the <strong>URL/Value binding</strong> property to the file. </p> </li>
      </ol>
<img alt="docs image" src="/images/apps/apps-docs-image-320358-d358e205.webp"/> </td>
   <td>
      <ol>
        <li> <p> In your app, reference the entity that holds the desired file. </p> </li>
        <li> <p> Bind the entity to a <strong>Table</strong> control. </p> </li>
        <li> <p> Add the <strong>Image</strong> control. </p> </li>
        <li> Set the <strong>Source</strong> property to <code>MainPage.Table.SelectedItem.FileColumn</code> </li>
      </ol>
</td>
  </tr>
 </tbody>
</table>

## Using files from a Storage Bucket in Image controls

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Legacy </p> </th>
   <th> <p> VB </p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
      <ol>
        <li> <p> In your app, reference the storage bucket that holds the desired file. </p> </li>
        <li> Create an app variable of type AppsFile. For example <code>fileVar</code> . </li>
        <li> <p> Add the <strong>Download file from Storage Bucket</strong> rule. </p> </li>
        <li> Assign the downloaded file to the previously created app variable ( <code>fileVar</code> ). </li>
        <li> <p> Add the <strong>Image</strong> control. </p> </li>
        <li> Set the <strong>URL/Value binding</strong> property to <code>fileVar</code> . </li>
      </ol>
</td>
   <td>
      <ol>
        <li> <p> In your app, reference the storage bucket that holds the desired file. </p> </li>
        <li> Create an app variable of type AppsFile. For example <code>fileVar</code> . </li>
        <li> <p> Add the <strong>Download file from Storage Bucket</strong> rule. </p> </li>
        <li> Assign the downloaded file to the previously created app variable ( <code>fileVar</code> ). </li>
        <li> <p> Add the <strong>Image</strong> control. </p> </li>
        <li> Set the <strong>Source</strong> property to <code>fileVar</code> . </li>
      </ol>
</td>
  </tr>
 </tbody>
</table>

## Using choice sets to populate List controls

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Legacy </p> </th>
   <th> <p> VB </p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td> <p><a href="https://docs.uipath.com/apps/automation-cloud/latest/legacy-user-guide/using-choice-set#procedure"> Leverage entities in your app by using choice sets </a></p> </td>
   <td>
      <ol>
        <li> <p> In your app, reference the entity with the choice set. </p> </li>
        <li> <p> Add the <strong>List</strong> control. </p> </li>
        <li> Set the <strong>List source</strong> property to <code>GetChoiceSet("entity_name")</code> . </li>
        <li> <p> Set the <strong>Column</strong> property to the choice set name. </p> </li>
      </ol>
<p> Read <a href="https://docs.uipath.com/apps/automation-suite/latest/user-guide/using-choice-set#procedure"> this procedure </a> for more information. </p> </td>
  </tr>
 </tbody>
</table>

## Referencing a choice set bound to List controls

| Legacy | VB |
| --- | --- |
| Steps 4 and 5 in [Leverage entities in your app by using choice sets](https://docs.uipath.com/apps/automation-cloud/latest/legacy-user-guide/using-choice-set#procedure) | ``` <PAGE_NAME>.<CONTROL_NAME>.SelectedItem.<COLUMN_NAME> ``` |

## Setting a single select choice set as the default value for controls

**Dropdown**, **Radio Button** and **List** controls support single select choice sets.

| Legacy | VB |
| --- | --- |
| ![docs image](/images/apps/apps-docs-image-315819-6ecde6b5.webp) | ``` <PageName>.<ControlName>.DataSource.data.Select(Function(x) x.NumberId).ToList(0) ``` |

## Setting a multiselect choice sets as the default value for controls

**Multiselect Dropdown** controls support multiselect choice sets.

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Legacy </p> </th>
   <th> <p> VB </p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td> <img alt="docs image" src="/images/apps/apps-docs-image-315829-4cb6e64b.webp"/> </td>
   <td> <button> assignment </button><pre>&lt;PAGE_NAME&gt;.&lt;MULTISELECT_CONTROL_NAME&gt;.DataSource.data.Where(Function(x) &lt;VARIABLENAME&gt;.&lt;ENTITY_FIELD_OF_TYPE_CS&gt;.contains(x.NumberId)).toList()</pre><p>Note: To use this expression, ensure the entity variable is set to <code>selectedItem</code> using a <strong>Set Value</strong> rule. </p></td>
  </tr>
 </tbody>
</table>

## Using static strings to populate List controls

| Legacy | VB |
| --- | --- |
| ``` =["Value1", "Value2", "Value3"] ``` | ``` AppsDataSource.from({"Value1", "Value2", "Value3"}) ``` |

## Bind a date to Date Picker controls

| Legacy | VB |
| --- | --- |
| To bind todays date, set the **Default Date** property to `=Now()` | To bind todays date, set the **Default Date** property to `DateOnly.FromDateTime(Now)` |
| To bind a specific date, for example 5th May 2021, set the **Default Date** property to `2021-01-05` | To bind a specific date, for example 5th May 2021, set the **Default Date** property to `new DateOnly(2021,1,25)` |

## Using an entity Date-Time field in Date Picker controls

| Legacy | VB |
| --- | --- |
| Bind the required entity field to the **Date Picker** control. | ``` DateOnly.FromDateTime(customerEntityVar.DOB.Value.Date) ``` |

## Computing the difference between two Date Picker values

| Legacy | VB |
| --- | --- |
| N/A | ``` MainPage.Datepicker1.Value.Value.DayNumber - MainPage.Datepicker.Value.Value.DayNumber ``` |

## Referencing errors

You can reference the errors from the following rules:

* Start Process
* Entity rules
* Queue rules
* Trigger Workflow rule

| Legacy | VB |
| --- | --- |
| [Start Process rule: Handling Errors](https://docs.uipath.com/apps/automation-cloud/latest/legacy-user-guide/rule-start-process#handling-errors) | In VB expressions, errors are exposed in the rule output. Reference an error as follows: ``` <PAGENAME>.<RULENAME>.Error.Message ```  ``` <PAGENAME>.<CONTROLNAME>.<RULENAME>.Error.Message ```  ![docs image](/images/apps/apps-docs-image-320415-19716b99.webp) |