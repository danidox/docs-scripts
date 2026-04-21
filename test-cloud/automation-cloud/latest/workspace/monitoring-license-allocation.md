---
title: "Monitoring license allocation"
visible: true
slug: "monitoring-license-allocation"
---

:::note
Feature availability depends on the cloud offering you use. For details, refer to the [feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

## From the Home page

The homepage displays license allocation at the organization level.

Check the **License Allocation** section to view the number of allocated licenses out of the total number of purchased licenses in your organization. Switch between the available tabs to change the displayed license information per license type.

!['License allocation' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/30621)

## From the Licenses page

You can view license allocation details from the platform-level **Licenses** page, for either the entire organization, or just one tenant:

* For the entire organization, access **Admin** > organization > **Licenses**.
* For a particular tenant, access **Admin** > tenant > **Licenses**.

The **Licenses** page displays the number of all purchased licenses in your organization. Switch between these tabs to view license information per license type:

* **Users** - displays user licenses.
* **Robots & services** - displays service capacity items, such as runtimes, Data Fabric units, and Computer Vision licenses.
* **Consumables** - displays licensed consumption units, such as AI Units, Robot Units, and Integration Service API calls.

If a license type is not displayed, it means there are 0 licenses of that type purchased for your organization.

### The Users and the Robots & services tabs

Hover over the progress bar on the **Users** and **Robots & services** tabs to view the number of allocated licenses out of the total number of purchased licenses in your organization.

### The Consumables tab

Select the cards on the **Consumables** tab to view details about how your organization's or tenant's service consumption units are used per month or per year.

The following table describes what you can expect to notice depending on the level:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-0FDFC14A-1652-41C5-9F86-063FBDD98F3A__TABLE_PFQ_1PV_QBC" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     <strong>
      Level
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Information
     </strong>
    </p>
   </th>
   <th>
    <p>
     <strong>
      Further details
     </strong>
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d64097e136" rowspan="7">
    <p>
     <strong>
      ORGANIZATION
     </strong>
    </p>
   </td>
   <td headers="d64097e143">
    <p>
     The total number of units in the account
    </p>
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      Their start
                                          date
     </li>
     <li>
      Their
                                          expiration date
     </li>
     <li>
      If the units
                                          reset monthly, their reset date
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    <p>
     The total number of consumed units vs. the total number of
                                       available units
    </p>
   </td>
   <td headers="d64097e150">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    <p>
     Usage details for Platform Units
    </p>
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      The total
                                          number of consumed units, counted from the start date.
     </li>
    </ul>
    <ul>
     <li>
      The number of
                                          units consumed each month, counted over the past 12
                                          months.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    <p>
     Usage details for AI units
     <sup>
      1
     </sup>
    </p>
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      The total
                                          number of consumed units, counted from the start date, and
                                          split per service which registers the consumption of such
                                          units.
     </li>
    </ul>
    <ul>
     <li>
      The number of
                                          units consumed each month, counted over the past 12 months,
                                          and split per service which registers the consumption of
                                          such units.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    <p>
     Usage details for robot units
    </p>
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      The number of
                                          units consumed each month, counted over the past 12 months,
                                          and split between Serverless and VM robots.
     </li>
     <li>
      The number of
                                          units consumed during the current month by Serverless
                                          robots.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    <p>
     Usage details for Integration Service API calls
    </p>
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      <p>
       The number of calls consumed each month, counted over the
                                             past 12 months, and split based on their type: API calls
                                             bundled with license or API calls purchased as a
                                             dedicated bundle.
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    <p>
     Usage details for agent units
    </p>
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      The total
                                          number of allocated and consumed units per tenant, counted
                                          from the start date.
     </li>
     <li>
      If no agent
                                          units are allocated to a tenant, consumption information is
                                          not displayed in the tenant list.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d64097e136" rowspan="6">
    <p>
     <strong>
      TENANT
     </strong>
    </p>
   </td>
   <td headers="d64097e143">
    <p>
     The total number of units allocated to the selected tenant
    </p>
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      Their start
                                          date
     </li>
     <li>
      Their
                                          expiration date
     </li>
     <li>
      If the units
                                          reset monthly, their reset date
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    <p>
     The total number of consumed units vs. the total number of
                                       available units
    </p>
   </td>
   <td headers="d64097e150">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    <p>
     Usage details for Platform Units
    </p>
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      The total
                                          number of consumed units, counted from the start date.
     </li>
    </ul>
    <ul>
     <li>
      The number of
                                          units consumed each month, counted over the past 12
                                          months.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    <p>
     Usage details for AI units
     <sup>
      1
     </sup>
    </p>
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      The total
                                          number of consumed units, counted from the start date, and
                                          split per service which registers the consumption of such
                                          units.
     </li>
    </ul>
    <ul>
     <li>
      The number of
                                          units consumed each month, counted over the past 12 months,
                                          and split per service which registers the consumption of
                                          such units.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    <p>
     Usage details for robot units
    </p>
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      The number of
                                          units consumed each month, counted over the past 12 months,
                                          and split between Serverless and VM robots.
     </li>
     <li>
      The number of
                                          units consumed during the current month by Serverless
                                          robots.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d64097e143">
    Usage details for agent
                                    units
   </td>
   <td headers="d64097e150">
    <ul>
     <li>
      The total
                                          number of consumed units, counted from the start date.
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

<sup>1</sup> You can view a detailed breakdown of AI units consumption across various products, projects, and hardware by checking out the [AI units consumption overview](https://docs.uipath.com/insights/automation-cloud/latest/user-guide/ai-units-consumption-overview) Insights dashboard.