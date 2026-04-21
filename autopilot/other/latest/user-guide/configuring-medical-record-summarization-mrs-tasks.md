---
title: "Configuring Medical Record Summarization (MRS) tasks"
visible: true
slug: "configuring-medical-record-summarization-mrs-tasks"
---

This page helps you how to set up Action Center tasks for use with the Medical Record Summarization (MRS) interface in Autopilot for Everyone. With the correct setup, tasks are properly identified and displayed, so end users can review, edit, and complete them in Autopilot for Everyone.

## About the MRS integration

The MRS integration shows specific Action Center tasks in a three-pane interface. This view includes the generated summary, a source document viewer, and an interactive Autopilot for Everyone chat with context of the summary.

## Configuring Action Center tasks for MRS integration

For an Action Center task to be recognized as an MRS task by Autopilot for Everyone, it must meet the following two conditions:

* Task tagging—The task **must contain at least one tag** with the display name `MRS` or `Autopilot`. Autopilot for Everyone uses this tag to identify and display the task in the specialized MRS interface.
* Required data properties—The task must contain the following key-value properties. These are typically passed as Action Center task output arguments from the automation that creates the Action Center task:

  | Property | Description | Format |
  | --- | --- | --- |
  | Summarization | The complete, AI-generated summary of the medical record. | String (Markdown) |
  | Citations | The source references for the information contained within the summary. | A structured format, such as JSON, that links citation markers in the summary to specific pages in the source document. |
  | InputFileSBPath | The full path and file name of the source document, such as the patient medical record PDF, within the specified storage bucket. | String |
  | InputFileSBName | The name of the Orchestrator storage bucket where the source document is located. This property was specifically added to support the MRS feature in Autopilot for Everyone. | String |

## How it works

Once a task is correctly configured, end users can:

1. See the task
   * The MRS task appears on your users Autopilot for Everyone main page > **Your Action Center Tasks** list. It is marked with an MRS icon and tag.
2. Open the task
   * To open the three-pane summarization view, users must select the task.
3. Interact with the task
   * Review the summary.
   * Select citations to view the source page.
   * Edit the summary text directly.
   * Use the chat pane to interact with the summary content.
4. Save or complete the task
   * Save their edits or submit the task to complete it.

## Limitations

Currently, the chat panel can use the summary text, but not the source file contents.