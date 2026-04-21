---
title: "Designing solutions"
visible: true
slug: "designing-solutions"
---

The design time experience has evolved from working on a single, standalone automation to designing an entire business process. Instead of editing a single, isolated automation, you can now work on multiple automations and their associated resources within the same solution.

Working with solutions allows you to:

* Define resources without leaving Studio Web.
* Design automations that reference defined resources before these resources are deployed in the UiPath platform. Automations interact with resource definitions in a contractual way, assuming that the resources exist with their specified definitions.

Each solution consists of one or several projects which can be managed from the **Solution Explorer**.

## The Solution Explorer

The **Solution Explorer** helps you manage the projects in your solution, as well as the project files in each project.

From the ![](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/548970) **Solution Explorer** button on the upper-left side of the designer, you can:

* Use the ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/548966) **Add to solution** button to:
  + Add a project to your solution (Agentic process, Agent, RPA Workflow, etc.).
  + Import an existing project.
* Use the ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/548974) **Search** button to find specific projects, files, pages, actions, variables, or arguments in your solution.
* Rename the solution by right-clicking it and selecting **Rename**.
* Open the **Properties** panel by right-clicking the solution, a project, or a file and selecting **Properties**. Here you can update its name and description.
* Move files and folders by dragging and dropping them in the desired location.
* Right-click a project to access project-specific options.
  :::note
  Windows projects are marked with a **Desktop** label and can only be edited in Studio.
  :::
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/605506)

A solution can be edited by multiple users simultaneously. However, only one user can work on a project at a time. Projects that are opened in another browser tab or by another user are marked with a lock icon in the **Solution Explorer**.

Project errors are visible to all users working on the same solution and are marked with an error icon in the **Solution Explorer**.
:::note
You cannot rename a project while another user is working on a project within the same solution.
:::
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/624890)

## The Resource Explorer

Resources added to your solution appear in a separate **Resource Explorer**, located at the bottom of the **Solution Explorer**. The Resource Explorer can be collapsed, expanded, or resized based on your needs.

Resources are automatically added to the solution as they are used by activities. Resources are grouped under these categories:

* **Apps** - User interfaces powered by automations that allow you to build custom business applications which connect to data.
* **Assets** - Shared variables or credentials that you can use in different automation projects.
* **Business rules** - Objects used to store and manage Decision Model and Notation (DMN) files.
* **Connections** - Integration Service connections that help in establishing tasks between single users and external applications.
* **Context** - Context Grounding indexes that give access to permissioned knowledge bases.
* **Processes** - Package versions linked to a particular folder.
* **Queues** - Containers that enable you to hold an unlimited number of items.
* **Storage buckets** - Per-folder storage solutions leveraged in creating automation projects.
* **Task catalogs** - Action containers where you can categorize your actions based on various criteria. The catalog that stores an action is set when an action is created, using action creation activities in Studio Web.
* **Dependencies** - Activity categories contextually linked into a specific project.

You can remove a resource by right-clicking it and selecting **Remove from solution**.

For more information on how to create, define, and use resources, refer to [Solution resources](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/solution-resources).

To learn more about solution-aware activities that leverage solution resources, refer to the [System activity package](https://docs.uipath.com/activities/other/latest/workflow/about-the-system-activities-pack), the [Persistence activity package](https://docs.uipath.com/activities/other/latest/workflow/about-the-persistence-activities-pack), and the [Integration Service user guide](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/connections#connections-in-solutions-management).
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/556124)

## The Data Manager

The **Data Manager** allows you to manage the data when working on an RPA workflow project that is part of your solution. This data includes:

* **Variables** - Store data and pass it between activities in a project.
* **Arguments** - Store data and pass it into or out of a project.
* **Entities** - Data Service records.

To learn more about the Data Manager, refer to [Managing the data in a project](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/managing-the-data-in-a-project#managing-the-data-in-a-project).

## The Errors panel

The **Errors panel** allows you to identify issues in the current RPA workflow project. To access the Errors panel for a project, select the ![](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/547990) icon on the upper-left side of the page. The number of identified issues is displayed next to the icon.

Opening the Errors panel shows you the list of identified errors or warnings. After selecting an error or warning, you can use the **Go to source** button to jump to the activity that has the incomplete or invalid configuration.

## The Toolbox

The **Toolbox** ![](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/503571) is visible in the context of working on an app project. From the Toolbox, you can add or search for [app controls](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/app-controls).

## The Deployment configuration panel

The **Deployment configuration panel** displays the components of the solution package. To access the Deployment configuration panel, select the ![](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/548023) icon on the upper-left side of the page.

You can change how the components are listed from the **View as list** and **View as tree** buttons. You can also use the **Search** button to find specific components.

Selecting a component allows you to review its properties. From the **Display** option, you can switch between viewing recommended properties or all properties.
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/580265)

## The Notifications panel

The **Notifications panel** lists cross-tenant notifications related to actions performed in the context of your solution. To access the Notifications panel, select the bell ![](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/548996) icon from the top navigation bar.

Notification can be filtered by the services they reference or by their severity.

To learn more, refer to [Notifications](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-notifications) in the Automation Cloud admin guide.