---
title: "IPsec and IKE policy configuration"
visible: true
slug: "ipsec-and-ike-policy-configuration"
---

The IPsec / IKE policy defines how the VPN tunnel is secured. Both sides, the UiPath gateway and your on-premises VPN device, must use compatible settings or the tunnel will fail to establish or to carry traffic.

This section explains what the settings mean, how UiPath options map to common firewall terminology, and the most common misconfigurations.

## Overview

A site-to-site VPN has two negotiation phases:

* **IKE Phase 1**
  + Establishes a secure control channel.
  + Used to authenticate peers and protect negotiation traffic.
* **IKE Phase 2 (IPsec / Quick Mode)**
  + Establishes data tunnels.
  + Used for actual application traffic.

Both phases must be compatible for the VPN to work.

## When do you need a custom IPsec/IKE policy?

UiPath gateways are created with a secure default policy that works with most modern VPN devices.

You only need to configure a custom policy if:

* Your on-premises device has strict crypto requirements.
* You must comply with internal or regulatory standards.
* You are matching an existing firewall configuration.

If your VPN works without a custom policy, do not change it.

## IKE Phase 1 (control channel)

Phase 1 settings in UiPath control how the negotiation channel is protected.

| Setting | Description |
| --- | --- |
| Encryption | How control traffic is encrypted. |
| Integrity | How traffic integrity is verified. |
| DH Group | How keys are exchanged. |

Supported Phase 1 options:

* **Encryption**
  + AES128, AES192, AES256
  + GCMAES128, GCMAES256
* **Integrity**
  + SHA1, SHA256, SHA384
  + MD5
* **DH Groups**
  + DHGroup1
  + DHGroup2
  + DHGroup14
  + DHGroup2048
  + DHGroup24
  + ECP256
  + ECP384
  + None

On firewall UIs these are often labelled **IKE Proposal** or **Phase 1 Proposal**.

## IKE Phase 2 (IPsec / Quick Mode)

Phase 2 parameters control how application traffic is protected.

| Setting | Description |
| --- | --- |
| IPSec Encryption | Data encryption |
| IPSec Integrity | Data integrity |
| PFS Group | Perfect Forward Secrecy |
| SA Lifetime | Rekey thresholds |

Supported Phase 2 options:

* **IPSec Encryption**
  + None
  + AES128, AES192, AES256
  + DES, DES3
  + GCMAES128, GCMAES192, GCMAES256
* **IPSec Integrity**
  + SHA1, SHA256
  + MD5
  + GCMAES128, GCMAES192, GCMAES256
* **PFS Groups**
  + PFS1
  + PFS2
  + PFS2048
  + PFS24
  + ECP256
  + ECP384
  + None

## Understanding PFS

On many on-premises devices, PFS is a checkbox combined with a DH group selection. In UiPath you select the PFS group directly.

Check the following table for a conceptual mapping.

| On-premises device | UiPath |
| --- | --- |
| PFS disabled | PFS Group = None |
| PFS enabled with DH Group 2 | PFS2 |
| PFS enabled with DH Group 14 | PFS2048 |
| PFS enabled with DH Group 24 | PFS24 |
| PFS enabled with ECDH | ECP256 / ECP384 |

For detailed mappings, check the Microsoft [documentation](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-compliance-crypto#which-diffie-hellman-groups-does-the-custom-policy-support).

## Critical rules and edge cases

A common failure is a GCMAES mismatch.

If you use GCMAES for IPSec encryption, select the same GCMAES algorithm and key length for IPsec integrity.

* Valid:
  + Encryption: `GCMAES128`
  + Integrity: `GCMAES128`
* Invalid:
  + Encryption: `GCMAES128`
  + Integrity: `SHA256`

This mismatch will prevent the tunnel from establishing.

**None** does not mean insecure by default. **Phase 2 Integrity = None** is valid only when using GCMAES, as this provides built-in integrity protection.

Using **None** with non-GCM encryption results in failure.

SA lifetime values must be compatible with your on-prem device. Mismatched lifetimes typically cause periodic disconnects rather than immediate failure.

## Common IPSec/IKE misconfigurations

| Symptom | Likely cause |
| --- | --- |
| Tunnel never comes up | Encryption or integrity mismatch |
| Tunnel flaps | SA lifetime mismatch |
| Phase 1 up, Phase 2 down | PFS mismatch |
| Works briefly then fails | Rekey mismatch |
| Looks correct but fails | GCMAES rule violated |

## Recommended approach

1. Start with default policy.
2. Only introduce a custom policy if required.
3. Match Phase 1 and Phase 2 exactly.
4. Pay special attention to:
   * PFS mapping
   * GCMAES rules
5. Change one parameter at a time.

## Key takeaway

IPsec/IKE policies must match conceptually, not just visually. Different vendors use different terminology for the same crypto concepts. Understanding the mapping avoids silent failures.