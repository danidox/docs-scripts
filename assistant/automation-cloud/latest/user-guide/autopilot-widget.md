---
title: "Autopilot™ widget"
visible: true
slug: "autopilot-widget"
---

The Autopilot widget enables interaction with Autopilot for Everyone directly from Assistant, provided it is installed in your tenant. If Autopilot for Everyone is not installed, the widget acts as a placeholder and provides access to the Autopilot Overview documentation.

If no policy is set for Assistant, the Autopilot widget is enabled by default.

For Assistant policies older than version 24.10.1, the Autopilot widget is disabled by default. To enable it:

* update your Assistant policy version to 24.10.1, or
* manually add the Autopilot widget to the policy.

## Enabling or disabling the Autopilot widget

In **Automation Ops** > **Governance** > **Policies**, for the selected Assistant policy, edit the `UiPath.Autopilot.Widget` properties:

* To enable the Autopilot widget in Assistant, check the **Is enabled** box.
* To disable the Autopilor widget in Assistant, clear the **Is enabled** checkbox.