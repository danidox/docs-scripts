---
title: "Rule: Submit Action"
visible: true
slug: "rule-submit-action"
---

Use the **Submit Action** rule to save and submit the changes made by a user upon completing a form or a certain UI interaction.

:::important
This rule becomes available for selection only after you add an action definition to your app.
:::

![docs image](/images/apps/apps-docs-image-346617-645d5568.webp)

## Action schema

This section displays the name of the action definition used in your app.

:::note
As only one action definition per app is allowed, this field is automatically filled in.
:::

## Input Override

In this section you can set values for the input arguments of the action.

Clicking the **Input Override** field opens the **Resources** panel, which displays the available input or input/output parameters of the selected action.

Select the parameters, and set them to the values of your app input controls.

Action properties, whether they are input or input/output parameters, can be accessed using the following syntax:

`ActionProperties.<action_property_name>`

The value expression of an app control has the following syntax:

`<Apps_MainPage_name>.<input_control_name>.value`

**For example:** You have the "name" input parameter in your "Voting App" action. You have a text control in your app called "text1". To bind the input parameter to the control value in Apps:
1. Select the "name" input parameter from the **Resources** panel. It should populate the field with the following expression:
   ```
   ActionProperties.Voting_app.name
   ```
2. In the **Enter value** field, set the following value to the "name" parameter:
   ```
   MainPage.text1.Value
   ```

:::note
You can add many input overrides as the number of your action input parameters.
:::
:::important
You should apply the input override for all action parameters you want to temporarily save, or send while submitting the action.
:::

## Action outcome

In this section, you can configure the outcome for completing the action.

The outcome options are defined in the definition schema of your action.

## On error

In this section, you can define rules to be executed when submitting the action encounters an error.

**For example:** To track the failure, you can add a **Show Message** rule. You can then specify the title, message, and type of the error.

## Rule output properties

* **Error -** references the error message shown if the job fails.