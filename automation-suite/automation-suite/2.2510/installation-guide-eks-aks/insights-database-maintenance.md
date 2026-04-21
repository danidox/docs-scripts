---
title: "Performing Insights database maintenance"
visible: true
slug: "insights-database-maintenance"
---

## Overview

Insights Database works using two tables: `dbo` and `read`. Both tables store data from Orchestrator databases and pass data between each other. Over time, tables store a large amount of data that can impact database performance. You can free up space by removing data that is not relevant or outdated.

The estimated threshold for storing historical data is set to

* Up to 100 million jobs
* Up to 1 billion job events
* Up to 100 million queue items
* Up to 500 million queue item events
* Up to 1 billion robot logs

Use the following database maintenance SQL scripts to create SQL Stored Procedures, then execute these SQL Stored Procedures to either delete all data from `[dbo].Jobs`, `[dbo].JobEvents`, `[dbo].QueueItems`, `[dbo].QueueItemEvents`, `[dbo].RobotLogs` tables, or just the `[dbo].RobotLogs`.

:::note
Back up your database before executing the scripts. Before running the `PROCEDURE [read].[Delete_Insights_Data_Read]` and `PROCEDURE [read].[Delete_Process_Logs_Read]` scripts, the Insights module needs to be disabled.
:::

## Considerations

* Scripts with the `_DBO` suffix are used to delete data from DBO schema tables,
* Scripts with the `_Read` suffix are used to delete data from Read schema tables.
* Large-sized batches might impact the speed of execution. Consider using the default batch size, which is set to 100000.

## Prerequisites

Before running the `PROCEDURE [read].[Delete_Insights_Data_Read]` and `PROCEDURE [read].[Delete_Process_Logs_Read]` scripts, the Insights module needs to be disabled.

1. Log in to the Automation Suite cluster.
2. Remove files that may conflict with the commands:
   ```
   rm -f appsettings.json
   ```
3. Get the current settings:
   ```
   ./bin/uipathctl config orchestrator get-config --app-settings > appsettings.json || echo '{}' > appsettings.json
   ```
   :::note
   Ignore the following message if it is displayed: `Cannot print custom config: Orchestrator custom config is missing appsettings.`. This error message only implies there are no custom settings.
   :::
4. Add the `Insights.ModuleEnabled` key and set it to `False`:
   ```
   jq '.["Insights.ModuleEnabled"] = "false"' appsettings.json > temp.json && mv -f temp.json appsettings.json
   ```
5. Update the configuration:
   ```
   ./bin/uipathctl config orchestrator update-config --app-settings appsettings.json
   ```
6. Validate the configuration:
   ```
   ./bin/uipathctl config orchestrator get-config --app-settings
   ```

The expected result is as follows:

   ```
   {
       "Insights.ModuleEnabled": "false"
   }
   ```

The result can contain other settings unrelated to Insights.
7. Run the maintenance scripts. After you run the maintenance script, re-enable Insights using the following steps.
8. Remove any conflicting files:
   ```
   rm -f appsettings.json
   ```
9. Remove the `Insights.ModuleEnabled` key:
   ```
   jq 'del(.["Insights.ModuleEnabled"])' appsettings.json > temp.json && mv -f temp.json appsettings.json
   ```
10. Update the configuration:
    ```
    ./bin/uipathctl config orchestrator update-config --app-settings appsettings.json
    ```
11. Confirm the configuration:
    ```
    ./bin/uipathctl config orchestrator get-config --app-settings
    ```

The expected result is as follows:

    ```
    {}
    ```

The result can contain other settings unrelated to Insights.

## Resources

