---
title: "Configuring NLog"
visible: true
slug: "configuring-nlog"
---

## Adding NLog extensions

Orchestrator loads the following extensions by default, so you do not need to include them in the folder or the NLog configuration:

* `NLog.Targets.ElasticSearch`
* `UiPath.Orchestrator.Logs.Elasticsearch`
* `Microsoft.ApplicationInsights.NLogTarget`
* `NLog.Extensions.AzureEventHub`

Only Linux-compatible extensions can be used in this setup, so make sure that your chosen NLog extension abides by this rule.

To make the extension available for use, it must uploaded to the cluster storage.

The `uipathctl` command line tool can do this via the `uipathctl config orchestrator upload` command:

```
uipathctl config orchestrator upload --nlog-extensions-directory /path/to/extensions/directory
```

If you use an external storage configuration at the cluster level, you must indicate this by including the `--use-external-storage` parameter.

## Advanced NLog configuration

1. Create the `nlog.config.json` file containing the standard sections: extensions, targets and rules.

The extensions section is an array of items that specify the extension assemblies, via `assemblyFile`, and the path of the assembly.

If custom nlog plugins were loaded (as described in the [Adding NLog extensions](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-nlog#adding-nlog-extensions) section), they will be referenced in the `extensions` section.
2. Configure the target and rule in the `nlog.config.json` file.
3. Apply the `nlog.config.json` file using the `uipathctl` command line tool:
   ```
   uipathctl config orchestrator update-config --nlog-config nlog.custom.json
   ```

Example `nlog.config.json` file that writes logs to Azure Blob:

   ```
   {   "NLog": {
           "extensions": [
               { "assemblyFile": "NLog.Extensions.AzureBlobStorage.dll" }
           ],
           "targets": {
               "azureBlob": {
                   "type": "AzureBlobStorage",
                   "connectionString": "DefaultEndpointsProtocol=https;AccountName=test;AccountKey=key;EndpointSuffix=core.windows.net",
                   "container": "orchestratorlogs",
                   "blobName": "${date:format=yyyy-MM-dd hh.mm}",
                   "layout": {
                     "type": "JsonLayout",
                     "includeAllProperties": true,
                     "Attributes": [
                       {"name": "ts","layout": "${longdate}"},
                       {"name": "level","layout": "${level:upperCase=true}"},
                       {"name": "logger","layout": "${logger}"},
                       {"name": "message","layout": "${message}"},
                       {"name": "exception","layout": "${onexception:${ui-pretty-exception}}"}
                     ]
                   }
               }
           },
           "rules": { "70_Final": { "writeTo": "stdout,azureBlob" } }
       }
   }
   ```

Example `nlog.config.json` file that writes robot logs to Splunk:

   ```
   {
       "Nlog": {
           "extensions": [
               { "assemblyFile": "NLog.Targets.Splunk.dll" },
               { "assembly": "UiPath.Orchestrator.Logs.DatabaseBulk.NLogTarget" }
           ],
           "targets": {
               "Splunk": {
                   "type": "BufferingWrapper",
                   "flushTimeout": 5000,
                   "target": {
                       "type": "SplunkHttpEventCollector",
                       "serverUrl": "http://splunk.example.com",
                       "token": "splunk-token",
                       "channel": "",
                       "source": "${logger}",
                       "sourceType": "_json",
                       "index": "uipath",
                       "retriesOnError": "0",
                       "batchSizeBytes": "0",
                       "batchSizeCount": "0",
                       "includeEventProperties": "true",
                       "includePositionalParameters": "true",
                       "includeMdlc": "true",
                       "maxConnectionsPerServer": "10",
                       "ignoreSslErrors": "false",
                       "useProxy": "false",
                       "proxyUrl": "",
                       "proxyUser": "",
                       "proxyPassword": ""
                   }
               }
           },
           "rules": {
               "20_Robot_Primary": { "writeTo": "Splunk,database,insightsRobotLogs" }
           }
       }
   }
   ```