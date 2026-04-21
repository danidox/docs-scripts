---
title: "Hardware and software requirements"
visible: true
slug: "hardware-and-software-requirements"
---

## Hardware requirements

The following hardware specifications list the minimum and recommended resources for a single robot to execute jobs.
:::important
These requirements only consider the resources needed for the automation, and do not include the resources used by other applications involved in the automations.
:::

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Resource </p> </th>
   <th> Minimum </th>
   <th> Recommended </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td> <p><strong>CPU</strong><sup> 1 </sup></p> </td>
   <td>
      <ul>
        <li> <p> For Intel x64: 2 x 1.8GHz 6I4-bit </p> </li>
        <li> <p> For ARM64: Apple M1 </p> </li>
      </ul>
</td>
   <td>
      <ul>
        <li> <p> For Intel x64: 4 x 2.4GHz 64-bit </p> </li>
        <li> <p> For ARM64: Apple M1 </p> </li>
      </ul>
</td>
  </tr>
  <tr>
   <td> <p><strong>RAM</strong><sup> 2 </sup></p> </td>
   <td> <p> 4 GB of available system memory </p> </td>
   <td> <p> 8 GB of available system memory </p> </td>
  </tr>
  <tr>
   <td> <p><strong>Disk Space</strong><sup> 3 </sup></p> </td>
   <td colspan="2"> <p><strong>UiPathStudio.msi</strong> : </p>
      <ul>
        <li> 3.4 GB for new silent installations. 1 GB of additional space is required for UI-based installations. </li>
        <li> 3.4 - 3.8 GB for automatic updates (varies depending on the version you are updating from). 1 GB of additional space is required for UI-based updates. </li>
      </ul>
<strong>UiPathRobot.msi</strong> :
      <ul>
        <li> 1.6 GB for new silent installations and updates. </li>
        <li> 1.9 GB for UI-based installations and updates. </li>
      </ul>
</td>
  </tr>
 </tbody>
</table>

<sup>1</sup> UiPath does not support the ARM architecture on Windows.

<sup>2</sup> Automations that use Document Understanding frameworks might need additional RAM.

<sup>3</sup> The disk space requirements do not include the space for the automation dependencies, such as packages and libraries.

### Hardware requirements for High-Density Robots
:::important
High-Density Robots are available on Windows platforms exclusively.
:::

For a High-Density setup, where multiple robots concurrently execute jobs on the same Windows Server machine, you must multiply the minimum and recommended hardware requirements with the number of runtimes set for the [machine template in Orchestrator](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-machines#adding-a-machine-template).

For example, with three users concurrently executing jobs, the minimum requirements are:

* For Intel x64, you need six cores of 1.8GHz 64-bit (2 x 1.8GHz 64-bit per runtime), and a RAM of 12 GB (4 GB per runtime).

### Hardware requirements for the live streaming and recording features

For scenarios where the [live streaming](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/live-streaming-and-remote-control) and [recording](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-recording) features are required, you must apply the recommended hardware requirements:

* **CPU—** For Intel x64: 4 x 2.4GHz 64-bit
* **RAM—**8 GB

## Software requirements

The following software specifications list the minimum and recommended resources for a single robot to execute jobs.
:::important
These requirements only consider the resources needed for the automation, and do not include the resources used by other applications involved in the automations.
:::

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> <p> Resource </p> </th>
   <th> Supported versions </th>
   <th> <p> Details </p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td rowspan="7"> <p><strong>Operating System</strong><sup> 2 </sup></p> </td>
   <td> <p> Windows 10 </p><p> Windows 10 N </p> </td>
   <td> <p> Works with Azure Virtual Desktops (AVD). <sup> 1,3 </sup></p><p> Supports Windows 365 machines. <sup> 3 </sup></p> </td>
  </tr>
  <tr>
   <td> <p> Windows 11 </p> </td>
   <td> <p> Works with Azure Virtual Desktops (AVD). <sup> 1,3 </sup></p><p> Supports Windows 365 machines. <sup> 3 </sup></p> </td>
  </tr>
  <tr>
   <td> <p> Microsoft Azure Windows 10 Enterprise Multi-Session </p> </td>
   <td> Works with Azure Virtual Desktops (AVD). <sup> 1,3 </sup> </td>
  </tr>
  <tr>
   <td> Microsoft Azure Windows 11 Enterprise Multi-Session </td>
   <td> Works with Azure Virtual Desktops (AVD). <sup> 1,3 </sup> </td>
  </tr>
  <tr>
   <td> <p> Windows Server 2016 </p><p> Windows Server 2019 </p><p> Windows Server 2022 </p><p> Windows Server 2025 </p> </td>
   <td> &nbsp; </td>
  </tr>
  <tr>
   <td> <p> Windows Server Core 2016 </p><p> Windows Server Core 2019 </p><p> Windows Server Core 2022 </p> </td>
   <td> <p> Can only run background unattended jobs. </p> By default, jobs run under the local system account. To use a specific user, set their credentials in Orchestrator. Then, on the robot machine, set the <code>UIPATH_HEADLESS_WITH_USER</code> environment variable to <code>True</code> . </td>
  </tr>
  <tr>
   <td> MacOS version 10.15 (Catalina) or greater. </td>
   <td> Required by the Assistant for Mac. </td>
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
   <td> <p> Version 4.7.2 or greater </p> </td>
   <td> <p> To run Studio in any of the available languages, install the matching language pack version for your .NET framework, and remove conflicting .Net versions. </p> </td>
  </tr>
 </tbody>
</table>
:::important
<sup>1</sup> To ensure unattended robots work correctly in AVD environments, always close or log out of sessions when finished. Leaving AVD sessions in a disconnected state prevents the robot from creating a new session for its job, as an existing session is already present, but the robot cannot access it. <sup>2</sup> We support UiPath software on officially supported operating systems, including Extended Security Update (ESU) versions. Although UiPath software may still run on unsupported OS versions, we do not provide updates or fixes for unsupported environments. <sup>3</sup> To ensure that unattended robots are available for taking jobs from Orchestrator, the AVD or Windows 365 machines need to stay **always-on**. You must disable the hibernation on the machines that you want to run as unattended robots.
:::