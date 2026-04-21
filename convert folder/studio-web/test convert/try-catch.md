---
title: "Try Catch"
visible: true
slug: "try-catch"
---

The **Try Catch** activity provides structured exception handling within workflows. Use it to define fallback actions for API failures, invalid data, or unexpected errors.

## Using Try Catch activity

To add a **Try Catch** activity to your workflow:

1. On your API workflow designer canvas, select the plus (+) icon. The **Add activity** menu appears.
2. Select **More ...** , then **Try Catch**.
3. In the **Properties** panel, provide a name for your error.
4. Add activities to the **Try** block. These are the activities monitored for errors.
5. Define the error-handling logic in the **Catch** block. If any step in the **Try** block fails, execution transitions to the **Catch** flow.
6. Debug the workflow to execute the activity and generate output fields for later use.

## Accessing error details

When an error occurs in the **Try** block, the **Try-Catch** activity exposes structured error details. To access the error details, use `$context.outputs.Try_Catch_X.error`, or `$error`.

The error object maintains a consistent structure, as follows:

```
"Try_Catch_1": {
        "error": {
          "type": "<runtime error source>",
          "title": "<summary error message>",
          "status": <response status code>,
          "detail": "<detailed error message",
          "data": {},
        }
      }
```

The error details are:

* **type**—Indicates the runtime source of the error.
* **title**—Provides a concise error summary.
* **status**—The HTTP status code (if applicable).
* **detail**—Offers a detailed explanation of the error.
* **data**— Includes additional metadata about the failed task. This field may not always be populated.

You can reference these properties to build structured error responses or trigger alerts.