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

* Robot execution duration per month by robot type.
* Robot concurrency - the maximum number of robots that executed at the same time.
* Metrics on jobs run, processes run, queue items, job failure rate, and users.
* Environment information.

You can upload the XML file in the [Customer Portal](https://customerportal.uipath.com/) to share your high-level self-hosted usage telemetry with the UiPath Support team.

You can opt out of generating this summarized telemetry by listing `service-metrics` in the excluded list in Automation Suite 2023.10 and higher.

## Generating the support bundle

To generate the support bundle, run the following command:

```
./uipathctl health bundle input.json --versions version.json
```

This tool takes some time to gather and store all the logs in a temporary location on your local / management machine.

The following table lists the optional flags the support bundle tool support:

|  |  |
| --- | --- |
| **Flags** | **Description** |
| `--output-dir /foo/bar` | Provide a directory path to store the support bundle. |
| `--skip-diagnose` | Boolean flag to skip the diagnostics report.  By default, the bundle contains the diagnostics reports. Use this flag to exclude the diagnostics report from the support bundle. |
| `--include-previous` | The default value is `true`.  If set to `false`, the support bundle skips the logs of the previous instance of the container in a pod. |
| `--exclude string` | Specify additional components (comma separated) to include in the bundle (such as `--exclude=service-metrics`). |
| `--limit-bytes int` | Limits the size of the logs by providing the integer value in bytes. |
| `--since-time` | Only return logs after a specific date. Defaults to all logs. |
| `--namespace` | When provided, retrieves the support bundle only from the specified namespace. |