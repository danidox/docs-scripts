---
title: "Assistant Web setup"
visible: true
slug: "assistant-web-setup"
---

To run automations in Assistant Web, you need either a local machine setup, or active cloud robots assigned to the same folder as the automation.

## Local machine setup

A local machine setup allows you to run background and foreground automations in Assistant Web.

To configure a local machine setup:

1. [Create a machine template and assign it a runtime license.](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/how-is-unattended-automation-performed#21-creating-a-machine-template)
2. [Assign the machine template to the folder where your automation resides](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-machines#assigning-machines-to-folders).
3. [Connect the robot to Orchestrator using the Client Credentials.](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/connecting-robots-to-orchestrator#connecting-unattended-robots-to-orchestrator)

## Cloud robots setup

Cloud robots, either Automation Cloud™ Robots - VM or Automation Cloud™ Robots - Serverless, allows you to run background automations without managing infrastructure.

For cross-platform automations in Assistant Web, an attended license is automatically activated when you sign in.

To use Serverless robots, [add them to your tenant](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/executing-unattended-automations-with-serverless-robots#step-2-adding-serverless-robots-to-your-tenant) and [assign them to the folder where your automation resides](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/executing-unattended-automations-with-serverless-robots#step-3-giving-access-to-folder-resources), just like machine templates.