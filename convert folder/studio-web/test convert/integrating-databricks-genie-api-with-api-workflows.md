---
title: "Integrating Databricks Genie API with API workflows"
visible: true
slug: "integrating-databricks-genie-api-with-api-workflows"
---

Databricks Genie enables natural language interaction with your enterprise data, allowing you to query, analyze, and act on datasets without needing to write code.

This guide provides a practical walkthrough of how to interact with a Databricks Genie API to get information based on a question input. It performs the following main actions:

* **Initializes variables—**Sets up necessary parameters like tokens, URLs, and IDs.
* **Gets a token**—Makes an HTTP POST request to obtain an access token for authentication.
* **Starts a conversation**—Sends the user question to the Genie API to initiate a conversation.
* **Polls for message completion**—Enters a **Do While** loop to repeatedly check the status of the Genie message until it is COMPLETED**.**
* **Retrieves query results**—Once the message is complete, it fetches the final query results from the Genie API and provides the retrieved data as the workflow output.
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615396)

## Prerequisites

First, you need to have a Genie space called "Item Restrictions" in your Databricks workspace.

Its purpose is to reference shipping restrictions for different products and provide answers regarding shipping details.

1. [Create an API workflow](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/managing-api-workflows#creating-api-workflows).
2. Define workflow inputs. Open **Data manager** and add a new **Inputs** parameter with the following configuration:
   * **Name**—Question
   * **Type**—String
   * Mark it as **Required**.
3. Define workflow variables. Open **Data manager** &gt; **Variables**, and add the following:
   * `token` (String)—Stores the authentication token required to access the Databricks Genie API.
   * `conversation_id` (String)—Tracks a specific conversation session with the Databricks Genie API. When you start a conversation, the API provides this ID, and you use it to refer to that ongoing conversation in subsequent requests.
   * `message_id` (String)—Refers to a specific message within a conversation. This ID is then used to retrieve the status and eventually the results of that particular message processing.
   * `attachment_id` (String)—Points to a specific attachment (which in this case holds the query result) associated with a message in the Genie API.
   * `url` (String)—Stores the base URL for the Databricks Genie API endpoint.
   * `space_id` (String)—Points to a specific space within Databricks Genie.
4. Add a **HTTP** activity to retrieve the access token and configure it as follows:
   * **Display name**—"Get token HTTP Request"
   * **Method**—POST
   * **Request URL**—`https://accounts.cloud.databricks.com/oidc/accounts/{account_id}/v1/token`
   * **Headers**—
     ```
     {
     "Authorization": "Basic <your_basic_token>",
     "Content-Type": "application/x-www-form-urlencoded"
     }
     ```
   * **Request body**—
     ```
     "grant_type=client_credentials&scope=all-apis"
     ```The context output name for this activity is `HTTP_Request_1`.
5. Assign the token retrieved from the previous activity to your `token` variable. Add an **Assign** activity and configure it as follows:
   * **To variable**—`token`
   * **Set value**—`$context.outputs.HTTP_Request_1.content.access_token`The context output name `HTTP_Request_1` may differ from the one used in your workflow.
6. Add a **HTTP** activity to start the conversation and configure it as follows:
   * **Display name**—"Start conversation HTTP Request"
   * **Method**—POST
   * **Request URL**—`https://{your-databricks-instance}/api/2.0/genie/spaces/{space_id}/start-conversation`, or build it with the Expression editor as
     ```
     $context.variables.url + "/api/2.0/genie/spaces/"+ $context.variables.space_id +"/start-conversation"
     ```
   * **Headers**—
     ```
     {"Authorization": "Bearer " + $context.variables.token}
     ```
   * **Request body**—
     ```
     {"content": $workflow.input.question}
     ```

Ensure the output is saved. You can retrieve `conversation_id` and `message_id` from the output of this activity.

The context output name for this activity is `HTTP_Request_2`.
7. Enter a loop to check the status of the Genie message until COMPLETED. Add a **Do While** activity and set the **Condition** to `$context.outputs.HTTP_Request_3?.content?.status !== "COMPLETED"`, where `HTTP_Request_3` refers to the Get message HTTP Request activity. This means the loop continues as long as the message status is not COMPLETED.
8. Inside the **Do while** loop:
   1. Add a **HTTP** activity for getting the last message and configure it as follows:
      * **Display name**—"Get message HTTP Request"
      * **Method**—GET
      * **Request URL**—`https://{your-databricks-instance}/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}`, or build it with the Expression editor as
        ```
        [ $context.variables.url+"/api/2.0/genie/spaces/"+$context.variables.space_id+"/conversations/", $context.outputs.HTTP_Request_2.content.conversation_id, "/messages/", $context.outputs.HTTP_Request_2.content.message_id ].join('')
        ```

Where `HTTP_Request_2` refers to the Start conversation HTTP Request activity.
      * **Headers**—
        ```
        {"Authorization": "Bearer " + $context.variables.token}
        ```
      * **Request body**—
        ```
        {"content": $workflow.input.question}
        ```The context output name for this activity is `HTTP_Request_3`.
   2. Add an **If** activity immediately after the Get message HTTP Request acitvity, and set the **Condition** to `$context.outputs.HTTP_Request_3?.content?.status === "COMPLETED"`, where `HTTP_Request_3` refers to Get message HTTP Request activity.
   3. On the **Then** (true) branch, add an **Assign** activity and configure it as follows:
      * **To variable**—`conversation_id`
      * **Set value**—`$context.outputs.HTTP_Request_3.content.conversation_id`, where `HTTP_Request_3` refers to Get message HTTP Request activity.
   4. Add another **Assign** activity:
      * **To variable**—`message_id`
      * **Set value**—`$context.outputs.HTTP_Request_3.content.message_id`, where `HTTP_Request_3` refers to Get message HTTP Request activity.
   5. Add another **Assign** activity:
      * **To variable**—`attachment_id`
      * **Set value**—`$context.outputs.HTTP_Request_3.content.attachments[0].attachment_id`, where `HTTP_Request_3` refers to Get message HTTP Request activity.
   6. On the **Else** branch, add a **Wait** activity and set duration to one second. This instructs the workflow to wait for a short period before retrying.
9. Exit the loop and add a **HTTP** activity to execute the SQL query and configure it as follows:
   * **Display name**—"Execute SQL HTTP Request"
   * **Method**—GET
   * **Request URL**—`https://{your-databricks-instance}/api/2.0/genie/spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}/attachments/{attachment_id}/query-result`, or build it with the Expression editor as
     ```
     $context.variables.url+"/api/2.0/genie/spaces/"+$context.variables.space_id+"/conversations/" + $context.variables.conversation_id + "/messages/"  + $context.variables.message_id + "/attachments/" +  $context.variables.attachment_id + "/query-result"
     ```
   * **Headers**—
     ```
     {"Authorization": "Bearer " + $context.variables.token}
     ```The context output name for this activity is `HTTP_Request_3`.
10. Define workflow outputs. Open **Data manager** and add the following **Inputs** parameters:
    * **Name**—row_count
    * **Type**—Number
    * Mark it as **Required**.and
    * **Name**—data_array
    * **Type**—Array
    * Mark it as **Required**.
11. Add a **Response** activity and configure it as follows:
    * **Response**—
      ```
      {
        "row_count": -75647404.57028332,
        "data_array": [
          [],
          [],
          [
            "ut et aute officia",
            "ex ut",
            "nisi non ut Lorem velit",
            "aliquip Duis consectetur irure id"
          ]
        ]
      }
      ```
12. Run the integration. Once deployed, the Workflow can be invoked with any natural language query. An example question could be : "Are there any restrictions to ship SKU ENB-SP-200 to Cuba?"

**Key take-aways:**
1. **Simple setup** – API Workflow provides a fast way to connect Genie without custom code.
2. **Consistent schema** – Genie responses are JSON-based, easy to parse into UiPath.
3. **Scalable integration** – Responses can be used in Apps, long-running workflows, or orchestrations.
4. **Rapid prototyping** – Setup for working automation takes minutes, allowing quick validation of use cases.