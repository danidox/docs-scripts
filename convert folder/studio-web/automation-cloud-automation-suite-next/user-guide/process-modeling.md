---
title: "Process modeling"
visible: true
slug: "process-modeling"
---

Agentic processes feature a dedicated designer where you can design and configure your long-running enterprise process in an industry-standard BPMN format.

Agentic processes feature interconnected elements (steps) which can be repositioned and deleted. Each element can be configured in the designer or in the **Properties** panel. Some elements act as events that control process executions, while others act as placeholders for other activities and workflows.

You can use connections ![](/images/studio-web/studio-web-image-529183.webp) to link elements in a way that is meaningful to your flow. You can also double-click on any element to rename it.

Use the marquee tool to select elements in the designer (click and drag) and the hand tool to navigate inside the canvas (**Space** key, then click and drag).

## The left toolbar

Every agentic process starts by default with a **Start Event**![](/images/studio-web/studio-web-image-529163.webp) element added to the designer. You can add other elements to your project from the left toolbar.

The left toolbar contains a wide range of BPMN elements, grouped under these categories:

* **Gateways**
* **Tasks**
* **Events**
* **Data**
* **Participants**

To model your agentic process, select an element in the left toolbar and drag it into the designer. You can start from the list of commonly-used elements, or select the **More options** button at the bottom of the toolbar to see the full list of supported BPMN elements.

You can also use Autopilot™ to create your business process model. To learn more, refer to [Autopilot™ for Maestro](https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/autopilot-for-maestro) in the Maestro user guide.

  ![Left toolbar](/images/studio-web/studio-web-left-toolbar-538359.webp)

## The element toolbar

The element toolbar is a horizontal menu that contains the actions that you can perform when selecting an element in the designer:

* **Change element** - Opens the **Change element** panel, where you can modify the selected element to a different element.
* **Add end event** - Appends an **End event** element to the selected element.
* **Add exclusive gateway** - Appends an **Exclusive gateway** element to the selected element.
* **Add task** - Appends a **Task** element to the selected element.
* **Add intermediate event** - Appends an **Intermediate event** element to the selected element.
* **Add text notation** - Appends a text annotation to the selected element.
* **Delete** - Deletes the selected element.
* **Connect** - Brings up the connector tool, with the selected element as the source step.

  ![Element toolbar](/images/studio-web/studio-web-element-toolbar-538367.webp)

The toolbar also appears when you select a connection, with the following options:

* **Add text notation** - Appends a text annotation to the selected connection.
* **Delete** - Deletes the selected connection.

## The validation panel

The validation panel is a rules engine that validates the agentic process with BPMN rules and best practices. You can access the validation panel from the bottom left of the designer. The panel shows the number of validation issues found in the process. Selecting a warning or error within the panel directs you to the affected element in the designer.

  ![Validation panel](/images/studio-web/studio-web-validation-panel-530184.webp)

## The menu options

Menu options can be found in the upper right of the designer. They contain the following options:

* **Import from file** - Imports a .bpmn file in the project and opens the BPMN model in the designer.
* **Download to file** - Exports the BPMN model currently displayed in the canvas as a .bpmn file.
* **Organize connections** - Automatically rearranges all connections in the designer to improve readability.
* **Show / hide validation errors** - Controls the visibility of validation errors.
* **Undo** - Reverts the action performed previously and displays the number of actions that can be undone.
* **Redo** - Repeats the action that was previously undone and displays the number of actions that can be redone.

  ![Menu options](/images/studio-web/studio-web-menu-options-530192.webp)

## The mini map

You can use the mini map in the bottom right of the designer to quickly navigate inside your agentic process. Dedicated buttons enable you to:

* **Zoom in** - Focus on a specific part of your process.
* **Zoom out** - Expand your view of the process.
* **Fit to view** - Automatically adjusts the size and position of the process.

  ![Mini map](/images/studio-web/studio-web-mini-map-541792.webp)

Inside the mini map, you can also click and drag to pan inside the process, and use the mouse wheel to zoom in and out.

## The context menu

The context menu appears when you right-click the designer or an element in the designer.

The following options are available when right-clicking the designer:

* **Organize connections** - Automatically rearranges all connections in the designer to improve readability.
* **Show / hide validation errors** - Controls the visibility of validation errors.

The following options are available when right-clicking an element:

* **Rename** - Renames the element.
* **Copy** - Copies the element.
* **Cut** - Removes the element from the designer and stores it in the clipboard.
* **Show properties panel** - Displays the properties of the element.
* **Remove** - Deletes the element from the designer.

The **Start Event** element contains these additional options:

* **Test** - Tests the entire agentic process.
* **Test step-by-step** - Tests each element in the agentic process one at a time.