---
title: "Autopilot Recorder for UI
            Automation"
visible: true
slug: "ui-automation-autopilot-recorder"
---

Autopilot Recorder for UI Automation is an AI-powered tool which aims to significantly accelerate and simplify the process of scaffolding basic UI Automation sequences.

You can create UI Automation sequences using the Recorder both by generating activities via a natural language prompt and by manually adding them.

:::important
There is no support for adding loops of conditional logic. The Recorder can only handle a pre-defined list of basic UI Automation activities. Extract Data Table is not supported yet.
:::

Once you have created the desired sequence, simply select **Save**. The activities needed to perform the sequence are then populated in your Studio Web workflow canvas.

## Accessing the Recorder

To access the Autopilot Recorder for UI Automation, follow these steps:

1. Open an existing Studio Web project or create a new one.
2. In the workflow, add a **Use Browser** activity.
3. Under **Work in scope**, select a tab to automate from the drop-down menu.
4. Select the **Generate the UI automation activities using Autopilot** icon from the top right corner of the informative screenshot box or the **Generate** button. The **Generate** button is visible only when there are no activities inside the **Use Browser** activity.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/437285)
5. The Recorder is now open.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/435636)

:::note
If you [create a project from scratch with Autopilot](https://docs.uipath.com/studio-web/automation-cloud/latest/user-guide/creating-a-project#creating-a-project-with-autopilot%E2%84%A2) and the workflow requires a UI Automation sequence, the part of the text prompt pertaining to the UI Automation sequence is pre-loaded in the Recorder once you select **Generate** in the **Use Browser** activity. Therefore, when you access the Recorder in this context, it goes directly into generating the activities.
:::

## Generating activities via text prompt

To generate activities via text prompt in the Recorder, follow these steps:

1. Select the plus button.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/437314)
2. Proceed with either step a or b. Regardless of the choice, the outcome is the same.
   1. 1. Select the **Generate with Autopilot** option from the list. This creates a placeholder activity card.
      2. Write a text prompt in the **Describe your actions on this page** text field, then press the `Enter` key or select the arrow symbol. A prompt is most effective if it precisely describes the task at hand. This could include instructions such as "create a new supplier" or "create a time off request between 25 and 30 December", instead of a generic instruction like "click the 'new' button".
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/437339)
   2. Write a text prompt in the search box, then press the `Enter` key or select the **Generate with Autopilot** option.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/437343)
3. The activities are now generated from the prompt. The Recorder uses only the following UI Automation activities to generate sequences:
   * Click
   * Type Into
   * Get Text
   * Select Item
   * Check/Uncheck
