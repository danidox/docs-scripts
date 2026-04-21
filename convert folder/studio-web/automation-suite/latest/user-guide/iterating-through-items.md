---
title: "Iterating through items"
visible: true
slug: "iterating-through-items"
---

Iterating refers to repeating one or more activities in your automation project for each individual item in a collection of items. To iterate through items, add one of the available **For Each** activities in which you define the collection, and then add the activities to repeat inside the For Each. When you configure the activities to repeat, indicate that an activity should use data from each item in the iteration by using a variable and selecting the **current item** option for the For Each activity from the variable selector.

A generic [For Each](https://docs.uipath.com/activities/other/latest/user-guide/for-each) activity is available in the Control category, and various For Each activities are available for specific types of data. For example:

* **For Each Email** ([Microsoft 365](https://docs.uipath.com/activities/other/latest/user-guide/office365-email-for-each-email-connections) and [Google Workspace](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-email-for-each-email-connections)) - Repeat one or more activities for each message in an email folder. The current item option is `CurrentEmail`.
* [For Each File/Folder](https://docs.uipath.com/activities/other/latest/user-guide/office365-drive-for-each-file-folder-connections) - Repeat one or more activities for each file or folder in a OneDrive or SharePoint folder. The current item option is `CurrentItem`.
* [For Each Row in Workbook](https://docs.uipath.com/activities/other/latest/user-guide/office365-excel-for-each-row-connections) and [For Each Row in Spreadsheet](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-sheets-for-each-row-connections)- Repeat one or more activities for each row in an Excel workbook and Google Spreadsheet respectively. The current item option is `CurrentRow`.
* [For Each Sheet in Workbook](https://docs.uipath.com/activities/other/latest/user-guide/office365-excel-for-each-row-connections) and [For Each Sheet in Spreadsheet](https://docs.uipath.com/activities/other/latest/user-guide/google-workspace-sheets-for-each-sheet-connections) - Repeat one or more activities for each sheet in an Excel workbook and Google Spreadsheet respectively. The current item option is `CurrentItem`.