---
title: "Autopilot for Everyone feature comparison"
visible: true
slug: "autopilot-for-everyone-feature-comparison"
---

The specifics of Autopilot for Everyone lie in how you install, configure, and interact with it. Table 1 summarizes different combinations in which Autopilot for Everyone is available for business users, and instructs where to install Autopilot for Everyone to enable usage in a particular Assistant instance.

Table 1. Installing and using Autopilot for Everyone matrix

| Installation and configuration | Usage in Assistant 2024.10.5+. | Usage in Assistant web |
| --- | --- | --- |
| In Automation Cloud: Admin section. | Supported | Supported |
| In Automation Cloud Public Sector: Admin section | Supported | Not supported |
| In Automation Cloud Dedicated: Admin section | Supported | Not supported |
| In Automation Suite on EKS/AKS: Admin section. | Supported | Not supported |
| In Automation Suite on OpenShift: Admin section | Supported | Supported |
| In Automation Suite on Linux: Admin section | Not supported | Not supported |

## Available features

So while the platform flavor offers the means to installation and configuration, it is the Assistant flavor that offers the interaction. Based on that, some capabilities may not be available, as follows:

* **Usage in Assistant standalone + installation in Automation Cloud:**
  + All documented capabilities are available.

* **Usage in Assistant standalone + installation in Automation Cloud Public Sector:**
  + Clipboard AI is not available.
  + No option to send feedback to UiPath. You can still send custom feedback using the SubmitAutopilotFeedback automation.
  + Installing Autopilot for Everyone only installs the Autopilot process in the Autopilot folder, unlike the default setup, which also includes processes for built-in automations.
  + Automatically installing additional toolsets is not supported. Instead, the **Tools bundle** tab provides instructions for manually downloading and installing out-of-the-box automations on your local device.
* **Usage in Assistant standalone + installation in Automation Cloud Dedicated:**
  + Clipboard AI is not available.
  + No option to send feedback to UiPath. You can still send custom feedback using the SubmitAutopilotFeedback automation.
  + Installing Autopilot for Everyone only installs the Autopilot process in the Autopilot folder, unlike the default setup, which also includes processes for built-in automations.
  + Automatically installing additional toolsets is not supported. Instead, the **Tools bundle** tab provides instructions for manually downloading and installing out-of-the-box automations on your local device.

* **Usage in Assistant web + installation in Automation Cloud:**
  + To run automations, you must create a [Cloud Robot - Serverless machine template](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/executing-unattended-automations-with-serverless-robots#step-2-adding-serverless-robots-to-your-tenant) and then [add both the template and the accounts to the specific automations folder](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/executing-unattended-automations-with-serverless-robots#step-3-giving-access-to-folder-resources).
  + Autopilot for everyone version 2025.4.1 is installed in your Automation Cloud tenant.
  + You do not need to install Robot and Assistant as a prerequisite.

* **Usage in Assistant standalone + installation in Automation Suite:**
  + You must configure your own LLM subscription in order to use Autopilot for Everyone. The subscription must be for one of the LLMs Autopilot for Everyone uses.
  + To update the Autopilot for Everyone version, you must update the Automation Suite version first.
  + Clipboard AI not available.
  + Express User licensing is not available in Automation Suite.
  + No option to send feedback to UiPath. You can still send custom feedback using the SubmitAutopilotFeedback automation.
  + The following toolset automations are not available: Uipath Product Documentation and Generate AI image.
  + The following advanced settings are not available: Send feedback to UiPath, Request classification prompt hints, and Context grounding search phrase hints.
  + Tabular search for uploaded CSV files is not supported.

## Version matrix

When you install Autopilot for Everyone in Automation Suite, you might notice that it uses a different version than Autopilot for Everyone in Automation Cloud. The Automation Suite version is specifically built for on-premises installation, while its baseline corresponds to an existing version developed for Automation Cloud.

To understand which features the Automation Suite version includes, refer to the release notes for its corresponding Automation Cloud baseline.

The following matrix shows the relationship between the available Automation Suite version and its Automation Cloud baseline:

| Autopilot for Everyone in Automation Suite on EKS/AKS and OpenShift | Baseline in Automation Cloud | Available in Automation Suite on EKS/AKS and OpenShift version |
| --- | --- | --- |
| 2025.9.3 | [2025.7.1](https://docs.uipath.com/autopilot/other/latest/release-notes/2025-7-1) | [2.2510.0](https://docs.uipath.com/automation-suite/automation-suite/2.2510/release-notes/automation-suite-on-eks-aks-2-2510-0) |
| 2025.9.4 | [2025.7.1](https://docs.uipath.com/autopilot/other/latest/release-notes/2025-7-1) | [2.2510.1](https://docs.uipath.com/automation-suite/automation-suite/2.2510/release-notes/automation-suite-on-eks-aks-2-2510-1) |
| 2025.9.5 | [2025.7.1](https://docs.uipath.com/autopilot/other/latest/release-notes/2025-7-1) | [2.2510.2](https://docs.uipath.com/automation-suite/automation-suite/2.2510/release-notes/automation-suite-on-eks-aks-2-2510-2) |