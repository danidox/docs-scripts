---
title: "Job executions"
visible: true
slug: "job-executions"
---

The UiPath Robot executes jobs across different operational environments:

* The Robot can execute tasks in [Windows sessions](https://docs.uipath.com/robot/standalone/latest/admin-guide/windows-sessions#windows-sessions), either as a console or RDP session, depending on the Orchestrator **LoginToConsole** setting.
* The Robot can concurrently run multiple [background automations](https://docs.uipath.com/robot/standalone/latest/admin-guide/background-process-automation#background-automations) in the same Windows session, with each automation having its own set of dependencies.
* The Robot can operate in Linux environments via [Linux Robots](https://docs.uipath.com/robot/standalone/latest/admin-guide/linux-robots#linux-robots), providing cross-platform automation within a functional Linux environment, made possible by a Docker image.
* The Robot can function in [High-Density environments](https://docs.uipath.com/robot/standalone/latest/admin-guide/high-density-robots#high-density-robots) where multiple robots run concurrently under different user accounts on Windows Server machines.
* The Robot can operate through [Citrix Apps virtualization](https://docs.uipath.com/robot/standalone/latest/admin-guide/robot-citrix-apps-virtualization#citrix-apps-virtualization), which allows it to be set up on a central server and delivered to devices via Citrix virtualization technology.