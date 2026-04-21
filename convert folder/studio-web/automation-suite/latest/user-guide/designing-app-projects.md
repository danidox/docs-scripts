---
title: "Designing app projects"
visible: true
slug: "designing-app-projects"
---

## Creating an app project

Creating an app project is similar to creating a regular Studio Web project:

1. [Go to the Workspace page in Studio Web](https://studio.uipath.com/projects).
2. On the upper-right side of the page, select **Create New**.
3. Select **App**.
4. A new app project opens. Choose whether to start from a blank page or a template.

If you are already familiar with designing apps, the experience of building apps in Studio Web is similar to that described in the [Apps guide](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/using-app-studio).
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/486297)

From the ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/503577) **Project Explorer** button on the upper-left side of the designer, you can:

* Use the ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/503563) **Add** button to add pages, workflows, folders, actions, and variables to your app project.
  :::note
  To import pages from another project, select the **Import an item** option. This will open a pop-up where you can select the desired pages.
  :::
* Use the ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/503567) **Search** button to find specific project files.
* Manage your project files. Depending on the file type, you can rename, open, add, move, reorder, delete, duplicate, debug, or invoke files. You can also import individual pages and resources.

From the ![](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/503571)**Toolbox** button, you can add or search for [app controls](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/using-app-studio#adding-controls).

## Adding automations

After creating and designing your first app project, you can leverage the power of Studio Web automations integrated directly into your app.

In Studio Web, interactions with your app (also known as events) are controlled using activities to build automations, as opposed to [rules](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/about-events-and-rules).

To customize interactions within your app using automations:

1. Select an app element that supports events (for example, **Clicked On** or **Loaded**).
2. Open the **Properties panel** and navigate to the **Events** tab.
3. Click the **Define automation** button.

Studio Web automatically creates a workflow triggered by the selected event.
:::note
App elements that contain automations feature the icon next to their name in the **Project Explorer**.
:::
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/486309)

In this workflow, you can add, edit, and delete any activity that is available in Studio Web. The newly-created workflow appears in the **Project Explorer** and can be tested, renamed, and invoked in other workflows. You can also create other independent workflows from the **Project Explorer** and invoke them.
:::important
* App projects do not have a main workflow.
* You cannot set workflow triggers in an app project.
:::

## Passing values between the app and automations

[Variables](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/variables-in-apps) are used to pass values between your app and workflows.

To use an app variable or control value in a workflow, select **See more** &gt; **Use Variable** next to an activity input field.
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/488723)

The [Expression Editor](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/configuring-activities#expression-editor) offers you more options to use app variables in complex expressions.
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/486726)

You can also use the [Set Variable Value](https://docs.uipath.com/activities/other/latest/workflow/assign) activity to retrieve and set values for existing app variables. The activity has a drop-down menu which is automatically populated with the variables defined in the app. In the **Value** field, you can select any compatible data type variable from Studio Web or write an expression.
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/486538)

To pass an automation value to the value of a control in the app, either use the output of an activity in your workflow, or use a Set Variable Value activity to directly pass the value of a variable to the value of a control.