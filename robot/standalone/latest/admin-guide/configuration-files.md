---
title: "Configuration files"
visible: true
slug: "configuration-files"
---

Once you edit configuration files, you need to restart the relevant Robot components for changes to take effect. The following list summarizes how to restart several components, based on the Robot installation mode.

Remember to save any ongoing work before you restart to avoid losing any unsaved progress.

* **Robot Service**
  + Service Mode installation
    1. Open **Task Manager** &gt; **Services**.
    2. Look for the `UiPathRobotSvc` service.
    3. Right-click the service and select **Restart**.
  + User Mode installation - Quit, then relaunch the Assistant, or:
    1. Open **Task Manager** &gt; **Details**.
    2. Select the `UiPath.Service.UserHost.exe` process.
    3. Select **End task**.
* **Update Service**
  1. Open **Task Manager** &gt; **Services**.
  2. Look for the `UiPath.UpdateService.Agent` service.
  3. Right-click the service and select **Restart**.
* **UiPath RobotJS ServiceHost**
  1. Open **Task Manager** &gt; **Services**.
  2. Look for the `UiPath.RobotJS.ServiceHost` service.
  3. Right-click the service and select **Restart**.
* **UiPath Assistant**
  1. In Assistant, select **Preferences**, then **Quit**.
  2. Relaunch the Assistant.
* **Widgets** - Restart the Assistant, or:
  1. Right-click the Assistant icon in the taskbar.
  2. Select **Reload Widgets**

## UiPath.config

The `UiPath.config` file contains essential configuration parameters for the Robot. As an admin, you can customize the behavior of your robots by editing the list of parameters in the config file.

:::note
Each environment might need specific notices, so UiPath allows you to apply different configurations based on the current environment of the robot, whether it's Development, Staging, or Production. Always be careful when editing this file, as inaccurate configuration may cause application issues.
:::

### Accessing the file

When you install your Robot, the system creates the `UiPath.config` file.

To access it, navigate to `C:\Program Files\UiPath\Studio\UiPath.config`.

### Customizable settings

The `UiPath.config` file consist of the following parameters:

* In the `connectionSettings` config section
  + `DefaultServiceUrl` (string) - Sets the default address the Robot uses to connect to Orchestrator. Example:
    ```
    string DefaultServiceUrl = "https://cloud.uipath.com"
    ```
  + `AutoSignIn` (bool) - Enables the auto sign-in feature for Assistant. Default value is `false`. Example:
    ```
    bool AutoSignIn = true.
    ```
  + `EnforceDefaultServiceUrl` (bool) - Enforces the address provided as `DefaultServiceUrl` to all users. Default value is `false`. Example:
    ```
    bool EnforceDefaultServiceUrl = true.
    ```
* In the `communicationSettings` config section
  + `MaxMessageSizeInMegabytes` (byte) - Sets the maximum size of a message the system can send or receive, in MB. Default value is `10`.

This is used to prevent overload or process crashes due to handling messages too large. Example:

    ```
    byte MaxMessageSizeInMegabytes = 10;
    ```
  + `InstallPackageTimeout` (TimeSpan) - Sets the time limit for package installations. Default value is 20 minutes.

If a package installation takes longer than the defined time, the system aborts the installation. Example:

    ```
    TimeSpan InstallPackageTimeout = TimeSpan.FromMinutes(20);
    ```
  + `RequestTimeout` (TimeSpan) - Defines how long the system waits for a communication response. Default value is 40 seconds.

If the system does not receive a response in the set period, it stops and moves forward. This prevents system hang-ups. Example:

    ```
    TimeSpan RequestTimeout = TimeSpan.FromSeconds(40);
    ```
* In the `packageSettings` config section
  + `PackagesInstallationFolder` (string) - Sets the default directory where packages are installed. Default value is `C:\UiPath\Packages`.
  + `SkipHttpConfigurationSources` (bool) - Enables the system to ignore package sources configured over HTTP, such as NuGet feeds. Default value is `false`.

This means the system does not retrieve packages from these sources, which is useful when the sources are not reliable or secure.
  + `DisableSecureXaml` (bool) - Allows the Robot to run potentially unsafe workflows. Default value is `false`.
  + `DirectDownload` (bool) - Allows direct download of packages, without prompting the user. Default value is `false`.
  + `PackageSaveWithoutNupkg` (bool) - Allows saving the packages without the `.nupkg` file. Default value is `false`.

This is helpful to reduce the download size.
* In the `analyticsSettings` config section
  + `Telemetry.Enabled` (bool) - Allows UiPath to collect and send usage data for analysis. Default value is `false`.
* In the `robotCacheSettings` config section
  + `SessionCacheDuration` (TimeSpan) - Defines how long the data from a specific session should be retained in the cache before being discarded. Default value is 30 seconds.

This is useful for reusing data such as variable values or details of operations, instead of recreating or refetching it. Example:

    ```
    TimeSpan SessionCacheDuration = TimeSpan.FromSeconds(30);
    ```
  + `GetResourceUrlCacheDuration` (TimeSpan) - Defines how long the URLs for resources, such as APIs or webpages, are stored in cache. Default value is one (1) hour.

This is useful for optimizing performance in scenarios where your robots need to access certain resources regularly. Example:

    ```
    TimeSpan GetResourceUrlCacheDuration = TimeSpan.FromHours(1);
    ```
* In the `robotJsSettings` config section
  + `ListenerPort` (int) - Sets the port number on which the Robot.js listens for incoming connections. Default value is `2323`.

This allows the robot service to interact with web applications running on local or remote servers. Example:

    ```
    int ListenerPort = 2323;
    ```
  + `TokenExpiryInDays` (int) - Sets the validity period, in days, of authentication tokens generated by the robot service. Default value is 30 days.

