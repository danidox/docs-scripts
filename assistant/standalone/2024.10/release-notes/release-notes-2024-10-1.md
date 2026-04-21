---
title: "2024.10.1"
visible: true
slug: "release-notes-2024-10-1"
---

**Release date: 1 July 2024**

## Preserving credentials casing

By default, login credentials (domain\username) are converted to UPPERCASE, which may cause automations to fail. To preserve the original casing, we've created a new system variable: `UIPATH_PRESERVE_CREDENTIALS_CASE`. Add it to your environment, and set its value to `True`**.**

## Errata

### New flag for live streaming in the ADDLOCAL parameter

**Added 9 October 2024**

Starting with 2024.10, to continue using the live streaming feature without disruptions, add the `LiveStreaming` flag to the `ADDLOCAL` command. This step installs the live streaming required software, RealVNC. Installations from GUI or without the `ADDLOCAL` command automatically install the live streaming software. This flag is available for both Studio and Robot installers.

Refer to the [UiPathRobot.msi Command Line Parameters](https://docs.uipath.com/robot/standalone/2024.10/user-guide/uipathrobotmsi-command-line-parameters) page for details and examples.

### Command line arguments for proxy settings

**Added 11 July 2024**

A new set of command line arguments allows you to set the proxy configuration during installation of your robots. These [proxy-related parameters](https://docs.uipath.com/robot/standalone/2024.10/user-guide/uipathrobotmsi-command-line-parameters) are available for both Studio and Robot installers.

## Improvements

### New operating system is supported

Robots can now run automations on Microsoft Azure Windows 11, Enterprise Multi-sessions.

### .NET 8 support
:::note
**Erratum: Added 12 July 2024** We now support .NET 8 for both Windows and cross-platform automation projects. Projects made using Studio 24.10 are only compatible with Robot 2024.10 or later. Robot 2024.10 maintains compatibility with projects published from older Studio versions using previous .NET frameworks. Refer to the [compatibility matrix](https://docs.uipath.com/overview/other/latest/overview/compatibility-matrix#automation-projects) for more details.
:::

**The following note has been corrected by the previous erratum:** Cross-platform and Windows projects are built with the most recent.NET 8 framework. Be aware that projects built with.NET 6 cannot be executed anymore, due to forward incompatibility.

### UiPath Assistant

* UiPath Assistant now displays the name, version, and size of packages being downloaded during project installation.
* You can now access the UiPath Diagnostic tool from the error dialog box.
* If you belong to several tenants, you can now switch between them using the new **Tenant** option in the top-right corner.
* For enhanced accessibility, we've moved the search bar to the top of the Assistant tabs.
* In response to user feedback, we've temporarily removed the robot character, with plans to reintroduce it effectively in the future.
* You can launch Task Mining for Automation Cloud instances.
* The **Picture in Picture** feature has been upgraded:
  + It is now called **Robot session**.
  + The **Join** button allows the user to interact with the Child Session or Secondary Desktop, depending on the project settings.
  + The **Leave Robot Session** button switches the Robot Session window to a view-only mode.
  + The **Keep on top** toggle was removed, as the Robot session window stays atop other applications.
  + The **Close** button (X) on the Robot Session window prompts a confirmation about stopping the running automations.

## Bug fixes

* We've fixed the issue where users were unable to log into their Virtual Desktop Infrastructure (VDI) accounts. This primarily occurred when a previous user did not log off after manually stopping an unattended automation via Orchestrator.
* When authenticating through client certificates, a bug prevented the robot from reading private keys from card readers. This mainly occurred when multiple card readers were present and at least one had unexpected issues.
* An issue prevented job failure recording for usernames that contained spaces.
* Sessions might have remained in use after a job was completed due to an incorrect status of the executor’s exit. The system now automatically terminates the executor 30 seconds after a job is completed.
* Creating a session assigned “RDP_xxxxx_xx” as the Client Name for the robot machine. With this update, the machine’s host name is used instead. This allows for reusing RDP licenses rather than allocating a new one for every session.
* Job recordings were failing during the upload stage.