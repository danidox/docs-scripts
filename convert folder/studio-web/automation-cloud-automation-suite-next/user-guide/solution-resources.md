---
title: "Solution resources"
visible: true
slug: "solution-resources"
---

Different services in the UiPath Platform<sup>TM</sup> provide different types of resources. For example, Orchestrator has assets, queues, and storage buckets, Integration Service has connections, and Data Service has entities.

Solution resources are one of the key elements of solutions. While working with resources is not something new, we have improved how you use them in the context of a solution.

## Resource definitions

In regular automation projects prior to solutions, activities referenced real resources that already existed when the automation was designed. Solutions introduce the concept of **resource definitions**.

You can view a resource definition as all the necessary information to create a resource. A resource definition enables resource creation whenever needed:

* At design time, when you start working on a solution for the first time. Instead of manually creating the required resources in their respective services (such as Orchestrator), these resources are automatically created for your before starting to debug your solution.
  :::note
  Currently, Context Grounding indexes are not automatically created before debugging.
  :::
* At deployment time, when everything required by the automation(s) gets deployed at one. This is predictable and fast, with minimal chances of errors due to misconfiguration.

Solutions in the unified developer experience enable resource creation and configuration in Studio Web, without the need to navigate to other services.

## Selecting a resource

Selecting a resource in an activity makes the solution aware of that resource. This means that the resource can be easily referenced from other parts of the same automation project, or even from other automation projects in the same solution.

To choose a resource to work with:

1. Select an activity option in an activity that handles resources (for example, the **Queue name** option in an **Add Queue Item** activity).
2. Select the resource from the list of available resources.

When selecting a resource, you can either:

* Define a new resource.
* Select an existing resource available in the solution.
* Select an existing resources available in the UiPath Platform<sup>TM</sup>.

  ![docs image](/images/studio-web/studio-web-docs-image-580178.webp)

If your solutions contains multiple projects, you can reference the resulting artifact of a project as a resource inside another project by using activities such as **Start Job** (for RPA workflow projects) or **Create App Task** (for app projects).

## Defining a new resource

To define a new solution resource:

1. Open the solution in Studio Web.
2. Add an activity that handles solution resources (for example, **Add Queue Item**).
3. Select an activity option that allows you to define a resource (for example, **Queue name**).
4. Select the **+ Resource** button.
5. Configure your new resource in the resource properties window.
6. Select the **Return to workflow** button to navigate back to the designer. You can also select the **Dismiss** button to return to the designer without saving the resource. The new resource is now available in the Resource Explorer and in the **Defined resources** category in the activity option.
   :::note
   Selecting the **+ Resource** button in activities that allow you to reference a project inside another project automatically creates a new project inside the solution and selects the new project as a resource.
   :::

Creating a resource definition only adds the resource configuration to the solution and does not create the resource in the UiPath Platform<sup>TM</sup>. Following our previous example, the queue has not yet been created in Orchestrator. The resource only appears under the **In solution** category in the **Queue name** activity option.

The resource is created in your Personal Workspace during the first debugging session only if does not already exist or if debugging is configured to use an existing solution.

   ![docs image](/images/studio-web/studio-web-docs-image-549026.webp)

## Selecting an existing solution resource

To select a resource that already exists in the UiPath Platform<sup>TM</sup> (for example, from Orchestrator), simply choose the resource from the **Platform resources** category in the activity option. You can also use the **Open Orchestrator** button to manage platform resources in Orchestrator.

## Selecting an existing platform resource

When you select a resource that is not already part of the solution, the solution becomes aware of the resource. This means that the solution:

* Adds the resource to the list of available solution resources. The resource thus becomes available for use throughout the solution.
* Copies the resource definition, enabling you to create the resource whenever needed.
* Keeps the link to the selected resource for debugging sessions.
  :::note
  If you select a resource that was previously selected in the same solution, the existing resource is used.
  :::