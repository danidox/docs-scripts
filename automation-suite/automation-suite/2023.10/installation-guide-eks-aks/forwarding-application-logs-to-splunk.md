---
title: "How to forward application logs to Splunk"
visible: true
slug: "forwarding-application-logs-to-splunk"
---

:::note
* This section applies only to Automation Suite versions 2023.10.6 and earlier. For newer Automation Suite versions, refer to
[Forwarding application logs to external tools.](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/forwarding-application-logs-to-external-tools)
* This section covers exporting POD logs. For exporting robot logs, see [Orchestrator - About Logs](https://docs.uipath.com/orchestrator/automation-suite/2023.10/user-guide/about-logs).
* Splunk is an external tool, and UiPath® does not have an opinion on how you should configure your Splunk setting. For more
details about HTTP Event Collector, see [Splunk official documentation](https://docs.splunk.com/Documentation).
:::

The Splunk-Fluentd stack is a centralized logging solution that allows you to search, analyze, and visualize log data. Fluentd collects and sends the logs to Splunk. Splunk retrieves the logs and lets you visualize and analyze the data.

## Creating a secret with a token

Create a Kubernetes secret with the HTTP Event Collector (HEC) token generated in the Splunk UI. This token is used for the authentication between Automation Suite and Splunk.

```
kubectl -n logging create secret generic splunk-hec-token --from-literal=splunk_hec_token=<splunk_hec_token>
```

## ClusterOutput to Splunk

A `ClusterOutput` defines where your logs are sent to and describes the configuration and authentication details.

To configure the [ClusterOutput](https://rancher.com/docs/rancher/v2.5/en/logging/custom-resource-config/outputs/#clusteroutputs-2-5-8) for Splunk, run the following command:

```
kubectl -n logging apply -f - <<"EOF"
apiVersion: logging.banzaicloud.io/v1beta1
kind: ClusterOutput
metadata:
  name: splunk-output
spec:
  splunkHec:
    buffer:
      tags: '[]'
      timekey: <splunk_hec_timekey>
      timekey_use_utc: true
      timekey_wait: 10s
      type: file
    hec_host: <splunk_hec_host>
    hec_port: <splunk_hec_port>
    hec_token:
      valueFrom:
        secretKeyRef:
          key: splunk_hec_token
          name: splunk-hec-token
    index: <splunk_hec_index>
    insecure_ssl: true
    protocol: <splunk_hec_protocol>
    source: <splunk_hec_source>
    sourcetype: <splunk_hec_source_type>
EOF
```

:::note
Replace the attributes between angle brackets `&lt; &gt;` with the corresponding values used in your Splunk configuration. For details, see the following table:
:::

| Attribute | Description |
| --- | --- |
| `splunk_hec_host` | The network host of your Splunk instance. This is usually the IP address or FQDN of Splunk. |
| `splunk_hec_port` | The Splunk port for client communication. This port usually differs from the port on which you launch the Splunk dashboard. The conventional HEC port for Splunk is `8088`. |
| `secret_key` | The secret key of the Splunk token. This is the name of the key in the secret you created in the previous step, which holds Splunk HEC token.  The presented manifest already contains the key: `splunk_hec_token`. If you have not altered the command to create a secret, you do not need to change this value. |
| `splunk_hec_timekey` value in `splunkHec.buffer` | The output frequency, or how often you want to push logs. We recommend using a 30-seconds (`30s`) interval. |
| `protocol` | The URL protocol. Valid values are `http` and `https`. You must use HTTPS protocol if you have SSL communication enabled on Splunk. |
| `splunk_hec_index` | The identifier for the Splunk index. Used to index events. |
| `splunk_hec_source` | The source field for events. |
| `splunk_hec_source_type` | The source type field for events. |

:::note
To filter logs in Splunk by environment type (dev, test, etc.), use the `source` attribute.
:::

The following example is based on the configuration presented on this page.

![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/333523)

## ClusterFlow in Fluentd

Use the `ClusterFlow` to define:

* the logs you want to collect and filter;
* the `ClusterOutput` to send the logs to.

To configure [ClusterFlow](https://rancher.com/docs/rancher/v2.5/en/logging/custom-resource-config/flows/) in Fluentd, run the following command:

```
kubectl -n logging apply -f - <<"EOF"
apiVersion: logging.banzaicloud.io/v1beta1
kind: ClusterFlow
metadata:
  name: splunk-flow
  namespace: logging
spec:
  filters:
  - tag_normaliser:
      format: ${namespace_name}/${pod_name}.${container_name}
  globalOutputRefs:
  - splunk-output
  match:
  - select:
      container_names:
      - istio-proxy
      namespaces:
      - istio-system
  - exclude:
      container_names:
      - istio-proxy
      - istio-init
      - aicenter-hit-count-update
      - istio-configure-executor
      - on-prem-tenant-license-update
      - curl
      - recovery
      - aicenter-oob-scheduler
      - cert-trustor
  - exclude:
      namespaces:
      - default
  - exclude:
      labels:
        app: csi-snapshotter
  - exclude:
      labels:
        app: csi-resizer
  - select: {}
EOF
```

## Searching in Splunk

1. Select **Search & Reporting**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/206338)
2. Search based on **Source**, **Index**, and **SourceType**.
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/206423)
   ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/206899)

## Troubleshooting

If, for some reason, the application logs are not pushed to Splunk, take the following steps:

1. Change the Fluentd log level to debug.
2. Query the Fluentd pod:
   ```
   kubectl patch logging -n logging  logging-operator-logging  --type=json -p '[{"op":"add","path":"/spec/fluentd/logLevel","value":debug}]'
   kubectl -n logging exec -it sts/logging-operator-logging-fluentd cat /fluentd/log/out
   ```
   :::note
   The Fluentd logs should indicate the cause of data not being pushed to Splunk.
   :::
3. After fixing the issue, restore the Fluentd log level:
   ```
   kubectl patch logging -n logging  logging-operator-logging  --type=json -p '[{"op":"remove","path":"/spec/fluentd/logLevel","value":debug}]'
   ```