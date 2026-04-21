---
title: "High availability and disaster recovery
         strategy"
visible: true
slug: "high-availability-and-disaster-recovery-strategy"
---

UiPath® has a High Availability (HA) and Disaster Recovery (DR) strategy designed to minimize service disruptions, protect critical data, and ensure continuity of operations during infrastructure failures or regional outages.

## High availability

The objective of UiPath® is to ensure service continuity during localized infrastructure failures.

High availability is achieved through the following:

* **Redundant architecture**: UiPath products and services are deployed across multiple availability zones within each supported region.
* **Load balancing**: Requests are automatically distributed across healthy service instances using both application-level and network-level load balancers.
* **Stateless designs**: Where possible, services are designed to be stateless, allowing traffic to shift between instances in the event of a failure.
* **Health checks and auto healing**: Automated health checks monitor service status. Failed instances are automatically replaced using orchestration tools such as Kubernetes or Auto Scaling Group.
* **Data replication**: Persistent data is replaced across availability zones to maintain availability and consistency.

## Disaster recovery

The objective of UiPath® is to restore service availability and recover critical data in the event of a regional outage or catastrophic failure.

Our data recovery strategy includes:

* **Region-level redundancy**: We maintain redundant deployments for critical services across geographically isolated regions.
* **Cross-region data replication**: Persistent data is asynchronously replicated across regions to support availability and consistency.
* **Regular backups**: All critical data is backed up on a regular cadence. Backups are encrypted at rest and stored in durable, cross-region object storage.
* **Disaster recovery drills**: Scheduled disaster recovery exercises validate our fail over procedures and help identify and address gaps in automation, tooling, or documentation.

<sup>1</sup>The Singapore region does not have a secondary region due to requirements. Therefore, no data is saved outside Singapore.

When an incident occurs, recovery targets are defined using the following metrics:

* **Recovery Time Objective** (RTO): The maximum acceptable duration that a system, application, or process can be unavailable after a failure or disaster.
* **Recovery Point Objective** (RPO): The maximum acceptable amount of data loss measured in time. It reflects how much data you can afford to lose in case of a failure.

The target recovery objectives of UiPath® are:

* **RTO**: Less than or equal to four hours.
* **RPO**: Less than or equal to 15 minutes.

## Continuous Improvement

Our high availability and disaster recovery practices are continuously evaluated and improved based on the following:

* Post-incident reviews and lessons learned.
* Changes in infrastructure or application architecture.
* Advancements in platform capabilities and industry best practices.
* Cost versus risk analysis.