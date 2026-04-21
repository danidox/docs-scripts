---
title: ".NET troubleshooting"
visible: true
slug: "net-troubleshooting"
---

## .NET required during the MSI upgrade

### Description

Upgrading the Robot with MSI installers (Studio or Robot) fails with the following error: "You must install.NET Desktop Runtime to run this application."

### Potential issue

The.NET Desktop Runtime or.NET Runtime installed on your machine may be corrupted.

### Solution

Uninstall the.NET Desktop Runtime/.NET Runtime from your device and run the UiPath MSI installer again.

## Activities cannot find .NET Runtime

### Description

Workflows using specific activity packages fail when executed by 2023.4.0 and newer robots. The following errors are displayed:

* "To run this application, you must install missing frameworks for .NET."
* "To run this application, you must install .NET."

### Impacted activity packages

* UiPath.Form.Activities version 2.0.x
* UiPath.IntelligentOCR.Activities
* UiPath.MobileAutomation.Activities
* UiPath.Vision
* UiPath.DocumentUnderstanding.Activities
* OCR related activities in the UiPath.UIAutomation.Activities package
* UiPath.OmniPage.Activities
* UiPath.OCR.activities

### Solution 1

Upgrade the activity packages of the problematic workflows to the latest versions.

### Solution 2

Add an **Invoke Code** activity at the start of the problematic workflow with the following snippet:

```
System.Environment.SetEnvironmentVariable("DOTNET_ROOT", System.AppContext.BaseDirectory)
```

### Solution 3

Install:

* .NET Desktop Runtime , for Windows OS
* .NET Runtime, for other operating systems, such as MacOS
* [.NET Framework Runtime](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net461)

## .NET 8 projects fail to run

### Description

Executing a Windows or a cross-platform process built using Studio 2024.2, on a 2023.12 Robot version or lower, fails with the following error: "RemoteException: NU1202: Package &lt;package_name&gt; &lt;version&gt; is not compatible with net6.0-windows7.0 (.NETCoreApp,Version=v6.0). Package &lt;package_name&gt; &lt;version&gt; supports: net8.0-windows7.0 (.NETCoreApp,Version=v8.0)."

### Potential issue

NuGet tries to resolve a package for.NET 6, whereas your automation was built using.NET 8. Such forward compatibility is not supported.

### Solution

Upgrade your Robots to version 2024.2.