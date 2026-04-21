---
title: "BGP configuration for UiPath VPN Gateways"
visible: true
slug: "bgp-configuration-for-uipath-vpn-gateways"
---

Border Gateway Protocol (BGP) is used to exchange routes dynamically between your on-premises network and the UiPath VPN Gateway.

BGP is the recommended routing method because it removes the need for manual route management and reduces connectivity issues, but it is not mandatory.

## How BGP works in UiPath

BGP support exists at the VPN Gateway level, but routing behavior is determined per connection. A single UiPath VPN Gateway can host a mix of BGP-enabled connections and static (non-BGP) connections. Each connection behaves independently.

For example, Site A may use BGP while Site B uses static routes, with both connecting to the same gateway.

## Gateway-level BGP properties

The gateway exposes a fixed gateway ASN, `65515`. BGP capability is always present on the gateway.

Your on-premises VPN device must support BGP and accept a peer with ASN `65515`.

## Connection-level routing behavior

When creating or editing a VPN connection you explicitly choose whether that connection uses BGP. If BGP is disabled, the connection uses static routing and you must define the on-premises CIDRs that should be reachable. Only those ranges will be routed through the tunnel.

If BGP is enabled, routes are exchanged dynamically. UiPath advertises all ACR VM pool CIDRs and the tenant’s serverless robot CIDR, and your on-prem device advertises its on-prem CIDRs.

To enable BGP on a connection you must provide the on-premises ASN and the BGP peer address used by your on-premises device. If either value is missing or incorrect, the BGP session will not establish.

## BGP peer IP address options

UiPath supports two ways to define BGP peer addresses.

**Gateway subnet IP (default & recommended).**

By default the VPN Gateway selects a private IP from the gateway subnet. This IP is shown on the gateway tile in the admin portal and is used as the gateway’s BGP peer address. Configure the gateway peer IP on your on-prem device and the on-prem peer IP on the VPN connection. This is the simplest and preferred option.

**APIPA BGP addresses (advanced).**

Automatic Private IP Addressing (APIPA) allows BGP peering without consuming IP addresses from the gateway subnet and should be used only when required by your on-premises VPN device. UiPath supports only the APIPA ranges `169.254.21.0/24` and `169.254.22.0/24`. Addresses outside these ranges are not supported.

## APIPA configuration

When using APIPA you must configure the APIPA address in two places: on the VPN Gateway (gateway APIPA address) and on the VPN connection (the on-premises peer APIPA address). These two addresses must form a binary-inverted pair. UiPath computes the partner peer address by toggling the last two bits of the IPv4 address:

```
PartnerPeer = Address XOR 0x3
```

This requirement means the two IPs must be inside the same `/30` and pair as `.1 ↔ .2` and

```
.0 ↔
        .3
```

. Valid examples:

* Gateway: `169.254.22.2` → Connection peer: `169.254.22.1`
* Gateway: `169.254.22.0` → Connection peer: `169.254.22.3`

An invalid pairing such as Gateway `169.254.22.2` with Connection peer `169.254.22.5` (not in the same `/30`) will prevent BGP from establishing. Note that in this situation the VPN tunnel may appear connected but no routes will be exchanged.

How to configure APIPA correctly:

1. Choose an APIPA address for the VPN Gateway (example: `169.254.22.2`).
2. Determine its binary-inverted twin (example: `169.254.22.1`).
3. Configure the gateway APIPA address on the VPN Gateway and the inverted peer address on the VPN connection.
4. Configure the same peer address on your on-premises VPN device.

If any step is skipped or mismatched, BGP will fail.

## Routing behavior summary

| Connection type | Route source | Notes |
| --- | --- | --- |
| BGP enabled | Dynamic (BGP) | Connection address ranges ignored |
| BGP disabled | Static | Address ranges define routing |

A single VPN Gateway can host both types simultaneously.

## Common BGP misconfigurations

| Symptom | Likely cause |
| --- | --- |
| VPN connected, no routes | BGP disabled on on-premises device |
| BGP never establishes | ASN mismatch |
| BGP enabled, no traffic | Firewall blocks robot CIDRs |
| Routes missing | APIPA pairing incorrect |
| One-way traffic | Return routes not installed |

## Recommendations

* Use BGP per connection whenever supported.
* Prefer gateway subnet IPs over APIPA unless required.
* Double-check ASN and BGP peer addresses.
* Verify that robot CIDRs are allowed through firewalls.
* Confirm route installation on your on-prem device.

## Key takeaway

BGP is configured per connection, not globally. APIPA requires an exact paired configuration on both sides. Understanding and applying this rule prevents most “VPN is up but traffic doesn’t flow” issues.