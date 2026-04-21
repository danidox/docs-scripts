---
title: "Building an agent in Studio Web"
visible: true
slug: "building-an-agent-in-studio-web"
---

This section walks you through how to build an agent in Studio Web. To make reliable production-grade agents, we highly recommend you check out [Best practices](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/best-practices).

## Exploring the agent workspace

Use the main Studio Web designer canvas to design your agent, and the left and right panels to explore the agent structure and resources.

## Creating the agent

1. Go to [studio.uipath.com](http://studio.uipath.com/).
2. Select **Create New** button, then select **Agent**.
3. Select the agent type:
   * **Autonomous**: Create an agent that acts independently to complete a given task.
   * **Conversational** (Preview): Create an assistant that interacts with users through real-time dialogie.
4. If you want to create your agent from scratch, select **Start fresh**.
5. If you want to generate your agent using Autopilot (Preview), describe the agent you want the create in the available message box, then select **Generate Agent**. Be as specific as possible, so that Autopilot can efficiently generate an agent.
6. The new solution opens, with the **Agent** designer canvas displayed.
7. When configuring your agent, you can choose between two design modes: the traditional Form view and the Flow view (Preview). Both modes share the same underlying agent definition and remain fully synchronized, so you can switch between them at any time without losing data. Use **Form view** for a structured, step-by-step configuration experience, or switch to **Flow view** for a visual, node-based layout that lets you see how your agent’s components connect and interact.

## Configuring the agent

When configuring your agent, you can choose between two design modes: the traditional Form view and the Flow view (Preview). Both modes share the same underlying agent definition and remain fully synchronized, so you can switch between them at any time without losing data.

Use **Form view** for a structured, step-by-step configuration experience, or switch to **Flow view** for a visual, node-based layout that lets you see how your agent’s components connect and interact.

### Build an agent using Form view (Default)

1. From the ![docs image](/images/studio-web/studio-web-docs-image-548970.webp) **Project Explorer** panel on the left, access the agent **Definition**, **Evaluation sets**, and **Evaluators**.

Figure 1. The Agent inside a Solution

   ![docs image](/images/studio-web/studio-web-docs-image-553787.webp)

   1. The **Definition** panel is where you design and define the core elements of an agent. The definition contains the following sections: **General**, **Tools**, **Contexts**, and **Escalations**.
      * Use the **General** section to define the prompts for your agent.
      * Use the **Tools** section to connect runtime tools, like Integration Service connectors or published automations.
      * Use the **Contexts** section to link knowledge sources using Context Grounding indexes to give your agent relevant data access.
      * Use the **Escalations** section to set up human-in-the-loop fallbacks and enable Agent Memory to persist interactions and help calibrate future agent escalations.
   2. The **Evaluation sets** panel is where you create evaluations and store results. Evaluations objectively measure your agent's output and assess whether or not it is consistent with your objectives. For details, refer to [Evaluations](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-evaluations).
   3. The **Evaluators** panel is where you create and manage the evaluators used in evaluations.
2. First, select your agent under **Project Explorer**. Right-click to select **Rename**, and give your agent a unique name.The agent name helps to identify the agent across projects.
3. Next, access the **Properties** panel from the right-hand side menu to select the large language model you want to use with your agent.
   1. Select a model from the available dropdown list. Models are provisioned through UiPath [AI Trust Layer](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-ai-trust-layer). For details, refer to [Configuring LLMs](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-ai-trust-layer#configuring-llms).
   2. Configure the **Temperature** and **Max. tokens per response** fields. These settings may be controlled by an Automation Ops governance policy. For details, refer to [Settings for Studio Web Policies](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-studio-web-policies).
   * **Temperature** determines the creativity factor of the LLM generation. You can set a value between 0 (Precise) and 1 (Creative).
   * **Max. tokens per response** refers to the maximum number of tokens to generate with the agent's response.

Figure 2. Configuring the model settings

   ![Configuring the model settings](/images/studio-web/studio-web-configuring-the-model-settings-587282.webp)
4. In the agent **Definition** panel, provide your agent with a **System prompt** and a **User prompt**.Add a well-structured prompt to give your agent instructions for what it should do, and constraints it should follow. For details, refer to [Prompts](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-prompts).
5. Use the **Data Manager** panel to define the agent input and output arguments used in the prompts.

Figure 3. Input arguments in the Data Manager panel

   ![Input arguments in the Data Manager panel](/images/studio-web/studio-web-input-arguments-in-the-data-manager-panel-587286.webp)
6. In the **Tools** section, select **Add tool** to add any tools your agent can use during execution.These can be a set of Integration Service activities, existing agents, and published automations to which you have access. Each tool must have a detailed description that helps inform the agent how and when to use this tool. For details, refer to [Tools](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-tools).
7. (Optional) In the **Contexts** section, select **Add context** to give the agent access to Context Grounding indexes.Choose an existing index available in your tenant, or select **Create new** to create a new index directly in Orchestrator. For details, refer to [Contexts](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-contexts).
8. (Optional) In the **Escalations** section, select **Add escalation** to add a human in the loop through an escalation app and enable Agent Memory.Adding an escalation allows your agent to involve a human to review, approve, or update output as it is running. For details, refer to [Escalations and Agent Memory](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-escalations-and-agent-memory).

### Build an agent using Flow view (Preview)

   ![docs image](/images/studio-web/studio-web-docs-image-608594.webp)

1. Open your agent project in Studio Web.
2. In the top-right corner of the design-time canvas, select the **Flow (Preview)** option from the authoring mode toggle.
   * The Flow canvas opens, displaying the agent structure as nodes.
   * You can switch back to Form view at any time. All changes are saved and translated automatically between the two modes.
3. Start with the **LLM node**.
   * Select it to open the **Properties panel** on the right, then choose and configure your model.
     + Select a model from the available dropdown list. Models are provisioned through UiPath [AI Trust Layer](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-ai-trust-layer). To learn how to use a custom model, refer to [Configuring LLMs](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-ai-trust-layer#configuring-llms).
     + Configure the **Temperature** and **Max. tokens per response** fields. These settings may be controlled by an Automation Ops governance policy. For details, refer to [Settings for Studio Web Policies](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-studio-web-policies).
       - **Temperature** determines the creativity factor of the LLM generation. You can set a value between 0 (Precise) and 1 (Creative).
       - **Max. tokens per response** refers to the maximum number of tokens to generate with the agent's response.
   * Once a model is selected, the node updates with the corresponding model family icon and the highlight disappears.
4. Configure the **Agent node**.
   * The Agent node is created by default alongside the LLM node.
   * Open the **Prompt** section on the right to define your system and user prompts. For conversational agents, this section is simplified and only the system prompt is shown.
   * Open the **Schema** section on the left to define input and output arguments in the **Data Manager** panel.
5. Add context, tools, and escalations. After completing the LLM and Agent nodes, three new node types become available:
   * **Context**: Select a Context Grounding index and adjust its search parameters.
   * **Tools**: Open the command palette, search for a deployed tool, and add it to your canvas. You can further configure each tool once added.
   * **Escalations**: Add a human-in-the-loop node that connects to the existing escalation configuration experience.
6. Access additional options by selecting the ⋮ (More actions) menu on a tool node. The following actions are available:
   * **Add breakpoint** – Inserts a breakpoint at the tool node. When the agent is debugged, execution pauses just before this tool runs, allowing you to inspect its inputs, outputs, and trace data. Breakpoints are useful for verifying tool logic and debugging errors during design-time testing.
   * **Add guardrail** – Opens the **Guardrail configuration** window, where you can define rules that restrict or monitor how the tool is used at runtime.
   * **Disable** – Temporarily disables the selected tool node from agent execution. Disabled tools remain on the canvas but are skipped during runtime and debugging, allowing you to test or refine the agent’s behavior without permanently removing the tool.

   ![docs image](/images/studio-web/studio-web-docs-image-608598.webp)
7. Debug your agent.
   * Select **Debug** to run your agent in design time.
   * As the agent executes, nodes light up in sequence to show the execution flow.
   * If you run simulations, nodes appear in a different color to indicate mocked data or tool calls.
   * For conversational agents, a persistent chat window allows you to test exchanges; each message triggers a debug run that displays highlights across the connected nodes.
   * You can also set breakpoints on specific nodes to pause execution and inspect inputs, outputs, and trace data.
8. Save and publish your changes.
   * All updates in Flow view are stored automatically and remain synchronized with Form view.
   * When ready, publish the agent to make it available for testing and deployment.

## Testing the agent

Now it's time to test your agent and see how you can improve it.

1. Navigate to the toolbar above the Studio Web designer.
2. Select the arrow next to the debugging environment, then select **Debug configuration**.
3. In the **Debug configuration** window, confirm the resources used in the solution and the sample input.
4. Select **Save and Run**.

### Evaluating the agent

Next, go to the **Evaluation sets** and **Evaluators** panels to review and measure your agent.

1. In the **Evaluation sets** panel, rename the default evaluation set and add test cases with expected outcomes.
2. In the **Evaluators** panel, add evaluators to validate the agent output.

Each evaluation links a known input with an assertion about the output.

### Calculating the Agent score [Preview]

Select **Open health score** from the right-side panel to calculate the agent score. Refer to [Agent score](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-score) to learn how it is calculated.

### Using Autopilot to improve your agent [Preview]

Select **Open Autopilot** from the right-side panel to receive suggestions on improving prompts, tools, and other components. Such improvements support a higher Agent Score and make your agent ready for deployment.

## Publishing and deploying the agent

Once you have tested, evaluated, and refined your agent, it's time to publish it. This step is necessary for the agent to be available in the [Run Job](https://docs.uipath.com/activities/other/latest/workflow/run-job) activity.

1. Select **Publish** to publish the agent to Orchestrator as a process. Select where to publish:
   1. **Orchestrator Personal Workspace Feed** - The process is published to your personal workspace and is only be available to you. This is the default selection.
   2. **Orchestrator Tenant Processes Feed** - The process is published to the global tenant feed and is available to all users in eligible folders.
2. Select a version. A version is generated automatically starting with 1.0.0 when you first publish, and then incremented automatically every time you republish.
3. Optionally, you can select **Submit as a template** to make the agent available as a template in your organization, or **Share**, to share it with users in your organization.

## Running the agent

Using agents as activities means you can incorporate them into workflows to handle parts of larger deterministic processes, have multiple agents act in series, and start agent execution based on triggers.

To incorporate your agent into a workflow, follow these steps:

1. Publish your agent to Orchestrator.
2. In Studio, use the [Run Job](https://docs.uipath.com/activities/other/latest/workflow/run-job) activity to integrate your agent into a workflow.
3. Whenever you make changes to your agent, republish the updated agent to Orchestrator and upgrade the corresponding process in Orchestrator. The [Run Job](https://docs.uipath.com/activities/other/latest/workflow/run-job) activity always executes the version of the agent currently configured in Orchestrator. This ensures that your workflow consistently uses the most up-to-date version of your agent.

Refer to the [System activities guide](https://docs.uipath.com/activities/other/latest/workflow/run-job) to learn how to configure and use the **Run Job** activity in your Studio workflows.

:::note
Starting with UiPath.System.Activities version 25.4.2, the execution of agents and other Orchestrator jobs has been consolidated and improved under the **Run Job** activity. Existing workflows using the [Run Agent](https://docs.uipath.com/activities/other/latest/workflow/run-agent) activity continue to function without changes, ensuring a smooth transition. When adding new agent-running functionality to your workflows, the system automatically suggests and implements the **Run Job** activity, even if you search for **Run Agent**.
:::