---
title: "December 2024"
visible: true
slug: "december-2024"
---

## December 17, 2024

**Build number: 2025.0.157**

### Introducing a new Studio, Robot, and Assistant release cadence for Automation Cloud customers

This release marks the launch of a new Studio, Robot, and Assistant release vehicle that aims to deliver continuous updates with a faster release cadence, ideal for supporting a cloud ecosystem.

The new Studio and Robot installers are available for users with an **Enterprise License** and can be downloaded from the Resource Center in UiPath Automation Cloud. You can access the Resource Center by clicking the help button ![](/images/robot/robot-image-509854.webp) and selecting the **Downloads** menu option in UiPath Automation Cloud.

**Key features**
* **Release cycle** - Every two months initially, targeting every two weeks.
* **Installers** - `UiPathStudioCloud.msi` and `UiPathRobot.msi`
* **Updates** - The latest **Enterprise Edition** MSI installer will be available in the Resource Center in UiPath Automation Cloud after each Enterprise release, ensuring you can always access the latest version.
* **Support** - Only the latest cloud version is supported.
* **Content** - The latest cloud version always contains the latest Studio features and fixes.

**Benefits of using the latest version of Studio**
* Access to the latest updates and innovative features developed by UiPath
* Reduced IT operations time and costs with Robot and Studio deployments
* Reduced risk of breaking existing automations
* Enhanced Robot, Studio Web, and Studio interoperability
* Streamlined access to preview features, which reduces the need to manually opt in

**Robot compatibility**

Studio stores the minimum Robot version required to run a project, indicated by the Studio version used for editing or publishing a workflow. This ensures that the current project can only be executed by robots of the same version or higher.

Running a process on an older robot version will result in an error message.

**Supported Studio versions**

The regular release cadence for the Community and Enterprise LTS releases remains the same. The **Studio Continuous release, short term support (STS)** aims to deliver the latest features to Enterprise customers in a cloud-like release cycle. This means that the Community and STS versions are released every two months, and the Enterprise LTS version is released once per year, following the [same versioning](https://docs.uipath.com/release-notes/other/latest/release-notes/about-release-versions).

| Releases | Timelines |
| --- | --- |
| Community | Every two months |
| Continuous Release, Short Term Support (STS) | Every two months, one week after Community |
| Enterprise LTS | Once a year (October) |

**About the Robot documentation**

To accommodate the new way of releasing Robot features, we have created two new documentation guides:

1. The [Robot Release Notes guide](https://docs.uipath.com/robot/standalone/latest/release-notes) outlines the changes included in each Robot Enterprise release.
2. The [Robot user guide](https://docs.uipath.com/robot/standalone/latest/admin-guide) provides details on the latest additions to Robot.

These new guides complement our existing Robot documentation and are updated with every release cycle.

### Bug fixes

* Sometimes, executing jobs would fail with the “Cannot access a closed pipe” or “Connection closed” exceptions. This behavior no longer occurs.
* On rare occasions, using the HTTP Request activity in a Legacy project caused the executor to crash unexpectedly with the error: "System.Exception: Could not retrieve the result of the job execution. This might be because a message was too large to process." The error appeared in Orchestrator for failed jobs.
* In coded workflows, an exception might occur when invoking a workflow multiple times in parallel. This was caused by the use of the `RunWorkflowAsync` method.