---
title: "The resources panel"
visible: true
slug: "the-lookup-panel"
---

The functionality of the resources panel aims to simplify the process of identifying available resources and binding them to the control properties and rules in your app.

The feature generates expressions depending on the properties context that activates the panel, and consequently lists only the bindable resources relevant to that specific control.

## Accessing the resources panel

You can access the resources panel for any control, integration, or rule property by clicking the tune icon ![](/images/apps/apps-image-280277-e5d8b471.webp), also known as the **Open resources** menu.

This opens the first menu of the panel, which displays different options and resources based on the property of the control that activated the panel:

## Available options and resources

With the resource panel, you can access the following options and resources:

* **Open expression editor** - to manually create or edit the VB expression
* **Query builder** - to manually query entities (for Data source or List source properties, provided you have an entity referenced in your app.)
* **Pages** - to reference other available pages within the app
* **Controls** - to bind the properties of the available controls
* **Icons** - to reference an available icon
* **App variables** - to bind the available variables
* **Media** - to bind the properties of the available images
* **Processes** - to bind the arguments of the available processes
* **Entities** - to bind the available entities
* **Storage Buckets** - to bind the available storage buckets
* **Queues** - to bind the arguments of the available queues
* **Clear** - to remove the current expression

## Accessing a resource properties

Expanding a resource lists the corresponding elements on the current app page. For example, expand the **Controls** resource to see all the controls on the page.

To locate a specific property or element, or to filter the list to elements with certain properties, use the search bar. For instance, to view all controls that have a **Data Source** property, write `datasource` in the search bar.

Expanding a specific element displays the available properties, which you can use for binding.

For example, in the following image, to bind the Layout control, you can only use the properties displayed in the panel:

  ![docs image](/images/apps/apps-docs-image-372977-e1019453.webp)

Be aware of the data type of the property or element you want to bind, to avoid errors. For example, you cannot bind a text variable to a property that requires integers. However, binding the elements via the resources panel implictly converts primitive data types, as follows:

## Converting primitive data types

| The data type required by the target property, the one from where you access the resource panel | The data type of the selected property, the one you select from the resource panel | The conversion expression |
| --- | --- | --- |
| String | Boolean, Integer, Decimal, Double, DateOnly | SelectedPropertyValue.ToString |
| Integer | String | CInt(SelectedPropertyValue) |
| Boolean | Integer, Decimal, Double, String | CBool(SelectedPropertyValue) |
| Decimal | Double, Integer | CDec(SelectedPropertyValue) |
| AppsDataSource | Array, List, DataTable | SelectedPropertyValue.ToListSource() |
| AppsFile | String | New AppsFile(SelectedPropertyValue) |

For example, this is how the resource panel converts strings to booleans.

  ![docs image](/images/apps/apps-docs-image-398047-ad3d1d00.webp)

Similarly, this is how the resource panel converts integers to strings:

  ![docs image](/images/apps/apps-docs-image-398051-2a29193f.webp)

## Using the resource panel

The resource panel helps you in a quicker and safer identification of the resource and their properties. To further edit the expression, use the editor to access VB methods or functions.

During rule configuration, the resource panel recognizes the context and suggests relevant resources. For instance, when setting up the **Add to Queue** rule, the panel displays all queues your app references. When you select a specific queue, the rule configuration continues to display the arguments for the chosen queue.

  ![docs image](/images/apps/apps-docs-image-401285-705460c2.webp)

## Examples

### Binding app variables using the resource panel

  ![docs image](/images/apps/apps-docs-image-400456-c2ea4eec.webp)

### Binding control properties using the resource panel

  ![docs image](/images/apps/apps-docs-image-398035-db0fc5d1.webp)

### Binding entities using the resource panel

  ![docs image](/images/apps/apps-docs-image-398023-35d0f645.webp)

### Binding icons using the resource panel

  ![docs image](/images/apps/apps-docs-image-398027-4792fdc8.webp)

### Binding media files using the resource panel

  ![docs image](/images/apps/apps-docs-image-401261-274848af.webp)

### Binding pages using the resource panel

  ![docs image](/images/apps/apps-docs-image-398018-55398df1.webp)

### Binding process arguments using the resource panel

  ![docs image](/images/apps/apps-docs-image-398031-019d71ae.webp)

### Binding queue arguments using the resource panel

  ![docs image](/images/apps/apps-docs-image-400476-8e4654a3.webp)

### Binding storage buckets using the resource panel

  ![docs image](/images/apps/apps-docs-image-401267-89d53089.webp)