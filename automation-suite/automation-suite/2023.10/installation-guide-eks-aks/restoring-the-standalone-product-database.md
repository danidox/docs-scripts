---
title: "Step 2: Restoring the standalone product database"
visible: true
slug: "restoring-the-standalone-product-database"
---

Here we introduce a way to use SQL Server Management Studio (SSMS) to restore the database of a standaloneproduct to the Automation Suite SQL Server instance. For details on downloading and installing SQL Server Management Studio, see [Migration prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migration-prerequisites#tool-for-managing-microsoft-sql-server).

1. In SQL Server Management Studio connect to the standalone product database, select **Tasks**, then choose **Deploy Database to Azure SQL**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/265120)
2. Select **Connect** to connect to the Automation Suite SQL database. Provide the new database name. Choose the directory to store the temporary database file.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/265124)
3. Wait for the deployment to complete.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/265132)
4. Record the connection string for the restored standalone product database in Automation Suite.

## Restoring the standalone Orchestrator database on EKS

If you migrate to Automation Suite on EKS, you cannot directly restore the Orchestrator database to the Azure SQL database. You must first back up the standalone Orchestrator database to a file and then restore to the RDS database.

If Orchestrator and Identity share their their database, you can skip step 4. If they have separate databases, you must back them up separately.

1. Log into the standalone machine and log into SQL Server using SSMS.
2. Back up the standalone Orchestrator database:
   1. Go to **Databases**, right-click the Orchestrator database, select **Tasks**, and select **Back Up**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/281119)
   2. Confirm the backup path.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/281124)
   3. Complete the backup.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/281128)
3. Restore the standalone Orchestrator database to RDS on the Automation Suite on EKS instance on the standalone machine
   1. Upload the backed up `bak` file to S3 bucket.
      ```
      aws s3 cp <local-file-path> s3://haonan-msi-asair-migration-bucket/<filename>
      ```

Sample:

      ```
      aws s3 cp "C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\20230401_0614.bak" s3://haonan-msi-asair-migration-bucket/20230401_0614.bak --region us-west-2
      ```
   2. Grant permission to the restored database on AWS.

### Granting permissions to the restored database on AWS

1. Go to IAM, and create a new role with `AWSBackupServiceRolePolicyForRestores` permissions.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/281136)
2. Go to RDS and select `Option groups`:
   1. Create a group and provide the following details:
      * Name: SqlServerBackupRestore
      * Description: xxx
      * Engine: Select your DB engine
      * Major Engine Version: Select version of your DB instance.
   2. Select **Create**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/281140)
   3. Select the name of created group to edit it as follows:
      1. Select **Add**.
      2. Select **SQLSERVER_BACKUP_RESTORE**.
      3. Select the IAM role you created in the previous steps.
      4. Select **Immediately** to schedule instant change.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/281145)
   4. Back to RDSDatabases and select your instance.
      1. Select **Modify**.
      2. Select Option group you created in the previous step.
      3. Select Next.
      4. Select Apply immediately (it should not cause service downtime).
      5. Apply changes by selecting Modify DB instance.
      6. If you have connection to database from SQL Management Studio, close it and connect again.
3. Follow [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html) to database backed up bak file to AWS S3 bucket. Sample command:
   ```
   exec msdb.dbo.rds_restore_database
       @restore_db_name='UiPath_20230531',
       @s3_arn_to_restore_from='arn:aws:s3:::haonan-msi-asair-migration-bucket/20230401_0614.bak',
       @with_norecovery=0,
   ```