The robot service uses these tokens to authenticate itself when interacting with other software components or services. Example:

    ```
    int TokenExpiryInDays = 30;
    ```
  + `AllowUrlList` (string) - Sets the list of URLS that the robot service can access. This helps ensure your robot service only interacts with approved services. Example:
    ```
    string AllowUrlList = "https://cloud.uipath.com";
    ```

:::important
* Always create a backup of the original `UiPath.config` file before making any changes. This can help restore the original settings if something goes wrong.
* To apply the updates made to the `UiPath.config` file, restart the UiPath service or the system.
* Local settings in the `UiPath.config` file take precedence over settings configured in Orchestrator.
* Sensitive data in `UiPath.config` file can be encrypted for additional security.
:::

## UiPath Robot system variables

Further custom behavior can be configured through system environment variables.

:::important
After modifying any of the system variables, restart the Robot Service.
:::

The following list summarizes the most common use cases:

* `UIPATH_SESSION_TIMEOUT` - Changes the default 60-second timeout for creating an interactive session. Adjust this value to adapt the Robot behavior based on the performance and load times of the system it interacts with.

Example:

  ```
  UIPATH_SESSION_TIMEOUT=75
  ```
* `UIPATH_PIP_SESSION_TIMEOUT` - Changes the default 180-second timeout for starting a process in a Robot session.

Example:

  ```
  UIPATH_PIP_SESSION_TIMEOUT=60
  ```
* `UIPATH_LANGUAGE` - Sets the language the Robot operates in. The order of precedence is:
  1. `UIPATH_LANGUAGE` value
  2. Machine environment variable
  3. Current thread UI culture
  4. Default UiPath language (English)Example:
  ```
  UIPATH_LANGUAGE=French
  ```
* `UIPATH_HEADLESS_WITH_USER` - Uses the credentials of a specific user, which was previously configured in Orchestrator.

Example:

  ```
  UIPATH_HEADLESS_WITH_USER=True
  ```
* `UIPATH_PRE_LOADED_EXECUTOR` - By default, a preloaded executor is launched when the Robot starts. To change this behavior and launch the preloaded executor only when the first process runs, set this variable to `None`.

Example:

  ```
  UIPATH_PRE_LOADED_EXECUTOR=None
  ```
* `UIPATH_DISABLE_PRE_LOADED_EXECUTOR` - Disables the preloaded executor feature.

Example:

  ```
  UIPATH_PRE_LOADED_EXECUTOR=None
  ```
* `UIPATH_ROBOTJS_ALLOWLIST` - Automatically accepts the robot consent dialog, when establishing the connection between the Robot JS SDK and the Robot Executor.

The variable accepts custom application URLs, separated by semicolons. Include the port number in the URL if it differs from the standard ports (80 or 443). Example:

  ```
  UIPATH_ROBOTJS_ALLOWLIST=cloud.uipath.com;mydomain.com;
  ```
* `UIPATH_DNS_MACHINENAME` - Allows using the DNS host name for Localhost when creating RDP sessions. To execute unattended jobs in environments with Kerberos authentication for RDP, set this value to True.

Example:

  ```
  UIPATH_DNS_MACHINENAME=True
  ```
* `NUGET_FALLBACK_PACKAGES` - Configures the paths to fallback packages folders. Use semicolons to separate multiple paths.

In the absence of this variable, the Robot searches for fallback packages folders in the `Nuget.config` file.
* `NUGET_SCRATCH` - Allows multiple User Mode robots on the same machine to share a local path for storing packages.

The value must be a path different to the Nuget installation folder, and it acts as a temporary folder for NuGet.
  :::note
  Only the `NUGET_SCRATCH` variable should use the configured temporary folder.
  :::
Example:

  ```
  NUGET_SCRATCH=C:\NuGetTempFolder
  ```
* `UIPATH_PRESERVE_CREDENTIALS_CASE` - Preserves the original casing of logging credentials (domain\username).

Example:

  ```
  UIPATH_PRESERVE_CREDENTIALS_CASE = True
  ```
* `UIPATH_SESSION_BEHAVIOR` - Configures the way the session restore behaves after a job completes. The following options are available:
  + `TryReuseAndRestoreSession`—Default option. Attempts to reuse the session and restore it to its previous state after a job completes. If there is no initial session to reuse, it logs off on restore.
  + `ForceNew`—Creates a completely new session, regardless of the previous session state. Always logs off on restore.
  + `LeaveSessionActive`—Prevents restoration of the initial session state.
  + `LeaveSessionDisconnected`—Always disconnects the session on restore.Example:
  ```
  UIPATH_SESSION_BEHAVIOR = LeaveSessionDisconnected
  ```
* `UIPATH_HTTP_CONNECTION_LIFETIME` - Defines how long the connection to Orchestrator remains open before it is closed and refreshed. Default duration is 30 minutes, but to adjust this value, use value in seconds.

Example:

  ```
  // to set 10 minutes                          
  UIPATH_HTTP_CONNECTION_LIFETIME = 600
  ```
* `UIPATH_FILE_LOG_LEVEL` - Defines the Execution log level used in the local file. This is different than the log level used for Orchestrator. The following options are available:
  + Verbose
  + Trace
  + Information
  + Warning
  + Error
  + Critical
  + OffExample:
  ```
  // to set verbose level locally
  UIPATH_FILE_LOG_LEVEL = Verbose
  ```
* `UIPATH_EXECUTOR_STARTUP_DELAY` - Defines the time in seconds to wait between session creation and Executor startup. This is used when your infrastructure needs to load some services (VPN, security) before the execution of your automation starts.

Example:

  ```
  // to set the delay to 5 seconds
  UIPATH_EXECUTOR_STARTUP_DELAY = 5
  ```