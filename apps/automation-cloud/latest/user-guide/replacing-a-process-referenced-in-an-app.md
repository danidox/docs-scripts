---
title: "Replacing a Process"
visible: true
slug: "replacing-a-process-referenced-in-an-app"
---

Apps Studio allows replacing the process referenced in the app. This capability is helpful when you move your apps between organizations or environments (Development, Test, and Production).

:::note
If you refresh or replace a process whose arguments are bound to one or more controls, then:
* the process argument is not removed from the process definition.
* the process datatype is not modified.
This behavior only applies for complex data type sub-properties, such as columns in a data table or properties of a .NET object.
:::

To replace a process with another one:

1. In the tree view, right-click on the process you want to replace, and then select **Replace**.

When you change the tenant, previously referenced processes become unavailable and they are marked as errors.

   ![docs image](/images/apps/apps-docs-image-92044-ab6e4074.webp)

   ![docs image](/images/apps/apps-docs-image-92436-470e09a3.webp)
2. The process replacement wizard opens. To select a process from a different tenant, click **pick a different tenant**.
   :::note
   Changing the tenant makes any resource hosted in that tenant unavailable. These resources and the controls where they were used are marked as errors.
   :::
3. In the left-hand panel, select the desired process by checking the box next to the process name. The list of the selected process details is displayed in the right-hand panel.
4. Once the process is selected, you can see the process details on the right panel.

The difference between the arguments of the old and the new processes are indicated with two icons:

   |  |  |
   | --- | --- |
   | A yellow plus icon | The argument exists only in the new process that replaces the old one. |
   | A red minus icon | The argument exists only in the old process that is being replaced. |

   ![docs image](/images/apps/apps-docs-image-92012-e3ad0858.webp)

   ![docs image](/images/apps/apps-docs-image-93975-f2c81ef5.webp)
5. Click **Replace** to replace the existing process with the new one selected.
   :::important
   You cannot undo the replacement of a process. Replacing a process where an argument is removed may lead to invalid bindings in the app.
   :::