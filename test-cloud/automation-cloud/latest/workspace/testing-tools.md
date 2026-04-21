---
title: "Testing tools"
visible: true
slug: "testing-tools"
---

The tools directly involved in performing testing with the UiPath platform comprise of the following tools: Studio, Orchestrator, Robot, Test Manager, Autopilot, and Agents. In addition to these, all the other services that the UiPath platform offers contribute to creating a robust testing project, from start to finish. Check out the following list and corresponding diagram to learn about every testing component and how it works:

* [Studio](https://docs.uipath.com/studio/standalone/latest): The IDE for test automation development, including both application and automation testing, enabling you to create test cases, using either a low-code or coded approach, depending on your editing needs, if you prefer a more visual approach, or a full coded experience.
* [Orchestrator:](https://docs.uipath.com/orchestrator/automation-cloud/latest) The tool that allows you to publish and execute your tests, via Test Manager or using a CI/CD pipeline.
* [Robots](https://docs.uipath.com/robot/standalone/latest/admin-guide/according-to-license#unattended-licenses):
  + **App Testing robot**: The vehicle connected to Orchestrator that executes any automation, including tests.
  + **Testing robot**: Used for running unattended automations for both development and testing purposes.
* [Test Manager](https://docs.uipath.com/test-manager/automation-cloud/latest): The test management tool and the ALM integrations that Test Manager offers.
* [Autopilot](https://docs.uipath.com/autopilot/other/latest/overview/about-autopilot): A set of advanced AI-powered experiences designed to automate and streamline various tasks. Autopilot, among other functionalities, offers a dedicated experience for testers via [Autopilot<sup>TM</sup> for Testers](https://docs.uipath.com/autopilot/other/latest/overview/autopilot-for-testers).
* **Agentic testing**: The approach of augmenting testers with agents to extend, accelerate, and simplify their work, achieved using the following tools:
  + [Autopilot](https://docs.uipath.com/autopilot/other/latest/overview/about-autopilot): A set of advanced AI-powered experiences designed to automate and streamline various tasks. Autopilot, among other functionalities, offers a dedicated experience for testers via [Autopilot<sup>TM</sup> for Testers](https://docs.uipath.com/autopilot/other/latest/overview/autopilot-for-testers).
  + [Agents](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/about-agents): Powered by technologies like large language models (LLMs), machine learning, and traditional enterprise automation. With agents you can achieve agentic test automation, that involvs orchestrating agents, robots, and humans in a unified automation ecosystem. You can leverage [low-code agents](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/building-an-agent-agent-builder), that you design and run within the platform, or [coded agents](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/about-coded-agents) that you design through direct code development in your preferred IDE, and connect them to your platform via a dedicated SDK.

Figure 1. Test Cloud tools for testing in Test Cloud

![Test Cloud tools for testing](https://docs-dev.uipath.com/api/binary/test-cloud/2/636657/550068)