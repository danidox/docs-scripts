---
title: "September 2025"
visible: true
slug: "september-2025"
---

## September 25, 2025

**Build number: 2025.0.176**

### Enhanced Robot Logging Configuration

Robot now supports dual logging with separate log levels for local files and Orchestrator. Use the `UIPATH_FILE_LOG_LEVEL` environment variable to set a different minimum log level for local file logging while maintaining a separate level for logs sent to Orchestrator.

This allows you to store detailed logs, such as INFO+ levels, locally on the machine while sending only higher-priority logs, such as WARN+ levels, to Orchestrator. Doing so reduces database growth while preserving comprehensive local diagnostic information. Valid values include: `Verbose`, `Trace`, `Information`, `Warning`, `Error`, `Critical` and `Off`.

### Bug fix

Packages generated with older Studio versions that used Invoke Workflow activity crashed if the invoked workflow was in a subfolder.

## September 10, 2025

**Build number: 2025.0.175**

### Support for file arguments for jobs

Starting with this version, the robot supports input and output arguments of type File.

### Bug fixes

* Occasionally, the robot would report the job was running, even though the Robot Executor already exited.
* Portable Executor now sets the right resolution when running on Windows.
* This version brings several performance fixes.