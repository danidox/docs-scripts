---
title: "Settings fields"
visible: true
slug: "settings-fields"
---

The **Settings** property of the Robot JavaScript SDK allows you to personalize and improve your control over the setup of the browser add-on.

```
class Settings {
  portNumber: number;
  pollTimeInterval: number;
  disableTelemetry: boolean;
  appOrigin: string;
}
```

| Attribute | Description |
| --- | --- |
| `portNumber` | Allows you to configure custom ports on which the back-end services run on. The default port number is **2323**. Please note that this is only available for Enterprise installations. |
| `pollTimeInterval` | Allows you to specify the time in milliseconds in which the Robot JavaScript SDK keeps track of a process execution from a web page. The default value is 250 milliseconds. This value determines the polling frequency from the web browser |
| `disableTelemetry` | Allows you to disable the telemetry flag. The default value is `false`. |
| `appOrigin` | Allows you to specify the application which uses the SDK. The default value is picked up from the `window.location.origin` class. |

```
const robot = UiPathRobot.init();
robot.settings.portNumber = 1234;
robot.settings.pollTimeInterval = 1000; 
robot.settings.disableTelemetry = true; 
robot.settings.appOrigin = 'MyApp';
```

## Add-on Settings

In order to change add-on settings, you need to change the `uipath.config` file from the `%ProgramFiles%\UiPath\Studio` folder.

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

## Default Overlay

It is possible to customize the consent screen displayed when a request is raised from a new domain. There are currently two screens that are delivered with the Robot JavaScript SDK:

#### Consent Prompt

The `consent-prompt` overlay is displayed when a request to access the UiPath Assistant is raised from a new domain.

![docs image](/images/robot/robot-docs-image-103463.webp)

#### Missing Components

The `missing-components` overlay is displayed when the required add-on is not present on the local machine.

![docs image](/images/robot/robot-docs-image-103674.webp)

Overlay messages can be configured as exemplified below.

```
// Consent code will be written to the console instead of showing default overlay
// Error logged to console when required components are missing insread of showing
// default error overlay
const robot = UiPathRobot.init();
robot.on('consent-prompt', function(consentCode){ console.log(consentCode) });
robot.on('missing-components', function(){ console.log('Missing components') });
```

## SDK Settings

The **Settings** property of the Robot JavaScript SDK allows you to personalize and improve your control over the setup of the browser add-on.

```
class Settings {
  portNumber: number;
  pollTimeInterval: number;
  disableTelemetry: boolean;
  appOrigin: string;
}
```

| Attribute | Description |
| --- | --- |
| `portNumber` | Allows you to configure custom ports on which the back-end services run on. The default port number is **2323**. Please note that this is only available for Enterprise installations. |
| `pollTimeInterval` | Allows you to specify the time in milliseconds in which the Robot JavaScript SDK keeps track of a process execution from a web page. The default value is 250 milliseconds. This value determines the polling frequency from the web browser |
| `disableTelemetry` | Allows you to disable the telemetry flag. The default value is `false`. |
| `appOrigin` | Allows you to specify the application which uses the SDK. The default value is picked up from the `window.location.origin` class. |

```
const robot = UiPathRobot.init();
robot.settings.portNumber = 1234;
robot.settings.pollTimeInterval = 1000; 
robot.settings.disableTelemetry = true; 
robot.settings.appOrigin = 'MyApp';
```