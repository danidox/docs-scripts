---
title: "Configuration steps"
visible: true
slug: "configuration-steps"
---

## Step 1. Create the VPN gateway

To create a VPN gateway for a tenant:

1. In Test Cloud, go to **Admin**.

If not already enabled, enable the new Admin experience using the toggle from the header.
2. From the **Tenants** panel on the left side, select the tenant for which you want to create a VPN gateway.

The settings page for the selected tenant opens.
3. Select the **VPN Gateway** tile.
4. Select **Create gateway for Tenant**. The **Create gateway** panel opens
5. In the **Name** field, type a name for the gateway, as you want it to be displayed in the tenant's **VPN Gateway** page.
6. In the **Address space for VPN gateway vnet** field, add the IP addresses you obtained from your network administrator.
   * Use CIDR notation
   * Minimum supported: `/27`
   * Recommended: `/25` or larger (private endpoints require `/25` or larger)
   * Cannot be modified after creation
     :::important
     * Vnet ranges for the gateway or for the VM pool cannot be modified once created.
     * Even if you assign a CIDR block to the VPN gateway network (for example, `/25`), traffic from machine pools or serverless machine templates with VPN enabled will not originate from this CIDR. The actual source IP addresses used for outgoing traffic are those of the CIDRs assigned to the individual machine pool or serverless template. Make sure to allow traffic from the CIDRs of your machine pools or serverless templates, not from the VPN gateway network's CIDR.
     :::
7. (Optional) If you want to use a DNS for this connection, select **Add DNS Address** and then:
   1. In the **DNS Address** field, add a DNS address.
   2. To add additional DNS addresses, select Add more to add another field and then add the address to that field.
      :::note
      You can add DNS addresses later, after the VPN gateway is created, but that requires that you restart all VMs that are connected to the gateway.
      :::
8. Select **Create** at the bottom of the panel to create the VPN gateway connection.

The panel closes and the VPN gateway status is **Provisioning**.

When complete, the status **Deployed** is displayed on the card of the gateway.
:::note
If the status is **Failed**, delete the gateway and re-create it by following the previous instructions.
:::

## Step 2. Create cloud robot templates
:::note
The VPN gateway must show the **Deployed** status before you can perform this step.
:::

The Vnet for a cloud robot template is created when each template is created.

### Cloud robots - VM

