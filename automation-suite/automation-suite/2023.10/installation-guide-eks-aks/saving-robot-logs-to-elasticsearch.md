---
title: "Saving robot logs to Elasticsearch"
visible: true
slug: "saving-robot-logs-to-elasticsearch"
---

Saving robot logs to an Elasticsearch server can be achieved through two types of configuration: basic and advanced.

The basic configuration provides default functionality that activates the preconfigured Elasticsearch NLog target, which is made up of an Elasticsearch target wrapped in a Buffering target. This type of configuration is enough in most scenarios.

However, if you need to further customize the rules, you can use the advanced configuration method.

:::note
The option to save robot logs to an Elasticsearch server only becomes effective once you configure it, and is not applied retroactively. This means that you will no longer have access to any logs that were already in the database at the time you configured the option, because logs can only be retrieved and displayed from a single destination.
:::

## Basic robot log Elasticsearch configuration

To apply the basic configuration, take the following steps. For more details, see [Configuring the Orchestrator parameters](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-orchestrator-parameters#configuring-orchestrator-parameters).

1. In the configuration file, add a new section called `orchestrator_robot_logs_elastic` to the Orchestrator configuration, as shown in the following example:
   ```
   "orchestrator": {
       "enabled": true,
       "orchestrator_robot_logs_elastic": {
           "elastic_uri": "https://elastic.example.com:9200",
           "elastic_auth_username": "elastic-user",
           "elastic_auth_password": "elastic-password"
       }
   }
   ```
2. Update the following parameters with your own values:

   | Parameter | Description |
   | --- | --- |
   | `elastic_uri` | The address of the Elasticsearch instance that must be used. You must provide the address as a URI, along with a username and password.  Example: `https://elastic.example.com:9200`  Make sure you do not include a trailing slash. |
   | `elastic_auth_username` | Example: `elastic-user` |
   | `elastic_auth_password` | Example: `elastic-password` |

The basic configuration supports Elasticsearch version 7.x. For Elasticsearch 8.x, you need to use the advanced configuration.

## Advanced robot log Elasticsearch configuration

:::important
Any changes you make per the next steps can negatively affect the functionality and stability of the entire system. It is advisable to only make changes if you understand their consequences.
:::

The advanced configuration allows you to fully customize your `NLog.config` target.

1. Follow the [basic configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/saving-robot-logs-to-elasticsearch#saving-robot-logs-to-elasticsearch) steps described previously.
2. Follow the [Advanced NLog configuration](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-nlog#configuring-nlog) steps, then update the `robotElasticBuffer` target with the properties that need to be changed.
   :::note
   The advanced configuration also supports Elasticsearch version 8.x.
   :::

Sample `nlog.config.json` for Elasticsearch 7.x

```
{
  "Nlog": {
    "targets": {
      "robotElasticBuffer": {
        "flushTimeout": 1000,
        "bufferSize": 1000,
        "slidingTimeout": false,
        "target": {
          "uri": "https://elastic.example.com:9200",
          "requireAuth": true,
          "username": "elastic-user",
          "password": "elastic-password",
          "index": "${event-properties:item=indexName}-${date:format=yyyy.MM}",
          "documentType": "logEvent",
          "includeAllProperties": true,
          "layout": "${message}",
          "excludedProperties": "agentSessionId,tenantId,indexName"
        }
      }
    }
  }
}
```

Sample `nlog.config.json` for Elasticsearch 8.x

```
{
  "Nlog": {
    "targets": {
      "robotElasticBuffer": {
        "flushTimeout": 1000,
        "bufferSize": 1000,
        "slidingTimeout": false,
        "target": {
          "uri": "https://elastic.example.com:9200",
          "requireAuth": true,
          "username": "elastic-user",
          "password": "elastic-password",
          "index": "${event-properties:item=indexName}-${date:format=yyyy.MM}",
          "documentType": "",
          "includeAllProperties": true,
          "layout": "${message}",
          "excludedProperties": "agentSessionId,tenantId,indexName"
        }
      }
    }
  }
}
```