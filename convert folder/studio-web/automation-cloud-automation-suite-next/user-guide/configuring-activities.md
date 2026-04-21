---
title: "Configuring activities"
visible: true
slug: "configuring-activities"
---

Activities can receive data as input and can generate output data that can be used as input in other activities. Key activity options or properties are visible by default in activity cards, and if an activity has additional properties, you can configure them by selecting **Show additional properties**.

The **Properties panel** allows you to control how activity properties appear. You can also use this panel to change the name of the project or the name of the workflow that is selected in the **Project explorer**.

To access the panel, select the corresponding icon on the upper-right side of the project page. Inside the Properties panel, you can switch at any time between two views:

* **Canvas view** - All the properties of the selected activity appear in the activity card.
* **Panel view** - All the properties of the selected activity, including advanced properties, appear only in the Properties panel and the activity card is collapsed.

  ![docs image](/images/studio-web/studio-web-docs-image-404384.webp)

Selecting **See more** ![docs image](/images/studio-web/studio-web-docs-image-see-more.png) next to an activity field displays the options for that field. The options for most fields are:

* **Use variable**
* **Text builder**
* **Create variable**
* **Open expression editor**
  :::note
  The available options may vary depending on the data types associated with the field.
  :::

Dedicated input controls, editors, and builders are available to help you configure activities depending on the data type, either directly from the activity in the project designer, or from an editor or builder.

Some activities define a scope or the conditions to be met for the execution of other activities added inside them. These are called container activities, and examples include:

* [For Each](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/iterating-through-items) activities
  - Define a collection of items and repeat the activities added inside them once for each of those items.
