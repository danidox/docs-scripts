---
title: "About Autopilot chat"
visible: true
slug: "about-autopilot-chat"
---

Autopilot offers a conversational interface designed to help you interact with UiPath products. It offers you a persistent, context-aware workspace where you can build automations, explore product features, or search documentation using natural language.

Autopilot maintains input history, interprets intent, and responds with relevant, task-specific suggestions. You can reference earlier inputs, adjust parameters, refine prompts, and clarify intent at any point in the workflow. You can ask Autopilot to explain a suggestion, rephrase an instruction, or modify an existing step, all from within the same interface.

Autopilot evolves at the same time with your automation logic, ensuring relevant recommendations as requirements change.

Here are the main capabilities of the chat experience:

* Context retention—remembers previous inputs and decisions.
* Prompt refinement—lets you edit your prompt in real-time to improve outcomes without starting from scratch.
* Conversational experience—uses natural language to ask questions and make changes.
* Inline suggestions—offers recommendations directly in the chat, specific to your current context.
* Unified workspace—keeps all interactions, iterations, and results in one place.
* Workflow continuity—maintains the flow across steps and stages.
* Interactive debugging—helps you identify and fix issues by asking follow-up questions or clarifying intent.
* Code and logic awareness—understands the structure of your automation or code and provides relevant guidance.

## Adoption in UiPath products

Autopilot offers a conversational framework that adjusts its capabilities based on the UiPath product you access it from. It is currently available in:

* [Orchestrator](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-orchestrator#orchestrator)
* [API workflows in Studio Web](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-studio-web#studio-web)
* [Studio 2025.10+](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-studio-desktop#studio)
* [Test Manager](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-test-manager#test-manager)


:::note
Each UiPath product where Autopilot chat is used features a specific suite of tools developed to help with your tasks. Consult the Connected sources section for details relevant to each product.
:::

## The LLM used

Autopilot can use various Large Language Models (LLMs) to power its capabilities. The choice of LLM influences performance, reasoning depth, and speed.

* **Gemini 2.5 Flash**—ideal for fast, general tasks without deep reasoning needs.
* **Gemini 2.5 Flash (Agent)**—combines speed with agentic capabilities for moderately complex, multi-step tasks.
* **Gemini 2.5 Pro**—best for complex automation building, reviewing, and debugging, offering deeper reasoning.
* **Gemini 2.5 Pro (Agent)**—the top choice for highly complex, agent-driven tasks requiring thoroughness and advanced planning.
* **GPT-5 Mini - Experimental**—for simple tasks where quick response time is paramount; an experimental model.
* **GPT-5 Mini - Experimental (Agent)**—experimental agentic model for quicker, structured outputs on simpler tasks.
* **GPT-5 - Experimental**—for general to complex tasks, leveraging cutting-edge, experimental LLM features.
* **GPT-5 - Experimental (Agent)**—experimental agentic model for complex, agent-driven tasks, using the newest models.

The **(Agent)** suffix indicates that the model is specifically configured to leverage agentic capabilities, such as:

* breaking down complex problems.
* selecting and using appropriate tools (Web Search, RPA Workflow Assistant).
* executing multi-step processes.
* monitoring progress and adapting its strategy.

If your task involves multiple steps, requires using tools, or needs deeper reasoning beyond a single response, opting for an **(Agent)** variant is generally recommended.

You can select the LLM from the Autopilot chat screen.


:::note
* To use these LLMs, check you have the required policies in AI Trust Layer.
* Specifically for the documentation AI functionality, Autopilot uses Azure OpenAI.
:::

## Data residency

For more information on data residency, refer to the [Global cloud regions](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/global-cloud-regions) topic.

## The AI Trust Layer policy

To use the AI capabilities provided by Autopilot, make sure you have an AI Trust Layer policy active and deployed to your tenant.

Learn how to:

* [Create a policy](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/create-a-governance-policy)
* [Configure the policy for AI Trust Layer](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-ai-trust-layer-policies)
* [Deploy the policy to the tenant where you want use Autopilot](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/deploy-governance-policies#deploy-policies-at-tenant-level)

## Disclaimer about Autopilot responses

Autopilot is designed to assist you across different UiPath products, and provides AI-powered support for a variety of tasks, such as building and editing automations, understanding complex workflows, or retrieving relevant information from documentation or other sources. While it can be highly effective, it may occasionally generate responses that are inaccurate, misleading, or incomplete. This is a known limitation of large language models and is sometimes referred to as "hallucination."

For example:

* Autopilot may suggest steps that do not apply to your current workflow.
* It may provide explanations that sound correct but are factually incorrect or based on outdated logic.
* When working with external information, such as documentation or web search, it may overlook important details or misinterpret source content.

Always review and validate its responses, especially when dealing with production workflows, data handling, or error-prone logic:

* Double-check suggestions before applying them, particularly in critical or high-risk workflows.
* Use the thumbs down button in the chat interface to flag unhelpful or incorrect responses.
* Review documentation links or search citations if provided. These often contain additional context not included in the summary.

Autopilot is a powerful assistant which works best as a collaborator, not a decision-maker. Your input and judgment remain essential for building safe, accurate, and effective automations.

## Feedback

Use the thumbs up and thumbs down feedback for all Autopilot responses. This helps us improve the future experience.