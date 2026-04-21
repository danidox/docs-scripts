---
title: "Updating credentials"
visible: true
slug: "updating-credentials"
---

## Guidelines

To update credentials for the different Automation Suite components, take the following steps:

1. Generate the `input.json` file.
2. Provide the new credentials for the given components in the `input.json` as described in each component section.
3. Run the `uipathctl` CLI as described in each component section.

## Generating the input.json file

Generate the latest `input.json` file as follows:

* **A**: Run the following command to get the latest revision of your `input.json` file:
  ```
  uipathctl manifest get-revision
  ```
* **B**: Run the following command to list all the past `input.json` files and determine the one you wish to choose:
  ```
  uipathctl manifest list-revisions
  ```

## Updating the SQL connection strings

There are multiple scenarios where you may want to update the connection string used by Automation Suite products to connect to the SQL database, such as the following:

* When periodically rotating the password used to connect to the database, for security and compliance
* When changing the FQDN for the SQL server
* When migrating the database to another SQL server for maintenance purposes
* When adding, modifying, or removing one or more connection attributes, such as `MultiSubnetFailover`
* When switching from basic authentication to integrated authentication using Kerberos and AD
  :::important
  Products in Automation Suite do not create tables or schema at the time of updating the SQL database connection string. Make sure your new connection string refers to the same database that you currently use. To avoid downtime during the update process, make sure that your current connection string is valid at the time of the update process. You can revoke your old connection string after the update.
  :::

### Updating the connection strings for installed products

To update the connection string for installed products in Automation Suite, connect to any of the server nodes and perform the following operations.

1. Generate the `input.json` file.
2. Provide the new connection strings for the installed products in the `input.json`.
3. Run the `uipathctl manifest apply` command.

#### Providing the new connection strings for installed products

There are two ways to provide the connection strings for products running in Automation Suite:

