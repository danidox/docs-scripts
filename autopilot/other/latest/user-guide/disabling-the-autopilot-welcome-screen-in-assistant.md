---
title: "Disabling the Autopilot welcome screen in Assistant"
visible: true
slug: "disabling-the-autopilot-welcome-screen-in-assistant"
---

If your organization does not use Autopilot for Everyone, create an Assistant policy in Automation Ops to disable the Autopilot widget. To hide the widget in the Assistant, apply the policy to your tenant.

## Enabling or disabling the Autopilot widget

In **Automation Ops** > **Governance** > **Policies**, for the selected Assistant policy, edit the `UiPath.Autopilot.Widget` properties:

* To enable the Autopilot widget in Assistant, check the **Is enabled** box.
* To disable the Autopilor widget in Assistant, clear the **Is enabled** checkbox.