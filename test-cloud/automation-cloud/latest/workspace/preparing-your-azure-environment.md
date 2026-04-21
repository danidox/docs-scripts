---
title: "Preparing your Azure environment"
visible: true
slug: "preparing-your-azure-environment"
---

Before configuring Private Link, ensure the following:

* You have an active Azure subscription.
* You have a VNet with an available subnet for the private endpoint.
* You have permissions to create:
  + Private Endpoints
  + Private DNS Zones
  + Virtual network links

UiPath enables inbound private connectivity per organization and separately approves each private endpoint connection request. You cannot enable it yourself from the Test Cloud portal.