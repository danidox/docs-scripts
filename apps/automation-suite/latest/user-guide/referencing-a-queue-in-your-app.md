---
title: "Referencing a Queue in Your App"
visible: true
slug: "referencing-a-queue-in-your-app"
---

To create better, more complex apps, UiPath Apps can connect and interact with queues from UiPath Orchestrator.

## Referencing a Queue From Orchestrator

Once a queue has been created in Orchestrator, you can reference that queue from an app.

:::note
Apps can reference only the queues that were created using a **Specific Data JSON Schema** file. ![docs image](/images/apps/apps-docs-image-293062-34ca17df.webp) An example of a schema definition: assignment
```
{
"definitions": {},
"$schema": "http://json-schema.org/draft-07/schema#",
"$id": "http://example.com/root.json",
"type": "object",
"title": "The Root Schema",
"required": [
"name"
],
"properties": {
"name": {
"type": "string"
},
"isPermanent": {
"type": "boolean"
},
"age": {
"type": "number"
},
"department": {
"type": "string",
"enum": ["Sales", "Marketing", "HR"]
}
}
}
```
:::

The following example shows you how to add an existing queue to an app:

1. From an existing app in App Studio, expand the dropdown menu at the right of the **Add control** button.
2. Select **Queue**.

   ![docs image](/images/apps/apps-docs-image-293067-a2dd07cb.webp)
3. A list of tenants for the current account is displayed. Select the tenant that hosts the entities you need to import, then click **Next**.

   ![docs image](/images/apps/apps-docs-image-292082-1d70b9bb.webp)
4. The **Add queue** wizard opens, displaying the list of queues in the selected tenant. Highlighting a queue displays its contents.
5. Select one or more queues. The right-hand panel displays the list of properties of the highlighted queue.

   ![docs image](/images/apps/apps-docs-image-333742-b8385f57.webp)
6. Check the box next to the queue you want to use in your app and click **Add**.
   :::note
   Queue permissions are managed in Orchestrator. Make sure you have the right permissions for the queue you want to add from Orchestrator.
   :::

## Updating a Referenced Queue

To update a referenced queue whose schema was changed, follow these steps:

1. From the **Queues** section in the tree view, select the queue you want to update.
2. Click on the **Refresh** icon.

   ![docs image](/images/apps/apps-docs-image-293078-e1fc3ead.webp)