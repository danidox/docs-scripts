---
title: "Automation Launchpad"
visible: true
slug: "automation-launchpad"
---

## Overview

**Automation Launchpad** is a UiPath first-party App that provides an out-of-the-box framework that you can use to quickly start and scale your user-facing automation program. Automation Launchpad is built with UiPath’s best practices, and governance procedures in place, to drive frictionless Automation User and Citizen Developer adoption.

## Requirements

### Licensing

**Enterprise Standard** or higher is needed to access Automation Launchpad.

For more information on UiPath licensing, check the [Licensing](https://docs.uipath.com/overview-guide/docs/licensing-levels) pages from the **Overview** guide.

### Technical

The following requirements must be met to implement Automation Launchpad:

* A working Automation Cloud<sup>TM</sup> environment with the following products:
  + Automation Hub
  + Apps
  + Data Service
  + Orchestrator
* 1 unattended license in the target tenant
* UiPath Studio connected to the target tenant

The following requirements are recommended for a smooth Automation Launchpad implementation:

* Use a dedicated attended tenant.
* Provision Automation Launchpad users using Active Directory.

### Set-up and Launch

Automation Launchpad and required artifacts, including the **Implementation Guide**, can be found under the **Resource Center** in Automation Cloud<sup>TM</sup> as a single downloadable file.

  ![docs image](/images/apps/apps-docs-image-92060-42bbb4d1.webp)

The downloaded file contains the following:

* `ALSchema.json`: schema file that needs to be imported into Data Service.
* `Automation Launchpad.uiapp`: app file that needs to be imported into UiPath Apps.
* `AutomationLaunchpadData.1.0.6.nupkg`: package dependency that needs to be imported into Orchestrator.
* `Get_UserMetrics.zip`: exports user metrics stored in Data Service into an Excel file.
* `GetLaunchpadStatistics.zip`: updates Data Service entities.
* `Implementation Guide_Automation Launchpad.pdf`: document that outlines the information needed for Automation Launchpad setup.

## Implementation Options

There are two options for implementation and support in the case of Automation Launchpad.

### Option 1

Automation Launchpad implementation and customization is managed by you. This means that:

* Implementation, customization, and support are not in scope for:
  + UiPath Product Support
  + Technical Account Management or Automation Program Advisory as provided in UiPath's Success Tiers or Premium Support offerings
  + Customer Success Managers
* Automation Launchpad support is solely available through the UiPath Professional Services [Support on Demand](https://docs.uipath.com/marketplace/v4.0/docs/support-on-demand) offering. This offering provides for up to two hours of support for no fee.

### Option 2

This option is strongly recommended, as it uses UiPath Professional Services, using the [UiPath Support on Demand](https://docs.uipath.com/marketplace/v4.0/docs/support-on-demand) offering. This includes:

* Up to 40 hours, and if applicable, existing service credits can be used.
* Install Automation Launchpad app and establish connections to Data Service, Orchestrator, and Automation hub.
* Configure and test the unattended automation.
* Time-permitting and per customer preference, optionally deploy up to eight [Ready-to-go automations](https://marketplace.uipath.com/collections) selected by UiPath.