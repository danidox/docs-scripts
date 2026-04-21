---
title: "Connector"
visible: true
slug: "connector"
---

The **Connector** activity provides access to Integration Service connectors and custom-built connectors. It helps your workflow interact with third-party APIs without a manual HTTP request configuration.

However, each connector includes a dedicated **HTTP Request** activity. This activity leverages existing connections for authentication, enabling interaction with any API endpoint beyond those covered by the connector prebuilt activities.

## Using the Connector activity

To add a **Connector** activity to your workflow:

1. On your API workflow designer canvas, select the plus (+) icon. The **Add activity** menu appears.
2. Select **Connector**. A pop-up window opens, showing all available connectors.
3. Select the desired connector type. The list of all available activities for the selected connector is displayed.
4. Select the activity you need.
5. In the **Properties** panel, configure the connection for the selected activity. If no connections are available, select **+ Connection** and follow the wizard instructions.
6. Configure the activity to your needs.
7. Debug the workflow to execute the activity and generate output fields for later use.

## Connector activity example

The following example uses the Salesforce connector and the **List All Records** activity to retrieve a specific user based on their email address.

Adjust the run configuration to match the data in your Salesforce environment. If you do not have access to a Salesforce environment, [sign up for a free account](https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/quickstart_dev_org.htm) and follow the authentication [setup instructions provided in our documentation](https://docs.uipath.com/integration-service/automation-suite/2024.10/user-guide/uipath-salesforce-sfdc-authentication).

Open the **Debug configuration** window, then paste and save the following JSON syntax in the **Project arguments** section:

```
{
  "email_address": "{insert_your_email_here}"
}
```

1. Once you establish the connection to the Salesforce connector, select the **List All Records** activity.
2. With the **List All Record**s activity selected, go to the **Properties** panel, and for the **Select object** field, select **Users**.
3. For the **Where** field, use the Expression editor to define the following search query:
   ```
   "email = '" + $workflow.input.email_address + "'"
   ```

You can also use input variables when defining the search query.
4. **Debug** your activity.