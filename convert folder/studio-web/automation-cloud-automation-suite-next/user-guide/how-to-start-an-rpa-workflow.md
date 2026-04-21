---
title: "How to start an RPA workflow"
visible: true
slug: "how-to-start-an-rpa-workflow"
---

A key step in designing an RPA workflow is deciding what will trigger the workflow. Each project contains one trigger which is the first activity in the main workflow. You select how an automation will start when you create a new project. When you create a project from a template, the template already contains the trigger.

Automations can be triggered in one of the following ways:

* **Manually** - The automation runs when you manually start it. When you select the option **Manual automation**, a [Manual Trigger](https://docs.uipath.com/activities/other/latest/user-guide/manual-trigger) activity is added to the workflow. This is the default trigger for automations.
* **On a schedule** - The automation runs at specified times according to a specified schedule. When you select the option **Scheduled automation**, a [Time Trigger](https://docs.uipath.com/activities/other/latest/user-guide/time-trigger) activity is added to the workflow. Use this type of trigger for automations that should run on a fixed schedule, for example when you need to upload a report weekly to an online file share. You configure the schedule from the activity.
* **By an event** - The automation runs when a specified event occurs in an application, for example when an item such as a file or record is created or updated, or when an email is received. Choose the application and then the event that triggers the automation, and the corresponding trigger activity is added to the workflow.

After the project is created, configure the trigger activity from the project designer so that the automation starts exactly when you want it to. For example, if you're using a time trigger, configure its schedule, if you're using an event trigger such as when an email is received, configure a filter to ensure the automation is triggered only by the right emails.

After you publish the project, you can [manage the trigger from Orchestrator](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-package-requirements).

## Testing the trigger

When you test a project that uses a manual or time-based trigger, the project starts as soon as you initiate the run.

When an event trigger is used, the robot tries to find a recent item that matches the configuration of the trigger. You can test your event trigger before running a project using the option available in the trigger activity. This checks whether there are any items that match the current setup of the trigger.

  ![docs image](/images/studio-web/studio-web-docs-image-372555.webp)

Information about the trigger test is displayed in the **Output** panel, including the properties and resulted test values of any item that is found. This data is then also displayed in the variable selection window when you select the output variable for the trigger in other activities in the project. The data is immediately available for use when reopening a project and is user-specific. If no item is found, you can:

* Expand the search to increase the time interval by selecting a time option from the drop-down menu. You can then test your trigger again using the new interval.
* Select a suggested non-matching item from the drop-down menu.

For example:

* To test an [Email received](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-trigger-new-email-received) trigger in Gmail with a specific filter set up, send yourself an email that matches the filter.
* To test a [File created](https://docs.uipath.com/activities/other/latest/user-guide/office365-trigger-new-file-created) trigger in Microsoft OneDrive with a specific filter set up, create a file that matches the filter.

## Changing the trigger in a project

To change the trigger in a project, on the trigger activity, select **Actions** ![docs image](/images/studio-web/studio-web-image-More_VT.png) &gt; **Change trigger**. The four most frequently used trigger categories appear in the first row of the trigger selection window.

  ![docs image](/images/studio-web/studio-web-docs-image-337084.webp)