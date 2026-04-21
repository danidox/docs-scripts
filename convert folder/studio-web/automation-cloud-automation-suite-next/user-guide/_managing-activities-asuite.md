---
title: "Managing the activities in a
         project"
visible: true
slug: "managing-activities"
---

## Renaming an activity

Every activity you add to a project has a default name. It is important to give your activities unique names that indicate what their purpose is and makes them easy to identify in your workflow.

To rename an activity, click the name displayed in the activity title bar or select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Rename**.

## Moving an activity

To move an activity inside your project, click and hold the activity icon displayed on left side of the activity title bar, then drag the activity and drop it in the desired location. Alternatively, you can cut the activity and then paste it somewhere else in your workflow.

## Cutting, copying, and pasting an activity

To cut or copy an activity, select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Cut** or **Copy**.

To insert the activity you copied or cut in another location, do one of the following:

* On the activity after which you want to insert it, select **Actions** ![docs image](/images/studio-web/studio-web-image-More_VT.png) &gt; **Paste**.
* Click the Add activity button where you want to insert the activity. An option to insert the activity is displayed at the top of the add activity window.

## Expanding or collapsing an activity

Collapsing activities helps save space on your project canvas, making it easier to navigate, especially in larger projects. You can keep activities expanded when you need to configure them, and then collapse them after you are done. As soon as you add a new activity, Studio Web automatically collapses the previous activity in the workflow.

To collapse / expand an activity, click anywhere in the empty space in the activity title bar, or select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Collapse** or **Expand**.

When working in container activities, you can collapse and expand the Body block by clicking the button on the right side.

## Adding an annotation to an activity

Annotations enhance projects by providing additional details about activities, aiding both yourself and collaborators in better understanding specific aspects when revisiting the project.

To add an annotation to an activity, select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Add annotation**, and then use the text box displayed under the title bar. After you add an annotation, you can edit it at any time. If you want to remove an annotation from an activity, select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Delete annotation**. Annotations are visible at the top of each activity. The annotation icon is displayed in the title bar of collapsed activities that contain an annotation.

## Disabling or enabling an activity

Disabling an activity lets you run your project without executing that activity, which can help you identify troubleshoot errors. For example, you may want to disable activities that aren't fully configured, activities with errors, or activities that do not behave as expected.

To disable an activity, select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Disable**. When an activity is disabled, it is placed inside a disabled activity container. You can still configure it, but, unless you enable it again, the activity won't be executed when you run the project. To re-enable an activity, select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Enable** on the disabled activity container.

## Extracting an activity as a new workflow

To break down large projects into smaller components, you can extract an activity or a sequence as a workflow. This creates a new workflow containing the targeted activity or sequence. An **Invoke Workflow File** activity is created in place of the extracted activity. Input and output variables used in the activity are automatically converted to **In** and **Out** arguments.

To extract an activity as a workflow, select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) **Extract as Workflow**. In the **New Workflow** window, type in the name of the workflow, choose the location where to store it inside the project, and select **Create**. If the extracted workflow has the same name as an existing workflow, the extracted workflow keeps the name of the existing workflow followed by an incremental number.

## Removing an activity

To remove an activity, select it and press the **Delete** key, or select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Delete**.

## Accessing the documentation for an activity

To open the activity documentation on the UiPath<sup>®</sup> documentation portal, select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Help** or press **F1** on your keyboard.

## Adding a breakpoint on an activity

A breakpoint purposely pauses the project execution on an activity which may cause execution issues. When you run the project, execution pauses before that activity runs which can help you identify and fix issues in your projects.

To add a breakpoint to an activity, select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Add breakpoint**.

When a breakpoint is set on an activity, the icon ![](/images/studio-web/studio-web-image-breakpoint.png) is displayed to the left of the activity's title bar.

To remove a breakpoint from an activity, select **Actions** ![](/images/studio-web/studio-web-image-More_VT.png) &gt; **Remove breakpoint**.

## Identifying errors in an activity

If an activity has an incomplete or invalid configuration, the ![](/images/studio-web/studio-web-image-error_icon.png) icon is displayed on the right side of each property with errors, and the property name and outline are colored in red. An error icon is also displayed on the right side of the title bar of the activity and of all of its parent activities.

Hover over the error icons to view more information about the cause of the error and possible solutions.

You can also see the errors or warnings in a project by accessing the **Issues Panel** from the ![](/images/studio-web/studio-web-image-547990.webp) icon on the upper-left side of the page. The number of identified issues is displayed next to the icon.

Opening the Issues Panel shows you the list of identified errors or warnings. After selecting an error or warning, you can use the **Go to source** button to jump to the activity that has the incomplete or invalid configuration.