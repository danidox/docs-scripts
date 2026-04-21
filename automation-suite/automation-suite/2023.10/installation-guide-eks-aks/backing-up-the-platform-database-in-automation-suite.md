---
title: "Step 3: Backing up the platform database in Automation Suite"
visible: true
slug: "backing-up-the-platform-database-in-automation-suite"
---

To back up the the database of the shared platform capabilities in Automation Suite, take the following steps. Note that the default name of this database is `AutomationSuite_Platform`.

1. Log into the Automation Suite SQL Server using SSMS.
2. Right-click **Database**, select **Tasks**, and then **Export Data-tier Application**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/265137)
3. Select the output path for the `BACPAC` file.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/265145)
4. Finish the process.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/265149)