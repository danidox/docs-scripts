---
title: "Installing with UiPathStudio.msi"
visible: true
slug: "installing-with-uipath-studio-msi-attended"
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
4. In the **Select install mode** section, decide who should be able to use the attended installation:
   * **Install for me only** - Installs Studio, Robot, and Assistant in the user profile folder. No administrator privileges needed. Follow step 6 for options on installation packages.
   * **Install for all users on this computer** - Installs Studio, Robot, and Assistant for all users on the machine. Needs administrator privileges. Follow step 9 for options on installation packages.
5. Select **Choose packages.**
6. For **Install for me only** installations, decide what software to install for running attended automations:
   * **Automation Developer** - Installs Studio, StudioX, Robot, and Assistant. Follow step 7 for advanced settings.
   * **Attended** - Installs Robot and Assistant. Follow step 8 for advanced settings.
7. To customize the **Automation Developer** installation, select **Advanced Settings**. Then customize the following settings:
   1. For **Installation Package**:
      * **Orchestrator URL** - The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
      * **Automatically sign in** - When your environment is configured to use [SSO with Azure Active Directory](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration), select this option to enable automatic authentication for your account.
   2. For **Extensions**, select the extensions you want to install. By default, the StudioX Excel Addin, UiPath JavaScript Robot Add-on, Chrome, and Edge Chromium extensions are installed.
      * **Packages configuration** - Select the **Disable Online Feeds** option if you want to disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
   3. For **Security**, select the security options for your installation:
      * **Enforce Signed Execution** - Instructs the Robot to execute signed packages exclusively.
      * **Disable Secured XAMLs** - Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
      * **Disable Telemetry** - Disables the collection of anonymous usage data for Studio and Robot.
8. To customize the **Attended** installation, select **Advanced Settings**. Then customize the following settings:
   1. For **Installation Package**:
      * **Orchestrator URL** - The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
      * **Automatically sign in** - When your environment is configured to use [SSO with Azure Active Directory](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration), select this option to enable automatic authentication for your account.
   2. For **Extensions**, select the extensions you want to install. By default, the UiPath JavaScript Robot Add-on, Chrome, and Edge Chromium extensions are installed.
      * **Packages configuration** - Select the **Disable Online Feeds** option if you want to disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
   3. For **Security**, select the security options for your installation:
      * **Enforce Signed Execution** - Instructs the Robot to execute signed packages exclusively.
      * **Disable Secured XAMLs** - Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
      * **Disable Telemetry** - Disables the collection of anonymous usage data for Studio and Robot.
9. For **Install for all users on this computer** installations, decide what software to install for running attended automations:
   * **Automation Developer** - Installs Studio, StudioX, Robot, and Assistant. Follow step 10 for advanced settings.
   * **Attended Robot** - Installs Robot and Assistant. Follow step 11 for advanced settings.
10. To customize the **Automation Developer** installation, select **Advanced Settings**. Then customize the following settings:
    1. For **Installation Package**:
       * **Installation Path** - The destination folder for installation, other than the default one in `%ProgramFiles%`.
       * **License Code (optional)** - The key for your standalone trial or enterprise license. Without a key during a the standalone trial setup, Studio prompts for it upon its first launch.
       * **Orchestrator URL** - The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
       * **Automatically sign in** - When your environment is configured to use [SSO with Azure Active Directory](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration), select this option to enable automatic authentication for your account.
       * **Automatically Starts Assistant with Windows** - Launches Assistant at Windows startup.
    2. For **Extensions**, select the extensions you want to install. By default, the UiPath JavaScript Robot Add-on, Chrome, and Edge Chromium extensions are installed.
       * **Host for SAP Solution Manager** - Available if you have the SAP connector for Microsoft is already installed on your machine. If selected, you need to provide the hostname or IP address for your SAP Solution Manager instance.
       * **Default download location** - The download location for activity packages. Default location is `%userprofile%.nuget\packages`.
       * **Packages configuration** - Select the **Disable Online Feeds** option if you want to disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
    3. For **Security**, select the security options for your installation:
       * **Enforce Signed Execution** - Instructs the Robot to execute signed packages exclusively.
       * **Disable Secured XAMLs** - Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
       * **Disable Telemetry** - Disables the collection of anonymous usage data for Studio and Robot.
11. To customize the **Attended Robot** installation, select **Advanced Settings**. Then customize the following settings:
    1. For **Installation Package**:
       * **Installation Path** - The destination folder for installation, other than the default one in `%ProgramFiles%`.
       * **License Code (optional)** - The key for your standalone trial or enterprise license. Without a key during a the standalone trial setup, Studio prompts for it upon its first launch.
       * **Orchestrator URL** - The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
       * **Automatically sign in** - When your environment is configured to use [SSO with Azure Active Directory](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration), select this option to enable automatic authentication for your account.
       * **Automatically Starts Assistant with Windows** - Launches Assistant at Windows startup.
    2. For **Extensions**, select the extensions you want to install. By default, the UiPath JavaScript Robot Add-on, Chrome, and Edge Chromium extensions are installed.
       * **Host for SAP Solution Manager** - Available if you have the SAP connector for Microsoft is already installed on your machine. If selected, you need to provide the hostname or IP address for your SAP Solution Manager instance.
       * **Default download location** - The download location for activity packages. Default location is `%userprofile%.nuget\packages`.
       * **Packages configuration** - Select the **Disable Online Feeds** option if you want to disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
    3. For **Security**, select the security options for your installation:
       * **Enforce Signed Execution** - Instructs the Robot to execute signed packages exclusively.
       * **Disable Secured XAMLs** - Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
       * **Disable Telemetry** - Disables the collection of anonymous usage data for Studio and Robot.
12. Select **Install**.