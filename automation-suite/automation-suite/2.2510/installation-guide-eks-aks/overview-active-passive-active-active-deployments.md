---
title: "Overview"
visible: true
slug: "overview-active-passive-active-active-deployments"
---

## Diagrams

The following diagram depicts a regular Active/Passive deployment of Automation Suite:

![docs image](https://docs.uipath.com/api/binary/automation-suite/2/596477/571551)

## Requirements

| Hardware | Requirements |
| --- | --- |
| Global Traffic Manager (GTM) | Distributes traffic to your Automation Suite multi-site deployment. The service must be highly available and immune to any deployment site. Additionally, the GTM must be able to configure the health check to isolate the faulty site quickly. The GTM is not mandatory but is recommended for a quick switchover. When configuring the Global Traffic Manager (GTM) for Active/Passive deployments, make sure to use `/orchestrator_/api/status` as the health endpoint. This is critical for effective disaster recovery management. |
| Load balancer | Every site needs a local load balancer that can load-balance the traffic to any node configured in the same site. |
| Node | Both sites must have identical number of nodes and for each site you must configure the cluster and nodes using the documentation provided in the [Kubernetes cluster and nodes](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/kubernetes-cluster-and-nodes#kubernetes-cluster-and-nodes) page.  For more details, see [Automation Suite Install Sizing Calculator](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/capacity-planning#capacity-planning). |
| SQL database | An external SQL server is required to store the data. For disaster recovery, you need Always On Availability Groups (or Amazon RDS's MSSQL with ReadReplica) with a primary SQL server in Site 1 and at least one secondary physically SQL Server (ReadReplica) located in Site 2 with data sync enabled. There is also a SQL listener deployed on top of the SQL server. Both clusters are configured to use the address of the same listener.  Both the active (primary) and passive (secondary) sites/clusters must use the Primary Database endpoint for database communication.  In the event of a disaster, once the read replica is promoted to primary, its endpoint must be updated in both the active and passive sites to serve as the new database connection string.  To simplify failover management, Amazon Route 53 can be used to create a DNS record for the database. Initially, it must point to the Primary Database Endpoint (or Listener). In case of a failover, the Route 53 record can be updated to point to the newly promoted primary database (formerly the read replica). |
| Objectstore | Any files or packages uploaded to products are stored in the objectstore. For greater resilience to failure, Automation Suite deployments require an external objectstore.  For effective disaster recovery, two objectstore instances are required; one instance must be situated in each data center. At any given time, only one objectstore instance must be actively used for reading and writing by both clusters. This process must be complemented by asynchronous replication to the secondary instance. |

## Load balancer and DNS configuration

This section outlines the infrastructure setup, DNS architecture, and routing logic for a system designed to operate in both normal and disaster recovery scenarios.

### Infrastructure overview

To support high availability and disaster recovery, the system requires a dual-load-balancer setup:

* **Primary Load Balancer**: Assigned to the **active (primary) cluster** for handling standard application traffic.
* **Secondary Load Balancer**: Assigned to the **passive (secondary) cluster**, ready to take over in case of a failure in the primary.

Each load balancer is assigned a unique Elastic IP (EIP), which serves as the endpoint for DNS resolution.

### DNS architecture

To facilitate traffic management and cluster-specific service accessibility, two tiers of DNS configuration are employed.

* **FQDN**: The application FQDN is the primary domain used by end users to access the application interface. This value corresponds to the `fqdn` field in `input.json`. For more details, refer to [Active/Passive configurations](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery-installation#disaster-recovery%3A-active%2Fpassive-configurations).
* **Cluster-specific FQDNs**: In addition to the main application FQDN, each cluster requires its own FQDN for administrative and monitoring tools. This value is defined under the `cluster_fqdn` field in each cluster’s `input.json`. For more details, refer to [Active/Passive configurations](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/disaster-recovery-installation#disaster-recovery%3A-active%2Fpassive-configurations).
* **Subdomains**: For comprehensive service access, a set of subdomains is configured for both the application FQDN and each cluster-specific FQDN. These include:
  + FQDN:
    - `apps.<domain>` – used by Apps.
    - `insights.<domain>` – used by for Insights.
  + Cluster-specific FQDN:
    - `alm.<domain>` – used by ArgoCD and for deployment management. This is required for both Active (primary) and Passive (secondary) clusters.
    - `monitoring.<domain>` – used for observability and alerts. This is required for both Active (primary) and Passive (secondary) clusters.All subdomains are directed to the same Elastic IP (EIP) as their respective root domain to maintain consistency and ease of routing.

### DNS routing logic

The DNS routing logic ensures that user traffic is directed to the appropriate load balancer depending on the system state
- either during normal operation or disaster recovery.
* **Normal Operations** (Primary Cluster is Active) In standard operation mode, DNS routes traffic as described in the following table:

  | FQDN type | Routing target |
  | --- | --- |
  | FQDN | Primary Cluster Load Balancer |
  | Primary Cluster FQDN | Primary Cluster Load Balancer |
  | Secondary Cluster FQDN | Secondary Cluster Load Balancer |

* **Disaster Recovery** (Secondary Cluster is Active) If the primary cluster fails, the system enters disaster recovery mode. In this state, DNS is adjusted to ensure service continuity:

  | FQDN type | Routing target |
  | --- | --- |
  | FQDN | Secondary Cluster Load Balancer |
  | Primary Cluster FQDN | Primary Cluster Load Balancer*(unchanged)* |
  | Secondary Cluster FQDN | Secondary Cluster Load Balancer*(unchanged)* |