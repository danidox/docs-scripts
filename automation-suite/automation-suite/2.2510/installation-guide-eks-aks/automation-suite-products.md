---
title: "Automation Suite products"
visible: true
slug: "automation-suite-products"
---

Automation Suite lets you manage your self-hosted UiPath® platform as one product. However, not all of our self-hosted products are part of Automation Suite.

The following products are part of the Automation Suite bundle. You have the ability to enable or disable products at any time after their installation.

* [Action Center](https://docs.uipath.com/action-center/automation-suite/2.2510) (Actions and Processes)
* [AI Center](https://docs.uipath.com/ai-center/automation-suite/2.2510) (AI Center connected to an external Orchestrator not supported)
  + [AI Computer Vision](https://docs.uipath.com/ai-computer-vision/automation-suite/2.2510/user-guide/introduction)
* [AI Trust Layer](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/about-ai-trust-layer)
  + LLM Gateway
  + LLM Observability
  + [Context Grounding](https://docs.uipath.com/automation-suite/automation-suite/2.2510/admin-guide/about-context-grounding) (also referred to Enterprise Context Service, or ECS)
* [Apps](https://docs.uipath.com/apps/automation-suite/2.2510)
* [Automation Hub](https://docs.uipath.com/automation-hub/automation-suite/2.2510)
* [Automation Ops](https://docs.uipath.com/automation-ops/automation-suite/2.2510)
* [Autopilot for Everyone](https://docs.uipath.com/autopilot/other/latest/user-guide/about-autopilot-for-everyone)
* [Data Service](https://docs.uipath.com/data-service/automation-suite/2.2510)
* [Document Understanding](https://docs.uipath.com/document-understanding/automation-suite/2.2510)
* [Insights](https://docs.uipath.com/insights/automation-suite/2.2510)
* [Integration Service](https://docs.uipath.com/integration-service/automation-suite/2.2510)
  + [GenAI activities](https://docs.uipath.com/integration-service/automation-suite/2.2510/user-guide/uipath-uipath-airdk)
* [Orchestrator](https://docs.uipath.com/orchestrator/automation-suite/2.2510)
  + [Automation Suite Robots](https://docs.uipath.com/orchestrator/automation-suite/2.2510/user-guide/about-automation-suite-robots)
  + [Coded agents](https://docs.uipath.com/orchestrator/automation-suite/2.2510/user-guide/managing-processes#deploying-agents)
* [Process Mining](https://docs.uipath.com/process-mining/automation-suite/2.2510)
* [Solutions](https://docs.uipath.com/solutions-management/automation-suite/2.2510/user-guide/solutions-management-overview)
* [Studio Web](https://docs.uipath.com/studio-web/automation-suite/2.2510)
* [Test Manager](https://docs.uipath.com/test-manager/automation-suite/2.2510)

Some Automation Suite products have additional dependencies on each other, as listed in the following table:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Product
   </th>
   <th>
    Dependency
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d18158e140">
    AI Computer Vision
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      AI Center
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    Apps
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      Data Service (for the Data Service integration)
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    Automation Hub
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      Orchestrator (for Automation Store, Studio, and Assistant integrations)
     </li>
    </ul>
    Note: As Task Mining is not available in Automation Suite, the Automation Hub integration with Task Mining is also not available.
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    Automation Suite Robots
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      Orchestrator
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    Document Understanding
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      AI Center for AI Center-based projects
     </li>
     <li>
      No dependencies for Document Understanding modern projects
     </li>
     <li>
      Action Center (for human-in-the-loop validation)
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    Integration Service
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      Automation Ops
     </li>
     <li>
      Orchestrator
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    Process Mining
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      Automation Hub (for sending ideas to Automation Hub, and for uploading app templates in Process Mining)
     </li>
     <li>
      Notification Service (for Export)
     </li>
     <li>
      Orchestrator (for Automation integration)
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    Studio Web
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      Automation Ops
     </li>
     <li>
      Automation Suite Robots
      <sup>
       *
      </sup>
     </li>
     <li>
      Data Service
     </li>
     <li>
      Document Understanding (for Document Understanding activities)
     </li>
     <li>
      Integration Service
     </li>
     <li>
      Orchestrator
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    LLM Gateway
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      Platform
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    LLM Observability
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      Platform
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    Context Grounding (ECS)
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      LLM Gateway
     </li>
     <li>
      Orchestrator
     </li>
     <li>
      Platform
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    Autopilot for Everyone
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      Platform
     </li>
     <li>
      Orchestrator
     </li>
     <li>
      Automation Ops
     </li>
     <li>
      ECS
     </li>
     <li>
      Solutions
     </li>
     <li>
      Integration Service
     </li>
     <li>
      LLM Gateway
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d18158e140">
    Solutions
   </td>
   <td headers="d18158e142">
    <ul>
     <li>
      Platform
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

* Running Studio Web without Automation Suite Robots is possible but not recommended, as the experience of using Studio Web will be affected.