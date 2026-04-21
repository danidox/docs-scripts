---
title: "Data residency"
visible: true
slug: "data-residency-"
---

In Test Cloud, services are deployed across multiple regions to support global availability, performance, and data residency requirements. As the cloud infrastructure expands, additional regions may become available to better support data sovereignty while maintaining high availability and low latency.

The region used for an organization or tenant can depend on factors such as licensing plans and regional preferences. This documentation provides information about where business data can be stored globally.

Depending on the cloud offering, the following regional deployment options may be available:

* **Automatic regional deployment:** Data is hosted in a region selected by UiPath based on availability, performance, and regulatory considerations. This is your type of regional deployment if you use [Test Cloud](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud#data-residency-test-cloud).
* **Region-specific availability:** Some cloud services are available only in specific geographic locations to meet regulatory or compliance requirements. This is your type of regional deployment if you use [Test Cloud Public Sector](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-public-sector#data-residency-test-cloud-public-sector).
* **Customer-selected region:** You can choose the cloud region where your data is stored during onboarding. This is your type of regional deployment if you use [Test Cloud Dedicated](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-dedicated#data-residency-test-cloud-dedicated). In customer-selected region deployments, availability may vary by region. Certain regions may have limited feature or hardware support (for example, GPU availability), which can affect where services can be deployed.