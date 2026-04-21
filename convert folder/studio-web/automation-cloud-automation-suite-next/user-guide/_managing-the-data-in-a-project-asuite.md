---
title: "Managing the data in a project"
visible: true
slug: "managing-the-data-in-a-project"
---

The **Data Manager** allows you to manage the data in an automation project. This data includes:

* **Variables** - Store data and pass it between activities in a project.
* **Arguments** - Store data and pass it into or out of a project.
* **Entities** - Data stored in records from [UiPath<sup>®</sup> Data Fabric](https://docs.uipath.com/data-service/automation-cloud/latest/user-guide/introduction), a centralized data modelling and storage service.

To access the Data Manager for a project, select the ![docs image](/images/studio-web/studio-web-docs-image-data-manager.png) icon on the left side of the Designer panel.

  ![docs image](/images/studio-web/studio-web-docs-image-613671.webp)

## Variable and argument types

Variables and arguments have different types depending on the data they store. There are multiple types of variables and arguments that you can create in Studio Web, the following being the most commonly used:

* **Text** - Stores text data. This type can be used to store any text-based information such as employee names, usernames, and any other string.
* **Number**- Stores numbers without decimals. You can use it to perform calculations, equations, and comparisons.
* **True or false** - Also called Boolean, this type has only two possible values, true or false. These enable you to make decisions and control the flow of your automation.
* **Number with decimal**- Similar with number, but useful when you need to use decimals for more precision.
* **Date** - Stores an instance in time represented by the date, hour, and minute.
* **File** - Stores a file or folder as a resource you can use in your project.
* **List** - Stores multiple values of the same type (text, number, true or false, number with decimal, date, or file). You can manipulate lists in your project by adding or removing values.
* **Array []** - Stores a fixed number of multiple values of the same type (text, number, true or false, number with decimal, date, or file).
* **Dictionary** - Stores a collection of key-value pairs. You select the data type for both the keys and the values (text, number, true or false, number with decimal, date, or file). The data type can differ between keys and values.

If you need to use a different data type, when you create a variable or an argument, select **Advanced types** to explore all available data types.

## Advanced data types

The date and time data type enables you to store information about any date and time. Keep these guidelines in mind when working with date and time formats:

* To output a date (without time), select the **DateOnly** advanced data type. For example, you can use:
  + `DateOnly.FromDateTime(DateTime.Now)`
  + `DateOnly.FromDateTime(DateTime.Parse("2024/05/30"))`
* To output a date with time, select the **Date** advanced data type. For **Date** outputs, the time zone is mandatory. If no time zone is specified, the output is rejected as not ISO compliant. For example, you can use:
  + `DateTime.SpecifyKind(DateTime.Now, DateTimeKind.Local)`
  + `DateTime.SpecifyKind(DateTime.Parse("2024/05/30T12:24:00"), DateTimeKind.Local)`

The last parameter can be either `DateTimeKind.Local` or `DateTimeKind.Utc`. Do not use `DateTimeKind.Unspecified`, as it lacks time zone information.

## Managing variables

You can use the Data Manager to manually create and manage variables. Variables that are automatically generated for activity outputs can be managed from the Data Manager after they are used in an activity.

### Creating a variable

1. Open the Data Manager by selecting the ![docs image](/images/studio-web/studio-web-docs-image-data-manager.png) **Open Data Manager** button on the left side of the Designer panel.
2. Select the **Add new item** **+** button next to **Variables**.
3. Provide the following information:
   * **Variable name** - Enter the variable name.
   * **Scope** - The context in which the variable can be used. All variables are currently **Global** (available in the entire workflow)
   * **Type** - The data type.
   * **Default value** - The default value.
   * **Description** - A meaningful description of the variable.
4. Select **Create**.

### Editing a variable

1. Open the Data Manager.
2. Under **Variables**, expand the variable you want to edit.
3. Edit the variable information.

### Renaming or deleting a variable

1. Open the Data Manager.
2. Hover over a variable.
3. Select the **Rename** button to enter a new variable name or the **Remove** button to delete the variable from the project. Note that you can't remove automatically generated variables.

### Changing a variable into an argument

1. Open the Data Manager.
2. Right-click a variable.
3. Select **Change into Argument**.

## Managing arguments

Arguments in the Data Manager are split between the **Inputs** and **Outputs** sections. Use the two sections to create and manager input and output arguments respectively.

### Creating an argument

1. Open the Data Manager by selecting the ![docs image](/images/studio-web/studio-web-docs-image-data-manager.png) **Open Data Manager** button on the left side of the Designer panel.
2. Select the **Add new item** **+** button next to **Inputs** or **Outputs**.
3. Provide the following information:
   * **Argument name**
     - Enter the argument name.
   * **Direction** - The argument direction:
     + **In** - The argument can be used to pass data into the project. This is the default option.
     + **Out** - The argument can be used to pass data out of the project.
     + **In/Out**
       - The argument can be used to pass data both into and out of the project.
   * **Type** - The data type.
   * **Default value**
     - The default value.
   * **Description** - A meaningful description of the argument.
4. Select **Create**.
   :::note
   You cannot set the default value of **Out** and **In/Out** arguments from the Data Manager. Use the [Set Variable Value](https://docs.uipath.com/activities/other/latest/workflow/assign) activity to set a default value for these types of arguments.
   :::

### Editing an argument

1. Open the Data Manager.
2. Under **Inputs** or **Outputs**, expand the argument you want to edit.
3. Edit the argument information.

### Renaming or deleting an argument

1. Open the Data Manager.
2. Hover over an argument.
3. Select the **Rename** button to enter a new argument name or the **Remove** button to delete the argument from the project.

### Changing an argument into a variable

1. Open the Data Manager.
2. Right-click an argument.
3. Select **Change into Variable**.

## Managing entities

Studio Web integrates with Data Fabric to make it easy to process entity records. [Data Fabric activities](https://docs.uipath.com/data-service/automation-cloud/latest/user-guide/data-service-studio-activities) are available to create, update, query, get, or delete entity records. You select the entity to use directly from Data Fabric activities in your projects, and the entities are then added to the Data Manager.

To view and manage entities added to your project, open the Data Manager by selecting the ![](/images/studio-web/studio-web-docs-image-data-manager.png) **Open Data Manager** button on the left side of the Designer panel. The list of entities is displayed under the **Entities** sections.

Right-click the **Entities** section to:

* **Update all entities** in your project.
* **Show all entities** in Data Fabric.

Right-click an entity to:

* **Remove** the entity from the project.
* **Show** the entity in Data Fabric.

## Managing the connections used in a project

1. In a project, click ![docs image](/images/studio-web/studio-web-docs-image-data-manager.png) on the upper-right side of the page.
2. The connections used in the project are displayed under **Connections**. This includes Integration Service connections as well as UI automation connections.

For each Integration Service connection, you can see the connection name, which activities use the connection, the activities and properties where user-specific data is used, and for some activities, you can click the icon next to each entry to scroll to the activity where the connection is used in the project. If a connection is invalid, the ![](/images/studio-web/studio-web-image-error_icon.png) icon is displayed next to the connection,

To more easily identify connections, you can add a few details that describe the role of each connection by selecting **See more** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Add purpose**.

To identify connections more easily, select the **Connection purpose** button next to a connection. Inside the connection purpose window, you can add a few details that describe the role of the connection, or you can delete the purpose of the connection. You can also hover over the **Connection purpose** button in the Data Manager to see details about the purpose. Hovering over a connection also shows information about the properties of that connection.