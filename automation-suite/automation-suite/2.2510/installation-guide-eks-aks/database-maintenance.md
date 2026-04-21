---
title: "Performing database maintenance"
visible: true
slug: "database-maintenance"
---

It is important to keep your databases free from clutter. To do this, we recommend performing the following operations:

* [Use SQL Server Maintenance Solution](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/database-maintenance#using-sql-server-maintenance-solution)
* [Delete old data periodically](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/database-maintenance#deleting-old-data-periodically)
* [Back up the database](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/database-maintenance#backing-up-the-database)

## Using SQL Server Maintenance Solution

SQL Server Maintenance Solution is a set of scripts that enable you to run backups, integrity checks, and index and statistics maintenance on all editions of Microsoft SQL Server, starting with the 2005 version. For details, see [this GitHub project](https://github.com/olahallengren/sql-server-maintenance-solution).

## Backing up the database

We recommend implementing regular backups of the SQL Server database, such as full weekly or daily incremental backups.

Additionally, we recommend using the DatabaseBackup stored procedure that is created using the script at [this location](https://ola.hallengren.com/sql-server-backup.html).

## Deleting old data periodically

### Shared Suite Capabilities

Create a separate database in which to save items before you delete them. This database acts as an archive for the items you may need to store for certain reasons, such as audits.

1. Create a new database called, for example, `UiPathArchives`:
   ```
   create database UiPathArchives
   ```
2. Create the following backup tables:
   1. `ArchiveAuditEvent` with the same structure as the `AuditEvent` table:
      ```
      SELECT * INTO [UiPathArchives].[dbo].[ArchiveAuditEvent] from [AutomationSuite_Platform].[adt].[AuditEvent] where 1 = 2
      ```
3. Archive the data:
   1. Archive audit records
      ```
      DECLARE @NumberOfDaysToKeep INT
      DECLARE @CurrentDate DATETIME

      -- Specify the number of days
      SET @NumberOfDaysToKeep = 60
      -- Archive the list of audit event records that you want to delete
      SET @CurrentDate = GetDate()
      BEGIN TRANSACTION
      INSERT INTO [UiPathArchives].[dbo].[ArchiveAuditEvent]
      SELECT
      [Id],[CreatedOn],[Version],[OrganizationId],[Source],[Category],[Action],[IsUserEvent],
      [UserId],[FullName],[Email],[DetailsVersion],[Details],[OperationId]
      FROM [adt].[AuditEvent]
      WHERE DateDiff(day, CreatedOn, @CurrentDate) > @NumberOfDaysToKeep
      -- Delete the audit events
      DELETE FROM [adt].[AuditEvent]
      WHERE EXISTS (SELECT 1 FROM [UiPathArchives].[dbo].[ArchiveAuditEvent] WHERE Id = [adt].[AuditEvent].[Id])
      COMMIT TRANSACTION
      ```

Old data is copied to these archives prior to being deleted when using the following query.
4. Delete data from the table.
   :::important
   Before running the following script, make sure to adapt them to your environment.
   :::

   1. Audit events
      ```
      declare @NumberOfDaysToKeep int
      declare @CurrentDate datetime

      -- Specify the number of days
      SET @NumberOfDaysToKeep = 60
      -- Create temporary table with the list of audit event records that you want to delete
      SET @CurrentDate = GetDate()
      SELECT
      [Id],[CreatedOn],[Version],[OrganizationId],[Source],[Category],[Action],[IsUserEvent],
      [UserId],[FullName],[Email],[DetailsVersion],[Details],[OperationId]
      INTO #TempAuditRecordsToDelete
      FROM [adt].[AuditEvent]
      WHERE DateDiff(day, CreatedOn, @CurrentDate) > @NumberOfDaysToKeep
      -- Review the audit event records to be deleted
      SELECT * FROM #TempAuditRecordsToDelete
      -- Delete the audit events
      BEGIN TRANSACTION
      DELETE FROM [adt].[AuditEvent]
      WHERE EXISTS (SELECT 1 FROM #TempAuditRecordsToDelete WHERE Id = [adt].[AuditEvent].[Id])
      DROP TABLE #TempAuditRecordsToDelete
      COMMIT TRANSACTION
      ```

### Identity Server

Create a separate database in which to save items before you delete them. This database acts as an archive for the items you may need to store for certain reasons, such as audits.
:::note
The database maintenance script provided in this section is supported only when using SQL Server on-premises. It does not work with Azure SQL. If your Automation Suite deployment uses Azure SQL, do not run this script.
:::

1. Create a new database called, for example, `UiPathIdentityArchives`:
   ```
   create database UiPathIdentityArchives
   ```
2. Create the following backup tables:
   1. `ArchiveLoginAttempts` with the same structure as the `UserLoginAttempts` table:
      ```
      select * into [UiPathIdentityArchives].[dbo].[ArchiveUserLoginAttempts] from [AutomationSuite_Platform].[identity].[UserLoginAttempts] where 1=2
      ```

Old data is copied to these archives prior to being deleted when using the following query.
3. Delete data from the table.
   :::important
   Before running the following script, make sure to adapt them to your environment.
   :::

   1. User login attempts

To delete login attempts older than 60 days, for example, use the following query. It can be executed manually or scheduled in an SQL Server Job.

      ```
      declare @NumberOfDaysToKeep int
      set @NumberOfDaysToKeep = 60
      if OBJECT_ID('[UiPathIdentityArchives].[dbo].[UserLoginAttemps]') = NULL 
        begin select * into [UiPathIdentityArchives].[dbo].[UserLoginAttemps] from [identity].UserLoginAttempts where 1=2 end
      begin transaction
        set identity_insert [UiPathIdentityArchives].[dbo].[UserLoginAttemps] on
        insert into [UiPathIdentityArchives].[dbo].[UserLoginAttemps] ([Id],[PartitionId],[UserId],[UserNameOrEmailAddress],[ClientIpAddress],[ClientName],[BrowserInfo],[Result],[CreationTime],[AuthenticationProvider],[PartitionName])
          select [Id],[PartitionId],[UserId],[UserNameOrEmailAddress],[ClientIpAddress],[ClientName],[BrowserInfo],[Result],[CreationTime],[AuthenticationProvider],[PartitionName]
            from [identity].UserLoginAttempts where DateDiff(day, CreationTime, GetDate()) > @NumberOfDaysToKeep
        delete from [identity].UserLoginAttempts where DateDiff(day, CreationTime, GetDate()) > @NumberOfDaysToKeep
      commit transaction
      ```

### Orchestrator

For details on how to periodically delete old data from the Orchestrator database, see [Cleaning up the Orchestrator database](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/cleaning-up-the-orchestrator-database#cleaning-up-the-orchestrator-database).

### Automation Hub

Automation Hub relies on its historical data for runtime views and dashboards, and due to its nature, it does not have the concept of cleaning up old data. Similar to other services, it is recommended to regularly back up the Automation Hub database through methods such as full weekly backups or daily incremental backups.

### Process Mining

Process Mining on Automation Suite provides built-in automatic database cleanup ensuring optimal efficiency and performance. This guarantees the regular removal of unnecessary data, keeping your database cleaned up and functional without the need for any manual actions to free up resources.