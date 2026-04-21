---
title: "Data Flow Between UiPath Apps and Orchestrator"
visible: true
slug: "data-flow-between-uipath-apps-and-orchestrator"
---

While UiPath Apps is a cloud hosted experience, it can be used with automation in an on-premise or self-hosted Orchestrator. The following is a summary of the data that is transferred when a client browser open a UiPath App and runs automation:

* On navigation to the app, the App definition is retrieved from the UiPath Apps web service. This definition has no data, only the metadata used to render the application in the browser.
* When the start process rule (attended) is executed by an app, the browser contacts the local attended robot and passes input arguments. This is used to execute an automation locally on the client machine where the app is running. When the automation completes, the local robot returns the output arguments from the automation to the app in the browser. The only data that is exposed by the robot are the output arguments and any logging messages coded into the automation; no other data, screenshots, etc. seen by the automation leaves the box.
* When the start process rule (unattended) is executed by an app, the browser contacts Orchestrator via the Apps service and passes input arguments. This is used to execute an automation on an available unattended robot. When the automation completes, Orchestrator sends the output arguments from the automation to the Apps service, which routes them to the app in the browser. The only data that is exposed by the robot are the output arguments and any logging messages coded into the automation; no other data, screenshots, etc. seen by the automation leaves the box.

In both the attended and unattended cases, the only data that is sent to and stored by Orchestrator are:

1. The inputs + outputs of all processes that are run
2. Logging messages added by the RPA developer to the process (this is opt-in)

In all cases, communication between Orchestrator and Apps service is encrypted end-to-end. Input and output arguments are never stored in the Apps service.

## Cloud data flow diagram

## Unattended

The graphic below describes the **UiPath Apps** data flow for cloud, using unattended robots.

   ![docs image](/images/apps/apps-docs-image-91972-56244b6a.webp)

1. The user navigates to an app using a browser on the client machine.
2. The browser calls the **UiPath Apps** service in the cloud to retrieve the **Apps** definition (metadata).
3. The **Apps** definition is sent to the browser where the **Apps** runtime renders the app.
4. The app calls the cloud-hosted **UiPath Orchestrator** to run an unattended process, via the apps service.
5. **Orchestrator** reaches out to an Unattended Robot to execute the process.
6. The process output is returned to **Orchestrator**.
7. The client app is notified of the process results.
   :::note
   Only the process inputs and outputs are returned to **Orchestrator**. The app automated by RPA, and all its data, remains on the robot machine.
   :::

## Attended

The graphic below describes the **UiPath Apps** data flow for cloud, using attended robots.

   ![docs image](/images/apps/apps-docs-image-92224-d8b5b016.webp)

1. The user navigates to an app using a browser on the client machine.
2. The browser calls the **UiPath Apps** service in the cloud to retrieve the **Apps** definition (metadata).
3. The **Apps** definition is sent to the browser where the **Apps** runtime renders the app.
4. The app calls the local robot service on the client machine to execute a process. The results are returned locally.
5. Audit trail is logged to **Orchestrator**, including process output.
   :::note
   Only the process inputs and outputs are returned to **Orchestrator**. The app automated by RPA, and all its data, remains on the robot machine.
   :::

## Hybrid data flow diagram

The sections below describes the **UiPath Apps** data flow when using cloud apps with an [on-prem](https://docs.uipath.com/apps/automation-suite/latest/user-guide/onprem#connecting-apps-to-an-on-premises-orchestrator-instance) (or self hosted) **Orchestrator**.

## Unattended

The graphic below describes the **UiPath Apps** data flow for hybrid, using unattended robots.

   ![docs image](/images/apps/apps-docs-image-92864-598b7315.webp)

1. The user navigates to an app using a browser on the client machine.
2. The browser calls the **UiPath Apps** service in the cloud to retrieve the **Apps** definition (metadata).
3. The **Apps** definition is sent to the browser where the **Apps** runtime renders the app.
4. The app calls your self-hosted **UiPath Orchestrator** on-premises to run an unattended process, via the apps service.
5. **Orchestrator** reaches out to an Unattended Robot to execute the process.
6. The process output is returned to **Orchestrator**.
7. The client app is notified of the process results.
   :::note
   Only the process inputs and outputs are returned to **Orchestrator**. The app automated by RPA, and all its data, remains on the robot machine.
   :::

## Attended

The graphic below describes the **UiPath Apps** data flow for hybrid, using attended robots.

   ![docs image](/images/apps/apps-docs-image-92756-adb6fcc6.webp)

1. The user navigates to an app using a browser on the client machine.
2. The browser calls the **UiPath Apps** service in the cloud to retrieve the **Apps** definition (metadata).
3. The **Apps** definition is sent to the browser where the **Apps** runtime renders the app.
4. The app calls the local robot service on the client machine to execute a process. The results are returned locally.
5. Audit trail is logged to **Orchestrator**, including process output.
   :::note
   Only the process inputs and outputs are returned to **Orchestrator**. The app automated by RPA, and all its data, remains on the robot machine.
   :::