---
title: "UiPath Assistant on Mac"
visible: true
slug: "uipath-assistant-on-mac"
---

The UiPath Assistant is available on MacOS and allows users to access, manage, or run cross-platform automations, and connect the Robot to Orchestrator.
:::note
The UiPath Assistant is compatible with MacOS version 10.15 (Catalina) and newer.
:::

## Download

The UiPath Assistant can be downloaded from the Customer Portal or from the Automation Cloud.

### Download from the Customer Portal

1. Go to the [Customer Portal website](https://customerportal.uipath.com/product-downloads).
2. Search for your product and click the collapse icon on the right.
3. Download the DMG file, based on your platform, the following options are available:
   * Download for Intel Macs - x64
   * Download for Apple Silicon

### Download from the Automation Cloud

1. Go to the Automation Cloud website.
2. Click the Help icon ![docs image](/images/assistant/assistant-docs-image-250695-25eb4d71.webp)on top of the page, and select Downloads from the dropdown menu.

   ![docs image](/images/assistant/assistant-docs-image-395683-802d075e.webp)
3. In the **Featured Download** section, choose one of the following options based on your platform:
   * Download for Intel Macs - x64
   * Download for Apple Silicon

## Installation

To install the UiPath Assistant for MacOS, follow the steps below:

1. Double-click the DMG file to make its content available.
2. Drag the application from the DMG window into the Applications directory to install it.
3. Wait for the copy process to finish.

## Connecting to Orchestrator

To connect the Robot and UiPath Assistant to Orchestrator, use one of the following options:

* [Interactive Sign-in](https://docs.uipath.com/robot/standalone/2025.10/user-guide/setting-up-interactive-sign-in)
* [Machine Key](https://docs.uipath.com/orchestrator/standalone/2025.10/user-guide/connecting-robots-to-orchestrator)
* [Client Credentials](https://docs.uipath.com/orchestrator/standalone/2025.10/user-guide/robot-authentication-with-client-credentials)
:::note
When using the UiPath Assistant and Robot on MacOS, local feeds are not supported. Automations are retrieved from Orchestrator and only the cross-platform ones are available. The same applies for the [Marketplace Widget](https://docs.uipath.com/assistant/standalone/2025.10/user-guide/marketplace-widget) when used in the Assistant on MacOS.
:::

### UiPath Extensions

When run on MacOS, processes that use web automations in browsers require Google Chrome Extension or Safari Extension to work.

When the Assistant is launched for the first time, if the Chrome extension is not detected, a prompt is displayed on the Assistant home page to install it.

You can add the extensions from the **UiPath extensions** section of the **Preferences** menu in the Assistant.

Once the installation is complete, the browser must be restarted and the extension enabled manually.

### Testing Processes on MacOS

When designing a process for MacOS in Studio, the testing is done using [Remote Debugging](https://docs.uipath.com/studio/standalone/2025.10/user-guide/remote-debugging) and connecting to the specific MacOS machine.

### Logging

UiPath Assistant logs are found in the `combined.logs` file from the `/Users/john.doe/Library/Application Support/UiPath/` folder.

These logs contain all actions done by the user in the Assistant and any errors. Other specific Assistant files can be found in that folder as well.

### Known Issues and Limitations

When using the Assistant on MacOS, the following features are not available:

* [Picture In Picture](https://docs.uipath.com/assistant/standalone/2025.10/user-guide/picture-in-picture).
* Sending Processes to desktop.
* [Task Capture Launcher](https://docs.uipath.com/assistant/standalone/2025.10/user-guide/task-capture-launcher).
* RobotJS is not compatible with Safari browser.
* The UiPath Diagnostic Tool is not available on MacOS machines. Instead, in Assistant, in the **Troubleshoot** section, certain log files are collected manually, which results in an archive used for debugging.

## Updating the Orchestrator Connection

You can update the default Orchestrator service URL for Mac from the `store.json` (`/Applications/UiPath Assistant.app/Contents/Robot/uipath.config~/Library/Application Support/UiPath/store.json`):

```
"MAIN_WINDOW_SERVICE_LOGIN_DETAILS": {
        "nextServiceUrl": "https://cloud.uipath.com",
        "defaultServiceUrl": "https://cloud.uipath.com"
    }
```

## Opting Out of Telemetry

To disable the Telemetry in UiPath Assistant for Mac, add this in `uipath.config` file (you can find it in `/Applications/UiPath Assistant.app/Contents/Robot`):

```
<add key="Telemetry.Enabled" value="false"/>
```
:::important
Opting out of telemetry also disables Sentry.
:::