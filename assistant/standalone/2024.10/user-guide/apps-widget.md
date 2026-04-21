---
title: "Apps Widget"
visible: true
slug: "apps-widget"
---

The Apps Integration Widget allows you to access your UiPath Apps directly from the UiPath Assistant and start them just like any other automation.

After you have the widget in Assistant, the available apps appear in the UiPath Assistant right under the Automations list and they work in a similar way. Clicking on them displays more details such as a description, owner, creation date and version. From the contextual menu, you can also use the “Send to desktop” feature and simply create a desktop shortcut for the app.

The Apps Widget is enabled by default.

To not display the Apps Widget to users, you need to create and deploy a policy in Automation Ops that disables the Apps Widget. For this, when creating the policy, set the `Is Enabled` field to `No`.
:::important
At least one App has to be published for the Apps Widget to appear in the UiPath Assistant.
:::