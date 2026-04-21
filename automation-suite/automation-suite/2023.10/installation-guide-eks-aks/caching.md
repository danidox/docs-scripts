---
title: "Caching"
visible: true
slug: "caching"
---

UiPath® products on Automation Suite require caching capabilities. You must provision Cloud Redis (Azure/AKS) or ElastiCache (AWS/EKS). For a list of prerequisites and compatible versions, see [Compatibility matrix](https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/compatibility-matrix#compatibility-matrix).

:::warning
Automation Suite on EKS/AKS does not currently support the [Redis database clustering](https://redis.io/docs/latest/operate/rs/databases/durability-ha/clustering/) capability that AWS and Azure offer. Therefore, you must select a Redis service using Redis Active/Passive cluster. For example, AWS refers to Redis database clustering as ElastiCache Redis (cluster mode enabled) cluster, so you must select [Redis (cluster mode disabled) cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/GettingStarted.CreateCluster.html#Clusters.Create.CON.Redis-gs) instead.
:::

Multiple services in Automation Suite, such as Orchestrator and Identity, use Redis as a distributed cache, for speeding up critical and high volume operations. These services store data that is accessed frequently in Redis, to avoid either retrieving the data from the database or doing expensive computations multiple times.

The following recommendations are specific to Azure. The general recommendation is to choose an SKU with at least 1GB capacity and a Service Level Agreement (SLA) for production environments.

For Redis cache requirements, the provisioning plan can vary, depending on the type of environment you want to deploy, such as a testing environment or a production environment:

* **Basic**: it is not recommended for production deployment since it does not offer Service Level Agreement (SLA). However, it could be used for a test environment.
* **Standard C1** (1GB): It provides decent capacity and performance suitable for a majority of installations. It also allows future scaling to higher levels, including Standard C2 or Premium.
* **Standard C2**: A step furhter than Standard C1, it provides larger capacity and better performance as compared to C1.
* **Premium**: The most recommended option, as it provides availability zones promoting a higher SLA, and VNet integration for enhanced security.

After meeting the caching prerequisites, you must pass the access information in the `input.json` file, as shown in the following example:

```
"fabric": {
  "redis": {
    "hostname": "xx",
    "password": "xx",
    "port": 6380,
    "tls": true
  }
}
```

:::note
Set the value of the `tls` parameter to `true` only if the Redis URL is trusted by a known authority or if you added the certificates to the additional CA certificates. Otherwise, set the value of the `tls` parameter to `false`.
:::