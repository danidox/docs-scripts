---
title: "Integrating Snowflake Cortex API with API workflows"
visible: true
slug: "integrating-snowflake-cortex-api-with-api-workflows"
---

Snowflake Cortex Agents unlock natural language interaction with your data, helping you query, analyze, and act on enterprise datasets.

This workflow acts as an intermediary to run an "ORDERS_AGENT" in Snowflake. It takes a question as input, sends it to the Snowflake Cortex Agent API, and then returns the API response directly as the workflow output.

![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615405)

## Prerequisites

First, you need to have a Cortex Agent set up in your Snowflake account.

1. [Create an API workflow](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/managing-api-workflows#creating-api-workflows).
2. Define workflow inputs. Open **Data manager** and add a new **Inputs** parameter with the following configuration:
   * **Name**—Question
   * **Type**—String
   * Leave the **Required** checkbox empty.
3. Add a **HTTP** activity and configure it as follows:
   * **Method**—POST
   * **Request URL**—Provide the Cortex Agent run endpoint, specific to your Snowflake account and agent, for example `"https://{your_snowflake_env}/api/v2/databases/SNOWFLAKE_INTELLIGENCE/schemas/AGENTS/agents/ORDERS_AGENT:run"`
   * **Headers**—
     ```
     {
       "Content-Type": "application/json",
       "Accept": "application/json",
       "Authorization": "Bearer <Add your snowflake_token here>"
     }
     ```
   * **Request body**—
     ```
     {
         "messages": [
             {
                 "role": "user",
                 "content": [
                     {
                         "type": "text",
                         "text": $workflow.input.Question
                     }
                 ]
             }
         ],
         "toolChoice": {
             "type": "auto"
         }
     }
     ```
4. Add a **Response** activity and leave it as is. This captures and returns the output from the Cortex agent as a JSON.
5. Run the integration. Once deployed, you can invoke the workflow with any natural language query. The workflow passes the question to the Cortex Agent, receives the streaming output, and returns a structured JSON response that can be used in downstream automations.

**Key take-aways:**
* **Streaming is seamless** – Although Cortex API is streaming-only, the API workflow built-in support meant no additional coding was required to parse and collect results.
* **Consistent API contract** – All Cortex Agents share the same request/response shape. Your integration does not need to change as your agents become more advanced.
* **Rapid prototyping** – From setup to working integration took minutes. This speed allows teams to quickly validate use cases and iterate.