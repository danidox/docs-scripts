---
title: "Running a project"
visible: true
slug: "running-a-project"
---

You can debug your projects by running them directly from the workflow designer.

Projects run on the robot type selected for your account. By default, automations run on [Automation Cloud™ - Serverless](https://docs.uipath.com/orchestrator/v0/docs/automation-cloud-robots-serverless) robots. For more information, see [unattended robot setup](https://docs.uipath.com/orchestrator/v0/docs/enabling-users-to-run-automations-on-unattended-infrastructure-via-unattended-robots).

You can also use your local machine to run your projects by expanding the drop-down menu next to the debug button and selecting the **On local machine** or **On cloud** options.

Note that debugging locally requires you to install and run UiPath® Assistant 2024.10.5 or newer. If UiPath Assistant is not installed on your machine, you are prompted to download it when you choose to test on your machine. You also need to be signed in to Assistant and Studio Web using the same user name and within the same organization and tenant.

The options for running a project are:

* **Debug on cloud** or **Debug on local machine** - The entire project is run, starting with the main workflow. When you run the project, you can select **Stop** to stop the execution and return to the project.
  :::tip
  If you want an automation to pause before a certain activity, add a breakpoint to that activity. For example, you may want to check the results of the steps in a workflow up to a certain point before continuing with the execution. To add a breakpoint, select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Add breakpoint** for that activity. When the breakpoint is reached, the workflow pauses, and you can either stop execution, continue running the rest of the workflow, or continue running the workflow step by step.
  :::

As the project runs, an hourglass icon is displayed at the top of the activity that is currently executed. The icon turns to a green checkmark when the activity was run successfully. If an error occurs when executing an activity, execution stops, a red error icon is displayed at the top of the activity, and the activity header is also highlighted in red. Hover over the icon to see the error message with the cause of the error.

  ![docs image](/images/studio-web/studio-web-docs-image-398565.webp)
* **Debug step-by-step** - The project runs one activity at a time, starting with the main workflow, allowing you to validate each step along the way. The following options are available when you run step-by-step:
  + **Stop** - Stops the execution and returns to the project.
  + **Continue** - Runs all remaining steps or until the first breakpoint is reached.
  + **Next Step** - Runs only the next step.

You can view details about the progress of each run in the [Run output](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/viewing-the-run-output) panel.
:::tip
To make it easier to follow the progress of the execution and view information about the outcome of activities, add **Write Line** or **Log Message** activities at certain points in your projects. These activities display messages in the **Run output** panel and can be configured to include the output of previous activities in the messages. For example, in a project that contains a number of activities that process a spreadsheet, you can add a Write Line activity after the last of the activities and configure it to display the message **Finished processing *FileName*** where the file name can be populated dynamically using the output of a previous activity that retrieved the spreadsheet.
:::

In projects that contain multiple workflow files, **Test** and **Test step-by-step** run the main workflow regardless of the workflow you are currently working on.

To debug a specific workflow in your project, right-click the workflow file in the **Project explorer** and select:

* **Debug** to run the entire workflow.
* **Debug step-by-step** to run the workflow one activity at a time.

## Watching variables when debugging a project

When you're debugging a project step by step, you can follow the values of variables, arguments, and expressions as the workflow runs by selecting **Open watches panel** ![](/images/studio-web/studio-web-image-watches.png) on the right of the workflow designer. Watching values can be helpful in identifying potential issues.

Variables and arguments are automatically added to the watches. You can expand the entries for variables and arguments that have multiple properties to view the values of the available properties.

To add a watch:

1. Select **Open watches panel** ![docs image](/images/studio-web/studio-web-image-watches.png) on the right of the project page.
2. Type a value in the provided text box and press **Enter**. As you start typing, autocomplete suggestions are displayed.

Internal trigger event values (such as `UipathEvent` or `UipathEventObjectType`) are not displayed as local variable values in the Watches panel. However, these values are available in the [Expression Editor](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/configuring-activities#expression-editor).

If you are using an Orchestrator event trigger to start an automation (as opposed to a trigger which is explicitly set in the workflow), you can only access its event trigger data in the Expression Editor. To learn more about Orchestrator triggers, see the [Orchestrator guide](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-triggers).