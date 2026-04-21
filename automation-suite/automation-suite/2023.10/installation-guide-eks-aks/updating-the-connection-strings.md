---
title: "Step 5: Updating the migrated product connection strings"
visible: true
slug: "updating-the-connection-strings"
---

## Downloading uipathctl

To download `uipathctl`, see [Downloading the installation packages](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/downloading-the-installation-packages#downloading-the-installation-packages).

## Generating the configuration file

To generate the `input.json` configuration file, take one of the following steps:

* **Option A**: Generate the latest `input.json` file:
  ```
  uipathctl manifest get-revision | Out-File -Encoding ascii input.json
  ```
* **Option B**: List all the past `input.json` files and determine which one you want to choose:
  ```
  uipathctl manifest list-revisions
  ```

## Replacing the connection string and starting the installation

1. Move the `versions.json` file to the same directory as `input.json`. You can get `versions.json` from the Automation Suite installation folder.
2. Provide the new connection strings for the installed products.
   * To provide the restored connection string to the Orchestrator service, add or update `sql_connection_str` under `orchestrator` in the `input.json` file:
     ```
     "orchestrator": {
       "sql_connection_str": "<restored orchesrator connection string>",   (added line)
       "enabled": true
     }
     ```
   * If Test Automation tables are placed inside the standalone Orchestrator database, you can also add the same connection string for Test Automation feature inside the `input.json` file:
     ```
     "orchestrator": {
       "testautomation": {
         "enabled": true,
         "sql_connection_str": "<restored orchestrator connection string>"
       },
       "sql_connection_str": "<restored orchestrator connection string>",   (added line)
       "enabled": true
     }
     ```
   * If Test Automation tables are not placed inside the standalone Orchestrator database, you have to add or update `sql_connection_str` under `testautomation` in the `input.json`:
     ```
     "testautomation": {
        "enabled": true,   
        "sql_connection_str": "<restored test-automation connection string>",  (added line)
     }
     ```
   * To provide the restored connection string to the Insights service, add or update `sql_connection_str` under `insights` in the `input.json` file.
     ```
     "insights": {   
        "sql_connection_str": "<restored connection string>",   (added line)
        "enabled": true }
     ```
   * To provide the restored connection string to the Test Manager service, add or update `sql_connection_str` under `test_manager` in the `input.json` file.
     ```
     "test_manager": {
       "sql_connection_str": "<restored test_manager connection string>",   (added line)
       "enabled": true
     }
     ```
3. Update the `input.json` file by running the installer.
   * To migrate Orchestrator only, run the following command:
     ```
     uipathctl manifest apply input.json --only orchestrator --versions versions.json
     ```
   * To migrate Insights only, run the following command:
     ```
     uipathctl manifest apply input.json --only insights --versions versions.json
     ```
   * To migrate Test Manager only, run the following command:
     ```
     ./bin/uipathctl manifest apply cluster_config.json --only test_manager --versions versions/helm-chart.json
     ```:::note
If you run the command on Windows, replace `uipathctl` with `.\uipathctl.exe` in the command.
   :::
4. Remap the organization IDs in the Insights tables. For more details, see [Remapping the organization IDs](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/remapping-the-organization-id#remapping-the-organization-ids).
5. Run the Test Manager migration script and provide the necessary parameters:
   ```
   ./testmanager_migrator.sh -k <encryption_key> -y
   ```

   1. To migrate the Test Automation module, as part of Orchestrator, run the following command:
      ```
      ./bin/uipathctl manifest apply cluster_config.json --only testautomation --versions versions/helm-chart.json
      ```