* [If](https://docs.uipath.com/activities/other/latest/user-guide/if) - Evaluates a condition and determines the flow of the automation by executing specific activities based on whether the condition is met.
* [Use Browser](https://docs.uipath.com/activities/docs/n-application-card) - Attaches to a page in your browser and executes all the UI automation activities added inside it on that page.

The following sections describe how you can use some of the available editors and builders.

## Expression Editor

Write complex expressions to configure activity properties. The Expression Editor is available for most activity properties and features intelligent code completion for variables, arguments, methods, properties, classes, or keywords. You can write expressions on multiple lines and use Ctrl + Space to see the list of available options. You can also select **Insert variable** to open the variable selection window and select a variable, argument, or property.

Use Ctrl + F inside the editor to open the search and replace capabilities. The error icon indicates if there is an incompatibility between an expression and the activity property type (for example, using an expression of type **String** in a property of type **Boolean**).

You can test the value of valid expressions by selecting **Test**. Testing expressions that use complex values is currently not supported.

### Generate expressions using Autopilot™

You can also utilize natural language to describe your expression using Autopilot™ generative AI capabilities. Instead of manually writing an expression in the Expression Editor, you can use the generate expression field to describe your desired action (for example, “Extract the total revenue from the sales report”).

The AI model will generate an expression based on the provided description, which will then be displayed in the editor. You can then modify the generated expression or accept it as is. The AI model continuously learns from the descriptions you submit, allowing it to refine and improve its performance over time. The model is also capable of using user-defined variables and arguments and is aware of any expression already used.

Select the **Fix** button next to an error icon and Autopilot will try to fix the mismatch and provide a valid expression. An error message informs you if the expression cannot be fixed automatically.

### Example of using the Expression Editor with Autopilot capabilities

A simple way to test the capabilities of Autopilot is to transform a variable from lowercase to uppercase. To do this:

1. Create a new project with a manual trigger and create a new variable (for example, **MyVariable**).
2. Set the variable's type to **Text** and **Default value** to "example".
3. Add a [Set Variable Value](https://docs.uipath.com/activities/other/latest/workflow/assign) activity.
4. In the **Set value** field, select **See more** ![docs image](/images/studio-web/studio-web-image-More_VT.png) &gt; **Open expression editor**.
5. In the generate expression field, type your instructions in natural language (for example, "Convert `MyVariable` to uppercase").
6. Select to generate your expression. Optionally, select **Test** in the Expression Editor to test the new value of the variable.
7. Select **Save** to use the expression generated by Autopilot.
8. In the **To variable** output field, select **MyVariable**.

   ![docs image](/images/studio-web/studio-web-docs-image-381843.gif)
9. Add a [Log Message](https://docs.uipath.com/activities/other/latest/workflow/log-message) activity.
10. In the **Message** field, write the message you want to log (for example, "My variable, `MyVariable`, is now uppercase"), and select a log level.
11. Select **Debug on cloud** at the top of the designer to test the automation, and check the run output panel to see the variable changed from lowercase ("example") to uppercase ("EXAMPLE").

    ![docs image](/images/studio-web/studio-web-docs-image-381860.webp)

## Filter Builder

Create a complex filter with one or more conditions. Filters allow your automations to pinpoint the exact items that should be used. For example, most event triggers contain filters that help you determine the exact criteria an event must meet for the automation to start.

To build a filter:

1. Select the item to filter on from the field on the left. For example, when filtering emails, you can select an email field such as **From** or **Body**.
2. Select an operator from the dropdown in the middle to use for comparing the item. There are multiple operators you can choose from depending on the data type. For example, when filtering emails by sender, you can select the operator **contains** or **does not contain** for the From field.
3. Select from the field on the right the value with which to compare the selected item.

To create a filter with multiple conditions, click **Add condition** in the Filter Builder and build each additional condition in a similar way. When you add multiple conditions, a dropdown menu appears at the top of the window where you must select when the filter applies: select `All (AND)` if the filter applies when all the conditions are met, or `Any (OR)` if the filter applies when any of the conditions is met.

#### Example of building a filter

You are designing an automation that is triggered by the **File Created** event in [OneDrive](https://docs.uipath.com/activities/other/latest/user-guide/office365-trigger-new-file-created) or [Google Drive](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-trigger-new-file-created) and you only want the automation to run when files with the extensions are created: **pdf**, **tif**, **jpg**, **png**, **jpeg**.

1. In the trigger activity, select **Additional filters** to open the Filter Builder.
2. Add a condition for each file extension to include in the filter by selecting **Extension** from the first field, **contains** from the second field, and entering an extension in the third field.
3. Select **Any (OR)** from the dropdown at the top of the window to indicate that the creation of files with any of the extensions should trigger the automation.

   ![docs image](/images/studio-web/studio-web-docs-image-276038.webp)

## Condition Builder

Define a true or false statement that an activity evaluates to determine how the automation should continue.

To build a condition:

1. Select a first value to compare from the field on the left, for example a variable from your project.
2. Select an operator from the dropdown in the middle to use for comparing the first value. There are multiple operators you can choose from depending on the data type.: `greater than`, `greater than or equal`, `less than`, `less than or equal`, `equals`, `not equals`, `is empty text`, `is not empty text`, `is true`, `is false`, `starts with`, `does not start with`, `ends with`, `does not end with`, `contains`, `does not contain`, `has value`, `has no value`, `list is empty`, `list is not empty`.
3. Depending on the operator, you may also need to select from the field on the right a second value with which to compare the first value.

To create a statement with multiple conditions, click **Add** in the Condition Builder and provide the same information for each additional statement. When you add multiple statements, a dropdown menu appears at the top of the window where you must select when the statement is true: select `All (AND)` if the statement is true when all the conditions are met, or `Any (OR)` if the statements is true when any of the conditions are met.

#### Example of building a condition

You are designing an automation that moves every file that is created in a certain folder in your Google Drive or OneDrive to one of two folders based on the size of each file: files 1MB or over go to the **Big files** folder, while files under 1MB go to the **Small files** folder.

1. Configure the **File Created** trigger.
2. Add an **If** activity and click the **Condition** field to open the Condition Builder.
3. In the Condition Builder, add the condition "the file size is less than 1MB". We will use the **SizeInBytes** property of the created file, and 1MB = 1000000 Bytes.
   1. Click the first field, and select **File Created** &gt; **Show more** &gt; **File** &gt; **SizeInBytes**.
   2. From the middle field, select **less than**.
   3. In the third field, enter `1000000`, and then click **Save**.

   ![docs image](/images/studio-web/studio-web-docs-image-359828.webp)
4. We will then add two **Move File** activities to move the created file as follows:
   * One activity in the **Then** branch of the If activity. This is the activity executed when the condition is met (the file size is under 1MB) so we will select **Small files** as the destination folder.
   * The other activity in the **Else** branch of the If activity. This is the activity executed when the condition is not met (the file size is not under 1MB) so we will select **Big files** as the destination folder.

   ![docs image](/images/studio-web/studio-web-docs-image-386172.webp)

## Collection Builder

Create a collection of items of the same type.

To build a collection, select the item, and then select **Add entry** for each entry you want to add.

#### Example of building a collection

You are designing an automation that where you retrieved files in two different download activities. You then want to upload the files to OneDrive or Google Drive using one **Upload Files** activity.

1. In the Upload Files activity, select **See more** ![docs image](/images/studio-web/studio-web-docs-image-see-more.png) &gt; **Build a collection of files** next to the **File(s)** field.
2. Select **Click to open the collection builder**.
3. Select **Add**, then click the first field and select the output of the first Download File activity. Repeat for the output of the second activity, and then click **Save**.

   ![docs image](/images/studio-web/studio-web-docs-image-359844.webp)

## Date and Time Selector

Select a date from the calendar and a time of day (hour and minute). Available for fields that require a date and time value.

   ![docs image](/images/studio-web/studio-web-docs-image-275952.webp)

When using a variable in a field that accepts date and time values, snippets are also available, enabling you to quickly add common date and time variables:

* Today
* Yesterday
* Tomorrow
* Two Days Ago
* Start Of Last Workweek
* End Of Last Workweek
* Start Of Next Week
* Start Of Next Month
* Start Of This Week
* Start Of This Month
* Start Of Last Month
* Start Of This Year
* 3 Months Ago
* 6 Months Ago
* Now

## Data Mapping Editor

The **Data Mapping** editor simplifies end-to-end business processes automation involving complex data structures. Data mapping helps you map complex data objects between systems within a single Integration Service activity.

To access the Data Mapping editor:

1. Add an Integration Service activity to your workflow.
2. Select the **Switch to object view** button in the body of the activity.
3. Select the activity field you want to edit. The Data Mapping editor opens.

   ![docs image](/images/studio-web/studio-web-docs-image-569848.webp)

Alternatively, you can reach the Data Mapping editor by selecting **See More** ![](/images/studio-web/studio-web-image-549570.webp) &gt; **Data Mapping** next to the activity field.

The editor has two modes:

1. A standard mode that opens each time you access the editor. This is the default mode.
2. An advanced mode that you can enable from the **Advanced mode** toggle in the top-right corner of the editor.

Inside the standard mode, you can:

* Use the **Expand all** and **Collapse all** buttons to expand or collapse all nested object properties.
* Select the search icon to find a specific property or variable.
* View all the properties of the object in the **Destination properties** column. Some properties can be expanded to reveal additional nested properties (for example, properties of type list). Each property has a display name to easily distinguish it in the list, as well as the exact API name defined by the third-party application.
* Map an object property to an activity output in the **Mapping** column. Select the field next to each property and choose a variable from the **Use variables** selector. You can also select the **See more** ![docs image](/images/studio-web/studio-web-image-549570.webp) button to:
  + Open the **Use variables** selector.
  + Open the **Expression Editor**.
  + Clear any value in the activity output field.
* Select a variable that is available in the workflow from the **Available variables** column. Variables can be dragged and dropped inside the activity outputs listed under the **Mapping** column.
* Enable or disable **Advanced mode**. In advanced mode, you can only map properties by typing an expression or by using the **Use variables** selector. Dragging and dropping variables from the **Available variables** column is not available.
  :::note
  In Studio, the Data Mapping editor is only available in Advanced mode.
  :::

An error icon in the activity output field indicates if there is an incompatibility between a variable and the activity output type.

After mapping an object property to an activity output, select the **Save** button to record your changes.
:::note
If a nested property or a parent property is already mapped, the other cannot be mapped.
:::

Select **Switch to fields view** in the body of the activity to go back to updating activity fields inline.
:::important
To use the outputs created in the Data Mapping editor, ensure that you are using the activity in **object view**. If the activity is used in **fields view**, the mappings created in the Data Mapping editor are not considered when running the workflow.
:::