---
title: "Referencing a Process From Orchestrator"
visible: true
slug: "connecting-your-app-to-an-orchestrator-tenant"
---

UiPath Apps offers the the ability to connect an app to an automation process. Your app can be used as an interface for providing inputs to the process or as a visual canvas to display outputs to your users.

:::note
When sending a DataTable from one process to a second process using Apps, the columns order in a row may not be same.
:::

## Referencing a Process From Orchestrator

Once a process has been published to Orchestrator, you can reference that process from an app.

The following example shows you how to add a published process to an app:

1. From an existing app in App Studio, expand the dropdown menu at the right of the **Add control** button.
2. Select **Process**.

   ![docs image](/images/apps/apps-docs-image-293118-9abb60ff.webp)
3. A list of tenants for the current account is displayed. Select the tenant that hosts the process you need to reference, then click **Next**.

   ![docs image](/images/apps/apps-docs-image-292082-1d70b9bb.webp)
4. The **Add process** wizard opens, displaying the list of processes in the selected tenant, grouped by folders.
5. Select one or more processes. The right-hand panel displays the description, and the input and output arguments of the highlighted process.

   ![docs image](/images/apps/apps-docs-image-293131-e6a49975.webp)
6. Check the box next to the process you want to use in your app and click **Add**.
   :::note
   Process permissions are managed in Orchestrator. Make sure you have the right permissions for the process you want to add from Orchestrator. For specific setup instructions, check out [Managing Roles](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-roles) in Orchestrator.
   :::
   :::important
   By default, App Studio does not recognize the fields of a .NET object used as an input/output argument for your process (for example, a DataTable object). To allow App Studio to identify these fields:
   * **Run your process** before adding it to your app. Apps checks the job history and automatically detects the schema/fields of the .NET object.
   * **Manually specify object fields** for process input/output. If your process has no job history, then after you add it to your app, you must manually specify
   its fields. Be aware that manually added parameters are removed when the process is refreshed.
   :::

## Updating a referenced process

To update a referenced process whose workflow was changed, follow these steps:

1. From the **Processes** section in the tree view, select the process you want to update.
2. Click on the **Refresh process** icon.

   ![docs image](/images/apps/apps-docs-image-303139-4c886a8e.webp)

Refreshing the process retrieves the most recent bindings. However, some of the new bindings may throw errors which need to be manually resolved.

## Binding Process Inputs/Outputs Arguments

To bind an input or output argument to a control or rule using the **Expression editor**, use the following syntax:

```
Processes.[Process_name].[name_of_the_argument]
```

To identify the list of input and output arguments of a process, select it from the **Processes** list on the left-side panel:

![docs image](/images/apps/apps-docs-image-294458-c0575198.webp)

:::note
Make sure the process is referenced in your app.
:::

## Launching a Process

The following example shows how to start a process when a Button control is clicked. You can use the events of any control.

1. In your app, add a **Button** control.
2. Select the **Button** control, go to the **Events** tab, and click **Create rule**. The wizard for configuring rules opens.

   ![docs image](/images/apps/apps-docs-image-293159-85f33d9a.webp)
3. From the dropdown, select the **Start process** rule.

   ![docs image](/images/apps/apps-docs-image-293163-237e5723.webp)
4. Click the **What process to start** field. The **Resources** panel opens, displaying the list of available processes.
5. Select the process you want to start by double-clicking it.
   :::note
   By default, processes run in the attended mode. To run the process unattended, select the **Unattended** option. ![docs image](/images/apps/apps-docs-image-293167-e25a5736.webp)
   :::
:::important
* An Orchestrator
account cannot consume more than 100 unique unattended processes across all of the public apps they use during their account lifetime.
* For cloud Orchestrator instances and non-public apps, the limitation does not apply.
:::

## Interim Process Result

To use a **UiPath<sup>®</sup> Studio Activity**, the following environment must be set up:

* UiPath<sup>®</sup> Studio v2022.4 + with UiPath<sup>®</sup> Robot v2020.10+
* The `UiPath.WorkflowEvents.Activities` package is installed