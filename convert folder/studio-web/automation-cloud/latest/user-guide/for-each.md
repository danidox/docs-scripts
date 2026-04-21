---
title: "For Each"
visible: true
slug: "for-each"
---

The **For Each** activity iterates over arrays and executes a defined set of steps for each array element. Use the **For each** activity to handle API responses containing object arrays, such as lists of users, orders, or records that require individual processing.

## How to aggregate data in an array

A common use case for the **For Each** activity is aggregating data from multiple API calls into a structured array using the **Script** activity.

The **For Each** activity automatically collects the output of the last activity within its **Body** flow, and compiles it into an array available in its own output.

## Using the For Each activity

To add a **For each** activity to your workflow:

1. On your API workflow designer canvas, select the plus (+) icon. The **Add activity** menu appears.
2. Select **Loop**, then **ForEach**.
3. In the **Properties** panel, configure the following fields:
   * **In**—Use the Expression editor to specify the array for iteration. Usually, this array comes from a previous API response.
   * **Item name**—Assign a reference name for array elements (default is `currentItem`). Use this reference to access each item during iteration.
4. In the **Body** of the **ForEach** loop, add the activities to process the array items.
5. Add activities to the **Then** and **Else** branches as needed.
6. Debug the workflow to execute the activity and generate output fields for later use.

## For Each activity example

The following example iterates over an array of employee objects, combines the first and last names of each employee, and returns the aggregated results in a structured response.

Open the **Debug configuration** window, then paste and save the following JSON syntax:

```
{
    "employees": [
        {
            "first_name": "Bobbie",
            "last_name": "Draper",
            "position": "administration",
            "email": "bdraper@rocinante.com"
        },
                {
            "first_name": "James",
            "last_name": "Holden",
            "position": "manager",
            "email": "jholden@rocinante.com"
        }
    ]
}
```

1. On your API workflow designer canvas, add a **For Each** activity.
2. Configure the **For Each** fields as follows:
   * **In**—Use the Expression editor to reference the `employees` array from the run configuration:
     ```
     $workflow.input.employees
     ```
   * **Item name**—Assign a reference name for array elements (default is `currentItem`). Use this reference to access each item during iteration.
3. In the **Body** of the **For Each** loop, add a **Script** activity.
4. For the **Script** activity, use Expression editor to create a JSON that combines the `first_name` and `last_name` properties into an object:
   ```
   return {
       "name": $currentItem.first_name + " " + $currentItem.last_name
   }
   ```
5. **Save** the configuration.
6. At the end of the workflow, add a **Response** activity.
7. Configure the response as follows:
   * **Type**—Success
   * **Details**—Open the Expression editor and write the following:
     ```
     $context.outputs.For_Each_2
     ```This step adds a validation at the beginning of the workflow to confirm a valid transaction exists before processing.
8. Debug the workflow to execute the activity.
9. Check the **Output** panel to review the response.