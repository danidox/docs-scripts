---
title: "Rule: Add to Queue"
visible: true
slug: "rule-add-to-queue"
---

Use the **Add to Queue** rule to add a new queue item in Orchestrator.

![docs image](/images/apps/apps-docs-image-330207-24fce053.webp)

## What queue to use

Clicking the **What queue to use** field opens the **Resources** panel, which displays the available queues.

Select the queue you want to use by double-clicking on it. Once selected, the following properties become available:

* Input Override
* When successfully added to queue
* When queue item addition failed
* Other properties
* Wait for queue item results
* When item transaction started
* When item transaction is successful
* When item transaction failed

## Input Override

In this section you can set values for the input arguments of the queue.

Clicking the **Input Override** filed opens the **Resources** panel, which displays the available input/output arguments of the selected queue.

Select the input arguments, and set their values as the values of the input controls in your app.

The input argument of the queue has the following syntax:

`Queues.<queue_name>.<input_argument_name>`

The value expression of the Apps control has the following syntax:

`<Apps_MainPage_name>.<input_control_name>.value`

**For example:** You have an input argument in your queue called "employer_name". You have a text control in your app called "text1". To bind the queue argument to the control value in Apps, write the following expression in the **Enter value** field: `MainPage.text1.Value`.
:::note
When the queue inputs are linked to control values, these values are automatically passed into the queue when it starts.
:::

## When successfully added to queue

In this section you can define rules to be executed right after the item is added to the queue.

**For example:** You can display a success message after the item is added to the queue using the **Show Message** rule and selecting **Success** from the **Type** dropdown.

## When queue item addition failed

In this section you can define rules to be executed when the addition of an item to the queue failed.

**For example:** To track the failure, you can add a **Show Message** rule. You can then specify the title, message, and type of the error.

## Other properties

In this section you can configure how to process queue items:

**Priority** : The processing priority level of the queue item.

Can be set to **Low**, **Normal**, or **High**.

**Normal** by default.

The priority is only editable for queues with **disabled** SLA predictions. If SLA predictions are enabled, the priority is set to **High** by default.

**Postpone by (*)** : The number of hours (in decimals) the processing of the queue item should be postponed.

**Deadline on (*)** : The number of hours (in decimals) during which the processing of the queue item should be completed.
    :::note
    The counter starts as soon as the item is added to queue.
    :::

**Reference** : The custom identifier you added to a transaction or a group of transactions.

The reference can be unique, depending on what you chose in the **Unique Reference** field when you created the queue.

(*) You can specify a date by binding the value of a **Date Picker** control or a process output parameter.

## Wait for queue item results

By default, the process adds the queue item and executes the rules that follow the current **Add to queue** rule.

To wait until the item added to the queue is successfully proceesed or failed, select the **Wait for queue item results** box.

## When item transaction started

In this section you can define rules to be executed right after a queue item is being picked up for processing.

**For example:** You can display a message to inform users that the transaction started using the **Show Message** rule.

## When item transaction is successful

In this section you can define rules to be executed when the transaction completes successfully.

**For example:** You can display a success message after the transaction completion using the **Show Message** rule and selecting **Success** from the **Type** dropdown.

## When item transaction failed

In this section you can define rules to be executed right when the transaction fails.

**For example:** To track the failure, you can add a **Show Message** rule. You can then specify the title, message, and type of the error.

## Rule output properties

* **Error -** references the error message shown if the job fails.