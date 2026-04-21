---
title: "Forwarding logs to external tools"
visible: true
slug: "forwarding-logs-to-external-tools"
---

You can forward logs to external tools, such as Splunk, using the OpenTelemetry Collector. For details on how to install and use the OpenTelemetry Collector, refer to the official documentation of the tool provider (such as Splunk [official documentation](https://docs.splunk.com/observability/en/gdi/opentelemetry/collector-kubernetes/install-k8s.html)).

:::note
This method refers to forwading logs from infrastructure and application pods. For saving robot logs, please refer to [Saving robot logs to Elasticsearch](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/saving-robot-logs-to-elasticsearch#saving-robot-logs-to-elasticsearch).
:::

By default, Automation Suite includes a [logging operator.](https://kube-logging.dev/) To use a custom logging operator, refer to the [Bring your own components](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/configuring-inputjson#bring-your-own-components) section for instructions on how to opt out of the default setup.

In its default configuration, Automation Suite forwards pod logs to the object storage bucket used by the platform components.