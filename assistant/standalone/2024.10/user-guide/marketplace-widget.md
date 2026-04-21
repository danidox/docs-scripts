---
title: "Marketplace Widget"
visible: true
slug: "marketplace-widget"
---

The UiPath Marketplace Widget provides an easy way for business users to access ready-to-go automations that are published in the [UiPath Marketplace](https://marketplace.uipath.com/). With multiple reusable listings covering numerous industries and use cases, you no longer need to build everything from scratch over and over again.

All of this is available in the UiPath Assistant through the Marketplace Widget.
:::important
UiPath Assistant v2021.10 and newer is needed to use the Marketplace Widget.
:::

The Marketplace Widget is enabled by default for all UiPath Assistant v2021.10 users, and appears in the UiPath Assistant as a new tab in the header.

## Installing Automations from Marketplace

In order to use an automation from the Marketplace, you need to go to the Marketplace Widget tab, select the automation you want to use and click on Install.

The automation gets added to your Personal Workspace in Orchestrator and you'll be able to run it just like any other automation.
:::important
The Marketplace Widget makes use of the Personal Workspace configured in Orchestrator to install automations. The Personal Workspace is required and needs to be enabled for the user.
:::
:::note
The Marketplace Widget is available for offline users to browse for ready-to-go automations, but they must Sign In in order to install any of them.
:::

## Updating Marketplace Automations

When a new version of an automation gets published in Marketplace, a note appears under the automation name and you are able to install the update directly from the UiPath Assistant by opening the Details Panel and clicking on **Update**. The change is also pushed to the Orchestrator Personal Workspace.

In the Automation Details panel, a new tab describes what's included in the updated version.

## Sorting Automations

In the Marketplace widget, the list of ready-to-go automations can be sorted by the following options:

* Recommended (Default).
* Alphabetical.
* Rating.
* Most Downloaded.
  :::note
  This feature is available starting with Marketplace Widget 1.2.0 which is compatible with UiPath Assistant 2021.12 version and higher.
  :::

## Details Panel

## Field Descriptions

Selecting an automation opens the details panel where you can find additional information such as:

* Title (clicking on the title opens the automation page in Marketplace in a browser window)
* Automation Description
* Reviews (rating and user reviews)
* Number of Downloads
* Author
* Last Update Date
* Media: Videos & Images
* Compatibility
* License
* Dependencies
* Supported by Publisher
* Documentation
* Feedback (Write a review, Ask a question)
:::note
Depending on the automation, some fields might not be available.
:::

## Actions

* Install
* View
* Update
  :::note
  If an automation is already installed, the **Install** button changes to **View**. If an automation has a new version published in Marketplace, the **Update** button is displayed.
  :::

## Configuring Input Parameters

Automations that use configurable parameters can be edited from the details panel of the UiPath Assistant.

## Deploying the Marketplace Widget

Just like the [Apps Widget](https://docs.uipath.com/assistant/standalone/2024.10/user-guide/apps-widget), the deployment of the Marketplace Widget is handled through Automation Ops Policies.
:::note
In order to not display the Marketplace Widget to users, you need to create and deploy a policy that disables the Marketplace Widget (*Is Enabled* set to *No*). In the scenario where Automation Ops is not used, you must modify the local file as described [here](https://docs.uipath.com/assistant/standalone/2024.10/user-guide/widgets).
:::

To filter the content displayed in the Marketplace Widget, enable the 'Only UiPath content' check box. This will show only the automations produced by UiPath.

  ![docs image](/images/assistant/assistant-docs-image-102607-96e9787a.webp)

## Disabling the Marketplace Widget

## Through Automation Ops

The Marketplace Widget can be disabled through Automation Ops by removing the check from the "Is enabled" checkbox in the policy.

  ![docs image](/images/assistant/assistant-docs-image-102458-e515bf33.webp)

## Without Automation Ops

## On Windows

If you aren't using Automation Ops, you must add the `UIPATH_DISABLE_MARKETPLACE_WIDGET` environment variable on the client machine with the value set to `True`.

## On MacOS

To disable the Marketplace widget on MacOS, run the following command to set the `UIPATH_DISABLE_MARKETPLACE_WIDGET` variable on the machine: `launchctl setenv UIPATH_DISABLE_MARKETPLACE_WIDGET TRUE` .
:::important
The `UIPATH_DISABLE_MARKETPLACE_WIDGET` environment variable overwrites the Automation Ops policy.
:::