---
title: "Configuring VPN for cloud robots"
visible: true
slug: "configuring-vpn-for-cloud-robots"
---

:::note
Feature availability depends on the cloud offering that you use. For details, refer to the [Feature availability page](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/test-cloud-feature-availability#test-cloud-product-and-feature-availability).
:::

You can create a VPN gateway for a tenant so that your [VM cloud robots](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-automation-cloud-robots-vm) or [serverless cloud robots](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/automation-cloud-robots-serverless) can access your on-premises resources that are behind a firewall.

This page describes:

* How the UiPath VPN Gateway works at a networking level.
* How to plan CIDR ranges, routing, firewall rules, and DNS correctly.
* How to configure site-to-site VPN connections, including static routing, BGP, and custom IPsec or IKE policies.

## Prerequisites
:::important
Installing custom software on your VM, such as VPN clients, may interfere with core services and make the VM unusable. Use the configuration in this chapter instead.
:::

To set up the VPN gateway, you must meet the following requirements:

* Be an organization administrator in Test Cloud.
* Have an Orchestrator role that includes the **Machines - Edit** permission.
* Information required from your network administrator:
  + A list of reserved IP address ranges located in your on-premises network configuration, in CIDR notation. As part of configuration, you need to specify the IP address range prefixes that we will route to your on-premises location.
  + The private CIDRs you want UiPath to reach over the VPN (your on-premises networks).
  + A pre-shared key (PSK) for each VPN device.
    :::important
    The subnets of your on-premises network must not overlap with the virtual network subnets to which you want to connect.
    :::
  + Use compatible VPN devices and have the ability and know-how to configure them, as described in [About VPN devices for connections - Azure VPN Gateway](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices). For details on the default connection parameters, read the [Default policies for Azure](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices#ipsec).
  + Your VPN device must use externally-facing, public IPv4 addresses.
  + 
    :::note
    The pre-shared key should consist of a maximum 128 printable ASCII characters. Do not use space, hyphen `-`, or tilde `~` characters.
      :::

## Understanding networking and CIDRs for UiPath VPN connectivity

This section describes how networking works when using a UiPath VPN Gateway, and why choosing the correct CIDR ranges is critical for a successful and future-proof setup.

You do not need deep networking knowledge to follow this section, but it is important to read it carefully before creating a VPN Gateway.

### Mental model

When you create a VPN Gateway in UiPath Automation Cloud, you are extending your private on-premises network into the UiPath cloud.

This means:

* Your on-premises network and UiPath cloud robot networks become part of one private routing domain
* Cloud robots access your on-premises resources using private IP addresses
* The VPN Gateway does not act as a proxy or NAT device
* Source IP addresses matter and must be routable in both directions

Because of this, CIDR ranges must be planned carefully and must not overlap.

### What is a CIDR?

A CIDR defines a range of private IP addresses.

Examples:

* `10.10.0.0/27` → 32 IP addresses
* `10.10.0.0/25` → 128 IP addresses
* `10.10.0.0/24` → 256 IP addresses

A smaller number after the slash means a larger network.

### Networks involved in a UiPath VPN setup

In a UiPath VPN configuration, multiple distinct network ranges are involved, each with a specific purpose:

* VPN Gateway network
* ACR VM pool networks (VM-based cloud robots)
* Serverless robot network

These networks must all be distinct and non-overlapping.

#### VPN Gateway network (mandatory)

This CIDR defines the subnet where the VPN Gateway itself is deployed. It is used for:

* VPN tunnel endpoints
* BGP peering (if enabled)

The VPN Gateway network does not host robots or workloads

Size requirements:

* Minimum supported size: `/27`
* Recommended size: `/25` or larger

Example:

* Minimum: `10.10.0.0/27`
* Recommended: `10.10.0.0/25`
:::important
This network cannot be changed after the VPN Gateway is created.
* VPN Gateways require a `/27` or larger network (for example,
`/27`, `/26`, `/25`).
* Private endpoints are only supported for `/25` or larger
networks.
* If you create a VPN Gateway with a `/27` CIDR:
+ The entire CIDR will be dedicated to the gateway subnet.
+ Private endpoint creation will be disabled.
+ Supporting future networking features may become impossible.
:::

As a recommendation, always use at least a `/25` CIDR for the VPN Gateway network.

Using `/27` is supported, but it should be considered legacy-only or last-resort, as it significantly limits future expansion.

#### Automation Cloud Robot VM pool CIDRs (VM-based cloud robots)

Each Automation Cloud Robot VM pool (VM-based cloud robots) runs in its own private network range.

* These CIDRs define the source IP addresses of VM-based robots.
* Traffic to your on-premises network originates from these ranges.
:::note
* Each VM pool must have its own unique CIDR
* Must not overlap with:
+ VPN Gateway CIDR
+ Serverless robot CIDR
+ On-premises network CIDRs
:::

Example:

* VPN Gateway: `10.10.0.0/25`
* ACR VM Pool 1: `10.20.0.0/24`
* ACR VM Pool 2: `10.21.0.0/24`

On-premises firewalls must explicitly allow traffic from Automation Cloud Robot VM pool CIDRs. Return routes must exist so responses can flow back to the robots. Overlapping CIDRs will cause routing failures that cannot be fixed later.

#### **Serverless robot CIDR (single, shared network)**

Serverless robots use one single shared network per tenant and there is only one serverless robot CIDR. This is because there is only one serverless robot template, respectively all serverless robot templates in a tenant point to the same VPN configuration. All serverless robot executions of a tenant share this network.

Example:

* Serverless Robots: `10.30.0.0/16`
:::important
You cannot create multiple serverless robot CIDRs.
:::

Since there cannot be multiple serverles robot CIDRs:

* The chosen CIDR must be large enough.
* It must not overlap with:
  + VPN Gateway CIDR
  + Any Automation Cloud Robots VM pool CIDR
  + On-premises networks

If the serverless CIDR overlaps with your on-premises network, VPN connectivity will not work.

### Firewall and routing implications

Because the VPN Gateway does not perform NAT, traffic to on-premises systems comes from robot CIDRs:

* Automation Cloud Robots VM pool CIDRs
* Serverless robot CIDR

The CIDRs must be allowed in both on-premises firewalls and any intermediate network security devices.

Additionally, reverse routes must exist so traffic can return to UiPath. This can be achieved using either static routes, or BGP.

### Best practices

Recommended minimum design:

* VPN Gateway CIDR: `/25` or larger
* Separate, non-overlapping CIDRs for:
  + VPN Gateway
  + Each ACR VM pool
  + Serverless robots
* Ensure all robot CIDRs are:
  + Allowed through on-prem firewalls
  + Routable in both directions
:::important
Treat the UiPath VPN Gateway as a network extension, not a tunnel appliance. Proper CIDR planning upfront prevents outages, support cases, and re-deployment later.
:::

## The VPN gateway workflow schema

This schema shows how the VPN connection is established betweenyour on-premises network and UiPath cloud robot networks.

Connecting to a VPN gateway allows VM-based cloud robots (ACR VM pools) and serverless robots to access restricted resources in your on-premises network.

Figure 1. VPN gateway workflow schema ![The VPN gateway workflow schema](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/638461)

The flow is as follows:

1. Identify the on-premises CIDRs you want UiPath to reach (your internal private address ranges). These are the CIDRs that must be reachable through the VPN.
2. In your local network, provide the IP ranges of the ACR-VM pools (6, 7) to allow their traffic into the network.
3. Create the UiPath VPN Gateway network (Gateway subnet CIDR). This network hosts the VPN gateway resources only (tunnel endpoints and BGP peering).
   * Minimum supported: `/27`
   * Recommended: `/25` or larger
   * Private endpoints require `/25` or larger
   * Cannot be changed after creation
4. UiPath creates a public IP for the VPN Gateway. Your on-premises VPN device uses this public IP as the remote peer. BGP Peer Address and ASN will also be available once provisioning is complete.
5. Create a site-to-site tunnel between your on-premises VPN device public IP and the UiPath VPN Gateway public IP.
6. Routing is established (static or BGP):
   * Static routing (BGP disabled on the connection): you enter the on-premises CIDRs on the connection; only those ranges are routed to on-premises.
   * Dynamic routing (BGP enabled on the connection): routes are exchanged dynamically.
7. Robot traffic originates from robot CIDRs, not the gateway CIDR:
   * Each ACR VM pool CIDR (each pool has its own CIDR).
   * The single Serverless robot CIDR (one per tenant).
8. Your on-premises firewall (and any intermediate firewalls) must allow inbound from the robot CIDRs to the on-prem resources, and ensure return routing back to those robot CIDRs (static routes or BGP).
:::important
The VPN Gateway does not perform NAT. CIDRs must be non-overlapping, and source IPs must be routable both ways.
:::