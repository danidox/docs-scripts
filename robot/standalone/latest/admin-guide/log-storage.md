---
title: "Log storage"
visible: true
slug: "log-storage"
---

## Orchestrator storage

When the Robot is connected to Orchestrator, only logs matching the level set in Assistant or Orchestrator appear on the [Logs](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-logs) page. If Orchestrator is unavailable, [logs are stored in a local path](https://docs.uipath.com/robot/standalone/latest/admin-guide/log-storage) - `C:\Windows\System32\config\systemprofile\AppData\Local\UiPath\Logs\execution_log_data`, within the available disk space, until the connection is restored. When the connection is restored, the logs are sent in batches in the order they had been generated.

## NLog storage

:::important
The Robot update overwrites and resets this file, removing any prior edits.
:::

Additionally, log storage can be configured by editing the `NLog.config` file. Diagnostic logs are collected by the **Internal** type logger and are forwarded by using [NLog targets](https://github.com/nlog/nlog/wiki/Targets). By default, execution logs are stored in a file in the `%LocalAppData%\UiPath\Logs` folder. The messages are collected by the **WorkflowLogging** logger and can be forwarded by using [NLog targets](https://github.com/nlog/nlog/wiki/Targets), as specified by the following parameters in the `NLog.config` file:

```
<?xml version="1.0" encoding="utf-8" ?>
<nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <variable name="WorkflowLoggingDirectory" value="${specialfolder:folder=LocalApplicationData}/UiPath/Logs" />
  <rules>
    <logger name="WorkflowLogging" writeTo="WorkflowLogFiles" final="true" />
  </rules>
  <targets>
    <target type="File" name="WorkflowLogFiles" fileName="${WorkflowLoggingDirectory}/${shortdate}_Execution.log" layout="${time} ${level} ${message}" keepFileOpen="true" openFileCacheTimeout="5" concurrentWrites="true" encoding="utf-8" writeBom="true" />
  </targets>
</nlog>
```

## Log storage by Robot mode

Robot logs are stored differently, based on the user running the automation, which can be the local user (for User Mode robots), or the Local System user (for Service Mode robots):

**Execution logs in `.log` format**
* Service mode:
  + Windows OS—`C:\Users\user\AppData\Local\UiPath\Logs`
* User mode:
  + Windows OS—`%LocalAppData%\UiPath\Logs`
  + Linux—`~/.local/share/UiPath/Logs`
  + MacOS—`~/Library/Application Support/UiPath/Logs`

**Execution logs in LiteDB format**
* Service mode:
  + Windows OS—`C:\Windows\System32\config\systemprofile\AppData\Local\UiPath\Logs\execution_log_data`
* User mode:
  + Windows OS—`%LocalAppData%\UiPath\Logs\execution_log_data`
  + Linux—`~/.local/share/UiPath/Logs/execution_log_data`
  + MacOS—`~/Library/Application Support/UiPath/Logs/execution_log_data`

**Diagnostic (or internal) logs**
* Service mode:
  + Windows OS—`%ProgramData%\UiPath\Logs\internal`
* User mode:
  + Windows OS—`%LocalAppData%\UiPath\Logs\internal`
  + Linux—`~/.local/share/UiPath/Logs/internal`
  + MacOS—`~/Library/Application Support/UiPath/Logs/internal`

**Update logs**
* Service mode:
  + Windows OS—`%ProgramData%\UiPath\UpdateService\Logs`
* User mode:
  + Windows OS—`%LocalAppData%\UiPath\UpdateService\Logs`
  + Linux—`~/.local/share/UiPath/UpdateService/Logs`
  + MacOS—`~/Library/Application Support/UiPath/UpdateService/Logs`