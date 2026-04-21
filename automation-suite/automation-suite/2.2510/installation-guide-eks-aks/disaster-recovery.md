---
title: "Disaster recovery - Active/Passive"
visible: true
slug: "disaster-recovery"
---

This article walks you through the core concepts and architecture of Automation Suite disaster recovery, covering Active/Passive deployments.

:::important
Active/Passive mode is currently available only for EKS.
:::

Ensuring continuous business automation is at the core of any automation platform. Automation Suite can withstand the complete failure of nodes, entire data centers, or regions. You can deploy Automation Suite as an Active/Passive configuration.

Automation Suite multi-site deployments in Active/Passive mode support the following scenarios:

* **Same-region deployment** – Two Automation Suite clusters deployed in the same region;
* **Cross-region deployment** – Two Automation Suite clusters deployed in different regions.

The following table provides details on which Automation Suite products you can deploy in Active/Passive mode.

| Product | Support for Active/Passive |
| --- | --- |
| Orchestrator | ✅ |
| Action Center | ✅ |
| AI Center | ✅ |
| Apps | ✅ |
| Automation Ops | ✅ |
| Automation Suite Robots | ✅ |
| Computer Vision | ✅ |
| Data Service | ✅ |
| Document Understanding | ✅ |
| Test Manager | ✅ |
| Automation Hub | ✅ |
| Insights | ✅ |
| Process Mining | ✅ |
| Integration Service | ✅ |
| LLM gateway | ✅ |
| LLM observability | ✅ |
| ECS | ✅ |
| Studio Web | ✅ |
| Autopilot for Everyone | ❌ |
| Solutions | ❌ |

:::note
* You can install products that are not supported in Disaster Recovery with Active/Passive . However, you cannot use these products
when the primary cluster is down.
* For AI Center, the training pipeline functionality is available only in the primary cluster.
:::

## Requirements

To configure an Active/Passive deployment, make sure you meet the following requirements:

* Hardware
* Database
* Amazon Elastic Cache (Redis)
* S3 (Object Store)
* SQS (Queues)
* Route 53
* Product-specific requirements

### Hardware

The secondary (Passive) hardware cluster must be identical to the Primary hardware cluster.

### Database

The database must be accessible from both the Active and Passive clusters.

### Amazon Elastic Cache (Redis)

The system must operate separately for both the Active cluster and the Passive cluster.

### S3 (Object Store)

The S3 system must be synchronized and it must support Cross-Region Replication (CRR).

### SQS (Queues)

SQS must operate separately on Active and Passive setups.

### Route 53

Route53 must be used to control the routing of traffic. Configuration in Route53 is required to direct traffic to the active load balancer when functional.

In case of a disaster, the traffic must be re-routed to the passive load balancer using route 53.

### Product-specific requirements

If your deployment includes Studio Web or Insights, you must enable backup and restore for their persistent volumes (PVC-backed data) to ensure these products can recover properly during failover and failback. For details, refer to:

* [AKS backup and restore](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/aks-backup-and-restore#aks-backup-and-restore)
* [EKS backup and restore](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/eks-backup-and-restore#eks-backup-and-restore)