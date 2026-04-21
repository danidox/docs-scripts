---
title: "Managing tenant and service visibility"
visible: true
slug: "managing-tenant-and-service-visibility"
---

:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

## Overview

The Tenant and service visibility capability ensures that non-admin users can see only:

* The tenants that contain services they have permission to access.
* The services for which they have explicit permissions.

This capability is particularly useful when you need to restrict users from viewing tenants or services outside their scope.

### How it works

The behavior follows two principles:

* If a user has permission to a service, they can see that service.
* If that service exists in a tenant, the user can see that tenant.

If a user does not have permissions to any available services within a tenant, that tenant is hidden from them.

### Scope of the feature

#### Available services

Tenant and service visibility applies to the following services:

* Actions
* Agents
* Apps*
* Automation Ops*
* Data Fabric
* Document Understanding
* Insights
* Maestro*
* Orchestrator
* Processes
* Task Mining
* Test Manager
* Integration Service (via Orchestrator permissions)
* Special considerations apply. See **Organization-level services** below.
  ![Enabling services at the tenant-level](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/645146)

#### Unavailable services

Tenant service and visibility does not apply to the following services:

* Automation Hub
* Process Mining
* IXP
* AI Center

If any of these unavailable services are enabled in a tenant, that tenant may become visible to users even if they do not have permissions to use those services.

If users attempt to access such services without permission, they receive an error.

### Organization-level services

Tenant service and visibility does not work for services provisioned at the **organization level**, including:

* Apps
* Agents
* Automation Ops
* Maestro
* Studio Web

Because these services do not have strictly tenant-level permissions, but organization-level permissions, their presence can affect tenant visibility behavior.

Even if users do not have permissions within a tenant, the tenant may still appear visible if it contains one of these services.

#### Workaround for unavailable and organization-level services

To ensure proper behavior when unavailable services are enabled, or organization-level services are provisioned, you must hide those services from **Admin** > **Settings** > **Advanced** > **UI Customization**, using the [Hiding services](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-organization-settings#hiding-services) capability.

Organization admins continue to see services hidden at the organization level and can share the direct service URL with non-admin users who require access.
:::note
* If these services remain visible in the product launcher, tenants containing
them may become visible to users. This happens even when users do not have permissions specific to these services.
:::

### Known limitations

#### Feature not visible as a UI item

Managing tenant and service visibility is not displayed as a UI item that can be toggled on or off. The feature can be triggered in the existing services menu by changing a user's permission in Orchestrator, or based on settings you make in the existing organization by navigating to [Enabling or disabling services](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-services#enabling-or-disabling-services).

#### Managing visibility for Integration Service, Actions and Processes is done via Orchestrator permissions

You can control Integration Service, Actions and Processes visibility via Orchestrator permissions. If a user has any permission in Orchestrator, they can view and use Integration Service, Actions, or Processes.
:::note
The Orchestrator level does not offer granular permission that determines user access to the Integration Service, Actions, or Processes. The workaround for this issue is to use the [Advanced settings](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-organization-settings#hiding-unused-services) from the tenant level to hide the service for non admin users.
:::

## Setting up a test scenario

The following example demonstrates how to validate tenant and service visibility. If you already have an existing tenant and permissions for available services, you can skip to [Checking the setup for tenant and service visibility](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-tenant-and-service-visibility#validating-tenant-and-service-visibility).

1. [Create two tenants](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-tenants#adding-tenants):
   1. **Production**
   2. **Testing**

      !['Create two tenants example' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/397927)
2. [Create a group](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-accounts-and-groups#adding-groups) named **UAT Users**.
3. In the **Production** tenant, ensure that the **UAT Users** group does not have permissions in any service. As an example, for Document Understanding, navigate to **Manage Access** and check that the **UAT Users** group does not have a role assigned.
   !['Manage access' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/397938)
4. In the **Testing** tenant, assign roles and permissions to **UAT Users** group for selected services (such as Orchestrator, Document Understanding, Insights, etc.). For example, for Document Understanding, navigate to **Manage Access** and assign a role to the **UAT Users** group.
   !['Role assignment' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/398732)

## Validating tenant and service visibility

The following steps and scenarios serve as examples on how to validate the setup for tenant and service visibility. If you already have an existing setup, you can check tenant and service visibility using your own group and tenant(s).

### Scenario 1: Service visibility in the product launcher

The following scenario describes how service visibility in the left rail operates based on user permissions.

1. Follow the [Setup to test tenant and service trimming](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-tenant-and-service-visibility#setting-up-a-test-scenario) steps, where UAT Users group has permissions only in **Testing** tenant.
2. Log in as a user from the **UAT Users** group.
3. Inspect the homepage and product launcher. **Expected result**: On the homepage, the user only sees the **Testing** tenant, not the **Production** tenant, because the users from the **UAT Users** group only have access to services from the **Testing** tenant. When the **Testing** tenant is selected, the user sees the services they have access to in the product launcher.
   :::note
   If the user has permissions for only one tenant, that tenant name does not appear on the homepage.
   :::
:::note
:::

   ![docs image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/639006)

### Scenario 2: Tenant visibility inside a service (based on service permissions)

The following scenario describes how tenant visibility at service level operates based on service permissions.

1. Follow the [Setup to test tenant and service trimming](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-tenant-and-service-visibility#setting-up-a-test-scenario) steps, where UAT Users group has permissions only in **Testing** tenant.
2. Log in as a **UAT Users** group member, select an enabled service from the product launcher (for example, Document Understanding), then open the tenant picker.

**Expected result**: The user cannot view the tenant picker anymore because they only have permissions to view enabled services in the **Testing** tenant, and not the **Production** tenant.
   !['Welcome to Document Understanding' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/397977)

### Scenario 3: Tenant visibility based on service availability

The following scenario describes how tenant visibility at service level operates based on service availability.

1. Follow the [Setup to test tenant and service trimming](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-tenant-and-service-visibility#setting-up-a-test-scenario) steps, where UAT Users group has permissions only in the **Testing** tenant.
2. Log in as an organization admin with full rights.
3. [Disable or enable the service](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/managing-services#enabling-or-disabling-services).
4. Log in as a user from the **UAT Users** group. Notice that you can only view the enabled services in the left rail or for which you have permissions in that particular tenant.
5. Check what the user sees in the tenant picker.

## FAQs

* **How long will it take for the tenant visibility to take effect after the role assignment changes in the service?**: It can take up to 30 minutes for direct role assignment changes and up to 1 hour for group membership, based permissions changes.
* **Will this feature work also with UiPath Assistant?**: Yes, but only if you have installed version 2023.4 or higher of UiPath Assistant.
* **Where can I view this feature in the user interface?** :The enhanced access control for tenants and services is not visible as a UI item that can be toggled on or off. The feature is triggered based on settings you make in the existing cloud organization.
* **Would this feature affect my data?**: The feature works with the visibility of the data and features of the users. It does not affect or can cause any data loss.