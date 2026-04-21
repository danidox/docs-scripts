---
title: "Manual migration"
visible: true
slug: "manual-migration"
---

This page outlines the manual steps to perform data migration from your on-premises Orchestrator tenants to Cloud Orchestrator services. This method requires that you manually recreate your on-premises configuration and entities in your cloud organization.
:::note
Feature availability depends on the cloud offering you use. For details, refer to the [feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

## Manually recreating your Orchestrator setup
:::note
You must perform the following operations in Orchestrator, as described in the table, and make sure that you have the required [permissions](https://docs.uipath.com/orchestrator/v0/docs/default-roles).
:::

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Step
    </p>
   </th>
   <th>
    <p>
     Operation
    </p>
   </th>
   <th>
    <p>
     Details
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d169931e45">
    <p>
     1
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/configuring-tenant-settings">
      Configure tenant settings
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    <p>
     On the
     <strong>
      General
     </strong>
     tab, adjust the time zone of the tenant, the language of the user interface for Orchestrator, and toggle the
     <strong>
      Modern Folders
     </strong>
     feature.
    </p>
    <p>
     On the
     <strong>
      Deployment
     </strong>
     tab, configure and secure the automation packages feeds.
    </p>
    <p>
     On the
     <strong>
      Mail
     </strong>
     tab, configure email settings.
    </p>
    <p>
     On the
     <strong>
      Scalability
     </strong>
     tab, specify if the Robot service should subscribe to Orchestrator's SignalR channels, and configure the transport protocols
                                 that work best for you.
    </p>
    <p>
     On the
     <strong>
      Non-Working Days
     </strong>
     tab, define a list of non-business days, per tenant, on which you may configure your schedules to not run.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     2
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     Configure alert subscription settings
    </p>
   </td>
   <td headers="d169931e51">
    <p>
     To receive alerts for a category, you need to have the corresponding permissions on that category as well.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     3
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-folders">
      Create folders
     </a>
     and subfolders, and assign users to them accordingly
    </p>
   </td>
   <td headers="d169931e51">
    <p>
     Perform this step if you need more folders.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     4
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-credential-stores">
      Add credential stores
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    <p>
     Cloud Orchestrator supports most third party stores.
    </p>
    <p>
     For a full list of supported credential stores, refer to
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-credential-stores">
      Credential stores
     </a>
     .
    </p>
    <p>
     For a list of unsupported credential stores, or custom secure store plugins, refer to
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/orchestrator-credentials-proxy-installation">
      Orchestrator Credentials Proxy
     </a>
     as a potential solution.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     5
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-assets-in-orchestrator">
      Create assets
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    &nbsp;
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     6
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/studio/standalone/latest/user-guide/about-publishing-automation-projects">
      Publish packages from Studio
     </a>
     or
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-packages#manually-uploading-packages-to-orchestrator">
      upload them manually
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    &nbsp;
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     7
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-libraries#manually-uploading-a-library-to-orchestrator">
      Upload libraries
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    <p>
     In Cloud Orchestrator, you can only publish libraries at service level. To share libraries between Orchestrator services,
                                 you can use a custom feed.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     8
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-triggers">
      Define triggers
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    &nbsp;
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     9
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-machines">
      Provision machines
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    &nbsp;
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     10
    </p>
   </td>
   <td headers="d169931e48">
    Depending on your cloud offering:
    <ul>
     <li>
      Create Robots in classic folders, or
     </li>
     <li>
      Manage Robots in modern folders
     </li>
    </ul>
   </td>
   <td headers="d169931e51">
    <ul>
     <li>
      In classic folders, Robots need to be added to
                                    environments.
     </li>
     <li>
      In modern folders, Robot settings are controlled at user level.
                                    Robots are automatically provisioned for users with access to
                                    the new modern folder.
     </li>
    </ul>
    <p>
     Environments are not used in the context of a modern folder.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     11
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-processes">
      Deploy processes
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    &nbsp;
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     12
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/action-center/automation-cloud/latest/user-guide/action-catalogs">
      Create action catalogs
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    &nbsp;
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     13
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-queues-in-orchestrator">
      Create queues
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    &nbsp;
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     14
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-webhooks">
      Create webhooks
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    <p>
     You can define webhooks at any point, depending on when you want to be notified during the migration.
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d169931e45">
    <p>
     15
    </p>
   </td>
   <td headers="d169931e48">
    <p>
     Disconnect your Robots from the on-premises instance and then
     <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/connecting-robots-to-orchestrator">
      connect each Robot to your Orchestrator service
     </a>
    </p>
   </td>
   <td headers="d169931e51">
    <p>
     Robots can be connected to only one source at a time. When a Robot is disconnected from the
                                 on-premises Orchestrator and connected to Cloud Orchestrator, it
                                 automatically consumes a new license from the cloud offering.
    </p>
   </td>
  </tr>
 </tbody>
</table>