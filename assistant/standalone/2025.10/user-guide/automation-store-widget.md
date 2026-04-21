---
title: "Automation Store Widget"
visible: true
slug: "automation-store-widget"
---

The Automation Store widget provides users easy access to internal ready-to-go automations available in the Automation Store directly from the UiPath Assistant.

## Prerequisites

To use the Automation Store widget, the following conditions must be met:

* The Assistant must be connected to a tenant that has Automation Store enabled and some automations deployed.
* UiPath Assistant version 2021.10 or later is installed.
* A policy is configured in Automation Ops to deploy this widget to your Assistant.
  :::note
  [Automation Store](https://docs.uipath.com/automation-hub/docs/automation-store) is available only with an enterprise license or under an enterprise trial.
  :::
  :::important
  The Automation Store widget is only available if you are both connected and signed in to an Orchestrator server URL.
  :::

## Installing an Automation

All automations available in the Automation Store can be found on the UiPath Assistant homepage, in the **Automation Store** section. To add an automation to your list of processes, select the automation and click **Install**.
:::important
When the Automation Store Widget is used on MacOS, only cross-platform automations can be run. Automations not built for cross-platform fail with the following error when started: `The process cannot run on macOS because it is not compatible with this platform`.
:::

## Field Descriptions for Automations

Selecting an automation displays additional information about it, as described in the following table.

| Field | Description |
| --- | --- |
| Title | The title of the automation. Clicking the title takes you to the Automation Store webpage for the specific automation. |
| Category | Displays the category of the automation (e.g. HR, Finance, IT). |
| Description | Description of the automation provided by the author. |
| Rating | The average rating of the automation based on user feedback. |
| Reviews | The total number of reviews. |
| Author | The name of the person who built the automation. |
| Number of downloads | How many people downloaded the automation. |
| Avg savings a month | How many hours, on average, the automation saves the business user. |
| Media | Media provided by the author for the automation, if available. |
| Applications | What applications are used in the automation (e.g. Excel, Outlook). |
| Send a review or question | Click this link to go to the Automation Store webpage where you can add a review or a question about the automation. |
| Tags | This section displays custom tags added for the automation. |

## Updating an Installed Automation

If an update is available for an automation added from the Automation Store, the **Update** tab is displayed when you select the automation from the list. Select the **Update** tab and then click the **Update** button to get the latest version.

## Sharing an Idea in Automation Hub

If you know of a repetitive task or a process that could be automated, you can easily go to Automation Hub and [share your idea](https://docs.uipath.com/automation-hub/docs/submit-an-idea) directly from the Assistant by clicking the **Submit an Idea** tile from the Launchpad.

This opens a questionnaire in Automation Hub that enables you to add details about your automation idea and submit it for review.

You can enable or disable the "Automation Hub: Submit an Idea" menu from the **Launchpad** section in the **Preferences** menu in the UiPath Assistant.

## Deploying the Automation Store Widget

Just like for any other widget, the Automation Store Widget deployment is handled through Automation Ops policies.

## Searching Related Automation Hub Ideas

When the Automation Store Widget is deployed, the search functionality in Assistant also returns related ideas part of Automation Hub, but not deployed in the Automation Store.