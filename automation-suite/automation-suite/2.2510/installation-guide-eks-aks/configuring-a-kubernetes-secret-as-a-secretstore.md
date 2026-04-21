---
title: "Configuring a Kubernetes Secret as a secretstore"
visible: true
slug: "configuring-a-kubernetes-secret-as-a-secretstore"
---

By default, credentials are defined in `input.json`. To improve security, you can split the data into two parts:

* `input.json` for storing configuration values only.
* Kubernetes Secret to store credentials (serves as the secretstore).
  :::note
  You cannot store certificate paths or certificate-related credentials as part of the secretstore.
  :::

## Prerequisites

If the namespace does not already exist, create it before deploying UiPath products, as follows:

```
kubectl create namespace <uipath-namespace>
```

:::note
The secret must be created in the namespace where `uipath` products have to be deployed.
:::

## Configuring input.json

For `uipathctl` to identify that credentials are stored in a Kubernetes Secret, add the following section to `input.json`:

```
"secret_store": {
  "enabled": true,
  "secret_name": "uipath-credentials" // Secret deployed in uipath ns with all the credentials configured.
}
```

Depending on how you want to manage credentials, your `input.json` can contain either both configuration and credentials, or configuration only and credentials are stored in the secret, as shown in the following diagram:

![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/618822)

* The following example shows a default `input.json` with configuration and credentials:
  ```
  {
    "admin_username": "admin",
    "admin_password": "password",
    "apps": {
      "enabled": true,
      "external_object_storage": {
        "enabled": true,
        "account_key": "secretkey",
        "account_name": "as-storage-account",
        ...
      }
    },
    "external_object_storage": {
      "enabled": true,
      "account_key": "secretkey",
      ...
    },
    "fabric": {
      "redis": {
        "hostname": "redis-cache.mycompany.com",
        "password": "redispassword",
        "port": 6380,
        "tls": true
      }
    },
    "fqdn": "automationsuite.mycompany.com",
    "orchestrator": {
      "enabled": true,
      "sql_connection_str": "Server=tcp:mssql.mycompany.com,1443;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=sqladmin;Password='sqlpassword';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
      "external_object_storage": {
        "enabled": true,    
        "account_key": "secretkey",
        "account_name": "os-storage-account",
        ...
      },
      ...
    },
    "registries": {
      "docker": {
        "url": "registry.uipath.com",
        "username": "username",
        "password": "password"
      },
      "helm": {
        "url": "registry.uipath.com",
        "username": "username",
        "password": "password"
      }
    },
    "snapshot": {
      "enabled": true,
      "external_object_storage": {
        "enabled": true,    
        "client_id": "1fbd7d95-5f8c-4f70-90a6-fdf20310d10e",
        "client_secret": "client-secret",
        ...
      }
    },
    "storage_class": "managed-premium",
    "storage_class_single_replica": "azurefile-csi",
    "sql_connection_string_template": "Server=tcp:mssql.mycompany.com,1443;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=sqladmin;Password='sqlpassword';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
    "sql_connection_string_template_jdbc": "jdbc:sqlserver://mssql.mycompany.com:1443;database=DB_NAME_PLACEHOLDER;user=sqladmin;password={sqlpassword};encrypt=true;trustServerCertificate=true;loginTimeout=30;hostNameInCertificate=mssql.mycompany.com",
    "sql_connection_string_template_odbc": "SERVER=mssql.mycompany.com,1443;DATABASE=DB_NAME_PLACEHOLDER;DRIVER={ODBC Driver 17 for SQL Server};UID=sqladmin;PWD={sqlpassword};Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;hostNameInCertificate=mssql.mycompany.com",
    "sql_connection_string_template_sqlalchemy_pyodbc": "mssql+pyodbc://sqladmin:sqlpassword@mssql.mycompany.com:1443/DB_NAME_PLACEHOLDER?driver=ODBC+Driver+17+for+SQL+Server",
    "postgresql_connection_string_template_sqlalchemy_pyodbc": "postgresql+psycopg2://sa:&lt;password&gt;@135.235.240.165:5432/DB_NAME_PLACEHOLDER"
  }
  ```
