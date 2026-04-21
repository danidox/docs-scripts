---
title: "The Autopilot for Everyone tenant card"
visible: true
slug: "the-autopilot-for-everyone-tenant-card"
---

To install Autopilot for Everyone without organization-level administrative rights, access the tenant-level dedicated card, then follow the installation steps.

The card is displayed when you go to the Admin section of your organization and select the tenant where you want to install Autopilot for Everyone. Once you select the card, the AAutopilot for Everyone installation page opens, with the tenant preselected by default.

## Known issues

* The **Tenant Admin** role does not explicitly include permissions to access Autopilot for Everyone. This may cause confusion, as your effective rights extend beyond those defined in the selected role. As a result, you may see the Autopilot for Everyone card even if it is not explicitly enabled through role settings.
* Custom roles can install Autopilot for Everyone through the card, even if their definitions do not include related permissions. This may also cause confusion, as users might see or interact with the card unintentionally.
* The Autopilot for Everyone card is displayed for all tenants in the organization. Accessing the card and navigating through tenants may cause a display of errors, because of missing permissions.