---
title: "Operational considerations"
visible: true
slug: "operational-considerations"
---

## Certificate trust

If the gateway presents a certificate that chains to a non-public CA (for example, Cloudflare Origin CA), install the issuing certificate in your client trust stores.

If you do not configure trust correctly, TLS connections can fail even when DNS and routing are correct.

## Failover handling

UiPath does not automatically redirect your private endpoint during a regional incident.

When instructed by UiPath:

* Update DNS to point to the failover region’s private endpoint.
* Update private endpoint targeting if required.
* Validate connectivity.

Test your failover procedure in advance. DNS caching can delay changes during an incident.