---
title: "Generating VB expressions using a text prompt"
visible: true
slug: "using-autopilot-to-generate-vb-expressions"
---

## Prerequisites

To generate VB expressions using text prompts, your tenant must have sufficient Autopilot actions available.

To generate VB expressions using a text prompt in Autopilot, follow these steps:

1. Go to the app where you want to add a VB expression.
   :::note
   * Referring to all controls within a container by the name of the container is not supported. If an expression depends on multiple
   controls, the prompt must include every control name.
   :::
2. Add a new control or select an existing control.
3. In the **Properties** panel**,** select a condition where you wish to add the VB expression. Select the configuration button, then select **Open expression editor.** The expression editor opens.

When you write a text prompt describing the VB expression you want to add, Autopilot writes the generated VB expression and makes it available for use in the **Expression editor** text field.

## Examples of Autopilot text prompts for VB expressions

Here are a few examples of useful prompts and their use cases.

| **Apps controls** | **Intended functionality** | **Text prompt examples** |
| --- | --- | --- |
| Input controls | Disables a **Submit** button if a field is empty. | "If username and password are empty set to true" |
| App variables | Enables a button if an app variable called "item list" has a length greater than 10. | "If item list length is greater than 10" |
| Custom objects | Prints a personalized welcome message. | "Concatenate "Welcome" with current user displayname and email id" |
| Media | Renders a media file you have added to the app. | Simply write the file name: "image_01" |
| Process | Completes a message with a value from a process. | "Concatenate user billing total amount" |
| Process and app variables (sorting and filtering) | Assigns a value from a process data table to an app variable data table. | "Sort `process users.datatable` by rating in descending order and filter where name contains john" |
| Custom function (string addition) | Adds a string to a list called "itemlist". | "Add `firstname` to `itemlist"` |
| Query parameters | Fetches runtime parameters given to the app in the form of a string. In this case, the time zone and region of a user. | "Concatenate apps timezone and region query parameters" |