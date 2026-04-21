---
title: "Licensing robots for attended automations"
visible: true
slug: "licensing-robots-attended"
---

To execute attended automations, you need to allocate one or more [user licenses](https://docs.uipath.com/overview/other/latest/overview/user-licensing) to your robots.

The following user licenses are available for attended automations:

* Attended
* Citizen Developer
* Automation Developer

## Via Orchestrator

To license a robot for attended automations, first upload and activate a license in Orchestrator, then connect the robot to that Orchestrator instance.

To connect a robot to Orchestrator:

* [Configure the Interactive Sign-In in Assistant](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/connecting-robots-to-orchestrator#connecting-attended-robots-to-orchestrator).
* In the Assistant, use the [Client ID connection type](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/connecting-robots-to-orchestrator#using-the-client-credentials-in-the-assistant), and provide the client credentials.
* In the Command Line Interface, use the[`--connect` command](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/connecting-robots-to-orchestrator#using-the-client-credentials-in-the-command-line), and provide the client credentials.

## Via Command Line (using the License Tool)

To license a robot without connecting it to Orchestrator, use the License Tool `activate` command in the Command Prompt. The license activation can be done offline and online.

Check out the [LicenseTool utility](https://docs.uipath.com/robot/standalone/latest/admin-guide/according-to-license#licensetool-utility) for more commands and parameters.

### For online activation

Run the following command in the same directory where the `UiPath.LicenseTool.exe` is found, and `1234-5678-9010-1112`is the license string.

```
C:\Program Files\UiPath\Studio\UiPath.LicenseTool.exe activate -l 1234-5678-9010-1112
```

### For offline activation

Run the following command in the same directory where the `UiPath.LicenseTool.exe` is found, and `c:\Downloads\license.txt` is the path to the license file.

```
C:\Program Files\UiPath\Studio\UiPath.LicenseTool.exe activate-offline -f c:\Downloads\license.txt
```