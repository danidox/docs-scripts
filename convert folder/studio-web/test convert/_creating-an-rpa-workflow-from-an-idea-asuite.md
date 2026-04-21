---
title: "Creating an RPA workflow from an
         idea"
visible: true
slug: "creating-an-rpa-workflow-from-an-idea"
---

An RPA workflow consists of a sequence of related, interconnected activities. An activity is the basic building block of an automation, representing a step or a task in a workflow that you can automate.

To create an RPA workflow:

1. Break down the idea you want to automate into each of its individual steps, decide what should trigger the automation, and identify all the apps and services you use in it.
2. Create a project in Studio Web.
3. Identify the activities that enable you to automate each of the steps, add them to your project and configure them in the project designer.
4. Test your project. It may not run successfully from the first try and you may need to make adjustments and run it a few times before you get it to work as you want it to.
5. Publish your project to make it available as an automation. If it uses an event trigger or a time trigger, the automation will run automatically.

## Example of creating an RPA workflow

An idea can be as simple as "I want every canceled event to be automatically removed from my Outlook calendar".

Breaking down the process and how we can automate it, we want to:

* Automate the Outlook calendar, so we will use Microsoft Office 365 activities.
* Run the automation whenever a calendar event is updated, so the automation will be triggered by the **Calendar Event Updated** event.
* Remove an event only if it was canceled, so we will add a condition to only process the event if it has been canceled using an **If** activity. and then add a **Delete Event** activity to remove it from our calendar if the condition is met.

#### Build the RPA workflow

1. [Go to the Automations](https://studio.uipath.com/projects) page in Studio Web and create a new project. For the trigger, select the Microsoft 365 event [Calendar Event Updated](https://docs.uipath.com/activities/other/latest/user-guide/office365-trigger-event-updated). The trigger activity is added to the project.
2. In the **Calendar Event Updated** activity, add or select a connection.
3. Click **Add activity** ![docs image](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/StudioWeb/plus-add-activity.png) after the trigger and add an **If** activity. This activity enables you to define a condition, then add activities to execute when the condition is met inside the **Then** branch, and optionally activities to execute when the condition is not met in the **Else** branch. For our scenario, we need the condition *the event is canceled* and we will only use the **Then** branch to add an activity to delete the event when the condition is met.
4. In the **If** activity, click the **Condition** field to open the **Condition builder**:
   1. In the first field, we want to find the **IsCancelled** event property for the event that triggered the automation. We can search for the text *cancel*, or select **See more** ![docs image](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/StudioWeb/see-more.png) &gt; **Use variable** &gt; **Calendar Event Updated** &gt; **Event** &gt; **IsCancelled**.
   2. In the second field, select **is true**.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/279848)
5. Click **Add activity** ![docs image](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/StudioWeb/plus-add-activity.png) in the **Then** box and add a Microsoft 365 [Delete Event](https://docs.uipath.com/activities/other/latest/user-guide/office365-calendar-delete-event-connections) activity. We will configure it to delete the event that triggered the automation.
   1. Add or select a connection.
   2. **Event to delete** - Click and select **Calendar Event Updated** &gt; **Event** to indicate that you want to delete the event. Because this activity is added inside the Then branch, the event will be deleted only if it was canceled.
   3. **Delete** - Select **Single event only** to only delete the occurrence, if the event is recurring.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627900/279856)

#### Debug the RPA workflow

To debug the automation, make sure a recently canceled event exists in your Outlook calendar. You can select **Test trigger** in the trigger activity to check whether you have at least one event that was recently updated.

Click **Debug on cloud** at the top of the designer to test the automation, and check you calendar to see if the canceled event has been removed.

#### Publish the RPA workflow

If the automation works as expected, all you need to do in order for it to run is to publish it to your personal workspace. Click **Publish** at the top of the designer, enter a suggestive name and description, and click **Publish**.