In Orchestrator, create one or more **Cloud robot - VM** pools, following the instructions in [Creating the cloud robot pool](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/running-unattended-automations-using-cloud-robots-vm#step-1-creating-the-cloud-robot-pool). During setup, make sure to select the **Connect VPN Gateway** option.

For each pool, you can monitor the **VPN status** from the **Machines** > **Manage Cloud Robot - VM** page.
:::note
Existing Cloud robot - VM pools cannot connect to the VPN gateway. You must create new ones. Additionally, for pools that were set up to connect to the tenant's VPN gateway, you have the option to edit the pool and switch off the **Enable VPN Integration** toggle to disconnect the pool. Once disconnected, you cannot reconnect the pool to the VPN gateway.
:::

### Cloud robots - Serverless

In Orchestrator, edit or create **Cloud robot - Serverless** templates, following the instructions in [Automation Cloud™ robots - Serverless](https://docs.uipath.com/orchestrator/v0/docs/automation-cloud-robots-serverless) . During setup, make sure to configure options on the **Network Configuration** page.

## Step 3. Creating the site-to-site connection

With the VPN gateway deployed, you can now connect your on-premises networks to it.

The gateway card displays the public IP address, which is an essential information for the tunnel configuration.

To configure the VPN gateway to connect to a VPN device:

1. In your organization, go to **Admin** > **Tenant** > **VPN Gateway**.
2. On the tile for the gateway, select **Add connection**.

The **Create connection** panel opens.
3. Provide values for the following fields:

   | Option | Description |
   | --- | --- |
   | Connection name * | Provide a name for your connection. |
   | Shared key (PSK) * | Write a secret phrase or string. You need to remember this exact key and provide it when you configure the connection on your on-premises device. |
   | Public IP for the VPN device * | Provide the public IP address of your on-premises VPN device. **Important:** Do not provide the public IP address of the VPN gateway shown on the card. That gateway public IP must be configured on your on-premises device as the remote peer. |
4. Choose the routing type for this connection between **Static routing (BGP disabled)** or **Dynamic routing (BGP enabled)**.

A single UiPath VPN gateway can host a mix of BGP and non-BGP connections.

   1. **Static routing (BGP disabled)**

If BGP is disabled on the connection, you must configure which on-premises CIDRs UiPath should route to.

**Address space for the on-premises device ***: specify all private CIDRs on your on-premises network that must be reachable through this connection. Only these ranges are routed to your on-prem via this tunnel.
      :::note
      If you configured DNS server IP addresses on the gateway, ensure those DNS IPs fall within one of the on-prem CIDRs defined here (so the gateway can reach them through the tunnel).
      :::
   2. **Dynamic routing (BGP enabled)**

If BGP is enabled on the connection:
      * Routes are exchanged dynamically.
      * UiPath advertises:
        + All ACR VM pool CIDRs
        + The serverless robot CIDR
      * Your on-premises device advertises its on-prem CIDRs.

Provide values for the following fields:
      * **On-premises ASN**: the ASN used by your on-premises VPN device.
      * **BGP peer address**: the IP address used by your on-premises device for BGP peering.

If either value is missing or incorrect, BGP will not establish.
5. Optionally, you can define custom configurations for the IPSec/IKE policy. Use this section to ensure compatibility with the specific security settings required by your on-premises VPN device, or to implement advanced security policies tailored to your organization needs. To do this, turn on the **Custom IPSec/IKE policy** toggle.
   :::note
   Only IKEv2 is supported.
   :::

   1. For **IKE Phase 1**, provide values for the following fields:

Encryption * : Provide the matching encryption method for the initial secure key exchange (IKE Phase 1). This must be identical to the UiPath Gateway setting (for example, AES-256, GCMAES).

Possible values: GCMAES256, GCMAES128, AES256, AES192, AES128

Integrity * : Provide the matching data integrity check for the initial IKE Phase 1 communication (for example, SHA-256, SHA-512). This must match the UiPath Gateway.

Possible values: SHA384, SHA256, SHA1, MD5

DH Group * : Provide the matching Diffie-Hellman (DH) group for the secure key exchange in IKE Phase 1 (for example, Group 14, Group 19). This must match the UiPath Gateway.

Possible values: DHGroup24, ECP384, ECP256, DHGroup14, DHGroup2048, DHGroup2, DHGroup1, None
   2. For **IKE Phase 2 (IPSec)**, provide values for the following fields:

IPsec Encryption * : Provide the matching encryption method for data traffic within the VPN tunnel (IPSec Phase 2) (for example, AES-256, 3DES). This must match the UiPath Gateway.

Possible values: GCMAES256, GCMAES192, GCMAES128, AES256, AES192, AES128, DES3, DES, None

IPsec Integrity * : Provide the matching data integrity check for traffic within the VPN tunnel (IPSec Phase 2) (for example, SHA-256, SHA-512). This must match the UiPath Gateway.

Possible values: GCMAES256, GCMAES192, GCMAES128, SHA256, SHA1, MD5

PFS Group * : Provide the matching Perfect Forward Secrecy (PFS) group for IPSec Phase 2, if enabled on the UiPath Gateway (for example, Group 14, Group 19). If one side uses PFS, the other should match or disable it.

Possible values: PFS24, ECP384, ECP256, PFS2048, PFS2, PFS1, None

IPSec SA lifetime in Kilobytes * : Provide the duration for active secure connections (IKE and IPSec). These are local settings; matching is not strictly required, but similar values are recommended for consistency.

Possible values: minimum 1,024, default 10,2400,000

IPsec SA lifetime in seconds * : Provide the duration for active secure connections (IKE and IPSec). These are local settings; matching is not strictly required, but similar values are recommended for consistency.

Possible values: minimum 300, default 27,000
6. Select **Add connection**. Once the configuration is complete, it may take some time for the connection status to update to **Connected**.

The panel closes and the new connection is displayed on the **Connections** page. The connection is ready to use when the **Connection status** column displays **Connected**.

A **Connected** status means the Pre-Shared Key (PSK), peer Public Internet Protocol (IP) address, and IPSec/IKE Policy parameters are configured correctly, and an encrypted tunnel exists.
:::note
If the connection status is **Connection failed**, you must delete the connection and create it again.
:::

To add more connections, on the **Connections** page, select **Create connection**.
:::note
You can add up to 25 connections.
:::