---
title: "Configuring the firewall for Automation Cloud
            Dedicated"
visible: true
slug: "configuring-the-firewall-for-dedicated"
---

For general network configuration and firewall information, refer to [Configuring the firewall](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-firewall#configuring-the-firewall)

## Automation Cloud Dedicated Portal

Allow these domains used by Automation Cloud Dedicated Portal:
:::important
If you use Azure buckets, they must not be located in the tenant's region or in the failover region.
:::

### Domains

| Scenario | Domains |
| --- | --- |
| Sign in with basic authentication | `https://<customURL>.dedicated.uipath.com`  `https://sandbox.stg.dedicated.uipath.com`  `https://platform-cdn.uipath.com` |
| Sign in with Azure Active Directory (Azure AD) | `https://aadcdn.msftauth.net``https://<customURL>.dedicated.uipath.com` `https://sandbox.stg.dedicated.uipath.com` `https://login.microsoftonline.com` |
| Sign in with UiPath Assistant (basic email) | `*-signalr.service.signalr.net` For events related to signing in with basic authentication:  `https://<customURL>.dedicated.uipath.com`  `https://sandbox.stg.dedicated.uipath.com` `https://platform-cdn.uipath.com` |
| Sign in with UiPath Studio (basic email) | `https://api.nuget.org``*-signalr.service.signalr.net``https://gallery.uipath.com``https://pkgs.dev.azure.com` For events related to signing in with basic authentication:  `https://<customURL>.dedicated.uipath.com`  `https://sandbox.stg.dedicated.uipath.com` `https://platform-cdn.uipath.com` |
| Static assets: Fonts, Styling and CDN hosted scripts | Fonts: `https://use.typekit.net``https://fonts.gstatic.com``https://platform-cdn.uipath.com` Images: `https://s.gravatar.com``https://secure.gravatar.com``https://*.wp.com``https://*.googleusercontent.com``https://i.ytimg.com``https://platform-cdn.uipath.com` CSS: `https://fonts.googleapis.com/css``https://use.typekit.net``https://p.typekit.net``https://platform-cdn.uipath.com` Scripts: `https://primer.typekit.net``https://use.typekit.net``https://platform-cdn.uipath.com` |

### Outbound Robot connections

During the workflow execution, the Robot connects to different services to download required automation packages, check licenses, verify certificates, and more.

The following table lists the outbound connections that must be allowed:

| Hostname | Purpose |
| --- | --- |
| `https://<customURL>.dedicated.uipath.com`  `https://sandbox.stg.dedicated.uipath.com` | For Automation Cloud Dedicated Orchestrator. |
| `download.uipath.com` | To download Studio or Robot MSI installers during automatic updates. |
| `pkgs.dev.azure.com`  `uipathpackages.myget.org` | The Robot downloads the required activity packages. |
| `*.vo.msecnd.net` | Azure CDN, used by Myget for distributing files |
| `activate.uipath.com` | Licensing Server. If we block this service then UiPath® is not able to check the license status and verify the data in the license folder. |
| `jptk0*.proinity.net` | The Robot validates the root certification authority of the code signing certificate. Please notice that this happens only if the root certification authority is not already in the Windows Certificate Store. |
| `*.nuget.org` | The Robot downloads the required activity dependencies. |
| `a23-*-*-*.deploy.static.akamaitechnologies.com` | The Robot checks whether or not the code signing certificate has been revoked. |
| `x1.i.lencr.org` | To verify whether the Let's Encrypt certificate authority has revoked the code signing certificate. |
| `*.service.signalr.net` | The Robot connects to Orchestrator's SignalR channels. |
| `*.ingest.sentry.io` | The UiPath® Assistant sends the application errors to Sentry in order to track and solve the most usual problems. |
| `dev.azure.com`  `pkgs.dev.azure.com`  `*.blob.core.windows.net` | To enable UiPath Robots to store and retrieve data using Azure storage services. |
| `gallery.uipath.com`  `marketplace.uipath.com`  `*.pkgs.visualstudio.com` **Note:**`gallery.uipath.com/api/v2` redirects to `uipath.pkgs.visualstudio.com`. | These are the URLs for the Marketplace NuGet feed |
| `dc.applicationinsights.azure.com`  `dc.applicationinsights.microsoft.com`  `dc.services.visualstudio.com`  `*.in.applicationinsights.azure.com` | The Robot uses these endpoints to send telemetry data. |
| `asstoffalp.z6.web.core.windows.net` | Used to load components for the UiPath® Assistant for Excel add-in. |
| `*.trafficmanager.net` | Proxy service used by the [Live Streaming](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/live-streaming-and-remote-control) feature to connect between the robot and browser. |

### Outbound IPs for notifications

You can configure Notification service systems to use SMTP servers from your own on-premises or cloud networks. If you want to provide additional security to your Notification service system, you can protect it with a firewall, and only allow Notification Service's outbound static IP ranges through it. Reach out to the [UiPath support team](https://www.uipath.com/company/contact-us/cloud-platform-technical-support) for the list of outbound IP ranges that you need to allow behind your firewall.

## Action Center

### Domains

The following table lists the domains used by Action Center that we recommend allowing, based on the functionality you plan to use:

| Scenario | Domains to Allow |
| --- | --- |
| Authentication | `https://<customURL>.dedicated.uipath.com`  `https://sandbox.stg.dedicated.uipath.com`  `https://lh3.googleusercontent.com/` |
| Navigate to Action Center page | `https://<customURL>.dedicated.uipath.com`  `https://sandbox.stg.dedicated.uipath.com`  `https://uipath-acc-prod.azureedge.net/`  `https://www.youtube.com/`  `https://platform-cdn.uipath.com/`  `https://fonts.gstatic.com/`  `*.googleapis.com` |
| View/Assign/Un-assign/Delete an Action | `https://<customURL>.dedicated.uipath.com`  `https://sandbox.stg.dedicated.uipath.com`  `https://api.smartling.com/`  `https://uipath-acc-prod.azureedge.net/`  `*.cloudfront.net`  `https://platform-cdn.uipath.com/`  `https://fonts.gstatic.com/`  `*.googleapis.com` |
| Storage bucket (File upload/download) | `*.blob.core.windows.net` |

## Automation Ops

### Automation Ops

The following table lists the domains used by Automation Ops:

| Scenario | Domains to Allow |
| --- | --- |
| Navigate to the Automation Ops page | `https://stdadmstgcdn.azureedge.net`  `https://app.vssps.visualstudio.com`  `https://stdadmstgcdn.blob.core.windows.net`  `https://nexus.ensighten.com`  `https://<customURL>.dedicated.uipath.com`  `https://sandbox.stg.dedicated.uipath.com`  `https://platform-cdn.uipath.com`  `https://use.typekit.net`  `https://p.typekit.net`  `https://content.usage.uipath.com`  `https://dc.services.visualstudio.com`  `https://data.usage.uipath.com`  `*-signalr.service.signalr.net`  `https://s.gravatar.com`  `https://i2.wp.com`  `https://github.com`  `https://github.githubassets.com`  `https://avatars.githubusercontent.com`  `https://collector.github.com`  `https://api.github.com` |

## Data Service

The following table lists the domains used by Data Service:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-E2F26D3C-79EB-42D6-94E4-6807ED425D0A__TABLE_F3J_SHY_C3C" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Scenario
   </th>
   <th>
    Domains to Allow
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="GUID-E2F26D3C-79EB-42D6-94E4-6807ED425D0A__D43563E1180">
    All Data Service operations
   </td>
   <td headers="GUID-E2F26D3C-79EB-42D6-94E4-6807ED425D0A__D43563E1183">
    <ul>
     <li>
      <p>
       <code>
        https://&lt;customURL&gt;.dedicated.uipath.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://sandbox.stg.dedicated.uipath.com
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-E2F26D3C-79EB-42D6-94E4-6807ED425D0A__D43563E1180">
    Fetching static frontend content
   </td>
   <td headers="GUID-E2F26D3C-79EB-42D6-94E4-6807ED425D0A__D43563E1183">
    <ul>
     <li>
      <p>
       <code>
        *.cloudapp.azure.com
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-E2F26D3C-79EB-42D6-94E4-6807ED425D0A__D43563E1180">
    Sending notifications to notification hub
   </td>
   <td headers="GUID-E2F26D3C-79EB-42D6-94E4-6807ED425D0A__D43563E1183">
    <ul>
     <li>
      <p>
       <code>
        *.service.signalr.net
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-E2F26D3C-79EB-42D6-94E4-6807ED425D0A__D43563E1180">
    Collection of telemetry
   </td>
   <td headers="GUID-E2F26D3C-79EB-42D6-94E4-6807ED425D0A__D43563E1183">
    <ul>
     <li>
      <p>
       <code>
        *.visualstudio.com
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

## Insights

### Domains

The following table lists the domains used by Insights:

| Scenario | Domains to Allow |
| --- | --- |
| Navigate to the Insights page | `https://<customURL>.dedicated.uipath.com`  `https://sandbox.stg.dedicated.uipath.com`  `https://uipath-insights-statics.azureedge.net/` |

### Outbound IP ranges

Due to a limitation on Microsoft side for Log Export, you cannot set up inbound IP restriction when your Azure blob storage account and the Insights infrastructure is under the same region in Azure. For more information on this limitation, check the [Restrictions for IP network rules](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal#restrictions-for-ip-network-rules) page from the Microsoft Azure Blob Storage documentation.

## Orchestrator

### Domains

Robots send traffic to these Automation Cloud<sup>TM</sup> Dedicated Orchestrator domains. We recommend that you allow these domains to ensure proper functioning of your automations, as described in the following table:

| Module or Functionality | Domains to Allow |
| --- | --- |
| UiPath Orchestrator | `https://<customURL>.dedicated.uipath.com` `https://sandbox.stg.dedicated.uipath.com` `https://orch-cdn.uipath.com` |
| Automation Cloud<sup>TM</sup> Dedicated Robots - VM | `https://<customURL>.dedicated.uipath.com` `https://sandbox.stg.dedicated.uipath.com`  `https://download.uipath.com` |
| Storage | `*.blob.core.windows.net` If using Amazon s3 buckets:  `*.s3.amazonaws.com` |
| Package and library feeds  (library, tenant processes, and others) | `https://pkgs.dev.azure.com` |
| Azure SignalR | `*.service.signalr.net` |
| Studio and Robot auto-update functionality | `https://download.uipath.com` |

## Test Manager

### Domains

The following table lists the domains used by Test Manager that we recommend allowing, based on the functionality you plan to use:

| Module or functionality | Domains to allow |
| --- | --- |
| UiPath Test Manager | `https://<customURL>.dedicated.uipath.com`  `https://sandbox.stg.dedicated.uipath.com` |
| Azure SignalR | `*.service.signalr.net` |