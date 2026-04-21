---
title: "Step 1: Saving the connection strings"
visible: true
slug: "saving-the-connection-strings-and-tenant-names"
---

Save the following information for further usage:

* The connection string for the Orchestrator database in the standalone deployment;
  + The `test-automation` database connection string.
* The connection string for the Insights database in the standalone deployment;
* The connection string for the `AutomationSuite_Platform` database in the Automation Suite deployment. You can retrieve the connection string from the `input.json` file, under the `platform` parameter.
* The following Test Manager information from the `appsettings.production.json` file located in the Test Manager installation directory:
  + The connection string for the Test Manager database in the standalone deployment.

You can find the connection string in the following key: `Database.ConnectionString.testmanagementhub`.
  + The storage location information stored in the `Storage.Location` key.
  + The information stored in the `Security.DataEncryptionKey` key.
  :::note
  If the `appsettings.production.json` file is encrypted, you can use the Test Manager provisioning tool to decrypt it. For more information, visit [Test Manager config file encryption](https://docs.uipath.com/test-suite/standalone/2023.10/installation-guide/test-manager-config-file-encryption).
  :::