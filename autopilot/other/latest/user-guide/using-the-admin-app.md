---
title: "Using the Admin App"
visible: true
slug: "using-the-admin-app"
---

To access the Admin App, you need to be assigned to the Orchestrator folder where the Admin App has been deployed. Use the Admin App to add custom starter prompts and to configure properties for the automations in your personal workspace.

1. In Assistant, log in to the organization and tenant that hosts the Admin App.
2. Find the Admin App in the **Apps** list on the **Dashboard** tab, and **Run** it.
3. To customize starter prompts, select the **Customize Starter Prompts** card, or the **Custom Starter Prompts** tab.
   1. To add a new prompt, select **Add new prompt**. This opens the Add new prompt dialog.
   2. In the **Department** field, write the name of the department for which the new starting prompt should apply.
   3. In the **Category** field, write the name of the category for which the new starting prompt should apply.
   4. In the **Prompt displayed to the user** field, write the title of the starting prompt displayed upon start-up.
   5. In the **Prompt** field, write the prompt that that appears in the chat box.
      :::important
      If you want to include placeholders, make sure to surround the placeholder text between triple chevrons `<<<` `>>>`.
      :::
   6. Select **Add** to complete the addition process.
   7. To upload multiple custom prompts at once, select [**Upload**](https://docs.uipath.com/autopilot/other/latest/user-guide/stating-prompts#uploading-starting-prompts).
   8. To download the existing custom prompts, select [**Download**](https://docs.uipath.com/autopilot/other/latest/user-guide/stating-prompts#downloading-starting-prompts).
   9. Save your changes by selecting **Publish changes**, then restart Autopilot for everyone.
4. To customize properties for the automations in personal workspace, select the **Automation Property Manager** card, or the **Automation Properties** tab:
   1. Optionally, select the **Autopilot-enabled processes only** option. This sorts the automation list to display only the processes that have the `Autopilot` label.
   2. The **Automation Name** list displays only the automations in your personal workspace. Select one to configure it.
   3. In the **Automation prompt description** field, describe what the automation is expected to do.
   4. If you want this automation to be identified and run by Autopilot in the chat, select the **Enable for Autopilot** option.
   5. To have this automation execute before providing an answer to users in the chat, select the **Set as data source** option. When the answer is generated, it contains information gathered from running this automation.
   6. If the automation has been designed with arguments, these are displayed in the arguments table. To edit the argument-level properties of the selected automation, double-click each field.
   7. In the **Display name** field, write the name this argument should display to users in the automation card in the chat. For example, "Priority."
   8. In the **Argument prompt description** field, write the description for the AI to interpret or understand it. It should offer context about what the argument is. For example, "The priority of the email. Choices include low, high. If not provided, default is low."
   9. In the **Description to user** field, write the description the users should see in the automation card in the chat. For example, "Priority of the email."
   10. In the **Dropdown options** field, provide a comma-separated list of options available to users for selection. These options are specifically interpreted by the automation, so it is important to limit user choices to predefined values. Allowing free text input can lead to automation failures due to unexpected or incompatible values. For example, "Low, Normal, High".
   11. To force the argument to be displayed in the **Hidden inputs** section of the automation card, select the **Hidden** option.
   12. Hit Enter, then select **Update** to save the current configuration.
   13. Save your changes by selecting **Publish changes**, then restart Autopilot for everyone.