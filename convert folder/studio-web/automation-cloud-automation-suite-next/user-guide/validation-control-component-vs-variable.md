---
title: "Validation Control object vs variable"
visible: true
slug: "validation-control-component-vs-variable"
---

The Validation Control object and the Validation Control variable are both part of how UiPath Apps handle the Validation Control component, but they serve different purposes. If you want to bind logic, reference field values, or manage validation results, use the variable. If you want to adjust layout or properties of the visible control, use the object.

Here is a breakdown of the differences between the object and the variable, so you can use them correctly in your app:

Expand Table

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> Feature </th>
   <th> Validation Control object </th>
   <th> Validation Control variable </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th> What it is </th>
   <td> This is the UI component you drag onto a canvas when building your web app in Studio Web. </td>
   <td> This is an auto-generated app variable that links to the Validation Control object. It holds all the data and logic behind the UI, such as taxonomy, extraction results, and current user selections. </td>
  </tr>
  <tr>
   <th> What it does </th>
   <td>
      <ul>
        <li> Displays the document and extracted data to the user. </li>
        <li> Allows direct user interaction in the browser, to review or correct information. </li>
        <li> Supports basic App controls properties, such as <strong>DataSource</strong> , <strong>Hidden</strong> , <strong>Disabled</strong> , and <strong>ShowDocumentType</strong> . </li>
      </ul>
</td>
   <td>
      <ul>
        <li> Allows programmatic access to the Validation Control data. </li>
        <li> Allows reading and writing data. </li>
        <li> Stores data and exposes logic behind the control. </li>
      </ul>
</td>
  </tr>
  <tr>
   <th> Where to use it </th>
   <td>
      <ul>
        <li> In the app designer, during design time. </li>
        <li> For UI-level logic, such as styling or setting visibility at runtime, for example <code>ValidationControl1.Hidden = true</code> . </li>
      </ul>
</td>
   <td>
      <ul>
        <li> In expressions or automation activities, such as <strong>Set Variable Value</strong> . </li>
        <li> For binding dropdowns, running logic, updating field values, or accessing document metadata. </li>
        <li> In more complex workflows where you need to inspect or update the contents of the validation task dynamically. </li>
      </ul>
</td>
  </tr>
 </tbody>
</table>