---
title: "DNS configuration for UiPath VPN Gateways"
visible: true
slug: "dns-configuration-for-uipath-vpn-gateways"
---

Correct DNS configuration is critical for reliable VPN connectivity. Misconfigured DNS is one of the most common causes of intermittent or hard-to-diagnose failures.

This section explains how DNS works on the VPN Gateway and what is required for it to function correctly.

## How DNS works on the VPN Gateway

When you configure DNS servers on a UiPath VPN Gateway, the gateway uses those servers for all name resolution. DNS servers configured on the gateway are not queried in sequence, nor are they used on a per-domain basis or treated as conditional forwarders.

In practice, this means that every DNS server you add must be able to resolve all domain names the gateway needs to reach. The list of servers exists to provide availability and redundancy, not to split resolution responsibility between servers.

## Primary and Secondary DNS

Many users assume that DNS servers configured on the gateway are tried one after another, that if DNS server A cannot resolve a name, DNS server B will be tried. That is not the case.

A DNS server is only bypassed if it is completely unreachable. If a server responds but cannot resolve a name, the query fails and another server is not tried. This behavior can produce intermittent failures, situations where some automations succeed while others fail, and errors that appear unrelated to networking.

## What DNS servers should you configure?

Configure DNS servers that can resolve your internal on-premises domain names and any external domain names your automations require. The servers must be reachable from the VPN Gateway network and should return consistent results.

Typical, valid options include on-premises Active Directory DNS servers, centralized enterprise DNS resolvers, or cloud-hosted DNS servers that are reachable over the VPN.

## What not to do

Avoid mixing DNS servers with different responsibilities (for example one server that resolves only internal domains and another that resolves only internet names) or relying on conditional forwarders that are not visible to the gateway.

Do not assume the gateway will fall back to the “secondary” server when a query fails on the “primary.” These configurations commonly cause name resolution flapping, timeouts, and unpredictable automation behavior.

## Example of a correct DNS setup

A simple, correct setup is to configure two or more DNS servers that are functionally equivalent and reachable over the VPN.

For example:

* DNS Server 1: `192.168.10.10`
* DNS Server 2: `192.168.10.11`

Both servers must be reachable via the VPN and be capable of resolving both internal hostnames and any required external names. This provides redundancy, not specialisation.

## Key takeaway

DNS servers configured on the VPN Gateway must be functionally equivalent. They exist for availability, not for splitting responsibility. If a domain name cannot be resolved by every configured DNS server, the VPN Gateway may fail to resolve it at all.

## Recommendation

Use two or more DNS servers with identical resolution capabilities and test resolution for both internal services and external dependencies. Do not rely on DNS server ordering or on implicit fallback behavior.