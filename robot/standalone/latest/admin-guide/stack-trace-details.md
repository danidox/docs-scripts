---
title: "Stack trace details"
visible: true
slug: "stack-trace-details"
---

Runtime errors provide a human-readable stack trace to help you locate the activity that caused your workflow execution to fail. This stack trace is visible at runtime in Studio, Orchestrator, and in Robot logs.

It contains the workflow file name, activities name, and execution hierarchy, as follows:

![Stack trace details in Studio](/images/robot/robot-stack-trace-details-in-studio-555505.webp)

* **Source**: The activity that caused the error.
* **Message**: The error message.
* **Exception type:** The specific type of the exception thrown.
* A stack trace showing the path from the main workflow down to the activity that generated the error. For the example in the image, the hierarchy is: Main &gt; Main Sequence &gt; Sequence1 &gt; Activity1 &gt; Sequenc &gt; Sequence3 &gt; Parallel3 &gt; Throw.