---
title: "Configuring agentic process elements"
visible: true
slug: "configuring-agentic-process-elements"
---

Once you have modeled an agentic process in Studio Web, the next step is its implementation. Whether you created an agentic process from scratch or imported one, implementation is done primarily by selecting elements in the designer and configuring them in the **Properties panel**.

The Properties panel features several configuration sections depending on the type of element that is selected:

* **General** - Contains fields for information such as:
  + **Name** - The element label that you see in the designer.
  + **ID** - The system generated unique ID. This is the value used to reference the element in other properties and expressions.
  + **Description** - Additional details for the element.
* **Implementation** - Type-specific details for the selected element (such as actions, agents, or connectors).
* **Inputs** - Required or optional input data for the selected element.
* **Outputs** - Output data for the selected element. Outputs can be used as variables or expressions in other elements.

Selecting **See more** ![docs image](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/StudioWeb/see-more.png) next to a field displays the options for that field. The options for most fields are:

* **Use variable** - Selects an existing variable or element output value.
* **Open expression editor** - Opens the Expression Editor to build complex expressions.
* **Use JSON editor** - Opens the JSON Editor to build JSON input.
* **Date and time** - Opens the date and time builder.
* **Data fabric editor** - Opens the Data Fabric Editor to use properties from a data fabric entity.

Variables are used to configure element properties and pass values between your elements, automations, agents, app tasks, and connections. Element outputs are automatically available as variables throughout the process.

You can create variables by selecting the **Create new** button at the bottom of the Properties panel. Inside the **Add variable** window, you can assign a name and value to your variable and select the variable type (string, integer, float, double, or boolean).

The Expression Editor is used to write more complex expressions to configure element properties. The Expression Editor is available for most element properties and features intelligent code completion for variables, arguments, methods, properties, objects, or keywords. You can write expressions on multiple lines and use **Ctrl + Space** to see the list of available options. You can open the variable selection panel and select a variable, argument, or property. You can also provide and test values and see the output of an expression.

The JSON Editor is used to construct JSON input.