---
title: "Rule: Update Entity Record"
visible: true
slug: "rule-update-entity-record"
---

Use the **Update Entity Record** rule to update a specific record of an entity which was imported from Data Service in your app.

![docs image](/images/apps/apps-docs-image-294336-46883076.webp)

## Which entity's record should be updated?

Clicking the **Which entity's record should be updated?** field opens the **Resources** panel, which displays the available imported Data Service entities.

Select the entity to update by double-clicking on it. Once selected, the following properties become available:

* Values to set
* When updated
* On Error

## Entity record Id

Provide the ID of the record you want to update.

You can find the ID in **Data Service** &gt; [Entity_name] &gt; **Data.**

To use the record ID in this rule, bind the entity to a control, (for example, a **Table** control), then use the **SelectedItem** method to access the ID of the item:

```
MainPage.MyTable.SelectedItem.Id
```

## When updated

In this section you can define rules to be executed right after the entity record has been updated.

**For example:** You can display a success message after the record is updated using the **Show Message** rule and selecting **Success** from the **Type** dropdown.

## On Error

In this section you can define rules to be executed when the process of updating a record encounters an error.

**For example:** To track the failure, you can add a **Show Message** rule. You can then specify the title, message, and type of the error.

## Rule output properties

* **Error -** references the error message shown if the job fails.