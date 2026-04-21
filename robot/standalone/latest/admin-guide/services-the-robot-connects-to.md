---
title: "Configuring networking settings"
visible: true
slug: "services-the-robot-connects-to"
---

Executing a workflow implies robot operations such as downloading the automation package, checking licenses, or verifying certificates. To do that, the robot needs to connect to several services. For a successful execution, make sure to grant your robot access to the listed services:

## Outbound connections

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
   <th> <p> Hostname </p> </th>
   <th> <p> Protocol </p> </th>
   <th> <p> Port </p> </th>
   <th> <p> Application </p> </th>
   <th> <p> Usage </p> </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td> <p><code>cloud.uipath.com</code></p> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> https </p> </td>
   <td> <p> To access Automation Cloud Orchestrator. </p> </td>
  </tr>
  <tr>
   <td> <code>download.uipath.com</code> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> https </p> </td>
   <td> To download Studio or Robot MSI installers during automatic updates. </td>
  </tr>
  <tr>
   <td> <p><code>activate.uipath.com</code></p> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> https </p> </td>
   <td> <p> To access the licensing server, for checking the license status and verifing data in the license folder. </p> </td>
  </tr>
  <tr>
   <td> <p><code>jptk0*.proinity.net</code></p> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> https </p> </td>
   <td> <p> Hardened/offline images with Windows Update or Automatic Root Updates disabled. Environments where the Trusted Root store has been pruned by policy.In those cases, the Robot may reach out to validate the CA as UiPath describes. </p> </td>
  </tr>
  <tr>
   <td> <p><code>*.nuget.org</code></p> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> https </p> </td>
   <td> <p> To download the required activity dependencies. </p> </td>
  </tr>
  <tr>
   <td> <p><code>a23-*-*-*.deploy.static.akamaitechnologies.com</code></p> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 80 </p> </td>
   <td> <p> http </p> </td>
   <td> <p> To verify if the code signing certificate has been revoked. </p> </td>
  </tr>
  <tr>
   <td> <p><code>x1.i.lencr.org</code></p> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 80 </p> </td>
   <td> <p> http </p> </td>
   <td> <p> To verify whether the Let's Encrypt certificate authority has revoked the code signing certificate. </p> </td>
  </tr>
  <tr>
   <td> <p><code>*.service.signalr.net</code></p> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> https, wss </p> </td>
   <td> <p> To connect to the SignalR channels provided by Orchestrator. </p> </td>
  </tr>
  <tr>
   <td> <p><code>*.ingest.sentry.io</code></p> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> https </p> </td>
   <td> <p> Required by Assistant, to send application errors to Sentry. This helps tracking and solving the most common problems. </p> </td>
  </tr>
  <tr>
   <td> <p><code>dev.azure.com</code></p><p><code>pkgs.dev.azure.com</code></p><p><code>*.blob.core.windows.net</code></p> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> https </p> </td>
   <td> <p> To enable UiPath Robots to store and retrieve data using Azure storage services. </p> </td>
  </tr>
  <tr>
   <td> &nbsp; </td>
   <td> &nbsp; </td>
   <td> &nbsp; </td>
   <td> &nbsp; </td>
   <td> &nbsp; </td>
  </tr>
  <tr>
   <td> <p><code>gallery.uipath.com</code></p><p><code>marketplace.uipath.com</code></p><p><code>*.pkgs.visualstudio.com</code></p><p>Note: <code>gallery.uipath.com/api/v2</code> redirects to <code>uipath.pkgs.visualstudio.com</code></p></td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> https </p> </td>
   <td> <p> To access the Marketplace NuGet feed. </p> </td>
  </tr>
  <tr>
   <td> <p><code>dc.applicationinsights.azure.com</code></p><p><code>dc.applicationinsights.microsoft.com</code></p><p><code>dc.services.visualstudio.com</code></p><p><code>*.in.applicationinsights.azure.com</code></p> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> https </p> </td>
   <td> <p> To send telemetry data. </p> </td>
  </tr>
  <tr>
   <td> <p><code>asstoffalp.z6.web.core.windows.net</code></p> </td>
   <td> TCP </td>
   <td> 443 </td>
   <td> https </td>
   <td> <p> Required by Assistant, to load components for the Excel add-in. </p> </td>
  </tr>
  <tr>
   <td> <code>*.trafficmanager.net</code> </td>
   <td> <p> TCP </p> </td>
   <td> <p> 443 </p> </td>
   <td> <p> wss </p> </td>
   <td> Required by the <a href="https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/live-streaming-and-remote-control"> Live streaming </a> feature, to connect the robot and the browser. </td>
  </tr>
 </tbody>
</table>

## Outbound connections in JSON format

Copy the data in the JSON format and paste it in your network configuration file:

```
[
    "cloud.uipath.com",
    "download.uipath.com",
    "pkgs.dev.azure.com",
    "activate.uipath.com",
    "jptk0*.proinity.net",
    "*.nuget.org",
    "a23-*-*-*.deploy.static.akamaitechnologies.com",
    "x1.i.lencr.org",
    "*.service.signalr.net",
    "*.ingest.sentry.io",
    "dev.azure.com",
    "pkgs.dev.azure.com",
    "*.blob.core.windows.net",
    "gallery.uipath.com",
    "marketplace.uipath.com",
    "*.pkgs.visualstudio.com",
    "dc.applicationinsights.azure.com",
    "dc.applicationinsights.microsoft.com",
    "dc.services.visualstudio.com",
    "*.in.applicationinsights.azure.com",
    "asstoff1bp.z6.web.core.windows.net",
    "*.trafficmanager.net"
  ]
```