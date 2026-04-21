---
title: "Starting prompts"
visible: true
slug: "stating-prompts"
---

Starting prompts are predefined instructions aimed to provide effective instructions on executing common tasks. You can create starting prompts based on the department they apply to, such as "General," "Sales," or "HR," and on the category of action they initiate, such as creating, analyzing, scheduling, or optimizing.

## Default versus customized prompts

If no customized prompts exist in any folder you can access, Autopilot displays a set of default prompts. Once you add even a single custom starting prompt, the default ones are no longer displayed. When defining a starting prompt, you must provide a department and a category. All changes are captured in the `starting_prompts.json` file, which is generated automatically when you add the first custom prompt. You can find it in the **Autopilot Document Config** storage bucket of the selected folder.

## Prompts displayed to users

If you have access to multiple folders and each one has a set of starting prompts defined, Autopilot aggregates all the prompts and displays them at startup. Duplicate entries are removed.

## Featured prompts

You can feature, or pin, starting prompts. Featured or pinned prompts are always visible at the top of the list in the UI upon start up.

## Placeholders in prompts

To include placeholders in starting prompts, surround them with a pair of triple chevrons `<<<` `>>>`. Users can identify placeholders by the blue highlight around them, which indicates that they should be replaced. For example, if a user selects the prompt "Give me weather information for `<<<`location`>>>`.", the user can replace `<<<`location`>>>` with the name of their current city. Then Autopilot fetches data for that specific location and provides an answer.

## Viewing the starting prompts in a folder

When you first access the **Starting prompts** panel, no folder is selected, and no starting prompts are displayed.

To display the starting prompts in a specific folder, select the folder from the **Orchestrator folder** dropdown menu. The **Configured folders only** checkbox next to the folder dropdown menu allows you to sort the list to display only the folders that have custom starting prompts predefined. Leaving this option clear displays all the folders in the tenant you can access.

Once you select a folder, the following options become active:

* **Upload** - allows you to upload a CSV file containing multiple custom starting prompts.
  :::important
  Existing starting prompts in the folder are overwritten.
  :::
* **Download** - allows you to download the current starting prompts to a CSV file.
* **Create new** - allows you to add a new starting prompt in the selected folder.

## Adding starting prompts

To add a new starting prompt:

1. Navigate to the Automation Cloud™ > **Admin** > **AI Trust Layer** > **Autopilot for Everyone** tab, then choose the tenant where Autopilot for Everyone is installed.
2. Expand the **Starting prompts** settings section.
3. From the **Orchestrator Folder** dropdown, select the folder where you want to add new prompts.
4. To filter the folders that have custom starting prompts predefined, select the **Configured folders only** checkbox. Leaving this option clear displays all the folders you can access in the selected tenant.
5. Select the **Create new** option. The **Creating new starting prompt** panel opens.
6. In the **Department*** field, write the name of the department for which the new starting prompt should apply.
7. In the **Category*** field, write the name of the category for which the new starting prompt should apply.
8. In the **Prompt displayed to the user*** field, write the title of the starting prompt displayed upon start-up.
9. In the **Prompt sent to AI*** field, write the prompt that that appears in the chat box.
   :::important
   If you want to include placeholders, make sure to surround the placeholder text between triple chevrons `<<<` `>>>`.
   :::
10. If you want this starting prompt to always show up in the Autopilot chat, select the **Display prompt as featured prompt** option.
11. To prompt users to upload files, select the **Require a file upload along with prompt** option.
12. Select **Save** to create the starting prompt. The panel closes and you are returned to the **Starting Prompts** table.
13. Select **Save Changes**. This generates the `starting_prompts.json` file and automatically creates the storage bucket in the selected folder, but only if these don not exist already. The JSON file should contain all the previously added prompts.

## Editing starting prompts

To edit an existing prompt:

1. Navigate to the Automation Cloud™ > **Admin** > **AI Trust Layer** > **Autopilot for Everyone** tab, then choose the tenant where Autopilot for Everyone is installed.
2. Expand the **Starting prompts** settings section.
3. From the **Orchestrator Folder** dropdown, select the folder containing the prompt you want to edit.
4. To filter the folders that have custom starting prompts predefined, select the **Configured folders only** checkbox. Leaving this option clear displays all the folders you can access in the selected tenant.
5. For the desired prompt, select **Edit**. The **Updating starting prompt** opens.
6. Modify the desired properties as needed.
7. Select **Save** to update the starting prompt. The panel closes and you are returned to the **Starting Prompts** table.
8. Select **Save Changes** to update the corresponding `starting_prompts.json` file.

## Deleting starting prompts

To delete an existing prompt:

1. Navigate to the Automation Cloud™ > **Admin** > **AI Trust Layer** > **Autopilot for Everyone** tab, then choose the tenant where Autopilot for Everyone is installed.
2. Expand the **Starting prompts** settings section.
3. From the **Orchestrator Folder** dropdown, select the folder containing the prompt you want to delete.
4. To filter the folders that have custom starting prompts predefined, select the **Configured folders only** checkbox. Leaving this option clear displays all the folders you can access in the selected tenant.
5. For the desired prompt, select **Delete**. A confirmation message is displayed.
6. Select **Confirm** to delete the prompt, or **Cancel** to dismiss the action.
7. Select **Save Changes** to update the corresponding `starting_prompts.json` file.

## Reverting to default prompts

Adding even a single custom starting prompt removes all default ones. To continue to use them, select the **Add default prompts** option. This appends the default prompts to the list. Remember, changes apply only after selecting **Save changes**.

## Downloading starting prompts

To download the current list of starting prompts for the selected folder, select **Download**. This saves the `starting_prompts.csv` file in the Downloads directory on your device. If no prompts exist in the folder, a blank CSV is downloaded.

The CSV file has the starting prompt properties as headers: `department`, `category`, `title`, `prompt`, `isFeatured`, `requiresFileUpload`.

## Uploading starting prompts

To add multiple starting prompts at once, select **Upload**. This action opens the **Upload starting prompts** panel. Ensure you have a prepared CSV file with these headers in order: `department`, `category`, `title`, `prompt`, `isFeatured`, `requiresFileUpload`. The values for these headers should adhere to the following:

* `department`: the name of the department to which the prompt applies
* `category`: the name of the category to which the prompt applies
* `title`: the title of the starting prompt
* `prompt`: the prompt displayed in the chat box
* `isFeatured`: use TRUE to pin the prompt; use FALSE otherwise
* `requiresFileUpload`: use TRUE if uploading a file is necessary; use FALSE otherwise