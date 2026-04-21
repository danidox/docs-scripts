---
title: "Test Automation SQL connection string is
            ignored"
visible: true
slug: "test-automation-sql-connection-string-is-ignored"
---

## Description

When you provide an SQL connection string under the `orchestrator.testautomation` section of the cluster configuration file, the `uipathctl` binary ignores the connection string and uses the one under the `orchestrator` section instead. As the following sample shows, the ignored connection string is the value of the `sql_connection_str` parameter:

```
"orchestrator": {
  "testautomation": {
    "enabled": true,
    "sql_connection_str": "Server=tcp:new-sql-server-name,1433;Initial Catalog=new-db;Persist Security Info=False;User Id=test;Password='************';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=True;Connection Timeout=30;Max Pool Size=100;"
  }
}
```

## Solution

To address the issue, take the following steps:

1. Perform a Base64 encoding of the SQL connection string that you provided as the value of the `sql_connection_str` parameter:
   ```
   echo -n "<sql_connection_str under orchestrator.testautomation in cluster config file>" | base64 -d
   ```
2. Run the following command to edit the `orchestrator-secrets` secret:
   ```
   kubectl edit secret orchestrator-secrets -n uipath
   ```
3. In the secret, update the value of the `sqlConnectionStringTA` parameter with the Base64-encoded connection string value.
4. Check if you successfully updated the connection string value:
   ```
   kubectl get secret orchestrator-secrets -n uipath -o jsonpath="{.data.sqlConnectionStringTA}" |  base64 --decode
   ```
5. In the ArgoCD app UI, navigate to **Orchestrator &gt; Details &gt; Parameter &gt; Values &gt; Inside values &gt; Update**.
6. Under the `connectionStrings` section, update the value of the `TestAutomation` parameter with the plain-text value of the connection string, as shown in the following sample:
   ```
   connectionStrings:
     TestAutomation: <Plain-text value of sql_connection_str under orchestrator.testautomation in cluster config file>
   ```