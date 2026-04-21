---
title: "Insights volumes created in two different
            zones following migration"
visible: true
slug: "insights-volumes-created-in-two-different-zones-following-migration"
---

## Description

When you migrate from Automation Suite on Linux to Automation Suite on EKS/AKS and your target cluster spans multiple zones, Insights-related volumes are occasionally created in two different zones. As a result, you may encounter issues when bringing up the Insights service.

## Solution

To address the problem, take the following steps:

1. Before migration, cordon the nodes in all zones, with the exception of the zone where you want the volumes to be located. To cordon the nodes, run the following command:
   ```
   kubectl cordon <node name>
   ```
2. Execute the Automation Suite on Linux to Automation Suite on EKS/AKS migration by running the command in Step 1 of [Running the cluster migration](https://docs.uipath.com/automation-suite/automation-suite/2.2510/installation-guide-eks-aks/migrating-between-automation-suite-clusters#running-the-cluster-migration).
3. Uncordon all the nodes you cordoned before the migration by running the following command:
   ```
   kubectl uncordon <node name>
   ```