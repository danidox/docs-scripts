---
title: "Rule: Create Entity Record"
visible: true
slug: "rule-create-entity-record"
---

Use the **Create Entity Record** rule to add a new record to an entity which was imported from Data Service in your app.

![docs image](/images/apps/apps-docs-image-291224-02334f19.webp)

## Which entity should record be created in?

Clicking the **Which entity should record be created in?** field opens the **Resources** panel, which displays the available imported Data Service entities.

Select the entity to add a new record to by double-clicking on it. Once selected, the following properties become available:

* Values to set
* When created
* On Error

## Values to set

Once you add the entity you want to work with, the fields for a new record are listed in this section. Mandatory fields are marked with an asterisk.

## When created

In this section you can define rules to be executed right after the creation of a new entity record is complete.

**For example:** You can display a success message after the record is created using the **Show Message** rule and selecting **Success** from the **Type** dropdown.

## On Error

In this section you can define rules to be executed when the process of creation a new record encounters an error.

**For example:** To track the failure, you can add a **Show Message** rule. You can then specify the title, message, and type of the error.

## Rule output properties

* **Error -** references the error message shown if the job fails.
* **RecordId -** references the ID of the specified record.