---
title: "Basic architecture considerations"
visible: true
slug: "basic-architecture-considerations"
---

As with any multi-site deployment, the primary architecture considerations for Automation Suite account for infrastructure, latency, data source, management, Recovery Time Objective, Recovery Point Objective, etc.

## Infrastructure

We recommend using the same hardware for both clusters. However, the Automation Suite cluster will likely work with similar hardware configurations with little difference. Heterogeneous hardware may increase complexity and slow down troubleshooting.

## Management

The two Automation Suite clusters are independent and do not share any configuration. Therefore, any management or maintenance activity must be done individually on these clusters. For instance, you must update the SQL connection strings on both clusters, configure certificates separately, etc. In addition, you must monitor the two clusters independently, upgrade them individually, etc.

## Datasource

The objectstore, combined with the SQL database, forms the state of an installed product on Automation Suite.

SQL Server configuration plays a vital role in a multi-site deployment. Though SQL Server is a component external to Automation Suite, a few additional steps are required to ensure true HA when working with Automation Suite.

The SQL Server must be configured in the Always On Availability Group or failure over groups. It must be spread across both sites to ensure accurate High Availability when one site is down. Both clusters must use the same SQL listener endpoint in the connection string. Furthermore, it is recommended to set the `MultiSubnetFailover=True` property in the connection string when the SQL server/databases are distributed across multiple subnets.

For more details, refer to [Working with read replicas for Microsoft SQL Server in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.ReadReplicas.html), [Always On availability groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/always-on-availability-groups-sql-server?view=sql-server-2017), and [Prerequisites, Restrictions, and Recommendations for Always On availability groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/prereqs-restrictions-recommendations-always-on-availability?view=sql-server-2017).

The external objectstore is immune to possible corruption due to node failure. Data replication and disaster recovery can be carried out independently of Automation Suite. Like SQL Server, the external objectstore must be configured in a highly available Disaster Recovery setup. The primary objectstore instance is physically located in the primary data center, and at least one secondary instance is located in the secondary data center with data sync enabled. You can configure a load balancer on the objectstore to ensure both Automation Suite clusters refer to the same endpoints. This makes the deployment independent of how the objectstore is configured internally.

:::important
For AWS S3, the [multi-region access point](https://aws.amazon.com/s3/features/multi-region-access-points/) does not support all the s3 APIs required by all the products running in Automation Suite. For details on the list of support APIs, see [Using Multi-Region Access Points with supported API operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html). You can create two buckets per product/suite in both regions and enable synchronization. The Automation Suite cluster running in the same region will refer to the buckets in the same region.
:::

## Recovery Time Objective

Your organization’s policy around RTO is vital in designing your multi-site Automation Suite cluster. To achieve the desired RTO, take the following aspects into consideration:

* Design of the Traffic Manager;
* Availability of the nodes in the secondary/passive cluster;
* Dynamic workload availability on the secondary cluster; for example, MLSkill;
* Configuration Management.

### Traffic Manager

To unlock the full potential of both clusters, it is crucial to configure the Traffic Manager appropriately. The setup should ideally facilitate the distribution of traffic to both clusters. This strategy not only ensures a balanced load distribution, but also safeguards business continuity, mitigating any potential disruptiveness if either site experiences a complete shutdown.

### Nodes availability

In the event of a disaster that results in one site becoming entirely non-operational, the other site must have enough capacity to ensure that business automation is not impacted. Insufficient capacity at the functioning site may negatively affect the running of the business and potentially lead to significant operational issues.

### Dynamic workload availability

A few products, such as AI Center, deploy the ML Skills dynamically at the runtime. The deployment of the skills in another cluster is always asynchronous. This cannot guarantee their availability. To ensure that your automation solution returns online within the desired time, you can periodically sync the skills in another cluster.

### Configuration management

Since multi-site Automation Suite deployments consist of two distinct clusters, any operation performed on any cluster must be performed on the other cluster in time to reduce the drift. This ensures that both clusters possess similar configurations and that no additional effort is required during recovery.

## Recovery Point Objective

Your organization’s policy around Recovery Point Objective (RPO) is vital in designing your multi-site Automation Suite cluster. To achieve the desired RPO, you must take the following aspects into account:

* Data synchronization;
* Scheduled backup.

### Data synchronization

When written to the primary data source, data must also be synced to the secondary cluster. However, there is a risk of data loss when the data center is down, and data is not synced. Exemplary network configurations, such as high bandwidth and low latency between the two data centers, can speed up synchronization.

### Scheduled backup

Not all disaster recovery provides complete immunity to data loss. However, you can deploy a regular and periodic backup strategy to minimize the impact of the disaster on data recovery. For details, see [Backing up and restoring the cluster](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/backing-up-and-restoring-the-cluster#backing-up-and-restoring-the-cluster).