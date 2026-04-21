---
title: "Autopilot chat in UiPath products"
visible: true
slug: "autopilot-chat-in-uipath-products"
---

Autopilot offers a conversational framework that adjusts its capabilities based on the UiPath product you access it from. It is currently available in:

* [Orchestrator](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-orchestrator#orchestrator)
* [API workflows in Studio Web](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-studio-web#studio-web)
* [Studio 2025.10+](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-studio-desktop#studio)
* [Test Manager](https://docs.uipath.com/autopilot/other/latest/user-guide/autopilot-chat-in-test-manager#test-manager)


:::note
Each UiPath product where Autopilot chat is used features a specific suite of tools developed to help with your tasks. Consult the Connected sources section for details relevant to each product.
:::

## Maestro

The Autopilot chat in Maestro provides agentic capabilities to assist you in your BPMN modeling environment for various tasks. These capabilities include:

* Creating and editing BPMN models
* Writing expressions
* General Q&A about UiPath, RPA, BPMN, and the current model
* Suggestions for configuring activities
* Conversion from images and documents to BPMN models
* Preserving chat history and context across requests

### Connected sources

The Autopilot chat in Maestro leverages a range of built-in tools to support your modeling work. By default, all tools are enabled.

* **Web Search**—Answers questions that require updated, external information.
* **UiPath Documentation Search**—Retrieves content from UiPath official documentation.
* **Web Reader**—Extracts and summarizes content from public web pages when you provide a URL.
* **BPMN Q&A Agent**—Answers questions about BPMN standards, reviews diagrams for best practices, identifies potential issues, and helps you understand complex process flows.
* **BPMN Agent**—Creates and edits BPMN diagrams. Use this to design a new process from scratch, modify an existing one, or convert process descriptions from documents and images into a BPMN diagram on the canvas.


:::important
Autopilot for Maestro uses large language models (LLMs). Always review and validate the generated models, expressions, and explanations before you run them in production.
:::

### For BPMN modeling

Autopilot helps you build and evolve automation-ready BPMN workflows in Maestro using natural language and documents.

Use the chat to:

* Generate end-to-end BPMN diagrams from a plain-language description or from uploaded files.
* Add, remove, or reshape tasks, gateways, events, and subprocesses without manually placing every element.
* Propose and apply refactorings, such as splitting large tasks, introducing subprocesses, or improving parallelization.
* Author C# or JavaScript expressions for Script tasks, conditions, and data mappings, including complex logic.
* Explain what parts of the model do, including how data flows between activities and where errors might occur.
* Suggest validation and error-handling patterns, such as retries, timeouts, and compensation flows.
* Compare two process variants and highlight structural or behavioral differences.