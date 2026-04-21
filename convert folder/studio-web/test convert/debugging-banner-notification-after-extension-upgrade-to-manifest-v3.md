---
title: "Debugging banner notification after
            extension upgrade to Manifest V3"
visible: true
slug: "debugging-banner-notification-after-extension-upgrade-to-manifest-v3"
---

After the upgrade of the Studio Web browser extension to version 24.10 (Manifest V3 compatible), the debugging banner containing the message *"UiPath Studio Web Automation" started debugging this browser* is displayed at design time every time you start an interactive selection.

![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/422815)

The debugger banner appears because the [chrome.debugger](https://developer.chrome.com/docs/extensions/reference/api/debugger) API is used to load the UI Automation selection screen code in the target tab.

This banner is a security feature designed by Chrome to inform you when a debugger is active. You can safely close the banner by clicking the **Cancel** button. This action does not affect the functionality of the extension.

Even if dismissed, the debugging banner reappears every time you start an interactive selection via the **Indicate target on screen** or **Edit target** activity options or when selecting a browser tab for the [Use Browser](https://docs.uipath.com/activities/other/latest/ui-automation/n-application-card) activity.

## Workarounds for hiding the debugging banner

#### Install the extension via group policy

When an extension is installed via group policy in Chrome or Edge, it typically does not trigger the debugging banner (*…started debugging this browser*) associated with the use of the `chrome.debugger` API.

This can be done by adding to the [ExtensionInstallForceList](https://chromeenterprise.google/policies/?policy=ExtensionInstallForcelist) group policy the values with the appropriate Extension ID:

* for Chrome: `conkfbpnllelocpogdmbilgmnkabjfmf;https://clients2.google.com/service/update2/crx`
* for Edge: `hmpkmollbbcoopahpbplbdaapacncbbc;https://edge.microsoft.com/extensionwebstorebase/v1/crx`

#### Start the browser with the silent debugger switch

You can also hide the debugging banner by adding this command line switch when starting the browser: `--silent-debugger-extension-api`.

When you start Chrome or Edge with this switch, it silences the debugger warnings that typically appear when an extension uses the `chrome.debugger` API.

Example for Chrome:

`"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --silent-debugger-extension-api`