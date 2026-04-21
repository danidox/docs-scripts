---
title: "Managing products"
visible: true
slug: "managing-products"
---

You can enable and disable products in Automation Suite at any point post-installation.

To do that, you must access and update the `input.json` file and apply the new configuration via `uipathctl.`

:::important
You cannot enable or disable any product during an Automation Suite upgrade.
:::

## Step 1: Changing the product selection in the configuration file

1. Change the product selection in the configuration file.

To do that, edit `input.json` with the editor of your choice.
2. In the services list, set the `enable` flags to `true` or `false` for the specific services you want to enable or disable. See the following examples for individual products.
   :::note
   You can manage Action Center and Apps simply by updating the `enable` flag. Other products might require an additional step to configure the installation. See the following instructions for details.
   :::

### Enabling or disabling Action Center

See the following configuration details for enabling or disabling Action Center in the `input.json` file:

```
"actioncenter": {
  "enabled": "true" //Set to "false" to disable the Action Center
}
```

### Enabling or disabling Apps

Apps requires updating the `enable` flag and an SQL database.

If you previously set a value for `sql_connection_string_template_odbc` in `input.json`, then the default database name is `AutomationSuite_Apps`.

To change the default database name, you need to update the `sql_connection_str` inside the Apps field. This overrides the default database and connection string template set in `sql_connection_string_template_odbc`.

See the following configuration details for enabling or disabling Apps in the `input.json` file:

```
"apps": {
  "enabled": "true" //Set to "false" to disable the Apps
  "sql_connection_str": "" ////Optional and only require to override the default database name
}
```

### Enabling or disabling AI Center

AI Center requires updating the `enable` flag and an SQL database.

If you previously set a value for `sql_connection_string_template_jdbc` in `input.json`, then the default AI Center database name is `AutomationSuite_AICenter`.

To change the default database name, you need to update the `sql_connection_str` inside the AI Center field. This overrides the default database and connection string template set in `sql_connection_string_template_jdbc`.

See the following configuration details for enabling or disabling AI Center in `input.json`:

```
"aicenter": {
  "enabled": "true", //Set to "false" to disable the AICenter
  "sql_connection_str": "" //Optional and only required to override the default database name
}
```

AI Center installed in Automation Suite on AKS/EKS cannot connect to an external Orchestrator.

### Enabling or disabling AI Trust Layer

To enable all AI Trust Layer components, in the `llmgateway` and `llmobservability` sections of the `input.json` file, set the enabled flag to `true`:

```
"llmgateway": {
      "enabled": true, //Set to "false" to disable
      "sql_connection_str": "" //Optional and only require to override the default database name
    },
"llmobservability": {
      "enabled": true, //Set to "false" to disable
      "sql_connection_str": "" //Optional and only require to override the default database name
```

### Enabling or disabling Automation Hub

To enable Automation Hub, in the `automation_hub` section of the `input.json` file, set the `enabled` flag to `true`:

```
"automation_hub": {
  "enabled": "true" //Set to "false" to disable Automation Hub
  "sql_connection_str": "" //Optional and only require to override the default database name
}
```

To disable Automation Hub, set the `enabled` flag to `false` in the `automation_hub` section of the `input.json` file.

### Enabling or disabling Automation Ops

Automation Ops requires updating the `enable` flag and an SQL database.

If you previously set a value for `sql_connection_string_template` in `input.json`, then the default database name for Automation Ops is `AutomationSuite_Platform`.

To change the default database name, you need to update the `sql_connection_str` inside the Automation Ops field. This overrides the default database and connection string template set in `sql_connection_string_template`.

:::note
Automation Ops shares a database with the core platform, including Orchestrator. If you change the database here, you update the database for the core platform as well.
:::

See the following configuration details for enabling or disabling Automation Ops in `input.json`:

```
"automation_ops": {
  "enabled": "true", //Set to "false" to disable the Automation Ops
  "sql_connection_str": "" //Optional and only require to override the default database name
}
```

### Enabling or disabling Automation Suite Robots

:::note
Before enabling Automation Suite Robots, make sure you meet the requirements.
:::

To enable Automation Suite Robots, take the following steps:

1. Enable the `asrobots` flag in the `input.json` file. If you want to enable package caching, make sure to properly configure the `packagecaching` and `packagecachefolder` flags as well.
   ```
   {
     "asrobots": {
        "enabled": Boolean,
        "packagecaching": Boolean,
        "packagecachefolder": String
     }
   }
   ```

