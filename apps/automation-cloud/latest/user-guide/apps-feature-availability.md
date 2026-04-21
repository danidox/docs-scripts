---
title: "Apps feature availability"
visible: true
slug: "apps-feature-availability"
---

The following table compares the availability of Apps types, and corresponding features, across all UiPath cloud offerings: Automation Cloud and Test Cloud, Automation Cloud Public Sector and Test Cloud Public Sector, as well as Automation Cloud Dedicated and Test Cloud Dedicated. The table focuses exclusively on Apps functionality. Additional platform-level differences, such as product availability, are covered separately in the Automation Cloud and Test Cloud admin guides.

<table cellpadding="4" cellspacing="0">
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th> App type </th>
   <th> Capability </th>
   <th> Automation Cloud </th>
   <th> Automation Cloud Public Sector </th>
   <th> Automation Cloud Dedicated </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td rowspan="10"> <strong>Standalone apps</strong> Important: Creation of new standalone apps in App Studio is no longer supported. Existing standalone apps and app migrations continue to be supported. </td>
   <td> Availability </td>
   <td> ✅ (existing apps and migrations only; new creation disabled) </td>
   <td> ✅ (existing apps and migrations only; new creation disabled) </td>
   <td> ❌ </td>
  </tr>
  <tr>
   <td> Base URL </td>
   <td colspan="2"> <code>&#123;AutomationCloudURL}/&#123;organizationName}/apps_</code><sup> 1 </sup> </td>
   <td> N/A </td>
  </tr>
  <tr>
   <td> The location of building the app </td>
   <td> <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/using-app-studio#using-app-studio"> App Studio </a> </td>
   <td> <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/using-app-studio#using-app-studio"> App Studio </a> </td>
   <td> N/A </td>
  </tr>
  <tr>
   <td> App automation model </td>
   <td> <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/about-events-and-rules#about-events-and-rules"> Event-driven </a> (rules and events defined in the app) </td>
   <td> <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/about-events-and-rules#about-events-and-rules"> Event-driven </a> </td>
   <td> N/A </td>
  </tr>
  <tr>
   <td> Access to platform resources ( <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/referencing-an-entity-in-your-app#referencing-an-entity-in-your-app"> entity </a> , <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/connecting-your-app-to-an-orchestrator-tenant#referencing-a-process-from-orchestrator"> process </a> , <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/referencing-a-storage-bucket-from-orchestrator#referencing-a-storage-bucket-from-orchestrator"> storage bucket </a> , <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/referencing-a-queue-in-your-app#referencing-a-queue-in-your-app"> queue </a> , <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/adding-an-action-to-your-app#adding-an-action-to-your-app"> action </a> ) </td>
   <td> Added as app resources and used in app events </td>
   <td> Added as app resources and used in app events </td>
   <td> N/A </td>
  </tr>
  <tr>
   <td> <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/adding-a-connection-to-your-app"> Connections </a> </td>
   <td> ❌ <sup> 2 </sup> </td>
   <td> ❌ </td>
   <td> ❌ </td>
  </tr>
  <tr>
   <td> <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/text-to-app#using-a-text-prompt-to-generate-an-app"> Designing your app with Autopilot </a> </td>
   <td> ❌ </td>
   <td> ❌ </td>
   <td> N/A </td>
  </tr>
  <tr>
   <td> <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/adding-an-action-to-your-app#adding-an-action-to-your-app"> Action Center integration </a> </td>
   <td> ✅ </td>
   <td> ✅ </td>
   <td> N/A </td>
  </tr>
  <tr>
   <td> <a href="https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-logs#classic-logs"> Classic logs </a> </td>
   <td> ✅ </td>
   <td> ✅ </td>
   <td> N/A </td>
  </tr>
  <tr>
   <td> <a href="https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-logs#unified-logs"> Unified logs </a> </td>
   <td> ✅ </td>
   <td> ❌ </td>
   <td> N/A </td>
  </tr>
  <tr>
   <td rowspan="11"> <strong>RPA apps</strong> </td>
   <td> Availability </td>
   <td> ✅ </td>
   <td> ✅ </td>
   <td> ✅ </td>
  </tr>
  <tr>
   <td> Base URL </td>
   <td colspan="3"> <code>&#123;AutomationCloudURL}/&#123;organizationName}/studio_</code><sup> 3 </sup> </td>
  </tr>
  <tr>
   <td> The location of building the app </td>
   <td> <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/designing-app-projects"> Studio Web </a> </td>
   <td> <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/designing-app-projects"> Studio Web </a> </td>
   <td> <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/designing-app-projects"> Studio Web </a> </td>
  </tr>
  <tr>
   <td> Onboarded to <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/about-solutions"> Solutions project type </a> in Studio Web </td>
   <td> ✅ </td>
   <td> ✅ </td>
   <td> ✅ </td>
  </tr>
  <tr>
   <td> Automation model </td>
   <td> <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/designing-app-projects#adding-automations"> Workflow-driven </a> (event handlers are workflows) </td>
   <td> <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/designing-app-projects#adding-automations"> Workflow-driven </a> (event handlers are workflows) </td>
   <td> <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/designing-app-projects#adding-automations"> Workflow-driven </a> (event handlers are workflows) </td>
  </tr>
  <tr>
   <td> Access to platform resources ( <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/working-with-entities-in-an-app-project"> entity </a> , process, storage bucket, queue, <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/designing-an-action-app"> action </a> ) </td>
   <td> Through RPA workflows </td>
   <td> Through RPA workflows </td>
   <td> Through RPA workflows </td>
  </tr>
  <tr>
   <td> <a href="https://docs.uipath.com/apps/automation-cloud/latest/user-guide/adding-a-connection-to-your-app"> Connections </a> </td>
   <td> ✅ (through workflows) </td>
   <td> ✅ (through workflows) </td>
   <td> ✅ (through workflows) </td>
  </tr>
  <tr>
   <td> <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/designing-an-action-app"> Action Center integration </a> </td>
   <td> ✅ </td>
   <td> ✅ </td>
   <td> ✅ </td>
  </tr>
  <tr>
   <td> <a href="https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/designing-your-app-with-autopilot"> Designing your app with Autopilot </a> </td>
   <td> ✅ </td>
   <td> ✅ </td>
   <td> ❌ </td>
  </tr>
  <tr>
   <td> <a href="https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-logs#classic-logs"> Classic logs </a> </td>
   <td> ✅ </td>
   <td> ✅ </td>
   <td> ✅ </td>
  </tr>
  <tr>
   <td> <a href="https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-logs#unified-logs"> Unified logs </a> </td>
   <td> ✅ </td>
   <td> ❌ </td>
   <td> ❌ </td>
  </tr>
 </tbody>
</table>

<sup>1</sup>The access URLs for each UiPath cloud offering are the following:

* Automation Cloud and Test Cloud: `https://cloud.uipath.com/{organizationName}/apps_`
* Automation Cloud Public Sector and Test Cloud Public Sector: `https://govcloud.uipath.us/{organizationName}/apps_`
* Automation Cloud Dedicated and Test Cloud Dedicated: `https://<customURL>.dedicated.uipath.com/{organizationName}/apps_`

<sup>2</sup> Integrating connections was available as a public preview, but the capability was discontinued.

<sup>3</sup> The access URLs for each UiPath cloud offering are the following:

* Automation Cloud and Test Cloud: `https://cloud.uipath.com/{organizationName}/studio_`
* Automation Cloud Public Sector and Test Cloud Public Sector: `https://govcloud.uipath.us/{organizationName}/studio_`
* Automation Cloud Dedicated and Test Cloud Dedicated: `https://<customURL>.dedicated.uipath.com/{organizationName}/studio_`