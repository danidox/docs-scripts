---
title: "Configuring private connectivity"
visible: true
slug: "configuring-private-connectivity"
---

This section outlines the UiPath-specific configuration. For Azure portal steps, use Microsoft documentation.

## 1. Create the private endpoint

Create a Private Endpoint in the VNet where your client workloads run.

Use the following configurations for the endpoint:

* Connection method: **Connect to an Azure resource by resource ID or alias**
* Resource ID: Use the value from the **Available regions** section.
* Target sub-resource: Use the **Subresource** value from the regional table

For detailed Azure instructions, refer to [Create a private endpoint by using the Azure Portal](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal?tabs=dynamic-ip).

After the endpoint is created:

1. Record the private IP address assigned to the endpoint.
2. You will use this IP address when configuring DNS.

## Configure the Private DNS zone

Your VNet must contain a Private DNS zone for `uipath.com`. This ensures traffic resolves to the private endpoint instead of the public endpoint.

1. Create the Private DNS zone, using the steps detailed in the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal).
2. Link the `uipath.com` Private DNS zone to the VNet where the private endpoint exists. For step-by-step guidance in Azure, refer tot the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links).
3. Add the following A type records to your `uipath.com` Private DNS zone:

   | Record name | Type | TTL | Value | Notes |
   | --- | --- | --- | --- | --- |
   | `cloud` | A | 100 | <Your private endpoint IP address> | Use the private IP assigned to your endpoint |
   | `account` | A | 100 | 104.18.34.171 | N/A |
   | `ah-prod-webclient-blue-us` | A | 100 | 104.18.174.91 |  |
   | `content.usage` | A | 100 | 34.111.138.51 | N/A |
   | `data.usage` | A | 100 | 34.107.204.85 | N/A |
   | `orch-cdn` | A | 100 | 104.18.174.91 | N/A |
   | `platform-cdn` | A | 100 | 104.18.174.91 | N/A |
   | `sol-cdn` | A | 100 | 104.18.174.91 | N/A |
   :::important
   * The `cloud` record must point to your private
   endpoint IP.
   * You are responsible for maintaining these DNS records in your
   environment.
   * If you override `uipath.com` privately, ensure all
   required records exist to avoid resolution failures.
   :::
4. After configuring DNS, validate that:
   * `cloud.uipath.com` resolves to the private endpoint IP from your client subnets.
   * Clients can authenticate and access Test Cloud through the private endpoint.If DNS is misconfigured, traffic may fail to connect or may route traffic to the public endpoint.

## 3. Request private endpoint approval

After completing the private endpoint and DNS configuration:

1. Contact UiPath Support.
2. Request approval of your private endpoint connection.

The endpoint remains in a **Pending** state until UiPath approves it from the Application Gateway side.

Once approved, the connection status changes to **Approved**, and traffic flows through the private connection.