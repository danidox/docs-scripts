---
title: "Common VPN vendor mapping (UiPath IPSec / IKE)"
visible: true
slug: "common-vpn-vendor-mapping-uipath-ipsec--ike"
---

This section helps map common on-premises VPN device terminology to the IPsec / IKE settings used by UiPath VPN Gateways.

Different vendors use different names for the same cryptographic concepts.

UiPath uses standard IPsec and IKE terminology, which may look unfamiliar if you are accustomed to firewall-specific configuration screens.

## General mapping principles

Before reviewing vendor-specific examples, keep the following general principles in mind:

* **IKE Phase 1** is commonly referred to as IKE Proposal, Phase 1 Proposal, or IKE Policy on firewall devices.
* **IKE Phase 2** is commonly referred to as IPsec Proposal, Quick Mode, or Phase 2 Policy.
* **Perfect Forward Secrecy (PFS)** is often implemented on firewalls as a checkbox combined with a Diffie-Hellman group. In UiPath, selecting a PFS group implicitly enables PFS.

## FortiClient (Fortinet)

Table 1. Phase 1 (IKE)

| FortiGate | UiPath |
| --- | --- |
| IKE version | IKEv1 or IKEv2 |
| Encryption | AES128, AES256 |
| Authentication | SHA1, SHA256 |
| DH group | DHGroup2, DHGroup14, DHGroup24 |
| Authentication method | Pre-shared key |

Example (common FortiGate configuration):

* Encryption: AES256
* Authentication: SHA256
* DH Group: 14

Equivalent UiPath Phase 1 configuration:

* Encryption: AES256
* Integrity: SHA256
* DH Group: DHGroup14

Table 2. Phase 2 (IPSec)

| FortiGate | UiPath |
| --- | --- |
| Encryption | AES128, AES256, GCM AES |
| Authentication | SHA1, SHA256, GCM |
| Enable PFS | Select PFS group |
| PFS group | PFS14, PFS2048, ECP256 |
:::important
If FortiGate uses GCM, UiPath must use matching GCM settings for both encryption and integrity (for example, `GCMAES256` for both).
:::

## Palo Alto Networks (PAN-OS)

Table 3. Phase 1 (IKE Crypto Profile)

| Palo Alto | UiPath |
| --- | --- |
| Encryption | AES128, AES256 |
| Authentication | SHA1, SHA256 |
| DH group | Group2, Group14, Group20 |
| Authentication method | Pre-shared key |

DH group mapping:

* Group14 → DHGroup14
* Group20 → ECP384

Table 4. Phase 2 (IPsec Crypto Profile)

| Palo Alto | UiPath |
| --- | --- |
| Encryption | AES128, AES256, AES-GCM |
| Authentication | SHA1, SHA256, None (GCM) |
| Enable PFS | Select PFS group |
| DH group | PFS2, PFS14, PFS2048 |

**Common Palo Alto mistake**

Using AES-GCM with SHA256 integrity is invalid. Use the following correct configuration instead:

* Encryption: GCMAES256
* Integrity: GCMAES256

## Cisco ASA / Firepower

Table 5. Phase 1 (IKE Policy)

| Cisco | UiPath |
| --- | --- |
| Encryption | AES, 3DES |
| Hash | SHA, SHA256 |
| DH group | 2, 14, 24 |
| Authentication | Pre-shared key |

Example Cisco configuration:

* Encryption: AES-256
* Hash: SHA256
* Group: 14

Equivalent UiPath Phase 1 configuration:

* Encryption: AES256
* Integrity: SHA256
* DH Group: DHGroup14

Table 6. Phase 2 (Transform Set)

| Cisco | UiPath |
| --- | --- |
| Encryption | esp-aes, esp-gcm |
| Authentication | esp-sha-hmac, none |
| PFS | group2, group14 |

Cisco GCM example: ESP-GCM 256

Equivalent UiPath configuration

* Encryption: GCMAES256
* Integrity: GCMAES256
* PFS: None (unless explicitly enabled)

## Check Point

Table 7. Phase 1

| Check Point | UiPath |
| --- | --- |
| Encryption | AES128, AES256 |
| Integrity | SHA1, SHA256 |
| DH group | Group2, Group14 |

Table 8. Phase 2

| Check Point | UiPath |
| --- | --- |
| Encryption | AES, AES-GCM |
| Integrity | SHA, SHA256, None |
| PFS | Enabled + DH group |
:::important
* When PFS is enabled, select the corresponding PFS group in UiPath.
* When using GCM, encryption and integrity must use matching GCM
algorithms.
:::

## **Quick reference: PFS and DH group mapping**

Table 9. Quick reference

| Firewall terminology | UiPath |
| --- | --- |
| DH Group 1 | PFS1 |
| DH Group 2 | PFS2 |
| DH Group 14 | PFS2048 |
| DH Group 24 | PFS24 |
| ECDH Group 19 | ECP256 |
| ECDH Group 20 | ECP384 |

## When in doubt

If you are unsure how to map your firewall configuration to UiPath settings:

1. Start with the default UiPath IPsec / IKE policy.
2. Verify that the VPN tunnel establishes successfully.
3. Introduce a custom policy only if required.
4. Change one parameter at a time.

## Key takeaway

Most VPN failures are not caused by incorrect cryptographic algorithms, but by mismatched terminology between vendors. This section is intended to bridge that gap and simplify configuration across common VPN platforms.