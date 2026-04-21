---
title: "Do While"
visible: true
slug: "do-while"
---

The **Do While** activity enables workflows to repeatedly execute one or more activities. Use it for paging through API datasets or repeating actions until a specific property in the response changes.

## Using the Do While activity

To add a **Do While** activity to your workflow:

1. On your API workflow designer canvas, select the plus (+) icon. The **Add activity** menu appears.
2. Select **Loop**, then **Do While**.
3. In the **Properties** panel, configure the following fields:
   * **Condition**—Use the Expression editor to specify the condition evaluated after each iteration. Usually, this condition references data from a previous API response.
   * **Limit**—Specify a number or combine context and workflow data to set a dynamic limit for loop iterations. This helps prevent excessive iterations, handling large data sets, or avoid infinite loops.
4. In the **Body** of the **Do While** loop, add the activities to process the items.
5. Use the **Break** activity to exit the loop early. Place it within an **If** activity to conditionally break the loop based on a defined condition.
6. Debug the workflow to execute the activity and generate output fields for later use.

## Do While activity example

For an extensive example using the Do While activity, refer to [Paging over HTTP calls](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/paging-over-http-calls#paging-over-http-calls).