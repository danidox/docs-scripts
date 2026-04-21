---
title: "Automation Suite overview"
visible: true
slug: "automation-suite-overview"
---

Automation Suite enables you to deploy the UiPath® business automation platform in your environment of your choice. Depending on your needs, you can deploy the platform on Linux servers (bare-metal or virtual machines) in your data center or public cloud (Azure, AWS, or GCP), or on your Kubernetes clusters in Amazon Web Services (Elastic Kubernetes Service) or Microsoft Azure (Azure Kubernetes Service).

Automation Suite includes:

* **All Server Products** (except for any new products shipping in Automation Cloud first).
* **All Shared Suite Capabilities** that enable you to easily configure the integration with existing enterprise systems, such as AD, AAD, or SAML, across all products; a common experience is offered across the suite for the user, tenant, external applications, and license management.
* **Common end-user portal**.

This guide provides documentation for installing Automation Suite on your EKS or AKS clusters.

If you are looking for our classic deployment experience in a Linux environment, refer to the [Automation Suite on Linux Installation Guide](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide/automation-suite-overview).

For an in-depth perspective on each deployment model, see [Cross-deployment model feature comparison](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/automation-suite-overview#cross-deployment-model-feature-comparison).

## Key benefits
  ![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/209162)

### Deployment scenarios

You can deploy Automation Suite in an online or offline environment, with or without a proxy.

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

For details, see [Upgrade](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/upgrading-automation-suite#upgrading-automation-suite-on-eks%2Faks) and.

### Troubleshooting

You can run health checks and tests to help detect issues and whether they are in the infrastructure layer or within Automation Suite.

## Cross-deployment model feature comparison

We aim to provide feature parity between our Automation Suite deployment models. However, there will always be some differences you should be aware of.

If you need to deploy Automation Suite on containerized platforms such as AKS or EKS, refer to the [Automation Suite on EKS/AKS Installation Guide](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/automation-suite-overview).

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <strong>
     User scenario/Feature
    </strong>
   </th>
   <th>
    <strong>
     Automation Suite on Linux
    </strong>
   </th>
   <th>
    <strong>
     Automation Suite on AKS
    </strong>
   </th>
   <th>
    <strong>
     Automation Suite on EKS
    </strong>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td colspan="4" headers="d37050e174 d37050e177 d37050e180 d37050e183">
    <p>
     <strong>
      Service capabilities
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Orchestrator
   </td>
   <td headers="d37050e177">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    AI Center
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    AI Center with external orchestrator (standalone)
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    <p>
     ❌
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     ❌
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Apps
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Action Center
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Automation Hub
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Automation Ops
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Data Service
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Document Understanding
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Insights
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Automation Suite Robots
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Process Mining
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Task Mining
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Test Manager
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Integration Service
   </td>
   <td headers="d37050e177">
    <p>
     ❌
    </p>
   </td>
   <td headers="d37050e180">
    ❌
   </td>
   <td headers="d37050e183">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Communications mining
   </td>
   <td headers="d37050e177">
    ❌
   </td>
   <td headers="d37050e180">
    ❌
   </td>
   <td headers="d37050e183">
    ❌
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Studio Web
   </td>
   <td headers="d37050e177">
    ❌
   </td>
   <td headers="d37050e180">
    ❌
   </td>
   <td headers="d37050e183">
    ❌
   </td>
  </tr>
  <tr>
   <td colspan="4" headers="d37050e174 d37050e177 d37050e180 d37050e183">
    <p>
     <strong>
      Architecture
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Kubernetes
   </td>
   <td headers="d37050e177">
    Rancher RKE2
   </td>
   <td headers="d37050e180">
    AKS
   </td>
   <td headers="d37050e183">
    EKS
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Databases
   </td>
   <td colspan="3" headers="d37050e177 d37050e180 d37050e183">
    <ul>
     <li>
      <p>
       MS SQL
      </p>
     </li>
    </ul>
    Note:
    <p>
     Additional Microsoft SQL platforms, such as Azure SQL Database or Azure SQL Managed Instance, as well as Amazon Relational
                                       Database Service are also supported as long as the Microsoft SQL Server database engine meets the requirements.
    </p>
    <ul>
     <li>
      <p>
       PostgreSQL for Process Mining Airflow database
      </p>
     </li>
    </ul>
    Note:
    <p>
     Automation Suite 2023.10.9 or higher.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    <p>
     Storage
    </p>
   </td>
   <td headers="d37050e177">
    <ul>
     <li>
      <p>
       Option 1: Object Storage (Ceph)
      </p>
     </li>
     <li>
      <p>
       Option 2: Object storage external to the cluster
      </p>
     </li>
    </ul>
    <p>
     UiPath&reg; provides Ceph.
    </p>
   </td>
   <td headers="d37050e180">
    <ul>
     <li>
      <p>
       Object Storage: Azure Blob
      </p>
     </li>
     <li>
      <p>
       Filesystem: Azure Filesystem
      </p>
     </li>
     <li>
      <p>
       Block Storage: Azure Disks
      </p>
     </li>
    </ul>
   </td>
   <td headers="d37050e183">
    <ul>
     <li>
      <p>
       Object Storage: AWS S3
      </p>
     </li>
     <li>
      <p>
       Filesystem: AWS EFS
      </p>
     </li>
     <li>
      <p>
       Block Storage: AWS EBS
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    <p>
     Service Mesh and Routing
    </p>
   </td>
   <td headers="d37050e177">
    <p>
     Rancher provided Istio Service Mesh
    </p>
    <p>
     Routing via envoy ingress gateway
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     OSS Istio Service Mesh
    </p>
    <p>
     Routing via WASM plugin
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     OSS Istio Service Mesh
    </p>
    <p>
     Routing via WASM plugin
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    <p>
     OPA
    </p>
   </td>
   <td headers="d37050e177">
    <p>
     OSS Gatekeeper
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     OSS Gatekeeper
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     OSS Gatekeeper
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    <p>
     Monitoring
    </p>
   </td>
   <td headers="d37050e177">
    <p>
     Rancher provided Prometheus &amp; Grafana
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     OSS Prometheus &amp; Grafana
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     OSS Prometheus &amp; Grafana
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    <p>
     Caching
    </p>
   </td>
   <td headers="d37050e177">
    <p>
     Embedded Redis with in the cluster and provided by UiPath&reg;
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     Cloud Redis outside the cluster and managed by customer
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     Cloud Redis outside the cluster and managed by customer
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    <p>
     Logging Aggregation
    </p>
   </td>
   <td headers="d37050e177">
    <p>
     Rancher provided Fluend/Fluent-bit
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     OSS Fluend/Fluent-bit
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     OSS Fluend/Fluent-bit
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    <p>
     Cert Manager
    </p>
   </td>
   <td headers="d37050e177">
    <p>
     OSS Cert Manager
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     OSS Cert Manager
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     OSS Cert Manager
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    <p>
     Deployment tool
    </p>
   </td>
   <td headers="d37050e177">
    <p>
     OSS ArgoCD
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     OSS ArgoCD
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     OSS ArgoCD
    </p>
   </td>
  </tr>
  <tr>
   <td colspan="4" headers="d37050e174 d37050e177 d37050e180 d37050e183">
    <p>
     <strong>
      Deployment scenario
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Single Node (Non-production)
   </td>
   <td headers="d37050e177">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     ❌
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     ❌
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Multi Node (HA)
   </td>
   <td headers="d37050e177">
    <p>
     ✅ (requires additional HAA license)
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     ✅
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Online
   </td>
   <td headers="d37050e177">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Offline
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     ✅
    </p>
   </td>
  </tr>
  <tr>
   <td colspan="4" headers="d37050e174 d37050e177 d37050e180 d37050e183">
    <strong>
     Deployment method
    </strong>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Advanced CLI
   </td>
   <td headers="d37050e177">
    <code>
     install-uipath.sh
    </code>
   </td>
   <td headers="d37050e180">
    <p>
     <code>
      uipathctl
     </code>
    </p>
   </td>
   <td headers="d37050e183">
    <code>
     uipathctl
    </code>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Interactive Installer
   </td>
   <td headers="d37050e177">
    ✅ (
    <code>
     InstallUiPathAS.sh
    </code>
    )
   </td>
   <td headers="d37050e180">
    <p>
     ❌
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     ❌
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Marketplace
   </td>
   <td headers="d37050e177">
    <p>
     ✅ (AWS QS Only)
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     ❌
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     ❌
    </p>
   </td>
  </tr>
  <tr>
   <td colspan="4" headers="d37050e174 d37050e177 d37050e180 d37050e183">
    <p>
     <strong>
      Installation
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    <p>
     A la carte product selection
    </p>
   </td>
   <td headers="d37050e177">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Custom domain
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Custom certificates
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Hardware requirements validation
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Proxy configuration
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Optional OSS/fabric component
   </td>
   <td headers="d37050e177">
    <p>
     ❌
    </p>
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td colspan="4" headers="d37050e174 d37050e177 d37050e180 d37050e183">
    <strong>
     Enterprise grade features
    </strong>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Disaster Recovery
   </td>
   <td headers="d37050e177">
    <p>
     ✅ (Active Passive deployment)
    </p>
   </td>
   <td headers="d37050e180">
    ❌
    <p>
     (Multi-zone architecture for UiPath&reg; services without zone affinity. Insights not supported.)
    </p>
   </td>
   <td headers="d37050e183">
    ❌
    <p>
     (Multi-zone architecture for UiPath&reg; services without zone affinity. Insights not supported.)
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Backup/restore
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Upgrade
   </td>
   <td headers="d37050e177">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td colspan="4" headers="d37050e174 d37050e177 d37050e180 d37050e183">
    <strong>
     Troubleshooting
    </strong>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Support bundle
   </td>
   <td headers="d37050e177">
    ✅(
    <code>
     support-bundle.sh
    </code>
    )
   </td>
   <td headers="d37050e180">
    ✅ (
    <code>
     uipathctl
    </code>
    )
   </td>
   <td headers="d37050e183">
    ✅ (
    <code>
     uipathctl
    </code>
    )
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Diagnostic tool
   </td>
   <td headers="d37050e177">
    ✅(
    <code>
     diagnostics-report.sh
    </code>
    )
   </td>
   <td headers="d37050e180">
    ✅(
    <code>
     uipathctl
    </code>
    )
   </td>
   <td headers="d37050e183">
    ✅ (
    <code>
     uipathctl
    </code>
    )
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Health Checks
   </td>
   <td headers="d37050e177">
    <p>
     ❌
    </p>
   </td>
   <td headers="d37050e180">
    ✅ (
    <code>
     uipathctl
    </code>
    )
   </td>
   <td headers="d37050e183">
    ✅ (
    <code>
     uipathctl
    </code>
    )
   </td>
  </tr>
  <tr>
   <td colspan="4" headers="d37050e174 d37050e177 d37050e180 d37050e183">
    <strong>
     Security
    </strong>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    FIPS enabled host
   </td>
   <td headers="d37050e177">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     ❌
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Gatekeeper/OPA policy
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Network policy
   </td>
   <td headers="d37050e177">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Hardened UiPath&reg; service container images
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    ArgoCD SSO
   </td>
   <td headers="d37050e177">
    <p>
     ✅ (LDAP only)
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     ✅
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    mTLS for service communication
   </td>
   <td headers="d37050e177">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     ✅
    </p>
   </td>
  </tr>
  <tr>
   <td colspan="4" headers="d37050e174 d37050e177 d37050e180 d37050e183">
    <strong>
     Migration options
    </strong>
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Standalone Orchestrator to Automation Suite full migration
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Standalone Orchestrator to Automation single tenant migration options
   </td>
   <td headers="d37050e177">
    ✅
   </td>
   <td headers="d37050e180">
    ✅
   </td>
   <td headers="d37050e183">
    ✅
   </td>
  </tr>
  <tr>
   <td headers="d37050e174">
    Automation Suite embedded to AS on AKS/EKS
   </td>
   <td headers="d37050e177">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e180">
    <p>
     ✅
    </p>
   </td>
   <td headers="d37050e183">
    <p>
     ✅
    </p>
   </td>
  </tr>
 </tbody>
</table>

## Evaluation guide

### Requirements and installation

| Details | Instructions |
| --- | --- |
| Requirements and installation instructions for Automation Suite. | [Automation Suite requirements](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/kubernetes-cluster-and-nodes#kubernetes-cluster-and-nodes)  [Automation Suite installation](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/installing-automation-suite#installing-automation-suite) |

### Platform evaluation

| Details | Instructions |
| --- | --- |
| Complete an initial platform configuration. | [Automation Suite Configuration checklist](https://docs.uipath.com/automation-suite/automation-suite/2023.10/admin-guide/configuration-checklist) |
| Connect your first robot | [Connecting Attended Robots](https://docs.uipath.com/automation-suite/automation-suite/2023.10/admin-guide/connecting-your-first-robot) |
| Monitor the stack, troubleshoot issues, create alerts, and view dashboards from a centralized location. | [Troubleshooting tools](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/troubleshooting-tools#troubleshooting-tools)  [Using the monitoring stack](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/using-the-monitoring-stack#using-the-monitoring-stack) |

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