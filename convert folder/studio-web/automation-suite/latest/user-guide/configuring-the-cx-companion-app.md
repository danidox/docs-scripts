---
title: "Configuring the CX Companion app"
visible: true
slug: "configuring-the-cx-companion-app"
---

The CX Companion can be used as is or customised according to your business needs. This section documents how you can configure CX Companion, using the [sample app](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/set-up-a-sample-app) to exemplify some of the settings.

## Prerequisites

* CX Companion requires a serverless or unattended robot to be set up in the deployed folder.
* We recommend using CX Companion in external events mode, but please note that for ease of use, query parameters mode is enabled by default. See the *Configure the data input mode* section below for more details. When using external events:
  + To integrate with Salesforce, install and configure the [CX Companion SF plugin in Salesforce](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/cx-companion-salesforce-plugin#cx-companion-salesforce-plugin).
  + To integrate with a different host platform, install and configure the [UiPath Communication Driver](https://www.npmjs.com/package/@uipath/apps-communication-driver) in the host application.
* To run actions in attended mode, CX Companion requires UiPath Assistant version 2025.0.167 or later.
* If you want to launch other apps from CX Companion, you must use the [Apps connector](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/about-the-uipath-apps-connector) in Integration Service. Make sure your organization's governance policies are configured to allow the use of this connector:
  + Because this connector is currently available in preview, the option **Enable preview packages and activities** must be selected in the Studio Web governance policy deployed in your organization. This makes the **List Deployed Apps** activity available in workflows. For more information, see [Settings for Studio Web Policies](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-studio-web-policies#activities) in the Automation Ops guide.
  + Make sure the Apps connector in enabled in your Integration Service policy. For more information, see [Settings for Integration Service policies](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/settings-for-integration-service-policies) in the Automation Ops guide.

## Configure the data input mode

The app can use one of the following data input modes:

* **Query parameters** - Use this option if CX Companion will be deployed as standalone. To allow you to quickly test the CX Companion app, this option is enabled by default in the template. The initiate workflow for using query parameters is `MainPage_Load_Initiate_Request_QueryParam.xaml`.
* **External events** - Use this option if you want to embed CX Companion in a host application such as Salesforce. The initiate workflow for using external events is `MainPage_Initiate_Request.xaml`. This is the recommended option, but it is not enabled by default in the template. To use this option:
  + **In the CX Companion app designer** - In the App **Properties** panel, make sure **External events** is enabled and add the domain of your host application in the **Allowed origins** text box. For more information about enabling external events, see [Set an external context using external events](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/set-an-external-context-using-external-events).
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/592091)
  + **In the CX Companion app designer** - Disable query parameters mode by opening the **Data Manager** in the workflow file

`MainPage_Load_Initiate_Request_QueryParam.xaml` and setting the variable `ConfigEnableQueryParamMode` to `False`. The default value is `True`.
  + **In the host application** - For Salesforce, install and configure the [CX Companion SF plugin](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/cx-companion-salesforce-plugin#cx-companion-salesforce-plugin). For all other host applications, install and configure the [UiPath Communication Driver](https://www.npmjs.com/package/@uipath/apps-communication-driver).

## Configure a 360 process (optional)

A mock 360 process is included in the solution and invoked by the app to retrieve customer data from the host application. You can customize this process as needed or create another process, publish it to Orchestrator, and configure the CX Companion to use it by selecting it from the **Invoke Process: Start 360 Process** activity in the initiate workflow and configuring the required arguments as needed.

## Configure the folder for actions

Actions refer to the automations, apps, and agents published to Orchestrator that users can run. CX Companion is configured to have different folders for actions based on the input object type. For example, in the [sample app](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/set-up-a-sample-app) two types are defined, **Case** and **Account**. As long as the folder structure in Orchestrator matches the configuration in the app, when a record of a certain type is loaded in the app, the Actions panel is populated with the actions in the folder defined for that type.

1. Open the **Data Manager** in the initiate workflow for the data input mode.
2. Enter the automations root folder path in the value field of the `ConfigAutomationsRootFolderPath` variable. For example, *CXCompanionAutomations/AllActions* in the sample app.
3. Configure the automation types in the `ConfigAutomationFoldersByType` variable. In this dictionary variable, each key is an object type and its value is the name of the Orchestrator sub-folder that contains the automations for that object type. In the sample app, the variable is configured as follows:

   | Key | Value |
   | --- | --- |
   | Case | Case Automations |
   | Account | Account Automations |

This corresponds to the following folder structure in Orchestrator.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/606215)

In the Actions panel of the app, the actions for the object type are displayed, with a tab representing each sub-folder found in the folder for that type.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/606208)
4. Configure whether or not to include deployed apps in available actions:
   * If you are using query parameters mode and want to also launch deployed apps, configure the [List Deployed Apps](https://docs.uipath.com/activities/other/latest/integration-service/uipath-uipath-apps-List-Deployed-Apps) activity in both `MainPage_Load_Initiate_Request_QueryParam.xaml` and `MainPage_Initiate_Request.xaml` by adding a UiPath Apps connection.
   * If you are using external events mode and want to also deploy apps, configure the **List Deployed Apps** activity in `MainPage_Initiate_Request.xaml` by adding a UiPath Apps connection, and delete or disable the activity **If: Load Apps list if enabled** in `MainPage_Load_Initiate_Request_QueryParam.xaml`.
   * If you don't intend to deploy apps from CX Companion, delete or disable the activity **If: Load Apps list if enabled** in both initiate workflows.
5. After the solution is deployed:
   1. Go to the folder where the app is deployed and edit it.
   2. On the **Package requirements** page, select the connection configuration.
   3. If you want the same connection to be used by all the users, select that connection. If you want to allow app users to create their own connection, select **Configurable by users** in order to prompt the users to create a connection the very first time they load the app.

:::note
You can test the app using [sample mock automations](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/set-up-a-sample-app).
:::

## Running in attended or unattended mode

CX Companion requires a serverless or unattended robot to be set up in the deployed folder.

To run actions in unattended or serverless mode, after you deploy the app, you can use the URL in your host environment with no additional configuration required.

If you need to run some actions in attended mode, you must run the app in attended mode by appending a query parameter to the app URL:

* When using CX Companion within Salesforce, append `attendedMode=enabledWithRobotJSHandler`.
* When using CX Companion within another third party system, append `attendedMode=enabled`.

Make sure the Assistant is running and is connected to the same tenant where the app is deployed. CX Companion requires Assistant version 2025.0.167 or later.

By default, all actions will run only in unattended mode even if the app is running in attended mode, To run actions in attended mode, mark the action as attended or add the label `Attended` to the process deployed to Orchestrator.

## Configure the app to use a single type of object

If you don't want actions to be displayed based on different object types (e.g. case and account), you can configure it to use a single object type:

1. Remove the default value of the `ConfigInputDataObjectTypeKeyName` variable in the initiate workflow.
2. Remove `Type` from the `ConfigRequiredInputProperties` variable in the initiate workflow.
3. Remote `Type` key-value pair from the `ConfigQueryParameterNameMap` variable in the initiate workflow.
4. Set the root folder name in the `ConfigAutomationsRootFolder` variable in the initiate workflow.
5. If the root folder is at the top level, you can remove the value in the `ConfigAutomationsRootFolderPath`. If it is at a nested level, set the root folder path in this variable.
6. Customise the 360 panel as needed. For details, see *Data shown in the 360 panel* in the **Additional customizations** section below. The Switch case blocks can be removed and you can keep the set of Assign value activities. In addition, if applicable, update the hidden property of the 360 panel container to be based only on `show360Spinner` and not on type.

## Action inputs

The input form is dynamically created based on input arguments. The form currently supports only the following primitive types: **Text**, **Number**, **Boolean**, **DateOnly**. If any other type argument is passed, a text box will be displayed. For date-based inputs, instead of using DateTime, use DateOnly to get a date picker control.

## Action outputs

All action output arguments are shown in Automation Tracker with argument name as the title. The values of output arguments can be plain text or HTML. Any other complex type data received is displayed in string format.

Automation Tracker supports copying to clipboard. One of the following three options can be added to an element and the element will get a copy icon:

* `data-copyable="true"` - Copies the element's text content.
* `class="copyable"` - Copies the element's text content.
* `data-copy-text="custom text"` - Copies the specified custom text.

## Embedding the app

You can copy the app URL from a dialog displayed at the end of the deployment process. Alternatively, after deploying the app, navigate to **Orchestrator** &gt; **Automations** &gt; **[folder_name]** &gt; **Apps**, then click **More options** next to the app, and select **Copy URL**.
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/595686)

For more information, see [Publishing, deploying, and upgrading app projects](https://docs.uipath.com/studio-web/automation-suite/latest/everyone-user-guide/publishing-deploying-upgrading-app-projects) and [Managing Apps](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-apps#deploying-apps).

When embedding the app in iframes of the host application, include `embed_` in the URL to allow logging in through a pop-up. For external events mode, include the query parameter `target` and set the domain name as the value, e.g. `&target=https://www.example.com`. For example: `https://cloud.uipath.com/embed_/appsdev/apps_/default/run/production/22986e36-8b04-4593-b82f-aae4c14bb2dc/bd8c8ef5-a94a-43f5-9a5b-6df73d8f7aa6/IDc0b72c47295b49abaea6b701cfa5b730?el=VB&uts=true&target=https://www.example.com`

## Additional customizations

Most customizations can be done by editing variables in the app workflow files. The variables with a name starting with `Config` can be changed to customize the app. In some scenarios, activities must be updated as well.

* **Unique key name** - In external events mode, the input request object can have multiple properties, while in query parameters mode, multiple query parameters might be sent as inputs. The property that holds the unique identifier must be configured in the `ConfigInputDataObjectUniqueKeyName` variable in the initiate workflow. In the sample app, `Id` is the property name used to uniquely identify the current request. This unique value is used to maintain the action execution results as well.
* **Input type key name** - To allow configuring different root folders based on request type, the app needs to know the property name holding the type of object. The property that holds the unique identifier must be configured in the `ConfigInputDataObjectTypeKeyName` variable in the initiate workflow. In the sample app, `Type` is the property name. If you don’t have different types of objects, remove the value in this variable.
* **Required properties to start** - If any mandatory inputs are required to start the 360 process, specify those properties in the `ConfigRequiredInputProperties` variable in the initiate workflow. If the defined required properties don't have values, an error message will be thrown at runtime and subsequent activities won’t run. When configuring this variable, consider that:
  + It is mandatory to add the **Unique key name** to the collection.
  + If you don’t have different types of objects, you should not include the **Input type key name** in the collection.
  + Add any additional required properties to the collection.
* **Configure query parameters**: - In query parameter mode, the values of the parameters in the `ConfigQueryParameterNameMap` variable in `MainPage_Load_Initiate_Request_QueryParam.xaml` will be fetched and set to the input object. In this dictionary, the keys are the property names in the input object and the values are the query parameter names.
* **Data shown in the 360 panel** - This is configured by directly setting the value for each item. In the sample app, two sets are available, one for the **Case** type and another for the **Account** type. When one set is shown, the other is hidden based on type. Labels are static and can be changed as needed.
  + Set the respective control values in the activity **Try Catch: Set input data in 360 Panel** in the initiate workflow. Inside this block, a Switch is used to configure based on type. Use this block to set values based on the input object data.
  + To set data from the 360 process to show in the 360 panel, use the activity **Try Catch: Set 360 data from process in 360 Panel** in the initiate workflow and configure values as needed.
* **Hiding the 360 panel** - To hide the 360 panel from the app, set the variable `ConfigHide360Panel` to `True` in the initiate workflow. Even though the panel is hidden, the 360 process is still executed and the values are used to prefill input arguments in the form when an action is run.
* **Map input properties to action input arguments** - The values coming from an external event, query parameter, and the 360 process can be used to prefill the input form shown before executing an action. By default, if the action argument names match with any of the input object property names or 360 output property names, the values are prefilled. You can configure additional values using the following variables in the `ActionListPage_StartActionButton_click.xaml` workflow:
  + `ConfigInputArgumentsInputObjectPropertyMap` - Dictionary where the keys are action input argument names and the values are input object property names. The input objects are created from query parameters or messages from external events.
  + `ConfigInputArgumentsDat360ObjectPropertyMap` - Dictionary where the keys are action input argument names and the values are 360 output argument names.
* **Enable context-based filtering of actions** - By default, all actions are always listed for all request types. Using this option, you can display related actions based on the current request context. To enable it:
  1. In the `MainPage_Action_Folder_Change.xaml` workflow, set the `ConfigEnableContextFiltering` variable to `True`.
  2. Set the `ConfigContextFilteringPropertyName` value to the property name from the 360 process object that must be matched with action labels.
  3. Add tags to deployed actions in Orchestrator. Add the label `Common` to actions that you want to be always available irrespective of action type.
  4. For other actions that should be available only for specific request types, add tags as needed. Actions will be displayed when the tag value matches the value of the property configured in step 2. Multiple tags can be added to a single action to list the action for multiple request types.
  5. If you are using query parameter mode, configure the variables mentioned in steps 1 and 2 in the `MainPage_Load_Initiate_Request_QueryParam.xaml` workflow as well.

## Limitations and workarounds

* The custom list control which is used to show the list of actions cannot expand based on available space. Configure the height of this control so that it suits the most used screen size.
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/592116)
* Each row in the custom list has a fixed height. If the action name or description is long, it might get truncated. Use a shorter name and description for better alignment.
* The external events workflow cannot be tested using the debug option. To test, you must deploy and integrate the app in a host environment.