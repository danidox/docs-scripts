---
title: "Response"
visible: true
slug: "response"
---

The **Response** activity terminates an API workflow and sends a structured response to the requester. The response typically includes a status and additional data.

Use the **Response** activity to:

* Always return the correct status and response details.
* End workflows with a clear and structured result.
* Handle errors gracefully, especially when combined with the **Try/Catch** activity.

The **Response** activity should be the final step in a workflow, to ensure the process provides the intended information.

:::note
Currently, schema validation is not enforced, so if the data returned in the **Response** activity includes more or fewer properties than those defined in the output schema, the workflow does not fail.
:::

## Best practices

* Always configure your **Output schema** in the **Data manager** before adding a **Response** activity. When you define the schema first, the system automatically suggests aligning your **Response** activity with it.
* Use a **Response** step when your calling party, such as Maestro or an agent, expects a response.
* You can skip adding a **Response** when you are building system-to-system integrations or an unattended automation.

## Using Response activity

To add a **Response** activity to your workflow:

1. On your API workflow designer canvas, select the plus (+) icon. The **Add activity** menu appears.
2. Select **Response**.
3. In the **Properties** panel, configure the following fields:
   * **Mark job as failed**—Turn this option on mark the entire workflow as failed. This is useful for explicitly signaling that a logical error occured, even if no technical exception was thrown.
   * **Response**—Use the Expression editor to define a JSON object containing the desired response information. You can also provide a static value or a variable.
4. **Save** the configuration.

## Response activity example

The following example retrieves a worker from Workday and aggregates details about their manager and direct reports.

The following image displays the example workflow:

   ![Workday workflow](/images/studio-web/studio-web-workday-workflow-583220.webp)

### The Failure response

The workflow returns a **Failure** status with an error message if any retrieval step fails.

To achieve this:

* Wrap the retrieval steps inside a **Try/Catch** block.
* If an error occurs, the **Error Response** step in the **Catch** flow returns a structured failure response.

Configure the **Response** with the following details:

* **Type**—Failure
* **Details**—Open the Expression editor and write the following:
  ```
  ({
      "error_message": $context.outputs.Try_Catch_3.error.title,
      "status": $context.outputs.Try_Catch_3.error.status
  })
  ```

Here, `$context.outputs.Try_Catch_3.error` provides a structured error output from the **Try-Catch** activity. When the **Try** flow encounters an error during execution, the workflow returns the following output:

![Failure response output](/images/studio-web/studio-web-failure-response-output-583225.webp)

### The Success response

The workflow returns a **Success** status with the aggregated worker information. The **Search Workers by Name or ID** activity returns an array, even when ther is only one match. There, we use a **For Each** activity to process each result, and then consolidate the data using a **Script** activity.

Configure the **Response** with the following details:

* **Type**—Success
* **Details**—Open the Expression editor and write the following:
  ```
  ({
      "workers": $context.outputs.For_Each_2.results
  })
  ```

Here, `workers` contains the aggregated output from the **Script** step of the **For Each** loop. The workflow returns the following output:

![Success response output](/images/studio-web/studio-web-success-response-output-583255.webp)