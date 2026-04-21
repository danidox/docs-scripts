---
title: "Set an external context using external events"
visible: true
slug: "set-an-external-context-using-external-events"
---

External events are custom cross-window communication messages that enable secure data exchange between parent windows and apps embedded in child windows (iframes). At runtime, this enables apps to listen for configured external events and execute the associated automations.

External events bring:

* **Event-driven architecture** - Trigger specific actions based on custom event types.
* **Secure messaging** - Ensure communication only occurs between trusted origins.
* **Real-time data exchange** - Enable dynamic interactions between the host application and embedded UiPath Apps.

## Prerequisites

The external events functionality relies on the **UiPath Communication Driver**, a lightweight and secure communication library for cross-window messaging.

The UiPath Communication Driver must be installed in the host platform. Go to the [npm package page](https://www.npmjs.com/package/@uipath/apps-communication-driver) to download the driver and read detailed documentation on how to install and use it.

## Enabling external events

1. Open an app.
2. Right-click **App** in the project explorer and select **Properties**.
3. Expand the **External events** section and select **Enable**.
4. In the **Allowed origins** field, enter the domain of the host application. You can add multiple entries by adding a comma-separated list of URLs. Allowed origins are critical for the security of external events. Defining allowed origins enables:
   * **Validation of message sources** - Only processes messages from specified origins.
   * **Targeted message delivery** - Ensures responses go to intended recipients.
   * **Prevention of CSRF attacks** - Blocks unauthorised cross-site requests.
   * **Maintaining data integrity** - Ensures trusted communication channels.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/592179)

## Creating an external event

1. Open an app and select a page in the project explorer.
2. Navigate to the **Events** tab in the **Properties** panel.
3. Select **Create external event**.
4. Enter a meaningful name for the external event.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/593149)
5. Select **Define workflow file** to configure the workflow file to be executed for the defined event. The data received in the external event is available in the workflow argument named **ExternalEventData**.