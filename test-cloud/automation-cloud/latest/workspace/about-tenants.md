---
title: "About tenants"
visible: true
slug: "about-tenants"
---

**Tenants** allow you to model your organization structure, separating your business flows and information just like in real-life organizations. They are containers where you can organize your services and manage them for a group of users. For example, you can create tenants for each of your departments and decide what services you want to enable for each, based on their needs. In each tenant, you can have one instance of each of the cloud services.

## Default tenant

When you get started with an organization, your first tenant, called **DefaultTenant**, is automatically created.

## Multitenancy
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

Multitenancy lets you create multiple tenants within a single organization to isolate data and manage access across departments. Each tenant operates independently, which helps support separate automation initiatives and enforce data separation within the organization.

Depending on the cloud offering, all tenant data is stored either in the cloud in a database shared only between tenants that belong to the same organization, or in your private infrastructure.

Users invited to an organization can view and access only the tenants and services permitted by their assigned roles and permissions. TOPLEVELNOTEMARKER
:::note
For organizations that had multiple Orchestrator services before the introduction of tenants, the platform automatically creates one tenant for each existing Orchestrator service. Each tenant inherits the name of the corresponding Orchestrator service.
:::

## Orchestrator in your organization

All tenants contain an Orchestrator service.

While in on-premises Orchestrator, your Orchestrator instance can include several tenants, in cloud you have one Orchestrator service in each tenant.

A Test Cloud tenant is different from an [Orchestrator tenant](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-tenants#about-tenants) .

The following table describes the differences between an a Test Cloud tenant and an on-premises Orchestrator tenant.

| Tenant in Test Cloud | Tenant in on-premises Orchestrator |
| --- | --- |
| Is a subdivision of the cloud organization | Is a subdivision of the Orchestrator instance |
| Includes one Orchestrator service | Is a part of Orchestrator |
| Includes several other cloud services (UiPath® products), all within the organization | Is not in the same medium as your other UiPath products and interacts with them through integrations |
:::note
For more information about the differences between on-premises Orchestrator and the Orchestrator service in cloud offerings, also refer to [Orchestrator differences](https://docs.uipath.com/overview-guide/docs/orchestrator-differences).
:::

## Viewing tenants

Organization administrators can view and manage all of the tenants in their organization.

All existing tenants are displayed on the **Admin** page, in the panel on the left:

!['Viewing tenants' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/390991)

### Tenant statuses

Tenants can be in one of two states:

* **Enabled** - the tenant is active and can be accessed by users.
* **Disabled** - the tenant is not active and unavailable to users. **Disabled** is shown next to the tenant name in the tenants panel:

  !['Tenant statuses' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30777)

### Switching tenants

If your organization has multiple tenants and you have access to more than one, you can switch between tenants while on the page of a tenant-specific service. This lets you work with the data that exists within the selected tenant for the various services, which can be different than what is available in other tenants, or your service-level roles can be different between tenants.

To switch the context in which you are working to a different tenant, select the tenant list in the top right and select another tenant:

  !['Switching tenants' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/390995)

The page refreshes and then shows data for the newly selected tenant.