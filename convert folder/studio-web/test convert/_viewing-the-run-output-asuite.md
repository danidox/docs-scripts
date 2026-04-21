---
title: "Viewing the run output"
visible: true
slug: "viewing-the-run-output"
---

The Run output window provides real-time information on each step in the automation and displays any errors that might show up. The window opens automatically when you start a run, and you can also open or hide it at any time by clicking the run output icon on the right of the project page.

Information about each step in the automation is displayed as it's happening. Before the actual workflow execution starts, a few steps are executed in preparation of each run: the project is built, the robot machine is initialized, the project and its dependencies are transferred to the robot machine. You can copy any entry by hovering over an event in the output log and clicking the **Copy to clipboard** button.

In the Run output window, you can:

* View the run status: running, succeeded, failed, paused, or stopped.
* Download logs - Download the run output in a TXT file that contains more detailed information such as a more exact timestamp and the log level of each event
* Search and filter - Use the search box and the filter menu to search in the output and filter the messages by severity.
* Click on an error message and navigate to the activity that caused it.
* When you run a project that contains UI automation activities, a live stream of the execution is displayed in a window that you can resize and take control of.
  ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/246170)

## Live streaming and taking control in projects with UI automation

When running a project that involves browser interactions using UI automation activities, you can view the execution in a window available in the run output. This comes in helpful when troubleshooting or debugging and also allows you to take control in situations where human intervention is required, such as accepting cookies on a website or completing a captcha.

The following options are available while live streaming the automation:

* Open in a new tab: opens the live streaming window in a separate tab in the same browser.
* Toggle full screen: opens the live stream of the automation in full screen mode.
* Toggle picture in picture: opens the live stream of the automation in a picture in picture window.
  + This window can be moved, resized, and stays on top of other windows.
  + Closing the window does not stop the automation, it just minimizes the window to the **Run output** panel.
* **Take Control**: only available when using the **Open in a new tab** or **Toggle full screen** options.