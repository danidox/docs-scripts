---
title: "Widgets"
visible: true
slug: "widgets"
---

A Widget refers to a plug-in integrated with the UiPath Assistant holding a specific functionality.

The procedure to download a Widget goes through the following steps:

1. UiPath Assistant reaches out to Automation Ops to fetch the Governance Policy.
2. The UiPath Assistant looks in the Orchestrator Library Feed for the requested Widget.
3. If the Widget is not found there, the Official NuGet Feed is used.
   :::note
   If both feeds are allowed, the UiPath Assistant prioritizes the Orchestrator Library Feed over the Official NuGet Feed.
   :::
4. Widget is downloaded and added to the UiPath Assistant.

   ![docs image](/images/assistant/assistant-docs-image-102799-cd346eb7.webp)
:::note
* Any error encountered related to a widget is displayed in the widget sections.
* In order to see a new widget, you need to Quit and restart the UiPath Assistant or sign out and sign back in.
:::