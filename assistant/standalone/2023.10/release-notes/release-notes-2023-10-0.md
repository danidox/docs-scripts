---
title: "2023.10.0"
visible: true
slug: "release-notes-2023-10-0"
---

**Release date: 25 October 2023**

In this release, the Robot and UiPath Assistant went through some changes and a lot of improvements. All these to provide an even better performance and experience while using them.

Read more about this release below:

## What's New

**Disconnected credentials proxy**

Starting with the 2023.10 release, if you are using the Cloud Orchestrator, unattended robots can now retrieve Windows credentials directly from a credentials vault using the Disconnected proxy, instead of going through Orchestrator.

Find out more in the [Orchestrator Credentials Proxy](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/orchestrator-credentials-proxy-installation) documentation.

**New connection messages**

With this release, we have improved the troubleshooting experience of connection errors by adding a specific code to each error.

Additionally, we have compiled a list of the most common connection errors, their cause, and resolution.

**Updated loading states**

Starting with the 2023.10 release, new loading states can be seen in the Assistant interface, including the one for installing automations. The Assistant now displays meaningful information, such as the number of activity packages downloaded for an automation, to offer a better understanding of what's going on under the hood.

![docs image](/images/assistant/assistant-docs-image-327205-cad2f339.webp)

**Launch Studio Web from Assistant**

Now, the search bar in Assistant also returns Studio Web Templates, which can act as a starting point for a process you want to automate. If you want to start from scratch, launch Studio Web from the UiPath Products section and create the automation yourself.

Separate installer for Robot and Assistant

A new **UiPathRobot.msi** installer is now available, enabling you to install only Robot and Assistant. The installer does not contain any Studio-related options and is significantly smaller than UiPathStudio.msi, making it easier to install Robot and Assistant.

What you should know:

* You cannot upgrade an older installation performed with UiPathStudio.msi using UiPathRobot.msi.
* Just like in previous releases, you can also use UiPathStudio.msi to install Robot and Assistant.

## Improvements

* Starting with this release, the [Picture in Picture - Virtual Desktop](https://docs.uipath.com/robot/standalone/2023.10/user-guide/pip-virtual-desktop) feature also displays a preview of is happening while the automation runs. This means you no longer have to switch to the virtual desktop to watch the process execution.
* Multiple functional, visual, and accessibility improvements have been added in this release as well.
* If you are installing the attended robot in user mode and your environment is configured to use [SSO with Azure Active Directory](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration), you can now enable automatically signing in to your account during installation.
* The Linux robot image now uses a non-priviledged user.
* The **Disconnect** command line argument now has two additional properties:
  + **--wait** - If there is a job running on the machine, the robot is disconnected only after the job completes.
  + **--force** - If there is a job running on the machine, the job gets killed and only afterwards the robot is disconnected

## Bug Fixes

* An issue causing Workflow Validation to not finish has been resolved.
* An issue causing a 405 Method Not Allowed response when connecting to Orchestrator has been resolved.
* An issue causing the MacOS version of Assistant to show a blank screen has been resolved.
* Some additional visual bugs have been resolved for the UiPath Assistant interface.
* **Erratum - added April 3, 2024:** The following bug was partially fixed in 2023.10.0. A full fix is provided in version 2023.10.5.

An issue causing Assistant to throw the `` Format string contains an unescaped latin alphabet character `n` `` error when running a job has been resolved.

## Known Issues

* On Windows 11 22H2, you cannot run an automation in PiP - Child Session when an automation in PiP Virtual Desktop is running.
* Azure Virtual Desktop multisession VM (Windows 10) does not support PiP.
* Trying to run a package from a network path or an Azure File Share fails with the "`System.Xaml.XamlObjectWriterException: Cannot create unknown type [....]`" error.

## Removals

* Starting with the 2023.10 enterprise release, Windows 8.1 and Windows 2012 R2 are no longer supported.

## Upcoming deprecations

* Starting with 2024.4 enterprise release, TightVNC will be deprecated.
* Starting with 2024.4 enterprise release, Robot JavaScript SDK and Robot API will become deprecated.
  + **Erratum added 23 January 2025**: Initially announced for Studio 2024.4, the deprecation of RobotJS and RobotAPI has been postponed indefinitely.

## Activity Pack Versions

The following activity packages and versions are included in the installer and can be found in the local feed.

| Activity Pack | Version |
| --- | --- |
| UiPath.UIAutomation.Activities | [v23.10.3](https://docs.uipath.com/activities/docs/release-notes-uipath-uiautomation-activities#v23103) |
| UiPath.System.Activities | [v23.10.2](https://docs.uipath.com/activities/docs/release-notes-uipath-system-activities#v23102) |
| UiPath.Excel.Activities | [v2.22.2](https://docs.uipath.com/activities/docs/release-notes-uipath-excel-activities#v2222) |
| UiPath.Mail.Activities | [v1.21.1](https://docs.uipath.com/activities/docs/release-notes-uipath-mail-activities#v1211) |
| UiPath.Word.Activities | [v1.18.1](https://docs.uipath.com/activities/docs/release-notes-uipath-word-activities#v1181) |
| UiPath.ComplexScenarios.Activities | [v1.5.0](https://docs.uipath.com/activities/docs/release-notes-uipath-complexscenarios-activities#v150) |
| UiPath.Presentations.Activities | [v1.12.2](https://docs.uipath.com/activities/docs/release-notes-uipath-presentations-activities#v1122) |
| UiPath.Testing.Activities | [v23.10.0](https://docs.uipath.com/activities/docs/release-notes-uipath-testing-activities#v23100) |
| UiPath.WebAPI.Activities | [v1.18.0](https://docs.uipath.com/activities/docs/release-notes-uipath-web-activities#v1180) |
| UiPath.Form.Activities | [v23.10.3](https://docs.uipath.com/activities/docs/release-notes-uipath-form-activities#v23103) |
| UiPath.Callout.Activities | [v23.10.3](https://docs.uipath.com/activities/other/latest/user-guide/release-notes-uipath-callout-activities#v23103) |