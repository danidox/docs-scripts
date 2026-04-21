---
title: "Using the monitoring stack"
visible: true
slug: "using-the-monitoring-stack"
---

The monitoring stack for Automation Suite clusters includes Prometheus, Grafana, and Alertmanager, which are automatically installed unless you choose to bring your own monitoring stack.

This page describes a series of monitoring scenarios optimized to work with the monitoring tool, which is bundled with the Automation Suite cluster. If you choose to bring your own monitoring stack, make sure to follow the official documentation of your tools to monitor the health of the cluster.

:::important
When using collectors to export metrics to third-party tools, enabling application monitoring may disrupt the functionality of Automation Suite.
:::

## Accessing the monitoring tools

### Overview

The monitoring stack for Automation Suite clusters includes Prometheus, Grafana, and Alert Manager.

You can access the Automation Suite monitoring tools individually using the following URLs:

Expand Table

| **Application** | **Tool** | **URL** | **Example** |
| --- | --- | --- | --- |
| Metrics | Prometheus | `https://monitoring.fqdn/metrics` | `https://monitoring.automationsuite.mycompany.com/metrics` |
| Dashboard | Grafana | `https://monitoring.fqdn/grafana` | `https://monitoring.automationsuite.mycompany.com/grafana` |
| Alert Management | Alert Manager | `https://monitoring.fqdn/alertmanager` | `https://monitoring.automationsuite.mycompany.com/alertmanager` |

### Monitoring tool authentication

To access the monitoring tools for the first time, follow the instructions in [Accessing Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/accessing-automation-suite#accessing-monitoring).

## Checking currently firing alerts

To view the alerts, navigate to Prometheus using `https://monitoring.fqdn/metrics` and select the **Alerts** tab. Here you can see all the alerts configured in Automation Suite.

* To view the active alerts, filter the alert status by using the **Firing** checkbox.
* For more details about certain alerts, expand the alerts you want to view.
  ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/556773)

## Silencing alerts

If alerts are too noisy, you can silence them. To do that, take the following steps:

1. Access Alert Manager using `https://monitoring.fqdn/alertmanager`.
2. Find the alert in question, and select **Silence**.
3. Fill in the **Creator** and **Comment** details, and select **Create**. The alert should no longer show on the **Monitoring Dashboard** or be reported to any of the configured receivers.

## Configuring the alerts

:::note
Before starting configuring the alerts, make sure to [enable kubectl](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/accessing-automation-suite#enabling-kubectl).
:::

### Adding a new email configuration

To add a new email configuration after an installation, run the following command:

```
./uipathctl config alerts add-email \
  --name test \
  --to "admin@example.com" \
  --from "admin@example.com" \
  --smtp server.mycompany.com \
  --username admin \
  --password somesecret \
  --require-tls \
  --ca-file <path_to_ca_file> \
  --cert-file <path_to_cert_file> \
  --key-file <path_to_key_file> \
  --send-resolved \
  --ASEA
```

| Flag | Description | Example |
| --- | --- | --- |
| `name` | The name of the email configuration | `testconfig` |
| `to` | The email address of the receiver | `admin@example.com` |
| `from` | The email address of the sender | `admin@example.com` |
| `SMTP` | SMTP server URL or IP address and port number | `server.mycompany.com:567` |
| `username` | Authentication username | `admin` |
| `password` | Authentication password | `securepassword` |
| `require-tls` | Boolean flag to denote that TLS is enabled at the SMTP server. | N/A |
| `ca-file` | File path containing the CA Certificate of the SMTP server. This is optional if the CA is private. | `./ca-file.crt` |
| `cert-file` | File path containing the certificate of the SMTP server. This is optional if the certificate is private. | `./cert-file.crt` |
| `key-file` | File path containing the private key of the certificate of the SMTP server. This is required if the certificate is private. | `./key-file.crt` |
| `send-resolved` | Boolean flag to send an email once the alert is resolved. | N/A |
| `ASEA` | Boolean flag to indicate that you installed Automation Suite on EKS or AKS. | N/A |

### Removing an email configuration

To remove an email configuration, you must run the following command. Make sure to pass the name of the email configuration you want to remove.

```
./uipathctl config alerts remove-email --name test --ASEA
```

### Updating an email configuration

To update an email configuration, you must run the following command. Make sure to pass the name of the email configuration you want to update and the additional optional parameters you want to edit. These parameters are the same as the ones for adding a new email configuration. You can pass one or more flags at the same time.

```
./uipathctl config alerts update-email --name test --ASEA [additional_flags]
```

## Accessing Grafana dashboard

To access Grafana dashboards, you must retrieve your credentials and use them to log in:

* Username:
  ```
  kubectl -n monitoring get secrets/grafana-creds -o "jsonpath={.data.admin-user}" | base64 -d; echo
  ```
* Password:
  ```
  kubectl -n monitoring get secrets/grafana-creds -o "jsonpath={.data.admin-password}" | base64 -d; echo
  ```

## Monitoring Persistent Volumes

You can monitor persistent volumes via the **Kubernetes / Persistent Volumes** dashboard. You can keep track of the free and used space for each volume.

![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/206631)

You can also check the status of each volume by selecting the **PersistentVolumes** item within the **Storage** menu of the **Cluster Explorer**.

## Monitoring hardware utilization

To check the hardware utilization per node, you can use the **Node/exporter/nodes** dashboard. Data on the CPU, Memory, Disk, and Network is available.

You can monitor the hardware utilization for specific workloads using the **Kubernetes / Compute Resources / Namespace (Workloads)** dashboard. Select the **uipath** namespace to get the needed data.

## Creating shareable visual snapshot of a Grafana chart

1. Select the menu button next to the chart title, and then select **Share**.
2. Select the **Snapshot** tab, and set the **Snapshot name**, and **Expire**.
3. Select **Publish** to [snapshot.raintank.io.](http://snapshot.raintank.io/)

For more details, see the Grafana documentation on [sharing dashboards](https://grafana.com/docs/grafana/latest/sharing/share-dashboard/#publish-a-snapshot).

:::note
This snapshot is viewable on the public Internet by anyone with the link.
:::

## Creating custom persistent Grafana dashboards

For details on how to create custom persisten Grafana dashboards, see [Grafana documentation](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/create-dashboard/).

## Available metrics

You can search for available metrics in the Prometheus UI.

Documentation on the available metrics is here:

* [https://github.com/prometheus/node_exporter#enabled-by-default - Connect to preview](https://github.com/prometheus/node_exporter#enabled-by-default)
* [https://github.com/kubernetes/kube-state-metrics/tree/master/docs#exposed-metrics - Connect to preview](https://github.com/kubernetes/kube-state-metrics/tree/master/docs#exposed-metrics)
* [Querying Metrics from Prometheus](https://istio.io/latest/docs/tasks/observability/metrics/querying-metrics/) (Istio)