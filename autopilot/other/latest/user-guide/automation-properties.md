---
title: "Tools"
visible: true
slug: "automation-properties"
---

## Overview

The **Tools** section helps you:

* Control which automation bundle to install, via the **Tools bundle** tab.
* Control how automations behave in Autopilot for Everyone, via the **Configure tools** tab.

## Tools bundle

Autopilot for Everyone comes with a catalog of automations ready for use, catering to multiple needs. When you install and deploy Autopilot, you also deploy a set of default automations, which were designed to satisfy the most common business requests. To leverage extended functionality, you can install additional automation toolsets from Autopilot for Everyone > **Tools bundle** tab.

The **Tools bundle** tab offers automatic installation of [additional toolsets from Marketplace](https://docs.uipath.com/autopilot/other/latest/overview/out-of-the-box-automations#marketplace-toolsets). It also provides version control: the **Version** column displays the current installed version, and the **Install status** column shows which tools might need installation or updates.


:::important
**Automation Cloud™ Public Sector limitation** Automation Cloud™ Public Sector users cannot automatically install additional toolsets. Instead, the **Tools bundle** tab provides instructions on how to manually download out-of-the-box automations to your local device and install them.
:::

## Configure tools

The **Configure tools** tab helps you control how automations behave in Autopilot for Everyone. Automation properties are stored as key-value pairs in Orchestrator, for each selected Autopilot process. Initially, all options are disabled until a folder is selected.

Once you select a folder from the **Orchestrator Folder** dropdown menu, the **Autopilot enabled processes only** option is displayed. If selected, it filters automations in that folder by those that have the `Autopilot` label. Otherwise, all automations in the folder are displayed.

Use the **Automation** dropdown menu to select a automation and configure its properties.

The properties are:

* **Automation prompt description—**Describes to Autopilot what the automation does. Accepts maximum 256 characters. If left blank, it uses the process description. Adds the following key-value pair in Orchestrator:
  + Key: `AutopilotPromptDescription`
  + Value: description of the process
* **Enable for Autopilot—**If selected, enables the automation in Autopilot, so it knows to recommend it in chat and to execute it. Adds the label "Autopilot" to the automation.
* **Set as pre-response action—**If selected, sets the automation as a pre-response action, meaning the automation runs in the background before Autopilot responds to the query. Autopilot can run up to six pre-response actions for a single prompt. If the automation has insufficient information to set up the pre-response action, it asks for additional data. For example, it might need to establish a new connection, scenario in which it displays a card prompting for a connection setup, or it may ask you for data in the chat. Autopilot also shares the execution status and, depending on the number of pre-response actions run, it displays either the automation name or "Searched multiple sources". Hovering over the "i" icon shows the executed automations and their inferred arguments. Adds the following key-value pair in Orchestrator:
  + Key: `AutopilotPreResponseAction`
  + Value: `True`
* **Output instructions—**Instructs Autopilot about the way the output should be displayed.
  + **Summarize the output in a user-friendly way—**Autopilot displays the automation output in a way that is easy for users to understand.
  + **Display the information in a table—**Autopilot displays the automation output in a tabular format.
  + **Display the output in bulleted form—**Autopilot displays the automation output as an unordered list.
  + **Display the entire output exactly in a readable format—**Autopilot displays the raw, unaltered automation output, but in a readable format. For example, if the output is an array, Autopilot displays it as a list, with each array element on a new line:
    ```
    [
      "Item 1",
      "Item 2",
      "Item 3"
    ]
    ```
* **Argument-level properties—**Configures the display and behavior of arguments in automation cards:
  + **Name—**The name of the argument as it appears in Studio. This field is read-only.
  + **Display name—**The name of the argument that should be displayed in the automation card.
  + **Description to user—**An additional description for the argument, to provide more context to the user.
  + **Description to Autopilot—**The description of the argument to the AI, to provide more context to Autopilot and how to infer its value.
  + **Dropdown options—**The comma-separated list of options that should be displayed if the argument type is a string. If provided, the argument field displays as a dropdown menu. Otherwise, the argument field displays a text box. These options are specifically interpreted by the automation, so it is important to limit user choices to predefined values. Allowing free text input can lead to automation failures due to unexpected or incompatible values.
  + **Hidden—**If true, forces the argument to be displayed in the collapsed **Hidden inputs** menu of the automation card.Adds a key-value pair in Orchestrator for each argument:
  + Key: argument name
  + Value: concatenated string of argument-level properties
    :::important
    Autopilot hides optional arguments that are not inferred.
    :::

When you are finished configuring the properties for a process, select **Save changes**. This overwrites the tags and the key-value pairs for the process in Orchestrator.

Select **Reset** to discard all changes, and reload the existing properties of the process.

## Managing automation properties

To edit the properties of an automation:

1. Navigate to the Automation Cloud™ > **Admin** > **AI Trust Layer** > **Autopilot for Everyone** tab, then choose the tenant where Autopilot for Everyone is installed.
2. Expand the **Tools** section, and select the **Configure tools** tab.
3. Select the **Orchestrator Folder** where the desired automation resides.
4. Optionally, select the **Autopilot enabled processes only** option. This sorts the automation list to display only the processes that have the `Autopilot` label.
5. Select the **Automation**.
6. In the **Automation prompt description** field, describe what the automation is expected to do.
7. If you want this automation to be identified and run by Autopilot in the chat, select the **Enable for Autopilot** option.
8. To have this automation execute before providing an answer to users in the chat, select the **Set as pre-response action** option. When the answer is generated, it contains information gathered from running this automation.
9. From the **Output instructions** dropdown, select how the automation output should be displayed to users.
10. Select **Save changes** to save the current configuration.

## Managing argument-level properties

If an automation has been designed with arguments, these are displayed as tabular data. To edit the argument-level properties of an automation:

1. Navigate to the Automation Cloud™ > **Admin** > **AI Trust Layer** > **Autopilot for Everyone** tab, then choose the tenant where Autopilot for Everyone is installed.
2. Expand the **Tools** section, and select the **Configure tools** tab.
3. Select the **Orchestrator Folder** where the desired automation resides.
4. Optionally, select the **Autopilot enabled processes only** option. This sorts the automation list to display only the processes that have the `Autopilot` label.
5. Select the **Automation**.
6. In the arguments table, select **Edit** for the desired argument. The **Updating automation properties** panel opens.
   :::important
   You cannot edit the **Name** field, as this is a value set at design time in Studio.
   :::
7. In the **Display name** field, write the name this argument should display to users in the automation card in the chat. For example, "Priority."
8. In the **Description to user** field, write the description the users should see in the automation card in the chat. For example, "Priority of the email."
9. In the **Description to Autopilot** field, write the description for the AI to interpret or understand it. It should offer context about what the argument is. For example, "The priority of the email. Choices include low, high. If not provided, default is low."
10. In the **Dropdown options** field, provide a comma-separated list of options available to users for selection. These options are specifically interpreted by the automation, so it is important to limit user choices to predefined values. Allowing free text input can lead to automation failures due to unexpected or incompatible values. For example, "Low, Normal, High".
11. To force the argument to be displayed in the **Hidden inputs** section of the automation card, select the **Hidden** option.
12. Select **Save** to update the argument-level properties. The panel closes and you are returned to the arguments table.
13. Select **Save changes** to save the current configuration.