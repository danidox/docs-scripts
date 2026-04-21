---
title: "Configuring the firewall"
visible: true
slug: "configuring-firewall"
---

This page lists the domains (FQDNs) and outbound IP ranges (CIDRs) that must be allowed for the cloud offering and associated UiPath services to function correctly in environments where network access is restricted to approved destinations. Depending on how your organization manages outbound and inbound traffic, these allow lists may be applied in your firewall or in another network security layer that governs external connectivity. TOPLEVELNOTEMARKER
:::note
LaunchDarkly is no longer used by UiPath services. If you previously allow-listed LaunchDarkly domains, you can safely remove them from your firewall rules.
:::

## Overview

UiPath services require two types of allow lists, determined by who initiates the connection:

* **DNS domain allowlist (FQDNs)**: Apply when users, robots, or on-premises components connect to UiPath. Examples include signing into Automation Cloud Portal, Orchestrator, or Test Manager, or accessing any UiPath interface. In these scenarios, your environment is the requester and the connectivity is controlled by DNS names. These domains must always be allow listed by FQDN (referred to in this page as domains), because their underlying infrastructure is distributed.
* **Outbound IP ranges (CIDRs)**: Apply when UiPath connects to your systems. Examples include cloud portal accessing your Azure Key Vault for Customer-Managed Keys, IXP syncing with Microsoft Exchange, Test Manager connecting to SAP, or Integration Service and Apps calling your endpoints. In these scenarios, UiPath is the requester, and your firewall sees traffic originating from UiPath outbound IP ranges. To allow traffic originating from UiPath, you must allow the corresponding CIDR blocks (referred to in this page as Outbound IP ranges).

## How to use this section

To ensure uninterrupted access to UiPath services:

1. Navigate to the cloud offering that you use: [Test Cloud](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-the-firewall-for-cloud#configuring-the-firewall-for-test-cloud), [Test Cloud Public Sector](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-the-firewall-for-public-sector#configuring-the-firewall-for-automation-cloud-public-sector), or [Test Cloud Dedicated](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-the-firewall-for-dedicated#configuring-the-firewall-for-automation-cloud-dedicated).
2. Identify the UiPath services used in your tenant.
3. For each service:
   1. Configure the domain allow list with all the mentioned domains.
   2. Configure the outbound IP ranges where UiPath connects to your systems.
      :::note
      When specified, use the outbound ranges that correspond to your tenant’s region. If your tenant migrates to another region, update outbound IP ranges accordingly.
      :::

The following sections provide the required domains and outbound IP ranges that should be allowed for UiPath services.