---
title: "FAQ"
visible: true
slug: "solutions-faq"
---

## Does it matter which "type" of solution I create?

No, solutions do not have a specific "type". A solution is simply a container that groups automations and related resources. The behavior of a solution is determined by the automations it contains. When you create a new solution, you select the automation type from which you will start building your solution.

## My business process requires an automation. What options do I have?

When designing an automation, you may need to execute logic from another automation. The following options are available:

1. Define the automation in the solution by adding a new project of that specific type. You can thus fully control how the automation works.
2. Import an existing project in your solution. This copies the project into the solution, so the original project remains unchanged and continues to exist independently.
3. Reference a deployed process from the UiPath Platform. This copies the process definition from Orchestrator without including the source code. However, when you publish the solution, the underlying NuGet package is also included in the solution package.

## I updated a process outside my solution. How do I update its definition in the solution?

If you work on a separate automation that is published and deployed independently, you can update its definition in the solution to reference the latest version from the **Deployment configuration** panel.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615004)

## How do I migrate my existing projects to a solution?

You can import your existing projects into a solution. Importing does not change the original project, but creates a copy of it within the solution.

## I get a "Failure to start the Orchestrator RPA job" error. What do I do?

This error occurs when an automation in the solution attempts to start another automation. Let’s look at the following example featuring a solution with two projects —an agentic process (Maestro) that calls an assistant agent:
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615150)

You start by debugging the agent first (the **Deploy resources before debugging** option in the **Debug configuration** window is disabled):
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615154)

The agent runs successfully in debugging, as expected:
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615158)

Next, you want to debug the agentic process that calls the agent (again, the **Deploy resources before debugging** option is disabled):
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615162)

Unfortunately, an error appears in the agentic process. Why does this happen?
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615166)

The error occurs because when you debug a project, it is not deployed anywhere. The project runs directly in a "Studio Web Debugging" job. In this case, since you debugged each project individually with the **Deploy resources before debugging** option disabled, neither project was ever deployed to any folder.

The **Output** panel offers this explanation:
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615170)

Fortunately, there is an easy fix. When debugging a project that has dependencies (such as an agentic process), make sure to deploy the dependent projects first. You can do this in one of two ways:

1. Enable the **Deploy resources before debugging** option in the **Debug configuration** window to deploy the latest resources to your personal workspace:
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615174)
2. Navigate to **Debug** &gt; **Deploy Project for Debugging**. This will deploy all projects to your personal workspace so they can be referenced by other projects (such as the agentic process) during debugging.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615178)

You can then view these deployments in your debug solution folder in your personal workspace:
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615182)

You can now see that the agentic process executes successfully after choosing one of the two options:
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615186)