Expand Table

   | Parameter | Default value | Description |
   | --- | --- | --- |
   | `packagecaching` | `true` | When set to `true`, robots use a local cache for package resolution. |
   | `packagecachefolder` | `/uipath_asrobots_package_cache` | The disk location on the serverless agent node where the packages are stored. |
   :::note
   Package caching optimizes your process runs and allows them to run faster. NuGet packages are fetched from the filesystem instead of being downloaded from the Internet/network. This requires an additional space of minimum 10GB and should be allocated to a folder on the host machine filesystem of the dedicated nodes.
   :::
2. If you use a multi-node HA-ready production setup, you must configure a specialized agent node for Automation Suite Robots.

To disable Automation Suite Robots, disable the `asrobots` flag in the `input.json` file.

### Enabling or disabling Context Grounding

To enable Context Grounding Service, in the `ecs` section of the `input.json` file, set the `enabled` flag to `true`:

```
"ecs": {
      "enabled": true, //Set to "false" to disable
      "sql_connection_str": "", //Optional and only require to override the default database name
      "sql_vector_connection_str": "", //Optional and only require to override the default database name
    }
```

### Enabling or disabling Data Service

Data Service requires updating the `enable` flag and an SQL database.

If you previously set a value for `sql_connection_string_template` in `input.json`, then the default database name is `AutomationSuite_DataService`.

To change the default database name, you need to update the `sql_connection_str` inside the Data Service field. This overrides the default database and connection string template set in `sql_connection_string_template`.

See the following configuration details for enabling or disabling Data Service in `input.json`:

```
"dataservice": {
  "enabled": "true", //Set to "false" to disable the Data Service,
  "sql_connection_str": "" //Optional and only require to override the default database name
}
```

### Enabling or disabling Document Understanding

Document Understanding requires updating the `enable` flag and an SQL database.

If you previously set a value for `sql_connection_string_template_odbc` in `input.json`, then the default database name is `AutomationSuite_DU_Datamanager`.

To change the default database name, you need to update the `sql_connection_str` inside the Document Understanding field. This overrides the default database and connection string template set in `sql_connection_string_template_odbc`.

If you want to only enable AI Center-based projects, provide the following configuration details in the `input.json` file:

```
"documentunderstanding": {
  "enabled": "true", //Set to "false" to disable the Document Understanding
  "sql_connection_str": "" //Optional and only required to override the default database name
}
  "pyodbc_sql_connection_str": "" //Optional and only required to override the default database name
    }
```

If you want to enable both AI Center-based projects and Document Understanding modern projects, provide the following configuration details in the `input.json` file:

```
"documentunderstanding": {
  "enabled": "true", //Set to "false" to disable the Document Understanding
  "sql_connection_str": "" //Optional and only required to override the default database name
}
  "pyodbc_sql_connection_str": "" //Optional and only required to override the default database name
  "modernProjects": {
      "enabled": "true" //Set to "false" to disable Document Understanding modern projects
      "enable_cpu_inference": "false"  //Set to "true" to use CPU instead of GPU for AIHM and SSDE services during DU installation. 
    }
```

### Enabling or disabling Insights

Insights requires updating the `enable` flag and an SQL database.

If you previously set a value for `sql_connection_string_template` in `input.json`, then the default database name is `AutomationSuite_Insights`.

To change the default database name, you need to update the `sql_connection_str` inside the Insights field. This overrides the default database and connection string template set in `sql_connection_string_template`.

To enable the Insights Real-time monitoring feature, set the `enable_realtime_monitoring` flag to `true`.

Insights has an optional SMTP configuration to enable receiving email notifications. For details, see Configuring input.json.

See the following configuration details for enabling or disabling Insights in `input.json`:

```
"insights": {
  "enabled": "true", //Set to "false" to disable the Insights,
  "enable_realtime_monitoring": "false", //Set to "true" to enable Insights Real-time monitoring,
  "sql_connection_str": "" //Optional and only require to override the default database name
}
```

### Enabling or disabling Integration Service

To enable Integration Service, in the `integrationservices` section of the `input.json` file, set the `enabled` flag to `true`:

```
"integrationservices": {
  "enabled": "true" //Set to "false" to disable Integration Service
  "sql_connection_str": "" //Optional and only require to override the default database name
}
```

### Enabling or disabling Orchestrator

To enable Orchestrator, set the `orchestrator` flag to `true` in the `input.json` file.

```
"orchestrator": {
  "enabled": "true" //Set to "false" to disable Orchestrator
  "sql_connection_str": "" //Optional and only require to override the default database name
}
```

To disable Orchestrator, set the `orchestrator` flag to `false` in the `input.json` file.

### Enabling or disabling Process Mining

