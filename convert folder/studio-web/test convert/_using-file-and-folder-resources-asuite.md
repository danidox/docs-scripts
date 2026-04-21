---
title: "Using file and folder resources"
visible: true
slug: "using-file-and-folder-resources"
---

You can automate workflows involving file and folder operations such as copying, downloading, uploading, moving, or deleting across online applications and services. Microsoft 365 and Google Workspace activities enable you to browse the online storage to indicate which files or folders to use in your workflows.

## Retrieving files

When creating workflows across different online applications, the first step in using a file or folder resource is to make it available in your automation using activities that retrieve files such as:

* **File Created** (for [Google Drive](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-trigger-new-file-created) or [Microsoft One Drive and SharePoint](https://docs.uipath.com/activities/other/latest/user-guide/office365-trigger-new-file-created)) and **File Updated** (for [Google Drive](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-trigger-file-updated) or [Microsoft One Drive and SharePoint](https://docs.uipath.com/activities/other/latest/user-guide/office365-trigger-file-updated)) triggers - Start an automation when a file is created or updated.
* **Download** activities - Download files from an online app or service. **Download File** activities are available for multiple online apps and services and **Download Email Attachments** activities are available for [Gmail](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-email-download-attachments-connections) and [Microsoft Outlook](https://docs.uipath.com/activities/other/latest/user-guide/office365-email-download-email-attachments-connections).
* **Get** activities - Get a reference to file resources in an online app for use in other activities. For example, **Get File/Folder** and **Get File List** activities for Google Drive or Microsoft OneDrive and SharePoint.
* **For each file/folder** - Iterate over a list of files and folders in [Google Drive](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-drive-for-each-file-folder-connections) or [Microsoft OneDrive and SharePoint](https://docs.uipath.com/activities/other/latest/user-guide/office365-drive-for-each-file-folder-connections).

## Uploading and sending files

After a file resource is retrieved in an automation, you can then upload or send it. For example:

* **Upload** activities - Upload files to an online app or service. **Upload File** activities are available for multiple online apps and services.
* Activities that send emails with attachments, such as **Send Email**, **Reply to Email** for Google Drive or Microsoft OneDrive and SharePoint, or activities that send files, such as [Send File to Channel](https://docs.uipath.com/activities/other/latest/user-guide/uipath-salesforce-slack-upload-file) for Slack.

## Moving files and folders

Dedicated activities are available for moving files inside Google Drive ([Move File](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-drive-move-file-connections)) and files or folders inside Microsoft OneDrive and Sharepoint ([Move File/Folder](https://docs.uipath.com/activities/other/latest/user-guide/office365-drive-move-item-connections)).

## Deleting files and folders

Dedicated **Delete file** activities are available for deleting files from multiple applications. The **Delete File/Folder** activities for [Google Drive](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-drive-delete-file-or-folder-connections) and [Microsoft OneDrive and Sharepoint](https://docs.uipath.com/activities/other/latest/user-guide/office365-drive-delete-item-connections) can delete both files and folders.

## File resource properties

In addition to the resource itself, you can use various properties to perform certain actions in your automations. For example, you can create conditions based on the size or extension of a file to filter which files to use, or add the name of the file in the body of an email.

The following table lists the most common file resource properties. Not all properties are available for all activities.

| Property | Description |
| --- | --- |
| FullName | File name including extension. |
| Name | File name without extension. |
| Extension | File extension. |
| CreationDate | Date and time when the file was created. Additional values are available based on the date, for example the day of the week, or parts of the date such as the year. |
| LastModifiedDate | Date and time when the file was last modified. Additional values are available based on the date, for example the day of the week, or parts of the date such as the year. |
| ID | Unique ID of the resource. |
| MimeType | Media type of the resource, if available. |
| SizeinBytes | Size in bytes. |
| IsFolder | Whether the resource is a folder. |
| IsResolved | Whether the remote resource is available for use. |
| Uri | URI identifying the remote resource. |
| LocalPath | The path to where the resource is downloaded locally. |
| LocalCopy | Reference to the local copy of the resource. |

## Examples of using file resources in an automation

#### Upload email attachments from Gmail to Google Drive

This simple automation is triggered when a new email with attachments is received, it downloads the email attachments, and then uploads them to a Google Drive folder.

1. Create a new project, and select the Google Workspace [Email Received](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-trigger-new-email-received) as the trigger.
2. In the trigger activity:
   1. Create or select a connection.
   2. Select **Show additional options**, and then the option **With attachments only**.
   3. Select the folder where emails arrive from the **Email folder or label** field.
3. Add a Google Workspace [Download Email Attachments](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-email-download-attachments-connections) activity. In the activity, select a connection, then for the **Email** option select the field labeled **Click to use a variable**, and then **Email received** &gt; **Email**.
4. Add a Google Workspace [Upload Files](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-drive-upload-files-connections) activity. In the activity:
   1. Create or select a connection.
   2. Select the **File(s)** field labeled **Click to use a variable**, and then select **Download Email Attachments** &gt; **Attachments**.
   3. Select the **Destination folder** using the folder browser.

#### Send email when new file is created

This simple automation sends an email when a new file is created in a Microsoft OneDrive folder. The activities used in this example are also available for Google Drive, so you can use the same steps to build a similar automation if you are using Google Workspace instead of Microsoft 365.

1. Create a new project, and select the Microsoft 365 [File Created](https://docs.uipath.com/activities/other/latest/user-guide/office365-trigger-new-file-created) as the trigger.
2. In the trigger activity:
   1. Create or select a connection.
   2. Select the folder the folder where the file is created from the **In location** field, for example **Reports**.
3. Add a Microsoft 365 [Send Email](https://docs.uipath.com/activities/other/latest/user-guide/office365-email-send-mail-connections) activity. In the activity:
   1. Create or select a connection.
   2. Add a recipient in the **To** field.
   3. Add a subject in the **Subject** field, for example *Report created*.
   4. Add a body in the **Body** field. For example, to enter a message that contains the name of the new file *A new report, `File name`, is available in the Reports folder.*
      1. Type *A new report,* .
      2. To add the variable for the file name after the last character, select **File created** &gt; **Show more** &gt; **File** &gt; **FullName**.
      3. Continue typing after the variable *is available in the Reports folder*.