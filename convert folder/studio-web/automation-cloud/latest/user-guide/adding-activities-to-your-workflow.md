---
title: "Adding activities to a project"
visible: true
slug: "adding-activities-to-your-workflow"
---

Activities are executed in the order in which you add them to the project. To add an activity, click the **Plus** ![](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/StudioWeb/plus-add-activity.png) button in the location you want to add it in your workflow - before or after an existing activity, or inside a container activity.

A new window opens displaying all the available activities grouped by category. For example, the **Google Workspace** category groups all activities that automate Gmail, Google Drive, Google Sheets, and Google Calendar, while **UI Automation** contains all the activities that enable you to automate interactions with web pages.

To find the activity you need, search for the action you want to perform and check the results, or browse the list to see what activities are available for the categories you need. The six most recently used activities and categories across all your projects are displayed first.

The first time you add an activity from a category to a project, the activity package for that category is installed in the project, which can take a few seconds. When you then add other activities from the same category, they are added almost instantly.

The activities available in Studio Web are from official packages published and maintained by UiPath<sup>®</sup>. If preview activities and packages are enabled by your administrator, **Preview** ![](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/StudioWeb/preview.png) is displayed on the icon of pre-release packages and activities. Administrators can also enable the use of custom activities included in [libraries](https://docs.uipath.com/studio/docs/about-libraries) published to the Orchestrator libraries feed.

Some activities packages (for example, UI Automation) contain activities that are only usable in Studio Desktop. You can recognize these activities by the Studio Desktop ![](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/365967) icon next to their name. To see these activities in the list of available activities, toggle the **Show Studio Desktop activities** button at the bottom of the window. Adding a Studio Desktop activity prompts you to open the project in Studio Desktop and converts the project to the Windows compatibility. For more information, refer to [Opening a project in Studio Desktop](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/opening-a-project-in-studio-desktop).

To manage project dependencies, open the project in Studio Desktop. To learn more, refer to [Managing Dependencies](https://docs.uipath.com/studio/standalone/latest/user-guide/managing-dependencies) in the Studio user guide.

![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/359809)

## Adding activities with Autopilot™

When searching for an activity, you can use Autopilot™ to generate the next steps in your automation. To access this feature, simply describe in the search bar what you want to achieve and click the **Generate with Autopilot** option.

A new sequence is added to your workflow with an annotation that contains your instructions. You can choose to save this sequence and come back to it later or click the **Generate** button. If you choose the latter, Autopilot will then analyze your instructions, identify relevant activities, and add them in a logical sequence. If the instructions are not valid, you are asked to try a different description. While this process is running, you can cancel and return to the previously generated sequence.

After processing your instructions, a preview of the proposed workflow is created inside the sequence. The preview contains the activities that will be used in your automation, each with a descriptive name. Hovering over an activity reveals its standard name.

If you are not satisfied with the structure created by Autopilot, you can refine your initial instructions by clicking inside the annotation, editing the description, and selecting the **Generate** button again, which will create a new workflow preview.

After ensuring the workflow works as expected, select the **Confirm** button to have Autopilot build the workflow. Otherwise, select the **Cancel** button to discard the preview. By default, Autopilot keeps the sequence surrounding the resulting workflow, enabling you to further edit the generated workflow.

After the workflow is created, you can modify your instructions by clicking inside the sequence's annotation and repeating the process of generating a new workflow preview. If you wish to remove the sequence surrounding a generated workflow, select **Actions** ![](https://documentationpicturerepo.blob.core.windows.net/migrated/More_VT.png) next to the sequence's name and then the **Ungroup** option.

Apart from the new activity window, you can also use Autopilot to generate workflows from any sequence and scope activity, including sequences placed inside another sequence, by selecting **Actions**![docs image](https://documentationpicturerepo.blob.core.windows.net/migrated/More_VT.png) &gt; **Annotate with Autopilot**.

![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/399391)