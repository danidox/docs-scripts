---
title: "If"
visible: true
slug: "if"
---

The **If** activity enables conditional branches within API workflows to create dynamic execution paths based on data-driven conditions. Use the **If** activity for workflows that require different actions depending on real-time API responses, user inputs, or system states.

## Using the If activity

To add an **If** activity to your workflow:

1. On your API workflow designer canvas, select the plus (+) icon. The **Add activity** menu appears.
2. Select **If**.
3. In the **Properties** panel, write the expression in the **Condition** field.
4. Add activities to the **Then** and **Else** branches as needed.
5. Debug the workflow to execute the activity and generate output fields for later use.

## If activity example

The following example ensures that a transaction sync workflow only processes active customers who have made at least one transaction in the last 24 hours. If the conditions are not met, the workflow exits with a failure response.

Open the **Debug configuration** window, then paste and save the following JSON syntax:

```
{
  "id": 12345,
  "name": "John Doe",
  "isActive": true,
  "balance": 2500.75,
  "createdAt": "2025-03-25T12:00:00Z",
  "tags": [
    "premium",
    "verified",
    "active"
  ],
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zipCode": "10001",
    "coordinates": {
      "latitude": 40.7128,
      "longitude": -74.006
    }
  },
  "transactions": [
    {
      "transactionId": "txn_001",
      "amount": 150.5,
      "currency": "USD",
      "timestamp": "2025-03-25T10:30:00Z"
    },
    {
      "transactionId": "txn_002",
      "amount": -75.25,
      "currency": "USD",
      "timestamp": "2025-03-23T08:15:00Z"
    }
  ]
}
```

1. On your API workflow designer canvas, add an **If** activity.
2. Select the **Condition** field in the properties panel to open the Expression editor.
3. Use the Autopilot expression generator to create your condition, and prompt it the following:

"Write a conditional statement that checks that the input request is for an active customer and that there is at least one transaction object that was created in the last 24 hours".

The response should look like this:

   ```
   const now = new Date();
   const twentyFourHoursAgo = new Date(now.getTime() - 24 * 60 * 60 * 1000);

   if ($workflow.input.isActive) {
     const recentTransactions = $workflow.input.transactions.filter(transaction => {
       const transactionTimestamp = new Date(transaction.timestamp);
       return transactionTimestamp > twentyFourHoursAgo;
     });

     const hasRecentTransactions = recentTransactions.length > 0;

     hasRecentTransactions;
   } else {
     false;
   }
   ```
4. Check the **Activity test input** and **Expression output** panels to verify that the expression generates the expected results.
5. Save the **Condition** configuration.
6. To the **Then** branch, add a **Response** activity.
7. Configure the response as follows:
   * **Type**—Failure
   * **Details**—Open the Expression editor and write the following:
     ```
     {
         message: "Customer is not active or no transaction to process"
     }
     ```This step adds a validation at the beginning of the workflow to confirm a valid transaction exists before processing.