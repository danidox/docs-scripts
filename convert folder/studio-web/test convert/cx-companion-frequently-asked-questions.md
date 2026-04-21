---
title: "Frequently asked questions"
visible: true
slug: "cx-companion-frequently-asked-questions"
---

## What is CX Companion and what does it do?

CX Companion is a productivity tool designed for contact center representatives. It is offered as a fully customizable Apps in Studio Web solution template. This tool unifies customer context with AI agents, automations, and custom apps, all seamlessly deployed within the UiPath platform, enhancing efficiency and streamlining workflows.

It can be used as an embeddable interface for platforms like Salesforce (supported out of the box) or it can be used standalone, enabling contact center reps to view, run, and track automations, apps and AI agents based on the context of incoming calls or requests.​

## What are the typical use cases for CX Companion?

CX Companion is a versatile tool that can be applied across various industries, primarily focusing on contact center and service desk use cases, but its adaptability makes CX Companion suitable for a wide range of business needs.

* It can integrate seamlessly with host systems like Salesforce for service desk scenarios, enabling contact/service desk representatives to view and execute deployed automations, apps and AI agents.
* Alternatively, it can function as a standalone application, offering flexibility to address use cases beyond contact center and service desk operations.

## Where can I find the CX Companion template?

CX Companion is available as an Apps in Studio Web solution template in [UiPath Studio Web](https://studio.uipath.com/templates) and in the [UiPath Marketplace](https://marketplace.uipath.com/products/studio-web). It is available only in Automation Cloud, Automation Suite is not currently supported.

## How is CX Companion authenticated?

CX Companion uses the UiPath authentication in embedded or standalone mode.

## How is CX Companion integrated in the host environment? (e.g. Salesforce)?

CX Companion comes with an out-of-the-box integration with Salesforce. However, CX Companion does not restrict integration with any third party system.

Two components are available to enable the integration with Salesforce:

* CX companion comes with a downloadable [UiPath SDK (NPM Package)](https://www.npmjs.com/package/@uipath/apps-communication-driver) which includes a communication driver that allows passing the call context from Salesforce to the CX Companion app embedded in Salesforce via an iframe within the Salesforce Light Weight Component (LWC). With the release of CX Companion, we introduced the concept of [external events](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/set-an-external-context-using-external-events). External events are custom cross-window communication messages that enable secure data exchange between parent windows (e.g. Salesforce) and embedded apps (CX Companion) in child windows (iframes). At runtime, this enables apps to listen for configured external events and execute the associated automations.
* The UiPath [CX Companion Salesforce Plugin](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/cx-companion-salesforce-plugin#cx-companion-salesforce-plugin) listed on [Salesforce AgentExchange](https://agentexchange.salesforce.com/) enables the out-of-the-box integration of CX Companion with Salesforce when using external events. It allows the CX Companion app to render in the LWC iframe.
  1. Identify the URL where CX Companion is hosted.
  2. Set up a trusted URL.
  3. Modify custom metadata types.

## Why is the version 2.0 for CX Companion?

CX Companion 1.0 was the initial version of this tool, released in 2024. CX Companion 2.0 is the latest iteration, developed using UiPath Apps in Studio Web. The new version introduces enhanced functionality, leveraging the capabilities of Studio Web to provide a more robust and versatile app template. The version number reflects this significant upgrade.

## How is CX Companion licensed?

* **For Pricing v2** (already available) - Basic SKU for runtime users and Pro or Plus for developer license (to modify the template).
* **For Flex pricing** - Continue to use it based on the use case with respect to using automations, apps, and agents.

## What are the prerequisites for using CX Companion?

* CX Companion itself does not require any special license. However, appropriate UiPath licenses are required to run automations, agents, and apps via the CX Companion, depending on the specific business use case being addressed.
* CX Companion supports two operational modes:
  + **Unattended mode** - Designed to execute only unattended automation processes.
  + **Attended mode** - Allows execution of both attended and unattended automation processes. To run actions in attended mode, CX Companion requires UiPath Assistant version 2025.0.167 or later.
* Ensure your business use case aligns with the appropriate mode and licensing requirements before deploying CX Companion.
* If you are planning to view and launch deployed UiPath Apps, the UiPath Apps connector in Integration Service must be configured.

## Does CX Companion store any data?

No, CX Companion is an Apps in Studio Web template and serves as an interface for your deployed UiPath automations, apps, and agents. It does not store any data on its own.

## Does CX Companion generate any logs?

CX Companion captures logs within the app workflow, which can be viewed in the Orchestrator job logs for the CX Companion app process (code-behind workflow). These logs are useful for identifying issues in case of exceptions.

## What are the limitations of CX Companion?

* It will take 3.5 - 4 sec to start the web app (serverless code behind) when using medium-sized robots. Other processes will start only after this initial load time.
* Safari browser is not officially supported by Apps. Apps supports Google Chrome, Microsoft Edge, and Mozilla Firefox​.
* Apps is only browser-based; there is no native mobile support​.
* End users of CX Companion cannot switch language (e.g. English to German). Apps can be created in multiple languages at design time.​
* No attended automations possible on iOS devices from UiPath Assistant.​
* CX Companion is available only in Automation Cloud. CX Companion uses Apps in Studio Web, and it is not supported in Automation Suite at this time.​
* No automatic Companion template migrations or upgrades. CX Companion is shipped as an app template, upgrading to a higher version of Companion must be performed manually.​
* Apps runtime is not fully accessibility compliant.

## Where should I report issues or request enhancements for CX Companion?

You can report any issues or submit enhancement requests through the [Customer Portal](https://customerportal.uipath.com/).