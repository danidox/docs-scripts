---
title: "Tabs"
visible: true
slug: "tabs"
---

## General

The tab control lets you divide the information in your app by tabs. The behavior of the tab control differs depending on the selected mode: **Static** or **Dynamic**.

### Static tabs

When you add the **Tab** control, it displays three tabs by default (**Tab 1**, **Tab 2**, **Tab 3**). Expanding each tab within the control exposes the following properties:

* **Tab name**—The display name of the tab.
* **Page** —The Apps page to import within this tab.
* **Hidden**- If true, hides the control at runtime.
* **Disabled** - If true, disables the control at runtime.

The following properties apply to the entire **Tab** control.

* **Add new tab—**Add new tab to your data by clicking the plus "+" icon.
* **Active tab index**—Navigate to a specific tab using this property. The index starts at 0. For example, if you have four consecutive tabs named "Tab1", "Tab2", "Tab3", and "Tab4", then "Tab1" has the index `0`, "Tab2" has the index `1`, "Tab3" has the index `2`, and "Tab4" has the index `3`.
* **Hidden**—If true, hides the control at runtime.
* **Disabled**—If true, disables the control at runtime.

### Dynamic tabs

Dynamic tabs are generated at runtime from a list data source. To use this feature, select the **Dynamic** mode for your tabs. This is useful when the number of tabs you need varies and depends on the items in a list.

You can configure the following properties:

* **List source**—The source for the items to be displayed as tabs. Valid data types include arrays of String, Integer, or DateTime, DataTable, or arrays of an Object.
* **Column**—When the list source is either of type DataTable or an array of an Object, select the specific column (for DataTable data types) or the specific property (for Object arrays).
* **Page source**—The App page to use across all dynamic tabs.
* **Active tab index**—Navigate to a specific tab using this property. The index starts at 0. For example, if you have four consecutive tabs named "Tab1", "Tab2", "Tab3", and "Tab4", then "Tab1" has the index `0`, "Tab2" has the index `1`, "Tab3" has the index `2`, and "Tab4" has the index `3`.

For example, you can use dynamic tabs with Data Service entities, as follows:

* The **List source** property for the dynamic tabs is an entity in Data Service, for example, "Department":
  ```
  Fetch(of TPDepartment)(Nothing, Nothing, Nothing, Nothing, New ExpansionFieldOption(){addExpansionFieldOption("CreatedBy", New String(){"Id","Name"}), addExpansionFieldOption("UpdatedBy", New String(){"Id","Name"})})
  ```
* The **Column** property for the dynamic tabs is a field of the selected Data Service entity, for example "Name".
  :::note
  At runtime, you see as many tabs as the number of records in the selected entity field. The control is limited to displaying 50 records of your entity. If you have more than 50 records, the first 50 are displayed.
  :::
* For **Page source**, you can set up a page to display a table that updates based on the selected tab.

At runtime, the tabs you see are the records in the Name field of the Department entity. Switching tabs updates the content in the table.

  ![docs image](/images/studio-web/studio-web-docs-image-590311.webp)

## Events

* **Value changed**—Configure what happens when the value is changed.

## Style

* **Control Alignment**—By default, it is set to **Stretch**. A different alignment can be set.
  :::note
  The alignment is dependent on the layout selected for the parent (**Vertical** vs **Horizontal**).
  :::
* **Style**—The style of active and inactive tabs:
  + **Default**—Tabs are styled as classic browser tabs.
  + **Pills**—Tabs are rounded on both ends, resembling a pill shape.
  + **Tab color**—The text color for inactive tabs.
  + **Active tab color**—The text color for active tabs.
  + **Tab background**—The background color for inactive pill tabs.
  + **Active tab background**—The background color for active pill tabs.
  + **Large tabs**—If selected, tabs are enlarged.
* **Border**—The border for the control. You can configure border **Thickness**, **Color**, and **Radius**.
* **Font**—The font attributes for the tab text, such as font family, size, or color. By default, the control inherits the font family of the immediate parent container which is indicated by the keyword "Inherited".
* **Margin**—The margin of the control. By default, a margin of 4px is set. **Top/Bottom** and **Left/Right** margin properties are combined. To set different, separate values for **Top**, **Bottom**, **Left**, and **Right** margins, select the **Link** button at the right-hand side of the **Margin** section.
* **Size**—The **Width** and **Height** of the control. By default, the size is set to `auto`. To set minimum or maximum values, select the three dots (...). If the size of the control is smaller than the options, a scroll bar is displayed.

## VB properties

| VB property | Data type | Description |
| --- | --- | --- |
| `ActiveTabIndex` | Integer | Index of the currently active tab. |
| `ActiveTabName` | String | Name of the currently active tab. |
| `Hidden` | Boolean | If true, hides the control at runtime. |
| `Disabled` | Boolean | If true, disables the control at runtime. |
| `SelectedItem` | `Apps.Controls.TabularInitClass` | The currently selected tab in the **Tabs** control. |

:::important
For **Static** mode, `SelectedItem` and `ActiveTabName` are the same. For **Dynamic** mode:
* If the data source uses primitive types, `SelectedItem` and `ActiveTabName` are the same.
* If the data source is a data table or a list of objects, `SelectedItem` contains the full selected record. `ActiveTabName` shows only the name visible on the tab.
:::

## Keyboard Shortcuts

For improved accessibility, you can use the following keyboard shortcuts in the tabs list from the **General** tab in the configuration panel:

* **Up** and **Down** arrow keys to change the selected tab.
* **Alt**+**Up** arrow key to move the selected tab up.
* **Alt**+**Down** arrow key to move the selected tab down.