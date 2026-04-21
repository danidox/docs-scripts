---
title: "Context Grounding"
visible: true
slug: "context-grounding"
---

[Context Grounding](https://docs.uipath.com/activities/other/latest/integration-service/uipath-airdk-airdk-context-grounding) in Autopilot for Everyone allows you to search existing Context Grounding indexes to answer user queries.

For example, you want to query the HR documents of your organization, such as time and expense policies, or employee handbooks, using Autopilot. Using Context Grounding, an admin would create the index and enable it in Autopilot, which allows Autopilot to search the index to answer HR-related queries.

To use Context Grounding, make sure you meet the following criteria:

* Relevant PDF, CSV, JSON, DOCX, XLSX, and TXT documents are uploaded in a shared Orchestrator storage bucket.
* The index has been already created from the Orchestrator storage bucket.

## Managing Context Grounding indexes

Index creation is done in Orchestrator, in the tenant-level Indexes page. For details, refer to [Indexes](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-indexes).

Index enablement and management in Autopilot is done via the **Context Grounding** configuration section in Automation Cloud™ > **Admin** > **AI Trust Layer** > **Autopilot for Everyone**.

Once the index is created, [enable it in Autopilot](https://docs.uipath.com/autopilot/other/latest/user-guide/context-grounding#enabling-context-grounding-indexes) through the Context Grounding, panel.

## Managing access for Context Grounding indexes

Access to Context Grounding indexes is managed at the folder level. Users can access indexes under the following conditions:

* The index exists in the folder
* The user is assigned to the same folder where the index is located
* The [index is enabled in Autopilot](https://docs.uipath.com/autopilot/other/latest/user-guide/context-grounding#enabling-context-grounding-indexes)

## Adding Context Grounding indexes

To add a Context Grounding index, follow the steps described in [Creating indexes](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-indexes#creating-indexes), in the Orchestrator user guide.

## Enabling Context Grounding indexes

To enable an index for Autopilot for Everyone:

1. Navigate to the Automation Cloud > **Admin** > **AI Trust Layer** > **Autopilot for Everyone** tab, then choose the tenant where Autopilot for Everyone is installed.
2. Expand the **Context grounding** settings section.
3. Select the **Enable Index** option. The **Enable Index In Autopilot** panel opens.
4. From the **Orchestrator folder** dropdown, select the Orchestrator folder where your index resides.
5. From the **Index name** dropdown menu, select the index you want to add to Autopilot. The list of available indexes in the selected tenant is displayed.
6. In the **Description for Autopilot*** field, write a comprehensive description that should help Autopilot understand when to search for the selected index.

For example, for an index value "HR documents", the description could read "HR policy documents on time/expense, paternity, PTO, and employ handbook. Use for questions about company HR policies, providing accurate, up-to-date information to employees."
7. For indexes with structured tabular data, select the **Enable tabular query** checkbox to allow retrieval of that information.
8. Select **Enable** to add the index. The panel closes and you are returned to the **Context Grounding** table.


:::important
Changes are automatically saved.
:::

## Editing Context Grounding indexes

To edit an index for Autopilot for Everyone:

1. Navigate to the Automation Cloud > **Admin** > **AI Trust Layer** > **Autopilot for Everyone** tab, then choose the tenant where Autopilot for Everyone is installed.
2. Expand the **Context grounding** settings section.
3. For the desired index, select **Edit**. The **Updating index** opens.
4. Modify the desired properties as needed.
5. Select **Save** to update the index. The panel closes and you are returned to the **Context Grounding** table.


:::important
Changes are automatically saved.
:::

## Deleting Context Grounding indexes

To remove an index from Autopilot for Everyone:

1. Navigate to the Automation Cloud > **Admin** > **AI Trust Layer** > **Autopilot for Everyone** tab, then choose the tenant where Autopilot for Everyone is installed.
2. Expand the **Context grounding** settings section.
3. For the desired index, select **Delete**. A confirmation message is displayed.
4. Select **Delete** to delete the prompt, or **Cancel** to dismiss the action.


:::important
Changes are automatically saved.
:::

## Using tabular query with Context Grounding

This page explains how to enable the feature for a Context Grounding index and shares best practices for preparing data and writing queries.

### About the tabular query feature

The tabular query feature helps Autopilot for Everyone understand and answer natural language questions using structured data, such as CSV files. With it, you can query data, run comparisons, and get insights from your indexed tables directly in chat.

### Enabling tabular query

To enable the feature, check the **Enable tabular query** box when setting up a Context Grounding index in Autopilot for Everyone.

Once enabled, Autopilot can answer natural language questions using the structured data in your indexed files.

### Preparing data best practices

Your results depend on how clean and well-formatted your source data is. Use these tips to prepare and optimize your data for more accurate queries:

#### Ensure correct data types

Numerical operations, such as comparisons or calculations, need correct data types to work. Autopilot for Everyone needs to recognize numbers as numeric types (`Real` or `Integer`), not as text.

To check the data types Autopilor has assigned to your columns, use this prompt:

* "List 5 rows of data in <index_name> and list all the fields with their data types."

#### Ensure clean numeric and percentage columns

Remove special characters, such as the percent sign %, from your data columns before creating the index. Autopilot treats values such as `20%` as text, which prevents numerical queries from working correctly.

Make sure date columns use a consistent format, preferably `MM/DD/YYYY`. Use the data type check query to confirm that date columns are parsed as **Date Time** rather than plain text.

### Tabular query best practices

Clear prompts lead to better results. Keep these tips in mind when querying your tabular data:

#### Avoid complex schemas

Be careful with files that contain many columns. The more complex the data schema, the more likely it is that a natural language query will be misinterpreted.

#### Be aware of null values

Calculations ignore rows with null or empty values in a queried column. For example, when you sum four columns, the system excludes any row that has a null in one of them. To avoid this, normalize your data and replace nulls with appropriate values.

#### Specify your string match type

By default, the query engine compares strings using exact matches. To find partial matches, you must explicitly include them in your query:

* **For an exact match:** "BCA Claims and Consulting Ltd"
* **For a partial match:** "BCA Claims and Consulting Ltd. or any of its subsidiaries". This query returns any result that contains the substring "BCA Claims and Consulting Ltd."

#### Use the debug view

For advanced troubleshooting, use `Ctrl+Alt+Shift+D` to open the debug view. The panel shows how the query engine interpreted your natural language prompt, which can help you diagnose unexpected results.