---
title: "Q&A: Disaster Recovery"
visible: true
slug: "qa-multi-site-deployments"
---

* **Q:** Can I deploy Automation Suite in Active-Passive mode?
* **A:** Yes.
* **Q**: How many HAA licenses do I need for configuring Active/Passive?
* **A**: You need a total of two HAA licenses, one for each cluster. Each of the licenses must be for two shards.
* **Q:** Do I need to bring additional product licenses for the passive cluster?
* **A:** No, once you apply the licenses on the primary cluster, they are available to use in the secondary cluster as well.
* **Q:** Can I turn off the secondary cluster while not in use?
* **A:** Yes, in the case of an Active-Passive setup, you can switch off some or all nodes in the secondary cluster while not in use.
* **Q:** Can I install unsupported products in the secondary cluster?
* **A:** No, you cannot install products that are not supported in the secondary cluster. If you try such an installation, the products will be unusable.
* **Q**: Can I rebuild the primary cluster using the secondary cluster when the backup is unavailable?
* **A:** No, to rebuild the primary cluster, you need a backup. However, you can rebuild the secondary cluster using the primary cluster.
* **Q:** Can I deploy an in-cluster objectstore with Active-Passive configurations?
* **A:** No, multi-site deployments have a strict requirement for external objectstore.
* **Q:** Can I perform cluster management when one of the Automation Suite clusters is unavailable or switched off?
* **A:** You must perform most operations, such as SQL connection string update, on both clusters. Therefore, both clusters must be available. However, if the cluster is unavailable, and you must update a configuration, you can de-link the clusters and operate individually.
* **Q:** If a product is down in the primary cluster, can I only switch the traffic for that product to secondary?
* **A:** Only site-level fault tolerance is allowed. Granular product-level tolerance is not supported right now.
* **Q:** Can I choose not to deploy a product in multi-site?
* **A:** You must install all products on both sites. You cannot choose to deploy a product only on one side except to discover products and Insights.
* **Q:** Can I bring heterogeneous machines in both clusters?
* **A:** You can bring different configurations of machines on both sites as long as those machines meet the hardware and software requirements for an Automation Suite installation.
* **Q:** Can I bring lower-spec machines for the secondary cluster?
* **A:** Yes, you can choose to deploy a smaller or fewer machines in the secondary cluster. This can be done to save some cost when Insights, Process Mining, and Automation Hub are not installed.
* **Q:** Can I run the training pipeline in the secondary cluster?
* **A:** You can schedule the training pipeline only on the primary cluster. This means training pipeline functionality is temporarily unavailable when the primary cluster is down.
* **Q:** Can I use the same Automation Suite/product license on both sites?
* **A:** Though both clusters are individual clusters, they are configured to behave as a single deployment. This also means you do not have to provide two separate Redis licenses.
* **Q:** Can I promote the secondary cluster to the primary cluster?
* **A:** No, you cannot promote the secondary cluster to the primary cluster.
* **Q:** Can I convert the multi-site deployment back to a standard Automation Suite setup?
* **A:** No, this is currently not possible. The only option is to recreate the setup from a backup.
* **Q:** What happens when the primary cluster is temporarily down in Active-Passive mode?
* **A:** When the primary cluster is temporarily down, Automation is temporarily unavailable. You must switch the traffic to the secondary cluster using the steps described [here](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/switching-to-the-secondary-cluster#switching-to-the-secondary-cluster-manually-in-an-active%2Fpassive-setup "This section provides high-level instructions on how to manually switch the traffic to the secondary cluster in an Active/Passive setup.").
* **Q:** What happens when the primary cluster is permanently down in Active-Passive mode?
* **A:** When the primary cluster is permanently down, Automation is temporarily unavailable. You must switch to the secondary cluster using the steps described [here](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/switching-to-the-secondary-cluster#switching-to-the-secondary-cluster-manually-in-an-active%2Fpassive-setup "This section provides high-level instructions on how to manually switch the traffic to the secondary cluster in an Active/Passive setup."), then rebuild the primary cluster from backup.
* **Q:** What happens when the secondary cluster is temporarily down in Active-Passive mode?
* **A:** When the secondary cluster is temporarily down, Automation Suite is not impacted. However, Disaster Recovery is not available. Once the secondary cluster is back, re-apply any configuration made on the primary cluster to the secondary cluster.
* **Q:** What happens when the secondary cluster is permanently down in Active-Passive mode?
* **A:** When the secondary cluster is permanently down, Automation Suite is not impacted. However, Disaster Recovery is not available. You must rebuild the secondary cluster using the primary cluster.
* **Q:** What happens when both clusters are temporarily down in Active-Passive mode?
* **A:** When both clusters are temporarily down, the entire Automation Suite is down until one site is online.
* **Q:** What happens when both clusters are permanently down in Active-Passive mode?
* **A:** When both clusters are permanently down, the entire Automation Suite is down. To bring back the setup, you must restore the primary cluster using a backup, and re-build the secondary cluster from the primary cluster.
* **Q:** What happens when any of the products is down in the primary cluster in Active-Passive mode?
* **A:** When any of the products is down in the primary cluster, that product is not be available. There is no way for you to switch the traffic only for that product in the secondary cluster. And vice-versa. Only site-level fault tolerance is possible.
* **Q:** What happens when the primary data source is down, and the data is not replicated to the secondary data source in Active-Passive mode?
* **A:** In this case, there would be data loss. Your RPO would govern the data loss. The promotion of the secondary data source to the primary would be governed by your RTO.
* **Q:** What happens when the primary data source is back after a brief downtime in Active-Passive mode?
* **A:** When the primary data source is back after a brief downtime, you must ensure that unless all the data is re-synced back to the original data source, you do not start redirecting traffic to the primary cluster.
* **Q:** What happens when both data sources are down in Active-Passive mode?
* **A:** In this case, you should expect complete downtime. A few inflight transactions may be stuck in that state forever.
* **Q:** What happens when the secondary data source is down in Active-Passive mode?
* **A:** In this case, Automation Suite is not impacted. You must ensure that data is replicated when the secondary data source is online.