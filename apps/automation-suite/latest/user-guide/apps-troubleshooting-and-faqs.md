---
title: "Apps Troubleshooting and FAQs"
visible: true
slug: "apps-troubleshooting-and-faqs"
---

## Message: Connection to Apps Service Is Lost.

When saving Apps from **App Studio**, the following error message can occur:

"Connection to Apps service is lost."

### Possible Cause

1. You've lost internet connection. **Apps** requires an active internet connection to save changes you make to your app. OR
2. The reason for this error can be the fact that the App service uses WebSocket to save the App definition. OR
3. `wss://*.uipath.systems` is not added on your allow list.

### Solution for the WebSocket-related issue

First, ensure that you have an active internet connection. If you are still facing issues then:

1. Allow `apps-socket.uipath.com` to have long live connections by making sure you have the `connection: Upgrade` parameter in the header. This must be done with the help of your IT team.
2. Work with your IT or network team to understand how WebSocket traffic policies are being handled and alter them as needed.
3. Allow WebSocket connections by making sure that `apps-socket.uipath.com` is not added to your proxy policy. This must be done with the help of your IT team.

### Solution for the allow list issue

Add `wss://*.uipath.systems` to your allow list.

## Message: Errors in App

When previewing an app, the following error can occur, even if there are no errors:

"Errors in App"

### Possible Cause

One or more browser extensions can cause this error to occur.

### Solution

1. Try previewing the app in a different browser. OR
2. Deactivate all extensions from your current browser.

## Message: Process(Process_Name) Not Found.

An error stating a process is not found can occur in runtime, even if the process is available in Orchestrator.

### Possible Cause

Check the name of the process and make sure that it does not contain an underscore (`_`) character.

### Solution

Rename the process and remove all underscore (`_`) characters.

## Issue: Event on Page Load Not Working

Setting the control value using the **Set Values** rule in the **Page load** event results in not setting the control value properly.

### Solution

Instead of setting the control value in the **Page load** event, use the app variable in the **Set Values** rule and bind the app variables to the control. By doing so, the control value is being set correctly.

## Issue: Slower Performance

When custom list, table, list, and dropdown controls have a thousand or more records to display, the performance may get slower.

### Solution

Make sure to provide a height in the control size property and not leave it set to **Auto**. Once the height is specified, performance optimization kicks in, records being loaded progressively as the user scrolls.

## Issue: Default Selected Value Not Showing in Runtime

When in Apps design time, the default selected value is correctly displayed for the dropdown control, but when switching to runtime it is no longer displayed

### Solution

For this example we will use `10` as the value. To correctly display the value in runtime, insert the value in the following format: `=10`, instead of simply `10`.

## Issue: Custom Arguments Not Displayed

When adding custom arguments in the process details page, the newly added arguments are not displayed in the resource panel for binding.

### Solution

Make sure to first refresh the browser and then add the arguments by pressing the ![](/images/apps/apps-image-Add-a567890c.png) sign. If you do not refresh the browser first, the newly added arguments will not be displayed in the resource panel for binding.

## Issue: App Preview Does Not Work in the First Attempt

In some situations, app preview might not work in the first attempt.

### Solution

Make sure that any pop-up blockers are disabled in your browser. Once pop-ups are allowed, app preview works as expected.

## Issue: Unable to Preview an App or Run an App From the Home Page

When previewing or running an app from home page, the app does not load and can result in a blank page.

### Possible Cause

The start page of the app is not set. Since there is no start page set, the app cannot decide which page to run or preview.

### Solution

Set the start page explicitly from the tree view.

   ![docs image](/images/apps/apps-docs-image-94627-99f0eb06.webp)

## Issue: Variable Not Saved in the Get File From Storage Bucket Rule

When you assign an app variable in the **Assign file to app variable** property in the **Get File from Storage bucket** rule, the app variable is not saved.

### Solution

When you open the app designer, you have to add the app variable again. You can publish the app after adding the app variable and the published version will have the app variable. However, in design time, the app variable has to be added again each time you open the app in App Studio.

   ![docs image](/images/apps/apps-docs-image-92956-2ae933f6.webp)

## Issue: Incorrect Start Page Is Displayed When Previewing an App

When previewing an app, the displayed start page is not the correct one.

### Possible Cause

Two pages have the same order, leading to an incorrect start page in runtime.

### Solution

To display the correct page in runtime, follow these steps:

1. Clone the page that needs to be set as the start page.
2. Set the newly-cloned page as the start page.
3. Delete the original page.

You can now preview your app and the correct start page should be displayed.

## Issue: Borders Not Displayed Properly

In certain situations, when adding a tab, container, or page container the borders are not displayed properly if the content within has a larger width than the width of the parent control (tab, container or page container) and if a center or right alignment is applied on it. In this situation, the left portion of the content is cut off from the view and it will also be inaccessible using scroll.

### Possible Cause

This is a browser behavior issue that is seen when flex display and center alignment is used together.

### Solution

To get around this issue, we suggest using left alignment (justify left) or configure a width for the parent control that is larger (or at least equal) to the content inside it.

## Issue: AppInsightService.AppInsight Warning Message in Console Logs

In certain situations, the following warning message is continuously displayed in the console logs:

"`AppInsightService.AppInsight` not yet ready"

### Possible Cause

An ad blocker can cause this issue

### Solution

Make sure that any pop-up blockers are disabled in your browser.

## Issue: A Page Opened in Different Places at Once Is No Longer Updated

A page opened twice stops updating.

For example, you have a table inside a page container updating the value of a variable when a row is selected. Once this page is opened in a new pop-up page, the variable is no longer updated after closing the pop-up.

### Solution

To avoid similar situations, we do not recommend opening a page more than once at a time as it is not yet supported.

## Issue: Unable to Start Orchestrator Process

When passing an `Array[string]` variable from a process to **UiPath Apps**, the following error message can occur:

`Unable to start orchestrator process - invalid response received from orchestrator:orchestrator-start-process with message: The field InputArguments must be a string or array type with a maximum length of '10000'. and errorCode 0`

### Possible Cause

This issue is related to a payload size limit from Orchestrator. The limit only applies in unattended mode.

### Solution

* You can reduce the data being sent to Orchestrator or break the process into smaller ones.
* You can run the process in attended mode.

## Issue: Entities Intermittently Display an Error

Referenced entities may intermittently display an error.

### Solution

If there are no other errors, refresh your app to fix the errors.