---
title: "Managing project files and folders"
visible: true
slug: "managing-project-files-and-folders"
---

A project can contain multiple workflows which you can organize in folders.

By default, a project consists of a single workflow file named **Main.xaml** that contains the sequence of activities used in your automation. When you create complex automations, it is a good practice to break projects into multiple smaller workflows that are easier to organize and navigate, and which can be tested individually. To determine the order in which the workflows run, you link them by adding [Invoke Workflow File](https://docs.uipath.com/activities/other/latest/workflow/invoke-workflow-file) activities in the main workflow to call each workflow when it's needed.

You can also link a workflow file to another workflow by:

* Dragging the workflow from the **Project explorer** and dropping it inside the main workflow. This action creates an Invoke Workflow File activity that references the invoked workflow.
* Right-clicking the workflow in the **Project explorer** and selecting the **Invoke in current workflow** menu option. This action creates an Invoke Workflow File activity and adds it at the bottom of the main workflow.

For example, in a project where you use UI automation to process data in an online application, you can create two separate files for the sign-in steps and the data processing, and use the main workflow to add the trigger and call the two files using two Invoke Workflow File activities, invoking the sign-in workflow first.

You manage the project files from the **Project explorer**. If a project was edited in Studio Desktop, it may contain additional files and folders.

To open the Project explorer, select ![](https://documentationpicturerepo.blob.core.windows.net/screenshots/screenshots/StudioWeb/project-explorer.png) on the upper-left side of the designer. This is where you can:

* Rename the project by right-clicking it and selecting **Rename**.
* Open a workflow in the designer by selecting it.
* Add a workflow or a folder using the two buttons on the upper-left side of the panel. File and folder names can't start with the character `.` or contain the following special characters: `' ", < > | : * ? \ / ; % =`.
* Move files and folders by dragging and dropping them in the desired location.
* Rename or delete a file or folder by right-clicking it and selecting either **Rename** or **Delete**. You can't delete the main workflow.
* Duplicate a workflow file by right-clicking it and selecting **Duplicate**. The name of the new workflow is the name of the workflow you duplicated followed by 1. The duplicated workflow contains the same configured activities as the original workflow.
  :::note
  Currently, you can only duplicate workflow files, not other files and folders.
  :::
* Debug your entire workflow or test each activity at a time (debug step-by-step).
* Invoke the selected workflow into the current workflow.

## Managing files in projects edited with Studio Desktop

Projects that were edited in Studio Desktop may contain different types of files that can't be opened or edited in Studio Web. Please note the following:

* You can only edit sequences in Studio Web. Flowcharts, state machines, and test cases are not supported in Studio Web.
* Projects that contain flowchart workflows cannot be opened in Studio Web.
* Projects with multiple entry points can be opened in Studio Web, but not edited. Files that are set as entry points are highlighted in the Project explorer by a green arrow displayed on the icon and a text displayed when hovering the icon.
* If you create a project with multiple files in Studio Web, you can only edit the main workflow when you open it in the StudioX profile.
* You can only change which workflow is set as main from Studio Desktop. The name of the main workflow file is displayed in bold in the Project explorer.

## Test cases

You can perform automation testing in Studio Web by creating and using test cases. A test case is a specialized `.xaml` file that integrates testing into RPA workflow projects. Test cases define the actions, scenarios, data, and expected results needed to verify and validate the functionality of your automations.

Testing functionalities in Studio Web rely on the [Testing activity package](https://docs.uipath.com/activities/other/latest/workflow/about-the-testing-activities-pack).

To create a test case:

1. Open an RPA workflow project.
2. Open the **Project Explorer**.
3. Right-click the project and select **Add to project** &gt; **Test case**.

You can rename, delete, and debug a test case, as well as add activities in the same way you do in RPA workflows.

Publishing an RPA workflow project also publishes all test cases within that project. Published test cases can then be managed in [Test Manager](https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/managing-test-cases).