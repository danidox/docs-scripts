---
title: "Managing tenants"
visible: true
slug: "managing-tenants"
---

:::tip
For examples on how you can use tenants to create separation of resources within your organization, refer to [Examples of platform modelling](https://docs.uipath.com/overview-guide/docs/platform-guidelines-for-partners#examples-of-platform-modelling).
:::

## Adding tenants
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

**Before you begin**: This feature is not available on the **Community** or **Free** Flex licensing plans. These organizations are limited to one tenant, which is created automatically. For the Flex **Pro Trial** users, all tenants are created in the region where the organization data resides. For the Flex **Pro** and **Enterprise** customers, you can create new tenants in your preferred regions.

To create a new tenant, take the following steps:

1. Navigate to **Admin** in the Test Cloud portal.
2. In the **Tenants** view, select the **Plus** icon. The **Create new tenant** process starts with three steps to follow.
3. On the **General** step, provide the following information:
   1. Enter a name for your tenant in the **Name** field.

You can enter up to 32 alphabetical or numeric characters, starting with a letter. No spaces or special characters are allowed.

      :::important
      You can change the tenant name later, but there are consequences. Refer to [Changing the tenant name](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-tenants#changing-the-tenant-name-or-color).
      :::
   2. (Optional) Select a color from the **Color** picker to identify your tenant in the header when operating within that tenant.
   3. Select a tenant type from the **Environment type** section.

By selecting the environment type, you provide the specific configuration and infrastructure setup required for running and testing your automations.

You can choose from three types of environments:

      * **Production** tenants allow the latest versions of software, products, or updates to be pushed to users live.
      * **Development** tenants are used for development purposes without impacting live or operational tenants.
      * **Staging** tenants are used for testing purposes without impacting live or operational tenants, including canary environments.
        :::note
        If you want to independently run and test automations with the latest features, select **Use as a canary environment**. For more information, refer to [Using a canary environment](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-tenants#using-a-canary-tenant). If you already have a canary environment, even if it is currently disabled, you cannot select the checkbox to create another canary environment.
        :::

        ![Adding a new tenant](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/616561)
4. From the **Region** dropdown, choose the region for hosting your [service data](https://docs.uipath.com/overview-guide/docs/data-residency-cloud#service-data) for your tenant.
   :::important
   You cannot change the tenant region yourself after you create the tenant. If you need to change it later, you have to open a [support ticket](https://www.uipath.com/company/contact-us/cloud-platform-technical-support). When a tenant and associated data are moved to a new region, the tenant ID and folder ID are changed. You have to update your projects with the new tenant and folder IDs.
   :::
5. Select **Next** to proceed to the **Add services** step.
6. On the **Add services** step, select the checkboxes for the services that you want to make available within your new tenant.

The Orchestrator service is mandatory. Other services are only available if you have free licenses for them.

   :::note
   Services available in regions different from the chosen tenant region are labeled accordingly with the region in which they are hosted. For more information, refer to [Data residency](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/data-residency-).
   :::
7. Select **Next** to proceed to the **License allocation** step.

On the **License allocation** step, you can observe the available number of licenses for each type that you can allocate to your new tenant. If you want to keep some of the available licenses for other tenants, you can allocate a lower number of licenses to your new tenant from each of the available license types.
8. Select **Create** to close the wizard and create the tenant.

The new tenant is added to the **Tenants** panel and the tenant picker.

Production type tenants can be identified through the !['Production tenant' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/541698) icon. Non-production type tenants can be identified through the !['Non-production tenant' icon](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/541706) icon.

To be able to work in the tenant, you or a service administrator must assign roles and licenses for the services in the new tenant to users. For more information, refer to:

* [About accounts and groups](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-accounts#about-accounts-and-groups)
* [Assigning user licenses](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/allocating-user-licenses#assigning-user-licenses)

### Using a canary tenant

  !['Enterprise' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/449555)

You can add a canary tenant to your organization to view and test upcoming changes before they reach your other tenants. The canary tenant serves as an isolated medium that uses your current setup where you can check on the impact that upcoming changes have within the context of your current organization.

With a canary tenant, you can:

* view and test enterprise-only features before they reach enterprise environments
* test and run the same automations that you use in production.
:::important
* Do not use the canary tenant for production.
* This feature is a medium made available to you for testing purposes only and does not benefit from the same enterprise commitments
as your other tenants.
* The uptime guarantee offered by your enterprise plan does not apply to the canary tenant.
* While we encourage reporting any potential issues you encounter within the canary tenant, please note that we will address
them on a best-effort basis only.
:::

#### Early access window

The canary tenant receives updates to **enterprise functionality** for all of the supported services as soon as they are announced in the release notes, while your other tenants receive them at least 3 days later.

#### Included services

Only the certain UiPath® cloud services are available to be provisioned in a canary tenant, as described in the following table:

| Service name | Notes | Release notes |
| --- | --- | --- |
| **Orchestrator** | Data retention for Orchestrator within the canary tenant is reduced to the thresholds for community plans. | [Orchestrator release notes](https://docs.uipath.com/orchestrator/automation-cloud/latest/release-notes/release-notes-2022) |

If a service is not listed in the table, then it does not receive early updates in the canary tenant.
:::note
To provision a service in your canary tenant, you need to have licenses for that service.
:::

#### Data residency

The canary tenant and its [service data](https://docs.uipath.com/overview-guide/docs/data-residency-cloud#organization-data-and-service-data) is always hosted in the European Union (Europe) region and you cannot choose a different region.

Make sure that [Community outbound IP addresses](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/orchestrator-outbound-ip-addresses#community-users) are allowed through the firewall for canary tenants to work properly.

#### Tips

To make the most of your canary tenant, we recommend setting it up in the same way as your production tenants. This includes replicating the same:

* tenant settings in UiPath Orchestrator
* service-level settings for each of the services you provisioned in the canary tenant
* service-level roles and user licenses for your users
* automations in Orchestrator - You can use the [UiPath Orchestrator Manager](https://marketplace.uipath.com/listings/orchestrator-manager) to copy data from one of your tenants to the canary tenant.

## Editing tenants

When editing tenant settings, you can change the name, color, enable, disable, or delete the tenant.

### Changing the tenant name or color
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

1. Go to **Admin** and select the tenant in the panel on the left.
2. Select **Settings**.

The **Settings** page for the selected tenant opens.
3. Edit the tenant name if needed.
   :::important
   Changing a tenant's name disconnects your Robots and Mobile Orchestrator users, and invalidates any pending user invites. Refer to **Impact of Changing Tenant Names**.
   :::
4. From the list to the right of the name, select a different header color for the tenant, if needed.
5. Select **Save Changes** at the bottom of the page.

A confirmation message appears in the top right of the screen.

**Impact of changing tenant names**

Changing the name of any of your tenants greatly impacts your previous UiPath service configurations:

* Robots configured at Orchestrator services level are disconnected. [Reconnect your robots](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/connecting-robots-to-orchestrator), entering the new URLs.
* Service URLs previously bookmarked don't work anymore. Send your users the new URLs.
* Mobile Orchestrator users are disconnected. Send them the new service URLs to connect again.
* User invites sent before the change are not valid anymore. [Send new invites](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-account-groups#inviting-users) for your colleagues who haven’t joined yet.

### Enabling or disabling a tenant

Disabled tenants remain visible to organization administrators in the **Tenants** panel of the **Admin** page, but the tenant and its services are no longer available to users. Also, the licenses that were allocated to the tenant are released and returned to the organization's pool of licenses.

All data for the services is kept. You can later enable the tenant to access its services again.

1. Go to **Admin** and select the tenant in the panel on the left.
2. Select **Settings**.

The **Settings** page for the selected tenant opens.
3. Under **Disable Tenant**, select **Enable** or **Disable**, depending on the current state of the tenant.

A warning dialog opens.
4. In the dialog, select **Enable** or **Disable** to proceed.

A loading icon is shown next to the tenant in the **Tenants** panel on the left while the change is being processed.

After the icon disappears:

* If you disabled the tenant, **Disabled** appears to its right and the tenant and its services are no longer available to users.
* If you enabled the tenant, it is now restored as it was before being disabled. All licenses that it used before are also re-allocated if they were available in the organization pool. The tenant and its services are now available for use.

### Deleting a tenant

When deleting a tenant, you remove the tenant from your organization and also delete all of its services and any service data.

After deleting a tenant, all its licenses are freed up and available for you to allocate to other tenants.
:::note
If any processes are being executed in the tenant's Orchestrator service, you cannot delete the tenant.
:::

1. Go to **Admin** and select the tenant in the panel on the left.
2. Select **Settings**.

The **Settings** page for the selected tenant opens.
3. Under **Delete permanently**, select **Delete**, depending on the current state of the tenant.

The **Delete Tenant** dialog opens.
4. In the field, enter the tenant name, exactly as it is shown, including the letter case, and then select **Delete**.

A loading icon is displayed next to the tenant in the Tenants panel while the deletion is in progress. When complete, the tenant is removed from the Tenants panel.

### ALM endpoint

   ![SAP and UiPath](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/432571) To enable reliable log transfer from UiPath to SAP, you need to configure the **Application Lifecycle Management (ALM) endpoints** in UiPath.

1. Navigate to the Admin page in Automation Cloud.
2. Select your SAP tenant from the list.
3. Select **Settings**.
4. Go to the **ALM endpoint** tab.

Figure 1. ALM endpoint tab

   ![Screenshot with the ALM endpoint tab from the tenant administration page.](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/575434)
5. Fill in the needed parameters for the ALM endpoints.
   1. **Endpoint**: the base URL of the SAP Cloud ALM API.
   2. **Client ID**: the client identifier used to retrieve the authentication token.
   3. **Client Secret**: the secret key associated with the client ID for token generation.
   4. **Service ID**: the service identifier assigned to your UiPath tenant in SAP.
   5. **URL**: the URL endpoint used to obtain the authentication token.

## Editing tenant licenses
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

In **Admin > Tenant > Licenses**, you can view information about the licenses currently allocated to each tenant.

To change the license quantities, select **Edit allocation** in the top right corner.

For more information, refer to [Allocating licenses to tenants](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/allocating-licenses-to-tenants#assigning-licenses-to-tenants).

## The Autopilot for Everyone tenant card
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

To install Autopilot for Everyone without organization-level administrative rights, access the tenant-level dedicated card, then follow the installation steps.

The card is displayed when you go to the Admin section of your organization and select the tenant where you want to install Autopilot for Everyone. Once you select the card, the AAutopilot for Everyone installation page opens, with the tenant preselected by default.

### Known issues

* The **Tenant Admin** role does not explicitly include permissions to access Autopilot for Everyone. This may cause confusion, as your effective rights extend beyond those defined in the selected role. As a result, you may see the Autopilot for Everyone card even if it is not explicitly enabled through role settings.
* Custom roles can install Autopilot for Everyone through the card, even if their definitions do not include related permissions. This may also cause confusion, as users might see or interact with the card unintentionally.
* The Autopilot for Everyone card is displayed for all tenants in the organization. Accessing the card and navigating through tenants may cause a display of errors, because of missing permissions.