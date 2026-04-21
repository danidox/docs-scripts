---
title: "Hardware and Software Requirements"
visible: true
slug: "hardware-and-software-requirements"
---

## Hardware Requirements
:::important
The hardware and software requirements presented in this document refers to the minimum and recommended resources needed for one robot to run automations. Workflow complexity and additional software installed on the machine might affect the robot's performance.
:::

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> &nbsp; </th>
   <th> Minimum </th>
   <th> Recommended </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td> <p><strong>CPU</strong> (*) </p> </td>
   <td> <p> 2 x 1.8GHz 64-bit (x64) </p> </td>
   <td> <p> 4 x 2.4GHz 64-bit (x64) </p> </td>
  </tr>
  <tr>
   <td> <p><strong>RAM</strong> (**) </p> </td>
   <td> <p> 4 GB of available system memory </p> </td>
   <td> <p> 8 GB of available system memory </p> </td>
  </tr>
  <tr>
   <td> <p><strong>Disk Space</strong> (***) </p> </td>
   <td colspan="2"> <p> UiPathStudio.msi: </p>
      <ul>
        <li> 3.4 GB for new silent installations. 1 GB of additional space is required for UI-based installations. </li>
        <li> 3.4 - 3.8 GB for automatic updates (varies depending on the version you are updating from). 1 GB of additional space is required for UI-based updates. </li>
      </ul>
UiPathRobot.msi:
      <ul>
        <li> 1.6 GB for new silent installations and updates. </li>
        <li> 1.9 GB for UI-based installations and updates. </li>
      </ul>
<p> N/A </p> </td>
  </tr>
 </tbody>
</table>

(*) UiPath does not support the ARM architecture on Windows.

(**) Automations that use Document Understanding frameworks might need additional RAM.

(***) The disk space requirements do not include the space for the automation dependencies, such as packages and libraries.

You can also check out hardware requirements for [Studio](https://docs.uipath.com/studio/standalone/2023.10/user-guide/hardware-and-software-requirements) and [Orchestrator](https://docs.uipath.com/orchestrator/standalone/2023.10/installation-guide/orchestrator-hardware-requirements).

## Software Requirements

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> &nbsp; </th>
   <th> Supported Versions </th>
   <th> Particularities </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td rowspan="6"> <p><strong>Operating System</strong> (*) </p> </td>
   <td> <p> Windows 10 </p><p> Windows 10 N </p> </td>
   <td> <p> Works with Azure Virtual Desktops (AVD). <sup> 1 </sup></p><p> Supports Windows 365 machines. </p> </td>
  </tr>
  <tr>
   <td> <p> Windows 11 </p> </td>
   <td> <p> Works with Azure Virtual Desktops (AVD). <sup> 1 </sup></p><p> Supports Windows 365 machines. </p> </td>
  </tr>
  <tr>
   <td> <p> Microsoft Azure Windows 10 Enterprise Multi-Session </p> </td>
   <td> Works with Azure Virtual Desktops (AVD). <sup> 1 </sup> </td>
  </tr>
  <tr>
   <td> Microsoft Azure Windows 11 Enterprise Multi-Session </td>
   <td> Works with Azure Virtual Desktops (AVD). <sup> 1 </sup> </td>
  </tr>
  <tr>
   <td> <p> Windows Server 2016 </p><p> Windows Server 2019 </p><p> Windows Server 2022 </p> </td>
   <td> &nbsp; </td>
  </tr>
  <tr>
   <td> <p> Windows Server Core 2016 </p><p> Windows Server Core 2019 </p><p> Windows Server Core 2022 </p> </td>
   <td> <p> Can only run background unattended jobs. </p> The jobs run under the local system account by default. To use a specific user (credentials specified in Orchestrator), you need to configure the <code>UIPATH_HEADLESS_WITH_USER</code> environment variable on the robot machine and set the value to <code>True</code> . </td>
  </tr>
  <tr>
   <td> &nbsp; </td>
   <td> MacOS version 10.15 (Catalina) or greater. </td>
   <td> Required by the UiPath Assistant for Mac. </td>
  </tr>
  <tr>
   <td rowspan="2"> <p><a href="https://citrixready.citrix.com/uipath/uipath-studio.html"> Citrix environments </a></p> </td>
   <td> <p> XenApp v6.5 or greater </p> </td>
   <td> &nbsp; </td>
  </tr>
  <tr>
   <td> <p> XenDesktop v7.0 or greater </p> </td>
   <td> &nbsp; </td>
  </tr>
  <tr>
   <td> <p><strong>.NET Framework</strong></p> </td>
   <td> <p> Version 4.6.1 or greater </p> </td>
   <td> <p> If your machine runs Windows OS in a language other than English, install the corresponding language pack for the .Net framework version you are using. </p><p> This is required for running Studio in any of the available languages. The .Net framework and related language pack version must correspond, and any conflicting .Net framework versions installed on the machine should be removed. </p> </td>
  </tr>
 </tbody>
</table>
:::important
<sup>1</sup> To ensure unattended robots work correctly in AVD environments, always close or log out of sessions when finished. Leaving AVD sessions in a disconnected state prevents the robot from creating a new session for its job, as an existing session is already present, but the robot cannot access it. <sup>2</sup> We support UiPath software only on officially supported operating systems. Although UiPath software may still run on unsupported OS versions, we do not provide updates or fixes for unsupported environments.
:::