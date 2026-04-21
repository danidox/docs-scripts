---
title: "HTTP"
visible: true
slug: "http"
---

The **HTTP request** activity enables you to perform JSON-based API requests within your workflow. You can use the generic HTTP connector or any of the supported Integration Service connectors for authentication, but you also have the option to use the activity without a connection and provide authentication details directly in the request.

The activity provides full control over request configuration, allowing dynamic definition of methods, URLs, headers, and body content. After execution, the response data becomes available for reference in subsequent workflow steps, making it a critical component for interacting with external APIs.

:::note
You can leverage Autopilot to add the HTTP request for you by pasting the desired cURL into the chat.
:::

## Using the HTTP activity

To add an **HTTP request** activity to your workflow:

1. On your API workflow designer canvas, select the plus (+) icon. The **Add activity** menu appears.
2. Select **HTTP**.
3. In the **Properties** panel, configure the following fields:
   * **Authentication**—The type of authentication to use, either **Manual authentication** or **Connector based authentication**.
   * **Connector**—If you selected Connector based authentication, select the connector to use.
   * **Connection**—The connection established in Integration Service. Select an existing connection, click **+ Connection** to add a new connection, or click **Open connections** to manage connections.
   * **Method**—The HTTP method for the request, GET, POST, PATCH, DELETE, PUT, OPTIONS, or HEAD.
   * **Request URL**—The API endpoint for the request. You can dynamically build URLs using the Expression editor. For example, appending an ID retrieved from a previous workflow step. If a Base URL is set, enter a relative path. To override it, use an absolute URL with the same base domain.
   * **Headers**—The request headers as key-value pairs. Headers use a JSON object format and can be generated dynamically with the Expression editor. For example:
     ```
     {
       "Content-Type": "application/json",
       "Accept": "application/json",
       "Authorization": "Bearer jfio**********"
     }
     ```
   * **Query parameters**—The query parameters. Use the **Dictionary editor** to add new parameters.
     + Example: `query value "select * from Vendor"` (for QuickBooks Online).
   * **Body**—Available for all HTTP methods except GET, OPTIONS, and HEAD. Supports JSON-based payloads, allowing you to reference data from previous step outputs using the Expression editor.
4. Debug the workflow to execute the activity and generate output fields for later use.

## HTTP activity example

This following example makes a POST request to HTTPBin, which returns the request data for validation. The request includes dynamic path variables, headers, and a structured request body.

Open the **Debug configuration** window, then paste and save the following JSON syntax in the **Project arguments** section:

```
{
  "id": 12345,
  "name": "John Doe",
  "isActive": true,
  "balance": 2500.75,
  "createdAt": "2025-03-25T12:00:00Z",
  "tags": [
    "premium",
    "verified",
    "active"
  ],
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zipCode": "10001",
    "coordinates": {
      "latitude": 40.7128,
      "longitude": -74.006
    }
  },
  "transactions": [
    {
      "transactionId": "txn_001",
      "amount": 150.5,
      "currency": "USD",
      "timestamp": "2025-03-24T10:30:00Z",
    },
    {
      "transactionId": "txn_002",
      "amount": -75.25,
      "currency": "USD",
      "timestamp": "2025-03-23T08:15:00Z"
    }
  ]
}
```

1. On your API workflow designer canvas, add a **Script** activity, to output a Bearer token value:
   1. Open the Expression editor and return a JSON with a property named **bearer_token**:
      ```
      return {
          "bearer_token": "123321123321"
      }
      ```
   2. **Save**.
2. Add a **HTTP** activity to the designer canvas.
3. Configure the **HTTP** activity as follows:
   * **Method**—POST
   * **Request URL**—Use the Expression editor to build the URL string with an **id** path variable:
     ```
     "https://www.httpbin.org/anything/" + ($workflow.input.id)
     ```
   * **Headers**—Add headers by specifying a simple key-value JSON. You are also simulating the process for adding a bearer token as an Authorization header:
     ```
     {
         "Accept": "application/json",
         "Content-Type": "application/json",
         "Authorization": ("Bearer " + $context.outputs.Javascript_3.bearer_token)
     }
     ```
   * **Request body**—Use the Expression editor to dynamically build the request body by referencing your run configuration JSON. The goal is to pass an array of transactions wrapped within an object as the request payload:
     ```
     {
         "transactions": $workflow.input.transactions
     }
     ```

Notice that the **Expression output** panel shows what the final JSON should look like based on the **Activity test input** data:

![Test input and output panels](/images/studio-web/studio-web-test-input-and-output-panels-582812.webp)
4. Debug the workflow to execute the activity.
5. Check the **Output** panel to review the HTTP response.

   ![Debug panel with response](/images/studio-web/studio-web-debug-panel-with-response-582820.webp)