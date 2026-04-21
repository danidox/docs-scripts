---
title: "Automation Suite overview"
visible: true
slug: "automation-suite-overview"
---

Automation Suite enables you to deploy the complete UiPath® automation platform on containerized platforms such as AKS, a managed Kubernetes service offered by Azure, or EKS provided by Amazon AWS.

While these platforms offer robust options, Automation Suite is compatible with other environments as well:

* If you are interested in deploying Automation Suite in an OpenShift environment, see [Automation Suite on OpenShift Installation Guide.](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-openshift/automation-suite-overview)
* If you are looking for our classic deployment experience in a Linux environment, see [Automation Suite on Linux Installation Guide](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide/automation-suite-overview).

For an in-depth perspective on each deployment model, see [Cross-deployment model feature comparison](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/cross-deployment-model-feature-comparison#cross-deployment-model-feature-comparison).

Automation Suite includes:

* **The UiPath® server products**, with the exception of any new products shipping in Automation Cloud first.
* **All shared suite capabilities** that enable you to easily configure the integration with existing enterprise systems, such as AD, AAD, or SAML, across all products; a common experience is offered across the suite for the user, tenant, external applications, and license management.
* **Common end-user portal**.

This guide provides documentation for installing Automation Suite on your EKS or AKS cluster.

## Key benefits
  ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/209162)

### Deployment scenarios

You can deploy Automation Suite in an online or offline environment, with optional proxy use, in either lite mode or multi-node mode.

### Security and compliance

Automation Suite is pre-configured with optional OPA policies and network policies to follow the principles of the least privilege. In addition, to control the OPA policies, Automation Suite also bundles an optional Gatekeeper component.

### Prerequisites

Before installing Automation Suite, you must make sure that your cluster meets the infrastructure requirements.

### Installation

UiPath® provides the `uipathctl` CLI tool, which handles operations such as running prerequisite validations, installing Automation Suite on your cluster, and performing upgrades.

### Post-installation management

Automation Suite provides management operations via `uipathctl`, such as adding new products, updating certificates, configuring Automation Suite in maintenance mode, taking backups, and monitoring.

### Upgrade and migration

This section provides more details on how to upgrade Automation Suite or your infrastructure underneath Automation Suite, and how to migrate from standalone products to Automation Suite.

For details, see [Upgrade](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/upgrading-automation-suite#upgrading-automation-suite) and.

### Troubleshooting

You can run health checks and tests to help detect issues and whether they are in the infrastructure layer or within Automation Suite.

## Evaluation guide

### Requirements and installation

| Details | Instructions |
| --- | --- |
| Requirements and installation instructions for Automation Suite. | [Automation Suite requirements](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/kubernetes-cluster-and-nodes#kubernetes-cluster-and-nodes)  [Automation Suite installation](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/installing-automation-suite#installing-automation-suite) |

### Platform evaluation

| Details | Instructions |
| --- | --- |
| Complete an initial platform configuration. | [Automation Suite Configuration checklist](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/configuration-checklist) |
| Connect your first robot | [Connecting Attended Robots](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/connecting-your-first-robot) |
| Monitor the stack, troubleshoot issues, create alerts, and view dashboards from a centralized location. | [Troubleshooting tools](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/troubleshooting-tools#troubleshooting-tools)  [Using the monitoring stack](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/using-the-monitoring-stack#using-the-monitoring-stack) |

### Product evaluation

The following instructions take you to the corresponding product guides.

| Product | Evaluation checklist |
| --- | --- |
| Orchestrator | [Orchestrator configuration checklist](https://docs.uipath.com/orchestrator/automation-suite/2.2510/user-guide/orchestrator-configuration-checklist) |
| Automation Suite Robots | [Automation Suite Robots configuration checklist](https://docs.uipath.com/orchestrator/automation-suite/2.2510/user-guide/prerequisites) |
| Automation Hub | [Automation Hub configuration checklist](https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/automation-hub-configuration-checklist) |
| Automation Ops | [Automation Ops configuration checklist](https://docs.uipath.com/automation-ops/automation-suite/2.2510/user-guide/automation-ops-configuration-checklist) |
| Autopilot for Everyone | [Autopilot for Everyone configuration checklist](https://docs.uipath.com/autopilot/other/latest/user-guide/configuration-checklist-for-autopilot-for-everyone-in-automation-suite) |
| Test Manager | [Test Manager configuration checklist](https://docs.uipath.com/test-suite/automation-suite/2.2510/user-guide/test-manager-user-actions) |
| AI Center | [AI Center configuration checklist](https://docs.uipath.com/ai-center/automation-suite/2.2510/user-guide/ai-center-configuration-checklist) |
| Action Center | [Action Center configuration checklist](https://docs.uipath.com/action-center/automation-suite/2.2510/user-guide/action-center-configuration-checklist) |
| Apps | [Apps configuration checklist](https://docs.uipath.com/apps/automation-suite/2.2510/user-guide/apps-configuration-checklist) |
| Insights | [Insights configuration checklist](https://docs.uipath.com/insights/automation-suite/2.2510/user-guide/insights-configuration-checklist) |
| Data Service | [Data Service configuration checklist](https://docs.uipath.com/data-service/automation-suite/2.2510/user-guide/data-service-configuration-checklist) |
| Process Mining | [Process Mining configuration checklist](https://docs.uipath.com/process-mining/automation-suite/2.2510/user-guide/process-mining-configuration-checklist) |
| Document Understanding | [Document Understanding AI Center-based projects configuration checklist](https://docs.uipath.com/document-understanding/automation-suite/2024.10/classic-user-guide/document-understanding-deployed-in-automation-suite-first-run-experience)  [Document Understanding modern projects configuration checklist](https://docs.uipath.com/document-understanding/automation-suite/2024.10/user-guide/document-understanding-configuration-checklist) |
| Integration Service | [Integration Service configuration checklist](https://docs.uipath.com/integration-service/automation-suite/2.2510/user-guide/integration-service-configuration-checklist) |
| Studio Web | [Studio Web configuration checklist](https://docs.uipath.com/studio-web/automation-suite/2.2510/user-guide/studio-web-configuration-checklist) |
| AI Trust Layer | [AI Trust Layer configuration checklist](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/about-ai-trust-layer#ai-trust-layer-configuration-checklist) |
| Solutions | [Solutions configuration checklist](https://docs.uipath.com/solutions-management/automation-suite/2.2510/user-guide/solutions-configuration-checklist) |