---
title: "Automation Configuration"
visible: true
slug: "process-configuration"
---

Automation configuration allows you to change how an automation runs and what details it has.

You can set values for arguments directly from the UiPath Assistant which are saved and used every time the automation is run, making it easier to work with automations that require custom inputs and removing the need to create a new automation each time a value changes.

Input arguments can be found under the **Customize** section and are used to configure automations that make use of such variables.

Besides arguments, you can also configure an automation to always start in a [PiP Session](https://docs.uipath.com/assistant/standalone/2024.10/user-guide/picture-in-picture) from the same menu.

When an automation that contains arguments with the direction In is run for the first time, the UiPath Assistant automatically prompts you to provide values for the input arguments that do not have a default value that contains mandatory arguments.

## Configure Input Arguments

1. When you click an automation, detailed information is displayed in the right panel.
2. Set the value, and then click **Save**. The way in which you set the value of an argument depends on its type:
   * Int32 - enter a number
   * String - enter text
   * Boolean - select or clear a checkbox
   * DateTime - pick a date or time
     :::important
     The automations can also run with arguments that have other data types than the ones above, but those arguments are not displayed in Assistant. The values for these arguments are configured in Studio or in Orchestrator. In case the automation has default values both in Studio and Orchestrator, the values from Orchestrator will be used in Assistant.
     :::
:::note
The message `Use default value` means that the automation uses the default value set in Studio or Orchestrator. You can override this by pressing the **Edit** button ![docs image](/images/assistant/assistant-docs-image-252826-983205df.webp), or you can return to the default value by pressing the **Revert** button ![docs image](/images/assistant/assistant-docs-image-252830-ca541ec6.webp).
:::

## Configure Start in PiP

1. Hover over an automation and select **More actions**![docs image](/images/assistant/assistant-docs-image-253243-6683d327.webp) > **Show automation details**.
2. Under Picture in Picture, turn on the **Start in PiP** toggle. The next time you run the automation, it starts in a PiP session.

## Connections in UiPath Assistant

[Connections](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/connectors) can be used directly from the UiPath Assistant by accessing the **Automation Details** menu.

If an automation already has connections set up in Orchestrator, the user is able to select it from the list; otherwise, they can create a new one from the same menu.