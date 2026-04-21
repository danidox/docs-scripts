---
title: "User interface"
visible: true
slug: "user-interface"
---

API workflows are a new workflow tool within Studio Web. The designer canvas and side panels offer an updated experience, but the interface should feel familiar to users accustomed to traditional RPA workflows.

This documentation guides you step-by-step through each panel available.

## Explorer panel

![Explorer panel in API workflows](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/622241)

The **Explorer** panel gives you access to other projects within the solution.

To rename an API workflow, right-click on the parent folder and select **Rename**.

To share an API workflow across your organization, right-click the **API.json** file and select **Download file**.

## Debug configuration

![Debug configuration panel](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/622245)

The **Debug configuration** settings and the **Debug** functionality for the API workflow are located at the top of the page. These features are interconnected, as the **Debug configuration** allows you to specify your own data when testing workflows.

The **Debug configuration** is a flexible tool that lets you define and adjust JSON input data for testing and debugging.

## Publish

To publish the API workflow to the desired Orchestrator folder, such as your personal workspace or your tenant feed, select **Publish** next to the **Debug** button at the top of the page.

## Properties panel

![Properties panel](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/622250)

The **Properties** panel lets you configure each activity within an API workflow. When you add or select an activity in the designer canvas, the **Properties** panel opens automatically.

## Data manager panel

![Data manager panel](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/622254)

The **Data manager** panel lets you configure the request (input) and response (output) schemas for your API workflow.

## Deployment configuration panel

![Data manager panel](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/622309)

The **Deployment configuration** panel lets you configure all the assets used in your API wofklow, such as Integration Service connections, and add details about the deployment package, so you can easily turn it into a process in Orchestrator.

## Run output panel

![Run output panel](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/622279)

The **Run output** panel is the primary debugging tool for identifying errors or verifying that activities execute correctly. It allows you to evaluate the results of a workflow test run.

## Autopilot panel

![Autopilot panel](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/622270)

The Autopilot panel helps you create API workflows using simple, natural-language instructions. Instead of configuring complex workflows manually, describe your desired outcomes, and Autopilot translates your input into structured automation steps.

## Change history panel

![Change history panel](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/622294)

The **Change history** panel functions as a version control system for your API workflow, providing a complete audit trail of all committed changes.

* **Version iterations**—It logs the current and each published iteration of the workflow as a distinct, immutable version.
* **Read-only view**—You can access a read-only snapshot of any prior version to inspect the workflow state at that point in time.
* **State restoration**—You can revert the entire workflow current state to any previously saved version, effectively rolling back all subsequent modifications.