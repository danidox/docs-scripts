---
title: "Use arrays to populate Dropdown, Multiselect dropdown, and Radio Button controls"
visible: true
slug: "use-arrays-to-populate-dropdown-controls"
---

You can use arrays to populate the options of **Dropdown**, **Multiselect dropdown**, and **Radio Button** controls, by referencing them in the **List source** field of the control:

1. Select the control and go to **General** properties tab.
2. Open the expression editor for the **List source** field.
3. Write one of the following expressions:
   ```
   New List(Of String) From {"Value1", "Value2", "Value3"}.ToListSource()
   ```
   ```
   {"v1", "v2", "v3"}.ToListSource()
   ```