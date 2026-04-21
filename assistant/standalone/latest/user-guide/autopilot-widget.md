---
title: "Autopilot widget"
visible: true
slug: "autopilot-widget"
---

The Autopilot widget enables interaction with Autopilot for everyone directly from Assistant, provided it is installed in your tenant. If Autopilot for everyone is not installed, the widget acts as a placeholder and provides access to the Autopilot Overview documentation.

If no policy is set for Assistant, the Autopilot widget is enabled by default.

For Assistant policies older than version 24.10.1, the Autopilot widget is disabled by default. To enable it:

* update your Assistant policy version to 24.10.1, or
* manually add the Autopilot widget to the policy.

## Enabling or disabling the Autopilot widget

In **Automation Ops** > **Governance** > **Policies**, for the selected Assistant policy, edit the `UiPath.Autopilot.Widget` properties:

* To enable the Autopilot widget in Assistant, check the **Is enabled** box.
* To disable the Autopilor widget in Assistant, clear the **Is enabled** checkbox.

## Licensing and policies

To access Autopilot for everyone:

* Make sure you have an Automation Cloud™ Enterprise plan.
* Make sure you have a valid user license.

If the 24.10.1 Assistant policy is in place, the Autopilot for everyone widget appears by default. To disable the widget for your organization, apply your own Automation Ops policy. TOPLEVELNOTEMARKER
  :::important
  Tenant-level deployments of Assistant policies do not propagate correctly to users, and prevent the Autopilot for everyone widget from being displayed. As a temporary solution, deploy the Assistant policy directly to a user group with the intended users.
  :::