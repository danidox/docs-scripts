---
title: "About Events and Rules"
visible: true
slug: "about-events-and-rules"
---

When you design your app, you may need to associate user interactions to specific app behaviors. For example, when X happens, do Y, where:

* X is called an **Event**.
* Y is called a **Rule**.

Here are a few examples:

* When the "Submit deposit" button is clicked, run an automation.
* When the value of the "Cash In" textbox changes, change the label color to red if the value is &lt; 0.
* When the help icon is clicked, open the browser to show a documentation page.
* When a tab button is clicked, change the page container to show a different page.

By specifying what rules to execute when an event occurs, your app becomes a dynamic and interactive console.

## Events

Events are triggers that happen when a user interacts with an app or control. Each control supports a single event:

| Event | Control(s) |
| --- | --- |
| Clicked On | Button, Header, Label, Icon, Image, etc |
| Value Changed | Checkbox, Date picker, Dropdown, Slider, Switch, Text Area, Textbox, List |
| Loaded | Page, Table |

## Rules

Rules define what actions your app takes when a certain event occurs. Below is a list of the rules that Apps provides:

| Rule | Description |
| --- | --- |
| [Set Value](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-set-values#rule%3A-set-value) | Sets the value of a property. |
| [Show Message](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-show-message#rule%3A-show-message) | Shows a message as a toast notification. |
| [Open a Page](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-open-page#rule%3A-open-a-page) | Opens a page of the app as a pop-over or as the contents of a page container. |
| [Close Pop-Over/Bottom Sheet](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-close-pop#rule%3A-close-pop-over%2Fbottom-sheet) | Closes the current Pop-Over. |
| [Open URL](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-open-url#rule%3A-open-url) | Opens a URL in the browser. |
| [Show/Hide Spinner](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-show-spinner#rule%3A-show%2Fhide-spinner) | Shows or hides a spinner overlay to show the app as busy. |
| [If-Then-Else](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-if-then-else#rule%3A-if-then-else) | Provides support for conditional statements in the rules builder. |
| [Reset Value](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-reset-values#rule%3A-reset-values) | Reverts a control to a default value, or clears it if a default value is not configured. |
| [Create Entity Record](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-create-entity-record#rule%3A-create-entity-record) | Creates a Data Service entity. |
| [Update Entity Record](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-create-entity-record#rule%3A-create-entity-record) | Updates a Data Service entity. |
| [Delete Entity Record](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-delete-entity-record#rule%3A-delete-entity-record) | Deletes an entity from Data Service. |
| [Start process](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-start-process#rule%3A-start-process) | Starts a process. |
| [Add to Queue](https://docs.uipath.com/apps/automation-suite/latest/user-guide/rule-add-to-queue#rule%3A-add-to-queue) | Adds an item to queue. |

### Reordering Rules

To reorder rules, click the "gripper" icon at the left side of the rule name and relocate the rule.

  ![docs image](/images/apps/apps-docs-image-290830-62252644.gif)