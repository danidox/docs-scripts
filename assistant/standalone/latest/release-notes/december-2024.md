---
title: "December 2024"
visible: true
slug: "december-2024"
---

## December 17, 2024

**Build number: 2025.0.157**

### Introducing a new Studio, Robot, and Assistant release cadence for Automation Cloud customers

This release marks the launch of a new Studio, Robot, and Assistant release vehicle that aims to deliver continuous updates with a faster release cadence, ideal for supporting a cloud ecosystem.

The new Studio and Robot installers are available for users with an **Enterprise License** and can be downloaded from the Resource Center in UiPath Automation Cloud. You can access the Resource Center by clicking the help button ![](/images/assistant/assistant-image-509854-b334b0c3.webp) and selecting the **Downloads** menu option in UiPath Automation Cloud.

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

**About the Assistant documentation**

To accommodate the new way of releasing Assistant features, we have created two new documentation guides:

1. The [Assistant Release Notes guide](https://docs.uipath.com/assistant/standalone/latest/release-notes) outlines the changes included in each Assistant Enterprise release.
2. The [Assistant user guide](https://docs.uipath.com/assistant/standalone/latest/user-guide) provides details on the latest additions to Assistant.

These new guides complement our existing Assistant documentation and are updated with every release cycle.

### Tab updates

Several tabs for Marketplace and Automation Store apps in UiPath Assistant have been removed:

* **More details** tab: Previously available for Marketplace and Automation Store apps, its information has been moved to the main Details tab.
* **Update** tab: Previously shown when an app received a new version. Now, a banner notifies you if the selected app has an available update.
* **Error** tab: Previously displayed when the installation or update of an app failed. Now, a banner notifies you of any issues encountered during installation or updates.

### Multiple apps support

You can now open multiple UiPath Apps apps simultaneously from Assistant. Previously, opening a new app would close the existing one.

### Dynamic resizing of the Assistant window

We have removed the Expand/Collapse button from the toolbar. You can dynamically resize the Assistant window by dragging its edges.