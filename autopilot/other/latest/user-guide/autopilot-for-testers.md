---
title: "Generating tests"
visible: true
slug: "autopilot-for-testers"
---

## Overview

Autopilot helps you accelerate the testing lifecycle by generating, refactoring, and analyzing test cases using prompt-based generation. With a single natural language prompt, you can instruct Autopilot to create or modify manual, low-code, or coded test cases, directly within UiPath Studio or Test Manager.

This experience is non-conversational: you provide one prompt and Autopilot delivers the result. It is designed for quickly generating test assets or refining existing ones without switching contexts.

Autopilot integrates into your testing tools to streamline common QA tasks, helping teams design high-quality tests faster and with less manual effort.


:::tip
For an interactive, context-persistent, and chat-based experience, use the Autopilot chat. It offers similar generative capabilities, and allows you to refine tests, analyze failures, or explore results iteratively through natural conversation.
:::

:::note
To access the test generation capabilities, you first need to enable the Autopilot capabilities in Studio and Test Manager. For information on enabling and disabling Autopilot capabilities, visit [Enabling/disabling Autopilot](https://docs.uipath.com/autopilot/other/latest/user-guide/enable-disable-functionality).
:::

## Where test generation capabilities are available

* Test Manager – Use Autopilot to generate, import, and manage manual test cases, evaluate requirements, find obsolete or redundant tests, and analyze testing insights.
* Studio – Use Autopilot to generate, refactor, or enhance coded test cases, low-code tests, and API-based tests directly within your automation environment.

These integrations bring AI-powered testing assistance directly into the tools you already use for design, execution, and maintenance, ensuring consistency and speed across the testing lifecycle.

## Capabilities

Autopilot can help you:

* Evaluate requirements for quality aspects such as clarity, completeness, and consistency in Test Manager.
* Generate manual test cases and test steps for requirements and supporting documents in Test Manager.
* Import manual test cases from Excel files directly into Test Manager, while key data, such as title, description, and properties.
* Identify test cases that may no longer be relevant to an updated requirement.
* Generate manual test cases for SAP transactions in the Heatmap, and impacted transactions in Change Impact Analysis.
* Generate coded test cases from text or manual tests.
* Enhance existent coded automations using refactoring.
* Generate low-code test cases from text or manual tests.
* Generate coded test cases that employ APIs.
* Generate test data for your automations.
* Gain insights into why test cases are failing, without the need for pre-built reporting templates in Test Manager.
* Search any test object within a project, using natural language, and perform actions on the results.


:::note
Autopilot capabilities in Studio are available starting with Studio 2024.10.1, and 2024.10.5. For more information, visit the Studio [2024.10.1](https://docs.uipath.com/studio/standalone/2024.10/user-guide/release-notes-2024-10-1), and [2024.10.5](https://docs.uipath.com/studio/standalone/2024.10/user-guide/release-notes-2024-10-5) release notes.
:::

## Limitations

* When you evaluate the quality of a requirement, ensure that its description and supporting documents do not exceed the following limits: 128,000 tokens, which is equivalent to approximately 96,000 words, or 512,000 characters.
* When you evaluate the quality of a requirement Autopilot can generate a maximum number of 50 suggestions at a time. If a number of suggestions is not specified, then Autopilot generates the top 15 suggestions.
* You can only upload the following file extensions, when using Autopilot for testers:
  + Processes only text content – Autopilot processes only the text content from these file types:
    - TXT
    - BPMN
    - CSV
  + Processes both text and image content – Autopilot processes both the text and images from these file types:
    - DOCX
    - XLSX
    - PNG
    - JPG
    - PDF
* You can only generate test cases with maximum 50 steps.