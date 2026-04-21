---
title: "Automation Suite overview"
visible: true
slug: "migrating-from-in-cluster-to-external-redis"
---

This page outlines the capabilities and product offerings you can enjoy if you install Automation Suite, and helps you get an idea about the architecture you are about to build.

## Overview

Automation Suite enables you to deploy the full UiPath® automation platform in a Linux environment ranging from bare metal machines to on-premises Virtual Machine infrastructure, or cloud subscriptions to any of the major providers.

Managing multiple server product deployments independently usually requires configuring integrations with enterprise systems for authenticating and managing users, as well as managing and monitoring each deployment from an availability and scale perspective.

Automation Suite contains everything in one package that you can deploy in multi-node HA-ready production mode with automatic scaling and built-in HA, and monitor, configure, and upgrade as a whole. All the functionality available in Automation Cloud is adapted to make it easier for you to manage everything yourself with low total cost of ownership.

What Automation Suite includes:

* **All Server Products** (except for any new products shipping in Automation Cloud first).
* **All Shared Suite Capabilities** that enable you to easily configure the integration with existing enterprise systems, such as AD, AAD, or SAML, across all products. A common experience is offered across the suite for the user, tenant, external applications, and license management.
* **Common end user portal**.
* **Kubernetes-based infrastructure, cluster management, and monitoring tools**, all preconfigured, dedicated to and optimized for UiPath®. This enables running all the products at scale and with HA. This means you do not have to design, configure, and validate which Kubernetes versions and components for routing, storage, etc., work well with the UiPath® services.

Everything needed is included and optimized, **all supported by UiPath®.**

You just need to bring the machines, load balancer, and SQL. For the specific requirements for the machines as well as installation options and instructions, see and the remaining of this section.

For a leaner stack, reduced complexity, and more streamlined operations, Automation Suite is available for containerized platforms such as AKS, a managed Kubernetes service offered by Azure, or EKS provided by Amazon AWS. For more details, refer to [Automation Suite on EKS/AKS Installation Guide](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/automation-suite-overview).

For an in-depth perspective on each deployment model, see [Cross-deployment model feature comparison](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/cross-deployment-model-feature-comparison#cross-deployment-model-feature-comparison).

## Key benefits
  ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/287406/209162)

### Deployment Scenarios

* Online single-node evaluation
* Online multi-node HA-ready production
* Offline single-node evaluation
* Offline multi-node HA-ready production

### High Availability

We are enabling high availability (HA) by default for multi-node HA-ready production mode as part of the offering. This is enabled as part of the `cluster_config.json` configuration at installation time. We also support the ability to add more nodes to either single-node evaluation or multi-node HA-ready production configurations to scale out. However, we do not support going from non-HA to HA mode.

:::note
Insights does not support HA.
:::

### Upgrade

The upgrade process covers both the infrastructure and the entire UiPath® automation platform.

### Cluster management

We are using Rancher as the UI layer for managing our cluster. The UI provides a cluster explorer to manage the deployment.

### Monitoring

The platform exposes Grafana, Prometheus, and Alertmanager by default for troubleshooting and monitoring. See how to monitor the cluster, set alerts, create and view dashboards to track the deployment [here](https://rancher.com/docs/rancher/v2.6/en/monitoring-alerting/).

For more details, see [Monitoring Stack for UiPath Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/monitoring-automation-suite#using-the-monitoring-stack).

### Support Bundle

Support Bundle tool collects logs from the in-cluster object/blob store, logs from currently running pods (of last four hours), different events, and Kubernetes object definitions.

For more details on how to use the tool, see [Support Bundle](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/using-support-bundle-tool#using-the-automation-suite-support-bundle).

### Backup and restore

The suite supports backup and recovery for the entire cluster except for external data sources, such as SQL Server.

Cluster backup is enabled by default every 15 minutes.

For more details, see [Backing up and restoring the cluster](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/backing-up-and-restoring-the-cluster#backing-up-and-restoring-the-cluster).

### SQL authentication methods

The suite supports both SQL authentication and [Kerberos authentication](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/setting-up-kerberos-authentication#setting-up-kerberos-authentication) for all SQL database connections.

## Product offering

Learn more about [Automation Suite products](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/automation-suite-products#automation-suite-products).

## Evaluation guide

### Requirements and installation

| Details | Instructions |
| --- | --- |
| Requirements and installation instructions for Automation Suite. | [Requirements and installation instructions](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/hardware-and-software-requirements#hardware-and-software-requirements) |

### Platform evaluation

| Details | Instructions |
| --- | --- |
| Complete an initial platform configuration. | [Automation Suite Configuration checklist](https://docs.uipath.com/automation-suite/automation-suite/2023.10/admin-guide/configuration-checklist) |
| Connect your first robot | [Connecting Attended Robots](https://docs.uipath.com/automation-suite/automation-suite/2023.10/admin-guide/connecting-your-first-robot) |
| Monitor the stack, troubleshoot issues, create alerts, and view dashboards from a centralized location. | [Using the Diagnostics Tool](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/running-the-diagnostics-tool#running-the-diagnostics-tool)  [Using the Support Bundle tool](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/using-support-bundle-tool#using-the-automation-suite-support-bundle)  [Monitoring Automation Suite](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/monitoring-automation-suite#monitoring-automation-suite)  [Alerts](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/alerts#alerts) |

### Product evaluation

The following instructions take you to the corresponding product guides.

| Product | Evaluation checklist |
| --- | --- |
| Orchestrator | [Orchestrator configuration checklist](https://docs.uipath.com/orchestrator/automation-suite/2023.10/user-guide/orchestrator-configuration-checklist) |
| Automation Suite Robots | [Automation Suite Robots configuration checklist](https://docs.uipath.com/orchestrator/automation-suite/2023.10/user-guide/prerequisites) |
| Automation Hub | [Automation Hub configuration checklist](https://docs.uipath.com/automation-hub/automation-suite/2023.10/user-guide/automation-hub-configuration-checklist) |
| Automation Ops | [Automation Ops configuration checklist](https://docs.uipath.com/automation-ops/automation-suite/2023.10/user-guide/automation-ops-configuration-checklist) |
| Test Manager | [Test Manager configuration checklist](https://docs.uipath.com/test-suite/automation-suite/2023.10/user-guide/test-manager-user-actions) |
| AI Center | [AI Center configuration checklist](https://docs.uipath.com/ai-center/automation-suite/2023.10/user-guide/ai-center-configuration-checklist) |
| Action Center | [Action Center configuration checklist](https://docs.uipath.com/action-center/automation-suite/2023.10/user-guide/action-center-configuration-checklist) |
| Task Mining | [Task Mining configuration checklist](https://docs.uipath.com/task-mining/automation-suite/2023.10/user-guide/task-mining-configuration-checklist) |
| Apps | [Apps configuration checklist](https://docs.uipath.com/apps/automation-suite/2023.10/user-guide/apps-configuration-checklist) |
| Insights | [Insights configuration checklist](https://docs.uipath.com/insights/automation-suite/2023.10/user-guide/insights-configuration-checklist) |
| Data Service | [Data Service configuration checklist](https://docs.uipath.com/data-service/automation-suite/2023.10/user-guide/data-service-configuration-checklist) |
| Process Mining | [Process Mining configuration checklist](https://docs.uipath.com/process-mining/automation-suite/2023.10/user-guide/process-mining-configuration-checklist) |
| Document Understanding | [Document Understanding configuration checklist](https://docs.uipath.com/document-understanding/automation-suite/2023.10/user-guide/document-understanding-deployed-in-automation-suite-first-run-experience) |