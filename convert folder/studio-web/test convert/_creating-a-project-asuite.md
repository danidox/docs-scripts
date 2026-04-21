---
title: "Creating a project"
visible: true
slug: "creating-a-project"
---

There are multiple ways in which you can create a project. You can create a project from one of the available templates to get started quickly, create a project from scratch, import a project exported from Studio Web, or duplicate one of your existing projects.

## Creating a project from a template

Templates are preconfigured projects that automate common scenarios. You can use a template as is or you can use it as a starting point for a new project to avoid starting from scratch. Templates are also a good way to learn how to automate.

You can [create custom templates](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/creating-a-template-from-a-project) and make them available for everyone in the organization.

Use the search box at the top of the page to search in the list of templates by name, description, and apps that are used (searching is limited to 256 characters). You can also filter the available templates by project type.

If you want to always see a template at the top of the list, select **More actions** ![](https://documentationpicturerepo.blob.core.windows.net/migrated/More_VT.png) &gt; **Pin** for that template.

To create a project from a template:

1. [Go to the Templates page in Studio Web](https://studio.uipath.com/templates).
2. Select the template you want to use.
3. On the template page, you can view the template details. Some templates require no configuration, while others may need additional configuration to customize them with your data. You can do that on the template page or after the project is created.
4. Click **Use template**. If there is any required information you haven't provided, you are prompted to enter it. Select **Use template** to enter the information in the project later, or select **Keep editing** to go back and finish the configuration first.
5. The project is created and the workflow opens in the project designer.

If the project suits your needs, you can use it as is. Otherwise, you can edit it to make it work for you by editing the trigger, changing the activities it contains, removing or adding activities.

## Creating a project from scratch

1. [Go to the Automations page in Studio Web](https://studio.uipath.com/projects).
2. On the upper-right side of the page, select **New project**.
3. Your new project opens. To get started:
   1. Select how to trigger your automation
      - manually, on a schedule, or when an event occurs in an application. For more information, see .
   2. Give the project a name. The name is displayed on the upper-left side of the designer (by default *Untitled*). To edit it, right-click the project in the **Project explorer** and select **Rename**. Choose a descriptive name to make the project easy to identify.
   3. Click the **Plus** ![docs image](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/StudioWeb/plus-add-activity.png) button under the trigger activity and then add a first activity to start building your workflow.

## Importing a project downloaded from Studio Web

If someone sent you a project that they downloaded from Studio Web, you can import it to add it to your list of projects. Projects are exported as files with the UIP extension.

To import a project, drag a UIP file from the file explorer on your machine and drop it on the Automations page. Alternatively:

1. Go to the **Automations** page.
2. On the upper-right side of the page, select the arrow next to **New project**, and then select **Import project**.
3. In the import dialog, either select **Choose** to locate and open a UIP file from your machine, or drag a UIP file from your machine's file explorer and drop it in the dialog.
4. The imported project is added at the top of your projects list.

## Duplicating an existing project

You can create a copy of any of your existing projects by duplicating it.

1. Go to the **Automations** page.
2. Select **See more** ![docs image](https://documentationpicturerepo.blob.core.windows.net/migrated/More_VT.png) &gt; **Duplicate** next to the project to copy.

A new project is added at the top of your projects list. The name of the project is the name of the project you duplicated followed by `1`.