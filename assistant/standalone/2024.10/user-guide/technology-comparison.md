---
title: "Technology Comparison"
visible: true
slug: "technology-comparison"
---

Depending on your environment, type of automations, and applications used, you can choose one of the two available PiP technologies.

**PiP - Child Session** is best suited for complex automations that make use of hardware events and image-based automation, while **PiP - Virtual Desktop** provides a faster process start time and can run on more Windows operating systems.

If both PiP technologies are compatible with your environment and automations, **PiP - Virtual Desktop** is recommended as it is faster and uses less resources to start the automation. You can also keep a **PiP - Child Session** instance open throughout the day to achieve similar performance when starting an automation.

The main differences are presented below:

## Session authentication and VPN compatibility

| Scenario | PiP - Child Session | PiP - Virtual Desktop |
| --- | --- | --- |
| Normal Password Authentication | ✅ | ✅ |
| PIN Authentication | ✅`1` | ✅ |
| Smart Card Authentication | ✅`1` | ✅ |
| VPN Configurations | ✅`2` | ✅ |

`1` Only works the first time a PiP session is spawned. After that, the PiP session can be authenticated only using username and password until the next restart of the machine.

`2` More information on how PiP - Child Session works with VPN can be found [here](https://docs.uipath.com/assistant/standalone/2024.10/user-guide/pip-child-session#known-issues-and-limitations).

## UI Automation compatibility

| Scenario | PiP - Child Session | PiP - Virtual Desktop |
| --- | --- | --- |
| Edge/Chrome Browser Automation | ✅ | ✅`1` |
| Hardware Events UIAutomation | ✅ | ❌ |
| Image-Based Automation | ✅ | ❌ |
| Windows Messages`2` | ✅ | ✅ |
| Simulate`2` | ✅ | ✅ |

`1` UIAutomation Activities v22.4 and above is required for Edge/Chrome browser automation when using PiP - Virtual Desktop.

`2` These input methods may not work on all applications. Check the [Input methods](https://docs.uipath.com/studio/standalone/2024.10/user-guide/input-methods) table for the overall compatibility with applications.

## Applications and integrations usage

| Scenario | PiP - Child Session | PiP - Virtual Desktop |
| --- | --- | --- |
| Microsoft Office Suite | ✅ | ✅ |
| Other UiPath Activities/Integrations | ✅ | ✅ |

## Supported Operating Systems and Virtualization

| OS | PiP - Child Session | PiP - Virtual Desktop |
| --- | --- | --- |
| Windows 8/10/11 - Home Edition | ❌ | ✅ |
| Windows 8/10/11 - Pro/Enterprise Edition | ✅ | ✅ |
| Windows Server 2012/2016/2019/2022 | ❌ | ✅ |
| Mac OS X | ❌ | ❌ |
| Remote Desktop | ✅ | ✅ |
| App-V | ❌ | ✅ |

## Miscellaneous

| Scenario | PiP - Child Session | PiP - Virtual Desktop |
| --- | --- | --- |
| Ability to run an executable as administrator | ❌ | ✅ |
| Recording execution or taking screenshots | ✅ | ❌ |