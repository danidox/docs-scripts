---
title: "Rule: Start Process"
visible: true
slug: "rule-start-process"
---

Use the **Start process** rule to start the execution of a process.

:::warning
When you use this rule to start an **Unattended** process, select the **Any machine** or **Production machine** templates. Running **Unattended** processes with the **Testing** runtime selection is not supported, and displays the following error message: "No unattended runtimes configured on the machine".
:::

![docs image](/images/apps/apps-docs-image-291032-15c5eff1.webp)

## What process to start

Clicking the **What process to run** field opens the **Resources** panel, which displays the available processes.

Select the process you want to start by double-clicking on it. Once selected, the following properties become available:

* Run Asynchronous
* Type: Attended or Unattended
* Input Override
* When started
* When state changes
* When completed
* Errors

## Run Asynchronous

By default, processes run synchronously, meaning the rules that follow the current **Start process** rule do not execute until the selected process completes.

To run the remaining rules in parallel, select the **Run Asynchronous** box.

## Type: Attended or Unattended

To run the process in unattended mode, select the **Unattended** radio button. By default, the process is set to run in **Attended** mode.

## Input Override

In this section you can set values for the input arguments of the process.

Clicking the **Input Override** filed opens the **Resources** panel, which displays the available input/output arguments of the selected process.

Select the input arguments, and set their values as the values of the input controls in your app.

The input argument of the workflow has the following syntax:

`Processes.<process_name>.<input_argument_name>`

The value expression of the Apps control has the following syntax:

`<Apps_MainPage_name>.<input_control_name>.value`

**For example:** You have an input argument in your Studio workflow called "argument_1". You have a text control in your app called "text1". To bind the workflow argument to the control value in Apps, write the following expression in the **Enter value** field: `MainPage.text1.Value`.
:::note
When the process inputs are linked to control values, these values are automatically passed into the process when it starts.
:::

## When started

In this section you can define rules to be executed right after the execution of the process starts.

**For example:** You can show a spinner icon in this section, and then hide the spinner in the **When completed** section for workflow that take longer to execute.

## When state changes

In this section you can define rules to be executed when the state of the process changes.

The [Report Status activity](https://docs.uipath.com/activities/v1.0/docs/report-status) allows a message to be sent to the Assistant or an app during a process execution.

:::note
The process status only works in the case of attended automation.
:::

## When completed

In this section you can define rules to be executed after the execution of the process completes.

**For example:** For workflows that take longer to execute, you can show a spinner icon in the **When started** section, and hide it in this section.

## Errors

In this section you can define rules to be executed when the process encounters an error.

**For example:** To track the failure, you can add a **Show Message** rule. You can then specify the title, message, and type of the error.

## Rule output properties

* **Error -** references the error message shown if the job fails.
* **JobStatus** - references the status of the job.