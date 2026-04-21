---
title: "Script"
visible: true
slug: "script"
---

The **Script** activity uses JavaScript to enable custom data manipulation within your workflow. It integrates into API workflows, allowing you to:

* Extract, format, and restructure API responses.
* Aggregate and consolidate data.
* Perform calculations and data transformations.
* Standardize data formats for later steps.
* Run within the workflow execution context, accessing only existing workflow data and step outputs.

Use the **Script** activity to refine nested or fragmented API responses before passing them to subsequent workflow activities.

## Known limitations

* You cannot make API calls using the **Script** activity. Use the **HTTP request** activity instead.
* JavaScript code execution has a timeout of 30 seconds.

## Using the Script activity

To add a **Script** activity to your workflow:

1. On your API workflow designer canvas, select the plus (+) icon. The **Add activity** menu appears.
2. Select **Script**.
3. In the **Properties** panel, expand the Expression editor, then write your JavaScript logic in the **Code** panel.
4. Debug the workflow to execute the activity and generate output fields for later use.

For optimal usage, use the following recommendations:

* Use the `return` statement to efficiently structure JSON outputs.
* Use `.map()` to transform arrays into structured objects.
* Use Autopilot expression generator to automatically generate JavaScript based on workflow context, minimizing manual coding effort. For example: "I fetched responses from 3 HTTP calls, merge them into a JavaScript object".

## Script activity example

The following example consolidates data from multiple workflow steps into a structured JSON object using the **Script** activity. This approach is especially helpful with Workday APIs, which often require several endpoint calls to retrieve complete datasets, such as employee details, managers, and direct reports.

The following image shows the original workflow, which is going to be consolidated into a JSON object with the Script activity.
  ![Workday workflow](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/582850)

Open the **Debug configuration** window, then paste and save the following JSON syntax:

```
{
  "first_name": "Betty",
  "last_name": "Liu"
}
```

1. On your API workflow designer canvas, add a **Script** activity.
2. Open the Expression editor and paste the following implementation:
   ```
   return {

       // Details on the worker
       worker: {
           name: $currentItem.descriptor,
           email: $currentItem.person.email
       },

       // Details of their manager
       manager: {
           name: $context.outputs.Workers_3.content.descriptor,
           email: $context.outputs.Workers_3.content.person.email
       },

           // Details for their direct reports
       reports: $context.outputs.Workday_REST_HTTP_Request_4.content.data.map(report => ({
           name: report.descriptor,
           email: report.primaryWorkEmail
       }))
   }
   ```

Pay attention to the following areas in this example:

* Using `$context.outputs` to retrieve data from previous API calls.
* Using `.map()`to transform arrays into structured lists of reports.
* Combining multiple API responses into a single JSON object.