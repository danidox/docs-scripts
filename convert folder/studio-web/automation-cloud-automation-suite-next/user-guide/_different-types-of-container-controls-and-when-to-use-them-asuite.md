---
title: "Differences Between Container Controls"
visible: true
slug: "different-types-of-container-controls-and-when-to-use-them"
---

Learn the main differences between the container types:

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p><a href="https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/container#container"> Container </a></p> </th>
   <th> <p><a href="https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/container-layout#container-layout"> Container Layout </a></p> </th>
   <th> <p><a href="https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/page-container#page-container"> Page Container </a></p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td> <p> A single container which can hold controls and other containers within it. </p> </td>
   <td> <p> A container layout that groups several simple containers, and helps build a complex app layout. </p> </td>
   <td> <p> Page containers host another page in the current page. </p> </td>
  </tr>
  <tr>
   <td> <p> Grows based on the size of its contents. </p> </td>
   <td> <p> Has a fixed height, while its width depends on the screen width. </p> </td>
   <td> <p> Grows based on the size of the hosted page. </p> </td>
  </tr>
  <tr>
   <td>
      <ul>
        <li> Aligns a group of elements similarly. </li>
        <li> Aligns a specific element different from that of other elements. </li>
        <li> You can nest containers: <ul> <li> To align/position elements in the inner container differently to the outer one. </li>
        <li> <p> We recommend nesting maximum 4 containers for performance reasons, however no limit is imposed. </p> </li>
      </ul>
</li>
    </ul>
</td>
   <td>
      <ul>
        <li> <p> Creates the page structure. </p> </li>
        <li> We recommend using it only in page containers. </li>
        <li> <p> Nesting <strong>Container Layouts</strong> leads to extra spaces and maintenance issues. </p> </li>
      </ul>
</td>
   <td>
      <ul>
        <li> Useful for reusing components in your app, for example having a the same header or body across different pages of your app </li>
        <li> Helps app maintenance </li>
      </ul>
</td>
  </tr>
 </tbody>
</table>

## Example on How to Align Controls Using Containers

Assume your app contains a form, where you want to collect the following information from the user: First Name, Last Name, Email & School. While Email & School input boxes can be one below the other, we want the First Name and Last Name available side by side.

This can be accomplished by the following steps:

1. Add a new **Container**.
2. Change the layout of the **Container** to Horizontal.
3. Add the two **Textboxes** within the container.