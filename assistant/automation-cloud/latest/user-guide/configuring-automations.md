---
title: "Configuring automations"
visible: true
slug: "configuring-automations"
---

Automations that require configuration display the **Configuration** tab when selected.

You can configure input arguments or connections.

## Input arguments

The message **Use default value** means that the automation uses the default value set in Studio or Orchestrator. To override the default value, select **Edit**. To return to the default value, select **Revert**.

Input arguments can have the following data types:

* Int32—provide a number
* String—provide text
* Boolean—select or clear a checkbox
* DateTime—pick a date or time

Automations also use other data types, but those do not appear in Assistant Web. You configure their values in Studio or Orchestrator. If an automation has default values in both Studio and Orchestrator, Assistant Web uses the values from Orchestrator.

## Connections

[Connections](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/connectors) can be used directly from Assistant Web from the **Configure** tab.

If an automation already has connections set up in Orchestrator, you can select it from the list. Otherwise, you can add a new one.