---
title: "Setting up Kerberos authentication with basic MSSQL authentication for Process Mining"
visible: true
slug: "setting-up-kerberos-authentication-with-basic-mssql--authentication-for-process-mining"
---

:::note
When you are performing a new installation and you want to use Kerberos authentication, it is strongly recommended to configure process app security as `single_account`. Refer to [Configuring process app security](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-process-app-security-) for details.
:::

When you want to use Kerberos authentication for login to Automation Suite and use basic MSSQL authentication for Process Mining you need to add the following in the `processmining` section in the `input.json` file.

```
"kerberos_auth_config": {
      "enabled": false
    },
```

## Example Kerberos authentication with basic MSSQL and PostgreSQL authentication for Process Mining

The following code shows an example `processmining` section with Kerberos authentication with basic MSSQL and PostgreSQL authentication for Process Mining.

```
"processmining": {
    "enabled": true,
    "advanced_configuration": {},
    "airflow": {
      "metadata_db_connection_str": "postgresql+psycopg2://kerberos_user:@kerberospostgres.AUTOSUITEAD.LOCAL:5432/AutomationSuite_Airflow"
    }
  }
```