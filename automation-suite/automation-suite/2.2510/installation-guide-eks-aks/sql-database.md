---
title: "SQL database"
visible: true
slug: "sql-database"
---

:::important
Only Microsoft ODBC Driver 17 is supported.
:::

:::note
Unless otherwise specified in the dedicated requirements sections, these requirements are applicable to all Automation Suite products.
:::

You must bring an external SQL server to install Automation Suite and UiPath® products. Microsoft SQL Server 2016, 2017, 2019, and 2022 Standard and Enterprise editions are supported.

:::important
Currently, Orchestrator and AI Center require SQL Server version 2019 and higher to function optimally. SQL Server 2016 and 2017 are not supported in the Automation Suite versions from 2024.10.0 to 2024.10.2. All SQL versions are supported starting with Automation Suite versions 2024.10.3 or higher for all applications except Insights.
:::

Additional Microsoft SQL platforms, such as Azure SQL Database, Azure SQL Managed Instance, or Amazon Relational Database Service, are also supported as long as the Microsoft SQL Server database engine meets the requirements. For details, see [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix).

:::note
If Process Mining is enabled, PostgreSQL is required for the `AutomationSuite_Airflow` database. Refer to [SQL requirements for Process Mining](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#sql-requirements-for-process-mining) for more information.
:::
:::note
Make sure that the SQL server can be accessed from the cluster nodes.
:::
:::important
If you implement a Multi-AZ with Always On SQL setup where you specifically use a listener endpoint, such as with Amazon RDS, you must add an additional parameter, `MultiSubnetFailover`, to your connection strings. Automation Hub does not support `MultiSubnetFailover`.
:::

The `MultiSubnetFailover` parameter settings differ based on the type of connection string, as shown in the following examples:

* `sql_connection_string_template`: Set `MultiSubnetFailover=True`
* `sql_connection_string_template_jdbc`: Set `multiSubnetFailover=true`
* `sql_connection_string_template_odbc`: Set `MultiSubnetFailover=yes`
* `sql_connection_string_template_sqlalchemy_pyodbc`: Set `MultiSubnetFailover=YES`

The `MultiSubnetFailover` parameter allows for quick failover between multiple IPs from the DNS entry during any network or database disruptions.

Individual product support varies.

For each product you plan to deploy, you must:

* check the supported version of SQL Server as required by the product;
* meet the SQL Server configuration requirements, including SQL Server User permissions, as the product requires.

The general minimum hardware requirements for Microsoft SQL Server are as follows:

* 8 (v-)CPU
* 32 GB RAM
* 256 GB SSD

The minimum requirements are general guidance and do not guarantee reliable operation in a production deployment. Capacity planning is required to determine the hardware requirements for reliable operation. For details, see [Capacity planning](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/capacity-planning#capacity-planning).

Each UiPath® product requires its own SQL database.

## Database creation workflow

The interactive installer automatically creates databases using the following workflow:

1. The interactive installer script checks the value of the `sql.create_db` parameter in the `input.json` file.
   * If the `sql.create_db` parameter is set to `true`, the installer automatically generates all the databases on your behalf. In this case, the installer uses the default database names and default templates, and ignores any custom database names you provided.

For details, see [Automatically create the necessary databases](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#automatically-create-the-necessary-databases).
   * If `sql.create_db` is set to `false`, you must bring your own databases. In this case, you must manually set up your databases. Note that you can use custom database names, provided that you follow the provided naming conventions. This step is critical because we use the database name in conjunction with the connection template to form the database connection string. If you do not follow the recommended naming convention, you must provide the SQL connection strings yourself.

For details, see [Bring your own databases](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#bring-your-own-databases).
2. The interactive installer generates the connection strings as follows:
   * If you did not define a connection string for your service, the installer uses the connection template to generate all database connection strings.
   * If you defined a connection string for your service, the installer uses the provided connection string for your database.

## Automatically create the necessary databases

If you want the installer to create the databases, fill in the following fields of the `input.json` file:

| Parameter | Description |
| --- | --- |
| `sql.create_db` | Set to `true` to allow the installer to create the databases. Note that the installer uses the default database names and default templates, and ignores any custom database names you provided. |
| `sql.server_url` | FQDN of the SQL server, where you want the installer to configure database. |
| `sql.port` | Port number on which a database instance should be hosted in the SQL server. |
| `sql.username` | Username / user ID to connect to the SQL server. |
| `sql.password` | Password of the username provided earlier to connect to the SQL server. |

:::note
* Ensure the user has the `dbcreator` role. This grants them permission to create the database in SQL Server. Otherwise, the installation fails.
* Automatically creating the necessary databases does not work in combination with directory authentication. If you use directory
authentication, you must bring your own databases.
* ODBC connection does not support usernames that contain special characters. For database usernames for AI Center, Document
Understanding, and Apps, use only uppercase and lowercase letters.
:::
:::important
For Process Mining on Automation Suite, you need to manually create the PostgreSQL database for `AutomationSuite_Airflow` before installing or upgrading to Automation Suite 2.2510 or higher. The PostgreSQL database for Airflow will not be created automatically by the installer. Refer to [SQL requirements for Process Mining](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#sql-requirements-for-process-mining) for more information.
:::

## Bring your own databases

If you choose to bring your own databases for a new Automation Suite installation, we strongly recommend setting up new databases rather than using existing ones. This precaution is necessary to prevent any conflicts with the operation of Automation Suite that might occur due to leftover metadata from old databases.

If you bring your own database, you must provide the SQL connection strings for every database. Automation Suite supports the following SQL connection string formats:

:::note
For Document Understanding, make sure that you are using the same database, unless otherwise explicitly stated. Specific connection strings are assigned to various services and jobs that connect to the same database.
:::

Expand Table

| Parameter | Description | Products |
| --- | --- | --- |
| `sql_connection_string_template` | Full [ADO.NET](https://docs.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectionstring?view=dotnet-plat-ext-5.0#remarks) connection string where Catalog name is set to DB_NAME_PLACEHOLDER. The installer will replace this placeholder with the default database names for the installed suite services. | Platform  Orchestrator  Automation Suite Robots  Test Manager  Automation Hub  Automation Ops  Insights  Integration Service  Studio Web  Data Service  Process Mining  Document Understanding  LLM Gateway  LLM Observability  ECS  Solutions |
| `sql_connection_string_template_jdbc` | Full [JDBC](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=sql-server-ver15) connection string where database name is set to DB_NAME_PLACEHOLDER. The installer will replace this placeholder with the default database names for the installed suite services. | AI Center  Integration Service |
| `sql_connection_string_template_odbc` | Full [ODBC](https://www.connectionstrings.com/microsoft-sql-server-odbc-driver/) connection string where database name is set to DB_NAME_PLACEHOLDER. The installer will replace this placeholder with the default database names for the installed suite services. | Document Understanding  Apps  Integration Service |
| `sql_connection_string_template_sqlalchemy_pyodbc` | Full SQL alchemy [PYODBC](https://docs.sqlalchemy.org/en/14/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc) connection string where database name is set to DB_NAME_PLACEHOLDER. The installer will replace this placeholder with the default database names for the installed suite services. | Document Understanding |
| `postgresql_connection_string_template_sqlalchemy_pyodbc` | Full SQL alchemy [PSYCOPG2](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2) connection string where database name is set to DB_NAME_PLACEHOLDER. The installer will replace this placeholder with the default database names for the installed suite services. | Process Mining |

:::important
Make sure the SQL account specified in the connection strings is granted the `db_owner` role for all Automation Suite databases. If security restrictions do not allow the use of `db_owner`, then the SQL account should have the following roles and permissions on all databases:
* `db_securityadmin`
* `db_ddladmin`
* `db_datawriter`
* `db_datareader`
* `EXECUTE` permission on dbo, dt, authz, and msgbus schema
We only use the `db_securityadmin` and `db_ddladmin` roles during installation or if the databases are reprovisioned, so you may revoke these permission afterwards. Insights requires the `db_owner` role to be assigned for a successful installation.
:::
:::important
If you manually set the connection strings in the configuration file, you can escape SQL, JDBC, ODBC, or PYODBC passwords as follows:
* for SQL: add `'` at the beginning and end of the password, and double any other `'`.
* for JDBC/ODBC: add `{` at the beginning of the password and `}` at the end, and double any other `}`.
* for PYODBC: `username` and `password` should be url encoded to account for special characters. Document Understanding database passwords cannot start with `{`.
:::
:::important
The `AutomationSuite_ProcessMining_Airflow` database for Process Mining product **must** have `READ_COMMITTED_SNAPSHOT` enabled.
:::
:::note
By default, `TrustServerCertificate` is set to `False`, and you must provide an additional CA certificate for the SQL Server. This is required if the SQL Server certificate is self-signed or signed by an internal CA. If you do not provide the SQL Server certificate in this scenario, the prerequisite check will fail.
:::

sql_connection_string_template example

```
Server=tcp:sfdev1804627-c83f074b-sql.database.windows.net:1433;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=testadmin@sfdev1804627-c83f074b-sql.database.windows.net;Password=***;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Max Pool Size=100;
```

sql_connection_string_template_jdbc example

```
jdbc:sqlserver://sfdev1804627-c83f074b-sql.database.windows.net:1433;database=DB_NAME_PLACEHOLDER;user=testadmin;password=***;encrypt=true;trustServerCertificate=false;Connection Timeout=30;hostNameInCertificate=sfdev1804627-c83f074b-sql.database.windows.net"
```

sql_connection_string_template_odbc example

```
SERVER=sfdev1804627-c83f074b-sql.database.windows.net,1433;DATABASE=DB_NAME_PLACEHOLDER;DRIVER={ODBC Driver 17 for SQL Server};UID=testadmin;PWD=***;MultipleActiveResultSets=False;Encrypt=YES;TrustServerCertificate=NO;Connection Timeout=30;"
```

sql_connection_string_template_sqlalchemy_pyodbc example

```
mssql+pyodbc://testuser%40sfdev3082457-sql.database.windows.net:_-%29X07_%5E3-%28%3B%25e-T@sfdev3082457-sql.database.windows.net:1433/DB_NAME_PLACEHOLDER?driver=ODBC+Driver+17+for+SQL+Server"
```

postgresql_connection_string_template_sqlalchemy_pyodbc example (Process Mining)

```
postgresql+psycopg2://<user>:<password>@<host>:<port>/DB_NAME_PLACEHOLDER
```

sql_connection_string_template **and** postgresql_connection_string_template_sqlalchemy_pyodbc example (Process Mining)

```
"sql_connection_string_template": "Server=tcp:sfdev4515230-sql.database.windows.net,1433;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=testadmin@sfdev4515230-sql.database.windows.net;Password='07<l[xj-=~:z`Ds&nl';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Max Pool Size=100;"

"postgresql_connection_string_template_sqlalchemy_pyodbc ": 
"postgresql+psycopg2://<user>:<password>@sfdev4515230-postgresql.database.windows.net:5432/DB_NAME_PLACEHOLDER"
```

sql_connection_string_template **and** sql_connection_string_template_sqlalchemy_pyodbc example (Process Mining)

```
"sql_connection_string_template": "Server=tcp:sfdev4515230-sql.database.windows.net,1433;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=testadmin@sfdev4515230-sql.database.windows.net;Password='07<l[xj-=~:z`Ds&nl';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Max Pool Size=100;"

"sql_connection_string_template_sqlalchemy_pyodbc": "mssql+pyodbc://testadmin%40sfdev4515230-sql.database.windows.net:07%3Cl%5Bxj-%3D~%3Az%60Ds%26nl@sfdev4515230-sql.database.windows.net:1433/DB_NAME_PLACEHOLDER?driver=ODBC+Driver+17+for+SQL+Server"
```

Default and optional DB names for Automation Suite services

```
{
  "orchestrator": "AutomationSuite_Orchestrator",
  "orchestrator_ta": "AutomationSuite_Orchestrator",
  "asrobots": "AutomationSuite_Orchestrator",
  "orchestrator_upd": "AutomationSuite_Platform",
  "platform": "AutomationSuite_Platform",
  "test_manager": "AutomationSuite_Test_Manager",
  "automation_ops": "AutomationSuite_Platform",
  "automation_hub": "AutomationSuite_Automation_Hub",
  "insights": "AutomationSuite_Insights",
  "integrationservices": "AutomationSuite_Integration_Services",
  "studioweb": "AutomationSuite_StudioWeb"
  "dataservice": "AutomationSuite_DataService", 
  "aicenter": "AutomationSuite_AICenter",
  "documentunderstanding": "AutomationSuite_DU_Datamanager",
  "processmining_airflow": "AutomationSuite_Airflow",
  "processmining_metadata": "AutomationSuite_ProcessMining_Metadata",
  "processmining_warehouse": "AutomationSuite_ProcessMining_Warehouse",
  "apps": "AutomationSuite_Apps",
  "llmgateway": "AutomationSuite_LLMGateway",
  "ecs": "AutomationSuite_ECS",
  "ecs_vector": "AutomationSuite_ECSVector",
  "llmobservability": "AutomationSuite_Llmops",
  "automationsolutions": "AutomationSuite_AutomationSolutions",
}
```

:::note
If you want to override the connection string for any of the mentioned services, set the `sql_connection_str` for that specific service. You still have to manually create these databases before running the installer.
:::

Overriding the default connection string for Orchestrator and the platform

```
{
  "orchestrator": {
    "sql_connection_str": "Server=tcp:sfdev1804627-c83f074b-sql.database.windows.net,1433;Initial Catalog=CustomOrchDB;Persist Security Info=False;User Id=testadmin@sfdev1804627-c83f074b-sql.database.windows.net;Password=***;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Max Pool Size=100;"
  },
  "platform": {
    "sql_connection_str": "Server=tcp:sfdev1804627-c83f074b-sql.database.windows.net,1433;Initial Catalog=CustomIDDB;Persist Security Info=False;User Id=testadmin@sfdev1804627-c83f074b-sql.database.windows.net;Password=***;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Max Pool Size=100;"
  }
}
```

To override the database connection strings for other products, set the `sql_connection_str` in the corresponding product blocks. The connection string should have a format supported by the respective product.

Example for setting database connection string for AI Center

| Parameter | Description |
| --- | --- |
| `aicenter.sql_connection_str` | AI Center JDBC connection string |

:::note
Make sure the JDBC connection string has the format in the following sample:
:::

```
"aicenter": {
    "enabled": true,
    "sql_connection_str": "jdbc:sqlserver://sfdev1804627-c83f074b-sql.database.windows.net;database=aicenter;user=testadmin@sfdev1804627-c83f074b-sql.database.windows.net;password=TFgID_9GsE7_P@srCQp0WemXX_euHQZJ"
}
```

Sample Document Understanding connection string

```
"documentunderstanding": {
        "enabled": true,
        "sql_connection_str": "Server=SERVER_PLACEHOLDER;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=USER_PLACEHOLDER;Password='PASSWORD_PLACEHOLDER';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Max Pool Size=100;",
        "datamanager": {
            "sql_connection_str": "SERVER=SERVER_PLACEHOLDER;DATABASE=DB_NAME_PLACEHOLDER;DRIVER={ODBC Driver 17 for SQL Server};UID=USER_PLACEHOLDER;PWD={PASSWORD_PLACEHOLDER};;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;hostNameInCertificate=customer-sql.database.windows.net",
            "pyodbc_sql_connection_str": "mssql+pyodbc://testadmin%40sql.database.windows.net:Z%3Aw%21%zE%3Cb4@sql.database.windows.net:1433/DB_NAME_PLACEHOLDER?driver=ODBC+Driver+17+for+SQL+Server"
        }
    }
```

:::note
The data manager SQL connection string is optional only if you want to overwrite the default with your own.
:::

Sample Process Mining connection string (PostgreSQL)

```
  "processmining": {
    "enabled": true,
    "app_security_mode": "system_managed",
    "airflow": {
      "metadata_db_connection_str": "postgresql+psycopg2://testadmin:<password>@sfdev8454496-postgresql.postgres.database.azure.com:5432/AutomationSuite_Airflow"
    },
    "warehouse": {
      "sql_connection_str": "Server=tcp:kerberossql.autosuitead.local,1433;Initial Catalog=AutomationSuite_Warehouse;Persist Security Info=False;User Id=testadmin;Password='password';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
      "sqlalchemy_pyodbc_sql_connection_str": "mssql+pyodbc://testadmin:<password>@kerberossql.autosuitead.local:1433/AutomationSuite_Warehouse?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=YES&Encrypt=YES",
      "master_sql_connection_str": "Server=tcp:kerberossql.autosuitead.local,1433;Initial Catalog=master;Persist Security Info=False;User Id=testadmin;Password='password';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;"
    }
    "sql_connection_str": "Server=tcp:sfdev4515230-sql.database.windows.net,1433;Initial Catalog=AutomationSuite_ProcessMining_Metadata;User Id=testadmin@sfdev4515230-sql.database.windows.net;Password='password';Persist Security Info=False;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
  }
```

:::note
When using Kerberos authentication, utilize the `Integrated Security` and `Trusted_Connection` parameters. By setting `Integrated Security` to `true` and setting `Trusted_Connection` to `yes`, the credentials of the currently logged in user are used for the connection. In this case, you do not need to specify a separate username and password.
:::
:::important
Note that the names for *template* PYODBC connection string `postgresql_connection_string_template_sqlalchemy_pyodbc` (for PostgreSQL) and the PYODBC connection string `sqlalchemy_pyodbc_sql_connection_str` used when you *bring your own database* are different. Also connection string names are different for the template SQL `sql_connection_string_template` and `sql_connection_str` used when you *bring your own database*.
:::
:::important
If you bring your own database and you configured this using the `sql_connection_str` and `sqlalchemy_pyodbc_sql_connection_str` connection strings in the `processmining` section of the `input.json`file, the *template* connection strings `sql_connection_string_template` and `postgresql_connection_string_template_sqlalchemy_pyodbc` (for PostgreSQL) are ignored if specified.
:::
:::note
Set `MultiSubnetFailover=True` for `sql_connection_str` and `master_sql_connection_str` and `MultiSubnetFailover=Yes` for `sqlalchemy_pyodbc_sql_connection_str` connection strings. Note that for `pyodbc` you use '**=Yes'** instead of '**=True'**.
:::
:::note
Depending on the `app_security_mode` setting either a new SQL user is created for every Process Mining app by the system (`app_security_mode="system_managed"`), or a single SQL user account is created that is used for all process apps (`app_security_mode="single_account"`). Note that `app_security_mode="system_managed"` is the default setting, and that this requires advanced permissions for the database user. See [Configuring process app security](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/process-mining-specific-configuration).
:::

Sample Process Mining connection string

* Scenario: setup with Kerberos authentication (PostgreSQL)
```
"processmining": {
    "enabled": true,
    "airflow": {
      "metadata_db_connection_str": "postgresql+psycopg2://kerberos_user:@kerberospostgres.AUTOSUITEAD.LOCAL:5432/automationsuite_airflow"
    }
    "warehouse": {
        "sql_connection_str": "Server=tcp:assql2019.autosuitead.local,1433;Initial Catalog=AutomationSuite_ProcessMining_Warehouse;Persist Security Info=False;Integrated Security=true;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
        "sqlalchemy_pyodbc_sql_connection_str": "mssql+pyodbc://:@assql2019.autosuitead.local:1433/AutomationSuite_ProcessMining_Warehouse?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=YES&Encrypt=YES&Trusted_Connection=yes",
        "master_sql_connection_str": "Server=tcp:assql2019.autosuitead.local,1433;Initial Catalog=master;Persist Security Info=False;Integrated Security=true;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;"
      },
  },
```

Sample Process Mining connection string

* Scenario: Metadata database and data warehouse use separate SQL server (Non-Kerberos authentication).
```
"processmining": {
    "enabled": true,
    "warehouse": {
      "sql_connection_str": "Server=tcp:uipath-integration1.database.windows.net,1433;Initial Catalog=AutomationSuite_ProcessMining_Warehouse;Persist Security Info=False;User Id=userid;Password='password';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
      "sqlalchemy_pyodbc_sql_connection_str": "mssql+pyodbc://userid:password@uipath-integration1.database.windows.net:1433/AutomationSuite_ProcessMining_Warehouse?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=YES&Encrypt=YES",
      "master_sql_connection_str": "Server=tcp:uipath-integration1.database.windows.net,1433;Initial Catalog=master;Persist Security Info=False;User Id=userid;Password='password';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;"
    },
  "airflow": {
      "metadata_db_connection_str": "postgresql+psycopg2://testadmin:<password>@sfdev8454496-postgresql.postgres.database.azure.com:5432/AutomationSuite_Airflow"
    },
    "sql_connection_str": "Server=tcp:uipath-integration2.database.windows.net,1433;Initial Catalog=AutomationSuite_ProcessMining_Metadata;Persist Security Info=False;User Id=userid;Password='password';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",  
},
```

Sample Process Mining connection string

* Scenario: using custom `app_security_mode`.
```
"processmining": {
    "enabled": true,
    "app_security_mode": "system_managed",
    "warehouse": {
        "sql_connection_str": "Server=tcp:assql2019.autosuitead.local,1433;Initial Catalog=AutomationSuite_ProcessMining_Warehouse;Persist Security Info=False;Integrated Security=true;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
        "sqlalchemy_pyodbc_sql_connection_str": "mssql+pyodbc://:@assql2019.autosuitead.local:1433/AutomationSuite_ProcessMining_Warehouse?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=YES&Encrypt=YES&Trusted_Connection=yes",
        "master_sql_connection_str": "Server=tcp:assql2019.autosuitead.local,1433;Initial Catalog=master;Persist Security Info=False;Integrated Security=true;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;"
      },
   "airflow": {
      "metadata_db_connection_str": "postgresql+psycopg2://testadmin:<password>@sfdev8454496-postgresql.postgres.database.azure.com:5432/AutomationSuite_Airflow"
    },
```

Sample Studio Web connection string

```
"studioweb": {
      "enabled": true,
      "sql_connection_str": "Server=tcp:ci-asaksdev7031068.database.windows.net,1433;Initial Catalog=AutomationSuite_StudioWeb;Persist Security Info=False;User Id=mssqladminun;Password='****';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;"
      },
```

## SQL collation

Automation Suite supports SQL collation set to `SQL_Latin1_General_CP1_CI_AS` at both the server and database level. We strongly recommend this particular setup for optimum performance and stability.

While you have the flexibility to use a collation of your choice, be aware that untested configurations can potentially lead to unexpected issues.

:::important
We do not recommend using Binary SQL or any collations that are case-sensitive, as they cause known issues while installing Automation Suite.
:::

## SQL server ciphers

Only the listed SQL ciphers are supported in Automation Suite:

* `TLS_AES_256_GCM_SHA384`
* `TLS_CHACHA20_POLY1305_SHA256`
* `TLS_AES_128_GCM_SHA256`
* `TLS_AES_128_CCM_SHA256`
* `ECDHE-ECDSA-AES256-GCM-SHA384`
* `ECDHE-RSA-AES256-GCM-SHA384`
* `ECDHE-ECDSA-CHACHA20-POLY1305`
* `ECDHE-RSA-CHACHA20-POLY1305`
* `ECDHE-ECDSA-AES256-CCM`
* `ECDHE-ECDSA-AES128-GCM-SHA256`
* `ECDHE-RSA-AES128-GCM-SHA256`
* `ECDHE-ECDSA-AES128-CCM`
* `ECDHE-ECDSA-AES128-SHA256`
* `ECDHE-RSA-AES128-SHA256`
* `ECDHE-ECDSA-AES256-SHA`
* `ECDHE-RSA-AES256-SHA`
* `ECDHE-ECDSA-AES128-SHA`
* `ECDHE-RSA-AES128-SHA`
* `AES256-GCM-SHA384`
* `AES256-CCM`
* `AES128-GCM-SHA256`
* `AES128-CCM`
* `AES256-SHA256`
* `AES128-SHA256`
* `AES256-SHA`
* `AES128-SHA`
* `DHE-RSA-AES256-GCM-SHA384`
* `DHE-RSA-CHACHA20-POLY1305`
* `DHE-RSA-AES256-CCM`
* `DHE-RSA-AES128-GCM-SHA256`
* `DHE-RSA-AES128-CCM`
* `DHE-RSA-AES256-SHA256`
* `DHE-RSA-AES128-SHA256`
* `DHE-RSA-AES256-SHA`
* `DHE-RSA-AES128-SHA`
* `PSK-AES256-GCM-SHA384`
* `PSK-CHACHA20-POLY1305`
* `PSK-AES256-CCM`
* `PSK-AES128-GCM-SHA256`
* `PSK-AES128-CCM`
* `PSK-AES256-CBC-SHA`
* `PSK-AES128-CBC-SHA256`
* `PSK-AES128-CBC-SHA`
* `DHE-PSK-AES256-GCM-SHA384`
* `DHE-PSK-CHACHA20-POLY1305`
* `DHE-PSK-AES256-CCM`
* `DHE-PSK-AES128-GCM-SHA256`
* `DHE-PSK-AES128-CCM`
* `DHE-PSK-AES256-CBC-SHA`
* `DHE-PSK-AES128-CBC-SHA256`
* `DHE-PSK-AES128-CBC-SHA`
* `ECDHE-PSK-CHACHA20-POLY1305`
* `ECDHE-PSK-AES256-CBC-SHA`
* `ECDHE-PSK-AES128-CBC-SHA256`
* `ECDHE-PSK-AES128-CBC-SHA`
* `RSA-PSK-AES256-GCM-SHA384`
* `RSA-PSK-CHACHA20-POLY1305`
* `RSA-PSK-AES128-GCM-SHA256`
* `RSA-PSK-AES256-CBC-SHA`
* `RSA-PSK-AES128-CBC-SHA256`
* `RSA-PSK-AES128-CBC-SHA`

## SQL requirements for Full-Text Search

Context Grounding and Document Understanding require the SQL Server to have the Full-Text Search component of the SQL Server Database Engine, which is not always installed by default.

If you did not select Full-Text Search when you installed SQL Server, run SQL Server Setup again to add it before configuring Document Understanding.

For more info, check this guide on how to [add/install features on SQL server](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/add-features-to-an-instance-of-sql-server-setup?view=sql-server-2017#to-add-features-to-an-instance-of-). You can also check [here](https://docs.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2017?view=sql-server-2017#deciding-among--components) all the components that can be added to the SQL Server, which includes also Full-Text Search.

## SQL authentication

### Azure Active Directory based access to SQL from AKS

:::note
Insights and Studio Web currently do not support Microsoft Entra ID (formerly Azure Active Directory) authentication configuration for access to SQL.
:::

You may choose to access Microsoft SQL server via Azure Active Directory from AKS cluster. The following example shows some connections strings using the AAD access method:

```
  "sql_connection_string_template": "Server=tcp:sfdev3888449-sql.database.windows.net,1433;Authentication=Active Directory Service Principal;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=5c6b8ff1-efb4-48ca-a530-f744f1d438df;Password='I5V8Q~srSTWf0onUYeHLK..qLO69pP7MZ3KIMaB2';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Max Pool Size=100;",
  "sql_connection_string_template_jdbc": "jdbc:sqlserver://sfdev3888449-sql.database.windows.net;authentication=ActiveDirectoryServicePrincipal;database=DB_NAME_PLACEHOLDER;user=5c6b8ff1-efb4-48ca-a530-f744f1d438df;password={I5V8Q~srSTWf0onUYeHLK..qLO69pP7MZ3KIMaB2};encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;",
  "sql_connection_string_template_odbc": "SERVER=sfdev3888449-sql.database.windows.net;Authentication=ActiveDirectoryServicePrincipal;DATABASE=DB_NAME_PLACEHOLDER;DRIVER={ODBC Driver 17 for SQL Server};UID=5c6b8ff1-efb4-48ca-a530-f744f1d438df;PWD={I5V8Q~srSTWf0onUYeHLK..qLO69pP7MZ3KIMaB2};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;hostNameInCertificate=sfdev3888449-sql.database.windows.net",
  "sql_connection_string_template_sqlalchemy_pyodbc": "mssql+pyodbc://5c6b8ff1-efb4-48ca-a530-f744f1d438df:I5V8Q~srSTWf0onUYeHLK..qLO69pP7MZ3KIMaB2@sfdev3888449-sql.database.windows.net:1433/DB_NAME_PLACEHOLDER?driver=ODBC+Driver+17+for+SQL+Server&authentication=ActiveDirectoryServicePrincipal",
```

### Workload identity-based access to SQL from AKS

For general information on workload identity, see [Workload identity configuration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#workload-identity-configuration).

To set up SQL Server to use workload identity, run the following command:

```
az sql server ad-admin create --display-name test --object-id $userAssignedManagedIdentityObjectId -g $(TARGET_RG) -s $(TARGET_RG)
```

The following sample shows a valid SQL connection string template:

```
"sql_connection_string_template":"Server=tcp:sql_dns_name,1433;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;Authentication=Active Directory Managed Identity;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Max Pool Size=100;"
"sql_connection_string_template_jdbc":"jdbc:sqlserver://sql_dns_name;database=DB_NAME_PLACEHOLDER;authentication=ActiveDirectoryMSI;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;"
"sql_connection_string_template_sqlalchemy_pyodbc"://@sql_dns_name:1433/DB_NAME_PLACEHOLDER?driver=ODBC+Driver+17+for+SQL+Server"
"sql_connection_string_template_odbc": "SERVER=sql_dns_name;DATABASE=DB_NAME_PLACEHOLDER;DRIVER={ODBC Driver 17 for SQL Server};FEDAUTH=ActiveDirectoryDefault;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;hostNameInCertificate=*.database.windows.net"
```

If you enable Apps or Automation Hub, you must override their respective SQL connection strings in the `input.json` file to ensure workload identity support. The following sample shows an example of such SQL connection string overrides:

```
"apps": {
  "sql_connection_str": "Server=tcp:sql_dns_name,1433;Initial Catalog=AutomationSuite_Apps;Authentication=Active Directory Integrated;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
},
"automation_hub": {
  "sql_connection_str": "Server=tcp:sql_dns_name,1433;Initial Catalog=AutomationSuite_Automation_Hub;Authentication=Active Directory Integrated;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
},
```

## SQL requirements for Insights

:::note
Insights does not support Azure AD authentication. If you authenticate using Azure AD, dashboards cannot be loaded and data cannot be fetched from the Microsoft SQL database.
:::

Insights requires SQL Server 2019 or 2022, including support for columnstore index and `.json` functions. SQL Server Enterprise is recommended due to more efficient threading and scalability.

For Azure SQL, ensure the database is S3 service objective or higher.

Make sure the compatibility level for Insights database is set to 130 or higher. In most cases, the default settings meet this requirement. For more info, refer to [View or Change the Compatibility level of a Database - SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/databases/view-or-change-the-compatibility-level-of-a-database?view=sql-server-ver15).

The installation validates both conditions and alerts you if minimum requirements are not met.

## SQL requirements for Data Service

Data Service requires SQL Server version 2016 or higher.

If you create your own database using SQL Server version 2019 or higher, make sure to grant the following Data Service permissions to your users:

```
GRANT ALTER ANY SENSITIVITY CLASSIFICATION TO {userName};
GRANT VIEW ANY SENSITIVITY CLASSIFICATION TO {userName};
```

## SQL requirements for Process Mining

When you enable Process Mining for installation on Automation Suite must bring a PostgreSQL database for `AutomationSuite_Airflow`.

:::important
Starting with Process Mining on Automation Suite 2.2510 only PostgreSQL database is supported for the `AutomationSuite_Airflow` database.
:::

### `AutomationSuite_Airflow` PostgreSQL database

:::note
Before installing or upgrading to Automation Suite 2.2510 or higher, you need to manually create the PostgreSQL database for `AutomationSuite_Airflow`. The PostgreSQL database for Airflow will not be created automatically by the installer.
:::

:::note
When migrating from Microsoft SQL Server to PostgreSQL database data migration is not required. With a correct configuration setup, the database is rebuild when running Sync Airflow.
:::

**Supported PostgreSQL versions**

PostgreSQL versions 12.x to 16.x are supported. It is recommended to use the most recent version of PostgreSQL within this range for optimal compatibility and performance.

**Hardware requirements**

The machine on which the PostgreSQL database for Airflow is installed must meet the following harware requirements.

* **Cores:** 4
* **Memory:** 16 GiB
* **Storage:** 128 GiB
* **IOPS:** &gt;=500 IOPS

**Required permissions**

The PostgreSQL Airflow user (or any dedicated database user) must have

* "All Privileges" permissions for the designated Airflow database.
* "all grants" on the server’s public schema.
* "search_path" set to "public".
  :::note
  You may need to update PostgreSQL Host-Based Authentication file `pg_hba.conf` to add the Airflow user to the database access control list and reload the database configuration to apply the changes.
  :::
The following code shows an example for setting up a PostgreSQL database.

```
CREATE DATABASE airflow_db
  WITH ENCODING 'UTF8'
  LC_COLLATE='en_US.UTF-8'
  LC_CTYPE='en_US.UTF-8'
  TEMPLATE template0;

CREATE USER airflow_user WITH PASSWORD 'airflow_pass';
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;

-- PostgreSQL 15 requires additional privileges:
GRANT ALL ON SCHEMA public TO airflow_user;
```

The following code shows a database encoding validation example.

```
SELECT pg_encoding_to_char(encoding) AS encoding
FROM pg_database
WHERE datname = 'airflow_db';
```

Refer to the official [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/set-up-database.html#setting-up-a-postgresql-database) for more information on how to set up a PostgreSQL database for Airflow.

**Default server port**

The default server port for Airflow database connections with PostgreSQL is `5432`. If you are using the PgBouncer connection pooler, it is common to use port `6432`.

The following code blocks show some example connection strings for PostgreSQL using port `5432`.

Sample connection string:

```
postgresql+psycopg2://testadmin:<password>@test-cu231009v3-postgresql.postgres.database.azure.com:5432/automationsuite_airflow
```

Sample connection string for using Kerberos:

```
postgresql+psycopg2://kerberos_user:@kerberospostgres.AUTOSUITEAD.LOCAL:5432/automationsuite_airflow
```

Sample connection string for using Managed Identitiy:

```
postgresql+psycopg2://testmanagedidentity:@test-postgresql-1.postgres.database.azure.com/airflow-ci-sfasaksqacu8524745
```

The default server port can be configured to use any available port as per your system requirements.

**PgBouncer**

Since Airflow uses short-lived connections, it is highly recommended to set up PgBouncer. PgBouncer is a lightweight connection pooler for PostgreSQL.

Refer to the official [PgBouncer documentation](https://www.pgbouncer.org/config.html) for more information on how to set up PgBouncer.

:::note
When migrating from Microsoft SQL Server to PostgreSQL database data migration is not required. With a correct configuration setup, the database is rebuild when running Sync Airflow.
:::

### `AutomationSuite_ProcessMining_Warehouse` database

Process Mining on Automation Suite requires a separate Microsoft SQL Server for the `AutomationSuite_ProcessMining_Warehouse` for data storage for Process Mining process apps.

:::important
To ensure proper functioning of Process Mining, it is recommended to use Microsoft SQL Server 2022.
:::
This is an overview of hardware requirements and recommendations for setting up a Microsoft SQL Server database machine for `AutomationSuite_ProcessMining_Warehouse`.

To calculate the hardware requirements, you need to have an indication of:

* the number of (million) events in your process.
* the number of case and event fields in your output data.
  :::note
  In a development environment, for performance reasons, it is recommended to work on a small development dataset with a limited number of records.
  :::

You can use the [UiPath Automation Suite Install Sizing Calculator](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/capacity-planning#capacity-planning) to determine the hardware requirements for setting up a dedicated Microsoft SQL Server machine for Process Mining. When you add Process Mining to the **Product section**, the minimum requirements for 1 Dedicated SQL Server are displayed.

Refer to [Hardware requirements](https://docs.uipath.com/process-mining/automation-suite/2.2510/user-guide/hardware-requirements) for more informations.

The SQL user used in the connection strings must have the `db_securityadmin` database-level role both during and post-installation to enable per app security on the Process Mining data warehouse SQL Server. For details, see the official Microsoft documentation on [Database-level roles](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver16).

Refer to [Configuring process app security](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-process-app-security-) for more information.

:::note
It is recommended to enable case sensitivity in table and column names using the following command: `ALTER DATABASE AutomationSuite_ProcessMining_Warehouse COLLATE SQL_Latin1_General_CP1_CS_AS` This prevents errors when loading data caused by columns with similar names, such as **ID** and **id**. It also ensures that textual values differing only in capitalization are treated as distinct. For example:
* `'activity 1' == 'activity 1'`
* `'Activity 1' != 'activity 1'`
This prevents duplication issues in SQL transformations.
:::

## SQL requirements for AI Center

### Requirements for AI Center installed on a FIPS 140-2-enabled machine

To install AI Center on a FIPS 140-2-enabled machine, take the following steps:

1. Before starting the Automation Suite installation, take the following steps:
   1. Enable FIPS 140-2 on the machine on which you plan to install Microsoft Server by following the [Microsoft instructions](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/security/sql-2016-fips-140-2-compliant-mode#windows-system-administration-requirements).
   2. Install Microsoft SQL Server on the FIPS 140-2-enabled machine.
   3. Get the Microsoft SQL Server certificate by running the following command from the SQL Server or any server that can connect to the SQL server with the configured SQL host name:
      ```
      nmap -sV -p <port> -vv --script ssl-cert domain
      ```
2. During the Automation Suite installation, take the following steps:
   1. Append the following values to the AI Center `sql_connection_string_template_jdbc` connection string in the `input.json` file: `encrypt=true;trustServerCertificate=false;fips=true;`.

Example:

      ```
      jdbc:sqlserver://sfdev1804627-c83f074b-sql.database.windows.net:1433;database=DB_NAME_PLACEHOLDER;user=testadmin;password=***;encrypt=true;trustServerCertificate=false;fips=true;Connection Timeout=30;hostNameInCertificate=sfdev1804627-c83f074b-sql.database.windows.net"
      ```

For details on database configuration, see [Advanced installation experience](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/sql-database#bring-your-own-databases) and [Updating the SQL database](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/updating-credentials#updating-the-connection-strings-for-installed-products).
   2. Add the exported cert from step 1.c. to the trust store of the host machine. For details see [Updating the CA Certificates](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/managing-the-certificates#updating-the-ca-certificates).

## SQL requirements for HA

For a high-availability configuration of your SQL Server, select an Always On availability group. For more info, refer to [Overview of Always On availability groups](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver16).

## SQL requirements for Orchestrator

:::important
To increase performance, avoid deadlocks, and prevent dirty reads in SQL, make sure that the `READ_COMMITTED_SNAPSHOT` option is set to `ON`. To process the same queue with multiple robots, and snapshot isolation is turned on, make sure that the `ALLOW_SNAPSHOT_ISOLATION` option is set to `ON`.
:::

Use this query to check if `READ_COMMITTED_SNAPSHOT` and `ALLOW_SNAPSHOT_ISOLATION` are enabled or disabled:

```
SELECT is_read_committed_snapshot_on, snapshot_isolation_state FROM sys.databases
   WHERE name like 'PLACEHOLDER'
```

Make sure to replace PLACEHOLDER with your Orchestrator database name.

If the settings are enabled, the returned value will be `1`.

If the settings are disabled, the returned value will be `0`. Use this query to enable it:

```
# To enable READ_COMMITTED_SNAPSHOT
ALTER DATABASE <PLACEHOLDER>
SET READ_COMMITTED_SNAPSHOT ON

# To enable ALLOW_SNAPSHOT_ISOLATION
ALTER DATABASE <PLACEHOLDER>
SET ALLOW_SNAPSHOT_ISOLATION ON
```

Make sure to replace `<PLACEHOLDER>` with your Orchestrator database name.

If you use different databases for Test Automation and/or Update Server, `READ_COMMITTED_SNAPSHOT` and `ALLOW_SNAPSHOT_ISOLATION` must be enabled on those as well.