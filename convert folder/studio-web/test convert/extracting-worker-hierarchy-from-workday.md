---
title: "Extracting worker hierarchy from Workday"
visible: true
slug: "extracting-worker-hierarchy-from-workday"
---

The following tutorial demonstrates how to effectively use key features of API workflows:

* Input and output schemas
* Connector activities
* Connector HTTP activities
* JavaScript expressions
* Formatting and transforming responses
* Publishing workflows to Orchestrator

Workday contains extensive and sensitive employee data. Using an API workflow, you can extract and transform specific information. In this tutorial, the workflow retrieves an employee hierarchy based on first and last name requests.
  ![Full Workday API workflow](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/584628)

A valid connection to Workday is required.

1. [Create an API workflow](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/managing-api-workflows#creating-api-workflows).
2. Open **Data manager** and add the **firstname** and **lastname** properties as input. You can reference these properties later through the `$workflow.input` object.
3. Add a **Connector** and configure it to use the following **Workday (Rest)** activity: **Search Workers by Name or ID**.
   1. For the **Search string or ID** field, open the Expression editor and write the following:
      ```
      $workflow.input.firstName + " " + $workflow.input.lastName
      ```

![Search workers by Name or ID - workday activity](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/584633)
4. **Debug** your workflow and notice the successful response. Yet, zero workers were found.
5. Add an **If** activity, and use the following snippet as the **Condition**:
   ```
   $context.outputs.Workers_1.content.length <= 0
   ```
6. For the **Then** branch of the **If** activity, add a **Response** activity, and configure it as follows:
   * **Type**—Failure
   * **Details**—
     ```
     { "notFound": "No workers found for given input" }
     ```
7. **Debug** your workflow again. Since you did not provide the required input, the workflow automatically proceeds to this response and sets the workflow status to **Failed**.
8. Define a **[Debug configuration](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/managing-api-workflows#adding-a-debug-configuration)** with the following payload:
   ```
   {
     "firstName": "Betty",
     "lastName": "Liu"
   }
   ```
9. **Debug** your workflow until you begin to see results in the **content** property of the **Output** schema.
   ![Debugging workflow and content property](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/584641)
10. For the **Else** branch of the **If** activity, add a **Loop** &gt; **For Each** activity, and configure it as follows:
    * **In**—
      ```
      $context.outputs.Workers_1.content
      ```
    * **Item name**—currentItem
    * **Accumulate results**—On
11. In the **For Each** activity body, add three **Workday REST HTTP Request** activities for the **Workday (REST)** connector:
    * Workday REST HTTP Request 1: Find Direct Reports
    * Workday REST HTTP Request 2: Find Organization Details
    * Workday REST HTTP Request 2: Find PeersThis means that for every worker in the loop, the activity returns the mentioned details: direct reports, organization details, and peers.
12. Configure the **Workday REST HTTP Request 1: Find Direct Reports** activity as follows:
    * **Method**—GET
    * **Request URL**—
      ```
      "/common/v1/uipath_dpt1/workers/" + $currentItem.id + "/directReports"
      ```

Where `uipath_dpt1/workers` is part of the sandbox definition.
13. Configure the **Workday REST HTTP Request 2: Find Organization Details** activity as follows:
    * **Method**—GET
    * **Request URL**—
      ```
      "/common/v1/uipath_dpt1/supervisoryOrganizations/" + $currentItem.primaryJob.supervisoryOrganization.id
      ```

Where `uipath_dpt1/supervisoryOrganizations` is part of the sandbox definition.
14. Configure the **Workday REST HTTP Request 3: Find Peers** activity as follows:
    * **Method**—GET
    * **Request URL**—
      ```
      "/common/v1/uipath_dpt1/supervisoryOrganizations/" + $currentItem.primaryJob.supervisoryOrganization.id + "/workers"
      ```

Where `uipath_dpt1/supervisoryOrganizations` is part of the sandbox definition.
15. **Debug** your workflow again. Notice that the workflow successfully loops a specified number of times (based on the number of results from the first activity) over these three HTTP requests.
16. In the **For Each** activity body, add a **Script** activity after the previous three **Workday REST HTTP Request** activities.
17. To configure the **Script** activity, use the Autopilot generator in the Expression editor and provide the following prompt:

"From the previous 3 activities, create 3 objects. Object 1 is "manager" and should return the descriptor as name and person.email as email. Object 2 is peers from the 3rd http request and should loop over all results and return descriptor as "name" and primaryworkemail as "email". Last, add an object "reports" that loops over all first http results and report name (descriptor) and primaryworkemail as email."

The generated JavaScript code should look like the following:

    ```
    return {

        // Details on the worker

        manager: {

            name: $currentItem.descriptor,

            email: $currentItem.person.email

        },

        // Details for their peers

        peers: $context.outputs.Workday_REST_HTTP_Request_1.content.data.map(peer => ({

            name: peer.descriptor,

            email: peer.primaryWorkEmail

        })).filter(peers => peers.name !== $currentItem.descriptor), // Filter out the employee itself,

        // Details for their direct reports

        reports: $context.outputs.Workday_REST_HTTP_Request_3.content.data.map(report => ({

            name: report.descriptor,

            email: report.primaryWorkEmail

        }))

    }
    ```
18. Outside of the **For Each** loop, add a **Response** activity and configure it as follows:
    * **Type**—Success
    * **Details**
      ```
      $context.outputs.For_Each_1.results
      ```This step instructs the workflow to return the complete list of results generated by the **For Each** loop.
19. Debug your workflow end to end. You should have a successful execution and response schema should meet your needs.
20. Generate the **Output** schema of the successful execution of your workflow:
    1. Navigate to the **Output** section of the **Run output** panel.
    2. Select **Copy to clipboard**.
    3. Navigate to the **Output** section of the **Data Manager** panel.
    4. Select **Generate From Payload**.
    5. Paste the output copied from **Output** &gt; **Run output**.

Your API workflow now includes input and output schemas, allowing it to be invoked across the platform.
21. **Publish** your API workflow to Orchestrator.