---
title: "Running the support bundle tool"
visible: true
slug: "running-the-support-bundle-tool"
---

The Automation Suite support bundle tool collects application-level logs of UiPath® services and other software components, such as Istio, ArgoCD, etc. The Automation Suite support bundle tool also contains historical records you can use to analyze patterns when troubleshooting a problem. Detailed logs are particularly helpful when the potential root cause of an issue is not evident just by looking at the state of the cluster.

The Automation Suite support bundle tool is also needed when asking for guidance or a fix from the UiPath® Support team as they need it for analysis purposes.

:::note
The Automation Suite support bundle tool does not collect or store any PII or confidential data of you, your user, or your automation. UiPath® applications not not leak or log any confidential information in their records. At the platform level, the log collector is designed to mask any such critical information.
:::

High-level summarized usage telemetry is also exported with this tool generating an XML file. This telemetry includes:

* Automation Suite installation configuration details (such as Kubernetes flavor, installation mode, version, and enabled services, among other settings).
* Cluster-level resource usage information (such as CPU and memory availability and utilization, among other metrics).
* UiPathctl command execution details (such as status, logs, and duration, among other details).
* Usage telemetry:
  + Robot execution duration per month by robot type.
  + Robot concurrency - the maximum number of robots that executed at the same time.
  + Metrics on jobs run, processes run, queue items, job failure rate, and users.
  + Environment information.
  + AI Units usage summary if you use AI Center.

UiPath uses this data only for internal reporting to strengthen customer understanding and improve the quality of support and overall experience.

You can upload the XML file in the [Customer Portal](https://customerportal.uipath.com/) to share your high-level self-hosted usage telemetry with the UiPath Support team.

You can opt out of generating this summarized telemetry by listing `service-metrics` in the excluded list in Automation Suite 2.2510 and higher.

## Generating the support bundle

To generate the support bundle, run the following command:

```
./uipathctl health bundle input.json --versions versions.json
```

Starting with Automation Suite 2.2510.1, the paths to the configuration file (`input.json`) and the versions file `(helm-charts.json`) parameters are optional. You can generate the the support bundle simply by running:

```
./uipathctl health bundle
```

This tool takes some time to gather and store all the logs in a temporary location on your local / management machine.

The following table lists the optional flags the support bundle tool support:

| Flags | Description |
| --- | --- |
| `--output-dir string` | Specify the directory to store the support bundle. |
| `--namespace string` | Specify the namespace where UiPath Automation Suite is deployed. |
| `--include string` | Specify additional components (comma separated) to include in the bundle (such as `--include=historical-logs`). |
| `--exclude string` | Specify components (comma separated) to exclude from the bundle (such as `service-metrics`). |
| `--limit-bytes int` | Limits the size of the logs of running pods by providing the integer value in bytes. |

## Automation Suite Support Bundle Structure

The `.tar.gz` archive contains following files and folders:

| File/folder | Description |
| --- | --- |
| `current-logs` | Contains the live logs (such as logs for current and previous instance of pods). |
| `events.json` | Contains the event descriptions from all the namespaces. |
| `alerts` | Contains the active prometheus alerts in the cluster. |
| `namespace/resource/object.yaml` | Contains the object descriptions for the server-preferred/custom namespace and cluster-scoped resources. |
| `service-metrics` | Contains high level configuration and usage telemetry stored in individual XML files. |

:::note
Historical logs are not supported in EKS/AKS environments.
:::