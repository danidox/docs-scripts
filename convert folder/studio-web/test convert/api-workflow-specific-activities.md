---
title: "API workflows activities"
visible: true
slug: "api-workflow-specific-activities"
---

## Recommended best pratices

* Logically chain activities to ensure consistent data flow between worfklow steps.
* Use expressions in conditions, request URLs, and payloads for dynamic data handling.
* Use **Try-Catch** to handle potential failures in API calls or business logic.
* Debug workflows with sample inputs using **Debug configuration** to validate expressions and execution paths.
* Rename your `$context.outputs.activity_name` property so you can easily reference it in future expressions.