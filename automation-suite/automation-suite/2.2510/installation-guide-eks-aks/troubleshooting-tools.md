---
title: "Troubleshooting tools"
visible: true
slug: "troubleshooting-tools"
---

Automation Suite bundles two troubleshooting tools that can assist technicians and cluster administrators in diagnosing and addressing problems across various components.

## Diagnostics tool

The Automation Suite diagnostics tool is a self-help tool that runs a set of checks and provides a synopsis of what is wrong and the potential root cause.

We recommend that you use this tool as the first step if you face any issue.

## Support bundle

The Automation Suite support bundle tool collects application-level logs of UiPath® services and other software components, such as Istio, ArgoCD, etc. The Automation Suite support bundle tool also contains historical records you can use to analyze patterns when troubleshooting a problem. Detailed logs are particularly helpful when the potential root cause of an issue is not evident just by looking at the state of the cluster.

The Automation Suite support bundle tool is also needed when asking for guidance or a fix from the UiPath® Support team as they need it for analysis purposes.

:::note
The Automation Suite support bundle tool does not collect or store any PII or confidential data of you, your user, or your automation. UiPath® applications do not leak or log any confidential information in their records. At the platform level, the log collector is designed to mask any such critical information.
:::