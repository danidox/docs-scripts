---
title: "Managing services"
visible: true
slug: "managing-services"
---

In each tenant, you can provision each of the services for which you have a license. You can then manage and work in that service as needed, within the context of the tenant.
:::note
In the case of organization-level services such as UiPath Apps, data is not isolated by tenants. The same service is available across your organization.
:::

## Provisioning or removing services

You can:

* provision the services you need as part of the setup process when you add a tenant.
* for an existing tenant, provision new services or remove existing ones whenever you need, as described on this page.

### Provisioning services

By provisioning a service to an existing tenant, you are adding to the services that are available for use within the context of that tenant.

To provision services for an existing tenant, take the following steps:

1. Navigate to **Admin** and select the tenant in the left rail.
2. Select **Services**.

The **Services** page for the tenant opens, showing the services that are currently provisioned.
3. Select **Add Services**.
   :::note
   If you have already provisioned all services, the button is not available.
   :::

The **Add Services** panel opens.
4. Select the checkbox for each service that you want to add to this tenant.
   :::note
   Services that require a license and for which you do not have one available are not shown.
   :::
5. Select **Add**.

The panel closes and the tenant is briefly unavailable while the selected services are being provisioned.

When finished, the new services are displayed on the **Services** page.

### Removing services

Removing (or deleting) a service from a tenant means the service is no longer available to users while in the context of that tenant. If the service is provisioned in other tenants, it remains available for use in other tenants.

**Licenses**
* In the case of a service with a [service instance license](https://docs.uipath.com/overview-guide/docs/service-licensing#service-instances), such as UiPath Automation Hub, removing the service from the tenant also frees up one license unit for the service. You can then use the license to provision the service in a different tenant, if needed.
* In the case of a service with [user licenses](https://docs.uipath.com/overview-guide/docs/user-licensing) or [runtimes](https://docs.uipath.com/overview-guide/docs/service-licensing#runtimes-robot-licenses) (robot licenses) allocated, such as UiPath Orchestrator, the licenses that were used for the service are returned to the organization's pool of licenses and they can be re-allocated as needed.

To remove services from a tenant:

1. Go to **Admin** and select the tenant in the panel on the left.
2. Select **Services**.

The **Services** page for the tenant opens, showing the services that are currently provisioned.
3. On the card of the service you want to remove, select the **More** icon, and then select **Remove**.
   :::note
   The **Remove** option is not available for the Orchestrator service because it must be present in every tenant.
   :::

A confirmation dialog opens.
4. In the field, type the name of the service, exactly as it is shown (including capitalization), and then select **Delete**.

The dialog closes and, on the **Services** page, the service is removed from the list of services for the tenant.

While in the context of the tenant, the removed service is no longer available to users.

The licenses for the service, if any, are now available for use in other tenants.

## Enabling or disabling services

When you disable a service:

* Any existing license allocation for the service is removed and licenses are returned to the organization pool.
* The service data is retained and the service remains available to organization administrators in case you want to re-enable it later.
* The service is no longer available to users within the tenant for which it was disabled.

**Licenses**: When you enable a service, we attempt to re-allocate licenses for the service as they were before being disabled, but within the limit of the licenses currently available for the organization. Therefore, it is possible that previous license allocations are not fully restored if insufficient licenses are available.

To enable or disable a service take the following steps:

1. Navigate to **Admin** and select the tenant in the panel on the left.
2. Select **Services**.

The **Services** page for the tenant opens, showing the services that are currently provisioned.
3. On the card of the service you want to remove, select the **More** icon and then select **Disable** or **Enable**, depending on the current status of the service.
4. If you are disabling the service, a confirmation dialog opens. Select **Disable** to proceed.
   :::note
   You cannot disable Orchestrator, Insights, Data Fabric, or Integration Service as multiple UiPath® products require these services to operate correctly. You can, however, hide services for users from the left rail by navigating to the [UI Customization](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-organization-settings#hiding-services) settings at organization level.
   :::

After a short period, a confirmation message appears at the top of the page and the service status changes on the **Services** page. **Disabled** appears on the card of each disabled service.

## Accessing services

Users can access services:

* from the **Admin > Tenants** page, by selecting a tenant name to show its services and then selecting a service.
* from the **Home** page, in the case of services that have widgets on this page, such as the Orchestrator service.
* from the left rail, by selecting the icon for a service.