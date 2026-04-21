---
title: "Changing the tenant region"
visible: true
slug: "changing-the-tenant-region"
---

Changing the region of a tenant is not a self-service operation. The process requires assistance from UiPath Support and includes a follow-up service data migration step that you perform in your organization.
:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

## Overview

Changing a tenant region is a two-step process:

1. You raise an SLA ticket with UiPath Support which updates the tenant region.
2. You migrate supported service data to the new region using the **Change region** option.

The **Change region** tenant option becomes available in your organization only after UiPath Support processes your ticket.

## Before you begin

Review the following information before requesting a tenant region change:

### Planning and scheduling

1. Depending on the services used by your tenant, the move may require multiple days to complete. Move date(s) are determined based on required version compatibility across regions.
2. A four-hour maintenance window is allocated for the region change. The average downtime is typically less than 30 minutes, but this can vary depending on tenant size. In rare cases, particularly for very large tenants, the move may take longer.
3. During the scheduled downtime window, the tenant is temporarily inaccessible.
4. Any running jobs are paused during the move and automatically resume after completion.
5. If you have scheduled or suspended robot jobs, temporarily disable them during the downtime window to help ensure a smooth migration.
6. Notify your cloud organization members in advance about the scheduled downtime window.

### Scope and impact

1. Changing a tenant’s region does not affect the region of other tenants or the organization.
2. To move multiple tenants, submit and schedule region changes individually for each tenant.
3. To schedule a move for the entire organization, follow the [Performing a cloud organization data move](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/managing-organization-settings#performing-a-cloud-organization-data-move) procedure.
4. For additional details about data behavior, see [Organization and tenant services data](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/data-residency-cloud#organization-and-tenant-services-data).

### Data considerations

1. The **Change tenant region** wizard migrates service data only. It does not change the tenant region itself.
2. Only supported services are available for migration.
3. Services that are not supported must be recreated or manually reconfigured in the new region.
4. Some services may require additional configuration after migration.
5. Robot execution logs are retained for 30 days. Export logs in advance if you need to preserve them. For details, see [Robot logs](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/about-logs#classic-logs-robot-logs).
6. If your processes are integrated with UiPath Apps, you must update references after the move. See [Replacing a process](https://docs.uipath.com/apps/automation-cloud/latest/user-guide/replacing-a-process-referenced-in-an-app) for guidance.
7. Insights can be moved to a new region. However, historical data backfilling is supported only within 30 days after moving Orchestrator. If Orchestrator is moved more than 30 days before Insights, Insights is moved without historical data, and only limited data is available after migration.

## Performing a tenant service data move

### Step 1: Request a tenant region change

1. [Open an SLA ticket](https://www.uipath.com/company/contact-us/cloud-platform-technical-support) and request the move to one of the [available regions](https://docs.uipath.com/overview-guide/docs/data-residency-cloud#tenant-and-service-regions)
2. Provide the following information:
   * Organization name
   * Tenant name
   * Current region
   * Target region
   * Business justification, if required

After the request is reviewed and approved, UiPath updates the tenant region. Once this backend operation is completed, the **Change tenant region** option becomes available for the tenant in your organization.

If the option is not visible, the Support request has not yet been completed.

### Step 2: Migrate service data to the new region

After Support updates the tenant region, you must migrate supported service data so that it aligns with the new region.

To migrate service data:

1. Go to **Admin**.
2. Select the tenant for which the region change was approved.
3. Select **Change tenant region**. The **Change tenant region** wizard opens. Follow the three steps in the **Change tenant region** wizard to proceed: select the region, select the downtime window, and confirm the details.
   1. From the **Tenant target region** dropdown, select the target region.
   2. Review the list of services available to the selected region.
      :::note
      Note that region availability and data move support vary by service. If a service cannot be scheduled for migration, contact UiPath Support.
      :::
   3. Select **Next**.
   4. Select a preferred downtime window from the provided options. This is the scheduled period during which the migration will occur. If you do not select a preferred window, a downtime window is automatically assigned.
   5. Select **Next** to continue.
   6. Review the details of the selected region and scheduled region downtime window. Confirm that the information is correct.
   7. Select **Schedule** to request the tenant service data move.
4. Once scheduled, the tenant’s region status changes to **Region change scheduled** on the tenant’s **Settings** page.

   !['Region change scheduled' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/427822)

You can select the **Region change scheduled** status to view details about the scheduled move.

   !['Scheduled data move details' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/428528)

After the region and service data move is executed, verify the tenant’s new region by checking the **Region** section in **Admin > Tenant > Settings**.

## Canceling a tenant service data move

If you scheduled the move by mistake or need to cancel for any reason before the move of any services starts, take the following steps:

1. Navigate to **Admin**.
2. Select the tenant for which you want to cancel the scheduled move.
3. Select **Region change scheduled**.
4. Select **Cancel request** in the **Scheduled data move** right panel.

If you need assistance with canceling your region change, contact [UiPath Support](https://www.uipath.com/company/contact-us/cloud-platform-technical-support).