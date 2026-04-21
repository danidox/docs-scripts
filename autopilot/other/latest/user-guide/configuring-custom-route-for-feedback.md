---
title: "Configuring custom route for feedback"
visible: true
slug: "configuring-custom-route-for-feedback"
---

Use the **SubmitAutopilotFeedback** automation template to customize how Autopilot for Everyone routes your user feedback within your organization. 
:::important
* This capability applies starting with Autopilot for Everyone version 25.7.
* The **Send feedback using the SubmitAutopilotFeedback automation** advanced setting must be enabled.
* You must preserve the name of the automation, as Autopilot specifically looks for the **SubmitAutopilotFeedback** automation when routing your feedback.
:::

## The SubmitAutopilotFeedback automation

The automation receives structured input, including:

* User/session metadata
  + `orgName`
  + `tenantName`
  + `version`
* Feedback details
  + `type` (for example: `Thumbs_Up`, `Thumbs_Down`)
  + `category` (for example, `Other suggestion`)
  + `feedback` (user comments)
  + `userPrompt` (what the user asked)
  + `robotResponse` (what Autopilot for Everyone replied)
* Model and advanced settings configuration

You can route this data into systems such as Jira, internal databases, or analytics pipelines.

1. Create or customize the **SubmitAutopilotFeedback** automation using the [UiPath-provided template](https://documentationexamplerepo.blob.core.windows.net/examples/Autopilot%20template%20automation/SubmitAutopilotFeedback.zip).
2. Publish the automation to the Orchestrator folders your intended users can access.
3. In Autopilot for Everyone admin experience, enable the **Send feedback using the SubmitAutopilotFeedback automation** advanced setting.
4. Optionally, disable sending feedback to UiPath by turning off the **Send feedback to UiPath** advanced setting.