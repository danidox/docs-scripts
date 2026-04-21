---
title: "The Automation details tab"
visible: true
slug: "the-automation-details-tab"
---

The **Automation details** panel is displayed when you select an automation, with the following tabs:

## Details

The **Details** tab displays data the automation developer provided during design time in Studio. Once you select an automation in the left-side panel, the tab displays the automation name, followed by a shareable link, accessible only by users with the necessary permissions.

* **Description**, optionally accompanied by the **More details** link, which redirects you to Automation Hub
* **Version** of the automation package
* **Last Run** indicator
* **Last Updated** indicator
* Any external **Apps** that were used in the automation, such as Outlook, Acrobat Reader, etc.
* The Orchestrator **Folder** that stores the automation package

If the automation is ready for running, you can start its execution by selecting the **Run** button at the bottom of the tab. Otherwise, if it needs extra configurations, such as input arguments or connections, the button **Configure** is displayed and redirects you to the **Configure** tab.

## Configure

The **Configure** tab displays data the end user should consume during the execution of the automation:

* The **Inputs** section helps you configure the input argument required by the automation for a successful execution. Mandatory input fields are marked with an asterisk. If the automation was designed without input arguments, the **Inputs** section is absent.
  :::note
  If the process has input arguments, hover over the information icon to see their description.
  :::
* The **Connections** section helps you configure the connections required by the automation for a successful execution. If the automation was designed without connections, the **Connections** section is absent.
* The **Picture in picture** section allows you to turn on or off the Robot session. The setting is inherited from the project settings in Studio.
* The **Keyboard Shortcuts** section allows to set custom keyboard shortcuts to manage the execution of the automation, such as pause or stop commands.

Select **Save** to preserve the current configuration, then select **Run** to start the job execution.

## Jobs

The **Jobs** tab displays the custom messages created using the Report Status activity. These messages monitor the job execution and inform you about every action the automation takes, until it successfully completes or fails due to errors.

If the selected automation was never run in the past seven days, the **Jobs** tab is empty. Once you start running a process, the corresponding jobs and their statuses are displayed in this tab.

If a job execution fails, you are redirected to the **Jobs** tab to see the errors that occurred, regardless of the tab which was currently in focus.

Jobs from multiple running automations are divided into separate collapsible sections. To view details on a particular execution, expand the relevant job section.

Once a job completes, its execution details remain accessible on the **Jobs** tab for a week, then they get dismissed automatically. You can always access execution details in the **History** tab.

## History

Displays the job history for the selected automation, along with the job state and time stamp. Clicking on an entry displays the job details, such as machine name, error message, or output values (if applicable).