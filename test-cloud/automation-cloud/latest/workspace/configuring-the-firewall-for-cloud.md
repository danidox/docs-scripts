---
title: "Configuring the firewall for Test Cloud"
visible: true
slug: "configuring-the-firewall-for-cloud"
---

For general network configuration and firewall information, refer to [Configuring the firewall](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-firewall#configuring-the-firewall)

## Upcoming outbound IP ranges

Starting January 26, 2026, existing outbound IP ranges will be gradually replaced depending on the hosted region of your organization or UiPath service. Refer to the [UiPath Status page](https://status.uipath.com/) under **Scheduled Maintenance** for regional rollout updates.

**Exception - Automation Cloud Portal**: For Automation Cloud Portal outbound IP ranges used for Customer-Managed Keys (CMK), the transition has been paused. For this service, **existing and upcoming outbound IP ranges will coexist until April 2026**. Starting with April 2026 the gradual replacement of existing outbound IP ranges with the upcoming ones will begin.

The affected services include:

* Automation Cloud Portal (exception)
* Apps
* Automation Ops
* AI Trust Layer, specifically the Bring your own LLM capability
* Integration Service
* Test Manager

**What you need to do**

Update your firewall configuration using the values listed in the **Upcoming outbound IP ranges** column. For most UiPath services, existing outbound IP ranges will begin to be replaced starting January 26, 2026. To avoid service disruptions, ensure your firewall rules are updated as soon as possible. Monitor the [UiPath Status page](https://status.uipath.com/) for maintenance announcements related to this change.

For Automation Cloud Portal, ensure that **both the existing and upcoming outbound IP ranges** are allowed during the coexistence period, which lasts until April 2026.

## Test Cloud Portal

Allow these domains used by Test Cloud Portal:
:::important
If you use Azure buckets, they must not be located in the tenant's region or in the failover region.
:::

### Domains

| Scenario | Domains |
| --- | --- |
| Sign in with basic authentication | `https://account.uipath.com` `https://cloud.uipath.com`  `https://platform-cdn.uipath.com` |
| Sign in with Microsoft | `https://aadcdn.msftauth.net``https://account.uipath.com` `https://cloud.uipath.com` `https://login.live.com``https://login.microsoftonline.com``https://platform-cdn.uipath.com` |
| Sign in with Google | `https://account.uipath.com` `https://cloud.uipath.com` `https://accounts.google.com``https://google.com``https://lh3.googleusercontent.com``https://platform-cdn.uipath.com``https://www.gstatic.com` |
| Sign in with LinkedIn | `https://account.uipath.com``https://cloud.uipath.com``https://lnkd.demdex.net``https://platform-cdn.uipath.com``https://platform.linkedin.com``https://static-exp1.licdn.com``https://www.linkedin.com` |
| Sign in with Azure Active Directory (Azure AD) | `https://aadcdn.msftauth.net``https://cloud.uipath.com``https://login.microsoftonline.com` |
| Sign in with UiPath Assistant (basic email) | `*-signalr.service.signalr.net` For events related to signing in with basic authentication: `https://account.uipath.com` `https://cloud.uipath.com` `https://platform-cdn.uipath.com` |
| Sign in with UiPath Studio (basic email) | `https://api.nuget.org``*-signalr.service.signalr.net``https://gallery.uipath.com``https://pkgs.dev.azure.com` For events related to signing in with basic authentication: `https://account.uipath.com` `https://cloud.uipath.com` `https://platform-cdn.uipath.com` |
| Sign in for the first time / Reset password | `uipath.eu.auth0.com``account.uipath.com` |
| Static assets: Fonts, Styling and CDN hosted scripts | Fonts: `https://use.typekit.net``https://fonts.gstatic.com``https://platform-cdn.uipath.com` Images: `https://s.gravatar.com``https://secure.gravatar.com``https://*.wp.com``https://*.googleusercontent.com``https://i.ytimg.com``https://platform-cdn.uipath.com` CSS: `https://fonts.googleapis.com/css``https://use.typekit.net``https://p.typekit.net``https://platform-cdn.uipath.com` Scripts: `https://primer.typekit.net``https://use.typekit.net``https://platform-cdn.uipath.com` |
| Sign in via Auth0 (for EU) | `uipath.eu.auth0.com` |
| Update services | `ctldl.windowsupdate.com` To configure network connections, use [Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-update-services/deploy/2-configure-wsus#21-configure-network-connections). |
| Download Autopilot for Everyone from the AI Trust Layer admin section | `https://autopilot-prd.azureedge.net` |

### Outbound IP ranges to enable a firewall for the customer-managed key

Required only when the Automation Cloud Portal must connect to your Azure Key Vault for Customer-Managed Key (CMK) scenarios. These outbound IP ranges represent the source IP ranges that your firewall must allow. For details, refer to the [Enabling the firewall for the customer-managed key](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/enabling-a-firewall-for-your-key-vault#enabling-a-firewall-for-the-customer-managed-key) documentation.

The existing outbound IP ranges will be deprecated on January 26, 2026. To prevent service disruption, ensure that the IPs in the Upcoming IPs column are allowed before this date. TOPLEVELNOTEMARKER
  :::important
  If the upcoming outbound IP ranges are not allowed by January 26, 2026, you will be unable to use this functionality. Attempts to use this functionality may result in errors.
  :::

Allow these outbound IP ranges through your firewall: TOPLEVELNOTEMARKER
  :::note
  We recommend allowing all outbound IP ranges listed in the following table through your firewall.
  :::

| Regions | Existing outbound IP ranges | Upcoming outbound IP ranges |
| --- | --- | --- |
| Australia | ``` 20.213.69.140/30 20.92.42.116/30 ``` | ``` 13.75.193.208/30 13.75.193.248/30 23.101.232.52/30 23.101.238.168/30 ``` |
| Canada | ``` 20.220.159.8/30 20.104.134.160/30 ``` | ``` 20.220.216.172/30 20.220.216.176/30 40.86.221.132/30 40.86.219.8/30 ``` |
| Community | ``` 20.166.153.132/30 20.23.210.168/30 ``` | ``` 20.101.116.56/30 20.101.117.36/30 94.245.89.240/30 94.245.92.36/30 ``` |
| European Union | ``` 20.166.153.132/30 20.23.210.168/30 ``` | ``` 20.101.115.224/30 20.101.114.72/30 94.245.89.180/30 94.245.89.208/30 ``` |
| European Union (delayed) | ``` 20.166.153.132/30 20.23.210.168/30 ``` | ``` 20.101.117.40/30 20.101.117.64/30 94.245.92.148/30 94.245.92.208/30 ``` |
| India | ``` 20.219.182.96/30 52.140.57.140/30 ``` | ``` 104.211.95.48/30 104.211.88.192/30 104.211.218.32/30 104.211.216.236/30 ``` |
| Japan | ``` 20.78.114.120/30 104.215.9.124/30 ``` | ``` 20.46.112.236/30 20.46.113.0/30 104.46.228.24/30 104.46.228.96/30 ``` |
| Singapore | ``` 20.198.150.140/30 52.140.57.140/30 ``` | ``` 13.67.50.0/30 13.67.48.140/30 ``` |
| United Kingdom | ``` 20.90.169.148/30 51.142.146.56/30 ``` | ``` 20.90.81.12/30 20.90.81.60/30 51.140.206.232/30 51.140.204.72/30 ``` |
| United States | ``` 20.232.224.12/30 20.66.65.144/30 ``` | ``` 52.152.132.116/30 52.152.133.144/30 13.66.157.200/30 13.66.155.116/30 ``` |
| United States (delayed) | ``` 20.232.224.12/30 20.66.65.144/30 ``` | ``` 52.249.186.136/30 52.249.187.48/30 13.66.157.200/30 13.66.155.116/30 ``` |
| Switzerland | ``` 51.107.68.220/30 51.107.68.232/30 20.199.240.20/30 20.199.240.8/30 ``` | ``` 51.107.68.220/30 51.107.68.232/30 20.199.240.20/30 20.199.240.8/30 ``` |
| United Arab Emirates | ``` 40.123.215.148/30 40.123.215.168/30 20.45.67.8/30 20.45.67.20/30 ``` | ``` 40.123.215.148/30 40.123.215.168/30 20.45.67.8/30 20.45.67.20/30 ``` |

### Outbound IPs for notifications

You can configure Notification service systems to use SMTP servers from your own on-premises or cloud networks. If you want to provide additional security to your Notification service system, you can protect it with a firewall, and only allow Notification Service's outbound static IP ranges through it.

```
20.213.69.140/30
20.92.42.116/30
20.220.159.8/30
20.104.134.160/30
20.239.121.152/30
20.232.224.12/30
20.78.114.120/30
104.215.9.124/30
20.166.153.132/30
20.198.150.140/30
20.23.210.168/30
20.66.65.144/30
149.72.70.144
```

## Action Center

### Domains

The following table lists the domains used by Action Center that we recommend allowing, based on the functionality you plan to use:

The following table lists the domains used by Action Center that we recommend allowing, based on the functionality you plan to use:

| Scenario | Domains to Allow |
| --- | --- |
| Authentication | `https://cloud.uipath.com`  `https://account.uipath.com/`  `https://lh3.googleusercontent.com/` |
| Navigate to Action Center page | `https://cloud.uipath.com`  `https://uipath-acc-prod.azureedge.net/`  `https://www.youtube.com/`  `https://platform-cdn.uipath.com/`  `https://fonts.gstatic.com/`  `*.googleapis.com` |
| View/Assign/Un-assign/Delete an Action | `https://cloud.uipath.com`  `https://api.smartling.com/`  `https://uipath-acc-prod.azureedge.net/`  `*.cloudfront.net`  `https://platform-cdn.uipath.com/`  `https://fonts.gstatic.com/`  `*.googleapis.com` |
| Storage bucket (File upload/download) | `*.blob.core.windows.net` |

## AI Center

### Domains

The following table lists the domains used by AI Center:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-1B9727B9-3071-46C3-85A5-5A16E56B8E02__TABLE_CLR_FDQ_QHC" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    <p>
     Module or Scenario
    </p>
   </th>
   <th>
    <p>
     Domains to Allow
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td colspan="2" headers="d148245e871 d148245e877">
    <p>
     <strong>
      AI Center
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     Identity Server
    </p>
   </td>
   <td headers="d148245e877">
    <p>
     <code>
      https://cloud.uipath.com
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     PkgManager
    </p>
   </td>
   <td headers="d148245e877">
    <p>
     <code>
      https://cloud.uipath.com
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     Deployer
    </p>
   </td>
   <td headers="d148245e877">
    <p>
     <code>
      https://cloud.uipath.com
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     Helper
    </p>
   </td>
   <td headers="d148245e877">
    <p>
     <code>
      https://cloud.uipath.com
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     Trainer
    </p>
   </td>
   <td headers="d148245e877">
    <p>
     <code>
      https://cloud.uipath.com
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     AppManager
    </p>
   </td>
   <td headers="d148245e877">
    <p>
     <code>
      https://cloud.uipath.com
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     Upload files
    </p>
   </td>
   <td headers="d148245e877">
    <style>
     .css-17xdpgx{word-break:break-word;}.css-17xdpgx div{padding-left:10px;}.css-17xdpgx code{font-size:16px;}.css-17xdpgx img{margin-bottom:-5px;}
    </style>
    Australia:
    <code>
     https://aifproddataauetraining.blob.core.windows.net
    </code>
    Canada:
    <code>
     https://aifproddatacactraining.blob.core.windows.net
    </code>
    Europe:
    <code>
     https://aifproddatawetraining.blob.core.windows.net
    </code>
    Japan:
    <code>
     https://aifproddatajaetraining.blob.core.windows.net
    </code>
    Singapore:
    <code>
     https://aifproddataseatraining.blob.core.windows.net
    </code>
    USA:
    <code>
     https://aifproddataeustraining.blob.core.windows.net
    </code>
    GXP:
    <code>
     https://aifgxpdatawetraining.blob.core.windows.net
    </code>
   </td>
  </tr>
  <tr>
   <td colspan="2" headers="d148245e871 d148245e877">
    <p>
     <strong>
      Third-party Services
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     AppInsights
    </p>
   </td>
   <td headers="d148245e877">
    <p>
     <code>
      https://bam.eu01.nr-data.net
     </code>
    </p>
    <p>
     <code>
      https://eastus-6.in.applicationinsights.azure.com/
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     Static Assets
    </p>
   </td>
   <td headers="d148245e877">
    <p>
     <code>
      https://aifprodassets.azureedge.net
     </code>
    </p>
    <p>
     <code>
      https://i2.wp.com/cdn.auth0.com
     </code>
    </p>
    <p>
     <code>
      https://api.smartling.com
     </code>
    </p>
    <p>
     <code>
      https://s.gravatar.com
     </code>
    </p>
    <p>
     <code>
      https://js-agent.newrelic.com
     </code>
    </p>
    <p>
     <code>
      https://fonts.gstatic.com
     </code>
    </p>
    <p>
     <code>
      https://use.typekit.net
     </code>
    </p>
    <p>
     <code>
      https://fonts.googleapis.com
     </code>
    </p>
    <p>
     <code>
      https://d2c7xlmseob604.cloudfront.net
     </code>
    </p>
    <p>
     <code>
      https://du-prod-cdn.azureedge.net/
     </code>
    </p>
    <p>
     <code>
      https://aifprodassets.azureedge.net/
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td colspan="2" headers="d148245e871 d148245e877">
    <p>
     <strong>
      Navigate to AI Center
     </strong>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     Permissions
    </p>
   </td>
   <td headers="d148245e877">
    <p>
     <code>
      https://cloud.uipath.com
     </code>
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d148245e871">
    <p>
     OpenId configuration
    </p>
   </td>
   <td headers="d148245e877">
    <p>
     <code>
      https://cloud.uipath.com
     </code>
    </p>
    <p>
     <code>
      https://dc.services.visualstudio.com
     </code>
    </p>
    <p>
     <code>
      https://d2c7xlmseob604.cloudfront.net
     </code>
    </p>
    <p>
     <code>
      https://use.typekit.net
     </code>
    </p>
    <p>
     <code>
      https://fonts.googleapis.com
     </code>
    </p>
    <p>
     <code>
      https://aifstgassets.azureedge.net
     </code>
    </p>
    <p>
     <code>
      https://p.typekit.net
     </code>
    </p>
    <p>
     <code>
      https://fonts.gstatic.com
     </code>
    </p>
    <p>
     <code>
      https://api.smartling.com
     </code>
    </p>
    <p>
     <code>
      https://js-agent.newrelic.com
     </code>
    </p>
    <p>
     <code>
      https://i2.wp.com/cdn.auth0.com
     </code>
    </p>
    <p>
     <code>
      https://bam.eu01.nr-data.net
     </code>
    </p>
    <p>
     <code>
      https://du-prod-du-eus-signalr.service.signalr.net/
     </code>
    </p>
    <p>
     <code>
      wss://du-prod-du-eus-signalr.service.signalr.net/
     </code>
    </p>
   </td>
  </tr>
 </tbody>
</table>

## AI Computer Vision

The following table lists the endpoint values and server locations used by AI Computer Vision:

The following table lists the endpoint values and server locations used by AI Computer Vision:

| Endpoint Value | Server Location |
| --- | --- |
| `https://cv.uipath.com` | Nearest geolocation based on the request IP |
| `https://cv-eu.uipath.com` | West Europe |
| `https://cv-us.uipath.com` | US |
| `https://cv-delayed.uipath.com` | [Delayed enterprise ring deployment](https://docs.uipath.com/ai-computer-vision/automation-cloud/latest/user-guide/delayed-enterprise-ring-deployment), located in the United States |

## AI Trust Layer – Bring your own LLM

### Outbound IP ranges

Allow the following outbound IP ranges to establish communication between the Bring your own LLM functionality of AI Trust Layer, and your own system. TOPLEVELNOTEMARKER
:::important
Starting January 26, 2026, **existing outbound IP ranges** for this service are being gradually replaced based on your organization’s hosted region. Ensure that the **upcoming outbound IP ranges** are allowed in your firewall to prevent service disruptions. Refer to the [UiPath Status page](https://status.uipath.com/) for regional rollout updates.
:::

The Bring your own LLM functionality depends on Integration Service connectors for communication. To use this capability and create connections successfully, you must also add the [Integration Service outbound IP ranges](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-the-firewall-for-cloud#integration-service) to your allowlist.

Table 1. Outbound IP ranges for Bring your own LLM

| Region | Current outbound IP ranges | Upcoming outbound IP ranges |
| --- | --- | --- |
| Australia | ``` 20.28.250.185 4.147.230.122 20.70.108.149 13.70.189.36 ``` | ``` 13.75.193.208/30 13.75.193.248/30 23.101.232.52/30 23.101.238.168/30 ``` |
| Canada | ``` 20.200.74.11 20.175.244.6 20.175.13.214 4.239.106.142 ``` | ``` 20.220.216.172/30 20.220.216.176/30 40.86.221.132/30 40.86.219.8/30 ``` |
| Europe (European Union) | ``` 51.124.146.117 4.175.35.111 132.164.136.105 20.223.60.250 172.205.43.183 4.208.18.113 172.205.19.97 ``` | ``` 20.101.115.224/30 20.101.114.72/30 94.245.89.180/30 94.245.89.208/30 ``` |
| European Union delayed | ``` 4.175.237.158 4.207.163.181 ``` | ``` 20.101.117.40/30 20.101.117.64/30 94.245.92.148/30 94.245.92.208/30 ``` |
| Community (Europe) | ``` 20.238.238.150 132.220.170.20 4.175.35.116 172.205.108.34 20.105.97.152 172.205.16.240 172.205.36.80 172.205.17.92 ``` | ``` 20.101.116.56/30 20.101.117.36/30 94.245.89.240/30 94.245.92.36/30 ``` |
| India | ``` 20.219.243.101 52.172.50.27 ``` | ``` 104.211.95.48/30 104.211.88.192/30 104.211.218.32/30 104.211.216.236/30 ``` |
| Japan | ``` 20.46.112.236/30 20.46.113.0/30 104.46.228.24/30 104.46.228.96/30 ``` | ``` 20.210.61.234 48.218.152.22 40.74.89.29 104.215.28.230 ``` |
| Singapore | ``` 20.43.184.90 57.155.24.121 ``` | ``` 13.67.50.0/30 13.67.48.140/30 ``` |
| United Kingdom | ``` 172.166.81.40 20.254.140.213 ``` | ``` 20.90.81.12/30 20.90.81.60/30 51.140.206.232/30 51.140.204.72/30 ``` |
| United States | ``` 20.241.165.222 172.212.38.1 172.210.90.91 4.255.35.88 48.217.204.212 51.143.120.61 172.179.75.145 ``` | ``` 52.152.132.116/30 52.152.133.144/30 13.66.157.200/30 13.66.155.116/30 ``` |
| United States delayed | ``` 40.88.219.122 48.217.4.134 20.115.194.161 172.179.123.123 ``` | ``` 52.249.186.136/30 52.249.187.48/30 13.66.157.200/30 13.66.155.116/30 ``` |

## Apps

### Domains

The following table lists the domains used by Apps that you need to allow:

| Scenario | Domains to Allow |
| --- | --- |
| Navigate to Apps | `https://cloud.uipath.com`  `https://fonts.googleapis.com`  `https://cdnjs.cloudflare.com`  `https://uipath-apps-prd.azureedge.net`  `https://fonts.gstatic.com`  `https://dc.services.visualstudio.com` |
| Navigate to Apps | `https://govcloud.uipath.us`  `https://fonts.googleapis.com`  `https://cdnjs.cloudflare.com`  `https://uipath-apps-pgov.uipath.us`  `https://fonts.gstatic.com`  `https://usgovvirginia-1.in.applicationinsights.azure.us` |
| Create apps, or create apps via import, or add or delete process | `https://cloud.uipath.com`  `https://uipath-apps-prd.azureedge.net` |
| Create apps, or  create apps via import,  or add or delete process | `https://govcloud.uipath.us`  `https://uipath-apps-pgov.uipath.us` |
| Export, clone, share, delete, edit, or publish an app | `https://cloud.uipath.com` |
| Export, clone, share, delete, edit, or publish an app | `https://govcloud.uipath.us/` |
| Run or preview an app | `https://cloud.uipath.com`  `https://fonts.googleapis.com`  `https://cdnjs.cloudflare.com`  `https://uipath-apps-prd.azureedge.net`  `https://fonts.gstatic.com`  `https://dc.services.visualstudio.com` |
| Run or preview an app | `https://govcloud.uipath.us`  `https://fonts.googleapis.com`  `https://cdnjs.cloudflare.com`  `https://uipath-apps-pgov.uipath.us`  `https://fonts.gstatic.com`  `https://usgovvirginia-1.in.applicationinsights.azure.us` |
| Select on Processes or Create rule | `https://uipath-apps-prd.azureedge.net` |
| Select on Processes or Create rule | `https://uipath-apps-pgov.uipath.us` |
| Bind process | `https://uipath-apps-prd.azureedge.net`  `https://cloud.uipath.com`  `https://dc.services.visualstudio.com` |
| Bind process | `https://uipath-apps-pgov.uipath.us`  `https://govcloud.uipath.us`  `https://usgovvirginia-1.in.applicationinsights.azure.us` |
| General or Permission | `https://api.smartling.com` |
| Create or delete a page, or create or delete History | `https://cloud.uipath.com`  `https://api.smartling.com` |
| Create or delete a page, or create or delete History | `https://govcloud.uipath.us/` |
| Connect to Apps | `*.trafficmanager.net`  `wss://*.uipath.systems`  `wss://cloud.uipath.com` |

### Outbound IP ranges

The Apps service uses the outgoing IP ranges listed below for all external communications. The following table shows the available outbound IP ranges for each region.

The current outbound IP ranges will be deprecated on January 26, 2026. To avoid disruption, make sure to add the outbound IP ranges listed under the **Upcoming outbound IP ranges** column before this date. TOPLEVELNOTEMARKER
:::important
If the upcoming outbound IP ranges are not allowed by January 26, 2026, you will be unable to use this service. Attempts to use this service may result in errors.
:::

| Region | Current outbound IP ranges | Upcoming outbound IP ranges |
| --- | --- | --- |
| Europe | ``` 20.93.15.208 ``` | ``` 94.245.89.4/30 94.245.93.8/30 ``` |
| Europe (Secondary) | ``` 20.13.60.212 ``` | ``` 20.67.88.64/30 20.67.88.112/30 ``` |
| Europe - Community | ``` 4.207.32.162 ``` | ``` 94.245.93.132/30 94.245.93.148/30 ``` |
| Europe - Community (Secondary) | ``` 20.13.110.150 ``` | ``` 20.67.88.116/30 20.67.88.132/30 ``` |
| US | ``` 20.121.170.55 ``` | ``` 104.211.63.160/30 104.211.58.236/30 ``` |
| US (Secondary) | ``` 20.72.203.238 ``` | ``` 13.66.167.4/30 13.66.163.204/30 ``` |
| Canada | ``` 20.200.104.214 ``` | ``` 20.151.112.252/30 20.151.113.120/30 ``` |
| Canada (Secondary) | ``` 20.220.98.56 ``` | ``` 40.86.219.188/30 40.86.224.148/30 ``` |
| Singapore | ``` 20.44.206.197 ``` | ``` 104.215.184.68/30 104.215.185.96/30 ``` |
| Japan | ``` 20.89.117.202 ``` | ``` 20.89.104.152/30 20.89.104.200/30 ``` |
| Japan (Secondary) | ``` 104.46.238.159 ``` | ``` 40.74.64.240/30 40.74.65.80/30 ``` |
| Australia | ``` 20.167.34.255 ``` | ``` 13.75.193.84/30 13.75.193.112/30 ``` |
| Australia (Secondary) | ``` 20.11.199.185 ``` | ``` 13.77.46.56/30 13.77.40.228/30 ``` |
| India | ``` 4.224.9.5 ``` | ``` 40.80.89.64/30 40.80.89.136/30 ``` |
| India (Secondary) | ``` 13.71.90.136 ``` | ``` 104.211.218.152/30 104.211.222.120/30 ``` |
| UK | ``` 172.165.145.81 ``` | ``` 51.104.16.124/30 51.104.16.168/30 ``` |
| UK (Secondary) | ``` 51.141.6.153 ``` | ``` 51.140.205.20/30 51.140.205.248/30 ``` |
| Switzerland | ``` 51.107.68.220/30 51.107.68.223/30 20.199.240.20/30 20.199.240.8/30 ``` | ``` 51.107.68.220/30 51.107.68.223/30 20.199.240.20/30 20.199.240.8/30 ``` |
| United Arab Emirates | ``` 40.123.215.148/30 40.123.215.168/30 20.45.67.8/30 20.45.67.20/30 ``` | ``` 40.123.215.148/30 40.123.215.168/30 20.45.67.8/30 20.45.67.20/30 ``` |
| GXP US (Secondary) | ``` 52.143.81.192 ``` | ``` 13.66.166.60/30 13.66.160.164/30 ``` |
| GXP US | ``` 20.246.192.220 ``` | ``` 104.211.56.184/30 40.114.71.160/30 ``` |

Traffic from this IPs needs to be allowed through the Organization DMZ firewall and any other intermediate firewalls including the firewall on the computer/s in which Orchestrator application is hosted.

* The associated port on which Orchestrator application is hosted needs to be exposed through the DMZ on all relevant firewalls (see the previous point).
* An Orchestrator user who has read and execute access to relevant processes whose credential will be used from UiPath Apps to talk to Orchestrator.
* If using local robot process execution through RobotJS, please ensure RobotJS is properly configured using instructions provided at [RobotJS](https://docs.uipath.com/robot/standalone/2024.10/user-guide/about-the-robot-javascript-sdk).

#### Best practices

* Ensure that the On-Premise hosted Orchestrator is only accessible through a secure HTTPS channel.
* Create a low privilege user in Orchestrator that only has read and execute access to just the desired processes/folders and use that for the integration.

#### CORS policy requirements for Storage Buckets

When using storage buckets from an on-premises or hybrid Orchestrator, add `https://cloud.uipath.com` to the `acceptedRootURLs` list in the [UiPath.Orchestrator.dll.config file](https://docs.uipath.com/installation-and-upgrade/docs/uipath-orchestrator-dll-config).
:::note
* If your Orchestrator instance is hosted in Automation Cloud, this configuration is
already in place.
* For external buckets, configure the allowed origins as described in the [CORS and CSP configuration](https://docs.uipath.com/orchestrator/v0/docs/cors-csp-configuration) guide.”
:::

UiPath Apps uploads and downloads files using the SAS URL generated by Orchestrator when interacting with storage buckets hosted in an on-premises environment. End users must have the appropriate permissions granted through that SAS URL to perform both upload and download operations.
:::important
All access control is defined and enforced by the underlying storage account configuration. UiPath does not manage or override these permissions.
:::

If users encounter errors when uploading or downloading files through UiPath Apps, the **storage account’s SAS policies or access restrictions** should be reviewed and updated by the storage owner to ensure the required level of access.

### Content types to add to the allow list

UiPath Apps utilizes the content types `application/octet-stream` and `application/zip` for downloading specific DLL files required to run and preview created applications. It is important to ensure the following content types are allowed within your network settings to avoid interruptions in app functionality:

```
application/zip
application/octet-stream
application/json
text/html
application/javascript
text/css
font/woff2
image/vnd.microsoft.icon
image/svg+xml
image/bmp
image/jpeg
image/png
image/gif
```

**Key Considerations**

Apps are developed using Blazor technology, which processes assemblies directly in the browser. If restrictions for the required content types cannot be lifted within your network, Apps may not function as expected, as there are currently no alternative solutions to bypass these limitations.

**Apps in Studio Web as an alternative**

Apps in Studio Web are designed with a different architecture, that does not require downloading DLL files. If network restrictions prevent the use of Standalone Apps, consider adopting Apps in Studio Web (RPA Apps). This architecture eliminates dependency on restricted content types, ensuring smoother compatibility in restricted network environments.

## Automation Cloud Robots - Serverless

### Outbound IP ranges

Outbound IP ranges for Automation Cloud Robots - Serverless enable you to route outbound network traffic through a dedicated, static IP address ranges managed by UiPath. This allows you to whitelist or securely integrate with external systems that restrict incoming connections to known IPs.

**Configuration**

You can enable static outbound IP ranges while [creating the Serverless template](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/executing-unattended-automations-with-serverless-robots#step-2-adding-serverless-robots-to-your-tenant) and going to the **Network Configuration** page.

**Availability**

The outbound IP ranges can sometimes change as a result of infrastructure deployments. To help keep you on top of any changes, we have compiled a list of up-to-date static outbound IP ranges, in the following tables.

#### Community Users

| Region | CIDR | Outbound IP ranges |
| --- | --- | --- |
| Europe | ``` 20.191.43.0/30 20.191.42.240/30 ``` | ``` 20.191.43.0 20.191.43.1 20.191.43.2 20.191.43.3 20.191.42.240 20.191.42.241 20.191.42.242 20.191.42.243 ``` |

#### Enterprise Users

| Region | CIDR | Outbound IP ranges |
| --- | --- | --- |
| Australia | ``` 20.53.170.116/30 20.53.170.208/30 ``` | ``` 20.53.170.116 20.53.170.117 20.53.170.118 20.53.170.119 20.53.170.208 20.53.170.209 20.53.170.210 20.53.170.211 ``` |
| United States | ``` 20.102.5.168/30 20.102.0.76/30 172.202.61.224/30 * 20.15.227.248/30 * ``` | ``` 20.102.5.168 20.102.5.169 20.102.5.170 20.102.5.171 20.102.0.76 20.102.0.77 20.102.0.78 20.102.0.79 172.202.61.224 * 172.202.61.225 * 172.202.61.226 * 172.202.61.227 * 20.15.227.248 * 20.15.227.249 * 20.15.227.250 * 20.15.227.251 * ``` |
| Japan | ``` 20.44.188.168/30 20.44.185.192/30 ``` | ``` 20.44.188.168 20.44.188.169 20.44.188.170 20.44.188.171 20.44.185.192 20.44.185.193 20.44.185.194 20.44.185.195 ``` |
| Europe (European Union) | ``` 20.191.46.104/30 20.191.43.60/30 ``` | ``` 20.191.46.104 20.191.46.105 20.191.46.106 20.191.46.107 20.191.43.60 20.191.43.61 20.191.43.62 20.191.43.63 ``` |

* Added on February 18th, 2026.

## Automation Hub

### Domains

The following table lists the domains used by Automation Hub:

The following table lists the domains used by Automation Hub:

| Scenario | Domains to Allow |
| --- | --- |
| Navigate to the Automation Hub page | `https://cloud.uipath.com` `http://*.userpilot.io` `https://dc.services.visualstudio.com`  `https://ah-prod-ts-blue-eu.uipath.com`  `https://ah-prod-ts-blue-us.uipath.com`  `https://ah-prod-ts-blue-ja.uipath.com`  `https://ah-prod-ts-blue-au.uipath.com`  `https://ah-prod-ts-blue-ca.uipath.com`  `https://ah-prod-ts-blue-sea.uipath.com`  `https://ah-prod-ts-blue-uk.uipath.com`  `https://ah-prod-ts-blue-in.uipath.com`  `https://ah-gxp-ts-blue-us.uipath.com` |
| Use OpenAPI for Automation Hub | `https://automation-hub.uipath.com``http://ah-gxp-openapi-us.uipath.com` |

## Automation Ops

### Domains

The following table lists the domains used by Automation Ops:

| Scenario | Domains to Allow |
| --- | --- |
| Navigate to the Automation Ops page | `https://stdadmstgcdn.azureedge.net`  `https://app.vssps.visualstudio.com`  `https://stdadmstgcdn.blob.core.windows.net`  `https://nexus.ensighten.com`  `https://cloud.uipath.com`  `https://platform-cdn.uipath.com`  `https://use.typekit.net`  `https://p.typekit.net`  `https://content.usage.uipath.com`  `https://dc.services.visualstudio.com`  `https://data.usage.uipath.com`  `*-signalr.service.signalr.net`  `https://s.gravatar.com`  `https://i2.wp.com`  `https://github.com`  `https://github.githubassets.com`  `https://avatars.githubusercontent.com`  `https://collector.github.com`  `https://api.github.com` |

### Outbound IP ranges

The table below lists all outbound IP ranges currently used by Automation Ops. The existing outbound IP ranges will be deprecated on January 26, 2026. To prevent service disruption, ensure that the outbound IP ranges in the **Upcoming outbound IP ranges** column are added before this date. TOPLEVELNOTEMARKER
  :::important
  If the upcoming outbound IP ranges are not allowed by January 26, 2026, you will be unable to use this service. Attempts to use this service may result in errors.
  :::

| Region | Current outbound IP ranges | Upcoming outbound IP ranges |
| --- | --- | --- |
| Australia | ``` 20.28.250.185 4.147.230.122 20.70.108.149 13.70.189.36 ``` | ``` 13.75.193.208/30 13.75.193.248/30 23.101.232.52/30 23.101.238.168/30 ``` |
| Japan | ``` 20.210.61.234 48.218.152.22 40.74.89.29 104.215.28.230 ``` | ``` 104.46.228.24/30 104.46.228.96/30 20.46.112.236/30 20.46.113.0/30 ``` |
| United States | ``` 20.241.165.222 172.212.38.1 172.210.90.91 4.255.35.88 48.217.204.212 51.143.120.61 172.179.75.145 ``` | ``` 52.152.132.116/30 52.152.133.144/30 13.66.157.200/30 13.66.155.116/30 ``` |
| United States GXP | ``` 172.179.123.123 20.115.194.161 48.217.4.134 40.88.219.122 ``` | ``` 52.249.186.136/30 52.249.187.48/30 13.66.157.200/30 13.66.155.116/30 ``` |
| Europe | ``` 132.164.136.105 20.223.60.250 172.205.43.183 4.208.18.113 172.205.19.97 4.175.35.111 51.124.146.117 20.238.238.150 132.220.170.20 4.175.35.116 172.205.108.34 20.105.97.152 172.205.16.240 172.205.36.80 172.205.17.92 ``` | ``` 20.101.115.224/30 20.101.114.72/30 94.245.89.180/30 94.245.89.208/30 20.101.116.56/30 20.101.117.36/30 94.245.89.240/30 94.245.92.36/30 ``` |
| Europe GXP | ``` 4.175.237.158 4.207.163.181 ``` | ``` 94.245.92.148/30 94.245.92.208/30 ``` |
| Canada | ``` 20.200.74.11 20.175.244.6 20.175.13.214 4.239.106.142 ``` | ``` 20.220.216.172/30 20.220.216.176/30 40.86.221.132/30 40.86.219.8/30 ``` |
| Singapore | ``` 20.43.184.90 57.155.24.121 ``` | ``` 13.67.50.0/30 13.67.48.140/30 ``` |
| India | ``` 20.219.243.101 52.172.50.27 ``` | ``` 104.211.95.48/30 104.211.88.192/30 104.211.218.32/30 104.211.216.236/30 ``` |
| UK | ``` 172.166.81.40 20.254.140.213 ``` | ``` 20.90.81.12/30 20.90.81.60/30 51.140.206.232/30 51.140.204.72/30 ``` |
| Switzerland | ``` 51.107.68.220/30 51.107.68.232/30 20.199.240.20/30 20.199.240.8/30 ``` | ``` 51.107.68.220/30 51.107.68.232/30 20.199.240.20/30 20.199.240.8/30 ``` |
| United Arab Emirates | ``` 40.123.215.148/30 40.123.215.168/30 20.45.67.8/30 20.45.67.20/30 ``` | ``` 40.123.215.148/30 40.123.215.168/30 20.45.67.8/30 20.45.67.20/30 ``` |

## IXP

### Domains

The following table lists the domains that IXP uses:

| Scenario | Domains to Allow |
| --- | --- |
| Admin Portal / Identity Server | `https://cloud.uipath.com` |
| Static assets | `https://fonts.googleapis.com`  `https://fonts.gstatic.com` |
| Azure SignalR | `*.service.signalr.net` |
| Telemetry | `https://*.in.applicationinsights.azure.com`  `https://dc.services.visualstudio.com` |
| Pendo (clickable in-app guides) | `https://*.pendo.io` |
| Performance monitoring | `https://o486811.ingest.sentry.io` |

### Inbound IP ranges
:::note
This section applies only to legacy Re:infer customers.
:::

Add the following inbound IP ranges to your allow list to use IXP and create connections:

| Region | Inbound IP ranges |
| --- | --- |
| Europe | ``` 34.91.100.206 ``` |
| US | ``` 34.69.242.10 20.62.244.78 ``` |
| Japan | ``` 34.84.144.176 ``` |
| Australia | ``` 35.189.46.91 ``` |
| Canada | ``` 34.152.10.176 ``` |
| Singapore | ``` 35.240.179.214 ``` |

### Outbound IP ranges

Allow the following outbound IP ranges for IXP to sync emails from your Exchange. For details, check the [Overview Exchange integration](https://docs.uipath.com/communications-mining/automation-cloud/latest/developer-guide/overview-exchange-integration).

| Region | Outbound IP ranges |
| --- | --- |
| Europe | ``` 35.204.220.118 ``` |
| US | ``` 34.71.173.219 ``` |
| Japan | ``` 34.84.107.92 ``` |
| Australia | ``` 34.87.223.173 ``` |
| Canada | ``` 34.152.42.160 ``` |
| Singapore | ``` 34.143.128.81 ``` |

## Data Fabric

### Domains

The following table lists the domains used by Data Fabric:

| Scenario | Domains to Allow |
| --- | --- |
| All Data Fabric operations | `https://cloud.uipath.com` |
| Fetching static frontend content | `*.cloudapp.azure.com` |
| Sending notifications to notification hub | `*.service.signalr.net` |
| Collection of telemetry | `*.visualstudio.com` |

## Document Understanding

### Domains

The following table lists the domains used by Document Understanding:

| Module or Scenario | Domains to Allow |
| --- | --- |
| Navigate to Document Understanding | `https://*.uipath.com` |
| Azure | `https://*.azure.com` |
| Network | `https://*.azureedge.net`  `https://*.azurefd.net` |
| Telemetry | `https://*.visualstudio.com` |
| Azure SignalR | `https://*.service.signalr.net` |
| Storage | `https://*.trafficmanager.net`  `https://*.blob.core.windows.net` |
| Pendo | `https://*.pendo.io` |
| Public endpoints | Check the [Public endpoints](https://docs.uipath.com/document-understanding/automation-cloud/latest/user-guide/public-endpoints) page for the full list of public endpoints URLs. |

## Insights

### Domains

The following table lists the domains used by Insights:

| Scenario | Domains to Allow |
| --- | --- |
| Navigate to the Insights page | `https://cloud.uipath.com`  `https://*.lookercdn.com`  `https://uipath-insights-statics.azureedge.net/`  `https://*.looker.uipath.com/` |

### Outbound IP ranges

Outbound IP ranges allow you to add a list of IPs for Log Export and Real Time Data Export features to the allowlist and not open your network to all external IPs. If the Blob storage regions correspond to the respective Insights service region, you cannot use public IPs.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-8FFE3E9A-3678-4BDC-BE25-26EA0838F7B2__TABLE_XLC_RJY_DFC" summary="">
 <caption>
  Table 2. Insights Outbound static IP
                              ranges
 </caption>
 <colgroup>
  <col/>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Insights service region
   </th>
   <th>
    Blob storage region
   </th>
   <th>
    Functionality
   </th>
   <th>
    Outbound static IP ranges
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d148245e3738" rowspan="3">
    Europe
   </td>
   <td headers="d148245e3741" rowspan="3">
    <ul>
     <li>
      North Europe
     </li>
     <li>
      West Europe
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.209.242.155
52.158.117.70
48.209.163.160
132.220.192.40</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>48.209.165.211
4.209.26.11</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Looker SFTP notifications
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>34.159.94.48
34.159.97.39
34.89.186.9</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3738" rowspan="3">
    United States of America
   </td>
   <td headers="d148245e3741" rowspan="3">
    <ul>
     <li>
      North Europe
     </li>
     <li>
      West Europe
     </li>
     <li>
      East US
     </li>
     <li>
      West US
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.209.242.155
134.33.227.198
134.33.128.26</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.156.106.136
134.33.152.158</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Looker SFTP notifications
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>34.145.223.13
34.150.213.234
35.186.171.220</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3738" rowspan="3">
    Australia
   </td>
   <td headers="d148245e3741" rowspan="3">
    <ul>
     <li>
      North Europe
     </li>
     <li>
      Australia
                                       East
     </li>
     <li>
      West Europe
     </li>
     <li>
      Australia
                                       Southeast
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.209.242.155
4.254.65.248</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.237.200.13
4.237.193.83</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Looker SFTP notifications
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>34.151.78.48
34.116.85.140
34.87.195.36
35.189.54.47</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3738" rowspan="3">
    Japan
   </td>
   <td headers="d148245e3741" rowspan="3">
    <ul>
     <li>
      North Europe
     </li>
     <li>
      Japan East
     </li>
     <li>
      West Europe
     </li>
     <li>
      Japan West
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.209.242.155
135.149.20.42</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>74.176.138.15
135.149.17.81</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Looker SFTP notifications
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>34.84.4.218
34.146.68.203
34.85.3.198</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3738" rowspan="3">
    Canada
   </td>
   <td headers="d148245e3741" rowspan="3">
    <ul>
     <li>
      North Europe
     </li>
     <li>
      Canada
                                       Central
     </li>
     <li>
      West Europe
     </li>
     <li>
      Canada East
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.209.242.155
4.174.211.111</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>130.107.208.253
130.107.10.82</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Looker SFTP notifications
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>34.152.60.210
35.203.46.255
35.234.253.103
35.203.16.100</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3738" rowspan="3">
    Singapore
   </td>
   <td headers="d148245e3741" rowspan="3">
    <ul>
     <li>
      North Europe
     </li>
     <li>
      Southeast
                                       Asia
     </li>
     <li>
      West Europe
     </li>
     <li>
      East Asia
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.209.242.155
57.158.137.134</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>20.247.146.89
57.158.190.211</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Looker SFTP notifications
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>34.87.134.202
34.143.132.206
34.143.210.116
35.185.184.54</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3738" rowspan="3">
    India
   </td>
   <td headers="d148245e3741" rowspan="3">
    <ul>
     <li>
      North Europe
     </li>
     <li>
      Central
                                       India
     </li>
     <li>
      West Europe
     </li>
     <li>
      South India
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.209.242.155
98.70.224.34</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>135.235.177.71
135.235.249.14</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Looker SFTP notifications
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>35.200.158.11
34.100.209.232
34.93.170.82</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3738" rowspan="3">
    United Kingdom
   </td>
   <td headers="d148245e3741" rowspan="3">
    <ul>
     <li>
      North Europe
     </li>
     <li>
      UK South
     </li>
     <li>
      West Europe
     </li>
     <li>
      UK West
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.209.242.155
131.145.43.57</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>74.177.240.23
85.210.75.139</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Looker SFTP notifications
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>34.147.209.63
35.197.212.7
34.142.53.66</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3738" rowspan="3">
    GXP United States of America
   </td>
   <td headers="d148245e3741" rowspan="3">
    <ul>
     <li>
      East US
     </li>
     <li>
      West US
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>134.33.240.104</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>51.8.242.246
134.33.200.238</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Looker SFTP notifications
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>35.221.62.218
34.86.34.135
35.236.240.168</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3738" rowspan="3">
    GXP Europe
   </td>
   <td headers="d148245e3741" rowspan="3">
    <ul>
     <li>
      North Europe
     </li>
     <li>
      East US
     </li>
     <li>
      West Europe
     </li>
     <li>
      West US
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>134.33.240.104
52.158.122.175</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>52.158.126.222
20.13.193.184</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Looker SFTP notifications
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>34.90.52.191
35.204.216.7
35.204.118.28</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3738" rowspan="2">
    Switzerland
   </td>
   <td headers="d148245e3741" rowspan="2">
    <ul>
     <li>
      Switzerland North
     </li>
     <li>
      North Europe
     </li>
     <li>
      West Europe
     </li>
     <li>
      Switzerland West
     </li>
    </ul>
   </td>
   <td headers="d148245e3744">
    Log Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>4.209.242.155
20.208.76.154</pre>
   </td>
  </tr>
  <tr>
   <td headers="d148245e3744">
    Real Time Data Export
   </td>
   <td headers="d148245e3747">
    <button>
     assignment
    </button>
    <pre>20.250.215.68
20.208.77.215</pre>
   </td>
  </tr>
 </tbody>
</table>

#### Limitations

For Log Export, Google Storage does not support inbound IP restriction.

Due to a limitation on Microsoft side for Log Export, you cannot set up inbound IP restriction when your Azure blob storage account and the Insights infrastructure is under the same region in Azure. Because of this, you cannot use the following regions for blob storage account based on the Insights service region:

* Insights US: North Europe, East US
* Insights Europe: North Europe, West Europe (For Community Licensing)
* Insights UK: North Europe, UK South
* Insights Canada: North Europe, Canada Central
* Insights Singapore: North Europe, Southeast Asia
* Insights India: North Europe, Central India
* Insights Australia: North Europe, Australia East
* Insights Japan: North Europe, Japan East
* Insights GXP Europe: North Europe, East US
* Insights GXP US: East US

For more information on this limitation, check the [Restrictions for IP network rules](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal#restrictions-for-ip-network-rules) page from the Microsoft Azure Blob Storage documentation.

## Integration Service

### Outbound IP ranges

Add the following outbound IP ranges to your allow list to use Integration Service and create connections, as described in the following table.

The current outbound IP ranges will be deprecated on January 26, 2026. To avoid disruption, make sure to add the outbound IP ranges listed under the **Upcoming outbound IP ranges** column before this date. TOPLEVELNOTEMARKER
  :::important
  If the upcoming outbound IP ranges are not allowed by January 26, 2026, you will be unable to use this service. Attempts to use this service may result in errors.
  :::

| Region | Existing outbound IP ranges | Upcoming outbound IP ranges | Environment |
| --- | --- | --- | --- |
| Australia | ``` 13.210.116.107 13.54.88.227 13.55.113.75 20.11.199.185* 20.167.34.255* ``` | ``` 13.75.193.84/30 13.75.193.112/30 13.77.46.56/30 13.77.40.228/30 ``` | Production |
| Canada | ``` 20.200.104.214 20.220.98.56 ``` | ``` 20.151.112.252/30 20.151.113.120/30 40.86.219.188/30 40.86.224.148/30 ``` | Production |
| Europe | ``` 34.247.224.172 108.128.2.184 54.78.70.51 20.93.15.208* 20.13.60.212* ``` | ``` 94.245.89.4/30 94.245.93.8/30 20.67.88.64/30 20.67.88.112/30 ``` | Production |
| Japan | ``` 18.180.58.90 35.72.149.94 35.75.176.28 20.89.117.202* 104.46.238.159* ``` | ``` 20.89.104.152/30 20.89.104.200/30 40.74.64.240/30 40.74.65.80/30 ``` | Production |
| India | ``` 4.224.9.5 13.71.90.136 ``` | ``` 40.80.89.64/30 40.80.89.136/30 104.211.218.152/30 104.211.222.120/30 ``` | Production |
| Singapore | ``` 20.44.206.197 ``` | ``` 104.215.184.68/30 104.215.185.96/30 ``` | Production |
| Switzerland | ``` 51.107.68.220/30 51.107.68.232/30 20.199.240.20/30 20.199.240.8/30 ``` | ``` 51.107.68.220/30 51.107.68.232/30 20.199.240.20/30 20.199.240.8/30 ``` | Production |
| United Kingdom | ``` 172.165.145.81 51.141.6.153 ``` | ``` 51.104.16.124/30 51.104.16.168/30 51.140.205.20/30 51.140.205.248/30 ``` | Production |
| United States | ``` 3.225.236.232 18.209.239.173 3.211.174.83 20.121.170.55* 20.72.203.238* ``` | ``` 13.66.167.4/30 13.66.163.204/30 104.211.63.160/30 104.211.58.236/30 ``` | Production |
| GxP United States (Delayed update organizations) | ``` 4.208.84.37 172.211.163.224 20.246.192.220 52.143.81.192 3.232.246.199 3.233.230.152 34.204.62.188 ``` | ``` 13.66.166.60/30 13.66.160.164/30 104.211.56.184/30 40.114.71.160/30 ``` | Production |
| Community | ``` 20.13.110.150 4.207.32.162 ``` | ``` 94.245.93.132/30 94.245.93.148/30 20.67.88.116/30 20.67.88.132/30 ``` | Production |

<sup>*</sup>IP addresses marked with an asterisk (*) are designated for newly incorporated Azure regions. These IPs will supersede the existing regional IPs upon completion of the scheduled tenant migration process. For details, refer to the [Integration Service release notes](https://docs.uipath.com/integration-service/automation-cloud/latest/release-notes/april-2025#scheduled-tenant-migration).

## Orchestrator

### Domains

Robots send traffic to these Test Cloud Orchestrator domains. We recommend that you allow these domains to ensure proper functioning of your automations, as described in the following table:

Robots send traffic to these Automation Cloud<sup>TM</sup> Orchestrator domains. We recommend that you allow these domains to ensure proper functioning of your automations, as described in the following table:

| Module or Functionality | Domains to Allow |
| --- | --- |
| UiPath Orchestrator | `https://cloud.uipath.com``https://orch-cdn.uipath.com``https://account.uipath.com` |
| Automation Cloud<sup>TM</sup> Robots - VM | `https://cloud.uipath.com` `https://download.uipath.com` |
| Storage | `*.blob.core.windows.net` If using Amazon s3 buckets:  `*.s3.amazonaws.com` |
| Package and library feeds  (library, tenant processes, and others) | `https://pkgs.dev.azure.com` |
| Azure SignalR | `*.service.signalr.net` |
| Studio and Robot auto-update functionality | `https://download.uipath.com` |
| Traffic Manager (internal) | `*.trafficmanager.net` |

### Outbound IP ranges

We recommend allowing these outbound IP ranges, which send traffic from Orchestrator towards your resources. For details, refer to [Orchestrator outbound IP ranges](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/orchestrator-outbound-ip-addresses).

**Community users**

| Region | CIDR | Outbound IP ranges |
| --- | --- | --- |
| Europe (European Union) | ``` 20.123.102.24/30 20.50.147.88/30 168.63.58.240/30 168.63.56.100/30 20.71.24.32/30 20.71.24.128/30 20.166.153.132/30 20.23.210.168/30 ``` | ``` 20.123.102.24 20.123.102.25 20.123.102.26 20.123.102.27 20.50.147.88 20.50.147.89 20.50.147.90 20.50.147.91 168.63.58.240 168.63.58.241 168.63.58.242 168.63.58.243 168.63.56.100 168.63.56.101 168.63.56.102 168.63.56.103 20.71.24.32 20.71.24.33 20.71.24.34 20.71.24.35 20.71.24.128 20.71.24.129 20.71.24.130 20.71.24.131 20.166.153.132 20.166.153.133 20.166.153.134 20.166.153.135 20.23.210.168 20.23.210.169 20.23.210.170 20.23.210.171 ``` |

**Enterprise users**

| Region | CIDR | Outbound IP ranges |
| --- | --- | --- |
| Australia | ``` 20.92.156.92/30 23.101.220.128/30 23.101.208.196/30 20.213.69.140/30 20.92.42.116/30 ``` | ``` 20.92.156.92 20.92.156.93 20.92.156.94 20.92.156.95 23.101.220.128 23.101.220.129 23.101.220.130 23.101.220.131 23.101.208.196 23.101.208.197 23.101.208.198 23.101.208.199 20.213.69.140 20.213.69.141 20.213.69.142 20.213.69.143 20.92.42.116 20.92.42.117 20.92.42.118 20.92.42.119 ``` |
| Canada | ``` 20.116.141.44/30 20.63.56.64/30 20.63.56.68/30 20.220.159.8/30 20.104.134.160/30 ``` | ``` 20.116.141.44 20.116.141.45 20.116.141.46 20.116.141.47 20.63.56.64 20.63.56.65 20.63.56.66 20.63.56.67 20.63.56.68 20.63.56.69 20.63.56.70 20.63.56.71 20.220.159.8 20.220.159.9 20.220.159.10 20.220.159.11 20.104.134.160 20.104.134.161 20.104.134.162 20.104.134.163 ``` |
| United States | ``` 20.124.53.40/30 20.121.182.72/30 20.121.104.124/30 40.114.108.32/30 40.114.108.220/30 20.232.224.12/30 20.66.65.144/30 ``` | ``` 20.124.53.40 20.124.53.41 20.124.53.42 20.124.53.43 20.121.182.72 20.121.182.73 20.121.182.74 20.121.182.75 20.121.104.124 20.121.104.125 20.121.104.126 20.121.104.127 40.114.108.32 40.114.108.33 40.114.108.34 40.114.108.35 40.114.108.220 40.114.108.221 40.114.108.222 40.114.108.223 20.232.224.12 20.232.224.13 20.232.224.14 20.232.224.15 20.66.65.144 20.66.65.145 20.66.65.146 20.66.65.147 ``` |
| Japan | ``` 20.210.80.72/30 52.253.104.184/30 52.253.105.76/30 20.78.114.120/30 104.215.9.124/30 ``` | ``` 20.210.80.72 20.210.80.73 20.210.80.74 20.210.80.75 52.253.104.184 52.253.104.185 52.253.104.186 52.253.104.187 52.253.105.76 52.253.105.77 52.253.105.78 52.253.105.79 20.78.114.120 20.78.114.121 20.78.114.122 20.78.114.123 104.215.9.124 104.215.9.125 104.215.9.126 104.215.9.127 ``` |
| Europe (European Union) | ``` 20.223.90.156/30 20.223.16.0/30 4.207.205.236/30 168.63.58.108/30 168.63.58.144/30 20.166.153.132/30 20.23.210.168/30 ``` | ``` 20.223.90.156 20.223.90.157 20.223.90.158 20.223.90.159 20.223.16.0 20.223.16.1 20.223.16.2 20.223.16.3 4.207.205.236 4.207.205.237 4.207.205.238 4.207.205.239 168.63.58.108 168.63.58.109 168.63.58.110 168.63.58.111 168.63.58.144 168.63.58.145 168.63.58.146 168.63.58.147 20.166.153.132 20.166.153.133 20.166.153.134 20.166.153.135 20.23.210.168 20.23.210.169 20.23.210.170 20.23.210.171 ``` |
| Singapore | ``` 104.43.98.180/30 52.230.32.132/30 52.230.32.188/30 20.198.150.140/30 ``` | ``` 104.43.98.180 104.43.98.181 104.43.98.182 104.43.98.183 52.230.32.132 52.230.32.133 52.230.32.134 52.230.32.135 52.230.32.188 52.230.32.189 52.230.32.190 52.230.32.191 20.198.150.140 20.198.150.141 20.198.150.142 20.198.150.143 ``` |
| United Kingdom | ``` 20.90.174.164/30 51.140.5.96/30 51.140.6.156/30 20.90.169.148/30 51.142.146.56/30 ``` | ``` 20.90.174.164 20.90.174.165 20.90.174.166 20.90.174.167 51.140.5.96 51.140.5.97 51.140.5.98 51.140.5.99 51.140.6.156 51.140.6.157 51.140.6.158 51.140.6.159 20.90.169.148 20.90.169.149 20.90.169.150 20.90.169.151 51.142.146.56 51.142.146.57 51.142.146.58 51.142.146.59 ``` |
| India | ``` 4.224.102.80/30 40.80.89.112/30 40.80.89.132/30 20.219.182.96/30 52.140.57.140/30 ``` | ``` 4.224.102.80 4.224.102.81 4.224.102.82 4.224.102.83 40.80.89.112 40.80.89.113 40.80.89.114 40.80.89.115 40.80.89.132 40.80.89.133 40.80.89.134 40.80.89.135 20.219.182.96 20.219.182.97 20.219.182.98 20.219.182.99 52.140.57.140 52.140.57.141 52.140.57.142 52.140.57.143 ``` |
| Switzerland | ``` 51.107.68.220/30 51.107.68.232/30 20.199.240.20/30 20.199.240.8/30 ``` | ``` 51.107.68.220 51.107.68.221 51.107.68.222 51.107.68.223 51.107.68.232 51.107.68.233 51.107.68.234 51.107.68.235 20.199.240.20 20.199.240.21 20.199.240.22 20.199.240.23 20.199.240.8 20.199.240.9 20.199.240.10 20.199.240.11 ``` |
| United Arab Emirates | ``` 40.123.215.148/30 40.123.215.168/30 20.45.67.8/30 20.45.67.20/30 ``` | ``` 40.123.215.148/30 40.123.215.168/30 20.45.67.8/30 20.45.67.20/30 ``` |

**Delayed update organizations**

| Region | CIDR | Outbound IP ranges |
| --- | --- | --- |
| Europe (European Union) | ``` 168.63.56.128/30 168.63.56.212/30 20.166.153.132/30 20.23.210.168/30 4.207.205.236/30 ``` | ``` 168.63.56.128 168.63.56.129 168.63.56.130 168.63.56.131 168.63.56.212 168.63.56.213 168.63.56.214 168.63.56.215 20.166.153.132 20.166.153.133 20.166.153.134 20.166.153.135 20.23.210.168 20.23.210.169 20.23.210.170 20.23.210.171 4.207.205.236 4.207.205.237 4.207.205.238 4.207.205.239 ``` |
| United States | ``` 40.114.109.36/30 40.114.109.64/30 20.232.224.12/30 20.66.65.144/30 20.121.104.124/30 ``` | ``` 40.114.109.36 40.114.109.37 40.114.109.38 40.114.109.39 40.114.109.64 40.114.109.65 40.114.109.66 40.114.109.67 20.232.224.12 20.232.224.13 20.232.224.14 20.232.224.15 20.66.65.144 20.66.65.145 20.66.65.146 20.66.65.147 20.121.104.124 20.121.104.125 20.121.104.126 20.121.104.127 ``` |

### MCP Servers

The remote MCP Servers service uses the outgoing IP ranges listed below for all external communications. The following table shows the available outbound IP ranges for each region.

| Region | Outbound IP ranges |
| --- | --- |
| Europe | ``` 94.245.89.4/30 94.245.93.8/30 ``` |
| Europe (Secondary) | ``` 20.67.88.64/30 20.67.88.112/30 ``` |
| Europe - Community | ``` 94.245.93.132/30 94.245.93.148/30 ``` |
| Europe - Community (Secondary) | ``` 20.67.88.116/30 20.67.88.132/30 ``` |
| US | ``` 104.211.63.160/30 104.211.58.236/30 ``` |
| US (Secondary) | ``` 13.66.167.4/30 13.66.163.204/30 ``` |
| Canada | ``` 20.151.112.252/30 20.151.113.120/30 ``` |
| Canada (Secondary) | ``` 40.86.219.188/30 40.86.224.148/30 ``` |
| Singapore | ``` 104.215.184.68/30 104.215.185.96/30 ``` |
| Japan | ``` 20.89.104.152/30 20.89.104.200/30 ``` |
| Japan (Secondary) | ``` 40.74.64.240/30 40.74.65.80/30 ``` |
| Australia | ``` 13.75.193.84/30 13.75.193.112/30 ``` |
| Australia (Secondary) | ``` 13.77.46.56/30 13.77.40.228/30 ``` |
| India | ``` 40.80.89.64/30 40.80.89.136/30 ``` |
| India (Secondary) | ``` 104.211.218.152/30 104.211.222.120/30 ``` |
| UK | ``` 51.104.16.124/30 51.104.16.168/30 ``` |
| UK (Secondary) | ``` 51.140.205.20/30 51.140.205.248/30 ``` |
| GXP Europe | ``` 94.245.93.164/30 94.245.93.196/30 ``` |
| GXP Europe (Secondary) | ``` 20.67.88.148/30 20.67.88.164/30 ``` |
| GXP US | ``` 104.211.56.184/30 40.114.71.160/30 ``` |
| GXP US (Secondary) | ``` 13.66.166.60/30 13.66.160.164/30 ``` |

## Process Mining

### Domains

The following table lists the domains used by Process Mining:

| Module or Scenario | Domains to Allow |
| --- | --- |
| Identity Server | `https://cloud.uipath.com` |
| Static assets | `https://fonts.googleapis.com`  `https://fonts.gstatic.com`  `https://content.usage.uipath.com`  `https://s.gravatar.com`  `https://i1.wp.com` |
| Azure SignalR | `*.service.signalr.net` |
| Telemetry | `https://*.in.applicationinsights.azure.com` |
| Upload files | `*.blob.core.windows.net` |

## Solutions

### Domains

The following table lists the domains used by Solutions:

| Scenario | Domains to Allow |
| --- | --- |
| Navigate to the Solutions Management page | `https://cloud.uipath.com`  `https://fonts.googleapis.com`  `https://fonts.gstatic.com`  `https://dc.services.visualstudio.com`  `api.smartling.com`  `use.typekit.net`  `p.typekit.net`  `s.gravatar.com`  `i2.wp.com`  `https://platform-cdn.uipath.com`  `https://sol-cdn.uipath.com`  `https://solutions.uipath.com` |
| Storage | `*.blob.core.windows.net` |
| Azure SignalR | `*.service.signalr.net` |

## Studio Web

### Domains

The following table lists the domains used by Studio Web:

| Module or Functionality | Domains to Allow |
| --- | --- |
| Azure SignalR | `wss://*.service.signalr.net`  `https://*.service.signalr.net`  `wss://*.trafficmanager.net` |
| UiPath products | `https://*.uipath.com` |
| UiPath products (in-app feedback) | `https://studio-feedback.azure-api.net` |
| UiPath products (static assets) | `https://platform-cdn.uipath.com`  `https://content.usage.uipath.com`  `https://fonts.gstatic.com`  `https://d2c7xlmseob604.cloudfront.net`  `https://fonts.googleapis.com/`  `https://*.typekit.net`  `https://fonts.gstatic.com`  `https://s.gravatar.com`  `https://secure.gravatar.com`  `https://*.wp.com`  `https://*.googleusercontent.com`  `https://i.ytimg.com` |
| UiPath products (telemetry) | `https://data.usage.uipath.com` |
| Third-party services (clickable guides) | `https://*.pendo.io` |
| Third-party services (storage) | `https://*.blob.core.windows.net`  `https://*.amazonaws.com` |
| Third-party services (telemetry) | `https://dc.services.visualstudio.com` |
| Third-party services (translations helper) | `https://api.smartling.com` |

## Task Mining

### Domains

If your company uses proxies, the URLs, described in the following table, need to be added to the Firewall Exceptions so the Task Mining desktop components connect to our web servers.
:::note
The Task Mining Desktop application uses web sockets for real-time communication with the server (telemetry and governance). For the URLs and IPs to be allowed, the transparent proxy is expected to have the HTTPS and WSS protocols enabled.
:::

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87_TABLE_VWH_ZNV_QHC" summary="">
 <colgroup>
  <col/>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Component
   </th>
   <th>
    URL
   </th>
   <th>
    Port
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6056">
    Admin Portal
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6062">
    <code>
     https://cloud.uipath.com
    </code>
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6068">
    443
   </td>
  </tr>
  <tr>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6056">
    Web Portal
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6062">
    <code>
     *.blob.core.windows.net
    </code>
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6068">
    443
   </td>
  </tr>
  <tr>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6056">
    Pendo
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6062">
    <code>
     https://content.usage.uipath.com
    </code>
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6068">
    443
   </td>
  </tr>
  <tr>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6056">
    Azure App Insights
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6062">
    <p>
     <code>
      dc.services.visualstudio.com
     </code>
    </p>
    <p>
     <code>
      dc.applicationinsights.azure.com
     </code>
    </p>
    <p>
     <code>
      dc.applicationinsights.microsoft.com
     </code>
    </p>
    <p>
     <code>
      dc.services.visualstudio.com
     </code>
    </p>
    <p>
     <code>
      *.in.applicationinsights.azure.com
     </code>
    </p>
    <p>
     <code>
      live.applicationinsights.azure.com
     </code>
    </p>
    <p>
     <code>
      rt.applicationinsights.microsoft.com
     </code>
    </p>
    <p>
     <code>
      rt.services.visualstudio.com
     </code>
    </p>
    <p>
     <code>
      {region}.livediagnostics.monitor.azure.com
     </code>
    </p>
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6068">
    443
   </td>
  </tr>
  <tr>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6056">
    Azure Signalr
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6062">
    <ul>
     <li>
      <p>
       <code>
        service.signalr.net
       </code>
      </p>
      <p>
       <code>
        *.service.signalr.net
       </code>
      </p>
     </li>
    </ul>
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6068">
    443
   </td>
  </tr>
  <tr>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6056">
    Avatars
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6062">
    <code>
     i2.wp.com/cdn.auth0.com/avatars
    </code>
   </td>
   <td headers="GUID-3DB88B5E-1DEB-48B8-9EDB-12D0BFEAFF87__D109718E6068">
    443
   </td>
  </tr>
 </tbody>
</table>

## Test Manager

This section lists the domains used by Test Manager and the outbound IP ranges that you should consider allowing if you want to use various Test Manager capabilities.

### Domains

The following table lists the domains used by Test Manager that we recommend allowing, based on the functionality you plan to use:

| Module or functionality | Domains to allow |
| --- | --- |
| UiPath Test Manager | `https://cloud.uipath.com` |
| Azure SignalR | `*.service.signalr.net` |

### Outbound IP ranges for RFC connection

Allow the following outbound IP ranges to establish communication between UiPath Test Manager and your SAP system via an RFC connection. The following table shows the available outbound IP ranges for each region. TOPLEVELNOTEMARKER
  :::important
  Starting January 26, 2026, **existing outbound IP ranges** for this service are being gradually replaced based on your organization’s hosted region. Ensure that the **upcoming outbound IP ranges** are allowed in your firewall to prevent service disruptions. Refer to the [UiPath Status page](https://status.uipath.com/) for regional rollout updates.
  :::

| Region | Current outbound IP ranges | Upcoming outbound IP ranges |
| --- | --- | --- |
| Australia | ``` 20.167.34.255/32 20.11.199.185/32 ``` | ``` 13.75.193.84/30 13.75.193.112/30 13.77.46.56/30 13.77.40.228/30 ``` |
| Canada | ``` 20.200.104.214/32 20.220.98.56/32 ``` | ``` 20.151.112.252/30 20.151.113.120/30 40.86.219.188/30 40.86.224.148/30 ``` |
| Europe (European Union) | ``` 20.93.15.208/32 20.13.60.212/32 ``` | ``` 94.245.89.4/30 94.245.93.8/30 20.67.88.64/30 20.67.88.112/30 ``` |
| India | ``` 4.224.9.5/32 13.71.90.136/32 ``` | ``` 40.80.89.64/30 40.80.89.136/30 104.211.218.152/30 104.211.222.120/30 ``` |
| GXP United States | ``` 52.143.81.192/32 20.246.192.220/32 ``` | ``` 13.66.166.60/30 13.66.160.164/30 104.211.56.184/30 40.114.71.160/30 ``` |
| Japan | ``` 20.89.117.202/32 104.46.238.159/32 ``` | ``` 20.89.104.152/30 20.89.104.200/30 40.74.64.240/30 40.74.65.80/30 ``` |
| Singapore | ``` 20.44.206.197/32 ``` | ``` 104.215.184.68/30 104.215.185.96/30 ``` |
| United Kingdom | ``` 172.165.145.81/32 51.141.6.153/32 ``` | ``` 51.104.16.124/30 51.104.16.168/30 51.140.205.20/30 51.140.205.248/30 ``` |
| United States | ``` 20.72.203.238/32 20.121.170.55/32 ``` | ``` 13.66.167.4/30 13.66.163.204/30 104.211.63.160/30 104.211.58.236/30 ``` |

### Outbound IP ranges for web service connection

Allow the following static outbound IP ranges to enable the communication between UiPath Test Manager and your SAP system, via a web service connection.

Allow these outbound IP ranges through your firewall:

| Regions | Outbound IP ranges |
| --- | --- |
| Australia | ``` 20.213.69.140/30 20.92.42.116/30 ``` |
| Canada | ``` 20.220.159.8/30 20.104.134.160/30 ``` |
| Community | ``` 20.166.153.132/30 20.23.210.168/30 ``` |
| European Union | ``` 20.166.153.132/30 20.23.210.168/30 ``` |
| European Union (delayed) | ``` 20.166.153.132/30 20.23.210.168/30 ``` |
| India | ``` 20.219.182.96/30 52.140.57.140/30 ``` |
| Japan | ``` 20.78.114.120/30 104.215.9.124/30 ``` |
| Singapore | ``` 20.198.150.140/30 52.140.57.140/30 ``` |
| United Kingdom | ``` 20.90.169.148/30 51.142.146.56/30 ``` |
| United States | ``` 20.232.224.12/30 20.66.65.144/30 ``` |
| United States (delayed) | ``` 20.232.224.12/30 20.66.65.144/30 ``` |

### Outbound IP ranges for connectors

If you enhance your system's security with a firewall, consider allowing only Test Manager outbound IP ranges for using out-of-the-box connectors.

The following outbound IP ranges apply to all supported regions, including: Australia, Canada, European Union, India, Japan, Singapore, United Kingdom, United States, and GxP United States (delayed).

Allow these outbound IP ranges through your firewall:

| Regions | Outbound IP ranges |
| --- | --- |
| Australia, Canada, European Union, India, Japan, Singapore, United Kingdom, United States, and GxP United States (delayed) | ``` 20.92.42.116/30 20.213.69.140/30 20.220.159.8/30 20.104.134.160/30 20.23.210.168/30 20.166.153.132/30 20.219.182.96/30 52.140.57.140/30 20.66.65.144/30 20.232.224.12/30 104.215.9.124/30 20.78.114.120/30 20.198.150.140/30 51.142.146.56/30 20.90.169.148/30 ``` |