---
title: "Managing API workflows"
visible: true
slug: "managing-api-workflows"
---

## Creating API workflows

To create an API workflow solution:

1. In your Automation Cloud™ organization, open Studio Web.
2. Select **Create New** &gt; **API Workflow**. A new solution opens, with the **API Workflow** designer canvas displayed.

## Defining Input schemas

API Workflows typically require input from their calling parties. This is handled by defining JSON objects for both input and output, each following a JSON schema. These schemas establish the data types and structure for your objects. The defined objects can include nested objects, multiple properties, and arrays, allowing you to model complex data structures as needed.

The input schema specifies the data structure an external service must provide when triggering the workflow.

You can configure the input schema by uploading a JSON payload or by manually defining input parameters.

1. In your API workflow project, open the **Data manager** panel.
2. Select the **Input** tab.

To upload a JSON schema, follow Step 3.

To manually define input parameters, follow Step 4.
3. To upload a JSON schema with the input parameters already defined, select **Generate From Payload**.
   1. Provide the JSON with the expected input.
   2. Select **Generate Schema**.
   3. Review the generated schema and add descriptions to properties if necessary.
4. To manually define input parameters, select **Add property**.
   1. Configure the property details:
      * **Name**—Define the property key
      * **Type**—Select from String, Number, Integer, Boolean, Object, Array, Date-time, Date, Time.
        :::important
        If you are using an Object or an Array, define the properties for the nested items.
        :::
      * **Required**—Select this box to mark the property as required.
   2. Repeat the step until you define all input parameters.

## Defining Output schemas

The output schema defines the structure of the data returned by the API workflow, ensuring that any service calling the workflow understands the output format in advance. It is also required when the workflow includes a **Response** activity, as it determines the exact data sent back to the calling party.
:::note
Currently, schema validation is not enforced, so if the data returned in the Response activity includes more or fewer properties than those defined in the output schema, the workflow does not fail.
:::

The output schema includes fields explicitly defined within the schema itself, such as IDs or user-provided values, as well as outputs generated dynamically from workflow steps, such as API responses or calculated values.

You can configure the output schema by uploading a JSON payload or by manually defining output parameters.

1. In your API workflow project, open the **Data manager** panel.
2. Select the **Output** tab.

To upload a JSON schema, follow Step 3.

To manually define output parameters, follow Step 4.
3. To upload a JSON schema with the output parameters already defined, select **Generate From Payload**.
   1. Provide the JSON with the expected output.
   2. Select **Generate Schema**.
   3. Review the generated schema and add descriptions to properties if necessary.
4. To manually define output parameters, select **Add property**.
   1. Configure the property details:
      * **Name**—Define the property key
      * **Type**—Select from String, Number, Integer, Boolean, Object, Array, Date-time, Date, Time.
        :::important
        If you are using an Object or an Array, define the properties for the nested items.
        :::
      * **Required**—Select this box to mark the property as required.
   2. Repeat the step until you define all output parameters.

## Using the Expression editor

The Expression editor helps you access, evaluate, and manipulate data within API workflows. Use it to create conditional logic, configure activity fields, or write JavaScript activities.

### Expression editor layout

The layout of the **Expression editor** contains the following panels:

| Panel | Description |
| --- | --- |
| Input | The main panel is the input panel, where you write your JavaScript or JQ expressions.  This panel includes a built-in syntax-checker that identifies and highlights errors in your expression syntax. |
| Autopilot expression generator | Located at the bottom of the input panel, the Autopilot expression generator helps you create workflow expressions using natural language, instead of writing JavaScript.  Autopilot understands the context of your workflow, and enables you to reference objects and workflow steps simply by describing your desired outcome. |
| Activity test input | To the right-hand side of the code panel, the **Activity test input** panel allows you to review test data generated from previous workflow runs.  It provides sample data you can use to build and validate expressions, and it interacts directly with the **Expression output** panel to ensure your expressions produce the desired results. |
| Expression output | The **Expression output** panel displays the result of your expression based on the data from the **Activity test input** data. This allows you to validate that your expression generates the expected outcome.  If your expression has errors, the **Expression output** section highlights the problematic expression and provides a corresponding error message.  The result updates automatically whenever you modify the expression in the input panel. |

