---
title: "Installing on Windows OS"
visible: true
slug: "windows-installations"
---

UiPath provides two installers for Windows. You can download them from the Resource Center in UiPath Automation Cloud or from the [Product Downloads](https://customerportal.uipath.com/product-downloads) section in Customer Portal.

## About 32-bit and 64-bit versions

* Before the 2021.4 release, Studio and Robot were 32-bit applications. However, from version 2021.4 onward, a 64-bit installer is the default.
* Starting with version 2023.4, a 32-bit installer is no longer provided, and the `UiPathPlatformInstaller.exe` is discontinued beginning with version 2021.4.
* To update existing 32-bit or 64-bit `UiPathStudio.msi` and `UiPathPlatformInstaller.exe` installations on 64-bit operating systems, use `UiPathStudio.msi`.
* The default installation path for pre-2021.4, 32-bit installation on a 64-bit system was `C:\Program Files (x86)\UiPath\Studio`. Upgrading to 64-bit installers migrates the installation to the `C:\Program Files\UiPath\Studio` folder. Installations that use custom paths do not change their directory after update.

## About quick and custom installations

You can perform the installation for the current user in a default configuration by selecting the **Quick** option in the installation wizard (no administrator privileges required) or configure the installation by selecting the **Custom** option (requires administrator privileges for per-machine installations).

:::note
If you are using Microsoft Windows Server, per-user installations may not be completed successfully. If an error occurs stating that policies have been set to prevent the installation, you can do one of the following if you are an administrator on the machine:
* Open the Registry Editor, and then, in the registry key `HKLM\Software\Policies\Microsoft\Windows\Installer`, configure the policy `DisableMSI = 0` to enable the Windows installer for all applications.
* Perform the installation per machine by installing using the **Custom** option.
:::
The following table summarizes the differences and similarities between quick and custom installations.

|  | Quick | Custom |
| --- | --- | --- |
| **Installation context** | Per user | Per user or per machine |
| **Supported robot installation types** | User mode | User mode for attended installations (per-user and per-machine).  Service mode for unattended installations (per-machine). |
| **Administrator privileges required for the installation** | No | Required only for per-machine installations. |
| **Installation directory** | `%LocalAppData%\Programs` | A custom location can be selected. The default location is:  `%LocalAppData%\Programs` for per-user installations.  `%ProgramFiles%` for per-machine installations. |
| **Activation with Community license** | Supported | Supported |
| **Activation with Enterprise license** | Supported | Supported |
| **Administrator privileges required**  for connecting to Orchestrator | No | Required only for the Service Mode robot |
| **Connection to Orchestrator using interactive sign-in** | Supported | Supported `<sup>1</sup>` |
| **Connection to Orchestrator using the machine key** | Supported | Supported |
| **Unattended execution without user login** | Not supported | Supported only for the Service Mode robot |

`<sup>1</sup>` - For the Service Mode robot, you must first connect to Orchestrator using client credentials, and then you can use interactive sign-in to change the user who connects to Orchestrator.

## Using UiPathStudio.msi

`UiPathStudio.msi` is the Windows installer that targets mainly developers. When installed, the software package includes both the development environment (UiPath Studio), UiPath Robot, and UiPath Assistant to execute the developed workflows.

If you are looking to build, debug, and test automation on the same machine, use this installer.

### Available installation options

* **Quick** installation - Installs a default configuration in the `%localappdata%\Programs\UiPath` directory. The default configuration includes:
  + Studio, StudioX and Assistant
  + Robot in User Mode
  + StudioX Excel add-on (if you have Microsoft Excel already installed on your machine)
  + Chrome extension (if you have Google Chrome already installed on your machine)
  + Edge Chromium extension (if you have Microsoft Edge Chromium already installed on your machine)
  + JavaScript Robot Add-on
  + Extension for Microsoft Remote Desktop

* **Custom** installation - Allows you to select the components you want to install, and configure advanced settings. The installation path is `%LocalAppData%\Programs` for current user installations, and `%ProgramFiles%` for installations applicable to all users on the device.

### Custom installation - available options

* **Install for me only** - Install your custom configuration in the user profile folder. No administrator privileges needed.
* **Install for all users on this computer** - Installs your custom configuration for all users on the machine. Needs administrator privileges.

### Install for me only - available installation packages

**Automation Developer** - Installs the following configuration, for running attended automations:
* Studio, StudioX and Assistant
* Robot in User Mode

**Attended Robot -** Installs the following configuration, for running attended automations, and automatically starts Assistant with Windows.
* Assistant
* Robot in User Mode

When you select an option, the **Advanced Settings** configuration becomes available, with the following options:

* **Installation Package**
  + **Orchestrator URL** - the URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
  + **Automatically sign in** - When your environment is configured to use [SSO with Azure Active Directory](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration), you can enable automatic authentication for your account.
* **Extensions &gt; Tools**
  + StudioX Excel Addin
  + UiPath JavaScript Robot Add-on
  + UiPath extension for Chrome
  + UiPath extension for Edge Chromium
  + UiPath extension for Firefox
  + UiPath extension for Microsoft Remote Desktop
* **Extensions &gt; Packages configuration**
  + **Disable Online Feeds** - Optionally, disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
* **Security**
  + **Enforce Signed Execution** - Instructs the Robot to execute signed packages exclusively.
  + **Disable Secured XAMLs** - Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
  + **Disable Telemetry** - Disables the collection of anonymous usage data for Studio and Robot.

### Install for all users on this computer - available installation packages

**Automation Developer** - Installs the following configuration, for running attended automations:
* Studio, StudioX and Assistant
* Robot in User Mode

**Automation Developer** - Installs the following configuration, for running attended automations:
* Studio, StudioX and Assistant
* Robot in User Mode

**Attended Robot -** Installs the following configuration, for running attended automations, and automatically starts Assistant with Windows.

When you select an option, the **Advanced Settings** configuration becomes available.

* **Installation Package**
  + **Installation Path** - The destination folder for installation. Default path is `%ProgramFiles%`.
  + **License Code (optional)** - The key for your standalone trial or enterprise license. Without a key during a the standalone trial setup, Studio prompts for it upon its first launch.
  + **Orchestrator URL** - The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
  + **Automatically sign in** - When your environment is configured to use [SSO with Azure Active Directory](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration), you can enable automatic authentication for your account.
  + **Automatically Starts Assistant with Windows** - Launches Assistant at Windows startup.
* **Extensions &gt; Tools**
  + StudioX Excel Addin
  + UiPath extension for Java
  + UiPath JavaScript Robot Add-on
  + UiPath extension for Citrix
  + UiPath extension for Chrome
  + UiPath extension for Edge Chromium
  + UiPath extension for Firefox
  + UiPath extension for Microsoft Remote Desktop
  + UiPath extension for VMware
  + SAP Solution Manager - Available if you have the SAP connector for Microsoft is already installed on your machine. If selected, you need to provide the hostname or IP address for your SAP Solution Manager instance in the **Host** box.
* **Extensions &gt; Default download location**
  + The download location for activity packages. Default location is `%userprofile%.nuget\packages`.
* **Extensions &gt; Packages configuration**
  + **Disable Online Feeds** - Optionally, disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
* **Security**
  + **Enforce Signed Execution** - Instructs the Robot to execute signed packages exclusively.
  + **Disable Secured XAMLs** - Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
  + **Disable Telemetry** - Disables the collection of anonymous usage data for Studio and Robot.

**Unattended Robot** - Installs the following configuration, for running unattended automations:
* Assistant
* Robot in Service Mode

When you select an option, the **Advanced Settings** configuration becomes available.

* **Installation Package**
  + **License Code (optional)** - The key for your standalone trial or enterprise license. Without a key during a the standalone trial setup, Studio prompts for it upon its first launch.
  + **Orchestrator URL** - The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config`file.
  + **Client Id** and **Client Secret** - The client credentials from machine template objects. This pair produces a token, allowing unattended robots access to Orchestrator resources.
  + **Install UiPath Studio** - If selected, installs Studio for design purposes.
* **Extensions &gt; Tools**
  + StudioX Excel Addin
  + UiPath extension for Java
  + UiPath JavaScript Robot Add-on
  + UiPath extension for Citrix
  + UiPath extension for Chrome (*)
  + UiPath extension for Edge Chromium (*)
  + UiPath extension for Firefox
  + UiPath extension for Microsoft Remote Desktop
  + UiPath extension for VMware
  + SAP Solution Manager - Available if you have the SAP connector for Microsoft is already installed on your machine. If selected, you need to provide the hostname or IP address for your SAP Solution Manager instance in the **Host** box.(*) These options are selected by default.
* **Extensions &gt; Default download location**
  + The download location for activity packages. Default location is `%userprofile%.nuget\packages`.
* **Extensions &gt; Packages configuration**
  + **Disable Online Feeds** - Optionally, disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
* **Security**
  + **Enforce Signed Execution** - Instructs the Robot to execute signed packages exclusively.
  + **Disable Secured XAMLs** - Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
  + **Disable Telemetry** - Disables the collection of anonymous usage data for Studio and Robot.

## Using UiPathRobot.msi

`UiPathRobot.msi` is typically installed on Windows machines that mainly execute automations. No development environment is attached to this installation, and thus, resource allocation is primarily for running robots. It includes UiPath Robot and UiPath Assistant.

### Available installation options

* **Quick** installation - Installs a default configuration in the `%localappdata%\Programs\UiPath` directory. The default configuration includes:
  + Studio, StudioX and Assistant
  + Robot in User Mode
  + StudioX Excel add-on (if you have Microsoft Excel already installed on your machine)
  + Chrome extension (if you have Google Chrome already installed on your machine)
  + Edge Chromium extension (if you have Microsoft Edge Chromium already installed on your machine)
  + JavaScript Robot Add-on
  + Extension for Microsoft Remote Desktop

* **Custom** installation - Allows you to select the components you want to install, and configure advanced settings. The installation path is `%LocalAppData%\Programs` for current user installations, and `%ProgramFiles%` for installations applicable to all users on the device.

### Custom **-** available installation packages

**Install for me only: Attended** - Installs Robot and Assistant to run attended automations.
* Your custom configuration applies to the current user profile.
* Robot is installed in User Mode.
* No administrator privileges needed.

When you select this option, the **Advanced Settings** configuration becomes available.

* **Installation Package**
  + **Orchestrator URL** — The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
  + **Automatically sign in** — When your environment is configured to use [SSO with Azure Active Directory](https://docs-dev.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration), you can enable automatic authentication for your account.
* **Extensions &gt; Tools**
  + UiPath JavaScript Robot Add-on (*)
  + UiPath extension for Chrome (*)
  + UiPath extension for Edge Chromium (*)
  + UiPath extension for Firefox
  + UiPath extension for Microsoft Remote Desktop(*) These options are selected by default.
* **Extensions &gt; Packages configuration**
  + **Disable Online Feeds** - Optionally, disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
* **Security**
  + **Enforce Signed Execution** - Instructs the Robot to execute signed packages exclusively.
  + **Disable Secured XAMLs** - Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
  + **Disable Telemetry** - Disables the collection of anonymous usage data for Studio and Robot.

**Install for all users: Attended -** Installs Robot and Assistant to run attended automations.
* Your custom configuration applies to all users on the machine.
* Robot is installed in User Mode.
* Needs administrator privileges.
* Automatically starts Assistant with Windows.

When you select this option, the **Advanced Settings** configuration becomes available.

* **Installation Package**
  + **Installation Path** - The destination folder for installation. Default path is `%ProgramFiles%`.
  + **License Code (optional)** - The key for your standalone trial or enterprise license. Without a key during a the standalone trial setup, Studio prompts for it upon its first launch.
  + **Orchestrator URL** - The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
  + **Automatically sign in** - When your environment is configured to use [SSO with Azure Active Directory](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration), you can enable automatic authentication for your account.
  + **Automatically Starts Assistant with Windows** - Launches Assistant at Windows startup.
* **Extensions &gt; Tools**
  + UiPath extension for Java
  + UiPath JavaScript Robot Add-on (*)
  + UiPath extension for Citrix
  + UiPath extension for Chrome (*)
  + UiPath extension for Edge Chromium (*)
  + UiPath extension for Firefox
  + UiPath extension for Microsoft Remote Desktop
  + UiPath extension for VMware(*) These options are selected by default.
* **Extensions &gt; Default download location**
  + The download location for activity packages. Default location is `%userprofile%.nuget\packages`.
* **Extensions &gt; Packages configuration**
  + **Disable Online Feeds** - Optionally, disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
* **Security**
  + **Enforce Signed Execution** - Instructs the Robot to execute signed packages exclusively.
  + **Disable Secured XAMLs** - Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
  + **Disable Telemetry** - Disables the collection of anonymous usage data for Studio and Robot.

**Install for all users: Unattended** - Installs Robot to run unattended automations via Orchestrator, and installs Assistant to troubleshoot issues.
* Your custom configuration applies to all users on the machine.
* Robot is installed in Service Mode.
* Needs administrator privileges.

When you select this option, the **Advanced Settings** configuration becomes available.

* **Installation Package**
  + **Installation Path** - The destination folder for installation. Default path is `%ProgramFiles%`.
  + **License Code (optional)** - The key for your standalone trial or enterprise license. Without a key during a the standalone trial setup, Studio prompts for it upon its first launch.
  + **Orchestrator URL** - The URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file.
  + **Client Id** and **Client Secret** - The client credentials from machine template objects. This pair produces a token, allowing unattended robots access to Orchestrator resources.
* **Extensions &gt; Tools**
  + UiPath extension for Java
  + UiPath JavaScript Robot Add-on
  + UiPath extension for Citrix
  + UiPath extension for Chrome (*)
  + UiPath extension for Edge Chromium (*)
  + UiPath extension for Firefox
  + UiPath extension for Microsoft Remote Desktop
  + UiPath extension for VMware(*) These options are selected by default.
* **Extensions &gt; Default download location**
  + The download location for activity packages. Default location is `%userprofile%.nuget\packages`.
* **Extensions &gt; Packages configuration**
  + **Disable Online Feeds** - Optionally, disable the Official and Marketplace online feeds for activity packages. Recommended for offline environments.
* **Security**
  + **Enforce Signed Execution** - Instructs the Robot to execute signed packages exclusively.
  + **Disable Secured XAMLs** - Disables security of XAML files for Robots installed as a Windows service. Unsecured XAML files allow users to read and modify the process files and logic.
  + **Disable Telemetry** - Disables the collection of anonymous usage data for Studio and Robot.

## Using the Command Prompt

Installing Robot or Studio using command line parameters is useful for installation on multiple machines, for silent installations, and for saving system resources that a graphical wizard might consume. It also allows customized installation settings and integration with scripts.

:::important
To install the Robot using the command prompt, you need administrator privileges.
:::

### Best practices

* To escape the "%" character in system variable names, such as %username%, use the following command:
  ```
  ^ - UiPathRobot.msi PACKAGES_FOLDER=C:\Some\Path\^%USERNAME^%
  ```

  :::note
  In PowerShell, no escaping is needed.
  :::
* When using Active Directory domain accounts, specify the domain name in the folder structure:
  ```
  C:\packages\^%UserDomain^%.^%Username^%
  ```
* To use paths that contain spaces, use quotes:
  + In Command Prompt, use double quotes:
    ```
    UiPathRobot.msi APPLICATIONFOLDER="C:\folder name"
    ```
  + In PowerShell, use single and double quotes:
    ```
    ./UiPathRobot.msi APPLICATIONFOLDER='"C:\folder name"'
    ```

### Clean installations - command line parameters

These parameters are available when running the `UiPathStudio.msi` or `UiPathRobot.msi` from the command line.

* `/q` - Installs the specified UiPath features silently, without displaying the user interface.
* `/l*vx <LogFile>` - Generates an installer log file at the specified path. You can send the file further to our support team if, for any reason, you encounter difficulties during the installation process.
* `ADDLOCAL` - Allows selecting the features to install. Without this parameter, the following features are installed by default: Robot in Service Mode, Default activity packages, and JavaScript Add-on. It supports the following options:
  + `DesktopFeature`— Indicates that you want to install the Robot feature.
  + `Studio` (exclusively for UiPathStudio.msi) — Installs Studio. Must be used together with the `DesktopFeature` parameter.
  + `ExcelAddin` (exclusively for UiPathStudio.msi) — Installs the StudioX Excel Add-in. Must be used together with the `Studio` parameter.
  + `Robot` — Installs the Robot in User Mode or Service Mode, as well as the Assistant. Must be used together with the `DesktopFeature`parameter.
  + `RegisterService` — Required for Service Mode installations. Do not add it for User Mode installations.
  + `StartupLauncher` — Runs the Robot at Windows startup. Must be used together with the `DesktopFeature` parameter.
  + `Packages` (exclusively for UiPathStudio.msi) — Installs the default activity packages. Must be used together with the `Robot` parameter.
  + `JavaBridge` — Installs the UiPath Java Bridge for better integration and automation with Java applications. Adding this may increase installation time. Must be used together with the `Robot` parameter.
  + `ChromeExtension` — Installs the Google Chrome Extension. Must be used together with the `Robot` parameter.
  + `FirefoxExtension` — Installs the Firefox extension. Must be used together with the `Robot` parameter.
  + `EdgeExtension` — Installs the Microsoft Edge Chromium-based Extension. Must be used together with the `Robot` parameter.
  + `CitrixClient` — Installs the UiPath Citrix Client Extension. Must be used together with the `Robot` parameter. Not available for per-user installations.
  + `JavaScriptAddOn` — Installs the Browser Embedding add-on. Must be used together with the `Robot` parameter. Cannot be used with elevated rights.
  + `SapPlugin` (exclusively for UiPathStudio.msi) — Installs the SAP Solution Manager plugin. Requires the SAP Connector for Microsoft to be installed on your machine. On clean installs, you must also provide an address for the instance using the `SAP_SOL_MAN_HOST` parameter. Must be used together with the `Studio` parameter. Not available for per-user installations.
  + `VMwareExtension` — Installs the UiPath extension for VMware Horizon. Must be used together with the `Robot` parameter. Not available for per-user installations.
  + `WindowsRdpExtension` — Installs the UiPath extension for Windows Remote Desktop. Must be used together with the `Robot` parameter.
* `MSIINSTALLPERUSER` - Enables you to install only for the current user.
  + To install per user, add `MSIINSTALLPERUSER=1`. The following options are not available in per-user installations: RegisterService, CitrixExtension, VMwareExtension, PACKAGES_FOLDER, CODE.
  + To install per machine, do not include this parameter.
* `SAP_SOL_MAN_HOST` (exclusively for `UiPathStudio.msi`) - The hostname or IP address of your SAP Solution Manager instance. Required for clean installations where the `SapPlugin` parameter was added in the `ADDLOCAL` option.
* `APPLICATIONFOLDER` - Enables you to install the Robot in a custom location.
* `NUGET_OPTIONS` - For offline environments. If set to `DisableOnlineFeeds`, this parameter disables the online UiPath official and Community feeds for the Robot, and uses Orchestrator and local feeds exclusively.
  :::note
  The URL feeds remain in the configuration files, but are ignored.
  :::
* `PACKAGES_FOLDER`
  + Enables you to change the download location for your workflows and their dependencies. The chosen folder can be user-specific or accessible by all users on a machine.
  + Without this parameter, the default download location is `%userProfile%\.nuget\packages`.
  + Not available for per-user installations.
    :::note
    Make sure that all users that need to execute processes have read access to the new folder.
    :::
  + Find out how to set up [custom package folders and network paths](https://docs.uipath.com/robot/standalone/latest/admin-guide/setting-up-package-folders-and-network-paths-unattended#setting-up-package-folders-and-network-paths).
  + For installations on Windows Server machines that enable concurrent execution, you must provide paths that are specific to each user. Read more about [using the same path for multiple robots](https://docs.uipath.com/robot/standalone/latest/admin-guide/setting-up-package-folders-and-network-paths-unattended#setting-up-local-and-network-paths).
  + Find out [how to change the download folder for packages after installation](https://docs.uipath.com/studio/standalone/latest/user-guide/managing-activities-packages).
* `CUSTOM_NUGET_FEEDS` - Enables you to add custom NuGet activities feeds for Studio and/or Robot. This command only adds or updates the existing list of feeds. It must be populated with key-value pairs of type string:
  + Valid locations include online feeds, folder paths, and shared network drives.
  + Make sure that the provided feeds are accessible by all users on a given machine.
  + Separate feeds with semicolons (;). For example:
    ```
    CUSTOM_NUGET_FEEDS="FeedName1,https://my.custom.nuget.feed; FeedName2,D:\Custom\Activities\Packages\"
    ```
* `ENFORCE_SIGNED_EXECUTION` - Optional. Enables you to enforce your Robots to execute only signed packages. Without this parameter, package signing is not enabled. It has the following options:
  + `1` - The Robot only handles packages signed by UiPath-verified authors or repositories. To add your own certificate as a trusted source, modify the `nuget.config` file.
  + `0` - No package signing rule is enforced on your Robot deployment.For more details, see [Signing Packages](https://docs.uipath.com/studio/standalone/latest/user-guide/signing-packages).
* `CODE` - Licenses your Robot instance. Not available for per-user installations.
* `CLIENT_ID` and `CLIENT_SECRET` - Automatically connects the Robot to Orchestrator [using client credentials](https://docs.uipath.com/orchestrator/standalone/latest/user-guide/connecting-robots-to-orchestrator), while also installing it. For example:
  ```
  UiPathRobot.msi ORCHESTRATOR_URL=https://demo.uipath.com/company/tenant/orchestrator_ CLIENT_ID=1234-abcd-1ab2-cd32-1111 CLIENT_SECRET=2143ndafj32k
  ```
* `CHROME_INSTALL_TYPE` - Allows you to choose the installation method for the Chrome extension. Needs admin rights. Without this parameter, the most appropriate method is selected automatically. It has the following options:
  + `POLICYOFFLINE` - The Chrome Extension is automatically installed per system via the Group Policy [Offline](https://docs.uipath.com/studio/standalone/latest/user-guide/extension-for-chrome#offline) method, the equivalent of calling the `/Chrome-Policy-Offline` command using the [SetupExtensions tool](https://docs.uipath.com/studio/standalone/latest/user-guide/about-the-setupextensions-tool).
  + `POLICYONLINE` - The Edge Extension is automatically installed per system via the Group Policy [Online](https://docs.uipath.com/studio/standalone/latest/user-guide/extension-for-edge-chromium#online) method, the equivalent of calling the `/Edge-Chromium-PolicyGlobal` command using the [SetupExtensions tool](https://docs.uipath.com/studio/standalone/latest/user-guide/about-the-setupextensions-tool).
  + `MANUALPERMACHINE` - The Chrome Extension is installed for all users, the equivalent of calling the `/ChromeGlobal` command using the [SetupExtensions tool](https://docs.uipath.com/studio/standalone/latest/user-guide/about-the-setupextensions-tool).
  + `NATIVEHOSTONLY` - Only the Native Messaging Host component (`ChromeNativeMessaging.exe`) is installed, the equivalent of calling the `/ChromeNativeHostGlobal` command using the [SetupExtensions tool](https://docs.uipath.com/studio/standalone/latest/user-guide/about-the-setupextensions-tool).
  :::note
  The old installation methods names (`STORE`, `GLOBAL`) are kept for backwards compatibility.
  :::
* `EDGE_INSTALL_TYPE` - Allows you to choose the installation method for the Edge extension. Needs admin rights. Without this parameter, the most appropriate method is selected automatically. It has the following options:
  + `POLICYOFFLINE` - The Edge Extension is automatically installed per system via the Group Policy [Offline](https://docs.uipath.com/studio/standalone/latest/user-guide/extension-for-edge-chromium#offline) method, the equivalent of calling the `/Edge-Policy-Offline` command using the [SetupExtensions tool](https://docs.uipath.com/studio/standalone/latest/user-guide/about-the-setupextensions-tool).
  + `POLICYONLINE` - The Edge Extension is automatically installed per system via the Group Policy [Online](https://docs.uipath.com/studio/standalone/latest/user-guide/extension-for-edge-chromium#online) method, the equivalent of calling the `/Edge-Chromium-PolicyGlobal` command using the [SetupExtensions tool](https://docs.uipath.com/studio/standalone/latest/user-guide/about-the-setupextensions-tool).
  + `MANUALPERMACHINE` - The Edge Extension is installed for all users, the equivalent of calling the `/Edge-Chromium-Global` command using the [SetupExtensions tool](https://docs.uipath.com/studio/standalone/latest/user-guide/about-the-setupextensions-tool).
  + `NATIVEHOSTONLY` - Only the Native Messaging Host component (`ChromeNativeMessaging.exe`) is installed, the equivalent of calling the `/Edge-Chromium-NativeHostGlobal` command using the [SetupExtensions tool](https://docs.uipath.com/studio/standalone/latest/user-guide/about-the-setupextensions-tool).
  :::note
  The old installation methods names (`STORE`, `GLOBAL`) are kept for backwards compatibility.
  :::
* `DISABLE_SECURE_XAML` - Allows you to disable security of `XAML` files for Robots installed as a Windows service. Unsecured `XAML` files allow users to read and modify the process files and logic. It has the following options:
  + `0` - The default option. Enables security for `XAML` files for Windows service Robots.
  + `1` - Disables security for `XAML` files for Windows service Robots.
* `SERVICE_URL` - Allows you to define the URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file. Required by User Mode installations. Service Mode installations ignore this parameter.
* `ORCHESTRATOR_URL` - In clean installations, you can specify the main Orchestrator URL, used for retrieving auto-update information. For example: `https://orchestrator.local/organizationName/tenantName`.
* `TELEMETRY_ENABLED` - Allows you to disable the usage data collection. It has the following options:
  + `0` - Disables the telemetry for Studio and Robot.
  + `1` - Default option. Enables the telemetry for Studio and Robot.Find out how to [opt out of telemetry](https://docs.uipath.com/studio/standalone/latest/user-guide/opting-out-of-telemetry).
* `ENABLE_PIP` - Allows you to enable the Robot session (Picture in Picture) functionality of the machine. It has the following options:
  + `0` - Default option. The Robot session capability is disabled.
  + `1` - Enables the Robot session capability.
* `INSTALLER_LANGUAGE` - Enables you to select the display language of the installer. Without this parameter, the installer uses the language settings in Windows. It has the following options:
  + `2052` - Chinese (Simplified)
  + `12` - French
  + `7` - German
  + `17` - Japanese
  + `1` - Korean
  + `22` - Portuguese (Portugal)
  + `1046` - Portuguese (Brazil)
  + `25` - Russian
  + `10` - Spanish (Spain)
  + `2058` - Spanish (Mexico)
  + `31` - Turkish
* `ASSISTANT_OPTIONS` - Enables or disables the [Marketplace widget](https://docs.uipath.com/robot/standalone/latest/user-guide/marketplace-widget) for Assistant. It has the following options:
  + Absent or `EnableMarketplace` - The default option. Enables the widget.
  + `DisableMarketplace` - Disables the widget.
* `ORCHESTRATOR_AUTO_SIGNIN` - Enables automatic sign-in to your account. For User Mode installations and environments configured to use the [SSO with Azure Active Directory](https://docs.uipath.com/automation-cloud/automation-cloud/latest/admin-guide/azure-ad-integration). Must be used together with the `ORCHESTRATOR_URL` parameter. It has the following options:
  + `0` - Disables the automatic sign-in.
  + `1` - Enables the automatic sign-in.
* `ENFORCE_DEFAULT_SERVICE_URL` - Enforces the default service URL. For User Mode installations. Must be used together with the `ORCHESTRATOR_URL` parameter. It has the following options:
  + `0` - Disables the enforcement of the default service URL.
  + `1` - Enables the enforcement of the default service URL.
* `PROXY_SCRIPT_ADDRESS` - The address of the script that determines how and when to use the proxy. Should contain the URI of the script file, for example, `http://localhost/proxy.pac`.
  :::note
  * If you use this parameter, do not use other proxy-specific parameters.
  * When all parameters are present in the UiPath.config file, only the `ScriptAddress` key is used.
  :::
* `PROXY_ADDRESS` - The address of the proxy server, either IP or domain name. For example, `http://my.proxy.net:8008`.
  :::note
  To be used together with:
  * `PROXY_BYPASS_LOCAL_ADDRESS`
  * `PROXY_BYPASS_LIST`
  Or with:
  * `PROXY_USER_NAME`
  * `PROXY_PASSWORD`
  * `PROXY_DOMAIN`
  :::
* `PROXY_BYPASS_LOCAL_ADDRESS` - Allows direct connection for local addresses, bypassing the proxy server. Set it to 1 to bypass the local address, or to 0 otherwise.
  :::note
  To be used together with:
  * `PROXY_ADDRESS`
  * `PROXY_BYPASS_LIST`
  :::
* `PROXY_BYPASS_LIST` - The list of addresses that connect directly to the internet, bypassing the proxy server. Should contain RegExr strings that contain the URIs of servers to bypass. For example, `server.domain.local$;www.google.com;192.168.\d{1,3}.\d{1,3}`.
  :::note
  To be used together with:
  * `PROXY_ADDRESS`
  * `PROXY_BYPASS_LIST`
  :::
* `PROXY_USER_NAME` - Requires `PROXY_PASSWORD`. The username credential for proxy server authentication.
* `PROXY_PASSWORD` - The password associated with the username for proxy server authentication.
* `PROXY_DOMAIN` - The domain where the proxy server resides, required for authentication.

### Updating or modifying existing installations - command line parameters

These parameters are available when running the `UiPathStudio.msi` from the command line.

* `/q` - Not supported for changing an existing installation. Updates the specified UiPath features silently, without displaying the user interface.
* `ADDLOCAL` - Allows selecting the features to update. Without this parameter, the following features are updated by default: Robot in Service Mode, Default activity packages, and JavaScript Add-on. It supports the following options:
  + `DesktopFeature`— Indicates that you want to install the Robot feature.
  + `Studio` (exclusively for UiPathStudio.msi) — Installs Studio. Must be used together with the `DesktopFeature` parameter.
  + `ExcelAddin` (exclusively for UiPathStudio.msi) — Installs the StudioX Excel Add-in. Must be used together with the `Studio` parameter.
  + `Robot` — Installs the Robot in User Mode or Service Mode, as well as the Assistant. Must be used together with the `DesktopFeature` parameter.
  + `RegisterService` — Required for Service Mode installations. Do not add it for User Mode installations.
  + `LiveStreaming` - Installs the live streaming software (RealVNC) on the machine. See [The Live Streaming feature](https://docs.uipath.com/robot/standalone/latest/admin-guide/windows-installations#the-live-streaming-feature).
  + `StartupLauncher` — Runs the Robot at Windows startup. Must be used together with the `DesktopFeature` parameter.
  + `Packages` (exclusively for UiPathStudio.msi) — Installs the default activity packages. Must be used together with the `Robot` parameter.
  + `JavaBridge` — Installs the UiPath Java Bridge for better integration and automation with Java applications. Adding this may increase installation time. Must be used together with the `Robot` parameter.
  + `ChromeExtension` — Installs the Google Chrome Extension. Must be used together with the `Robot` parameter.
  + `FirefoxExtension` — Installs the Firefox extension. Must be used together with the `Robot` parameter.
  + `EdgeExtension` — Installs the Microsoft Edge Chromium-based Extension. Must be used together with the `Robot` parameter.
  + `CitrixClient` — Installs the UiPath Citrix Client Extension. Must be used together with the `Robot` parameter. Not available for per-user installations.
  + `JavaScriptAddOn` — Installs the Browser Embedding add-on. Must be used together with the `Robot` parameter. Cannot be used with elevated rights.
  + `SapPlugin` (exclusively for UiPathStudio.msi) — Installs the SAP Solution Manager plugin. Requires the SAP Connector for Microsoft to be installed on your machine. On clean installs, you must also provide an address for the instance using the `SAP_SOL_MAN_HOST` parameter. Must be used together with the `Studio` parameter. Not available for per-user installations.
  + `VMwareExtension` — Installs the UiPath extension for VMware Horizon. Must be used together with the `Robot` parameter. Not available for per-user installations.
  + `WindowsRdpExtension` — Installs the UiPath extension for Windows Remote Desktop. Must be used together with the `Robot` parameter.
* `REMOVE` - Disables a feature.
  :::note
  Robot cannot be removed.
  :::
* `NUGET_OPTIONS` - Not supported for changing an existing installation. For offline environments. If set to `DisableOnlineFeeds`, this parameter disables the online UiPath official and Community feeds for the Robot, and uses Orchestrator and local feeds exclusively.
  :::note
  The URL feeds remain in the configuration files, but are ignored.
  :::
* `ENFORCE_SIGNED_EXECUTION` - Optional. Enables you to enforce your Robots to execute only signed packages. Without this parameter, package signing is not enabled. Not supported for changing an existing installation. It has the following options:
  + `1` - The Robot only handles packages signed by UiPath-verified authors or repositories. To add your own certificate as a trusted source, modify the `nuget.config` file.
  + `0` - No package signing rule is enforced on your Robot deployment.For more details, see [Signing Packages](https://docs.uipath.com/studio/standalone/latest/user-guide/signing-packages).
* `SERVICE_URL` - Allows you to define the URL of the Orchestrator instance to connect to using Interactive Sign-In. This value is saved in the `uipath.config` file. Available when switching the Robot from Service Mode to User Mode, by not including the `RegisterService` parameter.
* `TELEMETRY_ENABLED` - Allows you to disable the usage data collection. Not supported for changing an existing installation. It has the following options:
  + `0` - Disables the telemetry for Studio and Robot.
  + `1` - Default option. Enables the telemetry for Studio and Robot.Find out how to [opt out of telemetry](https://docs.uipath.com/studio/standalone/latest/user-guide/opting-out-of-telemetry).
* `ASSISTANT_OPTIONS` - Enables or disables the [Marketplace widget](https://docs.uipath.com/robot/standalone/latest/user-guide/marketplace-widget) for Assistant. It has the following options:
  + Absent or `EnableMarketplace` - The default option. Enables the widget.
  + `DisableMarketplace` - Disables the widget.
* `DISABLE_SECURE_XAML` - Allows you to disable security of `XAML` files for Robots installed as a Windows service. Unsecured `XAML` files allow users to read and modify the process files and logic. Not supported for changing an existing installation. It has the following options:
  + `0` - The default option. Enables security for `XAML` files for Windows service Robots.
  + `1` - Disables security for `XAML` files for Windows service Robots.

## The live streaming feature

Starting with version 2024.10, the [live streaming](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/live-streaming-and-remote-control-via-realvnc) feature uses the RealVNC software, which comes bundled in the UiPath Robot and UiPath Studio 2024.10+ installers. Installing or upgrading to the 2024.10+ Robot using the GUI or the command prompt automatically installs RealVNC , unless the `ADDLOCAL` parameter is used. If you choose to use the `ADDLOCAL` parameter in a command prompt installation, you must add the `LiveStreaming` flag.

For example, the following `UiPathRobot.msi` command performs a custom installation or upgrade which also installs RealVNC, the software that is required for live streaming:

```
UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,RegisterService,LiveStreaming
```