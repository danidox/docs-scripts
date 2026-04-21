---
title: "Introduction"
visible: true
slug: "introduction"
---

**UiPath Apps** is a low-code application development tool that enables you to build and share enterprise-grade custom applications that deliver engaging user experiences. Using UiPath Apps, you can quickly build custom business applications that connect to data in any underlying cloud or on-premises system using the power of automation.

Apps built with **UiPath App Studio** provide rich controls for data access and update as well as conditional logic for complex business needs. The underlying UiPath RPA platform provides advanced workflow and business logic capabilities to automate your entire end to end business process.

![docs image](/images/apps/apps-docs-image-92492-da5f057f.webp)

Apps can be designed to run in multiple form factors such as a full-page console, a sidebar, or any other size for either desktop or mobile devices. Since applications are run from a browser, they can run seamlessly from any device.

Further, applications can be wrapped in the Electron framework or other technologies to provide a desktop application experience.

## UiPath Apps

Users see a list of all applications available to them in a single place; they can choose to run the application or share them with other users within their organization.

When a user runs an application, those designed to run automation locally on their desktop will trigger an Attended Robot to interact with back-end systems. Similarly, apps designed to run using unattended automation use Orchestrator to start a job on Unattended Robots.

![docs image](/images/apps/apps-docs-image-92508-651729f7.gif)

## UiPath App Studio

Citizen developers or RPA developers can design their own custom applications in Studio. You can drag and drop a variety of rich controls, configure complex rules, and connect to any RPA process through Orchestrator. Through the use of Attended and Unattended Robots, apps can aggregate and update business data from multiple systems in real-time. Robots connect to any system through our rich set of Activities (Excel, SAP, Salesforce, Microsoft Dynamics, and more) as well as legacy applications, mainframe applications, and VDIs.

Once built, these apps can be published and made available to anyone in your organization with a single click.

## Autopilot in Apps

Autopilot™ is an AI-powered feature which assists users in generating apps using a natural language text prompt, an existing PDF or image, or an existing Data Service entity. You can also add new pages to an app using any of these three modalities. Based on a text prompt, Autopilot™ can also generate VB expressions which can be used in an app.

![docs image](/images/apps/apps-docs-image-435949-0abfdf74.webp)

To find out more about how Autopilot can help accelerate your app development, refer to:

* [Using Autopilot in Apps](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/using-autopilot-in-apps) for an overview of the Autopilot features.
* [Designing your app with Autopilot](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/designing-your-app-with-autopilot) to learn how to design an app using Autopilot.

## Prerequisites

To start using the UiPath Apps platform you first need a UiPath Automation Cloud<sup>TM</sup> account.

To run UiPath Apps, all end-users must be added to your Automation Cloud<sup>TM</sup> account and meet the following requirements in order to run attended/unattended automation:

* **Attended:** UiPath Robot with JavaScript Add-in enabled. Refer to [UiPathRobot.js](https://docs.uipath.com/robot/docs/about-the-robot-javascript-sdk) for installation instructions. End-users must have attended processes used in your app available on their Attended Robot.
* **Unattended:** (one or more of the following)
  + Cloud Orchestrator tenant containing your processes. End-users must have sufficient Orchestrator permissions to run the unattended processes included in your app.
  + Hybrid w/ On-Prem – for details, refer to[Connect your on-premise orchestrator to UiPath Apps Service](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/onprem#connecting-apps-to-an-on-premises-orchestrator-instance).
* All other requirements for Studio, Robot & Orchestrator apply.

Minimum Supported Versions:

* Attended Robot 2019.10
* Orchestrator 2019.10
* Unattended Robot 2019.10
* Studio 2019.10

### Hardware requirements

For the optimal functionality of UiPath Apps, we recommend the following minimum hardware configuration:

|  |  |
| --- | --- |
| UiPath App Studio (for design time) | 8 CPU processor, 16 GB RAM |
| UiPath Apps (for runtime) | 4 CPU processor, 8 GB RAM |

The recommendation is based on a typical scenario where common applications are already running on the device (such as Microsoft Outlook, Microsoft Team, or an antivirus software).

While you can opt for a lower configuration than the recommended one, be aware that some performance degradation may occur.

## Browser Compatibility

UiPath Apps is supported in the latest versions of **Google Chrome**, **Microsoft Edge**, and **Mozilla Firefox**.