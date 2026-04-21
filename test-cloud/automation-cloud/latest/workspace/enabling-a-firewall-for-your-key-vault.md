---
title: "Enabling a firewall for the customer-managed key"
visible: true
slug: "enabling-a-firewall-for-your-key-vault"
---

You can apply an extra layer of security to your customer-managed key by enabling a firewall in the Azure Key Vault, and only allowing UiPath services to access the CMK.

To do so, access the **Networking** tab of your Azure Key Vault, and configure the following:

!['Networking tab in Microsoft Azure' image](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/251482)

1. In the **Firewalls and virtual networks** section, select **Allow public access from specific networks and IP addresses**.
2. In the **Firewall** section, add all the IPs listed under [Outbound IP ranges to enable a firewall for the customer-managed key](https://docs.uipath.com/test-cloud/automation-cloud/latest/workspace/configuring-firewall#configuring-the-firewall).

## Sample error for non-allow-listed IP addresses

If you have enabled a firewall, but have not added the previous IP addresses to the allow list, you are returned an error in the **Customer managed key configuration**. This is what it looks like in the browser's debugging console (F12):

```
Client address is not authorized and caller is not a trusted service.\r\nClient address: 20.78.114.120\r\nCaller: appid=7a47c7ed-2f6f-43e3-a701-c4b0204b7f02;oid=a31db968-dd56-4ddd-95cc-e7dddd0562d1;iss=https://sts.windows.net/d8353d2a-b153-4d17-8827-902c51f72357/\r\nVault: plt-nst-config-kv;location=northeurope\nStatus: 403 (Forbidden)
```

In the example, the missing IP is `20.78.114.120`. To overcome the issue, add the IP in the **Firewall** section mentioned in Step 2.