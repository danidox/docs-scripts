---
title: "January 2024"
visible: true
slug: "january-2024"
---

## 31 January 2024

### Improved trigger testing

When you in a project, the **Output** panel now displays the properties and returned test values of any matching item that is found. If a match is not found, other recent items are suggested and their properties and returned test values are displayed. To make it easier to use the trigger output, the returned values are also displayed when you select the trigger output variable in other activities later in a project.

The improved experience is available for event triggers that use Integration Service connections.

![Trigger testing](/images/sw/release-notes-trigger-testing-359382.webp)

### Improved experience of using variables

We've made a number of improvements that make it easier to work with variables:

* When an automatically generated output variable is added in an activity field or editor, the entry displays the icon of the activity which outputted the variable. In addition, variables have a shorter name and a more readable tooltip displayed on mouse hover.

  ![Activity field](/images/sw/release-notes-activity-field-359389.webp)
* The most common properties of variables are now displayed at the top of the list in the variable selection window. To access all variable properties, use the new **Show more** button.

  ![Use variable](/images/sw/release-notes-use-variable-359660.webp)
* The option to create a variable is now available in the **See more** ![docs image](/images/sw/release-notes-docs-image-see-more.png) menu of all activity fields where you can use a variable.

### More governance options

Governance policies now enable administrators to configure whether preview activities and packages are available to users, and control which activities and packages can be used in Studio Web. For more information, refer to the [Automation Ops User Guide](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-studio-web-policies).

## 29 January 2024

### Projects with multiple workflows

You can now create Studio Web projects with multiple workflows. This enables you to split larger projects into smaller files, making it easier to organize your automations and test workflows separately. Use the [Invoke Workflow File](https://docs.uipath.com/activities/other/latest/workflow/invoke-workflow-file) activity to link the workflows to the main workflow. You can manage the workflows from the new **Project explorer** available in your projects.

In projects that are also edited in Studio Desktop, the Project explorer is where you can access the entire folder structure, but you can only edit sequences. Other types of files such as flowcharts and state machines are not supported in Studio Web.

For more information, refer to.