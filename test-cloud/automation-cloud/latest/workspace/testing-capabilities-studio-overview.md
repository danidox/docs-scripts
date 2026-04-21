---
title: "Studio testing"
visible: true
slug: "testing-capabilities-studio-overview"
---

Studio is our IDE for test automation development. Studio supports both low-code and coded automations to create your test cases:

* **Low-code automations** use a visual interface with drag-and-drop activities, making it accessible for a broad user base.
* **Coded automations** allow you to create automations using code, which is ideal for more complex and collaborative projects. These automations use UiPath services, which are the equivalent of activity packages, coded automation APIs, which are similar to activities, external .NET NuGet packages, and your custom C# classes within Studio.

Studio enables you to create automated test cases in VB or C#, used in CI/CD pipeline scenarios.

* **Application testing** involves test cases and data-driven test cases, along with verification activities from the [Testing.Activities](https://docs.uipath.com/activities/other/latest/workflow/about-the-testing-activities-pack) package, that allows you to create reliable automated tests.
* **Automation testing** covers all the specific test cases and allows you to execute and manage the tests.
* **API testing** works through Postman for calls related to testing and APIs.

For more information on the testing capabilities available in Studio, visit [Studio testing](https://docs.uipath.com/studio/standalone/latest/user-guide/introduction-studiopro).

## Mobile testing

Mobile testing offers you a platform for designing and running device automation without physically using the device. The solution works with various device types and connects to device farms and emulators, allowing you to easily record and automate steps taken on a mobile device. The Mobile Device Manager simplifies device interaction, and the available debugging tools help you in creating effective tests.

The structure of the UiPath mobile testing consists of the following components:

* Mobile Automation activities (**MobileAutomation.Activities**): The specific activities assist you in creating mobile automations by performing tasks like installing and managing apps, retrieving attributes, tapping UI controls, or printing out logs.
* Studio: Serves as the environment for creating the automation workflows for mobile devices.
* Mobile Device Manager (MDM): A tool accessible from Studio that connects to real or emulated devices through Appium. With MDM you can record and perform actions, manage devices and applications, execute tests, and debug them. MDM supports Android, iOS, and Web for emulators and real devices connected through the cloud, your local network, or USB.

Studio, along with mobile automation activities, allows you to create effective mobile tests. Meanwhile, the MDM bridges your actions and the devices to ease the process of mobile testing.