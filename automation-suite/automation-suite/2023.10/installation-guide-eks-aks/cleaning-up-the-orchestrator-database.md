---
title: "Cleaning up the Orchestrator database"
visible: true
slug: "cleaning-up-the-orchestrator-database"
---

The following scripts replace any and all previous database cleanup scripts. They cover all necessary maintenance tasks and can be configured as needed.

:::important
* You can download the Orchestrator database maintenance scripts from the [Customer Portal](https://customerportal.uipath.com/product-downloads?q=Database%20Maintenance%20Scripts&s=recently_created&d=1).
:::

## SQL script

### Prerequisites

This is what you need to be able to run the `CreateOrchestratorCleanupObjects.sql` script:

* You must have access to the archive database from within the context of your Orchestrator database.
* You must be able to access the archive using 3-part names, such as `Archive.dbo.QueueItemsTableArchive`.

### How to use it

1. Run the `CreateOrchestratorCleanupObjects.sql` SQL script to create the following objects:
* The `dbo.__CleanupLog` table, which houses the execution logs.
* The `dbo.GetOrCreateArchiveTable` procedure, which creates or returns the archive table.
* The `dbo.RunOrchestratorCleanup` procedure, which performs the deletion and, optionally, the archival of old data.
2. Execute `dbo.RunOrchestratorCleanup` with the scheduling XML configuration file to perform the cleanup. For details on the XML file, see the **Scheduling the cleanup** section.
   :::note
   You can also use [SQL Server Agent](https://learn.microsoft.com/en-us/sql/ssms/agent/create-a-job) to perform the cleanup.
   :::

### Script sample

```
DECLARE @cleanupConfigXml XML = 
'<CleanupConfig totalRunMaxMinutes="180">
    <Table name="QueueItems" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="CreationTime" additionalFilter="Status IN (2, 3, 4, 5, 6)" daysOld="180" batchSize="50" forceCascade="1" shouldArchive="1" />
</CleanupConfig>';

EXEC dbo.RunOrchestratorCleanup 
@cleanupConfigXml = @cleanupConfigXml,
@archiveDatabaseName = 'OrchestratorArchive';
```

## PowerShell script

This is appropriate for situations where you cannot use the SQL script.

:::note
The PowerShell script is compatible with Powershell 5.1 and can be used with [Azure Automation runbooks](https://learn.microsoft.com/en-us/azure/automation/automation-runbook-types).
:::

### Prerequisites

The `RunOrchestratorCleanup.ps1` script must be able to communicate with both these [connection strings](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectionstring):

* `SourceConnectionString` - this is the Orchestrator database connection string.
* `DestinationConnectionString` - this is the archive database connection string. Note that the archive database must be created and setup in advance.

### Objects it creates

* The `dbo.__CleanupLog` table, which houses the execution logs.
* The `dbo.__CleanupIds` table, which stores a temporary batch of IDs that need to be cleaned up.

### Limitations

The script opens two connections: one to the Orchestrator database (via `SourceConnectionString`) and one to the archive database (via `DestinationConnectionString`). As such, no actual transaction is involved, since the data is copied from Orchestrator to the archive, after which it is deleted from Orchestrator.

This means that, if an exception is thrown anywhere between the two actions, causing the script to be re-executed, the same data might be copied again, thus leading to duplicates in the archive database.

However, since uniqueness is not enforced in the archive database, this does not lead to any issues.

### Script sample

```
.\RunOrchestratorCleanup 
-SourceConnectionString "Data Source=.;Initial Catalog=UiPath;User ID=sa;Password=******" 
-DestinationConnectionString "Data Source=.;Initial Catalog=<OrchestratorArchive>;User ID=sa;Password=******" 
-CleanupConfigXml '<CleanupConfig totalRunMaxMinutes="180"><Table name="QueueItems" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="CreationTime" additionalFilter="Status IN (2, 3, 4, 5, 6)" daysOld="180" batchSize="50" forceCascade="1" shouldArchive="1" /></CleanupConfig>'
```

## Scheduling the cleanup

You can choose what data to clean up from your database, when, and for how long the cleanup activity should be performed for each run, among others.

To do that, use the following XML file with either the SQL or the PowerShell script. **It is preconfigured with our recommended parameters**, but you can edit it if you want more advanced features. Please make sure you understand what each parameter does before you edit the script, as this can have serious consequences.

```
<CleanupConfig totalRunMaxMinutes="180">
    <Table name="QueueItems" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="CreationTime" additionalFilter="Status IN (2, 3, 4, 5, 6)" daysOld="180" batchSize="50" forceCascade="1" shouldArchive="1" />
    <Table name="Jobs" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="CreationTime" additionalFilter="State IN (4, 5, 6)" daysOld="180" batchSize="50" forceCascade="1" shouldArchive="1" />        
    <Table name="Logs" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="TimeStamp" additionalFilter="" daysOld="90" batchSize="1000" forceCascade="0" shouldArchive="1" />    
    <Table name="AuditLogs" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="ExecutionTime" additionalFilter="" daysOld="365" batchSize="25" forceCascade="1" shouldArchive="1" />
    
    <Table name="Tasks" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="DeletionTime" additionalFilter="IsDeleted = 1" daysOld="180" batchSize="10" forceCascade="0" shouldArchive="1" />
    <Table name="QueueProcessingRecords" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="ProcessingTime" additionalFilter="ReportType != -1" daysOld="30" batchSize="1000" forceCascade="0" shouldArchive="0" />
    <Table name="Sessions" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="ReportingTime" additionalFilter="" daysOld="180" batchSize="50" forceCascade="1" shouldArchive="0" />    
    
    <Table name="RobotLicenseLogs" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="StartDate" additionalFilter="" daysOld="180" batchSize="1000" forceCascade="0" shouldArchive="0" />    
    <Table name="UserNotifications" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="CreationTime" additionalFilter="" daysOld="90" batchSize="1000" forceCascade="0" shouldArchive="0" />
    <Table name="TenantNotifications" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="CreationTime" additionalFilter="" daysOld="90" batchSize="1000" forceCascade="0" shouldArchive="0" />    
    <Table name="Ledger" runMaxMinutes="-1" idColumn="LedgerId" dateTimeColumn="CreationTime" additionalFilter="" daysOld="7" batchSize="1000" forceCascade="0" shouldArchive="0" />
    <Table name="LedgerDeliveries" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="LastUpdatedTime" additionalFilter="" daysOld="7" batchSize="1000" forceCascade="0" shouldArchive="0" />
    <Table name="Assets" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="DeletionTime" additionalFilter="IsDeleted = 1" daysOld="120" batchSize="50" forceCascade="1" shouldArchive="0" />
    <Table name="__CleanupLog" runMaxMinutes="-1" idColumn="Id" dateTimeColumn="ExecutionTimeUtc" additionalFilter="" daysOld="7" batchSize="1000" forceCascade="0" shouldArchive="0" />
</CleanupConfig>
```

Even if one run only manages to partially clean up one or a few tables, subsequent runs will continue the cleanup, up until the script catches up with all the backlog. It is, therefore, important that you do not accumulate a larger backlog than the script is able to handle. If this happens, consider scheduling the script to run more frequently.

### Cleanup XML parameters

Expand Table

<table cellpadding="4" cellspacing="0" class="simpletable css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Parameter
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Explanation
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Possible values
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d25174e209">
    <p>
     <code>
      totalRunMaxMinutes
     </code>
    </p>
   </td>
   <td headers="d25174e213">
    <p>
     The maximum number of minutes that the script is allowed to execute for all tables during one run.
    </p>
   </td>
   <td headers="d25174e217">
    <p>
     Must be higher than 1.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d25174e209">
    <p>
     <code>
      name
     </code>
    </p>
   </td>
   <td headers="d25174e213">
    <p>
     The name of the table containing the data that you want to delete.
    </p>
   </td>
   <td headers="d25174e217">
    Example:
    <code>
     QueueItems
    </code>
   </td>
  </tr>
  <tr>
   <td headers="d25174e209">
    <p>
     <code>
      runMaxMinutes
     </code>
    </p>
   </td>
   <td headers="d25174e213">
    <p>
     The maximum number of minutes that the script is allowed to execute for a particular table during one run.
    </p>
    Important:
    <p>
     The amount of time you set here might sometimes run over by a couple of minutes.
    </p>
    In addition to that, the
    <code>
     totalRunMaxMinutes
    </code>
    takes precedence, and will always enforced, even if you set this parameter to
    <code>
     -1
    </code>
    .
   </td>
   <td headers="d25174e217">
    <code>
     -1
    </code>
    : the script will be executed for an unlimited number of minutes.
    <code>
     0
    </code>
    : the script will not execute for that particular table.
    <code>
     &gt;0
    </code>
    (i.e. a number chosen by you): the maximum number of minutes that the script will execute.
   </td>
  </tr>
  <tr>
   <td headers="d25174e209">
    <p>
     <code>
      idColumn
     </code>
    </p>
   </td>
   <td headers="d25174e213">
    <p>
     The ID of the column which contains the data you want to delete.
    </p>
   </td>
   <td headers="d25174e217">
    Example:
    <code>
     Id
    </code>
    from the
    <code>
     QueueItems
    </code>
    table
   </td>
  </tr>
  <tr>
   <td headers="d25174e209">
    <p>
     <code>
      dateTimeColumn
     </code>
    </p>
   </td>
   <td headers="d25174e213">
    <p>
     This differs depending on the data type.
    </p>
    It is used in combination with
    <code>
     daysOld
    </code>
    .
   </td>
   <td headers="d25174e217">
    Example:
    <code>
     CreationTime
    </code>
    for
    <code>
     QueueItems
    </code>
   </td>
  </tr>
  <tr>
   <td headers="d25174e209">
    <p>
     <code>
      additionalFilter
     </code>
    </p>
   </td>
   <td headers="d25174e213">
    <p>
     Any valid SQL statement for a filter.
    </p>
    <p>
     This can be left empty.
    </p>
   </td>
   <td headers="d25174e217">
    Example:
    <code>
     Status IN (2, 3, 4, 5, 6)
    </code>
    . This is included in the XML file recommended by us.
   </td>
  </tr>
  <tr>
   <td headers="d25174e209">
    <code>
     daysOld
    </code>
   </td>
   <td headers="d25174e213">
    <p>
     Allows you to keep a certain number of days' worth of data.
    </p>
    This is used in combination with
    <code>
     dateTimeColumn
    </code>
    .
   </td>
   <td headers="d25174e217">
    This must be set to a minimum of
    <code>
     2
    </code>
    .
                                 
Example: setting this parameter to
    <code>
     5
    </code>
    keeps all data that is 5 days old.
   </td>
  </tr>
  <tr>
   <td headers="d25174e209">
    <p>
     <code>
      batchSize
     </code>
    </p>
   </td>
   <td headers="d25174e213">
    <p>
     The number of table rows to be deleted in one iteration.
    </p>
    Important:
    <p>
     This is not used for tables where foreign keys are defined.
    </p>
   </td>
   <td headers="d25174e217">
    Example: setting this parameter to
    <code>
     50
    </code>
    for the
    <code>
     QueueItems
    </code>
    table deletes 50 items from that particular table.
   </td>
  </tr>
  <tr>
   <td headers="d25174e209">
    <code>
     forceCascade
    </code>
   </td>
   <td headers="d25174e213">
    <p>
     Allows you to execute the script for tables where foreign keys are defined.
    </p>
    Important:
The sample already uses
    <code>
     forceCascade
    </code>
    for the tables where it is necessary. You therefore do not need to change it.
   </td>
   <td headers="d25174e217">
    <code>
     0
    </code>
    : do not cascade.
    <code>
     1
    </code>
    : cascade. For example, setting this option for the
    <code>
     QueueItems
    </code>
    table will process both the
    <code>
     QueueItemEvents
    </code>
    and the
    <code>
     QueueItemComments
    </code>
    tables.
   </td>
  </tr>
  <tr>
   <td headers="d25174e209">
    <code>
     shouldArchive
    </code>
   </td>
   <td headers="d25174e213">
    <p>
     Allows you to choose whether you want to archive the data.
    </p>
   </td>
   <td headers="d25174e217">
    <code>
     0
    </code>
    : do not archive.
    <code>
     1
    </code>
    : archive.
   </td>
  </tr>
 </tbody>
</table>

## SQL and PowerShell scripts compared

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
    <p>
     <strong>
      Feature
     </strong>
    </p>
   </th>
   <th>
    <strong>
     SQL script
    </strong>
   </th>
   <th>
    <strong>
     PowerShell script
    </strong>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d25174e437">
    Cleanup XML
   </td>
   <td colspan="2" headers="d25174e441 d25174e444">
    <p>
     They both use the logic described in the
     <strong>
      <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/cleaning-up-the-orchestrator-database#scheduling-the-cleanup">
       Scheduling the cleanup
      </a>
     </strong>
     section.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d25174e437">
    <p>
     Execution log
    </p>
   </td>
   <td colspan="2" headers="d25174e441 d25174e444">
    They both create a
    <code>
     dbo.__CleanupLogs
    </code>
    table to store the logs of the execution.
                                 
You can query the logs of an execution by using
    <code>
     SELECT * FROM dbo.__CleanupLog WHERE ExecutionId = '&lt;execution_id&gt;' ORDER BY Id
    </code>
    .
                                 
You can check if an execution contained errors by using
    <code>
     SELECT * FROM dbo.__CleanupLog WHERE ExecutionId = '&lt;execution_id&gt;' AND IsError = 1
    </code>
    .
                                 
The
    <code>
     ExecutionId
    </code>
    parameter is generated with each execution of either of these scripts.
   </td>
  </tr>
  <tr>
   <td headers="d25174e437">
    <p>
     Archive table
    </p>
   </td>
   <td colspan="2" headers="d25174e441 d25174e444">
    <p>
     The archive table does not contain any indexes, foreign keys, or identity columns.
    </p>
    <p>
     <a href="https://learn.microsoft.com/en-us/sql/t-sql/data-types/rowversion-transact-sql?view=sql-server-ver16">
      Timestamp
     </a>
     type columns are not archived.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d25174e437">
    Archive table name
   </td>
   <td colspan="2" headers="d25174e441 d25174e444">
    <p>
     The names follow the same logic, and include a string based on the table schema.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d25174e437">
    Batch of IDs to be archived/deleted
   </td>
   <td headers="d25174e441">
    <p>
     Stored in a temporary table.
    </p>
   </td>
   <td headers="d25174e444">
    Stored in the
    <code>
     dbo.__CleanupIds
    </code>
    table.
   </td>
  </tr>
  <tr>
   <td headers="d25174e437">
    <p>
     Transaction
    </p>
   </td>
   <td headers="d25174e441">
    <p>
     A single transaction is performed for every batch, during which the data is both archived and deleted.
    </p>
    The batch size, i.e. the number of table rows to be processed, is defined in the XML file, through the
    <code>
     batchSize
    </code>
    parameter.
   </td>
   <td headers="d25174e444">
    <p>
     <a href="https://learn.microsoft.com/en-us/dotnet/api/microsoft.data.sqlclient.sqlbulkcopy">
      SqlBulkCopy
     </a>
     is used to copy the data.
    </p>
    <p>
     There is no single transaction performed for archival and deletion.
    </p>
   </td>
  </tr>
 </tbody>
</table>