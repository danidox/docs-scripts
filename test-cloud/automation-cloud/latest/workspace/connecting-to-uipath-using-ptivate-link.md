---
title: "Connecting to UiPath using private
            link"
visible: true
slug: "connecting-to-uipath-using-ptivate-link"
---

Route traffic from your Azure Virtual Network (VNet) to Test Cloud services through Azure Private Link to keep traffic off the public internet.

Azure Private Link lets you access UiPath services through a private endpoint in your Azure VNet. Use this configuration when your organization requires private network isolation for traffic originating from your Azure environment. Azure Private Link keeps the connection to `cloud.uipath.com` on a private network path through your private endpoint. Other UiPath subdomains still resolve to public IP addresses. TOPLEVELNOTEMARKER
:::note
This capability is not available for AI Center.
:::

## Traffic flow

Traffic follows this path:

1. Client devices or VMs (for example, Robots, Task Mining devices, browsers)
2. Customer VNet
3. Customer private endpoint
4. UiPath regional gateway (private connectivity entry point)
5. UiPath backend services

## Available regions

When you create the private endpoint, connect to the correct regional gateway:

| Region | Resource ID | Subresource |
| --- | --- | --- |
| **West US 2 (Primary)** | `/subscriptions/05f74eb7-7054-4e72-a744-2ce5d7180bd7/resourceGroups/plt-prd-gate-wus2-01-b-rg/providers/Microsoft.Network/applicationGateways/plt-prd-gate-wus2-01-b-appgw` | `plt-prd-gate-wus2-01-b-appgw-fip-config1` |
| **East US (Secondary)** | `/subscriptions/05f74eb7-7054-4e72-a744-2ce5d7180bd7/resourceGroups/plt-prd-gate-eus-01-b-rg/providers/Microsoft.Network/applicationGateways/plt-prd-gate-eus-01-b-appgw` | `plt-prd-gate-eus-01-b-appgw-fip-config1` |

## High availability and disaster recovery (HADR)

If you use two data centers:

* Connect your primary data center to **West US 2**.
* Connect your secondary data center to **East US**.

During the initial rollout phase, if you experience connectivity issues with West US 2, contact UiPath Support. You may temporarily use East US as your primary connection.