### Accessing data using JavaScript

There are several access points for workflow data:

* `$workflow`—Refers to the workflow-level configuration.
* `$context`—Refers to activity-level configuration.
* `$input`—Refers to the previously executed activity configuration.
* `$context.variables`—Refers to variable-level configuration.
  :::important
  Use the **Test input** screen within the **Expression editor** to reference step properties when building your expressions.
  :::

Expand Table

|  |  |  |
| --- | --- | --- |
| Access points | Description | How to use |
| `$workflow.input` | Stores the request schema and any values defined in the test configuration. | To access test configuration data within the **Expression editor**, enter the following syntax, and replace `{property_name}` with the specific property you want to reference: ``` $workflow.input.{property_name} ``` |
| `$context` | Stores the input and output data for each activity. To reference these properties in your expressions, first run and Debug the workflow . This generates step-level inputs and outputs visible in the **Test Input** screen. | To access the output response data of a specific step, use the following syntax pattern in the **Expression editor**, and replace `{step_name}` and `{property_name}` with your step and property names, respectively: ``` $context.outputs.{step_name}.content.{property_name} ``` |
| `$input` | Stores data passed directly from the previous step into the current step. Use `$input` to reference properties from the preceding step without navigating through the entire `$context`. | To access properties from the previous step, use the following syntax, and replace `{property_name}`with the property you wish to reference: ``` $input.{property_name} ``` |

## Testing API workflows

For a successful API workflow integration, test your workflow early and frequently. Regular testing helps you quickly identify and resolve errors. Features such as IntelliSense, auto-completion, Autopilot, and the Activity test input screen depend on test data. Execute the workflow regularly using the **Test** button to generate this data.

Testing ensures:

* Your data mappings between workflow steps are correct, preventing unexpected behavior.
* API requests are properly configured, ensuring reliable responses.
* Your workflow performs as intended, reducing the risk of unexpected errors in production.

### Understanding the Run Output information

The **Run Output** panel provides detailed information about workflow execution.

#### Activity input and output data

This data is available per selected activity and provides:

* **Input data—**Information a step receives from the previous activity.
* **Output data—**Information produced by the current step, passed to the next activity.

Review input/output data to confirm accurate mappings and data transformations.

#### API request information

When workflows interact with APIs, verify the following request details:

* **Request URL—**Confirm dynamic URL parameters resolve correctly.
* **Headers—**Ensure authentication and content-type headers are set appropriately.
* **Query Parameters—**Check that filters and parameters are correctly formatted.
* **Body Content—**Validate JSON structure matches the API requirements.

#### Successful API requests

For successful API requests, expand each step to review:

* **Request details—**URL, headers, query parameters, and body content.
* **Response details—**Status code, headers, and response content.
* **Output data—**Information generated by the API call for use in subsequent workflow steps.

#### Debug

To efficiently identify and debug workflow errors, follow these guidelines:

* **Error Indicators**
  + Steps encountering errors display an error icon.
  + Select the step to view detailed error messages and outputs.
* **Common Debugging Steps**
  + **Validate API requests**—Ensure request details such as URLs, headers, parameters, and body content match API documentation.
  + **Review error messages**—Examine error messages for clues about authentication errors, incorrect payloads, or scripting mistakes.

### Adding a Debug configuration

You can build and test your API workflow iteratively, validating each step as you add new activities. To run these tests effectively, you can define specific input data using the **Debug configuration** feature. This allows you to set a JSON input once and reuse it across all subsequent test runs. You can access the emulated data through the `$workflow.input` object during workflow execution.

To add a **Debug configuration**:

1. On the top of your API workflow designer canvas, open the **Debug** dropdown, then select **Debug configuration**.
2. In the window that opens, provide the test input data in the available fields, or upload a JSON payload.
3. **Save** your test configuration.
4. Once saved, you can access the test configuration in the Expression editor using the reference `$workflow.input.{propertyname}`. Additionally, the debug configuration is also displayed in the **Activity test input** panel of the Expression editor.

### Debugging your API workflow

