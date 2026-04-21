---
title: "September 2024"
visible: true
slug: "september-2024"
---

## 30 September 2024

### Improved Expression Editor

We have improved the design and functionality of the Expression Editor. Some changes include:

* Fixing line spacing and text alignment.
* Improving the layout of the **Test**, **Fix**, and **Insert Variable** buttons.
* Adding dedicated **Undo** and **Redo** buttons.
* Moving the breadcrumb navigation next to the **Expression editor** title.
* Improving the experience of testing an expression.
* Allowing you to resize the area where you can write expressions using the new **Expand editor** and **Collapse editor** buttons.

  ![Expression Editor](/images/sw/release-notes-expression-editor-466492.webp)

### Improvements

* User-defined strings used in activity properties now have a design consistent with other UI elements.
* Saving changes made to a workflow no longer times out when updating activity properties.
* To improve the functionality of Studio Web, we have created separate buttons for **Feedback**, **Restart getting started**, and **Manage access**, making these options more visible and easier to use. Each option has its own tooltip, which appears when hovering over the button.

### Recent activities updates

The following categories of activities are now in general availability:

* [Xero](https://docs.uipath.com/activities/other/latest/integration-service/uipath-xero-xero-activities)

The following categories of activities have received updates:

* [Google Workspace](https://docs.uipath.com/activities/other/latest/productivity/release-notes-uipath-gsuite-activities) (v2.7.21, v2.7.22)
* [Microsoft 365](https://docs.uipath.com/activities/other/latest/productivity/release-notes-microsoftoffice365-activities) (v2.7.21, v2.7.22)
* [System](https://docs.uipath.com/activities/other/latest/workflow/release-notes-uipath-system-activities) (v24.10.5)

The following categories of activities are now available in preview:

* [Active Directory](https://docs.uipath.com/activities/other/latest/it-automation/active-directory-activities)
* [Exchange Server](https://docs.uipath.com/activities/other/latest/it-automation/exchange-server-activities)
* [Google Tasks](https://docs.uipath.com/integration-service/automation-cloud/latest/user-guide/uipath-google-tasks)
* [HyperV](https://docs.uipath.com/activities/other/latest/it-automation/hyper-v-activities)
* [System Center](https://docs.uipath.com/activities/other/latest/it-automation/system-center-activities)
* [Workday REST](https://docs.uipath.com/activities/other/latest/integration-service/uipath-workday-workdayrest-activities)

## 2 September 2024

### Upgrade to .NET 8

Studio Web has been upgraded to [.NET 8](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-8/overview), the latest version of the.NET framework.

Please note that running automations now requires robots that use the.NET 8 framework. Serverless robots are automatically upgraded to.NET 8, but if you use your own cloud robots or local robots via UiPath® Assistant, these robots must use.NET 8 to run your automations correctly. Automations published before Studio Web was upgraded to.NET 8 (August 30) are not affected.

### Use Autopilot™ to automatically fix activity property errors

Autopilot can now automatically fix activity property errors by selecting the new **Fix** button located on the right side of a property with errors. To learn more, refer to.

  ![Autopilot fixing activity property errors](/images/sw/release-notes-autopilot-fixing-activity-property-errors-461977.webp)

### Recent activities updates

The following categories of activities have received updates:

* [UI Automation](https://docs.uipath.com/ACTIVITIES/other/latest/ui-automation/release-notes-uipath-uiautomation-activities-v24-10) (v24.10.3)