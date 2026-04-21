---
title: "Replacing an Entity"
visible: true
slug: "replacing-an-entity"
---

Apps Studio allows replacing the entity referenced in the app. This capability is helpful when you move your apps between organizations or environments (Development, Test, and Production).

To replace an entity with another one:

1. In the tree view, right-click on the entity you want to replace, and then select **Replace**.

When you change the tenant, previously imported entities become unavailable and they are marked as errors.

   ![docs image](/images/apps/apps-docs-image-98280-f0aa9988.webp)

   ![docs image](/images/apps/apps-docs-image-94964-a98d8d79.webp)
2. The entity replacement wizard opens. To select an entity from a different tenant, click **pick a different tenant**.
   :::note
   Changing the tenant makes any resource hosted in that tenant unavailable. These resources and the controls where they were used are marked as errors.
   :::
3. In the left-hand panel, select the desired entity by checking the box next to the entity name. The list of the selected entity fields is displayed in the right-hand panel.
4. Click **Replace**.

   ![docs image](/images/apps/apps-docs-image-92164-0fa65e2e.webp)

:::important
You cannot undo the replacement of an entity. Replacing an entity where a field is removed may lead to invalid bindings in the app. Make sure that you replace entities in the correct dependency order.
:::