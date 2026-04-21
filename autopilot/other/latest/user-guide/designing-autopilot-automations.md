---
title: "Designing relevant automations for Autopilot for Everyone"
visible: true
slug: "designing-autopilot-automations"
---

This page is targeted for automation developers, and guides them through the best practices on building automations which are optimized for Autopilot for Everyone.

Autopilot for Everyone can recommend and execute automations based on the user query. It also infers argument values to help setting up the automation. For these reasons, out-of-the-box automations have additional configurations and best practices to help facilitate Autopilot for Everyone features.

## Design best practices

To build automations that can be leveraged later by Autopilot for Everyone, we suggest the following best practices:

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p><strong>Project best practices</strong></p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
      <ul>
        <li> To allow Autopilot for Everyone to use the automation on MacOS, build the automation projects with the cross-platform compatibility. </li>
        <li> Focus each automation on a single task. For example, use one to five activities in a single sequence. </li>
      </ul>
</td>
  </tr>
 </tbody>
</table>

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p><strong>Input argument best practices</strong></p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
      <ul>
        <li> Use descriptive argument names and naming conventions, such as CamelCase format. </li>
        <li> If some arguments are mandatory for the successful execution of the automation, set them as required during the design time. </li>
        <li> Use the following data types exclusively: <ul> <li> String - rendered as a free text field </li>
        <li> Int32 - rendered as a whole number picker </li>
        <li> Double - rendered as a whole or decimal number picker </li>
        <li> Boolean - rendered as a True / False dropdown menu </li>
        <li> Datetime - rendered as a date-time picker </li>
      </ul>
</li>
    </ul>
</td>
  </tr>
 </tbody>
</table>

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p><strong>Output argument best practices</strong></p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
      <ul>
        <li> Use descriptive argument names and naming conventions, such as CamelCase format. </li>
        <li> Use the following output arguments exclusively: <ul> <li><code>ResultMessage</code> - can be either of the following: <ul> <li> A string message, which is display back to the user. It usually holds the results of the operation. </li>
        <li> A string serialization of a JSON or Data Table object. Important: Autopilot can understand JSON arrays with single-level JSON objects or flat Data Tables. </li>
      </ul>
</li>
       <li> <code>output_html</code> - A HTML string used by Autopilot for rendering. If you use this output, Autopilot renders the HTML in an iFrame. The automation must not be configured as a pre-response automation. </li>
      </ul>
</li>
    </ul>
</td>
  </tr>
 </tbody>
</table>

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p><strong>Exception handling best practices</strong></p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
      <ul>
        <li> <p> Use business rule exceptions and custom error messages to handle known errors, preventing the full stack trace from being sent to Autopilot for Everyone. </p> </li>
      </ul>
</td>
  </tr>
 </tbody>
</table>


:::note
To use existing automations in Autopilot for Everyone, make sure they adhere to the previously mentioned design considerations.
:::

## Automation properties for Autopilot for Everyone

Autopilot for Everyone recommends automations solely based on the descriptions you provide. For Autopilot for Everyone to suggest the correct automation, make sure each automation has distinct descriptions, to minimize overlaps. Autopilot for Everyone can also infer argument values needed for the automation, simplifying the process and reducing the need for you to understand all the details. During setup, be sure to provide clear arguments. When you run the automation, Autopilot for Everyone infers the argument values from the conversation or asks for additional details.

A set of metadata properties assist Autopilot for Everyone in understanding various aspects such as:

* What the automation does
* How the automation card is displayed
* How to infer the argument values
* How the automation should be run
* Any necessary context before executing the automation

Learn how to configure [Automation properties](https://docs.uipath.com/autopilot/other/latest/everyone-admin-guide/automation-properties).

## Automations that return large amounts of data

Autopilot for Everyone chat sessions have a limited capacity for information. Therefore, when building data-heavy automations, such as retrieval tasks, make sure to return only the relevant data.

To do this, consider the following:

* Include arguments in the automation for filtering purposes. For instance, if you retrieve events from Outlook, add arguments that could allow filtering the results by the subject or attendees.
* Create two automations:
  + One automation to return multiple objects with limited details, and
  + One automation to return extensive details for a single object.

## Autopilot for Everyone Studio template

The template UiPath provides has several design-specific recommendations already applied. To use the template, access it from [UiPath Marketplace > Studio > Templates](https://marketplace.uipath.com/listings/autopilot-automation-template4109) page.

After designing the automation, make sure to:

1. Publish the package to the tenant where Autopilot for Everyone is installed.
2. Create and deploy the corresponding process to a folder where the required users have access.
3. Configure the [automation properties](https://docs.uipath.com/autopilot/other/latest/everyone-admin-guide/automation-properties).