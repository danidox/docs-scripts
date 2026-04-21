---
title: "Installing with UiPathRobot.msi"
visible: true
slug: "installing-with-uipath-robot-msi-unattended"
---

Running the `UiPathRobot.msi` installs only Robot and Assistant.

First, download the installer from the [Product Downloads](https://customerportal.uipath.com/product-downloads) section in Customer Portal. Look for the **UiPath Robot & Assistant 2024.10** entry. Once the download is complete, continue with the following steps.

First, download the installer from the [Product Downloads](https://customerportal.uipath.com/product-downloads) section in Customer Portal. Look for the following entry:

* For Enterprise versions—**UiPath Robot & Assistant &lt;version_number&gt;**

Once the download is complete, continue with the following steps.

1. Launch the installer.
2. Read and accept the [License Agreement](https://www.uipath.com/developers/all-editions/license-agreement), which includes the UiPath terms of use for activity packages and their dependencies.
3. Select the type of installation: **Quick** or **Custom**.

If you select **Quick**, continue the installation by selecting **Install**.

For **Custom**, continue by selecting **Configure** and following the remaining steps.
4. In the **Choose an installation package** section, select **Install for all users: Unattended**.
5. To customize your unattended installation, select **[Advanced Settings](https://docs.uipath.com/robot/standalone/latest/admin-guide/windows-installations)**. Then customize the following settings:
   1. For **Installation Package**:
      * **Installation Path**—The destination folder for installation, other than the default one in `%ProgramFiles%`.
      * **License Code (optional)**—The key for your standalone trial or enterprise license. Without a key during a the standalone trial setup, Studio prompts for it upon its first launch.
      * **Orchestrator URL**—The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
      * **Client Id** and **Client Secret**—The client credentials from machine template objects. This pair produces a token, allowing unattended robots access to Orchestrator resources.
   2. For **Extensions**, select the extensions you want to install. By default, the Chrome and Edge Chromium extensions are installed.
      * **Default download location**—The download location for activity packages. Default location is `%userprofile%.nuget\packages`.
      * **Packages configuration**—Select the **Disable Online Feeds** option if you want to disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
   3. For **Security**, select the security options for your installation:
      * **Enforce Signed Execution**—Instructs the Robot to execute signed packages exclusively.
      * **Disable Secured XAMLs**—Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
      * **Disable Telemetry**—Disables the collection of anonymous usage data for Studio and Robot.
6. Select **Install**.