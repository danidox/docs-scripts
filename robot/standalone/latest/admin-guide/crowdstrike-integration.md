---
title: "CrowdStrike integration"
visible: true
slug: "crowdstrike-integration"
---

The integration of UiPath Robot with the CrowdStrike Falcon endpoint protection platform has the following advantages:

* Extended security posture for your organization - This means you can enhance the overall security framework of your organization.
* Business continuity for your robot workforce - This ensures your robot workforce continues to function without interruption.
* Improved visibility and analysis capabilities for your security team - The integration allows the security team to more easily monitor and analyze the actions of the robots.
* Seamless technical integration - This minimizing potential technical issues.

## Demo

The following demo shows how the integration provides an easy way to detect and selectively block any suspicious or malicious activity caused by the automation execution:

## Prerequisites for activation

* Robot and Studio minimum version: 2024.10.9
* Latest supported version of CrowdStrike Falcon sensor
* (Optional) 2024.10 Orchestrator or Automation Cloud Orchestrator `1`

The integration is **automatically activated** when both UiPath Robot and CrowdStrike Falcon sensor are installed on the machine.

`1` When the robot is connected to an Orchestrator older than 2021.10, the `TenantName`, `TenantKey`, and `TenantId` fields are not sent to the CrowdStrike cloud console.

## Integration architecture

Data related to automation execution contains annotation metadata which is sent to the CrowdStrike Falcon sensor. From there, it is sent to the CrowdStrike management console where it can be reviewed by the security team. The integration is based on the following components, which are split between UiPath and CrowdStrike:
  ![docs image](/images/robot/robot-docs-image-102227.webp)

## Metadata

The Robot sends the following metadata to CrowdStrike Falcon:

* Orchestrator URL - The URL that the robot uses for the Orchestrator connection (e.g. https://cloud.uipath.com).
* Tenant Name - The tenant in the Orchestrator instance used by the robot.
* Folder Info - The folder in Orchestrator where the process is found.
* Package Name - The name of the package used by the robot to run the automation.
* Process Name - The name of the process run by the robot.
* Process Key (ID) - The process key (identifier).
* Machine Name - The machine name on which the automation is running on.
* Windows User - The Windows user under which the automation is running.
* User Name - The username under which the automation is running.
* User's Email - The Orchestrator user's email that runs the job.
* Job ID - The job id in Orchestrator for the running job.
* Job Start Date - The date when the job was started.

This metadata provides CrowdStrike Falcon with necessary context and hints about how and where the automations run, aiding in assessing and analyzing security measures.

## Integration status

The integration status of your CrowdStrike Robot protection could be one of the following:

* **Enabled** - CrowdStrike protection is enabled; for machine templates, EDR protection is enabled on all host machines associated to that template.
* **N/A** - CrowdStrike protection is not enabled or the status is not known.
* **Mixed** (this status is only displayed for machine templates, and only on the **Machines** page) - CrowdStrike protection is enabled on some host machines connected to the template, and disabled on others, or the status is not available.

To see the integration status, access the following places:

* Orchestrator, on the **Tenant** &gt; **Machines** &gt; **Installed Versions & Logs** page, check the **EDR Protection** column. It displays the status of your CrowdStrike Robot protection per machine or machine template over the last 30 days.
* Assistant, hover over the tray icon.

## CrowdStrike documentation

Depending on the CrowdStrike account you are using, you can access one of the four documentation URLs:

1. [US-1](https://falcon.crowdstrike.com/documentation/12/hunting-and-investigation#rpa-integration)
2. [US-2](https://falcon.us-2.crowdstrike.com/documentation/12/hunting-and-investigation#rpa-integration)
3. [EU-1](https://falcon.eu-1.crowdstrike.com/documentation/12/hunting-and-investigation#rpa-integration)
4. [US-GOV-1](https://falcon.laggar.gcw.crowdstrike.com/documentation/12/hunting-and-investigation#rpa-integration)