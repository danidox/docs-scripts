---
title: "Robot components"
visible: true
slug: "robot-components"
---

A UiPath Robot is built on three fundamental components:

* [UiPath Robot Service](https://docs.uipath.com/robot/standalone/latest/admin-guide/service#robot-service)—This service is vital for maintaining the connection between the Robot and the Orchestrator, as it sends heartbeat signals at regular intervals to inform the Orchestrator of the Robot status. This communication helps monitor robot performance and manage orchestration.
* [The Executor](https://docs.uipath.com/robot/standalone/latest/admin-guide/robot-executor#robot-executor)—This is the workforce of a Robot. It performs activities within a workflow, such as clicking buttons, typing in fields, or extracting data – essentially replicating the actions a human takes on a computer.
* [The Command Line Interface](https://docs.uipath.com/robot/standalone/latest/admin-guide/command-line-interface#robot-command-line-interface)—The UiPath Robot Command Line Interface (CLI) allows you to control and manage the execution of automation workflows directly from the command line, providing another method of interaction besides Assistant.