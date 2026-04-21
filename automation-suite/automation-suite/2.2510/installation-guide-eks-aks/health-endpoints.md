---
title: "Health endpoints"
visible: true
slug: "health-endpoints"
---

To effectively monitor the health of your Automation Suite services, you can use the health endpoints available in this section. These endpoints allow you to quickly verify if a service is operating correctly.

The following table lists the Automation Suite products and services and their respective health endpoints.

Expand Table

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Service
   </th>
   <th>
    Health endpoint(s)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d74668e24">
    Platform
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/pap_/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/pap_/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/pdp_/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/identity_/.well-known/openid-configuration
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/identity_/web/
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/lease_/health/
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/license_/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/organization_/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/portal_/portal/shallow/healthStatus
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/audit_/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/resourcecatalog_/health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Action Center
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/actions_/
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/bupproxyservice_/health/ready
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/processes_/
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    AI Center
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/aifabric_/ai-app
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/aifabric_/ai-deployer/actuator/health/ready
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/aifabric_/ai-trainer/actuator/health/ready
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/aifabric_/ai-pkgmanager/actuator/health/ready
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/aifabric_/ai-helper/actuator/health/ready
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/aistorage_/health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Apps
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/&lt;org-name&gt;/apps_/default/api/v1/default/system-health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Autopilot for Everyone
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/autopilotforeveryone_/api/health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Automation Hub
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/automationhub_/fd-api/v1/ping
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/automationstore_/fd-api/v1/ping
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Solutions
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/automationsolutions_/health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Data Service
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/dataservice_/api/HealthCheck/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/dataservice_/assets
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Document Understanding
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/du_/api/documentmanager/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/du_/api/storage/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/du_/api/eventservice/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/du_/metering/alive
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/du_/ocr/info/ready
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/du_/extended-ocr/ready
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/du_/classify/MLclassification/info/ready
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/du_/svc/formextractor/info
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/du_/svc/intelligentkeywords/info
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    ECS
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/ecs_/health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Insights
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/insights_/health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Integration Services
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/connections_/schedulerstatus
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/connections_/dispatcherstatus
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/elements_/v1/elements/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/elements_/elements/api-v2/tickle
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    LLM Gateway
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/llmgateway_/health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    LLM Observability
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/llmops_/health
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/llmops_/tracesruntime/health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Notification Service
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/notificationservice_/notificationserviceapi/health/readiness
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/notificationservice_/usersubscriptionservice/health/readiness
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/notificationservice_/publishermetaservice/health/readiness
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Orchestrator
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/orchestrator_/api/health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Robotube
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/robotube_/healthz
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Studio Governance
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/roboticsops_/api/health
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Studio Web
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/studio_/backend/healthz
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/studio_/typecache/healthz/readiness
      </code>
     </li>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/studio_/
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d74668e24">
    Test Manager
   </td>
   <td headers="d74668e26">
    <ul>
     <li>
      <code>
       https://&lt;automation-suite-fqdn&gt;/testmanager_/api/health/live
      </code>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

## Checking service health

To check the health of a specific service, send a request to its corresponding endpoint, as show in the following example.

```
curl -kiso /dev/null -w "%{http_code}" https://<automation-suite-fqdn>/orchestrator_/api/health
```

A successful response with an HTTP status code 200 indicates that the service is healthy.