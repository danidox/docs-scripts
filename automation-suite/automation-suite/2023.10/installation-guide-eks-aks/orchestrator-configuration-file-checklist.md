---
title: "Orchestrator appSettings"
visible: true
slug: "orchestrator-configuration-file-checklist"
---

## What Orchestrator settings are available?

Standalone Orchestrator settings are stored in the `UiPath.Ochestrator.dll.config` file. For a complete list of standalone Orchestrator settings, see [UiPath.Orchestrator.dll.config](https://docs.uipath.com/orchestrator/standalone/2023.10/installation-guide/uipath-orchestrator-dll-config).

Note that some of these settings are not available in Automation Suite for one of the following reasons:

* The related feature is no longer supported (e.g. `DefaultFolderIsClassic`);
* The setting is managed at cluster level, and modifying it could disrupt the integration of Orchestrator with other services (e.g. `LoadBalancer.UseRedis`);
* There is another way to change that setting, such as via ArgoCD parameters.

## What Orchestrator settings I must not change?

The following table lists the parameters that were initially available in `UiPath.Orchestrator.dll.config` file but that you cannot or must not change in Automation Suite:

Expand Table

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
     Area
    </p>
   </th>
   <th>
    <p>
     Settings you must not change
    </p>
   </th>
   <th>
    <p>
     Alternative configuration
    </p>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d71922e56">
    <p>
     Storage
    </p>
   </td>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       Storage.Type
      </code>
     </li>
     <li>
      <code>
       Storage.Location
      </code>
     </li>
    </ul>
   </td>
   <td headers="d71922e62">
    We strongly recommend using the cluster-level storage configuration. This allows Orchestrator to be automatically configured.
                                 For more advanced storage configuration, see
    <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/overriding-cluster-level-storage-configuration#overriding-cluster-level-storage-configuration">
     Overriding cluster-level storage configuration
    </a>
    .
   </td>
  </tr>
  <tr>
   <td headers="d71922e56" rowspan="2">
    <p>
     Credential stores
    </p>
   </td>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       Plugins.SecureStores.Path
      </code>
     </li>
    </ul>
   </td>
   <td headers="d71922e62" rowspan="2">
    Changing
    <code>
     Plugins.SecureStores.Path
    </code>
    can break the custom credential store plugins. To configure credential stores plugins, see
    <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-credential-stores#configuring-credential-stores">
     Configuring credential stores
    </a>
    .
   </td>
  </tr>
  <tr>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       Plugins.SecureStores.CyberArk.CLIPasswordSDKExePath
      </code>
     </li>
     <li>
      <code>
       Plugins.SecureStores.CyberArk.UsePowerShellCLI
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d71922e56">
    Encryption key
   </td>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       EncryptionKey
      </code>
     </li>
    </ul>
   </td>
   <td headers="d71922e62">
    To migrate
    <code>
     EncryptionKey
    </code>
    from an existing Orchestrator, see
    <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/migrating-standalone-orchestrator#step-6%3A-migrating-standalone-orchestrator">
     Migrating Orchestrator
    </a>
    .
   </td>
  </tr>
  <tr>
   <td headers="d71922e56">
    <p>
     Robot logs
    </p>
   </td>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       Logs.RobotLogs.ReadTarget
      </code>
     </li>
    </ul>
   </td>
   <td headers="d71922e62">
    To configure robot logs, see
    <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/saving-robot-logs-to-elasticsearch#saving-robot-logs-to-elasticsearch">
     Saving robot logs to elasticsearch
    </a>
    .
   </td>
  </tr>
  <tr>
   <td headers="d71922e56">
    <p>
     Azure key vault
    </p>
   </td>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       Azure.KeyVault.ClientId
      </code>
     </li>
     <li>
      <code>
       Azure.KeyVault.CertificateThumbprint
      </code>
     </li>
     <li>
      <code>
       Azure.KeyVault.VaultAddres
      </code>
     </li>
     <li>
      <code>
       Azure.KeyVault.DirectoryId
      </code>
     </li>
    </ul>
   </td>
   <td headers="d71922e62">
    To configure
    <code>
     EncryptionKeyPerTenant.Enabled
    </code>
    and
    <code>
     EncryptionKeyPerTenant.KeyProvider
    </code>
    , see
    <a href="https://docs.uipath.com/automation-suite/automation-suite/2023.10/installation-guide-eks-aks/configuring-encryption-key-per-tenant#configuring-encryption-key-per-tenant">
     Configuring encryption key per tenant
    </a>
    .
   </td>
  </tr>
  <tr>
   <td headers="d71922e56">
    <p>
     Identity Server
    </p>
   </td>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       IdentityServer.Integration.Enabled
      </code>
     </li>
     <li>
      <code>
       IdentityServer.CloudIntegration.Enabled
      </code>
     </li>
     <li>
      <code>
       IdentityServer.Integration.Authority
      </code>
     </li>
     <li>
      <code>
       IdentityServer.Integration.ClientId
      </code>
     </li>
     <li>
      <code>
       IdentityServer.Integration.ClientSecret
      </code>
     </li>
     <li>
      <code>
       IdentityServer.Integration.UserOrchestratorApiAudience
      </code>
     </li>
     <li>
      <code>
       IdentityServer.S2SIntegration.Enabled
      </code>
     </li>
     <li>
      <code>
       IdentityServer.Integration.S2SOrchestratorApiAudience
      </code>
     </li>
    </ul>
   </td>
   <td headers="d71922e62">
    <p>
     N/A
    </p>
   </td>
  </tr>
  <tr>
   <td headers="d71922e56" rowspan="3">
    <p>
     Authentication
    </p>
   </td>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       ExternalAuth.System.OpenIdConnect.Enabled
      </code>
     </li>
     <li>
      <code>
       ExternalAuth.System.OpenIdConnect.Authority
      </code>
     </li>
     <li>
      <code>
       ExternalAuth.System.OpenIdConnect.ClientId
      </code>
     </li>
     <li>
      <code>
       ExternalAuth.System.OpenIdConnect.ClientSecret
      </code>
     </li>
     <li>
      <code>
       ExternalAuth.System.OpenIdConnect.RedirectUri
      </code>
     </li>
     <li>
      <code>
       ExternalAuth.System.OpenIdConnect.PostLogoutRedirectUri
      </code>
     </li>
    </ul>
   </td>
   <td headers="d71922e62" rowspan="3">
    N/A
   </td>
  </tr>
  <tr>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       WindowsAuth.Enabled
      </code>
     </li>
     <li>
      <code>
       WindowsAuth.Domain
      </code>
     </li>
     <li>
      <code>
       WindowsAuth.GroupMembershipCacheExpireHours
      </code>
     </li>
     <li>
      <code>
       WindowsAuth.ConvertUsersAtLogin
      </code>
     </li>
     <li>
      <code>
       Auth.Bearer.Basic.Expire
      </code>
     </li>
     <li>
      <code>
       Auth.DisabledPermissions
      </code>
     </li>
     <li>
      <code>
       Auth.RememberMe.Enabled
      </code>
     </li>
     <li>
      <code>
       Auth.AllowChangePassword
      </code>
     </li>
     <li>
      <code>
       Auth.AllowSelfEmailUpdate
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       ActiveDirectory.SearchInputMinimumLength
      </code>
     </li>
     <li>
      <code>
       ActiveDirectory.SearchResultsSizeLimit
      </code>
     </li>
     <li>
      <code>
       ActiveDirectory.SearchResultsTimeLimitSeconds
      </code>
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d71922e56">
    <p>
     Load balancer
    </p>
   </td>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       LoadBalancer.UseRedis
      </code>
     </li>
     <li>
      <code>
       LoadBalancer.Redis.ConnectionString
      </code>
     </li>
    </ul>
   </td>
   <td headers="d71922e62">
    N/A
   </td>
  </tr>
  <tr>
   <td headers="d71922e56">
    <p>
     Miscellaneous
    </p>
   </td>
   <td headers="d71922e59">
    <ul>
     <li>
      <code>
       MultiTenancy.TenantResolvers.HttpGlobalIdHeaderEnabled
      </code>
     </li>
     <li>
      <code>
       SystemJobs.LicenseExpirationAlert.DaysBefore
      </code>
     </li>
     <li>
      <code>
       autogenerateStatistics
      </code>
     </li>
     <li>
      <code>
       PasswordComplexity
      </code>
     </li>
     <li>
      <code>
       DefaultFolderIsClassic
      </code>
     </li>
     <li>
      <code>
       Tasks.ModuleEnabled
      </code>
     </li>
     <li>
      <code>
       Telemetry.Enabled
      </code>
     </li>
    </ul>
   </td>
   <td headers="d71922e62">
    N/A
   </td>
  </tr>
 </tbody>
</table>