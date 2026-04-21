---
title: "Command prompt examples for attended automations"
visible: true
slug: "uipathrobotmsi-command-prompt-examples-attended"
---

Consider the following examples for your use cases.

:::important
Make sure to run the command in the folder where the installer is located.
:::

## Using UiPathRobot.msi

* Installing the Robot in User Mode for the current user
  ```
  UiPathRobot.msi MSIINSTALLPERUSER=1 ADDLOCAL=DesktopFeature,Robot
  ```
* (Silent mode) Installing the Robot in User Mode
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,StartupLauncher,JavaBridge /Q
  ```
* (Silent mode) Installing the Robot in User Mode and the Chrome Extension using an online policy
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,ChromeExtension CHROME_INSTALL_TYPE=POLICYONLINE /Q
  ```
* (Silent mode) Installing the Robot in User Mode and connect it to Orchestrator
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot CONNECTIONSTRING=https://demo.uipath.com/api/robotsservice/GetConnectionData?tenantId=1 /Q
  ```
* (Silent mode) Installing the Robot in User Mode, and add two custom activity feeds
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot CUSTOM_NUGET_FEEDS="Feed Name1,https://my.custom.nuget.feed; FeedName2,D:\RPA\Activities\Packages\" /Q
  ```
* (Silent mode) Installing and licensing the Robot in User Mode, and the local activity feed
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,CODE=1234567890 /Q
  ```
* Installing the Robot in User Mode, and disabling the official online feeds
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot NUGET_OPTIONS=DisableOnlineFeeds
  ```
* (Silent mode) Uninstalling the Chrome Extension
  ```
  UiPathRobot.msi REMOVE=ChromeExtension /Q
  ```
* Setting up the auto-update connection
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot SERVICE_URL="https://demo.uipath.com/myorg/mytenant"
  ```

## Using UiPathStudio.msi

* Installing Studio and the Robot in User Mode for the current user
  ```
  UiPathStudio.msi MSIINSTALLPERUSER=1 ADDLOCAL=DesktopFeature,Studio,Robot
  ```
* Installing Studio, the Robot in User Mode, and the activity packages
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,Packages
  ```
* Installing the Robot in User Mode, and disable the official online feeds
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot NUGET_OPTIONS=DisableOnlineFeeds
  ```
* (Silent mode) Installing the Desktop suite
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,Packages,StartupLauncher,JavaBridge /Q
  ```
* (Silent mode) Installing the Desktop suite and the Chrome Extension using an online policy
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,Packages,ChromeExtension CHROME_INSTALL_TYPE=POLICYONLINE /Q
  ```
* (Silent mode) Installing Studio, the Robot in User Mode, and the activities packages, in a custom "D:\UiPath" folder
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,Packages APPLICATIONFOLDER=D:\UiPath /Q
  ```
* (Silent mode) Installing Studio, the Robot in User Mode, and add two custom activity feeds
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot CUSTOM_NUGET_FEEDS="Feed Name1,https://my.custom.nuget.feed; FeedName2,D:\RPA\Activities\Packages\" /Q
  ```
* (Silent mode) Installing the Robot in User Mode and connect it to Orchestrator
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot CONNECTIONSTRING=https://demo.uipath.com/api/robotsservice/GetConnectionData?tenantId=1 /Q
  ```
* (Silent mode) Installing and licensing Studio, the Robot in User Mode, and the local activity feed
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,Packages CODE=1234567890 /Q
  ```
* (Silent mode) Uninstalling the Chrome Extension
  ```
  UiPathStudio.msi REMOVE=ChromeExtension /Q
  ```
* Setting up the auto-update connection
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot SERVICE_URL="https://demo.uipath.com/myorg/mytenant"
  ```