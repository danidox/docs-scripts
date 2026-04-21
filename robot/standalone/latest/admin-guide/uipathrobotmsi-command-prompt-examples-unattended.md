---
title: "Command prompt examples for unattended automations"
visible: true
slug: "uipathrobotmsi-command-prompt-examples-unattended"
---

Consider the following examples for your use cases.

:::important
Make sure to run the command in the folder where the installer is located.
:::

## Using UiPathRobot.msi

* (Silent mode) Installing the Robot in Service Mode
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,RegisterService,StartupLauncher,JavaBridge /Q
  ```
* Installing the live streaming feature for Robot versions 2024.10+
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,RegisterService,LiveStreaming
  ```
* (Silent mode) Installing the Robot in Service Mode and the Chrome Extension using an online policy
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,RegisterService,ChromeExtension CHROME_INSTALL_TYPE=POLICYONLINE /Q
  ```
* (Silent mode) Installing the Robot in Service Mode and connect it to Orchestrator
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,RegisterService CONNECTIONSTRING=https://demo.uipath.com/api/robotsservice/GetConnectionData?tenantId=1 /Q
  ```
* (Silent mode) Installing the Robot in Service Mode, and add two custom activity feeds
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,RegisterService CUSTOM_NUGET_FEEDS="Feed Name1,https://my.custom.nuget.feed; FeedName2,D:\RPA\Activities\Packages\" /Q
  ```
* (Silent mode) Installing and licensing the Robot in Service Mode, and the local activity feed
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,RegisterService,CODE=1234567890 /Q
  ```
* Installing the Robot in Service Mode, and disabling the official online feeds
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,RegisterService NUGET_OPTIONS=DisableOnlineFeeds
  ```
* (Silent mode) Uninstalling the Chrome Extension
  ```
  UiPathRobot.msi REMOVE=ChromeExtension /Q
  ```
* Setting up the auto-update connection
  ```
  UiPathRobot.msi ADDLOCAL=DesktopFeature,Robot,RegisterService ORCHESTRATOR_URL="https://demo.uipath.com/myorg/mytenant/orchestrator_"
  ```

## Using UiPathStudio.msi

* Installing Studio, the Robot in Service Mode, and the activities packages
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,RegisterService,Packages
  ```
* Installing the Robot in Service Mode, and disable the official online feeds
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot,RegisterService NUGET_OPTIONS=DisableOnlineFeeds
  ```
* Installing the live streaming feature for Robot versions 2024.10+
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot,RegisterService,Packages,LiveStreaming
  ```
* (Silent mode) Installing the Desktop suite
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,RegisterService,Packages,StartupLauncher,JavaBridge /Q
  ```
* (Silent mode) Installing the Desktop suite and the Chrome Extension using an online policy
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,RegisterService,Packages,ChromeExtension CHROME_INSTALL_TYPE=POLICYONLINE /Q
  ```
* (Silent mode) Installing Studio, the Robot in Service Mode, and the activities packages, in a custom "D:\UiPath" folder
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,RegisterService,Packages APPLICATIONFOLDER=D:\UiPath /Q
  ```
* (Silent mode) Installing Studio, the Robot in Service Mode, and add two custom activity feeds
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,RegisterService CUSTOM_NUGET_FEEDS="Feed Name1,https://my.custom.nuget.feed; FeedName2,D:\RPA\Activities\Packages\" /Q
  ```
* (Silent mode) Installing the Robot in Service Mode and connect it to Orchestrator
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot,RegisterService CONNECTIONSTRING=https://demo.uipath.com/api/robotsservice/GetConnectionData?tenantId=1 /Q
  ```
* (Silent mode) Installing and licensing Studio, the Robot in Service Mode, and the local activity feed
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Studio,Robot,RegisterService,Packages CODE=1234567890 /Q
  ```
* (Silent mode) Uninstalling the Chrome Extension
  ```
  UiPathStudio.msi REMOVE=ChromeExtension /Q
  ```
* Setting up the auto-update connection
  ```
  UiPathStudio.msi ADDLOCAL=DesktopFeature,Robot,RegisterService ORCHESTRATOR_URL="https://demo.uipath.com/myorg/mytenant/orchestrator_"
  ```