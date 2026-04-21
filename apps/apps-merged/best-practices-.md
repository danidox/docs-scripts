---
title: "Best practices"
visible: true
slug: "best-practices-"
---

To build a high-performing app using VB expressions, consider the following recommendations and guidelines:

## Naming conventions

1. VB elements must respect the following naming conventions:
   1. It must begin with an alphabetic character or an underscore.
   2. It must only contain alphanumeric characters, and underscores.
   3. If it begins with an underscore, then it must contain at least one alphanumeric character.
   4. It must not be a reserved keyword.
   5. Name length is limited to 128 characters.
2. Apps controls and pages must respect the following naming conventions:
   1. Controls and pages cannot have same name
   2. Pages cannot have the default name of controls (for example: button, label)
      :::note
      Icons are identified as controls. Pages cannot have the default name of an icon.
      :::
   3. Page names must be unique in an app.
      :::note
      Page names are case insensitive, therefore "MainPage" and "mainPAGE" are considered duplicates.
      :::
   4. Control names must be unique within the page.
   5. Both control and page names must respect the naming conventions for a valid VB name.
3. Apps variables must respect the following naming conventions:
   1. It cannot have the same name as a control or a page
   2. It cannot have the default name of controls (for example: "button", "label")
   3. It must be unique in an app.
   4. It must respect the naming conventions for a valid VB name.

For more details, check this [link](https://learn.microsoft.com/en-us/office/vba/language/concepts/getting-started/visual-basic-naming-rules).