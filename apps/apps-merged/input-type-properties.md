---
title: "Input and Output Type Properties"
visible: true
slug: "input-type-properties"
---

You can use **Input/Output** arguments in UiPath Apps.

A process of type **Input/Output** is treated as a single property. No separate input and output versions are created for the same property. For this, a third category of properties called Input/Output is used.

![docs image](/images/apps/apps-docs-image-293177-89175a62.webp)

When a control is bound to a In/Out property, the same control works as input and as output. This means that while a process is running, the control value goes as input to the process, and once the process is completed, the same control is refreshed with the output value.

## Importing Apps

When importing an app from the cloud environment to an on-premises environment, which does not support **In/Out** properties, the following applies:

* The entire Input/Output section disappears.
* Bindings referring to properties from the Input/Output section are displayed as invalid.
* After replacing the process, the In/Out properties are added to both sections. You can now update the invalid bindings to point to the new properties.
  :::note
  Importing an app from cloud to Automation Suite is only supported for backwards compatibility, meaning you need to export on cloud before the Automation Suite version is released.
  :::