---
title: "Alerts troubleshooting"
visible: true
slug: "alerts-troubleshooting"
---

## Not receiving alerts for groups with SAML provisioning rule

**Problem:** Users do not receive configured alerts either in the user interface or via email when those alerts are configured for user groups with a SAML provisioning rule.

**Solution:** To resolve this issue, you can add affected users to the Administrators local group which allows them to receive alerts.
:::warning
Adding users to the Administrators group grants them with elevated privileges. Endeavor to understand the implications of these privileges. Ensure users are conferred administrator rights responsibly, maintaining a balance between the need for alerts access and preserving system security.
:::