* The following examples show the `input.json` with configuration only (`secret_store` configured) and the credentials stored separately in `credentials.json`:
  + `input.json` sample with configuration and `secret_store` configured:
    ```
    {
      "apps": {
        "enabled": true,
        "external_object_storage": {
          "enabled": true,
          ...
        }
      },
      "external_object_storage": {
        "enabled": true,
        ...
      },
      "fabric": {
        "redis": {
          "hostname": "redis-cache.mycompany.com",
          "port": 6380,
          "tls": true
        }
      },
      "fqdn": "automationsuite.mycompany.com",
      "orchestrator": {
        "enabled": true,
        "external_object_storage": {
          "enabled": true,
           ...
        },
        ...
      },
      "registries": {
        "docker": {
          "url": "registry.uipath.com"
        },
        "helm": {
          "url": "registry.uipath.com"
        }
      },
      "secret_store": {
        "enabled": true,
        "secret_name": "uipath-credentials",
        "provider_configs": []
      },
      "snapshot": {
        "enabled": true,
        "external_object_storage": {
          "enabled": true,
          ...
        }
      }
    }
    ```
  + `credentials.json` sample with credentials:
    ```
    {
      "admin_password": "password",
      "admin_username": "admin",
      "apps": {
        "external_object_storage": {

          "account_key": "secretkey"
        }
      },
      "external_object_storage": {
        "account_key": "secretkey"
      },
      "fabric": {
        "redis": {
          "password": "redispassword"
        }
      },
      "orchestrator": {
        "external_object_storage": {
          "account_key": "secretkey"
        },
        "sql_connection_str": "Server=tcp:mssql.mycompany.com,1443;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=sqladmin;Password='sqlpassword';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;"
      },
      "postgresql_connection_string_template_sqlalchemy_pyodbc": "postgresql+psycopg2://sa:&lt;password&gt;@135.235.240.165:5432/DB_NAME_PLACEHOLDER",
        "registries": {
        "docker": {
          "password": "password",
          "username": "username"
        },
        "helm": {
          "password": "password",
          "username": "username"
        }
      },
      "snapshot": {
        "external_object_storage": {
          "client_secret": "client-secret",
          "client_id": "1fbd7d95-5f8c-4f70-90a6-fdf20310d10e"
        }
      },
      "sql_connection_string_template": "Server=tcp:mssql.mycompany.com,1443;Initial Catalog=DB_NAME_PLACEHOLDER;Persist Security Info=False;User Id=sqladmin;Password='sqlpassword';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;",
      "sql_connection_string_template_jdbc": "jdbc:sqlserver://mssql.mycompany.com:1443;database=DB_NAME_PLACEHOLDER;user=sqladmin;password={sqlpassword};encrypt=true;trustServerCertificate=true;loginTimeout=30;hostNameInCertificate=mssql.mycompany.com",
      "sql_connection_string_template_odbc": "SERVER=mssql.mycompany.com,1443;DATABASE=DB_NAME_PLACEHOLDER;DRIVER={ODBC Driver 17 for SQL Server};UID=sqladmin;PWD={sqlpassword};Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;hostNameInCertificate=mssql.mycompany.com",
      "sql_connection_string_template_sqlalchemy_pyodbc": "mssql+pyodbc://sqladmin:sqlpassword@mssql.mycompany.com:1443/DB_NAME_PLACEHOLDER?driver=ODBC+Driver+17+for+SQL+Server"
    }%
    ```

## Storing credentials in a Kubernetes secret

The credentials are stored as part of a Kubernetes Secret, as shown in the following example:

