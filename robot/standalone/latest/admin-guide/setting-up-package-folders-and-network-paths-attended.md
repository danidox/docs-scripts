---
title: "Setting up package folders and network
            paths"
visible: true
slug: "setting-up-package-folders-and-network-paths-attended"
---

:::important
**Restart required!** Any update made to the config file requires a restart:
* For Service Mode robots: restart the Robot service.
* For User Mode robots: restart the user service, either by restarting the device or logging out of your user account and logging
back in.
:::

## Setting up a fallback package folder

To set up a fallback package folder using system enviroment variables:

1. Add the `NUGET_FALLBACK_PACKAGES` variable to your [system environment variables](https://docs.uipath.com/robot/standalone/latest/admin-guide/configuration-files#uipath-robot-system-variables).
2. For the variable, add the list of the absolute paths for the folder, separated by semicolons.
   :::important
   * If the environment variable does not exist, the robot tries to read the NuGet packages fallback folders from the `Nuget.config` file.
   * Processes deployed in fallback folders are not supported, only dependencies.
   :::

## Changing the download path for packages

The default download path for packages is `%userProfile%\.nuget\packages`.

To change the package download location, you can either edit the `UiPath.config` file, or use the `PACKAGES_FOLDER="new/download/path"` [parameter via the command line](https://docs.uipath.com/robot/standalone/latest/admin-guide/windows-installations) when installing Studio or Robot.

To edit the `UiPath.config` file, follow these steps:

1. Open the configuration file. You can find it in the `C:\Program Files\UiPath\Studio` folder.
2. In the `<packageSettings>` section, add a new entry called `packagesInstallationFolder`. Then, set its value as the path of the new download folder.
3. Save the changes and restart the Robot service or the device.
   :::note
   When changing the download folder, make sure that all users that need to run automations can access it.
   :::

For example:

```
<packageSettings>
  <add key="packagesInstallationFolder" value="C:\Nuget" />
</packageSettings>
```

## Setting up local and network paths

You can set a local or network path to enable several robots to use the same path. The setup depends on the robot operational mode: Service Mode or User Mode.

On Windows Server machines that allow concurrent executions on High-Density Robots, you need to set up unique paths for each user. This is due to the way mappings are resolved per user. Since the computer account owns the installed files, it does not have access to user-specific network mappings.

Using the same shared folder for all users in High-Density environments is supported with the following limitations: