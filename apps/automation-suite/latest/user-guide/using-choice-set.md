---
title: "Using Choice Set"
visible: true
slug: "using-choice-set"
---

A choice set is a type of a Data Service field, used to store an enumerated list of selectable items.

You can use a choice set to select an expense type, a forum post category, or a certain edition of a recurring event.

You can bind choice sets to the following controls:

* Dropdown
* Multiselect dropdown
* List
* Radio Button
  :::note
  Binding choice sets to a list source returns the options in that choice set. Binding choice sets to a selected item binds the field value of that selected item. When bounding to a selected item, it will bind the field value to that selected item.
  :::

## Before you start

Make sure:

* the entity with choice sets is imported in your app.
* you have the proper permissions from Data Service.

## Procedure

This example uses an entity called Fauna that has the following fields:

* Animals - type **Choice Set**, multiple selection not allowed
* Continent - type **Choice Set**, multiple selection allowed
* Endangered - type **Choice Set**, multiple selection not allowed
1. In your app, add the Fauna entity.

You must include at least one entity to use the `GetChoiceSet()` function.
2. Add a **Dropdown** control and configure it as follows:
   1. In the **List Source** field, reference the Animals choice set:
      ```
      GetChoiceSet("Animals")
      ```
   2. In the **Column** field, write "DisplayName". This displays the display name of the choice set as an option in your control.
3. Add a **Multiselect dropdown** control and configure it as follows:
   1. In the **List Source** field, reference the Continent choice set:
      ```
      GetChoiceSet("Continent")
      ```
   2. In the **Column** field, write "DisplayName". This displays the display name of the choice set as an option in your control.
4. Add a **Radio Button** control and configure it as follows:
   1. In the **List Source** field, reference the Endangered choice set:
      ```
      GetChoiceSet("Endangered")
      ```
   2. In the **Column** field, write "DisplayName". This displays the display name of the choice set as an option in your control.