4. The generated activities are populated in the Recorder. To transition to the next application state, select the **Test** button. The **Test** button is a one-click default-configured execution attempt with the sole purpose of helping you transition to the next application state so that you can continue scaffolding your automation.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/437352)
5. You have transitioned to the next application state. Executed activities are marked with a green checkmark. If, for some reason, the **Test** default-configured best-effort execution attempt fails, you can still interact with the application freely to manually execute the necessary steps. If the prompt is not covered in its entirety, select the **Continue 'prompt'** button.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/437356)
6. A new activity has been added in the Recorder. To transition to the next application state, select the **Test** button.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/437348)
7. You have transitioned to the next application state. You can use the **Continue 'prompt'** and **Test** alternatively until you reach the desired application state and the entire prompt is covered.
   ![docs image](https://docs-dev.uipath.com/api/binary/studio-web/2/627891/437360)

## Manually adding an activity

To manually add an activity in the Recorder, follow these steps:

1. Select the plus button.
2. Choose one of the following UI Automation activities from the list:
   * Click
   * Type Into
   * Get Text
   * Select Item
   * Check/Uncheck
   * Hover
   * Keyboard Shortcuts
   * Take Screenshot
   * Get Attribute
   * Mouse Scroll
   * Check Element
3. Indicate a target by selecting a UI element on the screen.
4. Indicate an anchor by selecting a nearby UI element that helps to uniquely identify the target.
5. Select **Confirm**.
6. The activity is now added in the Recorder.

## Actions you can take in the user interface

Explore the options available in the user interface as detailed in the following table.

<table cellpadding="4" cellspacing="0" class="table css-13i9z9m esqyda30" id="GUID-19CCFD15-9423-48B9-8194-AF0FE327149D__TABLE_TX4_XKM_WBC" summary="">
 <colgroup>
  <col/>
  <col/>
 </colgroup>
 <thead>
  <tr>
   <th>
    Options
   </th>
   <th>
    Description
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td headers="d5877e304">
    <strong>
     Generate
    </strong>
    button
   </td>
   <td headers="d5877e307">
    Opens the Recorder. You can also select the
    <strong>
     Generate the
                                    UI automation activities using Autopilot
    </strong>
    icon from the
                                 top right corner of the informative screenshot box.
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    Plus button
   </td>
   <td headers="d5877e307">
    Opens the search bar and the drop-down activity list.
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    Activity card
   </td>
   <td headers="d5877e307">
    You can perform the following:
    <ul>
     <li>
      Rearrange
                                       the activities in the Recorder by drag and dropping
                                       them.
     </li>
     <li>
      Access the selection screen by double clicking the
                                       activity card.
     </li>
     <li>
      Check the
                                       target and anchors of different activities without
                                       accessing the selection screen by simply selecting the
                                       activity card. This triggers a five-second highlight
                                       preview of the target and anchors.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    Activity card hamburger menu
   </td>
   <td headers="d5877e307">
    This contains the following options:
    <ul>
     <li>
      <strong>
       Properties
      </strong>
      - Opens the selection screen,
                                       where you can indicate the target and the anchor.
     </li>
     <li>
      <strong>
       Rename
      </strong>
      - Enables you to rename the activity. You can use up to
                                       100 characters.
     </li>
     <li>
      <strong>
       Delete
      </strong>
      - Deletes the activity card from the Recorder.
     </li>
    </ul>
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    <strong>
     Test
    </strong>
    button
   </td>
   <td headers="d5877e307">
    Executes all generated activities. This is a default
                                 configuration execution meant to help you to transition from one
                                 state of the application to another.
                                 Note: The
    <strong>
     Test
    </strong>
    button is not available in
                                    Safari.
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    <strong>
     Continue 'prompt'
    </strong>
    button
   </td>
   <td headers="d5877e307">
    Generates new activities in the Recorder to cover the entire
                                 prompt.
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    <code>
     Delete
    </code>
    key
   </td>
   <td headers="d5877e307">
    Deletes the selected activity card. Advanced user keyboard
                                 shortcut; no confirmation prompt is displayed.
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    <p>
     <strong>
      Generate with Autopilot
     </strong>
     trash bin button
    </p>
   </td>
   <td headers="d5877e307">
    Deletes the
    <strong>
     Generate with Autopilot
    </strong>
    placeholder
                                 activity card.
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    <code>
     Esc
    </code>
    key
   </td>
   <td headers="d5877e307">
    <p>
     Returns to the Studio Web canvas.
    </p>
    If you have made changes in the Recorder, a pop-up with the
    <strong>
     Save your changes made in the
                                       Selection Helper?
    </strong>
    message is displayed. You can
                                    select:
    <ul>
     <li>
      <strong>
       Cancel
      </strong>
      - Takes you back to the Recorder,
                                          where your changes are preserved.
     </li>
     <li>
      <strong>
       Don't Save
      </strong>
      - Takes you back to the Studio
                                          Web canvas without saving any changes.
     </li>
     <li>
      <strong>
       Save
      </strong>
      - Saves your changes and your UI
                                          Automation sequence is populated in the Studio Web
                                          canvas.
     </li>
    </ul>
    If the Properties panel is open, pressing
    <code>
     Esc
    </code>
    takes you back to the Activities view of the Recorder.
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    <strong>
     Cancel
    </strong>
    button
   </td>
   <td headers="d5877e307">
    Returns to the Studio Web canvas without saving any
                                 changes.
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    <strong>
     Save
    </strong>
    button
   </td>
   <td headers="d5877e307">
    Saves your workflow sequence and populates the activities in
                                 the Studio Web canvas.
   </td>
  </tr>
  <tr>
   <td headers="d5877e304">
    <strong>
     Help (F1)
    </strong>
    icon
   </td>
   <td headers="d5877e307">
    Opens the documentation page.
   </td>
  </tr>
 </tbody>
</table>

## Controlling Autopilot capabilities

Autopilot is enabled by default for all users.

You can disable Autopilot capabilities via Automation Ops governance policies in two ways:

* By adding a **Studio Web** policy and setting the **Allow Autopilot** option to **No**.
* By adding a **AI Trust Layer** policy and disabling the **Enable calls to third party AI models through AI Trust Layer** toggle button.

When either one of these options is disabled, you can still use the Autopilot Recorder for UI Automation, but you cannot generate activities via text prompts, you can just manually add activities in the Recorder.