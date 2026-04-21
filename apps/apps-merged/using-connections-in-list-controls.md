---
title: "Using connections in List controls"
visible: true
slug: "using-connections-in-list-controls"
---

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [Apps feature availability](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/apps-feature-availability#apps-feature-availability) page.
:::

This tutorial assumes you already have created a connection in **Integration Service**, and added it to your app**.** If you have not done so, go to **[Adding a connection to your app.](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/adding-a-connection-to-your-app)**
:::note
The Query Builder exclusively displays APIs with a response data type of List.
:::

You can add additional functionality to your app by invoking external APIs using connections. You can do this using the **Query Builder**. To add connections to List controls, follow these steps.

This tutorial uses the Jira connection in **Integration Service** as an example, and its **List issues** functionality. This query lists the currently open Jira issues in the table, and a few of their key attributes, such as priority and status, and sorts them by when they were created.

1. Go to the app containing the connection you want to use.
2. Select **Add control.**
3. In **Display controls,** select the **Table** control and add it to your app.
4. Once the **Table** control is in your app, select it from within the central **Designer** panel.
5. In the **General** properties of the **Table** control, go to the **Data source** field. Select **Open resources**.
6. Select the **Query builder** option.
7. In the **Select source** field, select the relevant connection. In this case, select **Jira.**
8. Select the second **Select source** field. To narrow your selection, type "**List: Issues**", then select the **List: Issues** option.
9. In the **JPL query** field, type the following, including the quotation marks:
   ```
   "project = ""DEV"" AND assignee IN (currentuser()) AND statusCategory in (""To Do"", ""In Progress"") ORDER BY created DESC"
   ```
10. Select the **Table** control you created in step 3.
11. In the **General properties panel**, select the first column. Click on the **Name** entry.
12. Rename the first column to "priority*".*
13. Under **Source,** click on the **Open resources** button.
14. Select **Expression editor.**
15. Type `"MainPage.Table.SelectedItem.fields.priority.name"`, including quotation marks.
16. Return to the **General properties** tab in the **Table.**
17. Select the second column. Rename it to "status"*.*
18. To change the data source, repeat steps 13-15 in the second column.
19. In the Expression editor, type "`MainPage.Table.SelectedItem.fields.status.name`", including quotation marks.
20. Return to the **General properties tab** in the **Table** again.
21. Select the third column. Rename it to "summary"*.*
22. Repeat steps 12-14 in the third column to change the data source.
23. In the Expression editor, type "`MainPage.Table.SelectedItem.fields.summary`.", including quotation marks.

The app displays the summary, status and priority of the listed Jira issues at runtime.