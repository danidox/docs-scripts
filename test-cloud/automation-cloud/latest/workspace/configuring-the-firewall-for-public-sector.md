---
title: "Configuring the firewall for Automation Cloud
            Public Sector"
visible: true
slug: "configuring-the-firewall-for-public-sector"
---

For general network configuration and firewall information, refer to [Configuring the firewall](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-firewall#configuring-the-firewall)

## Test Cloud Public Sector Portal

The following table lists the domains used by Test Cloud Public Sector Portal:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__TABLE_K5R_S3Y_C3C" summary="">
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
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E57">
    UiPath Automation Cloud Public Sector
   </td>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E60">
    <ul>
     <li>
      <code>
       https://govcloud.uipath.us
      </code>
     </li>
     <li>
      <code>
       https://govcloud.uipath.us/portal_/cloudrpa
      </code>
     </li>
     <li>
      <code>
       https://govcloud.uipath.us/portal_/signinwithsso
      </code>
     </li>
     <li>
      <code>
       https://govcloud.uipath.us/&lt;accountname&gt;/
      </code>
     </li>
     <li>
      <code>
       https://govcloud.uipath.us/&lt;accountname&gt;/&lt;tenantname&gt;/portal
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E57">
    Login flows (configured via SSO)
   </td>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E60">
    <ul>
     <li>
      <code>
       https://login.microsoftonline.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E57">
    Sign in with Azure Active Directory (Azure AD)
   </td>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E60">
    <ul>
     <li>
      <code>
       https://aadcdn.msftauth.net
      </code>
     </li>
     <li>
      <code>
       https://govcloud.uipath.us
      </code>
     </li>
     <li>
      <code>
       https://login.microsoftonline.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E57">
    Sign in with UiPath Assistant (basic email)
   </td>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E60">
    <ul>
     <li>
      <code>
       *-signalr.service.signalr.net
      </code>
     </li>
    </ul>
    <p>
     For events related to signing in with basic authentication:
    </p>
    <ul>
     <li>
      <code>
       https://account.uipath.com
      </code>
     </li>
     <li>
      <code>
       https://govcloud.uipath.us
      </code>
     </li>
     <li>
      <code>
       https://platform-cdn.uipath.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E57">
    Sign in with UiPath Studio (basic email)
   </td>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E60">
    <ul>
     <li>
      <code>
       https://api.nuget.org
      </code>
     </li>
     <li>
      <code>
       *-signalr.service.signalr.net
      </code>
     </li>
     <li>
      <code>
       https://gallery.uipath.com
      </code>
     </li>
     <li>
      <code>
       https://pkgs.dev.azure.com
      </code>
     </li>
    </ul>
    <p>
     For events related to signing in with basic authentication:
    </p>
    <ul>
     <li>
      <code>
       https://account.uipath.com
      </code>
     </li>
     <li>
      <code>
       https://govcloud.uipath.us
      </code>
     </li>
     <li>
      <code>
       https://platform-cdn.uipath.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E57">
    Static assets: Fonts, Styling and CDN hosted scripts
   </td>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E60">
    <p>
     Fonts:
    </p>
    <ul>
     <li>
      <code>
       https://use.typekit.net
      </code>
     </li>
     <li>
      <code>
       https://fonts.gstatic.com
      </code>
     </li>
     <li>
      <code>
       https://platform-cdn.uipath.com
      </code>
     </li>
    </ul>
    <p>
     Images:
    </p>
    <ul>
     <li>
      <code>
       https://s.gravatar.com
      </code>
     </li>
     <li>
      <code>
       https://secure.gravatar.com
      </code>
     </li>
     <li>
      <code>
       https://*.wp.com
      </code>
     </li>
     <li>
      <code>
       https://*.googleusercontent.com
      </code>
     </li>
     <li>
      <code>
       https://i.ytimg.com
      </code>
     </li>
     <li>
      <code>
       https://platform-cdn.uipath.com
      </code>
     </li>
    </ul>
    <p>
     CSS:
    </p>
    <ul>
     <li>
      <code>
       https://fonts.googleapis.com/css
      </code>
     </li>
     <li>
      <code>
       https://use.typekit.net
      </code>
     </li>
     <li>
      <code>
       https://p.typekit.net
      </code>
     </li>
     <li>
      <code>
       https://platform-cdn.uipath.com
      </code>
     </li>
     <li>
      <code>
       https://staticresources.uipath.us
      </code>
     </li>
    </ul>
    <p>
     Scripts:
    </p>
    <ul>
     <li>
      <code>
       https://primer.typekit.net
      </code>
     </li>
     <li>
      <code>
       https://use.typekit.net
      </code>
     </li>
     <li>
      <code>
       https://platform-cdn.uipath.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E57">
    Sign in via Auth0 (for EU)
   </td>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E60">
    <ul>
     <li>
      <code>
       uipath.eu.auth0.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E57">
    Update services
   </td>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E60">
    <ul>
     <li>
      <code>
       ctldl.windowsupdate.com
      </code>
     </li>
    </ul>
    <p>
     To configure network connections, use
     <a href="https://learn.microsoft.com/en-us/windows-server/administration/windows-server-update-services/deploy/2-configure-wsus#21-configure-network-connections">
      Microsoft
                                    documentation
     </a>
     .
    </p>
   </td>
  </tr>
  <tr>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E57">
    App Insights / Google Tag Manager
   </td>
   <td headers="GUID-825FE83D-9058-47CC-A883-17A91B43BC51__D58705E60">
    <ul>
     <li>
      <code>
       https://usgovvirginia-0.in.applicationinsights.azure.us
      </code>
     </li>
     <li>
      <code>
       https://www.googletagmanager.com/gtm.js?id=GTM-PLLP8P
      </code>
     </li>
     <li>
      <code>
       https://code.jquery.com/jquery-3.5.1.min.js
      </code>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>
:::important
If you use Azure buckets, they must not be located in the tenant's region or in the failover region.
:::

### Outbound IP ranges

To ensure proper functionality for UiPath services, we recommend allowing the following IPs:

```
52.247.128.100
52.227.65.197
52.245.221.122
```

## Action Center

### Domains

The following table lists the domains used by Action Center that we recommend allowing, based on the functionality you plan to use:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-68CE822E-48E9-438E-8334-D9722D794953__GUID-CE6E150D-8DBF-4228-91C9-DDC81CF8798A_TABLE_JKC_P4Q_3BC" summary="">
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
   <td headers="GUID-68CE822E-48E9-438E-8334-D9722D794953__D58705E394">
    Navigate to Action Center page
   </td>
   <td headers="GUID-68CE822E-48E9-438E-8334-D9722D794953__D58705E397">
    <ul>
     <li>
      <code>
       https://govcloud.uipath.us/&lt;accountName&gt;/&lt;tenantName&gt;/actions_
      </code>
     </li>
     <li>
      <code>
       https://govcloud.uipath.us/&lt;accountName&gt;/&lt;tenantName&gt;/processes_
      </code>
     </li>
     <li>
      <code>
       https://govcloud.uipath.us/&lt;accountName&gt;/&lt;tenantName&gt;/bupproxyservice_
      </code>
     </li>
     <li>
      <code>
       https://uipath-acc-pgov.uipath.us
      </code>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

## Automation Cloud Robots - Serverless

### Static IP configuration

Static IP for Cloud Robot - Serverless enables you to route outbound network traffic through a dedicated, static IP address range managed by UiPath. This allows you to whitelist or securely integrate with external systems that restrict incoming connections to known IPs.

### Configuration

You can enable Static IP while [creating the Serverless template](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/executing-unattended-automations-with-serverless-robots#step-2-adding-serverless-robots-to-your-tenant) and going to the **Network Configuration** page.

### Availability

The Stable IP feature is available for Cloud Robot - Serverless in supported regions.

These static IP addresses can sometimes change as a result of infrastructure deployments. To help keep you on top of any changes, we have compiled a list of up-to-date static egress IPs, which you can check in the following tables.

Table 1. Community users

| Region | CIDR | Outbound IP ranges |
| --- | --- | --- |
| Europe | ``` 20.191.43.0/30 20.191.42.240/30 ``` | ``` 20.191.43.0 20.191.43.1 20.191.43.2 20.191.43.3 20.191.42.240 20.191.42.241 20.191.42.242 20.191.42.243 ``` |

Table 2. Enterprise users

| Region | CIDR | Outbound IP ranges |
| --- | --- | --- |
| Australia | ``` 20.53.170.116/30 20.53.170.208/30 ``` | ``` 20.53.170.116 20.53.170.117 20.53.170.118 20.53.170.119 20.53.170.208 20.53.170.209 20.53.170.210 20.53.170.211 ``` |
| United States | ``` 20.102.5.168/30 20.102.0.76/30 ``` | ``` 20.102.5.168 20.102.5.169 20.102.5.170 20.102.5.171 20.102.0.76 20.102.0.77 20.102.0.78 20.102.0.79 ``` |
| Japan | ``` 20.44.188.168/30 20.44.185.192/30 ``` | ``` 20.44.188.168 20.44.188.169 20.44.188.170 20.44.188.171 20.44.185.192 20.44.185.193 20.44.185.194 20.44.185.195 ``` |
| Europe (European Union) | ``` 20.191.46.104/30 20.191.43.60/30 ``` | ``` 20.191.46.104 20.191.46.105 20.191.46.106 20.191.46.107 20.191.43.60 20.191.43.61 20.191.43.62 20.191.43.63 ``` |

## Automation Hub

### Domains

The following table lists the domains used by Automation Hub:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-B048F532-2682-4D9F-BB9E-BDC490F5CF0D__GUID-C1DFBEE3-697E-4036-B2A0-CFD693F34332_TABLE_NW5_14Y_PBC" summary="">
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
   <td headers="GUID-B048F532-2682-4D9F-BB9E-BDC490F5CF0D__D58705E648">
    Navigate to the Automation Hub page
   </td>
   <td headers="GUID-B048F532-2682-4D9F-BB9E-BDC490F5CF0D__D58705E650">
    <ul>
     <li>
      <p>
       <code>
        https://govcloud.uipath.us
       </code>
      </p>
     </li>
     <li>
      <code>
       http://*.userpilot.io
      </code>
     </li>
     <li>
      <p>
       <code>
        https://dc.services.visualstudio.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://ah-prod-ts-blue-eu.uipath.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://ah-prod-ts-blue-us.uipath.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://ah-prod-ts-blue-ja.uipath.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://ah-prod-ts-blue-au.uipath.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://ah-prod-ts-blue-ca.uipath.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://ah-prod-ts-blue-sea.uipath.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://ah-prod-ts-blue-uk.uipath.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://ah-prod-ts-blue-in.uipath.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://ah-gxp-ts-blue-us.uipath.com
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-B048F532-2682-4D9F-BB9E-BDC490F5CF0D__D58705E648">
    Use OpenAPI for Automation Hub
   </td>
   <td headers="GUID-B048F532-2682-4D9F-BB9E-BDC490F5CF0D__D58705E650">
    <ul>
     <li>
      <code>
       https://automation-hub.uipath.com
      </code>
     </li>
     <li>
      <code>
       http://ah-gxp-openapi-us.uipath.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-B048F532-2682-4D9F-BB9E-BDC490F5CF0D__D58705E648">
    Access Public Sector in Automation Hub
   </td>
   <td headers="GUID-B048F532-2682-4D9F-BB9E-BDC490F5CF0D__D58705E650">
    <ul>
     <li>
      https://govcloud.uipath.us
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

## Automation Ops

### Domains

The following table lists the domains used by Automation Ops:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-D6D5344C-91FF-4FAD-84DF-7AD1D51055C1__TABLE_T5C_LJY_C3C" summary="">
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
   <td headers="GUID-D6D5344C-91FF-4FAD-84DF-7AD1D51055C1__D58705E772">
    Navigate to the Automation Ops page
   </td>
   <td headers="GUID-D6D5344C-91FF-4FAD-84DF-7AD1D51055C1__D58705E775">
    <ul>
     <li>
      <code>
       https://usgovvirginia-0.in.applicationinsights.azure.us
      </code>
     </li>
     <li>
      <code>
       https://govcloud.uipath.us
      </code>
     </li>
     <li>
      <code>
       https://staticresources.uipath.us
      </code>
     </li>
     <li>
      <code>
       *-signalr.signalr.azure.us
      </code>
     </li>
     <li>
      <code>
       https://use.typekit.net
      </code>
     </li>
     <li>
      <code>
       https://p.typekit.net
      </code>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

## Data Service

### Domains

The following table lists the domains used by Data Service:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-09CB3F00-88CE-4DC6-86BE-36B90B0629B7__TABLE_IDW_LJY_C3C" summary="">
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
   <td headers="GUID-09CB3F00-88CE-4DC6-86BE-36B90B0629B7__D58705E819">
    All Data Service operations
   </td>
   <td headers="GUID-09CB3F00-88CE-4DC6-86BE-36B90B0629B7__D58705E822">
    <ul>
     <li>
      <p>
       <code>
        https://govcloud.uipath.us
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-09CB3F00-88CE-4DC6-86BE-36B90B0629B7__D58705E819">
    Fetching static frontend content
   </td>
   <td headers="GUID-09CB3F00-88CE-4DC6-86BE-36B90B0629B7__D58705E822">
    <ul>
     <li>
      <p>
       <code>
        https://staticds.uipath.us
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

## Document Understanding

### Domains

The following table lists the domains used by Document Understanding:

| Module or Scenario | Domains to Allow |
| --- | --- |
| Network and Storage | `https://*.uipath.us` |
| Telemetry and SignalR | `https://*.azure.us` |
| Public endpoints | Check the [Public endpoints](https://docs.uipath.com/document-understanding/automation-cloud-public-sector/latest/user-guide/public-endpoints) page for the full list of public endpoints URLs. |

## Insights

### Domains

The following table lists the domains used by Insights:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-A2A8BEF5-1AE3-4A78-9D97-1FC44E9AA443__GUID-29D72617-769B-4F8B-9BE4-618C59FC146C_TABLE_JKC_P4Q_3BC" summary="">
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
   <td headers="GUID-A2A8BEF5-1AE3-4A78-9D97-1FC44E9AA443__D58705E907">
    Navigate to the Insights page
   </td>
   <td headers="GUID-A2A8BEF5-1AE3-4A78-9D97-1FC44E9AA443__D58705E910">
    <ul>
     <li>
      <p>
       <code>
        https://govcloud.uipath.us
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://*.lookercdn.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://uipath-insights-statics.azureedge.net/
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://*.looker.uipath.com/
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

### Outbound static IP ranges

Outbound static IP ranges allow you to add a list of IPs for the Log Export functionality to the allowlist and not open your network to all external IPs.

To ensure proper performance for the Log Export functionality, make sure to add the [Outbound IP ranges](https://docs.uipath.com/automation-cloud-public-sector/automation-cloud-public-sector/latest/admin-guide/configuring-firewall#outbound-ips) from the **Test Cloud Public Sector Portal** section to the allowlist.

Due to a limitation on Microsoft side for Log Export, you cannot set up inbound IP restriction when your Azure blob storage account and the Insights infrastructure is under the same region in Azure. Because of this, you cannot use the USGov Virginia region for the blob storage account. For more information on this limitation, check the [Restrictions for IP network rules](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal#restrictions-for-ip-network-rules) page from the Microsoft Azure Blob Storage documentation.

## Orchestrator

### Domains

Robots send traffic to these Automation Cloud<sup>TM</sup> Public Sector Orchestrator domains. We recommend that you allow them to ensure proper functioning of your automations, as described in the following table:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__GUID-0973690E-3C06-45C6-A183-D2D568608B96_TABLE_RRR_ZKV_JBC" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Module or Functionality
   </th>
   <th>
    Domains to Allow
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1010">
    UiPath Orchestrator
   </td>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1013">
    <ul>
     <li>
      <code>
       https://govcloud.uipath.us
      </code>
     </li>
     <li>
      <code>
       https://orch-cdn.uipath.com
      </code>
     </li>
     <li>
      <code>
       https://account.uipath.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1010">
    Automation Cloud
    <sup>
     TM
    </sup>
    Public Sector Robots - VM
   </td>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1013">
    <ul>
     <li>
      <p>
       <code>
        https://govcloud.uipath.us
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://download.uipath.com
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1010">
    Storage
   </td>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1013">
    <p>
     If using Amazon s3 buckets:
    </p>
    <ul>
     <li>
      <code>
       *.s3.amazonaws.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1010">
    <p>
     Package and library feeds
    </p>
    <p>
     (library, tenant processes, and others)
    </p>
   </td>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1013">
    <ul>
     <li>
      <code>
       https://pkgs.dev.azure.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1010">
    Azure SignalR
   </td>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1013">
    <ul>
     <li>
      <code>
       *.service.signalr.net
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1010">
    Studio and Robot auto-update functionality
   </td>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1013">
    <ul>
     <li>
      <code>
       https://download.uipath.com
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1010">
    Traffic Manager (internal)
   </td>
   <td headers="GUID-B8F576A9-89BE-4979-BFAF-02DF63975579__D58705E1013">
    <ul>
     <li>
      <code>
       *.trafficmanager.net
      </code>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

## Process Mining

### Domains

The following table lists the domains used by Process Mining:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__TABLE_OPR_5JY_C3C" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Module or Scenario
   </th>
   <th>
    Domains to Allow
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__D58705E1139">
    Identity Server
   </td>
   <td headers="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__D58705E1141">
    <ul>
     <li>
      <p>
       <code>
        https://govcloud.uipath.us
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__D58705E1139">
    Static assets
   </td>
   <td headers="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__D58705E1141">
    <ul>
     <li>
      <p>
       <code>
        https://fonts.googleapis.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://fonts.gstatic.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://content.usage.uipath.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://s.gravatar.com
       </code>
      </p>
     </li>
     <li>
      <p>
       <code>
        https://i1.wp.com
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__D58705E1139">
    Azure SignalR
   </td>
   <td headers="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__D58705E1141">
    <ul>
     <li>
      <p>
       <code>
        *.signalr.azure.us
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__D58705E1139">
    Telemetry
   </td>
   <td headers="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__D58705E1141">
    <ul>
     <li>
      <p>
       <code>
        https://*.in.applicationinsights.azure.us
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__D58705E1139">
    Upload files
   </td>
   <td headers="GUID-469D48B5-77BA-42BA-8C0E-C064AE156B1D__D58705E1141">
    <ul>
     <li>
      <p>
       <code>
        *.blob.core.usgovcloudapi.net
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

## Test Manager

### Domains

The following table lists the domains used by Test Manager that we recommend allowing, based on the functionality you plan to use:

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-322882BE-3B2B-4A32-B72B-81F70E20FFE0__GUID-33F7A285-BBD0-49F6-A586-B0E6EB51AC2A_TABLE_N3P_1VG_2BC" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Module or functionality
   </th>
   <th>
    Domains to allow
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="GUID-322882BE-3B2B-4A32-B72B-81F70E20FFE0__D58705E1253">
    UiPath Test Manager
   </td>
   <td headers="GUID-322882BE-3B2B-4A32-B72B-81F70E20FFE0__D58705E1256">
    <ul>
     <li>
      <p>
       <code>
        https://govcloud.uipath.us
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="GUID-322882BE-3B2B-4A32-B72B-81F70E20FFE0__D58705E1253">
    Azure SignalR
   </td>
   <td headers="GUID-322882BE-3B2B-4A32-B72B-81F70E20FFE0__D58705E1256">
    <ul>
     <li>
      <p>
       <code>
        <code>
         *.signalr.azure.us
        </code>
       </code>
      </p>
     </li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>