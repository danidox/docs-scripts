---
title: "Creating a project"
visible: true
slug: "creating-a-project"
---

There are multiple ways in which you can create a project. You can create a project from one of the available templates to get started quickly, create a project from scratch, import a project exported from Studio Web, duplicate one of your existing projects, or use Autopilot™ to generate a project using natural language instructions.

## Creating a project from a template

Templates are preconfigured projects that automate common scenarios. You can use a template as is or you can use it as a starting point for a new project to avoid starting from scratch. Templates are also a good way to learn how to automate.

By default, multiple templates created by UiPath® are available. You can also [create custom templates](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/creating-a-template-from-a-project) and make them available for everyone in the organization.

The first time you open Studio Web. you are prompted to select the department you work in and the services you use. The templates recommended to you are based on your selection.
:::tip
If you later switch to another department or start using new services, you can change your preferences at any time by selecting ![docs image](/images/studio-web/studio-web-image-More_VT.png) &gt; **Restart getting started** at the top of any page. The recommended automations are updated based on your new selection.
:::

The available templates are displayed on the **Templates** page. The following information is displayed for each template: name, description, how many times it was used in automations, template author, as well as details regarding the applications in the automation, and the type of trigger it uses.

Use the search box at the top of the page to search in the list of templates by name, description, and apps that are used (searching is limited to 256 characters). You can also filter the available templates by project type.

If you want to always see a template at the top of the list, select **More actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Pin** for that template.

To create a project from a template:

1. [Go to the Templates page in Studio Web](https://studio.uipath.com/templates).
2. Select the template you want to use.
3. On the template page, you can view the template details. Some templates require no configuration, while others may need additional configuration to customize them with your data. You can do that on the template page or after the project is created. For example, for the [Upload email attachments to OneDrive or SharePoint](https://cloud.uipath.com/portal_/cloudrpa?redirectPath=studio_/templates/058a5dd9-fdf9-45e9-af46-466fb61310e8) template that you can use to automatically upload attachments from new emails to OneDrive or SharePoint, you must configure the connections to use for Microsoft Outlook 365 and Microsoft OneDrive & SharePoint (you need to create them if they don't already exist). You can also enable the **Advanced configuration** option to further configure the template (for example, the email folder to monitor for new emails and the folder where to move the received email after it is processed).
4. Click **Use template**. If there is any required information you haven't provided, you are prompted to enter it. Select **Use template** to enter the information in the project later, or select **Keep editing** to go back and finish the configuration first.
5. The project is created and the workflow opens in the project designer.

If the project suits your needs, you can use it as is. Otherwise, you can edit it to make it work for you by editing the trigger, changing the activities it contains, removing or adding activities.

## Creating a project from scratch

1. [Go to the Workspace page in Studio Web](https://studio.uipath.com/projects).
2. On the upper-right side of the page, select **Create New**.
3. Select **RPA Workflow**.
4. A new solution opens, with the designer canvas displayed. To get started:
   1. Select how to trigger your automation - manually, on a schedule, or when an event occurs in an application. For more information, see .
   2. Give the project a name. The name is displayed on the upper-left side of the designer (by default *Untitled*). To edit it, right-click the project in the **Project explorer** and select **Rename**. Choose a descriptive name to make the project easy to identify.
   3. Click the **Plus** ![docs image](/images/studio-web/studio-web-image-plus-add-activity.png) button under the trigger activity and then add a first activity to start building your workflow.

## Importing a project downloaded from Studio Web

If someone sent you a project that they downloaded from Studio Web, you can import it to add it to your list of projects. Projects are exported as files with the UIP extension.

To import a project, drag a UIP file from the file explorer on your machine and drop it on the Workspace page. Alternatively:

1. Go to the **Workspace** page.
2. On the upper-right side of the page, select the arrow next to **New project**, and then select **Import project**.
3. In the import dialog, either select **Choose** to locate and open a UIP file from your machine, or drag a UIP file from your machine's file explorer and drop it in the dialog.
4. The imported project is added at the top of your projects list.

## Duplicating an existing project

You can create a copy of any of your existing projects by duplicating it.

1. Go to the **Workspace** page.
2. Select **See more** ![docs image](/images/studio-web/studio-web-image-More_VT.png) &gt; **Duplicate** next to the project to copy.

A new project is added at the top of your projects list. The name of the project is the name of the project you duplicated followed by `1`.

## Creating a project with Autopilot™

Autopilot™ lets you use natural language to describe the structure and outcome of a project. There are several ways in which you can use Autopilot to create a workflow:

* Selecting the **Generate with Autopilot** button next to the search box at the top of the Templates page.
* Selecting the **Autopilot** card in the list of available templates. The Autopilot card is the first option you see in either **Card view** or **List view**.
* Choosing **Generate with Autopilot** from the arrow next to **New project** in the upper-right side of the Workspace page.

Selecting any of the above options will open the **Generate with Autopilot** window.

In this window, you can type your instructions using natural language. You can also start from one of the predefined examples. As you type, Autopilot will suggest appropriate activities categories based on certain keywords. After typing your instructions, select the **Generate** button and Autopilot will create a preview of your workflow. While the preview is loading, you can select the **Stop** button to cancel the process.

The generated preview contains the trigger and activities that will be used in your automation. The trigger and activities do not appear with their default names, but have titles which match the instructions you have given. Hovering over the icon of a trigger or activity reveals its parent category.

If you are not satisfied with the structure created by Autopilot, you can always refine your initial instructions and resubmit, which will generate a new workflow preview. After ensuring the workflow works as expected, select the **Continue** button to have Autopilot build the entire automations as a new Studio Web project. Otherwise, select the **Cancel** button to return to the Templates page or the **Clear** button to delete the preview.

You can also expand the **Recent** drop-down menu to access a list of recently-used prompts and the **How to build a prompt** drop-down menu to see how to write effective prompts.

  ![docs image](/images/studio-web/studio-web-docs-image-445755.webp)