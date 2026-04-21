---
title: "Viewing jobs"
visible: true
slug: "viewing-jobs"
---

If you want to know whether previous runs completed successfully or you need to investigate potential issues, go to the **Jobs** section to view a history of previous runs for published automations.

For each job, you can view when it last started and ended, its duration, the run status (**Successful**, **Faulted**, **Running**, **Pending**, or **Stopping**), the trigger type (manual, time, or event), the version of the automation, and the Orchestrator folder where the automation was published. Additionally, you can filter jobs by their status and location and refresh the list of jobs. You cannot filter if there are no jobs, but you can still refresh the list. You can also view more job details by clicking on a job.

Additional tools are available in the ![](/images/studio-web/studio-web-image-More_VT.png) **See more** menu on the right side of each job:

* **Restart** - Run the automation again.
* **View details** - View information about the job, such as the job status, input, and output. The window is resizable.
* **View logs** - View information about the job's run output. The panel is resizable.
* **Stop** - Stop the automation. Available when the run status is pending or running.
* **View recording** - For automations that contain [web browser interactions](https://docs.uipath.com/studio-web/automation-cloud/latest/everyone-user-guide/using-ui-automation#using-ui-automation-for-browser-interactions) using UI Automation activities, you can watch a recording of the actions performed by the robot. This feature is available only if [live streaming is enabled](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/live-streaming-and-remote-control) for the process in Orchestrator.
* **View this version** - Open this version of the automation in Studio Web in read-only mode.
* **View in Orchestrator** - See details about the job in Orchestrator. For more details, see [Managing Jobs](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-jobs#viewing-job-details) in the Orchestrator guide.

The **Jobs** section shows recently completed jobs. To see the full list of jobs associated with an automation, select the **detailed view** button next to the **Jobs** section title. From this view you can also filter runs by process name.

  ![docs image](/images/studio-web/studio-web-docs-image-440827.webp)