To debug your API workflow:

1. Open your API workflow. Make sure your workflow is fully configured and ready to run.
2. If your workflow depends on input data, for example, from an external system, define the **Debug configuration** before testing. This ensures every step receives the necessary data.
3. **Debug** your workflow. The **Debug** button is located at the top of the page. Select it to execute the workflow and see real-time results.
4. Once debugging starts, the **Run Output** panel appears on the right side of the screen. Here, you can see each step execution status clearly marked as **success**, **failure**, or **pending**.

## Publishing API workflows

:::important
Before publishing, test your API workflow using both success and failure scenarios to confirm that each scenario executes correctly.
:::
To publish your API workflow solution:

1. On your API workflow designer canvas, select **Publish**.
2. Select the location where your API workflow should be published:
   * Your Orchestrator personal workspace feed
   * Your Orchestrator tenant feed
3. Provide other details important for your API workflow, such as **Change log** and **Version**.
4. Select **Publish**. A notification informs you about the successful publishing of your API workflow.

If you published to your personal workspace feed, the workflow is visible in Orchestrator under **My Workspace &gt; Automations &gt; Processes**. API workflows are identifiable by the type **API**.

If you published to your tenant feed, the workflow is visible in Orchestrator under **Tenant &gt; Solutions**. API workflows are identifiable by the type **API**.

## Deploying API workflows

Once you published your API Workflow to the feed of your preference, you need to deploy the solution.

### Deploying API workflows from your personal workspace feed

Publishing to your personal workspace prepares the API workflow as a process in **Orchestrator &gt; My Workspace &gt; Your API workflow name subfolder &gt; Automations &gt; Processes.**
:::important
A dedicated subfolder is automatically created inside your personal workspace folder.
:::

### Deploying API workflows from your tenant feed

Publishing to your Orchestrator tenant uploads the API workflow package to **Orchestrator &gt; Tenant &gt; Solutions**.

To deploy it as a process:

1. Go to **Orchestrator &gt; Tenant &gt; Solutions**.
2. For the API workflow package you previously published to your tenant feed, select the three dots menu, then select **Deploy package**.
3. On the **Deploy solution version** wizard, configure the following details:
   1. **Deployment name**—add the name to be displayed on all pages which mention, list, or monitor processes. If left empty, the name of the package is used.
   2. **Destination folder**—indicate the folder to be used as a parent folder for the solution root. The solution is not deployed in the selected folder, but a new child folder is created.
   3. **Install as a new root folder under tenant**—select this checkbox to install the solution as a new root folder under the current tenant.
   4. **Solution root folder name**—change the root folder name.
4. Select **Review.** You can now save your solution as a draft, or validate it and continue.
5. Select **Deploy**. Now you can find your workflow as a process in the folder indicated at step 3 &gt; **Automations** &gt; **Processes**. You can identify an API Workflow by the type **API**.
6. Select **Activate deployment** to finish deploying your API workflow.

## Best practices

* Define clear **Input** and **Output** schemas so other UiPath products can understand and interact with your workflow.
* Leverage the quick execution speed of API workflows to test input and output payloads during design time.
* Use Autopilot to generate context-aware expressions and JavaScript code.
* Validate expressions in the Expression Editor output panel to catch syntax or logic issues before runtime.
* Interact with input and output data in the Run Output panel by expanding, collapsing, or copying values to the clipboard.
* Exit the workflow early by configuring a Response activity, either Success or Failure.
* In **Loop** activities, namely **For Each** and **Do While**, use **$input** instead of **$context** to access the previous object output.
* Use the **HTTP** activity to call APIs directly when a connector does not provide the required functionality. Choose between the native **HTTP** activity or the connector-specific **HTTP Request** activity.
* Using the **UiPath Orchestrator** connector, you can now access assets and credentials, which can then be securely used in request headers.
* Provide authentication tokens in the **HTTP** activity **Headers** property:
  ```
  { 
      Authorization: "<my_token>",
      "Content-Type": "application/json"
  }
  ```

For basic authentication, use:

  ```
  { Authorization: "Basic " + btoa("<username>:<pass>")}
  ```