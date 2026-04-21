---
title: "Default IPSec / IKE Policy"
visible: true
slug: "default-ipsec--ike-policy"
---

UiPath VPN Gateways are created with a default IPsec / IKE policy designed for maximum interoperability with a wide range of on-premises VPN devices. The information in this section is based on the Azure VPN Gateway default policies.

In most scenarios, no custom IPsec / IKE policy is required. You should configure a custom policy only if your on-premises VPN device enforces strict cryptographic requirements or cannot successfully negotiate a tunnel using the default policy.

## Terminology used in this section

The following terminology is used throughout this section:

* **SA**: Security Association
* **IKE Phase 1**: Main Mode
* **IKE Phase 2**: Quick Mode

## IKE Phase 1 - default parameters

IKE Phase 1 establishes the secure control channel used to authenticate peers and protect negotiation traffic.

Table 1. Default Phase 1 properties

| Property | Value |
| --- | --- |
| IKE version | IKEv1 and IKEv2 |
| Diffie-Hellman group | Group 2 (1024-bit) |
| Authentication method | Pre-shared key |
| SA lifetime | 28,800 seconds |
| Number of Quick Mode SAs | 100 |

UiPath VPN Gateways support the following encryption and integrity combinations as part of the default policy:

* AES256, SHA1
* AES256, SHA256
* AES128, SHA1
* AES128, SHA256
* 3DES, SHA1
* 3DES, SHA256

During negotiation, the gateway automatically selects the strongest mutually supported combination between UiPath and the on-premises VPN device.

## IKE Phase 2 - default parameters

IKE Phase 2 establishes the data tunnels used for application traffic.

Table 2. Default Phase 2 properties

| Property | Value |
| --- | --- |
| IKE version | IKEv1 and IKEv2 |
| SA lifetime (time) | 27,000 seconds |
| SA lifetime (bytes) | 102,400,000 KB |
| Dead Peer Detection (DPD) | Supported |

The default policy supports multiple encryption, integrity, and PFS combinations. The combination that is ultimately used depends on whether the UiPath VPN Gateway acts as the initiator or the responder during Phase 2 negotiation.

This behavior is expected in IPsec implementations and improves compatibility with a broad range of VPN devices.

## UiPath Gateway as initiator

When the UiPath VPN Gateway initiates Phase 2 negotiation, it supports the following combinations:

| Encryption | Authentication | PFS group |
| --- | --- | --- |
| GCM AES256 | GCM (AES256) | None |
| AES256 | SHA1 | None |
| 3DES | SHA1 | None |
| AES256 | SHA256 | None |
| AES128 | SHA1 | None |
| 3DES | SHA256 | None |

## UiPath Gateway as responder (full supported set)

When the UiPath VPN Gateway acts as the responder, it supports a wider set of combinations to maximize interoperability:

| Encryption | Authentication | PFS group |
| --- | --- | --- |
| GCM AES256 | GCM (AES256) | None |
| AES256 | SHA1 | None |
| 3DES | SHA1 | None |
| AES256 | SHA256 | None |
| AES128 | SHA1 | None |
| 3DES | SHA256 | None |
| DES | SHA1 | None |
| AES256 | SHA1 | 1 |
| AES256 | SHA1 | 2 |
| AES256 | SHA1 | 14 |
| AES128 | SHA1 | 1 |
| AES128 | SHA1 | 2 |
| AES128 | SHA1 | 14 |
| 3DES | SHA1 | 1 |
| 3DES | SHA1 | 2 |
| 3DES | SHA256 | 2 |
| AES256 | SHA256 | 1 |
| AES256 | SHA256 | 2 |
| AES256 | SHA256 | 14 |
| AES256 | SHA1 | 24 |
| AES256 | SHA256 | 24 |
| AES128 | SHA256 | None |
| AES128 | SHA256 | 1 |
| AES128 | SHA256 | 2 |
| AES128 | SHA256 | 14 |
| 3DES | SHA1 | 14 |

This broad responder support allows the UiPath VPN Gateway to interoperate with older VPN devices, strict enterprise firewalls, and devices that enforce specific PFS group requirements.

## Common misconception

**The default policy uses weak cryptography.**

This is incorrect. The default policy supports multiple cryptographic algorithms but does not enforce the weakest option. During negotiation, the strongest mutually supported combination is always selected.

## Key takeaway

The default IPsec / IKE policy is designed for compatibility first and should be used whenever possible. Define a custom policy only when there is a clear technical or compliance requirement.