[SQL Stored Procedures download location](https://github.com/UiPath/Insights-Customer/tree/master/Scripts/SQLServer/DataTrimmingScripts)

## SQL stored procedure 1: delete all data based on cut-off timestamp

Generate and save the following SQL Stored Procedures to delete all data types (`Jobs`, `JobEvents`, `QueueItems`, `QueueItemEvents`, `RobotLogs`) for a cut-off timestamp.

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <strong>
     SQL Stored Procedures
    </strong>
   </th>
   <th>
    <strong>
     Parameter
    </strong>
   </th>
   <th>
    <strong>
     Description
    </strong>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d61123e333">
    <strong>
     Delete_Insights_Data_DBO
    </strong>
   </td>
   <td headers="d61123e336">
    <ul>
     <li>
      @CutoffTimeStamp
      <code>
       DATETIME
      </code>
      (Required)
                                    Delete all five types of data before a specified timestamp (e.g.,
      <code>
       2021-01-01 01:00:05
      </code>
      ).
      <p>
       Do not provide a timestamp that deletes all data to an empty table.
      </p>
     </li>
     <li>
      @BatchSize
      <code>
       INT = 100000
      </code>
      (Optional)
                                    Default is set to
      <code>
       100000
      </code>
      .
      <p>
       Data is deleted batch by batch. For example, if you have 1 million RobotLogs and leave the default value, the delete command
                                       runs ten times to remove all data.
      </p>
     </li>
    </ul>
   </td>
   <td headers="d61123e339">
    Delete data from
    <code>
     [dbo].[Jobs]
    </code>
    ,
    <code>
     [dbo].[JobEvents]
    </code>
    ,
    <code>
     [dbo].[QueueItems]
    </code>
    ,
    <code>
     [dbo].[QueueItemEvents]
    </code>
    ,
    <code>
     [dbo].[RobotLogs]
    </code>
    tables based on a cut-off timestamp.
   </td>
  </tr>
  <tr>
   <td headers="d61123e333">
    <strong>
     Delete_Insights_Data_Read
    </strong>
   </td>
   <td headers="d61123e336">
    N/A
   </td>
   <td headers="d61123e339">
    Truncate
    <code>
     [read].Jobs
    </code>
    ,
    <code>
     [read].JobEvents
    </code>
    ,
    <code>
     [read].QueueItems
    </code>
    ,
    <code>
     [read].QueueItemEvents
    </code>
    ,
    <code>
     [read].RobotLogs
    </code>
    tables.
   </td>
  </tr>
 </tbody>
</table>

:::note
The Insights Dashboard widgets are available again after SQL Stored Procedure 1 has finished, and the data has been backfilled. Keep in mind that the backfill process may take hours to complete given that you have a large amount of data. When you first run the `Delete_Insights_Data_DBO` SQL Script, it creates a `QueueItems.IX_CreationTime` nonclustered index with the purpose of making future executions faster.
:::

## SQL stored procedure 2: delete RobotLogs data based on ProcessNames and Tenant ID

Generate and save this SQL Stored Procedure to delete RobotsLogs based on ProcessNames and Tenant ID.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <strong>
     SQL Stored Procedures
    </strong>
   </th>
   <th>
    <strong>
     Parameter
    </strong>
   </th>
   <th>
    <strong>
     Description
    </strong>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d61123e442">
    <strong>
     Delete_Process_Logs_DBO
    </strong>
   </td>
   <td headers="d61123e445">
    <ul>
     <li>
      @ProcessName
      <code>
       NVARCHAR(128)
      </code>
      (Required)
     </li>
    </ul>
    <p>
     The Orchestrator process name.
    </p>
    <ul>
     <li>
      @TenantId
      <code>
       INT
      </code>
      (Required)
     </li>
    </ul>
    <p>
     Tenant ID is required as two tenants might run processes with identical names.
    </p>
    <ul>
     <li>
      @BatchSize
      <code>
       INT = 100000
      </code>
      (Optional)
     </li>
    </ul>
    <p>
     Delete data in batches of 100000. See
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/insights-database-maintenance#considerations">
      Considerations
     </a>
     .
    </p>
   </td>
   <td headers="d61123e448">
    Delete data from
    <code>
     [dbo].[RobotLogs]
    </code>
    table by ProcessName and Tenant ID.
   </td>
  </tr>
  <tr>
   <td headers="d61123e442">
    <strong>
     Delete_Process_Logs_Read
    </strong>
   </td>
   <td headers="d61123e445">
    <ul>
     <li>
      @ProcessName
      <code>
       NVARCHAR(128)
      </code>
      (Required)
     </li>
     <li>
      @TenantId
      <code>
       INT
      </code>
      (Required)
     </li>
    </ul>
   </td>
   <td headers="d61123e448">
    Truncate
    <code>
     [read].RobotLogs
    </code>
    table.
   </td>
  </tr>
 </tbody>
</table>

:::note
The Insights Dashboard widgets related to RobotLogs are available again after SQL Stored Procedure 2 has finished, and the data has been backfilled. Keep in mind that the backfill process may take hours to complete given that you have a large amount of data.
:::

## Related articles

[Stored Procedures (Database Engine)](https://docs.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver15)