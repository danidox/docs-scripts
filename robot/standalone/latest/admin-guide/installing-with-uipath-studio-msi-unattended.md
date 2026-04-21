---
title: "Installing with UiPathStudio.msi"
visible: true
slug: "installing-with-uipath-studio-msi-unattended"
---

Running the `UiPathStudio.msi` installs Studio, Robot, and Assistant.

First, download the installer from the [Product Downloads](https://customerportal.uipath.com/product-downloads) section in Customer Portal. Look for the following entries:

* For Enterprise versions—**UiPath Studio &lt;version_number&gt;**
* For Community versions—**UiPath Studio, Robot, Assistant (Community Version)**

Once the download is complete, continue with the following steps.

1. Launch the installer.
2. Read and accept the [License Agreement](https://www.uipath.com/developers/all-editions/license-agreement), which includes the UiPath terms of use for activity packages and their dependencies.
3. Select the type of installation: **Quick (recommended for Community Users)** or **Custom (recommended for Enterprise/Advanced Users)**.

If you select **Quick (recommended for Community Users)**, continue the installation by selecting **Install**.

For **Custom (recommended for Enterprise/Advanced Users)**, continue by selecting **Configure** and following the remaining steps.
4. In the **Select install mode** section, select **Install for all users on this computer**, then select **Choose Packages**. You need administrator privileges to use this option.
5. In the **Choose an installation package** section, select **Unattended Robot**.
6. To customize your unattended installation, select **[Advanced Settings](https://docs.uipath.com/robot/standalone/latest/admin-guide/windows-installations)**. Then customize the following settings:
   1. For **Installation Package**:
      * **Installation Path**—The destination folder for installation, other than the default one in `%ProgramFiles%`.
      * **License Code (optional)**—The key for your standalone trial or enterprise license. Without a key during a the standalone trial setup, Studio prompts for it upon its first launch.
      * **Orchestrator URL**—The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
      * **Client Id** and **Client Secret**—The client credentials from machine template objects. This pair produces a token, allowing unattended robots access to Orchestrator resources.
      * **Install UiPath Studio**—If selected, installs Studio for design purposes.
   2. For **Extensions**, select the extensions you want to install. By default, the Chrome and Edge Chromium extensions are installed.
      * **Host for SAP Solution Manager**—Available if you have the SAP connector for Microsoft is already installed on your machine. If selected, you need to provide the hostname or IP address for your SAP Solution Manager instance.
      * **Default download location**—Available if you have the SAP connector for Microsoft is already installed on your machine. If selected, you need to provide the hostname or IP address for your SAP Solution Manager instance.
      * **Packages configuration**—Select the Disable Online Feeds option if you want to disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments**.**
   3. For **Security**, select the security options for your installation:
      * **Enforce Signed Execution**—Instructs the Robot to execute signed packages exclusively.
      * **Disable Secured XAMLs**—Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
      * **Disable Telemetry**—Disables the collection of anonymous usage data for Studio and Robot.
7. Select **Install** (requires administrator privileges).