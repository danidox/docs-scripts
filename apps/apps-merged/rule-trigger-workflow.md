---
title: "Rule: Trigger workflow"
visible: true
slug: "rule-trigger-workflow"
---

Use the **Trigger Workflow** rule to invoke a specific.xaml file in an attended automation.

![docs image](/images/apps/apps-docs-image-281968-ec53fa27.webp)

:::important
The **Trigger Workflow** rule helps improve data transfer between Apps and attended robots. To leverage the instant communication with the UiPath Robot, you must use Studio projects that were designed using the **[Apps-Workflow Communication](https://marketplace.uipath.com/listings/apps-workflow-communication-template)** template available in UiPath Studio. If the process is not running, the first instantiation of the **Trigger Workflow** rule starts the process through Robot JS, opening the communication channel between UiPath Apps and UiPath Robot.
:::

## Workflow file

Clicking the **Workflow file** field opens the **Resources** panel, which displays the available processes and their workflow files.

:::important
The panel lists only the .xaml files that were marked as entry points in the UiPath Studio project.
:::

Select the workflow which you want to execute when the control is operated. Once selected, the following properties become available:

* Input Override
* When started
* When completed
* Errors

## Input Override

In this section you can set values for the input arguments of the workflow.

Clicking the **Input Override** field opens the **Resources** panel, which displays the available input/output arguments of the selected.xaml file.

Select the input arguments, and set their values as the values of the input controls in your app.

The input argument of the workflow has the following syntax:

`Processes.<process_name>.<selected_xaml_file>.<input_argument_name>`

The value expression of the Apps control has the following syntax:

`<Apps_MainPage_name>.<input_control_name>.value`

**For example:** You have an input argument in your Studio workflow called "argument_1". You have a text control in your app called "text1". To bind the workflow argument to the control value in Apps, write the following expression in the **Enter value** field: `MainPage.text1.Value`.

## When started

In this section you can define rules to be executed right after the execution of the workflow starts.

**For example:** You can show a spinner icon in this section, and then hide the spinner in the **When completed** section for workflow that take longer to execute.

## When completed

In this section you can define rules to be executed after the execution of the workflow completes.

**For example:** For workflows that take longer to execute, you can show a spinner icon in the **When started** section, and hide it in this section.

## Errors

In this section you can define rules to be executed when the workflow encounters an error.

**For example:** To track the failure, you can add a **Show Message** rule. You can then specify the title, message, and type of the error.

## Rule output properties

* **Error -** references the error message shown if the job fails.
* **JobStatus -** references the status of the job.

## Sample project

To make it easier for you to observe the instant communication between UiPath Apps and UiPath Robot, we have prepared a sample project. Proceed with the following steps:

1. [Download the sample project](https://documentationexamplerepo.blob.core.windows.net/examples/Apps/Real%20Time%20Communication%20between%20Apps%20and%20Attended%20Robot.zip).
2. Unzip it to a folder on your local device. It should contain:
   * `Real Time City Weather Automation` folder - the Studio project
   * `Real Time City Details.uiapp` file - the Apps project
   * `Read Me.txt` file - the project description
3. In Studio, browse for the sample project and open the `project.json` file.
4. Publish the project to your personal workspace in Orchestrator. The corresponding process is automatically created.
5. In Apps, create a new app by importing the Apps project.
6. Replace the referenced process with the one that was automatically created upon publishing the project to your personal workspace.
   :::note
   If you renamed the process when publishing from Studio, replace any binding to match the new name.
   :::
7. Preview your app.
8. Search for a city, then select Enter. Notice how the **City Details** section is instantly updated with information.
9. Click the **Get Weather Details** and the **Get Pollution Details** buttons. Notice how the fields are instantly updated with information.

The first computation takes longer because it is the first instantiation of the job. After that, the job keeps running and instantly returns the results. When you close the Apps session, the job terminates.