:::important
If Process Mining is enabled, PostgreSQL is required for the `AutomationSuite_Airflow` database. Refer to [SQL requirements for Process Mining](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#sql-requirements-for-process-mining) for more information.
:::

To enable Process Mining, make the following changes to the `input.json` file:

1. Enable the `processmining` flag.
2. Configure the following connection string templates:
   * `sql_connection_string_template`
   * `sql_connection_string_template_jdbc`
   * `sql_connection_string_template_odbc`
   * `sql_connection_string_template_sqlalchemy_pyodbc`
3. Add a separate connection string for the second SQL Server:
   ```
   "processmining": {
     "enabled": true,
     "sql_connection_str": "", // dotnet connection string
     "sqlalchemy_pyodbc_sql_connection_str": "", 
     "warehouse": {
           "sql_connection_str": "",
           "sqlalchemy_pyodbc_sql_connection_str": ""
        }
   }
   ```

To disable Process Mining, disable the `processmining` flag.

### Enabling or Disabling Studio Web

#### EKS

To enable Studio Web, in the `studioweb` section of the `input.json` file, set the `enabled` flag to `true`.

```
"studioweb": {
  "enabled": "true" //Set to "false" to disable Studio Web
  "sql_connection_str": "" //Optional and only require to override the default database name
}
```

#### AKS

To enable Studio Web, in the `studioweb` section of the `input.json` file, set the `enabled` flag to `true`.

Storage quotas for project and package services use default values if other values are not defined. Make sure to define only values that are higher than the default values:

```
"studioweb": {
  "enabled": "true" //Set to "false" to disable Studio Web
  "sql_connection_str": "" //Optional and only require to override the default database name
  "project_service_storage_quota": "500Gi" (optional)
  "package_service_storage_quota": "300Gi" (optional)
}
```

### Enabling or disabling Test Manager

Test Manager requires updating the `enable` flag and an SQL database.

If you previously set a value for `sql_connection_string_template` in `input.json`, then the default database name is `AutomationSuite_Test_Manager`.

To change the default database name, you need to update the `sql_connection_str` inside the Test Manager field. This overrides the default database and connection string template set in `sql_connection_string_template`.

See the following configuration details for enabling or disabling Test Manager in `input.json`:

```
"test_manager": {
  "enabled": "true", //Set to "false" to disable the Test Manager,
  "sql_connection_str": "" //Optional and only require to override the default database name
}
```

### Enabling or disabling Autopilot for Everyone

To enable Autopilot for Everyone, in the `autopiloteveryone` section of the `input.json` file, set the `enabled` flag to `true`:

```
"autopiloteveryone": {
      "enabled": true //Set to "false" to disable
    }
```

### Enabling or disabling LLM gateway

To enable LLM gateway, in the `llmgateway` section of the `input.json` file, set the `enabled` flag to `true`:

```
"llmgateway": {
      "enabled": true, //Set to "false" to disable
      "sql_connection_str": "" //Optional and only require to override the default database name - dotnet connection string
    }
```

### Enabling or disabling LLM observability

To enable LLM observability, in the `llmobservability` section of the `input.json` file, set the `enabled` flag to `true`:

```
"llmobservability": {
      "enabled": true, //Set to "false" to disable
      "sql_connection_str": "" //Optional and only require to override the default database name - dotnet connection string
    }
```

### Enabling or disabling Solutions

To enable Solutions, in the `automationsolutions` section of the `input.json` file, set the `enabled` flag to `true`:

```
"automationsolutions": {
      "enabled": true, //Set to "false" to disable
      "sql_connection_str": "", //Optional and only require to override the default database name - dotnet connection string
    }
```

## Step 2: Running the installer to update the new product configuration

Once you update the `input.json`, run the following commands with the `uipathctl` installer to update the service configuration:

1. Run the following command to get an output of what changes will be made to the cluster:
   ```
   # uipathctl manifest apply --dry-run input.json --versions versions.json
   ```
2. To allow the installer to generate configurations, run the following command:
   ```
   uipathctl prereq create input.json --versions versions.json
   ```

For more details, refer to [Generating configurations automatically](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/checking-the-infrastructure-prerequisites).
3. To check the prerequisites based on the inputs you configured in the `input.json`, run the following command:
   ```
   uipathctl prereq run input.json --versions versions.json
   ```

For more details, refer to [Checking the prerequisites](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/checking-the-infrastructure-prerequisites).
4. To apply the changes on the cluster, run:
   ```
   # uipathctl manifest apply input.json --versions versions.json --log-level info --skip-helm
   ```