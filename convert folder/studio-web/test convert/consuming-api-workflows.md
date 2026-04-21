---
title: "Consuming API workflows"
visible: true
slug: "consuming-api-workflows"
---

## Consuming API workflows from Orchestrator

To run your published API workflows from Orchestrator:

1. In your Automation Cloud Orchestrator, go to the folder where the API workflow process exists.
2. Navigate to **Automations** &gt; **Processes**.
3. For the desired API workflow process, select **Start a job** at the end of the coresponding row.
4. In the page that opens, provide:
   * [Execution Target](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-jobs#execution-target) options
   * [Runtime Arguments](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-processes#runtime-arguments) options. The **Input** section represents your API request input schema, and allows you to specify properties to use as inputs for execution.
5. To run your process, select **Start**.

Once your workflow has successfully run, you can view the generated response in the workflow execution details: **Automations &gt; Jobs**.

## Invoking API workflows in an Agent

Extend the capability of your UiPath Agents by integrating API workflows as tools. Agents automatically query these workflows to gather relevant context, enabling precise control over the data available to your agents and AI models.

The following scenario demonstrates how an API workflow can transform data retrieved from Workday, limiting the information exposed to agents to names and email addresses only. In the Workday sandbox, Betty Liu is configured as a manager with assigned direct reports and peers. Example queries for the agent include:

* "Who reports to Betty Liu?"
* "Provide all peers for Betty Liu."
* "Do any of Betty Liu's peers have reports?"
  :::important
  The agent does not store your Workday credentials and relies solely on responses returned by the API workflow.
  :::

Before you begin, ensure the following prerequisites are met:

* You published your [Workday API workflow](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/extracting-worker-hierarchy-from-workday#extracting-worker-hierarchy-from-workday) to Orchestrator. Confirm that the workflow runs successfully when executed from Orchestrator.
* Platform units are assigned to your tenant.
* To follow the provided Workday integration example, ensure your workflow includes:
  + An input schema with fields for **first name** and **last name**.
  + An output schema containing arrays for **Peers** and **Direct Reports**.

1. [Create your agent manually](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/building-an-agent#creating-the-agent). Alternatively, use the Autopilot generator with the following prompt:

"Query workday for manager, reports and peers details."

Your agent is created with Autopilot, which suggests the agent prompts and configuration. In this example, the suggested prompts were initially accepted, but the **User Prompt** was later simplified to contain only the **{{ query }}** variable.
2. In the **Data manager** panel of your agent, define an **Input** property called `query`, of type String. This ensures your **User Prompt** contains a valid reference.
   ![Query variable in User prompt](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/584553)
3. Select **Debug on cloud**. You are prompted to provide the query for your **User Prompt**. However, the **Execution Trace** panel shows that the agent currently has no access to Workday, so it cannot provide a response yet.
4. From the **Tools** section of your agent, select **Add tool** &gt; **API workflow**.
5. Select the existing API workflow (the one that queries Workday), and provide a description for it. As a best practice, provide enough detail for the agent to automatically configure the workflow based on your prompt. A clear description typically includes details about your input parameters. For example:

"Takes a worker first and last name as input and provides their direct reports and peers in the response. The name input is the manager we will look up in Workday."
6. Run your agent again by selecting **Debug on cloud**. Provide the following querry: "Who reports to Betty Liu?". The **Execution Trace** panel now identifies that the agent calls the API workflow, including:
   * The request sent to the API workflow
   * The response received from the API workflow
   * How the agent uses the response to fullfil your query

Congratulations!

Now you can create variations of your agent user prompt. Depending on the query, the agent may trigger multiple calls to your API workflow before providing a complete response.

## Using API workflows as tasks in Maestro

API workflows as tasks in Maestro encapsulate detailed API chaining and data transformations. This keeps the primary Maestro process clear, concise, and easy to follow. By isolating specific API interactions within API workflows, you maintain readability and promote reusability across multiple processes.

The following scenario demonstrates how Maestro calls Workday APIs and then sends a Slack team notification whenever an employee was terminated.
   ![API workflows in an agentic process](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/584570)

Before you begin, ensure the following prerequisites are met:

* You published your [Workday API workflow](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/extracting-worker-hierarchy-from-workday#extracting-worker-hierarchy-from-workday) to Orchestrator. Confirm that the workflow runs successfully when executed from Orchestrator. Ensure your API workflow includes:
  + An input schema with fields for **First Name** and **Last Name**.
  + An output schema containing arrays for **Peers** and **Direct Reports**.

### Step 1: Creating an Agentic Process

1. [Create an agentic process.](https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/creating-and-agentic-project)
2. Add a **Start event** element. Name it "Employee Hired".
   1. For the **Action** property of the **Start event**, select **Wait for connector event**.
   2. For the **Connector** property, select **Workday REST - Worker Created**. This is the event that triggers the process.
3. Add a **Task** element and connect the **Start event** to it. Name it "Find Employee Relationships".
4. Add another **Task** element, name it "Send Notifications", and connect the Find Employee Relationships element to it.
5. Add an **End event**. Name it "Notification Sent".

This is the process setup. Whenever a new employee is hired, the process triggers the API workflow, which retrieves employee information such as their reporting structure and associated relationships.

### Step 2: Configuring the Find Employee Relationship task

The API workflow required by the agentic process resides in the Find Employee Relationships task. Here is how to configure it:

1. Select the **Find Employee Relationships** task.
2. For the **Action** property , select **Start and wait for API workflow**.
3. For the **API workflow** property, select the published Workday API workflow. The properties panel displays inputs and outputs for the selected workflow. For this example:
   * **Inputs** include **Last Name** and **First Name.**
   * **Outputs** include details for **Manager**, **Peers**, and **Reports**.
4. Configure inputs as follows:
   * **First Name** as a variable from the **Start event** response object. Open the Expression editor, select Insert variable and navigate to **Employee Hired &gt; response &gt; Worker &gt; Worker full name**. Then add `Split(' ')[0]` to the expression. It should look like the following:
     ```
     vars.response_1.worker.descriptor.Split(' ')[0]
     ```

Where `worker` is the response object from the **Start event** response, and`.Split(' ')[0]` splits the full name by the space character and fetches the first part of the full name.
   * **Last Name** as a variable from the **Start event** response object. Open the Expression editor, select Insert variable and navigate to **Employee Hired &gt; response &gt; Worker &gt; Worker full name**. Then add `Split(' ')[1]` to the expression. It should look like the following:
     ```
     vars.response_1.worker.descriptor.Split(' ')[1]
     ```

Where `worker` is the response object from the **Start event** response, and`.Split(' ')[1]` splits the full name by the space character and fetches the second part of the full name.

### Step 3: Customizing the Send Notification task

In this step, you configure the Send Notification task to use data returned from the API workflow executed at Step 2.

1. Select the **Send Notification** task.
2. For the **Action** property, select **Execute connector event**.
3. For the **Connector** property, select **Slack**, and configure it to use your **Connection**.
4. For the **Activity** property, select **Send Message to Channel**.
5. For the **Channel name/ID**, write the ID of the Slack channel where the notification should be sent.
6. For the **Message** property, select the output variables from Step 2: **Manager**, **Peers**, and **Reports**.
7. For the **Send as** property, select **bot**.

### Step 4: Testing your agentic process

To successfully test this agentic process, ensure you have access to your Workday sandbox environment.

Select **Test** to validate your workflow. Maestro prompts you to provide two essential connections:

* **Slack Connection—**Required by the **Send Notification** task.
* **Workday Connection—**Required by the **Start event**.
  :::important
  Maestro does not request connections for the API workflow since these connections are managed separately within the API workflow itself.
  :::