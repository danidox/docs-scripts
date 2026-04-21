---
title: "Automation Suite stack"
visible: true
slug: "automation-suite-stack"
---

## High-level architecture

Automation Suite on EKS/AKS allows you to bring and manage your own Kubernetes cluster, dedicated to Automation Suite.

![docs image](https://docs.uipath.com/api/binary/automation-suite/2/309203/330685)

There are three sections of the stack:

1. **UiPath® managed**: UiPath® services and components optimized for Automation Suite provided and supported by UiPath®.
2. **Optional to install**: If you have the same components pre-configured in your Kubernetes cluster, you can choose to skip installing them via Automation Suite. In this case, you will manage the lifecycle of these components.
3. **Customer managed:** Prerequisites for deploying Automation Suite on your cloud infrastructure managed and supported by you. For supported EKS/AKS configurations, see the [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix).

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Stack Component
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Description
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td colspan="2" headers="d74469e56 d74469e60">
    <p>
     <strong>
      UiPath&reg; managed
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     UiPath&reg; products
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     When you deploy Automation Suite, a minimum set of shared capabilities are installed by default, such as UiPath&reg; Portal, Identity,
                                    License, Org Management, and Audit.
    </p>
    <p>
     You can choose which UiPath&reg; products to enable on Automation Suite both at the time of installation or post-installation.
                                    Note that there are  you must address.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     ArgoCD
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Open-source declarative CD tool for Kubernetes. It follows the GitOps pattern of using Git repositories as the source of truth
                                    for defining the desired application state. It is optimized to provide application lifecycle management (ALM) capabilities
                                    for Automation Suite.
    </p>
   </td>
  </tr>
  <tr>
   <td colspan="2" headers="d74469e56 d74469e60">
    <p>
     <strong>
      Optional to install
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Gatekeeper and container policies
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Open-source tool that allows a Kubernetes administrator to implement policies for ensuring compliance and best practices in
                                    their cluster.
    </p>
    <p>
     If you bring your own Gatekeeper and associated policies, review the
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/security-and-compliance#security-and-compliance">
      access needed by Automation Suite
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Networking policies
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Kubernetes networking policies provide a way to control networking traffic flow at IP address or port level (Layer 4). Automation
                                    Suite comes with an optionally bundled component with networking policies implemented to follow security best practices.
    </p>
    <p>
     Note that Automation Suite-bundled networking policies are only compatible with Cilium CNI. If you use a different type of
                                    CNI or if you bring your own networking policies, make sure to check the compatibility of these policies with Automation Suite.
                                    For details, see
     <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/security-and-compliance#security-and-compliance">
      Security and compliance
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Cert Manager
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Cert Manager is an open-source certificate controller for Kubernetes. You can choose to keep the Cert Manager pre-configured
                                    within Automation Suite or bring your own. If you bring your own, you are responsible for managing the lifecycle of that component.
    </p>
    Note:
    <p>
     If you choose to bring your own Cert Manager, and your TLS certificate is issued by a private or non-public CA, you must manually
                                       include both the leaf certificate and intermediate CA certificates in the TLS certificate file. In case of public CAs, they
                                       are automatically trusted by client systems, and no further action is required on your part.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Prometheus
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Open-source system monitoring toolkit for Kubernetes. It can accept metrics from Kubernetes components and workloads running
                                    in the clusters and store those in time series database.
    </p>
    <p>
     If you choose not to install Automation Suite-bundled Prometheus, you must configure your Prometheus to collect metrics.
    </p>
    <p>
     Prometheus bundled with Automation Suite on EKS/AKS is not configured for high availability (HA) mode. If you require a monitoring
                                    stack with HA functionality, you must supply your own Prometheus.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Alert Manager
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Open-source tool that handles alerts sent by client applications such as the Prometheus server. It is responsible for deduplicating,
                                    grouping, and routing them to the correct receiver integrations, such as email, PagerDuty, or OpsGenie.
    </p>
    <p>
     Automation Suite configures custom alerts, such as certificate expiration. If you choose not to install Automation Suite-bundled
                                    Alert Manager, you must configure your own alerts.
    </p>
    <p>
     Alert Manager bundled with Automation Suite on EKS/AKS is not configured for high availability (HA) mode. If you require a
                                    monitoring stack with HA functionality, you must supply your own Alert Manager.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Grafana
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Open-source visualization tool used for querying and visualizing data stored in Prometheus. You can create and ship a variety
                                    of dashboards for cluster and service monitoring.
    </p>
    <p>
     If you choose not to install Automation Suite-bundled Alert Manager, you must create your own alerts.
    </p>
    <p>
     Grafana bundled with Automation Suite on EKS/AKS is not configured for high availability (HA) mode. If you require a monitoring
                                    stack with HA functionality, you must supply your own Grafana.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     FluentD and Fluent-bit
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Open-source log scraping solution. The logging operator deploys and configures a background process on every node to collect
                                    container and application logs from the node file system.
    </p>
    <p>
     If you choose not to install Automation Suite-bundled FluentD and Fluent Bit, you must configure your own log scraper.
    </p>
    If you do install them, ensure the cluster has a default storage class annotated with
    <code>
     storageclass.kubernetes.io/is-default-class: "true"
    </code>
    .
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Velero
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Open-source tool that allows you to take a snapshot backup and restore.
    </p>
    <p>
     If you choose not to install Automation Suite-bundled Velero, make sure you take backups as per your Disaster Recovery policy.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Istio
    </p>
   </td>
   <td headers="d74469e60">
    Open-source service mesh that provides functionality such as ingress, request routing, traffic monitoring, etc., for the microservices
                                 running inside the Kubernetes cluster.
   </td>
  </tr>
  <tr>
   <td colspan="2" headers="d74469e56 d74469e60">
    <p>
     <strong>
      Customer managed
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Kubernetes cluster (AKS or EKS)
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Azure Kubernetes Service and Elastic Kubernetes Service are managed Kubernetes services from Microsoft Azure cloud and Amazon
                                    Web Services, respectively. Make sure to configure the EKS/AKS clusters correctly with the required worker nodes and capacity.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Object storage
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Automation Suite and UiPath&reg; Services require Object Storage - Azure Blob Storage or Amazon S3 (Simple Storage Service).
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Block storage
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Block storage is similar to disk storage needed for Automation Suite platform and UiPath&reg; products. Automation Suite is compatible
                                    with Azure Disk Storage and Amazon&rsquo;s Elastic Block Storage.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     File Storage
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     File storage is hierarchical data storage methodology and is needed for several UiPath&reg; products. Automation Suite is compatible
                                    with Azure Files and Elastic File Storage from Microsoft and AWS clouds, respectively.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Caching
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     Caching is required by several UiPath&reg; products. Automation Suite is compatible with Cloud Redis for Azure and Elasticache
                                    for AWS.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d74469e56">
    <p>
     Database
    </p>
   </td>
   <td headers="d74469e60">
    <p>
     SQL Server and SQL databases are needed for all UiPath&reg; products. Automation Suite is compatible with Microsoft SQL server,
                                    Azure SQL and AWS managed (RDS) SQL services.
    </p>
    For the latest version of Airflow PostgreSQL is required for Process Mining
    <code>
     AutomationSuite_Airflow
    </code>
    database. (Automation Suite 2023.10.9 or newer versions).
   </td>
  </tr>
 </tbody>
</table>

## Responsibility matrix

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Activity
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      UiPath&reg; responsibility
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Customer responsibility
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d74469e263">
    <p>
     <strong>
      Infrastructure prerequisites
     </strong>
    </p>
   </td>
   <td headers="d74469e267">
    <ul>
     <li>
      <p>
       Document guidance on capacity for nodes in the cluster
      </p>
     </li>
     <li>
      <p>
       Document compatibility matrix of supported cloud services and their versions
      </p>
     </li>
     <li>
      <p>
       Document prerequisite validation checks before installation
      </p>
     </li>
    </ul>
   </td>
   <td headers="d74469e271">
    <ul>
     <li>
      <p>
       Provision required infrastructure resources dedicated to Automation Suite
      </p>
     </li>
     <li>
      <p>
       Manage the infrastructure on an ongoing basis (e.g., patching, availability, etc.)
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74469e263">
    <p>
     <strong>
      Managing optional components
     </strong>
    </p>
    <ul>
     <li>
      <p>
       UiPath&reg; services
      </p>
     </li>
     <li>
      <p>
       Components
      </p>
     </li>
    </ul>
   </td>
   <td headers="d74469e267">
    <ul>
     <li>
      <p>
       Provide validated stack with the components
      </p>
     </li>
     <li>
      <p>
       Supported by UiPath&reg;
      </p>
     </li>
     <li>
      <p>
       Upgrades provided by UiPath&reg; with new releases
      </p>
     </li>
    </ul>
   </td>
   <td headers="d74469e271">
    <ul>
     <li>
      <p>
       Choose to install Automation Suite with optional components (recommended) or bring your own
      </p>
     </li>
     <li>
      <p>
       If you bring your own components, you must manage the life cycle of said components
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74469e263">
    <p>
     <strong>
      Network policies (optionally provided by UiPath&reg;)
     </strong>
    </p>
   </td>
   <td headers="d74469e267">
    <ul>
     <li>
      <p>
       Provide networking policies as an optional component based on Cilium CNI
      </p>
     </li>
     <li>
      <p>
       Networking policies control access from UiPath&reg; services on an as-needed basis to follow principle of least privilege
      </p>
     </li>
     <li>
      <p>
       Publish documentation for required compatible networking policies
      </p>
     </li>
    </ul>
   </td>
   <td headers="d74469e271">
    <ul>
     <li>
      <p>
       Choose to use networking policies packaged with Automation Suite based on Cilium plugin or bring your own policies
      </p>
     </li>
     <li>
      <p>
       If you choose to install your own networking policies, you may need to adjust your policies based on
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/security-and-compliance#security-and-compliance">
        UiPath&reg; documentation
       </a>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74469e263">
    <p>
     <strong>
      Gatekeeper and OPA policies (optionally provided by UiPath&reg;)
     </strong>
    </p>
   </td>
   <td headers="d74469e267">
    <ul>
     <li>
      <p>
       Include optional Gatekeeper and OPA policies to control access privileges of the containers
      </p>
     </li>
     <li>
      <p>
       Documentation of compatible policies for you if you choose to bring your own Gatekeeper and policies
      </p>
     </li>
    </ul>
   </td>
   <td headers="d74469e271">
    <ul>
     <li>
      <p>
       Choose to install Gatekeeper and OPA policies that are part of Automation Suite or install your own Gatekeeper and associated
                                       container privilege policies
      </p>
     </li>
     <li>
      <p>
       Refer to
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/security-and-compliance#security-and-compliance">
        UiPath&reg; published policies
       </a>
       that are compatible with Automation Suite to make any necessary changes
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74469e263">
    <p>
     <strong>
      <code>
       uipathctl
      </code>
      (management tool)
     </strong>
    </p>
   </td>
   <td headers="d74469e267">
    <ul>
     <li>
      Provide management tool (similar to
      <code>
       kubectl
      </code>
      ) optimized for installing and
                                       managing Automation Suite
     </li>
     <li>
      <p>
       Documentation on how to use the tool associated with use cases (ex: running pre-checks, installing, etc.)
      </p>
     </li>
    </ul>
   </td>
   <td headers="d74469e271">
    <ul>
     <li>
      Management node / machine with
      <code>
       uipathctl
      </code>
      , connectivity to the cluster and
                                       cluster admin access to install and run Automation Suite
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74469e263">
    <p>
     <strong>
      Automation Suite upgrades
     </strong>
    </p>
   </td>
   <td headers="d74469e267">
    <ul>
     <li>
      <p>
       Provide minor updates to Long Term Support (LTS) versions that consist of service image updates
                                       for bug fixes and security patches typically every two
                                       months
      </p>
     </li>
     <li>
      <p>
       Provides new LTS versions of Automation Suite that consist of new service features (e.g.,
                                       Orchestrator) and updates component versions typically every
                                       six months. UiPath&reg; will also publish an updated
                                       compatibility matrix of the new LTS version and
                                       infrastructure components (e.g., EKS versions)
      </p>
     </li>
    </ul>
   </td>
   <td headers="d74469e271">
    <ul>
     <li>
      <p>
       Consume minor updates regularly to get bug fixes and security patches. Minor releases are meant to be lightweight
      </p>
     </li>
     <li>
      <p>
       Update to major LTS versions to get feature updates and updated compatibility matrix
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74469e263">
    <p>
     <strong>
      Infrastructure upgrades
     </strong>
    </p>
   </td>
   <td headers="d74469e267">
    <ul>
     <li>
      <p>
       Publish compatibility matrix for each new LTS version release
                                       to allow you to upgrade your infrastructure and stay within
                                       supported versions of EKS or AKS. For supported EKS/AKS
                                       versions, see the
       <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix">
        Compatibility matrix
       </a>
       .
      </p>
     </li>
    </ul>
   </td>
   <td headers="d74469e271">
    <ul>
     <li>
      <p>
       Update the infrastructure based on Automation Suite compatibility matrix
      </p>
     </li>
     <li>
      <p>
       Follow best practice of taking backups before upgrades
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74469e263">
    <p>
     <strong>
      Backup and Restore
     </strong>
    </p>
   </td>
   <td headers="d74469e267">
    <ul>
     <li>
      <p>
       Provide optional backup and restore functionality
      </p>
     </li>
     <li>
      <p>
       Document how to configure Automation Suite in maintenance mode and take backup
      </p>
     </li>
    </ul>
   </td>
   <td headers="d74469e271">
    <ul>
     <li>
      <p>
       Choose to install Automation Suite provided backup/restore functionality or use your own solution and follow UiPath&reg; documentation
                                       on best practices and maintenance mode
      </p>
     </li>
     <li>
      <p>
       For infrastructure prerequisites (such as SQL, or Storage), you must take backups
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74469e263">
    <p>
     <strong>
      Support
     </strong>
    </p>
   </td>
   <td headers="d74469e267">
    <ul>
     <li>
      <p>
       Provide support based on Support Programs mentioned
       <a href="https://www.uipath.com/support/packages-options">
        here
       </a>
       .
      </p>
     </li>
     <li>
      <p>
       Provide support for Automation Suite
      </p>
     </li>
     <li>
      <p>
       Provide diagnostics tool to help identify the root cause of common issues (the Automation Suite package or your infrastructure)
      </p>
     </li>
    </ul>
   </td>
   <td headers="d74469e271">
    <ul>
     <li>
      <p>
       Manage and support the infrastructure prerequisites or non-Automation Suite bundled components
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>