```
apiVersion: v1
kind: Secret
metadata:
  name: uipath-credentials
  namespace: uipath
type: Opaque
data:
  config.json: ewogICJhZG1pbl9wYXNzd29yZCI6ICJwYXNzd29yZCIsCiAgImFkbWluX3VzZXJuYW1lIjogImFkbWluIiwKICAiYXBwcyI6IHsKICAgICJleHRlcm5hbF9vYmplY3Rfc3RvcmFnZSI6IHsKCiAgICAgICJhY2NvdW50X2tleSI6ICJzZWNyZXRrZXkiCiAgICB9CiAgfSwKICAiZXh0ZXJuYWxfb2JqZWN0X3N0b3JhZ2UiOiB7CiAgICAiYWNjb3VudF9rZXkiOiAic2VjcmV0a2V5IgogIH0sCiAgImZhYnJpYyI6IHsKICAgICJyZWRpcyI6IHsKICAgICAgInBhc3N3b3JkIjogInJlZGlzcGFzc3dvcmQiCiAgICB9CiAgfSwKICAib3JjaGVzdHJhdG9yIjogewogICAgImV4dGVybmFsX29iamVjdF9zdG9yYWdlIjogewogICAgICAiYWNjb3VudF9rZXkiOiAic2VjcmV0a2V5IgogICAgfSwKICAgICJzcWxfY29ubmVjdGlvbl9zdHIiOiAiU2VydmVyPXRjcDptc3NxbC5teWNvbXBhbnkuY29tLDE0NDM7SW5pdGlhbCBDYXRhbG9nPURCX05BTUVfUExBQ0VIT0xERVI7UGVyc2lzdCBTZWN1cml0eSBJbmZvPUZhbHNlO1VzZXIgSWQ9c3FsYWRtaW47UGFzc3dvcmQ9J3NxbHBhc3N3b3JkJztNdWx0aXBsZUFjdGl2ZVJlc3VsdFNldHM9RmFsc2U7RW5jcnlwdD1UcnVlO1RydXN0U2VydmVyQ2VydGlmaWNhdGU9VHJ1ZTtDb25uZWN0aW9uIFRpbWVvdXQ9MzA7TWF4IFBvb2wgU2l6ZT0xMDA7IgogIH0sCiAgInBvc3RncmVzcWxfY29ubmVjdGlvbl9zdHJpbmdfdGVtcGxhdGVfc3FsYWxjaGVteV9weW9kYmMiOiAicG9zdGdyZXNxbCtwc3ljb3BnMjovL3NhOiZsdDtwYXNzd29yZCZndDtAMTM1LjIzNS4yNDAuMTY1OjU0MzIvREJfTkFNRV9QTEFDRUhPTERFUiIsCiAgICAicmVnaXN0cmllcyI6IHsKICAgICJkb2NrZXIiOiB7CiAgICAgICJwYXNzd29yZCI6ICJwYXNzd29yZCIsCiAgICAgICJ1c2VybmFtZSI6ICJ1c2VybmFtZSIKICAgIH0sCiAgICAiaGVsbSI6IHsKICAgICAgInBhc3N3b3JkIjogInBhc3N3b3JkIiwKICAgICAgInVzZXJuYW1lIjogInVzZXJuYW1lIgogICAgfQogIH0sCiAgInNuYXBzaG90IjogewogICAgImV4dGVybmFsX29iamVjdF9zdG9yYWdlIjogewogICAgICAiY2xpZW50X3NlY3JldCI6ICJjbGllbnQtc2VjcmV0IiwKICAgICAgImNsaWVudF9pZCI6ICIxZmJkN2Q5NS01ZjhjLTRmNzAtOTBhNi1mZGYyMDMxMGQxMGUiCiAgICB9CiAgfSwKICAic3FsX2Nvbm5lY3Rpb25fc3RyaW5nX3RlbXBsYXRlIjogIlNlcnZlcj10Y3A6bXNzcWwubXljb21wYW55LmNvbSwxNDQzO0luaXRpYWwgQ2F0YWxvZz1EQl9OQU1FX1BMQUNFSE9MREVSO1BlcnNpc3QgU2VjdXJpdHkgSW5mbz1GYWxzZTtVc2VyIElkPXNxbGFkbWluO1Bhc3N3b3JkPSdzcWxwYXNzd29yZCc7TXVsdGlwbGVBY3RpdmVSZXN1bHRTZXRzPUZhbHNlO0VuY3J5cHQ9VHJ1ZTtUcnVzdFNlcnZlckNlcnRpZmljYXRlPVRydWU7Q29ubmVjdGlvbiBUaW1lb3V0PTMwO01heCBQb29sIFNpemU9MTAwOyIsCiAgInNxbF9jb25uZWN0aW9uX3N0cmluZ190ZW1wbGF0ZV9qZGJjIjogImpkYmM6c3Fsc2VydmVyOi8vbXNzcWwubXljb21wYW55LmNvbToxNDQzO2RhdGFiYXNlPURCX05BTUVfUExBQ0VIT0xERVI7dXNlcj1zcWxhZG1pbjtwYXNzd29yZD17c3FscGFzc3dvcmR9O2VuY3J5cHQ9dHJ1ZTt0cnVzdFNlcnZlckNlcnRpZmljYXRlPXRydWU7bG9naW5UaW1lb3V0PTMwO2hvc3ROYW1lSW5DZXJ0aWZpY2F0ZT1tc3NxbC5teWNvbXBhbnkuY29tIiwKICAic3FsX2Nvbm5lY3Rpb25fc3RyaW5nX3RlbXBsYXRlX29kYmMiOiAiU0VSVkVSPW1zc3FsLm15Y29tcGFueS5jb20sMTQ0MztEQVRBQkFTRT1EQl9OQU1FX1BMQUNFSE9MREVSO0RSSVZFUj17T0RCQyBEcml2ZXIgMTcgZm9yIFNRTCBTZXJ2ZXJ9O1VJRD1zcWxhZG1pbjtQV0Q9e3NxbHBhc3N3b3JkfTtFbmNyeXB0PXllcztUcnVzdFNlcnZlckNlcnRpZmljYXRlPXllcztDb25uZWN0aW9uIFRpbWVvdXQ9MzA7aG9zdE5hbWVJbkNlcnRpZmljYXRlPW1zc3FsLm15Y29tcGFueS5jb20iLAogICJzcWxfY29ubmVjdGlvbl9zdHJpbmdfdGVtcGxhdGVfc3FsYWxjaGVteV9weW9kYmMiOiAibXNzcWwrcHlvZGJjOi8vc3FsYWRtaW46c3FscGFzc3dvcmRAbXNzcWwubXljb21wYW55LmNvbToxNDQzL0RCX05BTUVfUExBQ0VIT0xERVI/ZHJpdmVyPU9EQkMrRHJpdmVyKzE3K2ZvcitTUUwrU2VydmVyIgp9
```

## Creating the Kubernetes secret

The Kubernetes Secret can be created using the `credentials.json` file with the following command:

```
kubectl create secret generic <secret-name> \
  --from-file=config.json=<path-to-credentials.json>/credentials.json \
  --namespace=<uipath-namespace>
```