* A: Provide a connection string template that will be common to all the products running in Automation Suite. This approach will assume the default database names for all the products.
* B: Provide connection strings specific to each product.
  :::important
  Make sure you escape NET, JDBC, or ODBC passwords as follows:
  * for NET: add **`'`** at the beginning and end of the password, and double any other `'`.
  * for JDBC/ODBC: add **`{`** at the beginning of the password and **`}`** at the end, and double any other **`}`**. Do not double `{`.
  If you set `TrustServerCertificate=False`, then you may have to provide an additional CA certificate for the SQL Server. This is required if the SQL Server certificate is self-signed or signed by an internal CA. For details, see [Updating the CA certificates](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#updating-the-ca-certificates).
  :::
To encode or decode Base64 strings using PowerShell, you can use the following commands:

* decode Base64 string: `[System.Text.Encoding]::Default.GetString([System.Convert]::FromBase64String('<base64_string>'))`
* encode Base64 string: `[System.Convert]::ToBase64String([System.Text.Encoding]::Default.GetBytes('<plain_text>'))`

**A: Providing a common connection string for all products**

All the products running in Automation Suite refer to a common template connection string. **One use case for choosing this method would be when you want to change the password for all the products at once. Note that, in this case, the password will be the same for all the products.**

In this scenarios, the database names for all products must be the default ones, as required by Automation Suite. If the database names you configured do not meet the Automation Suite requirements, follow the next step.

:::tip
Check the list of databases and their default names in [SQL database](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#sql-database).
:::

The following table explains which template format the product services accept:

Expand Table

| Parameter | Description | Products |
| --- | --- | --- |
| `sql_connection_string_template` | Full [ADO.NET](https://docs.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectionstring?view=dotnet-plat-ext-5.0#remarks) connection string where Catalog name is set to `DB_NAME_PLACEHOLDER`. The installer will replace this placeholder with the default database names for the installed suite services. | Platform, Orchestrator, Automation Suite Robots, Test Manager, Automation Hub, Automation Ops, Insights, Data Service, Process Mining, ECS, LLM Gateway, LLM Observability, Solutions |
| `sql_connection_string_template_jdbc` | Full [JDBC](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=sql-server-ver15) connection string where database name is set to `DB_NAME_PLACEHOLDER`. The installer will replace this placeholder with the default database names for the installed suite services. | AI Center |
| `sql_connection_string_template_odbc` | Full [ODBC](https://www.connectionstrings.com/microsoft-sql-server-odbc-driver/) connection string where database name is set to `DB_NAME_PLACEHOLDER`. The installer will replace this placeholder with the default database names for the installed suite services. | Document Understanding, Apps |
| `sql_connection_string_template_sqlalchemy_pyodbc` | Full SQL alchemy [PYODBC](https://docs.sqlalchemy.org/en/14/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc) connection string where database name is set to `DB_NAME_PLACEHOLDER`. The installer will replace this placeholder with the default database names for the installed suite services. | Document Understanding |
| `postgresql_connection_string_template_sqlalchemy_pyodbc` | Full SQL alchemy [PSYCOPG2](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2) connection string where database name is set to DB_NAME_PLACEHOLDER. The installer will replace this placeholder with the default database names for the installed suite services. | Process Mining |

**sql_connection_string_template example**
```
Server=tcp:sfdev1804627-c83f074b-sql.database.windows.net:1433;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=testadmin;Password=***;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Max Pool Size=100;
```

**sql_connection_string_template_jdbc example**
```
jdbc:sqlserver://sfdev1804627-c83f074b-sql.database.windows.net:1433;database=DB_NAME_PLACEHOLDER;user=testadmin;password=***;encrypt=true;trustServerCertificate=false;Connection Timeout=30;hostNameInCertificate=sfdev1804627-c83f074b-sql.database.windows.net"
```

**sql_connection_string_template_odbc example**
```
SERVER=sfdev1804627-c83f074b-sql.database.windows.net,1433;DATABASE=DB_NAME_PLACEHOLDER;DRIVER={ODBC Driver 17 for SQL Server};UID=testadmin;PWD=***;MultipleActiveResultSets=False;Encrypt=YES;TrustServerCertificate=NO;Connection Timeout=30;"
```

**sql_connection_string_template_sqlalchemy_pyodbc example**
```
"mssql+pyodbc://testadmin%40sfdev4515230-sql.database.windows.net:<password>@sfdev4515230-sql.database.windows.net:1433/DB_NAME_PLACEHOLDER?driver=ODBC+Driver+17+for+SQL+Server"
```

**postgresql_connection_string_template_sqlalchemy_pyodbc example**
```
"postgresql+psycopg2://testadmin:<password>@sfdev8454496-postgresql.postgres.database.azure.com:5432/DB_NAME_PLACEHOLDER"
```

:::note
Update the `input.json` with the new connection string template you want to update.
:::

**B: Providing connection strings specific to each product**

**Platform**

The Platform service provides administrative capabilities such as organization and tenant management, licensing management, user management, etc. The Platform service is enabled by default and cannot be removed. Its default database name is `AutomationSuite_Platform`.

To provide a connection string for the Platform service, add or update the following section in the `input.json` file:

```
"platform": {
  "sql_connection_str": "***" // dotnet connection string 
}
```

**Orchestrator**

The default database name for Orchestrator is `AutomationSuite_Orchestrator`.

To provide a connection string for the Orchestrator service, add or update the following section in the `input.json` file:

```
"orchestrator": {
  "sql_connection_str": "***" // dotnet connection string
}
```

**Automation Suite Robots**

Automation Suite Robots and Orchestrator share the same database by default. The database name is `AutomationSuite_Orchestrator`.

To provide a connection string for Automation Suite Robots, add or update the following section in the `input.json` file:

```
"asrobots": {
  "sql_connection_str": "***" // dotnet connection string
}
```

**Automation Hub**

The default database name for Automation Hub is `AutomationSuite_Automation_Hub`.

To provide a connection string for the Automation Suite service, add or update the following section in the `input.json` file:

```
"automation_hub": {
  "sql_connection_str": "***" // dotnet connection string
}
```

**Automation Ops**

The default database name for Automation Ops is `AutomationSuite_Platform`.

To provide a connection string for the Automation Ops service, add or update the following section in the `input.json` file:

```
"automation_ops": {
  "sql_connection_str": "***" // dotnet connection string
}
```

**AI Center**

The default database name for AI Center is `AutomationSuite_AICenter`.

To provide a connection string for the AI Center service, add or update the following section in the `input.json` file:

```
"aicenter": {
  "sql_connection_str": "***" // jdbc connection string
}
```

**Apps**

The default database name for Apps is `AutomationSuite_Apps`.

To provide a connection string for the Apps service, add or update the following section in the `input.json` file:

```
"apps": {
  "sql_connection_str": "***" // odbc connection string
}
```

**Data Service**

The default database name for Data Service is `AutomationSuite_DataService`.

To provide a connection string for the Data Service service, add or update the following section in the `input.json` file:

```
"dataservice": {
  "sql_connection_str": "***" // dotnet connection string
}
```

**Document Understanding**

The default database name for Document Understanding is `AutomationSuite_DU_Datamanager`.

To provide a connection string for the Document Understanding service, add or update the following section in the `input.json` file:

```
"documentunderstanding": { 
"enabled": true,
"sql_connection_str": "***" // dotnet connection string,
"datamanager": {
 "sql_connection_str": "***" // odbc connection string
 "pyodbc_sql_connection_str": "***" // python sql connection string
 }
}
```

**Insights**

The default database name for Insights is `AutomationSuite_Insights`.

To provide a connection string for the Insights service, add or update the following section in the `input.json` file:

```
"insights": {
  "sql_connection_str": "***" // dotnet connection string
}
```

**Process Mining**

The default database name for Process Mining is `AutomationSuite_ProcessMining_Metadata`.

To provide a connection string for the Process Mining service, add or update the following section in the `input.json` file:

```
"process_mining": {
    "enabled": true,
    "sql_connection_str": "***", // dotnet connection string
    "airflow": {
        "metadata_db_connection_str": ""
    },
    "warehouse": {
        "sql_connection_str": "",
        "master_sql_connection_str": "",
        "sqlalchemy_pyodbc_sql_connection_str": ""
    }
}
```

**Test Manager**

The default database name for Test Manager is `AutomationSuite_Test_Manager` .

To provide a connection string for the Test Manager service, add or update the following section in the `input.json` file:

```
"test_manager": {
  "sql_connection_str": "***" // dotnet connection string
}
```

**Integration Services**

The default database name for Integration Services is `AutomationSuite_Integration_Services` .

To provide a connection string, add or update the following section in the `input.json` file:

```
"integrationservices": {
  "sql_connection_str": "***" // dotnet connection string
}
```

**Studio Web**

The default database name for Studio Web is `AutomationSuite_StudioWeb` .

To provide a connection string, add or update the following section in the `input.json` file:

```
"studioweb": {
  "sql_connection_str": "***" // dotnet connection string
}
```

**Context Grounding Service**

The default database name for Context Grounding are `AutomationSuite_ECS` and `AutomationSuite_ECSVector`.

To provide a connection string, add or update the following section in the `input.json` file:

```
"ecs": {
      "enabled": true, //Set to "false" to disable
      "sql_connection_str": "", //Optional and only require to override the default database name - dotnet connection string
      "sql_vector_connection_str": "", //Optional and only require to override the default database name - dotnet connection string
    }
```

**LLM Gateway**

The default database name for LLM gateway is `AutomationSuite_LLMGateway`.

To provide a connection string, add or update the following section in the `input.json` file:

```
"llmgateway": {
      "enabled": true, //Set to "false" to disable
      "sql_connection_str": "" //Optional and only require to override the default database name - dotnet connection string
    }
```

**LLM Observability**

The default database name for LLM Observability is `AutomationSuite_Llmops`.

To provide a connection string, add or update the following section in the `input.json` file:

```
"llmobservability": {
      "enabled": true, //Set to "false" to disable
      "sql_connection_str": "" //Optional and only require to override the default database name - dotnet connection string
    }
```

**Solutions**

The default database name for Automation Solution is `AutomationSuite_AutomationSolutions`.

To provide a connection string, add or update the following section in the `input.json` file:

```
 "automationsolutions": {
      "enabled": true, //Set to "false" to disable
      "sql_connection_str": "", //Optional and only require to override the default database name - dotnet connection string
    }
```

#### Running the uipathctl installer

To complete the update, run the `uipathctl` installer using the following command:

```
uipathctl manifest apply input.json --versions versions.json
```

## Updating Redis credentials

### Providing the new credentials for Redis

Update the following section in the `input.json` file with the new password and/or hostname:

```
"fabric": {
  "redis": {
    "hostname": "new_hostname",
    "password": "new_password",
    "port": 6380,
    "tls": true
  }
```

### Running the uipathctl installer

To complete the update of the Redis credentials, run the `uipathctl` installer using the following command:

```
uipathctl manifest apply input.json --only redis --versions versions.json
```

:::note
You can use the dry-run flag with `uipathctl` to print the result of the command without applying it.
:::

## Updating objectstore credentials

Update the following section in the `input.json` file with the new access_key, secret_key or acount_key and account_name:

```
"external_object_storage": {
  "enabled": false, // <true/false>
  "create_bucket": true, // <true/false>
  "storage_type": "s3", // <s3,azure,aws>
  "fqdn": "",  // <needed in case of aws non instance profile>
  "port": 443, // <needed in case of aws non instance profile>
  "region": "", 
  "access_key": "", // <needed in case of aws non instance profile>
  "secret_key": "", // <needed in case of aws non instance profile>
  "use_managed_identity": false, // <true/false>
  "bucket_name_prefix": "",
  "bucket_name_suffix": "",
  "account_key": "", // <needed only when using non managed identity>
  "account_name": "",
  "azure_fqdn_suffix": "core.windows.net",
  "client_id": "" // <optional field in case of managed identity>
},
```

### Running the uipathctl installer

To complete the update of the object store credentials, run the `uipathctl` installer using the following command:

```
uipathctl manifest apply input.json --versions versions.json
```

:::note
You can use the dry-run flag with `uipathctl` to print the result of the command without applying it.
:::

## Updating the registry credentials

When the container registry in use requires authentication to pull images, pods must use a secret named `uipathpullsecret`. To update `uipathpullsecret`, take the following steps:

1. Update the registry section of the `input.json` file:
   ```
     "registries": { 
       "docker": { 
         "url": "yourContainerRegistryUrl", 
         "username": "username", 
         "password": "newpassword" 
       }, 
       "helm": { 
         "url": "yourContainerRegistryUrl", 
         "username": "username", 
         "password": "newpassword" 
       } 
     }
   ```
2. Delete the existing `uipathpullsecret`:
   ```
   kubectl delete secret  uipathpullsecret -n <uipath>
   kubectl delete secret  uipathpullsecret -n <uipath-installer>
   ```
3. Rerun the installation command:
   ```
   uipathctl manifest apply input.json --versions versions.json
   ```