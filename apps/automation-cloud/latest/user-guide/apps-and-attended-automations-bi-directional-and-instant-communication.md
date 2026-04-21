---
title: "Apps and attended automations: bi-directional and instant communication"
visible: true
slug: "apps-and-attended-automations-bi-directional-and-instant-communication"
---

The bi-directional and instant communication between Apps and attended automations addresses the delayed user experience whenever an attended automation is started from Apps. This solution overcomes the time UiPath Robot takes to start up every time your apps starts an attended automation by:

* Decreasing the total execution time.
* Opening a bi-directional communication channel between Apps and the attended robot.
* Keeping the communication channel open for instant responses, until the app session is closed.

This way, Apps starts the process only once, then it invokes the.xaml files associated to different user interactions.

## Components

To leverage the bi-directional and instant communication between Apps and attended automations, use the following activities and rules:

* In UiPath Studio, use:
  + [**Apps request trigger**](https://docs.uipath.com/activities/other/latest/workflow/apps-request-trigger)activity
  + **[Handle apps request](https://docs.uipath.com/activities/other/latest/workflow/handle-apps-request)** activity
  + **[Apps-Workflow communication](https://marketplace.uipath.com/listings/apps-workflow-communication-template)** template
* In Apps, use:
  + **[Trigger workflow](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/rule-trigger-workflow#rule%3A-trigger-workflow)** rule

To get a sense of how these components work together for an instant communication, [see this example.](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/rule-trigger-workflow#sample-project)

## Considerations

Use these guidelines when you create your workflow with bi-directional and instant communication:

1. The **Send Interim Result** activity is not supported by this feature. Avoid adding this activity in the workflows that use the bi-directional communication.
2. In Apps Studio, you need to manually define the properties of complex objects, such as datatables or .net objects. For example, if you are using a data table as an output argument for a process, you must specify the data table column in the process **Details** page.
3. In UiPath Studio, mark the .xaml files invoked by your app as entry points. This way, the .xaml files are displayed in Apps Studio when you reference the associated process.
   :::note
   Apps Studio displays all .xaml files which are marked as entry points, regardless they are part of a workflow that uses bi-directional communication or not.
   :::
4. The bi-directional communication process has to be started by the app that referenced it.
5. If possible, use the **Starts in Background** option for these UiPath Studio projects. This is helpful to have the same app running simultaneously in multiple browser windows, without throwing errors.