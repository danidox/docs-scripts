---
title: "Rule: Reset Values"
visible: true
slug: "rule-reset-values"
---

Use the **Reset Values** rule to revert a control to their default value.

Clicking the **Items To Reset** filed opens the **Resources** panel, which displays the available controls.

![docs image](/images/apps/apps-docs-image-291108-28d95fc1.webp)

:::note
Applying this rule to a container or a page impacts all the controls within the container/page, including nested containers.
:::

## Available Controls

To better understand how the **Reset Values** rule works for different controls, check the table below.

:::note
If a control is not mentioned in the table below, the **Reset Values** rule does not apply to that control.
:::

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Control </p> </th>
   <th> <p> How it works </p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td> <p><strong>Checkbox</strong></p> </td>
   <td>
      <ul>
        <li> If no default value is configured for the control, the rule deselects the checkbox. </li>
        <li> If a default value is configured, the rule applies the default selection. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Date Picker</strong></p> </td>
   <td>
      <ul>
        <li> If no default value is configured for the control and if no default date is configured, the rule clears the date. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Dropdown</strong></p> </td>
   <td>
      <ul>
        <li> If a default value is configured, the rule only clears the selected value, not all control values. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Multiselect dropdown</strong></p> </td>
   <td>
      <ul>
        <li> If a default value is configured, the rule only clears the selected value, not all control values. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>File Uploader</strong></p> </td>
   <td>
      <ul>
        <li> The rule clears the content in the File Uploader control, so users can upload another file. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Radio Button</strong></p> </td>
   <td>
      <ul>
        <li> The rule removes any selection, unless a default value is configured. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Slider</strong></p> </td>
   <td>
      <ul>
        <li> The rule resets the slider bubble, unless a default value is configured. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Switch</strong></p> </td>
   <td>
      <ul>
        <li> The rule resets the switch, unless a default value is configured. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Text Area</strong></p> </td>
   <td>
      <ul>
        <li> The rule clears the values, unless a default value is configured. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Textbox</strong></p> </td>
   <td>
      <ul>
        <li> The rule clears the values, unless a default value is configured. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Edit grid</strong></p> </td>
   <td>
      <ul>
        <li> The rule clears the selected values. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Table</strong></p> </td>
   <td>
      <ul>
        <li> The rule clears the selected values. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Container</strong></p> </td>
   <td>
      <ul>
        <li> If you apply this rule to a container, it'll be applied to all controls within the container, including nested containers. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>Container Layout</strong></p> </td>
   <td>
      <ul>
        <li> If you apply this rule to a container, it'll be applied to all controls within the container, including nested containers. </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>App variable</strong></p> </td>
   <td>
      <ul>
        <li> The rule sets the value to empty. </li>
      </ul>
</td>
  </tr>
 </tbody>
</table>

## Example

You can use the **Reset Values** rule when building a form.

For example, you can add the rule to a **Submit** button at the end of a form and configure it to reset the whole container. This way, after filling in all the fields and submitting the information, the form resets to its default values and the user can fill it in a second time.