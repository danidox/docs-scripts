---
title: "Enabling/disabling Autopilot™"
visible: true
slug: "enable-disable-functionality"
---

Autopilot default setting is as follows:

* Generative and conversational - Enabled by default.
* Autopilot for Everyone - Disabled by default.

Autopilot capabilities in Studio Web can be controlled via Automation Ops policies. To define a Studio Web governance policy that disables Autopilot capabilities:

1. Add a new Studio Web policy in Automation Ops (for more information, see [Governance](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/define-governance-policies) in the Automation Ops guide).
2. Under the **Feature Toggles** tab, disable the **Allow Autopilot** setting, and then save your policy.

Autopilot capabilities in Studio and StudioX can be controlled via [Automation Ops policies](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-studio-policies#save-and-publish) or via [the file-based governance model](https://docs.uipath.com/studio/standalone/2024.10/user-guide/governance#studio-settings) (by editing the `EnableGenerativeAiParam` parameter).

To define a policy in Automation Ops that disables Autopilot capabilities for Studio or StudioX:

1. Make sure you are using the latest Studio or StudioX policy template.
2. Add a new Studio or StudioX policy.
3. Under the **Feature Toggles** tab, disable the **Allow Autopilot** setting, and then save your policy.

Autopilot capabilities in Studio Web, Studio, and StudioX can also be controlled by configuring the [AI Trust Layer policy](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-ai-trust-layer-policies).

Autopilot capabilities in Test Manager and Apps are controlled by configuring the [AI Trust Layer policy](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-ai-trust-layer-policies).

Autopilot for Everyone capabilities are controlled through the AI Trust Layer policy and the admin experience from the [AI Trust Layer page in Automation Cloud](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/about-ai-trust-layer).