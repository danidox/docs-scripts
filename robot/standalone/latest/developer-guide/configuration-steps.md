---
title: "Configuration Steps"
visible: true
slug: "configuration-steps"
---

## Prerequisites

In order for your automation projects to benefit from the Robot JavaScript SDK, the following prerequisites need to be met:

* Studio and Robot version 2021.10 or greater installed
* The UiPath JavaScript Add-On installed on the Robot machine

## Allowing access

When the UiPath Robot JavaScript Add-On is run, you need to provide access to your custom application or web page to connect to the Robot.

The access is handled by a two-step dialog. Both steps have to be confirmed in order to run RobotJS. They can be automated as described below.

## Browser access dialog

This step refers to the browser requesting permissions to open the UiPath Assistant.

## Automatically accepting the Browser access dialog

It can be automated by adding the `uipath-web://*` value as a trusted (allowed) URL in the browser's settings. The `uipath-web://*` refers to the UiPath Robot web protocol handler.

:::note
Based on the browser used, different settings need to be configured. For example, if you are using Google Chrome, follow the steps described in the [Google Chrome URLAllowlist](https://chromeenterprise.google/policies/#URLAllowlist) documentation.
:::
  ![docs image](/images/robot/robot-docs-image-103475.webp)

## Robot consent dialog

The robot consent dialog is used to allow the connection between the Robot JavaScript SDK and the Robot Executor.
  ![docs image](/images/robot/robot-docs-image-102156.webp)

## Automatically accepting the robot consent dialog

This can be automatically allowed by adding the `UIPATH_ROBOTJS_ALLOWLIST` System Environment Variable.

The values used in the variable need to be the URLs of your custom application or web page, separated by semicolon. The URL should contain the port number only if a standard port is not used (`80` or `443`).

## The Robot JavaScript SDK

This SDK provides all the necessary methods and properties you can include in your custom application or web page. You can download it as follows:

## NPM

The [npm package](https://www.npmjs.com/package/@uipath/robot) is available with TypeScript bindings. To include it in your project, you need to execute the following command at the root of your project directory:

```
npm install --save @uipath/robot
```

## CDN

For CDN, you need to include the SDK before closing the `</body>` tag.

```
<body>
...
...
<script href="//download.uipath.com/js/1.3.2/UiPathRobot.js"></script>
</body>
```

## Direct download

You can also grab the Robot JavaScript SDK via [direct download](https://download.uipath.com/js/1.3.1/UiPathRobot.js).

## Add-on settings

In order to change add-on settings, you need to add the `ListenerPort` and `TokenExpiryInDays` parameters in the `uipath.config` file from the installation folder. By default, the section does not contain any keys.

The configuration file needs to contain the following:

```
<robotJsSettings>
    <add key="ListenerPort" value="2323" />
    <add key="TokenExpiryInDays" value="30" />
</robotJsSettings>
```

| Attribute | Description |
| --- | --- |
| `ListenerPort` | The `UiPath.RobotJS.ServiceHost.exe` starts a **HttpListener** on the configured port and contains the information about other local listeners from the active user session on that system. Please note that the port value here needs to match the one configured in the **SDK Settings**. |
| `TokenExpiryInDays` | Any request coming from a new domain needs to have consent from the user to allow access of UiPath Robots from a web application. These consents are valid for the said number of days mentioned in this setting. |