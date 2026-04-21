---
title: "Retrieving ticket details"
visible: true
slug: "retrieving-ticket-details"
---

This tutorial demonstrates how to use API workflows and retrieve ticket details that are later integrated with Agents and Maestro.

The API workflow aims to retrieve incident details from ServiceNow, then validate and fetch additional information about the ticket creator and their associated company from Salesforce, if available.

![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615436)

![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/615440)

1. [Create an API workflow](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/managing-api-workflows#creating-api-workflows).
2. Open **Data manager** and add the **incidentNumber** as an **Input** property, with the following properties:
   * **Type:** String
   * **Description:** Reference for the incoming ticket number
   * **Required:** True
3. In **Data manager**, add **incidentObject** and **isValidCallerIdLink** as variables, with the following properties:
   * **incidentObject**—stores the enriched incident details.
     + **Type:** Object
     + **Default value:** leave empty
   * **isValidCallerIdLink**—verifies if the **caller_id_link** retrieved from ServiceNow is a valid URL.
     + **Type:** Boolean
     + **Default value:** false
4. Open the **Debug configuration** window. In the mandatory **incidentNumber** field, enter INC0026701.
5. Add a **Connector** activity and configure it to use the following **ServiceNow** activity: **Search Incidents by Incident Number**. This retrieves the incident details based on the incident number provided as input.
   1. Select your ServiceNow connection.
   2. Connect **Incident ID** to the following variable: **workflow** &gt; **input** &gt; **incidentNumber**.
   3. Rename the activity context output to `$context.outputs.incident_1`**.**
6. To check if any incident was found in the previous step, add an **If** activity with the following condition:
   ```
   $context.outputs.incident_1.content && $context.outputs.incident_1.content.length > 0
   ```
7. In the **Then** branch, if any incident is found, proceed to validate the `caller_id_link` and fetch more details. Add a **Try Catch** activity.
   1. Inside the **Try** block, add a **Script** activity with the following **Code**:
      ```
      const callerIdLink = $context.outputs.incident_1.content[0].caller_id_link;
      const urlRegex = /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/i;
      $context.variables.isValidCallerIdLink = (callerIdLink && urlRegex.test(callerIdLink));
      return $context.variables.isValidCallerIdLink;
      ```

Rename the activity to "Validate caller_id link", and the context output name to `$context.outputs.Validate_Caller_ID_Link`.
   2. Inside the same **Try** block, add an **If** activity with the following **Condition**: `$context.variables.isValidCallerIdLink`. Rename the activity to "If caller_id_link is valid", and the context output name to `$context.outputs.If_Caller_ID_Valid`.
   3. In the **Then** (link valid) branch of the previous **If** activity, add a **Connector** activity, **Service Now HTTP Request**, with the following configuration:
      * **ServiceNow connection**—ServiceNow Developer Account
      * **Method**—GET
      * **Request URL**—
        ```
        $context.outputs.incident_1.content[0].caller_id_link
        ```Rename the activity to "Get Ticket Creator". The context output name remains as `$context.outputs.ServiceNow_HTTP_Request_1`.
   4. In the **Else** (link invalid) branch of the previous **If** activity, add a **Script** activity with the following **Code**:
      ```
      console.error("Invalid caller_id_link, skipping 'Get Ticket Creator' activity.");
      return null;
      ```

Rename the activity to "Log invalid caller_id_link", and the context output name to `$context.outputs.Log_Invalid_Caller_ID`.
   5. Outside of the **If** activity, but still inside the **Try** block, add **Script** activity with the following **Code**. This activity combines the initial incident details with the fetched creator details into a single incident object.
      ```
      const incident = $context.outputs.incident_1.content[0];
      let creatorDetails = null;
      const creatorOutput = $context.outputs.ServiceNow_HTTP_Request_1.content;
      if (creatorOutput && Array.isArray(creatorOutput) && creatorOutput.length > 0) {
        creatorDetails = creatorOutput[0];
      } else if (creatorOutput && typeof creatorOutput === 'object' && creatorOutput !== null) {
        creatorDetails = creatorOutput;
      }

      let companyDetails = null;
      const companyOutput = $context.outputs.ServiceNow_HTTP_Request_1.content;
      if (companyOutput && typeof companyOutput === 'object' && companyOutput !== null) {
        companyDetails = companyOutput;
      } else if (companyOutput && Array.isArray(companyOutput) && companyOutput.length > 0) {
        companyDetails = companyOutput[0];
      }

      return {
        ...incident,
        creator: creatorDetails,
        company: companyDetails
      };
      ```

Rename the activity to "JS - Incident Object". The context output name remains as `$context.outputs.Javascript_1`.
   6. Assign the incident object to a variable: add the **Assign** activity with the following configuration:
      * **To variable**—Select the **incidentObject** variable defined in the beginning.
      * **Set value**—Reference the context name of the previous Script activity:
        ```
        $context.outputs.Javascript_1
        ```Rename the activity to "Assign incidentObject". The context output name remains as `$context.outputs.Assign_1`.
   7. In the **Catch** block of the curent **Try Catch** activity, add a **Script** activity with the following **Code**:
      ```
      let errorMessage = `Error in Try_Catch_1: ${$error.title || 'Unknown Error'}`;
      if ($error.detail) {
        errorMessage += `\nDetails: ${$error.detail}`;
      }
      if ($error.data && $error.data.status) {
        const statusCode = $error.data.status;
        if (statusCode === 0 || statusCode === -1) {
          errorMessage += "\nNetwork error: Unable to connect to ServiceNow.";
        } else if (statusCode >= 500 && statusCode < 600) {
          errorMessage += "\nServiceNow server error.";
        }
      }
      console.error(errorMessage);
      console.error("Stack Trace:", $error);
      return null;
      ```

Rename the activity to "Log error details", and the context output name to `$context.outputs.Log_Error_Catch`.
   8. If any error occurs, add an **Assign** activity to use the simplified incident object with the inital details from ServiceNow:
      * **To variable**—Select the **incidentObject** variable defined in the beginning.
      * **Set value**—
        ```
        (($incidentDetails) => ({ id: $incidentDetails.sys_id, number: $incidentDetails.number, short_description: $incidentDetails.short_description, description: $incidentDetails.description, state: $incidentDetails.state, urgency: $incidentDetails.urgency, impact: $incidentDetails.impact, opened_at: $incidentDetails.opened_at, closed_at: $incidentDetails.closed_at }))($context.outputs.curated_search_incident_1.content[0])
        ```The activity name and the context output name remain as they are.
8. Exit the **Try Catch** activity and add an empty **Response** in the **Else** branch. Rename the **Response** activity to "No results found".
9. To check if any incident object contains sufficient information about the creator email and company account ID, add an **If** activity with the following condition:
   ```
   $context.variables.incidentObject && $context.variables.incidentObject.creator && $context.variables.incidentObject.creator.email && $context.variables.incidentObject.company && $context.variables.incidentObject.company.account_id
   ```

   1. In the **Then** branch, add a **Connector** activity and configure it to use the **Salesforce** activity: **Search using SOQL**. Rename the activity to "Get Contact" and the context output name to `$context.outputs.soqlQuery_1`.
   2. In the **Query** field, open the Expression editor and write:
      ```
      "SELECT Id, Name, Email, AccountId FROM Contact WHERE Email = '" + $context.variables.incidentObject.creator.email + "' LIMIT 1"
      ```
   3. In the **Then** branch, add an **If** activity with the following **Condition**:
      ```
      $context.outputs.soqlQuery_1.content && $context.outputs.soqlQuery_1.content.length > 0
      ```

Rename the activity to "If Contact Found" and the context output name to `$context.outputs.If_Contact_Found`. This conditional activity checks if a contact was found in Salesforce.
   4. In the **Then** branch of the "If Contact Found" activity, add a **Connector** activity and configure it to use **Salesforce Get Account** activity:
      * **Salesforce connection**—Salesforce Developer Account
      * **Account ID**—
        ```
        $context.variables.incidentObject.company.account_id
        ```Rename the context output to `$context.outputs.curated_account_1`. This activity retrieves account details from Salesforce using the **account_id** from the enriched **incidentObject**.
   5. In the **Then** branch of the "If Contact Found" activity, add a **For Each** activity and configure it look in: `$context.outputs.soqlQuery_1.content`. This loop iterates through the results of the Salesforce contact search (though the SOQL query limits to 1). Inside the loop, it attempts to fetch case details related to the found contact.
   6. Inside the body of the **For Each** loop, add a **Connector** activity, **Service Now HTTP Request**, with the following configuration:
      * **ServiceNow connection**—Salesforce Developer Account
      * **Method**—GET
      * **Request URL**—
        ```
        "/services/data/v64.0/sobjects/Case/" + $currentItem.Id
        ```Rename the activity to "Case Details". The context output name remain as it is.
   7. Exit the **For Each** loop and add an empty **Response** activity.
   8. In the **Else** branch of the "If Contact Found" activity, add a **Response** activity with the following **Response**:
      * **Response**—
        ```
        "No Salesforce Contact found for the incident creator email."
        ```Rename the activity to "Return No Contact Found Error".