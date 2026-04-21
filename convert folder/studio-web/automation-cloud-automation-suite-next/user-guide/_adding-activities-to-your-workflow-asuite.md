---
title: "Adding activities to a project"
visible: true
slug: "adding-activities-to-your-workflow"
---

Activities are executed in the order in which you add them to the project. To add an activity, click the **Plus** ![](/images/studio-web/studio-web-image-plus-add-activity.png) button in the location you want to add it in your workflow - before or after an existing activity, or inside a container activity.

A new window opens displaying all the available activities grouped by category. For example, the **Google Workspace** category groups all activities that automate Gmail, Google Drive, Google Sheets, and Google Calendar, while **UI Automation** contains all the activities that enable you to automate interactions with web pages.

To find the activity you need, search for the action you want to perform and check the results, or browse the list to see what activities are available for the categories you need. The six most recently used activities and categories across all your projects are displayed first.

The first time you add an activity from a category to a project, the activity package for that category is installed in the project, which can take a few seconds. When you then add other activities from the same category, they are added almost instantly.

The activities available in Studio Web are from official packages published and maintained by UiPath<sup>®</sup>. If preview activities and packages are enabled by your administrator, **Preview** ![](/images/studio-web/studio-web-image-preview.png) is displayed on the icon of pre-release packages and activities. Administrators can also enable the use of custom activities included in [libraries](https://docs.uipath.com/studio/docs/about-libraries) published to the Orchestrator libraries feed.

Some activities packages (for example, UI Automation) contain activities that are only usable in Studio Desktop. You can recognize these activities by the Studio Desktop ![](/images/studio-web/studio-web-image-365967.webp) icon next to their name. To see these activities in the list of available activities, toggle the **Show Studio Desktop activities** button at the bottom of the window. Adding a Studio Desktop activity prompts you to open the project in Studio Desktop and converts the project to the Windows compatibility. For more information, refer to [Opening a project in Studio Desktop](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/opening-a-project-in-studio-desktop).

To manage project dependencies, open the project in Studio Desktop. To learn more, refer to [Managing Dependencies](https://docs.uipath.com/studio/standalone/latest/user-guide/managing-dependencies) in the Studio user guide.

:::note
Using Studio Web in an offline environment with an external Orchestrator host library feed requires the following activity categories to be available in the feed:
* `UiPath.System.Activities`
* `System.Activities`
:::

  ![docs image](/images/studio-web/studio-web-docs-image-359809.webp)