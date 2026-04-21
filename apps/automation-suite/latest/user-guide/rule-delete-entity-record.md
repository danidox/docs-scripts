---
title: "Rule: Delete Entity Record"
visible: true
slug: "rule-delete-entity-record"
---

Use the **Delete Entity Record** rule to delete a record from an entity which was imported from Data Service in your app.

![docs image](/images/apps/apps-docs-image-291250-d3d137d8.webp)

## Which entity record should be deleted?

Clicking the **Which entity record should be updated?** field opens the **Resources** panel, which displays the available imported Data Service entities.

Select the entity by double-clicking on it. Once selected, the following properties become available:

* Values to set
* When deleted
* On Error

## Entity record Id

Provide the ID of the record you want to delete.

You can find the ID in **Data Service** &gt; &lt;Entity_name&gt; &gt; **Data.**

To use the record ID in this rule, declare it as a variable of type **Guid**, or write the following syntax in the **Entity record Id** field:

```
New Guid("record_id_string")
```

## When deleted

In this section you can define rules to be executed right after the entity record has been deleted.

**For example:** You can display a success message after the record is deleted using the **Show Message** rule and selecting **Success** from the **Type** dropdown.

## On Error

In this section you can define rules to be executed when the process of updating a record encounters an error.

**For example:** To track the failure, you can add a **Show Message** rule. You can then specify the title, message, and type of the error.

## Rule output properties

* **Error -** references the error message shown if the job fails.