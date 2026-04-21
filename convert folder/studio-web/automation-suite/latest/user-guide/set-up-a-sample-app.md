---
title: "Set up a sample app"
visible: true
slug: "set-up-a-sample-app"
---

You can use the template and preconfigured assets that are available for download to build and test a sample app. In addition to the CX Companion template, this **[archive with assets for CX Companion](https://github.com/UiPath/AppsClientSample/blob/master/demo-apps/templates/CXCompanion.zip)** contains an `Automations` folder with mock automations that you can import in Studio Web and publish to Orchestrator.

To set up and test a sample app, follow the steps below. For details on how to configure the app, see [Configuring the CX Companion app](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/configuring-the-cx-companion-app).

1. Create an app from the CX Companion template.
2. Configure the data input mode. either external events or query parameters. We recommend external events when embedding the app in a host system and query parameters when deploying a standalone app. For details, see [Configuring the CX Companion app](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/configuring-the-cx-companion-app) &gt; *Configure the data input mode*.
3. `(Optional)` If you don't want to use the default 360 process included in the template, set up the CX Companion app to use a different 360 process. For details, see [Configuring the CX Companion app](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/configuring-the-cx-companion-app) &gt; *Configure a 360 process*.
4. Create individual projects from a few of the downloaded mock automations by importing them to Studio Web and publishing the automations to Orchestrator. CX Companion is configured to load actions from Orchestrator folders that use the same structure as the downloaded folder, so make sure to place the automations in an identical Orchestrator folder structure. For example:
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/606215)
5. Configure the folder for actions in the CX Companion app. For details, see [Configuring the CX Companion app](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/configuring-the-cx-companion-app) &gt; *Configure the folder for actions*.
6. Try to debug the app with the following query parameter:
   ```
   &requestType=Case&requestId=500gK000003MTaQQAW&requestCaseNumber=00001000
   ```

For this step, query parameters mode must be enabled in the app (external events can only be tested after deploying the app). The app should load and you should be able to see all deployed actions.
7. Try running the actions and view the results in Automation Tracker. For this step, make sure unattended or serverless machines are configured in the folder where actions are deployed.
8. [Publish and deploy](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/publishing-deploying-upgrading-app-projects) the app to Orchestrator (you can use the same folder or a different one). You can use the app URL to embed it in your host environment, depending on the data input mode. If you want to use external events, query parameters mode must be disabled by setting the variable `ConfigEnableQueryParamMode` to `False`.
9. When embedding the app in iframes of the host application, include `embed_` in the URL to allow logging in through a pop-up. For information about getting the app URL, see [Configuring the CX Companion app](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/configuring-the-cx-companion-app) &gt; *Embedding the app*
10. To test the app:
    * For external events mode, include the query parameter `target` and set the domain name as the value, e.g. `&target=https://www.example.com`.

This is a sample deployed app URL to use in an iframe:

`https://cloud.uipath.com/embed_/appsdev/apps_/default/run/production/22986e36-8b04-4593-b82f-aae4c14bb2dc/bd8c8ef5-a94a-43f5-9a5b-6df73d8f7aa6/IDc0b72c47295b49abaea6b701cfa5b730?el=VB&uts=true&target=https://www.example.com`

The event name configured in the sample App is `INITIATE_REQUEST`. Send an event from the host with this name and one of the following payloads to test the sample app: Sample payload 1: (Type: Case)

      ```
      {
          "RecordURL": "https://orgfarm-ef12b89682-dev-ed.develop.my.salesforce.com/lightning/r/Case/500gK000003MTaQQAW/view",
          "Type": "Case",
          "Id": "500gK000003MTaQQAW",
          "CaseNumber": "00001000",
          "Subject": "Starting generator after electrical failure",
          "Status": "Closed",
          "AccountId": "001gK0000048VSXQA2",
          "Origin": "Phone",
          "Priority": "High",
          "OwnerId": "005gK000001reLJQAY",
          "IncludeCaseHistory": true
      }
      ```

Sample payload 2: (Type: Account)

      ```
      {
          "RecordURL": "https://orgfarm-ef12b89682-dev-ed.develop.my.salesforce.com/lightning/r/Account/001gK0000048VSXQA2/view",
          "Type": "Account",
          "Id": "001gK0000048VSXQA2",
          "AccountNumber": "CD451796",
          "Name": "Edge Communications",
          "Website": "http://edgecomm.com",
          "Phone": "(512) 757-6000",
          "Industry": "Electronics",
          "BillingCountry": "United States",
          "BillingState": "TX",
          "BillingCity": "Austin",
          "BillingStreet": "312 Constitution Place\nAustin, TX 78767\nUSA",
          "OwnerId": "005gK000001reLJQAY",
          "RenewalDate": "2025-08-31",
          "thresholdDays": 5,
          "priorityCasesOnly": true
          }
      ```
      :::note
      You can test external events using the following playground:&lt;https://uipath.github.io/apps-demo-pages/app-cx-companion/&gt;.
      :::
    * For query parameters mode, Id and Type are required values. Pass the Id value in the `requestId` parameter and the Type in the `requestType` parameter. Additional parameters can be passed if needed. This is an example URL:
      ```
      https://cloud.uipath.com/embed_/appsdev/apps_/default/run/production/22986e36-8b04-4593-b82f-aae4c14bb2dc/bd8c8ef5-a94a-43f5-9a5b-6df73d8f7aa6/IDc0b72c47295b49abaea6b701cfa5b730?el=VB&uts=true&requestType=Case&requestId=500gK000003MTaQQAW&requestCaseNumber=00001000
      ```